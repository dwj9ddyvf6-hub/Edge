# Offline mechanics companion

Files: `edge_mechanics.py`, `test_edge_mechanics.py`. Python 3.10+, standard library only. Twenty-three synthetic test methods passed on 24 October 2026 after an independent review identified and corrected a numerical cancellation defect. These tests validate finite-model arithmetic and input handling; they are not market backtests or a measured trading-performance improvement.

## Functions and intended use

- `finite_value_of_information(joint_probabilities, action_utilities)`: the joint matrix is signal by state; the utility matrix is action by state. Returns the best uninformed value, informed value, gross information value and deterministic action choices. Every action, price, feasible set, horizon and complete net utility is held fixed across the comparison. Include an abstention action when appropriate. The function does not construct probabilities from prose or market prices. Information costs, price adjustment before execution, delay and different action menus need a fuller model; the nonnegative-free-information result does not apply unchanged to those cases.
- `seller_reservation_premium(probabilities, wealth, liabilities, gamma)`: computes the deterministic premium that leaves a CARA expected-utility seller indifferent to a terminal liability, given the current state-contingent wealth. Positive liabilities are payments out; negative values are receipts. No additional hedge decisions are optimized. Costs belong in the supplied liability exactly once, and all monetary values need the same terminal numeraire. Risk aversion is an explicit model input, not inferred or recommended. The computation does not establish that any offered premium is obtainable or that interim financing/margin is safe.
- `finite_payoff_check(payoffs, quantities, initial_cost, probabilities=None)`: checks terminal payoff algebra in supplied states. Financing and cash legs must be explicit. Separates nonnegative state payoffs, positive payoff somewhere, strict positivity everywhere, initial-cost condition, and positive-probability benefit under supplied probabilities. It reports a standard-arbitrage *shape* only when probabilities are supplied. It cannot establish complete contract semantics, true probability support, available size, simultaneous fills, funding, settlement or counterparty performance.

## Worked consequences

For a binary claim bought at 0.55 or passed, signals producing posteriors 0.2 and 0.8 with equal probability have gross value 0.125 when that quote remains available. Signals producing posteriors 0.3 and 0.5 have zero decision value at an executable price of 0.7, despite conveying information. Two individually useless signals can jointly matter: independent fair bits reveal their XOR only when combined; the test uses this as a complementary-information example.

For equally probable states, liability distribution {0, 20} and risk aversion 0.05, flat wealth yields a reservation premium about 12.40. Coupling the 20 liability with wealth 20 rather than wealth 100 changes the reservation premium sharply, although the liability's own mean and variance are unchanged. The test checks actual expected-utility equality at the computed price, the direction of a one-unit premium change, translation invariance, and restoration of extremely rare tilted states by large liabilities.

A zero-cost payoff {0, 1} with positive probability on each state passes the standard arbitrage shape but has no strictly positive minimum payoff. A pair of exact complementary payoffs, each paying one in its own state, plus an explicit 0.95 borrowing repayment, produces 0.05 in each state. Different weather-station contracts leave a state in which both risky legs lose; the checker catches the resulting -0.90 payoff only if that state and financing leg were supplied.

## Numerical and interpretation limits

- Inputs reject booleans, non-real values, NaN, infinity, ragged arrays, invalid dimensions, probabilities outside [0,1], materially nonunit probability totals, and nonpositive risk aversion. Totals within 1e-12 are normalized for floating-point residuals.
- Computation uses finite floats, stable log sums, exact rational differences of supplied floats for centering net wealth, and small-argument transforms. Intermediate values outside finite range raise `ValueError`. When opposing cash components leave a residual below 1e-8 of their scale, the premium calculation raises `ValueError` and requires higher precision instead of presenting lost digits as meaningful. Finite inputs do not promise arbitrary-precision outputs.
- A zero probability is the caller's assertion, not something justified by an event having been absent in a sample. The payoff result also reports the all-supplied-state condition so that a probability-support assertion is visible.
- Strict payoff signs use no tolerance that forgives negative cashflow. The information-value calculation removes only a few units in the last place of theoretically impossible negative roundoff.
- The calculations provide numerical checks inside an economic analysis. They do not replace the analysis, parameter estimation, empirical execution or explicit operational feasibility checks.

## Independent-review correction

The initial implementation added the liability exponent to an already rounded `log(p)-gamma*wealth` term. For equally probable states with wealth and liability both `{0, 1e16}` and gamma 1, it returned about 1.098612 instead of log(2), about 0.693147: adding the huge opposing exponents erased a probability term. The revised implementation centers net wealth before adding log probabilities. New regressions cover that case, unequal probabilities, small positive and negative liabilities against large common wealth, and explicit rejection when a tiny signed premium cannot be resolved credibly. The pre-fix result remains part of the independent review record; it is not treated as a passing calculation.

Run:

```bash
python -m unittest discover -s . -p test_edge_mechanics.py -v
```
