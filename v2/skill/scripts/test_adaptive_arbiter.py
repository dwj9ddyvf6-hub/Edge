"""Synthetic contract tests; not economic validation or execution simulations."""

from dataclasses import FrozenInstanceError, replace
import unittest

from adaptive_arbiter import (
    ActionRule, Candidate, Constraint, Distribution, Incumbent, InputRequirement,
    LoadAlternative, Observation, OutstandingOrder, Policy, ScenarioLoads,
    UtilityVector, robust_score, select,
)


SCENARIOS = ("joint_selloff", "joint_rally")
UTILITY_UNIT = "USD certainty-equivalent per one-day decision horizon"
NOW = 100


def loads(selloff=20.0, rally=20.0):
    return ScenarioLoads(SCENARIOS, ("signed_exposure",), ("USD",), ((selloff,), (rally,)))


def policy(hurdle=1.0):
    return Policy(
        version="research-policy-v1", scenarios=SCENARIOS,
        distributions=(Distribution("down_weighted", SCENARIOS, (0.75, 0.25)),
                       Distribution("up_weighted", SCENARIOS, (0.25, 0.75))),
        utility_unit=UTILITY_UNIT, hurdle=hurdle,
        constraints=(Constraint("signed_exposure", "USD", -100, 100),),
        action_menu=(ActionRule("alpha", (InputRequirement("quote", 5),)),
                     ActionRule("beta", (InputRequirement("quote", 20),
                                         InputRequirement("borrow", 10)))),
    )


def incumbent(**changes):
    base = Incumbent("held-policy", "hold-v4", True, NOW, loads())
    return replace(base, **changes)


def candidate(action_id="alpha", delta=(4.0, 8.0), *, held=None, after=None, **changes):
    held = held or incumbent()
    base = Candidate(
        action_id=action_id, decision_policy_version="research-policy-v1",
        incumbent_policy_id=held.policy_id, incumbent_policy_version=held.policy_version,
        incremental_utility=UtilityVector(SCENARIOS, UTILITY_UNIT, delta),
        post_action_position_loads=(LoadAlternative("no_new_fill", held.position_loads),
                                    LoadAlternative("full_fill", after or loads(40, 40))),
        observations=(Observation("quote", NOW, True), Observation("borrow", NOW, True)),
        eligible=True, evidence_passed=True, evidence_reference="synthetic-approved-evidence-v1",
        decision_deadline=NOW + 10,
    )
    return replace(base, **changes)


def choose(candidates, *, p=None, held=None, now=NOW, deadline=NOW + 20):
    return select(p or policy(), held or incumbent(), tuple(candidates),
                  now=now, decision_deadline=deadline)


def order(order_id, fill):
    return OutstandingOrder(order_id, (LoadAlternative("none", loads(0, 0)),
                                       LoadAlternative("full", fill)))


