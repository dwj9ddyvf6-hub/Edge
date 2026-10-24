import math
import unittest

from edge_mechanics import finite_value_of_information, seller_reservation_premium, finite_payoff_check


class InformationTests(unittest.TestCase):
    def test_executable_threshold_example(self):
        # Buy a binary claim at .55 or abstain; favorable posterior is .8.
        result = finite_value_of_information([[.4, .1], [.1, .4]], [[0, 0], [-.55, .45]])
        self.assertAlmostEqual(result.baseline_value, 0)
        self.assertAlmostEqual(result.informed_value, .125)
        self.assertAlmostEqual(result.gross_value, .125)
        self.assertEqual(result.signal_actions, (0, 1))

    def test_signal_information_without_decision_value(self):
        # Both .3 and .5 posteriors remain below the .7 executable threshold.
        result = finite_value_of_information([[.35, .15], [.25, .25]], [[0, 0], [-.7, .3]])
        self.assertEqual(result.gross_value, 0)
        self.assertEqual(result.signal_actions, (0, 0))

    def test_uninformative_signal_has_zero_value(self):
        result = finite_value_of_information([[.15, .35], [.15, .35]], [[0, 0], [-.6, .4]])
        self.assertAlmostEqual(result.gross_value, 0)
        self.assertEqual(result.signal_actions, (1, 1))

    def test_garbling_cannot_improve_fixed_problem(self):
        actions = [[0, 0], [-.55, .45]]
        exact = finite_value_of_information([[.5, 0], [0, .5]], actions)
        noisy = finite_value_of_information([[.4, .1], [.1, .4]], actions)
        blind = finite_value_of_information([[.25, .25], [.25, .25]], actions)
        self.assertAlmostEqual(exact.gross_value, .225)
        self.assertGreater(exact.gross_value, noisy.gross_value)
        self.assertGreater(noisy.gross_value, blind.gross_value)

    def test_xor_complementary_signals(self):
        # Independent fair bits A and B reveal Y=A XOR B only jointly.
        utilities = [[0, 0], [-.5, .5], [.5, -.5]]
        single = finite_value_of_information([[.25, .25], [.25, .25]], utilities)
        combined = finite_value_of_information([[.25, 0], [0, .25], [0, .25], [.25, 0]], utilities)
        self.assertEqual(single.gross_value, 0)
        self.assertAlmostEqual(combined.gross_value, .5)

    def test_free_optional_information_property_and_impossible_signal(self):
        for utility in ([[-7, 8], [3, -2], [0, 0]], [[-100, -10]], [[1, 2], [2, 1]]):
            result = finite_value_of_information([[.1, .3], [.2, .4], [0, 0]], utility)
            self.assertGreaterEqual(result.gross_value, 0)
            self.assertIsNone(result.signal_actions[-1])

    def test_action_independent_state_endowment_does_not_change_gain(self):
        joint = [[.4, .1], [.1, .4]]
        old = finite_value_of_information(joint, [[0, 0], [-.55, .45]])
        new = finite_value_of_information(joint, [[4, 10], [3.45, 10.45]])
        self.assertAlmostEqual(new.gross_value, old.gross_value)
        self.assertEqual(new.signal_actions, old.signal_actions)


class WarehouseTests(unittest.TestCase):
    def test_flat_endowment_analytic_entropic_price(self):
        actual = seller_reservation_premium([.5, .5], [100, 100], [0, 20], .05)
        self.assertAlmostEqual(actual, math.log((1 + math.e) / 2) / .05)
        self.assertGreater(actual, 10)

    def test_identical_liability_distribution_different_state_coupling(self):
        bad_state = seller_reservation_premium([.5, .5], [100, 20], [0, 20], .05)
        rich_state = seller_reservation_premium([.5, .5], [100, 20], [20, 0], .05)
        self.assertGreater(bad_state, 19)
        self.assertLess(rich_state, 1)
        self.assertGreater(bad_state, rich_state)

    def test_expected_utility_indifference_and_direction(self):
        p, w, loss, gamma = [.3, .7], [20, 80], [15, 0], .04
        premium = seller_reservation_premium(p, w, loss, gamma)
        baseline = sum(prob * -math.exp(-gamma * cash) for prob, cash in zip(p, w))
        def value(offer):
            return sum(prob * -math.exp(-gamma * (cash + offer - claim)) for prob, cash, claim in zip(p, w, loss))
        self.assertAlmostEqual(value(premium), baseline)
        self.assertLess(value(premium - 1), baseline)
        self.assertGreater(value(premium + 1), baseline)

    def test_cash_translation_and_liability_translation(self):
        p, w, loss = [.2, .8], [10, 40], [8, -2]
        original = seller_reservation_premium(p, w, loss, .1)
        shifted_w = seller_reservation_premium(p, [x + 1e10 for x in w], loss, .1)
        shifted_l = seller_reservation_premium(p, w, [x + 7 for x in loss], .1)
        self.assertAlmostEqual(shifted_w, original)
        self.assertAlmostEqual(shifted_l, original + 7)

    def test_constant_and_tiny_risk_aversion(self):
        self.assertEqual(seller_reservation_premium([.1, .9], [0, 50], [-3, -3], 2), -3)
        self.assertAlmostEqual(seller_reservation_premium([.5, .5], [20, 100], [0, 20], 1e-300), 10)

    def test_rare_tilted_state_can_return_through_large_liability(self):
        # Forming ordinary tilted probabilities first would underflow state 2.
        premium = seller_reservation_premium([.5, .5], [0, 1000], [0, 2000], 1)
        self.assertAlmostEqual(premium, 1000)

    def test_zero_probability_states_and_bounds(self):
        self.assertEqual(seller_reservation_premium([1, 0], [10, -1e200], [3, 1e200], 2), 3)
        for gamma in (.0001, .03, 1, 30):
            value = seller_reservation_premium([.2, .3, .5], [20, 50, 100], [-2, 4, 10], gamma)
            self.assertGreaterEqual(value, -2 - 1e-12)
            self.assertLessEqual(value, 10 + 1e-12)


