"""Finite, offline decision-selection reference; Python 3.10+, no dependencies.

Call ``select(policy, incumbent, candidates, now=..., decision_deadline=...)``.
All timestamps are integer UTC epoch seconds, and callers supply the clock.
Inputs and results are frozen dataclasses containing tuples, not mutable lists.

Each candidate supplies *incremental portfolio utility against the same feasible
incumbent policy*, in the policy's named unit and common ordered scenarios.
Execution, holding, impact, financing, and risk costs must already be included.
The only score is ``min_p sum_s p[s] * delta_utility[s]``. No additional cost
penalty is applied. A candidate must strictly exceed the common hurdle; among
qualifiers the greatest score wins, with action ID breaking exact ties.

Constraint tables have named units and two-sided bounds. Candidate position
tables are TOTAL post-action position loads, including existing positions but
excluding outstanding orders. Supply every plausible candidate fill outcome,
including unchanged positions. Each outstanding order independently reserves
every supplied fill alternative, including zero fill. Every Cartesian product
of outstanding fills is added to each position table in every common scenario.
This deliberately cannot assume cancellation, OCO, or opposite orders will net.
Only additive scenario loads are supported: nonlinear metrics must be converted
to validated conservative additive reservations outside this prototype. Common
stress scenarios preserve portfolio correlation; stand-alone risk totals do not.

Unknown/stale own state or an infeasible reserved incumbent returns
``remediation_needed`` and forbids alpha promotion. It never sends an order or
blindly flattens. Risk-reducing actions require a separate approved contingency
controller with its own observability, execution, and post-action checks.
``no_new_order`` retains the incumbent policy, which may hold nonzero positions.

This is a finite calculation, not full robust control, off-policy
evaluation, model identification, a market simulator, or evidence that any edge
exists. It cannot establish that supplied scenarios/fills are exhaustive,
utility estimates are true, or an action is executable. There is no network,
broker, learning, randomization, mutable state, or live-order path.

Run the synthetic tests: ``python -m unittest discover -s . -p test_adaptive_arbiter.py -v`` from this folder.
"""

from dataclasses import dataclass
from itertools import product
from math import fsum, isfinite
from typing import Optional