class ArbiterTests(unittest.TestCase):
    def test_01_paired_robust_delta_not_difference_of_robust_levels(self):
        # Separate minima use different worst distributions and would promote
        # this candidate; the correctly paired robust incremental score refuses.
        incumbent_values = (0.0, 100.0)
        action_values = (30.0, 30.0)
        delta = tuple(action - baseline for action, baseline in zip(action_values, incumbent_values))
        p = policy(hurdle=1)
        paired, worst = robust_score(p, UtilityVector(SCENARIOS, UTILITY_UNIT, delta))
        incorrect = min(sum(a * q for a, q in zip(action_values, d.probabilities))
                        for d in p.distributions) - min(
                            sum(b * q for b, q in zip(incumbent_values, d.probabilities))
                            for d in p.distributions)
        self.assertEqual(paired, -45.0)
        self.assertEqual(incorrect, 5.0)
        self.assertEqual(worst, "up_weighted")
        self.assertEqual(choose([candidate(delta=delta)], p=p).status, "no_new_order")

    def test_02_strict_hurdle_and_no_double_cost_penalty(self):
        # Values are net of all costs; no second penalty is subtracted here.
        equal = choose([candidate(delta=(1, 1))])
        self.assertEqual(equal.status, "no_new_order")
        clears = choose([candidate(delta=(1.00001, 1.00001))])
        self.assertEqual(clears.selected_action_id, "alpha")
        self.assertEqual(clears.selected_score, 1.00001)

    def test_03_largest_score_then_lexical_tie_and_duplicate_decision(self):
        a = candidate("alpha", (4, 8))
        b = candidate("beta", (4, 8))
        first = choose([b, a])
        self.assertEqual(first, choose([b, a]))
        self.assertEqual(first, choose([a, b]))
        self.assertEqual(first.selected_action_id, "alpha")
        self.assertEqual(choose([a, candidate("beta", (9, 9))]).selected_action_id, "beta")

    def test_04_action_specific_freshness_missing_invalid_and_future_data(self):
        old = (Observation("quote", 90, True), Observation("borrow", 95, True))
        outcome = choose([candidate("alpha", observations=old), candidate("beta", observations=old)])
        self.assertEqual(outcome.selected_action_id, "beta")
        self.assertIn("stale_or_future_input:quote", outcome.candidate_audits[0].reasons)
        variants = (((), "missing_input:quote"),
                    ((Observation("quote", NOW, False),), "invalid_input:quote"),
                    ((Observation("quote", NOW + 1, True),), "stale_or_future_input:quote"))
        for observations, reason in variants:
            with self.subTest(reason=reason):
                result = choose([candidate(observations=observations)])
                self.assertEqual(result.status, "no_new_order")
                self.assertIn(reason, result.candidate_audits[0].reasons)

    def test_05_candidate_and_global_deadlines_expire_at_equality(self):
        result = choose([candidate(decision_deadline=NOW)])
        self.assertIn("candidate_deadline_expired", result.candidate_audits[0].reasons)
        result = choose([candidate()], deadline=NOW)
        self.assertEqual(result.status, "no_new_order")
        self.assertIn("decision_deadline_expired", result.reasons)
        result = choose([candidate(decision_deadline=NOW + 1)], deadline=NOW + 1000)
        self.assertEqual(result.status, "selected")
        self.assertEqual(result.decision_deadline, NOW + 1)

    def test_06_evidence_eligibility_and_preapproved_action_menu(self):
        for changes, reason in (({"eligible": False}, "eligibility_gate_failed"),
                                ({"evidence_passed": False}, "evidence_gate_failed"),
                                ({"action_id": "unapproved"}, "action_not_preapproved")):
            with self.subTest(reason=reason):
                result = choose([candidate(**changes)])
                self.assertEqual(result.status, "no_new_order")
                self.assertIn(reason, result.candidate_audits[0].reasons)

    def test_07_unknown_stale_or_future_own_state_requires_remediation(self):
        for changes in ({"own_state_known": False}, {"state_observed_at": NOW - 6},
                        {"state_observed_at": NOW + 1}):
            with self.subTest(changes=changes):
                result = choose([candidate(delta=(1000, 1000))], held=incumbent(**changes))
                self.assertEqual(result.status, "remediation_needed")
                self.assertIsNone(result.selected_action_id)
                self.assertIn("alpha_promotion_forbidden", result.reasons)

    def test_08_infeasible_incumbent_forbids_even_reducing_alpha_action(self):
        held = incumbent(position_loads=loads(120, 120))
        action = candidate(held=held, after=loads(0, 0), delta=(100, 100))
        result = choose([action], held=held)
        self.assertEqual(result.status, "remediation_needed")
        self.assertEqual(result.incumbent_breach.load, 120)
        self.assertIsNone(result.selected_action_id)

    def test_09_opposing_outstanding_orders_cannot_be_blindly_netted(self):
        held = incumbent(position_loads=loads(80, 80),
                         outstanding_orders=(order("buy", loads(30, 30)),
                                             order("sell", loads(-30, -30))))
        # Both-full net is zero; buy-only reaches 110 and is reserved anyway.
        result = choose([], held=held)
        self.assertEqual(result.status, "remediation_needed")
        self.assertEqual(result.incumbent_breach.load, 110)
        self.assertEqual(result.incumbent_breach.outstanding_fills,
                         (("buy", "full"), ("sell", "none")))

    def test_10_candidate_reserves_all_simultaneous_outstanding_fills(self):
        held = incumbent(outstanding_orders=(order("buy-a", loads(25, 25)),
                                             order("buy-b", loads(25, 25))))
        result = choose([candidate(held=held, after=loads(60, 60))], held=held)
        self.assertEqual(result.status, "no_new_order")
        self.assertEqual(result.candidate_audits[0].breach.load, 110)
        self.assertEqual(len(result.candidate_audits[0].breach.outstanding_fills), 2)

    def test_11_correlated_portfolio_scenario_loads_include_existing_positions(self):
        # Existing and new positions lose together in the selloff. Their total
        # stressed loss 70+45 breaches 100 although each alone appears feasible.
        p = replace(policy(), constraints=(Constraint("joint_stress_loss", "USD", -100, 100),))

        def stress(down, up):
            return ScenarioLoads(SCENARIOS, ("joint_stress_loss",), ("USD",), ((down,), (up,)))

        held = incumbent(position_loads=stress(70, -20))
        result = choose([candidate(held=held, after=stress(115, -35))], p=p, held=held)
        self.assertEqual(result.status, "no_new_order")
        self.assertEqual(result.candidate_audits[0].breach.scenario, "joint_selloff")
        self.assertEqual(result.candidate_audits[0].breach.load, 115)

    def test_12_signed_short_exposure_lower_bound_is_enforced(self):
        result = choose([candidate(after=loads(-101, -101))])
        self.assertEqual(result.status, "no_new_order")
        self.assertEqual(result.candidate_audits[0].breach.load, -101)
        self.assertEqual(choose([candidate(after=loads(-100, -100))]).status, "selected")

    def test_13_hold_retains_nonzero_incumbent_and_empty_menu_is_valid(self):
        held = incumbent(position_loads=loads(70, -20))
        result = choose([], held=held, p=replace(policy(), action_menu=()))
        self.assertEqual(result.status, "no_new_order")
        self.assertEqual(result.incumbent_policy_id, held.policy_id)
        self.assertIn("retain_incumbent_policy", result.reasons)
        self.assertEqual(held.position_loads.values, ((70,), (-20,)))

    def test_14_malformed_probabilities_are_rejected(self):
        for probabilities in ((-0.1, 1.1), (float("nan"), 0), (float("inf"), 0),
                              (0.4, 0.4), (True, 0), (1.0,), [0.5, 0.5]):
            with self.subTest(probabilities=probabilities), self.assertRaises(ValueError):
                Distribution("bad", SCENARIOS, probabilities)
        with self.assertRaises(ValueError):
            replace(policy(), distributions=(Distribution("wrong", SCENARIOS[::-1], (0.5, 0.5)),))

    def test_15_utility_and_load_scenario_unit_alignment_is_strict(self):
        malformed = (replace(candidate(), incremental_utility=UtilityVector(SCENARIOS[::-1], UTILITY_UNIT, (4, 8))),
                     replace(candidate(), incremental_utility=UtilityVector(SCENARIOS, "bps", (4, 8))),
                     replace(candidate(), post_action_position_loads=(
                         LoadAlternative("none", loads()),
                         LoadAlternative("bad", ScenarioLoads(SCENARIOS, ("signed_exposure",),
                                                               ("shares",), ((40,), (40,)))))))
        for action in malformed:
            with self.subTest(action=action), self.assertRaises(ValueError):
                choose([action])

    def test_16_nan_shapes_mutability_and_duplicate_ids_are_rejected(self):
        constructors = (lambda: UtilityVector(SCENARIOS, UTILITY_UNIT, (float("nan"), 1)),
                        lambda: UtilityVector(SCENARIOS, UTILITY_UNIT, (10**400, 1)),
                        lambda: UtilityVector(SCENARIOS, UTILITY_UNIT, [1, 2]),
                        lambda: loads(float("inf"), 0),
                        lambda: ScenarioLoads(SCENARIOS, ("x",), ("USD",), ((1, 2), (3,))),
                        lambda: replace(policy(), hurdle=float("nan")),
                        lambda: choose([candidate(), candidate()]),
                        lambda: choose([candidate()], held=incumbent(own_state_known=False),
                                       p=replace(policy(), utility_unit="mismatched")))
        for constructor in constructors:
            with self.subTest(constructor=constructor), self.assertRaises(ValueError):
                constructor()

    def test_17_policy_is_frozen_and_candidates_must_pair_same_baseline_version(self):
        p = policy()
        with self.assertRaises(FrozenInstanceError):
            p.hurdle = 0
        for changes in ({"decision_policy_version": "changed"},
                        {"incumbent_policy_id": "flat-instead"},
                        {"incumbent_policy_version": "hold-v3"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                choose([candidate(**changes)])

    def test_18_all_candidate_fill_outcomes_are_reserved(self):
        action = candidate(post_action_position_loads=(LoadAlternative("none", loads()),
                                                       LoadAlternative("partial", loads(110, 50)),
                                                       LoadAlternative("full", loads(40, 40))))
        result = choose([action])
        self.assertEqual(result.status, "no_new_order")
        self.assertEqual(result.candidate_audits[0].breach.position_alternative, "partial")
        with self.assertRaises(ValueError):
            choose([candidate(post_action_position_loads=(LoadAlternative("full", loads(40, 40)),))])

    def test_19_zero_fill_required_and_combinatorial_cap_fails_closed(self):
        with self.assertRaises(ValueError):
            OutstandingOrder("bad", (LoadAlternative("full", loads(30, 30)),))
        held = incumbent(outstanding_orders=(order("one", loads(5, 5)), order("two", loads(5, 5))))
        with self.assertRaises(ValueError):
            choose([], held=held, p=replace(policy(), max_reservation_combinations=3))

    def test_20_multiple_named_constraint_units_and_finite_addition(self):
        constraints = (Constraint("signed_exposure", "USD", -100, 100),
                       Constraint("gross_shares", "shares", 0, 50))
        p = replace(policy(), constraints=constraints)
        base = ScenarioLoads(SCENARIOS, ("signed_exposure", "gross_shares"), ("USD", "shares"),
                             ((20, 20), (20, 20)))
        after = replace(base, values=((10, 60), (10, 60)))
        held = incumbent(position_loads=base)
        result = choose([candidate(held=held, after=after)], p=p, held=held)
        self.assertEqual(result.candidate_audits[0].breach.constraint, "gross_shares")
        self.assertEqual(result.candidate_audits[0].breach.unit, "shares")
        huge = replace(policy(), constraints=(Constraint("signed_exposure", "USD", -1e308, 1e308),))
        held = incumbent(position_loads=loads(1e308, 1e308),
                         outstanding_orders=(order("huge", loads(1e308, 1e308)),))
        with self.assertRaises(ValueError):
            choose([], held=held, p=huge)


if __name__ == "__main__":
    unittest.main()