class PayoffTests(unittest.TestCase):
    def test_zero_cost_boundary_arbitrage_not_sure_profit(self):
        result = finite_payoff_check([[0], [1]], [1], 0, [.5, .5])
        self.assertTrue(result.standard_arbitrage_shape)
        self.assertFalse(result.sure_profit_shape)
        self.assertTrue(result.nonnegative_with_positive_supplied_state)
        self.assertFalse(result.strictly_positive_all_supplied_states)

    def test_complements_with_explicit_cash_financing_leg(self):
        result = finite_payoff_check([[1, 0, 1], [0, 1, 1]], [1, 1, -.95], 0, [.5, .5])
        self.assertTrue(result.standard_arbitrage_shape)
        self.assertTrue(result.sure_profit_shape)
        self.assertAlmostEqual(result.minimum_supplied_payoff, .05)

    def test_mismatched_contracts_have_a_losing_state(self):
        # Downtown YES, airport NO, and explicit borrowed cash repayment.
        result = finite_payoff_check([[0, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 1]], [1, 1, -.9], 0, [.25] * 4)
        self.assertAlmostEqual(result.minimum_supplied_payoff, -.9)
        self.assertFalse(result.standard_arbitrage_shape)
        self.assertFalse(result.sure_profit_shape)

    def test_probability_support_is_explicit_not_invented(self):
        unknown = finite_payoff_check([[0], [1]], [1], 0)
        zero_positive = finite_payoff_check([[0], [1]], [1], 0, [1, 0])
        self.assertIsNone(unknown.standard_arbitrage_shape)
        self.assertIsNone(unknown.positive_probability_benefit)
        self.assertFalse(zero_positive.standard_arbitrage_shape)

    def test_initial_cost_and_all_state_vs_almost_sure_conditions(self):
        funded = finite_payoff_check([[2]], [1], 1, [1])
        self.assertFalse(funded.standard_arbitrage_shape)
        rebate = finite_payoff_check([[0], [0]], [1], -1, [.5, .5])
        self.assertTrue(rebate.standard_arbitrage_shape)
        self.assertTrue(rebate.sure_profit_shape)
        supported = finite_payoff_check([[-1], [1]], [1], 0, [0, 1])
        self.assertTrue(supported.standard_arbitrage_shape)
        self.assertFalse(supported.nonnegative_all_supplied_states)
        self.assertFalse(supported.sure_profit_shape)


class ValidationTests(unittest.TestCase):
    def test_invalid_inputs_are_rejected(self):
        calls = [
            lambda: finite_value_of_information([], [[0]]),
            lambda: finite_value_of_information([[.5], [.4]], [[0]]),
            lambda: finite_value_of_information([[1]], [[0, 1]]),
            lambda: finite_value_of_information([[.5, .5]], [[0], [1, 2]]),
            lambda: finite_value_of_information([[True]], [[0]]),
            lambda: finite_value_of_information([[1]], [[float('nan')]]),
            lambda: finite_value_of_information([[1]], [[10**400]]),
            lambda: seller_reservation_premium([1], [0], [1], 0),
            lambda: seller_reservation_premium([1], [0], [1], float('inf')),
            lambda: seller_reservation_premium([.5, .5], [0], [1, 2], 1),
            lambda: seller_reservation_premium([-.1, 1.1], [0, 0], [1, 2], 1),
            lambda: seller_reservation_premium([1], [False], [1], 1),
            lambda: seller_reservation_premium([.5, .5], [-1e308, 1e308], [0, 1], 1),
            lambda: finite_payoff_check([[0, 1]], [1], 0),
            lambda: finite_payoff_check([[0]], [1], 0, [.5, .5]),
            lambda: finite_payoff_check([[float('inf')]], [0], 0),
            lambda: finite_payoff_check([[1]], [1], True),
            lambda: finite_payoff_check([[1e308]], [1e308], 0),
        ]
        for call in calls:
            with self.subTest(call=call):
                with self.assertRaises(ValueError):
                    call()


if __name__ == '__main__':
    unittest.main()