def _text(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")


def _tuple(value: tuple, name: str, *, allow_empty: bool = False) -> None:
    if not isinstance(value, tuple) or (not allow_empty and not value):
        raise ValueError(f"{name} must be an immutable {'possibly empty ' if allow_empty else 'nonempty '}tuple")


def _names(values: tuple[str, ...], name: str) -> None:
    _tuple(values, name)
    for value in values:
        _text(value, name)
    if len(set(values)) != len(values):
        raise ValueError(f"duplicate {name}")


def _number(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        finite = isfinite(value)
    except OverflowError as error:
        raise ValueError(f"{name} exceeds the supported numeric range") from error
    if not finite:
        raise ValueError(f"{name} must be a finite number")


def _integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def _boolean(value: bool, name: str) -> None:
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be bool")


def _typed_tuple(values: tuple, cls: type, name: str, *, allow_empty: bool = False) -> None:
    _tuple(values, name, allow_empty=allow_empty)
    if any(not isinstance(value, cls) for value in values):
        raise ValueError(f"{name} must contain {cls.__name__}")


def _unique_ids(values: tuple, attribute: str, name: str) -> None:
    identifiers = tuple(getattr(value, attribute) for value in values)
    if len(set(identifiers)) != len(identifiers):
        raise ValueError(f"duplicate {name}")


@dataclass(frozen=True)
class UtilityVector:
    scenarios: tuple[str, ...]
    unit: str
    values: tuple[float, ...]

    def __post_init__(self) -> None:
        _names(self.scenarios, "utility scenarios")
        _text(self.unit, "utility unit")
        _tuple(self.values, "utility values")
        if len(self.values) != len(self.scenarios):
            raise ValueError("utility/scenario length mismatch")
        for value in self.values:
            _number(value, "utility")


@dataclass(frozen=True)
class Distribution:
    name: str
    scenarios: tuple[str, ...]
    probabilities: tuple[float, ...]

    def __post_init__(self) -> None:
        _text(self.name, "distribution name")
        _names(self.scenarios, "distribution scenarios")
        _tuple(self.probabilities, "probabilities")
        if len(self.probabilities) != len(self.scenarios):
            raise ValueError("probability/scenario length mismatch")
        for probability in self.probabilities:
            _number(probability, "probability")
            if probability < 0 or probability > 1:
                raise ValueError("probabilities must lie in [0, 1]")
        if abs(fsum(self.probabilities) - 1.0) > 1e-12:
            raise ValueError("probabilities must sum to one; never auto-normalized")


@dataclass(frozen=True)
class Constraint:
    name: str
    unit: str
    lower: float
    upper: float

    def __post_init__(self) -> None:
        _text(self.name, "constraint name")
        _text(self.unit, "constraint unit")
        _number(self.lower, "lower bound")
        _number(self.upper, "upper bound")
        if self.lower > self.upper:
            raise ValueError("lower bound exceeds upper bound")


@dataclass(frozen=True)
class ScenarioLoads:
    scenarios: tuple[str, ...]
    constraints: tuple[str, ...]
    units: tuple[str, ...]
    values: tuple[tuple[float, ...], ...]

    def __post_init__(self) -> None:
        _names(self.scenarios, "load scenarios")
        _names(self.constraints, "load constraints")
        _tuple(self.units, "load units")
        for unit in self.units:
            _text(unit, "load unit")
        if len(self.units) != len(self.constraints):
            raise ValueError("constraint/unit length mismatch")
        _tuple(self.values, "load rows")
        if len(self.values) != len(self.scenarios):
            raise ValueError("load/scenario length mismatch")
        for row in self.values:
            _tuple(row, "load row")
            if len(row) != len(self.constraints):
                raise ValueError("load/constraint length mismatch")
            for value in row:
                _number(value, "constraint load")


@dataclass(frozen=True)
class LoadAlternative:
    name: str
    loads: ScenarioLoads

    def __post_init__(self) -> None:
        _text(self.name, "fill alternative name")
        if not isinstance(self.loads, ScenarioLoads):
            raise ValueError("loads must be ScenarioLoads")


@dataclass(frozen=True)
class OutstandingOrder:
    order_id: str
    fill_alternatives: tuple[LoadAlternative, ...]

    def __post_init__(self) -> None:
        _text(self.order_id, "order ID")
        _typed_tuple(self.fill_alternatives, LoadAlternative, "order fill alternatives")
        _unique_ids(self.fill_alternatives, "name", "order fill alternatives")
        if not any(all(value == 0 for row in alternative.loads.values for value in row)
                   for alternative in self.fill_alternatives):
            raise ValueError("each outstanding order must reserve a zero-fill alternative")


@dataclass(frozen=True)
class InputRequirement:
    name: str
    max_age_seconds: int

    def __post_init__(self) -> None:
        _text(self.name, "input name")
        _integer(self.max_age_seconds, "maximum input age")


@dataclass(frozen=True)
class Observation:
    name: str
    observed_at: int
    valid: bool

    def __post_init__(self) -> None:
        _text(self.name, "observation name")
        _integer(self.observed_at, "observation timestamp")
        _boolean(self.valid, "observation validity")


@dataclass(frozen=True)
class ActionRule:
    action_id: str
    required_inputs: tuple[InputRequirement, ...]

    def __post_init__(self) -> None:
        _text(self.action_id, "action ID")
        _typed_tuple(self.required_inputs, InputRequirement, "required inputs", allow_empty=True)
        _unique_ids(self.required_inputs, "name", "required inputs")


@dataclass(frozen=True)
class Policy:
    version: str
    scenarios: tuple[str, ...]
    distributions: tuple[Distribution, ...]
    utility_unit: str
    hurdle: float
    constraints: tuple[Constraint, ...]
    action_menu: tuple[ActionRule, ...]
    max_own_state_age_seconds: int = 5
    max_reservation_combinations: int = 4096

    def __post_init__(self) -> None:
        _text(self.version, "policy version")
        _names(self.scenarios, "policy scenarios")
        _typed_tuple(self.distributions, Distribution, "distributions")
        _unique_ids(self.distributions, "name", "distribution names")
        if any(distribution.scenarios != self.scenarios for distribution in self.distributions):
            raise ValueError("distribution scenarios must exactly match policy order")
        _text(self.utility_unit, "policy utility unit")
        _number(self.hurdle, "economic/switching hurdle")
        if self.hurdle < 0:
            raise ValueError("economic/switching hurdle must be nonnegative")
        _typed_tuple(self.constraints, Constraint, "constraints")
        _unique_ids(self.constraints, "name", "constraints")
        _typed_tuple(self.action_menu, ActionRule, "action menu", allow_empty=True)
        _unique_ids(self.action_menu, "action_id", "approved action IDs")
        _integer(self.max_own_state_age_seconds, "maximum own-state age")
        _integer(self.max_reservation_combinations, "maximum reservation combinations")
        if self.max_reservation_combinations == 0:
            raise ValueError("maximum reservation combinations must be positive")


@dataclass(frozen=True)
class Incumbent:
    policy_id: str
    policy_version: str
    own_state_known: bool
    state_observed_at: int
    position_loads: ScenarioLoads
    outstanding_orders: tuple[OutstandingOrder, ...] = ()

    def __post_init__(self) -> None:
        _text(self.policy_id, "incumbent policy ID")
        _text(self.policy_version, "incumbent policy version")
        _boolean(self.own_state_known, "own-state knowledge")
        _integer(self.state_observed_at, "own-state timestamp")
        if not isinstance(self.position_loads, ScenarioLoads):
            raise ValueError("incumbent position loads must be ScenarioLoads")
        _typed_tuple(self.outstanding_orders, OutstandingOrder, "outstanding orders", allow_empty=True)
        _unique_ids(self.outstanding_orders, "order_id", "outstanding order IDs")


@dataclass(frozen=True)
class Candidate:
    action_id: str
    decision_policy_version: str
    incumbent_policy_id: str
    incumbent_policy_version: str
    incremental_utility: UtilityVector
    post_action_position_loads: tuple[LoadAlternative, ...]
    observations: tuple[Observation, ...]
    eligible: bool
    evidence_passed: bool
    evidence_reference: str
    decision_deadline: int

    def __post_init__(self) -> None:
        for value, name in ((self.action_id, "action ID"),
                            (self.decision_policy_version, "decision policy version"),
                            (self.incumbent_policy_id, "paired incumbent policy ID"),
                            (self.incumbent_policy_version, "paired incumbent policy version"),
                            (self.evidence_reference, "evidence reference")):
            _text(value, name)
        if not isinstance(self.incremental_utility, UtilityVector):
            raise ValueError("incremental utility must be UtilityVector")
        _typed_tuple(self.post_action_position_loads, LoadAlternative, "post-action alternatives")
        _unique_ids(self.post_action_position_loads, "name", "post-action alternatives")
        _typed_tuple(self.observations, Observation, "observations", allow_empty=True)
        _unique_ids(self.observations, "name", "observations")
        _boolean(self.eligible, "eligibility gate")
        _boolean(self.evidence_passed, "evidence gate")
        _integer(self.decision_deadline, "candidate decision deadline")


@dataclass(frozen=True)
class Breach:
    position_alternative: str
    outstanding_fills: tuple[tuple[str, str], ...]
    scenario: str
    constraint: str
    load: float
    lower: float
    upper: float
    unit: str


@dataclass(frozen=True)
class CandidateAudit:
    action_id: str
    evidence_reference: str
    reasons: tuple[str, ...]
    robust_score: Optional[float] = None
    worst_distribution: Optional[str] = None
    breach: Optional[Breach] = None


@dataclass(frozen=True)
class Decision:
    status: str
    policy_version: str
    incumbent_policy_id: str
    incumbent_policy_version: str
    as_of: int
    decision_deadline: int
    utility_unit: str
    hurdle: float
    selected_action_id: Optional[str]
    selected_score: Optional[float]
    reasons: tuple[str, ...]
    candidate_audits: tuple[CandidateAudit, ...]
    incumbent_breach: Optional[Breach] = None


def _validate_loads(policy: Policy, loads: ScenarioLoads) -> None:
    if loads.scenarios != policy.scenarios:
        raise ValueError("load scenarios must exactly match policy order")
    if loads.constraints != tuple(limit.name for limit in policy.constraints):
        raise ValueError("load constraint names/order mismatch")
    if loads.units != tuple(limit.unit for limit in policy.constraints):
        raise ValueError("load constraint units mismatch")


def _first_breach(policy: Policy, alternatives: tuple[LoadAlternative, ...],
                  orders: tuple[OutstandingOrder, ...]) -> Optional[Breach]:
    ordered_orders = tuple(sorted(orders, key=lambda order: order.order_id))
    fill_sets = tuple(tuple(sorted(order.fill_alternatives, key=lambda fill: fill.name))
                      for order in ordered_orders)
    for alternative in sorted(alternatives, key=lambda item: item.name):
        for fills in product(*fill_sets):
            for scenario_index, scenario in enumerate(policy.scenarios):
                for constraint_index, limit in enumerate(policy.constraints):
                    pieces = (alternative.loads.values[scenario_index][constraint_index],) + tuple(
                        fill.loads.values[scenario_index][constraint_index] for fill in fills)
                    try:
                        load = fsum(pieces)
                    except OverflowError as error:
                        raise ValueError("combined constraint load overflow") from error
                    _number(load, "combined constraint load")
                    if not limit.lower <= load <= limit.upper:
                        return Breach(alternative.name,
                                      tuple((order.order_id, fill.name)
                                            for order, fill in zip(ordered_orders, fills)),
                                      scenario, limit.name, load, limit.lower, limit.upper, limit.unit)
    return None


def robust_score(policy: Policy, delta: UtilityVector) -> tuple[float, str]:
    """Return worst paired delta and distribution ID; no baseline subtraction."""
    if delta.scenarios != policy.scenarios or delta.unit != policy.utility_unit:
        raise ValueError("utility scenarios/order or named units mismatch")
    evaluations = []
    for distribution in policy.distributions:
        terms = tuple(probability * utility
                      for probability, utility in zip(distribution.probabilities, delta.values))
        for term in terms:
            _number(term, "weighted utility")
        try:
            value = fsum(terms)
        except OverflowError as error:
            raise ValueError("robust score overflow") from error
        _number(value, "distribution utility")
        evaluations.append((value, distribution.name))
    return min(evaluations)


def select(policy: Policy, incumbent: Incumbent, candidates: tuple[Candidate, ...],
           *, now: int, decision_deadline: int) -> Decision:
    """Validate all inputs, gate alpha, reserve risk, and select deterministically.

    At either deadline equality the decision has expired. Missing/invalid/stale
    action data reject only that action; own-state uncertainty gates all alpha.
    Malformed structures, scenario/unit mismatches, and mixed baselines raise
    ValueError, even when an earlier global gate would have rejected promotion.
    The returned action ID is a proposal, never an execution instruction.
    """
    if not isinstance(policy, Policy) or not isinstance(incumbent, Incumbent):
        raise ValueError("Policy and Incumbent instances are required")
    _typed_tuple(candidates, Candidate, "candidates", allow_empty=True)
    _unique_ids(candidates, "action_id", "candidate action IDs")
    _integer(now, "decision timestamp")
    _integer(decision_deadline, "decision deadline")
    _validate_loads(policy, incumbent.position_loads)
    combinations = 1
    for order in incumbent.outstanding_orders:
        combinations *= len(order.fill_alternatives)
        if combinations > policy.max_reservation_combinations:
            raise ValueError("outstanding fill combinations exceed policy's finite computation cap")
        for alternative in order.fill_alternatives:
            _validate_loads(policy, alternative.loads)
    for candidate in candidates:
        if candidate.decision_policy_version != policy.version:
            raise ValueError("candidate decision policy version mismatch")
        if (candidate.incumbent_policy_id, candidate.incumbent_policy_version) != (
                incumbent.policy_id, incumbent.policy_version):
            raise ValueError("all candidates must use the SAME incumbent policy/version")
        if (candidate.incremental_utility.scenarios != policy.scenarios or
                candidate.incremental_utility.unit != policy.utility_unit):
            raise ValueError("utility scenarios/order or named units mismatch")
        for alternative in candidate.post_action_position_loads:
            _validate_loads(policy, alternative.loads)
        if not any(alternative.loads == incumbent.position_loads
                   for alternative in candidate.post_action_position_loads):
            raise ValueError("candidate must include unchanged positions as a no-new-fill outcome")

    def result(status: str, reasons: tuple[str, ...], audits: tuple[CandidateAudit, ...] = (),
               selected: Optional[CandidateAudit] = None, breach: Optional[Breach] = None) -> Decision:
        effective_deadline = decision_deadline
        if selected is not None:
            selected_candidate = next(candidate for candidate in candidates
                                      if candidate.action_id == selected.action_id)
            effective_deadline = min(decision_deadline, selected_candidate.decision_deadline)
        return Decision(status, policy.version, incumbent.policy_id, incumbent.policy_version,
                        now, effective_deadline, policy.utility_unit, policy.hurdle,
                        selected.action_id if selected else None,
                        selected.robust_score if selected else None, reasons, audits, breach)

    own_age = now - incumbent.state_observed_at
    if not incumbent.own_state_known or own_age < 0 or own_age > policy.max_own_state_age_seconds:
        return result("remediation_needed", ("own_state_unknown_invalid_or_stale", "alpha_promotion_forbidden"))
    breach = _first_breach(policy, (LoadAlternative("incumbent", incumbent.position_loads),),
                           incumbent.outstanding_orders)
    if breach is not None:
        return result("remediation_needed", ("reserved_incumbent_infeasible", "alpha_promotion_forbidden"),
                      breach=breach)
    if now >= decision_deadline:
        return result("no_new_order", ("decision_deadline_expired", "retain_incumbent_policy"))

    menu = {rule.action_id: rule for rule in policy.action_menu}
    audits = []
    for candidate in sorted(candidates, key=lambda item: item.action_id):
        reasons = []
        if candidate.action_id not in menu:
            reasons.append("action_not_preapproved")
        if not candidate.eligible:
            reasons.append("eligibility_gate_failed")
        if not candidate.evidence_passed:
            reasons.append("evidence_gate_failed")
        if now >= candidate.decision_deadline:
            reasons.append("candidate_deadline_expired")
        observations = {observation.name: observation for observation in candidate.observations}
        if candidate.action_id in menu:
            for requirement in menu[candidate.action_id].required_inputs:
                observation = observations.get(requirement.name)
                if observation is None:
                    reasons.append(f"missing_input:{requirement.name}")
                elif not observation.valid:
                    reasons.append(f"invalid_input:{requirement.name}")
                elif not 0 <= now - observation.observed_at <= requirement.max_age_seconds:
                    reasons.append(f"stale_or_future_input:{requirement.name}")
        if reasons:
            audits.append(CandidateAudit(candidate.action_id, candidate.evidence_reference, tuple(reasons)))
            continue
        breach = _first_breach(policy, candidate.post_action_position_loads, incumbent.outstanding_orders)
        if breach is not None:
            audits.append(CandidateAudit(candidate.action_id, candidate.evidence_reference,
                                         ("post_action_reservations_infeasible",), breach=breach))
            continue
        score, worst_distribution = robust_score(policy, candidate.incremental_utility)
        reasons = () if score > policy.hurdle else ("robust_delta_does_not_strictly_clear_hurdle",)
        audits.append(CandidateAudit(candidate.action_id, candidate.evidence_reference, reasons,
                                     score, worst_distribution))

    qualified = tuple(audit for audit in audits if not audit.reasons)
    if not qualified:
        return result("no_new_order", ("no_candidate_clears_all_gates", "retain_incumbent_policy"), tuple(audits))
    selected = min(qualified, key=lambda audit: (-audit.robust_score, audit.action_id))
    return result("selected", ("strict_robust_delta_hurdle_passed",), tuple(audits), selected)
