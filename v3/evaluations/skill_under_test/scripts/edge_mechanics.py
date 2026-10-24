"""Offline finite-model calculations for Trading Edge Lab.

These functions calculate consequences of caller-supplied probabilities, utility,
payoffs and state definitions. They do not estimate an edge, validate a model,
infer contract semantics, calculate broker margin, or authorize/submit orders.
All money quantities must use one declared terminal cash numeraire.
"""

from dataclasses import dataclass
import math
from numbers import Real
from typing import Optional, Sequence, Tuple


def _number(value: Real, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{label} must be a real number, excluding bool")
    try:
        result = float(value)
    except (ValueError, OverflowError) as exc:
        raise ValueError(f"{label} is outside finite float range") from exc
    if not math.isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def _vector(values: Sequence[Real], label: str) -> Tuple[float, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{label} must be a nonempty sequence")
    try:
        result = tuple(_number(v, label) for v in values)
    except TypeError as exc:
        raise ValueError(f"{label} must be a nonempty sequence") from exc
    if not result:
        raise ValueError(f"{label} must be nonempty")
    return result


def _matrix(values: Sequence[Sequence[Real]], label: str) -> Tuple[Tuple[float, ...], ...]:
    try:
        rows = tuple(_vector(row, label) for row in values)
    except TypeError as exc:
        raise ValueError(f"{label} must be a nonempty rectangular matrix") from exc
    if not rows or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError(f"{label} must be a nonempty rectangular matrix")
    return rows


def _sum(values, label: str) -> float:
    try:
        result = math.fsum(values)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{label} arithmetic exceeded finite precision") from exc
    if not math.isfinite(result):
        raise ValueError(f"{label} arithmetic exceeded finite precision")
    return result


def _probabilities(values: Sequence[Real], label: str) -> Tuple[float, ...]:
    result = _vector(values, label)
    if any(p < 0 or p > 1 for p in result):
        raise ValueError(f"{label} must be in [0, 1]")
    total = _sum(result, label)
    if not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError(f"{label} must sum to 1 within 1e-12")
    # Explicitly normalize only the admitted floating-point summation residual.
    return tuple(p / total for p in result)


@dataclass(frozen=True)
class InformationValue:
    baseline_value: float
    informed_value: float
    gross_value: float
    baseline_action: int
    signal_actions: Tuple[Optional[int], ...]


def finite_value_of_information(joint_probabilities, action_utilities) -> InformationValue:
    """Evaluate free optional information in a fixed finite decision problem.

    joint_probabilities[signal][state] supplies P(signal, state).
    action_utilities[action][state] supplies complete already-net utility on
    the SAME action menu, prices, horizon and opportunity set in both cases.
    Ties choose the first action. An impossible signal has action None.

    Gross information value excludes acquisition cost. Signal-driven price
    changes, execution delays, changing feasible actions and estimation error
    are outside this comparison; subtracting an arbitrary fee does not model
    those changes. Utilities may include existing portfolio wealth and risk.
    """
    joint = _matrix(joint_probabilities, "joint probabilities")
    utilities = _matrix(action_utilities, "action utilities")
    if len(utilities[0]) != len(joint[0]):
        raise ValueError("utilities and probabilities must share state count")
    flat = _probabilities(tuple(p for row in joint for p in row), "joint probabilities")
    width = len(joint[0])
    joint = tuple(flat[i:i + width] for i in range(0, len(flat), width))
    marginal = tuple(_sum((row[j] for row in joint), "marginal") for j in range(width))
    baseline_scores = tuple(_sum((p * u for p, u in zip(marginal, action)), "utility") for action in utilities)
    baseline_action = max(range(len(utilities)), key=baseline_scores.__getitem__)
    baseline = baseline_scores[baseline_action]
    choices = []
    contributions = []
    for row in joint:
        if not any(row):
            choices.append(None)
            contributions.append(0.0)
            continue
        scores = tuple(_sum((p * u for p, u in zip(row, action)), "utility") for action in utilities)
        best = max(range(len(utilities)), key=scores.__getitem__)
        choices.append(best)
        contributions.append(scores[best])
    informed = _sum(contributions, "informed value")
    gain = _number(informed - baseline, "information value")
    # Theory guarantees nonnegative gain here; remove only a few ulps of drift.
    if gain < 0 and gain >= -8 * math.ulp(max(abs(informed), abs(baseline), 1.0)):
        gain = 0.0
    if gain < 0:
        raise ValueError("numerical result violates the fixed-menu information comparison")
    return InformationValue(baseline, informed, gain, baseline_action, tuple(choices))


def _logsumexp(values: Tuple[float, ...]) -> float:
    maximum = max(values)
    return maximum + math.log(_sum((math.exp(v - maximum) for v in values), "log sum"))


def seller_reservation_premium(probabilities, wealth, liabilities, gamma) -> float:
    """Minimum deterministic terminal premium for a supplied CARA seller model.

    U(w)=-exp(-gamma*w), gamma>0, and positive liability means money paid out.
    Solve E[U(W+premium-L)] = E[U(W)] with the existing hedge set frozen.
    The premium is [log E exp(-gamma*(W-L))-log E exp(-gamma*W)]/gamma.
    Wealth/liability coupling matters. Negative liabilities and premiums are
    allowed. Probabilities and risk aversion are supplied, never inferred.

    This terminal expected-utility calculation excludes path liquidity,
    margin, default, additional hedging choices, fees and policy authorization.
    Include relevant terminal costs in L; assess interim feasibility separately.
    """
    p = _probabilities(probabilities, "probabilities")
    w = _vector(wealth, "wealth")
    liability = _vector(liabilities, "liabilities")
    risk_aversion = _number(gamma, "gamma")
    if risk_aversion <= 0:
        raise ValueError("gamma must be positive")
    if len(p) != len(w) or len(p) != len(liability):
        raise ValueError("probabilities, wealth and liabilities must share length")
    active = [(prob, cash, loss) for prob, cash, loss in zip(p, w, liability) if prob > 0]
    minimum_wealth = min(cash for _, cash, _ in active)
    lower = min(loss for _, _, loss in active)
    upper = max(loss for _, _, loss in active)
    if lower == upper:
        return lower
    log_base = tuple(_number(math.log(prob) - risk_aversion * _number(cash - minimum_wealth, "wealth range"), "scaled wealth") for prob, cash, _ in active)
    offsets = tuple(_number(loss - lower, "liability range") for _, _, loss in active)
    scaled = tuple(_number(risk_aversion * offset, "scaled liability") for offset in offsets)
    base_log_sum = _logsumexp(log_base)
    if max(scaled) <= 0.5:
        weights = tuple(math.exp(x - base_log_sum) for x in log_base)
        total = _sum(weights, "tilted probabilities")
        weights = tuple(x / total for x in weights)
        # expm1(x)/x and log1p(x)/x avoid cancellation, including tiny gamma.
        mean_excess = _sum((weight * offset * (math.expm1(x) / x if x else 1.0) for weight, offset, x in zip(weights, offsets, scaled)), "premium moment")
        growth = risk_aversion * mean_excess
        premium = lower + mean_excess * (math.log1p(growth) / growth if growth else 1.0)
    else:
        numerator = tuple(_number(log_weight + offset, "premium exponent") for log_weight, offset in zip(log_base, scaled))
        premium = lower + (_logsumexp(numerator) - base_log_sum) / risk_aversion
    return _number(premium, "reservation premium")


@dataclass(frozen=True)
class PayoffShape:
    terminal_payoffs: Tuple[float, ...]
    minimum_supplied_payoff: float
    nonpositive_initial_cost: bool
    nonnegative_all_supplied_states: bool
    strictly_positive_all_supplied_states: bool
    nonnegative_with_positive_supplied_state: bool
    positive_probability_benefit: Optional[bool]
    standard_arbitrage_shape: Optional[bool]
    sure_profit_shape: bool


def finite_payoff_check(payoffs, quantities, initial_cost, probabilities=None) -> PayoffShape:
    """Check payoff algebra ONLY over the states and cashflows supplied.

    payoffs[state][leg] are terminal net leg cashflows; quantities are signed.
    initial_cost is the complete executable upfront cost. Terminal cashflows
    must already include relevant costs and explicit financing/cash legs;
    initial_cost is not silently subtracted from them again.

    A standard arbitrage SHAPE requires nonpositive initial cost, nonnegative
    payoff on the supplied probability support and strictly positive benefit
    with positive probability (or a strictly negative initial cost). It is None
    when no probabilities are provided. Sure-profit shape requires nonnegative
    payoffs in EVERY supplied state and a strictly positive benefit in every
    such state, either initially or terminally. A {0,1} zero-cost payoff can
    have standard shape while not having sure-profit shape.

    None of these fields proves actual arbitrage: complete and correct state
    semantics, real probability support, simultaneous executable size, funding,
    interim cash obligations, settlement/default and legality remain unverified.
    There is no epsilon that forgives a genuinely negative state payoff.
    """
    matrix = _matrix(payoffs, "payoffs")
    size = _vector(quantities, "quantities")
    cost = _number(initial_cost, "initial cost")
    if len(matrix[0]) != len(size):
        raise ValueError("payoff columns and quantities must share length")
    terminal = tuple(_sum((x * q for x, q in zip(row, size)), "terminal payoff") for row in matrix)
    smallest = min(terminal)
    all_nonnegative = smallest >= 0
    positive_some = any(x > 0 for x in terminal)
    benefit = None
    standard = None
    if probabilities is not None:
        p = _probabilities(probabilities, "probabilities")
        if len(p) != len(terminal):
            raise ValueError("probabilities and payoff rows must share length")
        supported = [x for x, prob in zip(terminal, p) if prob > 0]
        benefit = cost < 0 or any(x > 0 for x in supported)
        standard = cost <= 0 and min(supported) >= 0 and benefit
    return PayoffShape(terminal, smallest, cost <= 0, all_nonnegative,
                       smallest > 0, all_nonnegative and positive_some,
                       benefit, standard,
                       cost <= 0 and all_nonnegative and (cost < 0 or smallest > 0))
