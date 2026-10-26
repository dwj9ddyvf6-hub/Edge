"""Research statistics for strategy work, standard library only.

Calculators for supplied numbers: multiple testing, dependence-aware t-statistics, Sharpe-ratio inference, power and
null calibration. None of them estimates a market fact by itself.

Ported from the desk's own statistics module where it already did the job (probabilistic and deflated Sharpe ratio,
minimum track record length, Benjamini-Hochberg) and extended with Newey-West, block bootstrap, minimum detectable
effect and a random-walk null harness.

Conventions
- Sharpe ratios are per period (daily SR for daily returns). Annualise outside: SR_ann = SR * sqrt(periods a year).
- Kurtosis is raw (a normal distribution has 3), as in Bailey and Lopez de Prado.
- n counts observations; for power, count independent observations (non-overlapping windows, event clusters).

Command line (examples):
    python research_stats.py dsr --sr 0.1581 --n 1250 --skew -3 --kurt 10 --var-sr 0.002 --trials 100
    python research_stats.py mintrl --sr 0.5774 --benchmark 0.2887 --skew -0.72 --kurt 5.78
    python research_stats.py emax --trials 16500000
    python research_stats.py mde --sd 0.08 --n 40
    python research_stats.py bh --q 0.10 0.001 0.02 0.04 0.3
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass
from math import fsum
from statistics import NormalDist
from typing import Callable, List, Optional, Sequence

EULER_GAMMA = 0.5772156649015329
_NORMAL = NormalDist()


def norm_cdf(x: float) -> float:
    return _NORMAL.cdf(x)


def norm_ppf(p: float) -> float:
    if not 0.0 < p < 1.0:
        raise ValueError("probability must be strictly between 0 and 1")
    return _NORMAL.inv_cdf(p)


# ---------------------------------------------------------------------------------------------------------------
# Multiple testing


@dataclass(frozen=True)
class BHResult:
    rejected: List[bool]
    adjusted: List[float]
    n_rejected: int
    q: float


def bh_fdr(pvalues: Sequence[float], q: float = 0.10) -> BHResult:
    """Benjamini-Hochberg step-up at false-discovery rate q.

    Rejects the k smallest p-values, where k is the largest rank with p_(k) <= k q / m. Returns rejections and
    BH-adjusted p-values, both in input order. Valid under independence or positive dependence; for arbitrary
    dependence divide q by the harmonic number H_m (Benjamini-Yekutieli).
    """
    if not 0.0 < q < 1.0:
        raise ValueError("q must be strictly between 0 and 1")
    m = len(pvalues)
    for p in pvalues:
        if not (0.0 <= p <= 1.0) or math.isnan(p):
            raise ValueError("p-values must lie in [0, 1]")
    if m == 0:
        return BHResult([], [], 0, q)
    order = sorted(range(m), key=lambda i: pvalues[i])
    k = 0
    for rank, i in enumerate(order, 1):
        if pvalues[i] <= rank * q / m:
            k = rank
    rejected = [False] * m
    for rank, i in enumerate(order, 1):
        rejected[i] = rank <= k
    adjusted = [0.0] * m
    running = 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        running = min(running, pvalues[i] * m / rank)
        adjusted[i] = running
    return BHResult(rejected, adjusted, k, q)


# ---------------------------------------------------------------------------------------------------------------
# Dependence


@dataclass(frozen=True)
class MeanTest:
    mean: float
    se: float
    t: float
    p_two_sided: float
    lags: int
    n: int


def newey_west_t(x: Sequence[float], lags: int, mu0: float = 0.0) -> MeanTest:
    """t-statistic for the mean of x with a Newey-West (Bartlett-weighted) long-run variance.

    S = g0 + 2 * sum_{l=1..L} (1 - l / (L + 1)) g_l, with g_l = (1/n) sum_t (x_t - xbar)(x_{t-l} - xbar), and
    se = sqrt(S / n). For h-period returns sampled every period (overlapping windows) use lags >= h - 1; the desk
    used lag = h. The p-value is a normal approximation, optimistic in short samples with persistent regressors.
    """
    n = len(x)
    if n < 2:
        raise ValueError("need at least two observations")
    if lags < 0 or int(lags) != lags:
        raise ValueError("lags must be a non-negative integer")
    lags = min(int(lags), n - 1)
    mean = fsum(x) / n
    d = [v - mean for v in x]
    s = fsum(v * v for v in d) / n
    for lag in range(1, lags + 1):
        weight = 1.0 - lag / (lags + 1.0)
        s += 2.0 * weight * fsum(d[t] * d[t - lag] for t in range(lag, n)) / n
    s = max(s, 0.0)
    se = math.sqrt(s / n)
    diff = mean - mu0
    if se == 0.0:
        t = 0.0 if diff == 0.0 else math.copysign(math.inf, diff)
    else:
        t = diff / se
    p = 2.0 * (1.0 - norm_cdf(abs(t))) if math.isfinite(t) else 0.0
    return MeanTest(mean, se, t, p, lags, n)


def overlapping_returns(prices: Sequence[float], horizon: int) -> List[float]:
    """Log returns over `horizon` periods, one per period (consecutive windows overlap by horizon - 1)."""
    if horizon < 1:
        raise ValueError("horizon must be at least 1")
    return [math.log(prices[i + horizon] / prices[i]) for i in range(len(prices) - horizon)]


@dataclass(frozen=True)
class BootstrapResult:
    estimate: float
    low: float
    high: float
    se: float
    n_boot: int
    block: int
    kind: str


def _quantile(sorted_values: Sequence[float], prob: float) -> float:
    """Linear interpolation between order statistics (position prob * (n - 1))."""
    n = len(sorted_values)
    pos = prob * (n - 1)
    lo = int(math.floor(pos))
    hi = min(lo + 1, n - 1)
    frac = pos - lo
    return sorted_values[lo] * (1.0 - frac) + sorted_values[hi] * frac


def block_bootstrap_ci(x: Sequence[float], block: int, stat: Optional[Callable[[Sequence[float]], float]] = None,
                       n_boot: int = 2000, alpha: float = 0.05, seed: int = 0,
                       kind: str = "moving") -> BootstrapResult:
    """Percentile confidence interval for stat(x) that keeps serial dependence inside blocks.

    kind="moving": blocks of fixed length start uniformly in [0, n - block] (Kuensch). kind="stationary": blocks of
    geometric length with mean `block`, wrapped circularly (Politis and Romano). Choose the block from the
    dependence horizon (for example the holding period); try neighbouring lengths, because the interval depends on it.
    """
    n = len(x)
    if n < 2:
        raise ValueError("need at least two observations")
    if not 1 <= block <= n:
        raise ValueError("block must be between 1 and len(x)")
    if not 0.0 < alpha < 1.0 or n_boot < 10:
        raise ValueError("need 0 < alpha < 1 and n_boot >= 10")
    if kind not in ("moving", "stationary"):
        raise ValueError("kind must be 'moving' or 'stationary'")
    stat = stat or (lambda v: fsum(v) / len(v))
    rng = random.Random(seed)
    values = list(x)
    stats = []
    for _ in range(n_boot):
        sample: List[float] = []
        if kind == "moving":
            while len(sample) < n:
                start = rng.randrange(0, n - block + 1)
                sample.extend(values[start:start + block])
        else:
            p_new = 1.0 / block
            pos = rng.randrange(n)
            while len(sample) < n:
                sample.append(values[pos])
                pos = rng.randrange(n) if rng.random() < p_new else (pos + 1) % n
        stats.append(stat(sample[:n]))
    stats.sort()
    mean_b = fsum(stats) / n_boot
    se = math.sqrt(fsum((s - mean_b) ** 2 for s in stats) / (n_boot - 1))
    return BootstrapResult(stat(values), _quantile(stats, alpha / 2.0), _quantile(stats, 1.0 - alpha / 2.0), se,
                           n_boot, block, kind)


# ---------------------------------------------------------------------------------------------------------------
# Sharpe-ratio inference (Bailey and Lopez de Prado)


def _sr_variance_factor(sr: float, skew: float, kurtosis: float) -> float:
    return 1.0 - skew * sr + (kurtosis - 1.0) / 4.0 * sr * sr


def probabilistic_sharpe(sr: float, n: float, skew: float = 0.0, kurtosis: float = 3.0,
                         sr_benchmark: float = 0.0) -> float:
    """PSR(SR*) = Phi((SR - SR*) sqrt(n - 1) / sqrt(1 - skew SR + (kurtosis - 1)/4 SR^2)).

    The probability that the true per-period Sharpe ratio exceeds sr_benchmark, given n returns with the stated
    skewness and raw kurtosis. Assumes independent returns; serial correlation needs an adjusted SR first.
    """
    if n <= 1:
        raise ValueError("need more than one return")
    factor = _sr_variance_factor(sr, skew, kurtosis)
    if factor <= 0.0:
        raise ValueError("moments imply a non-positive variance for the Sharpe estimate")
    return norm_cdf((sr - sr_benchmark) * math.sqrt(n - 1.0) / math.sqrt(factor))


def expected_max_sharpe(var_sr: float, n_trials: float) -> float:
    """SR0: the expected maximum Sharpe ratio among n_trials skill-less trials with cross-trial variance var_sr.

    SR0 = sqrt(var_sr) ((1 - gamma) Phi^-1(1 - 1/N) + gamma Phi^-1(1 - 1/(N e))). With var_sr = 1 it is the
    expected best z-score of N independent null tests. N is the number of independent trials; correlated variants
    count for fewer.
    """
    if var_sr < 0.0:
        raise ValueError("var_sr must be non-negative")
    if n_trials < 1:
        raise ValueError("n_trials must be at least 1")
    if n_trials == 1 or var_sr == 0.0:
        return 0.0
    z = (1.0 - EULER_GAMMA) * norm_ppf(1.0 - 1.0 / n_trials) + EULER_GAMMA * norm_ppf(
        1.0 - 1.0 / (n_trials * math.e))
    return math.sqrt(var_sr) * z


@dataclass(frozen=True)
class DeflatedSharpe:
    dsr: float
    sr0: float
    psr0: float


def deflated_sharpe(sr: float, n: float, var_sr: float, n_trials: float, skew: float = 0.0,
                    kurtosis: float = 3.0) -> DeflatedSharpe:
    """DSR = PSR(SR0): the PSR of the selected strategy against the best that n_trials skill-less trials would show.

    Use the selected strategy's own n, skew and kurtosis, and the variance of the per-period Sharpe ratios across
    all trials. A DSR below 0.95 means the selection alone can explain the result at 95% confidence.
    """
    sr0 = expected_max_sharpe(var_sr, n_trials)
    return DeflatedSharpe(probabilistic_sharpe(sr, n, skew, kurtosis, sr0), sr0,
                          probabilistic_sharpe(sr, n, skew, kurtosis, 0.0))


def min_track_record_length(sr: float, skew: float = 0.0, kurtosis: float = 3.0, sr_benchmark: float = 0.0,
                            confidence: float = 0.95) -> float:
    """MinTRL = 1 + (1 - skew SR + (kurtosis - 1)/4 SR^2) (z_conf / (SR - SR*))^2, in periods.

    The number of returns needed before SR > SR* holds at the given confidence. Returns math.inf when SR <= SR*.
    """
    if sr <= sr_benchmark:
        return math.inf
    factor = _sr_variance_factor(sr, skew, kurtosis)
    if factor <= 0.0:
        raise ValueError("moments imply a non-positive variance for the Sharpe estimate")
    return 1.0 + factor * (norm_ppf(confidence) / (sr - sr_benchmark)) ** 2


# ---------------------------------------------------------------------------------------------------------------
# Power


def min_detectable_effect(sd: float, n: float, alpha: float = 0.05, power: float = 0.80,
                          two_sided: bool = True) -> float:
    """Smallest true mean effect a z-test detects with the given power: (z_{1-a} + z_power) sd / sqrt(n).

    n is the number of independent observations (non-overlapping windows, sessions or event clusters). A null
    result is evidence of absence only for effects above this size; below it the result is INCONCLUSIVE.
    """
    if sd < 0.0 or n <= 0:
        raise ValueError("need sd >= 0 and n > 0")
    z_alpha = norm_ppf(1.0 - alpha / 2.0) if two_sided else norm_ppf(1.0 - alpha)
    return (z_alpha + norm_ppf(power)) * sd / math.sqrt(n)


def required_n(effect: float, sd: float, alpha: float = 0.05, power: float = 0.80, two_sided: bool = True) -> float:
    """Independent observations needed to detect `effect` with the given power (inverse of min_detectable_effect)."""
    if effect == 0.0:
        return math.inf
    z_alpha = norm_ppf(1.0 - alpha / 2.0) if two_sided else norm_ppf(1.0 - alpha)
    return ((z_alpha + norm_ppf(power)) * sd / abs(effect)) ** 2


# ---------------------------------------------------------------------------------------------------------------
# Null calibration


@dataclass(frozen=True)
class NullResult:
    rate: float
    hits: int
    n_paths: int
    ci_low: float
    ci_high: float


def wilson_interval(hits: int, n: int, confidence: float = 0.95) -> tuple:
    """Wilson score interval for a binomial proportion."""
    if n <= 0 or not 0 <= hits <= n:
        raise ValueError("need n > 0 and 0 <= hits <= n")
    z = norm_ppf(0.5 + confidence / 2.0)
    phat = hits / n
    denom = 1.0 + z * z / n
    centre = (phat + z * z / (2.0 * n)) / denom
    half = z * math.sqrt(phat * (1.0 - phat) / n + z * z / (4.0 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


def gaussian_random_walk(rng: random.Random, n_steps: int, start: float = 100.0, step_sd: float = 0.01,
                         drift: float = 0.0) -> List[float]:
    """A geometric random walk: log price increments are iid normal. It has no edge by construction."""
    prices = [start]
    log_p = math.log(start)
    for _ in range(n_steps):
        log_p += drift + step_sd * rng.gauss(0.0, 1.0)
        prices.append(math.exp(log_p))
    return prices


def random_walk_null(test: Callable[[List[float]], bool], n_paths: int = 200, n_steps: int = 500, seed: int = 0,
                     generator: Optional[Callable[[random.Random, int], List[float]]] = None) -> NullResult:
    """Run `test` on simulated price paths with no edge and report how often it fires (its false-positive rate).

    Run the whole pipeline (features, selection, test) on the null before trusting it on real data. If the rate is
    far above the nominal level, the pipeline, not the market, produced the finding. `generator(rng, n_steps)` can
    supply a different null (for example block-resampled real returns); the default is gaussian_random_walk.
    """
    if n_paths < 1 or n_steps < 2:
        raise ValueError("need n_paths >= 1 and n_steps >= 2")
    rng = random.Random(seed)
    make = generator or gaussian_random_walk
    hits = sum(1 for _ in range(n_paths) if test(make(rng, n_steps)))
    low, high = wilson_interval(hits, n_paths)
    return NullResult(hits / n_paths, hits, n_paths, low, high)


# ---------------------------------------------------------------------------------------------------------------
# Command line


def _main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("dsr", help="deflated Sharpe ratio")
    for name in ("--sr", "--n", "--var-sr", "--trials"):
        p.add_argument(name, type=float, required=True)
    p.add_argument("--skew", type=float, default=0.0)
    p.add_argument("--kurt", type=float, default=3.0)
    p = sub.add_parser("psr", help="probabilistic Sharpe ratio")
    p.add_argument("--sr", type=float, required=True)
    p.add_argument("--n", type=float, required=True)
    p.add_argument("--skew", type=float, default=0.0)
    p.add_argument("--kurt", type=float, default=3.0)
    p.add_argument("--benchmark", type=float, default=0.0)
    p = sub.add_parser("mintrl", help="minimum track record length, in periods")
    p.add_argument("--sr", type=float, required=True)
    p.add_argument("--skew", type=float, default=0.0)
    p.add_argument("--kurt", type=float, default=3.0)
    p.add_argument("--benchmark", type=float, default=0.0)
    p.add_argument("--confidence", type=float, default=0.95)
    p = sub.add_parser("emax", help="expected maximum Sharpe (or z with --var-sr 1) of N null trials")
    p.add_argument("--trials", type=float, required=True)
    p.add_argument("--var-sr", type=float, default=1.0)
    p = sub.add_parser("mde", help="minimum detectable effect")
    p.add_argument("--sd", type=float, required=True)
    p.add_argument("--n", type=float, required=True)
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.80)
    p.add_argument("--one-sided", action="store_true")
    p = sub.add_parser("bh", help="Benjamini-Hochberg")
    p.add_argument("--q", type=float, default=0.10)
    p.add_argument("pvalues", type=float, nargs="+")
    a = parser.parse_args(argv)
    if a.cmd == "dsr":
        r = deflated_sharpe(a.sr, a.n, a.var_sr, a.trials, a.skew, a.kurt)
        print(f"SR0 {r.sr0:.6f}  DSR {r.dsr:.6f}  PSR(0) {r.psr0:.6f}")
    elif a.cmd == "psr":
        print(f"PSR {probabilistic_sharpe(a.sr, a.n, a.skew, a.kurt, a.benchmark):.6f}")
    elif a.cmd == "mintrl":
        print(f"MinTRL {min_track_record_length(a.sr, a.skew, a.kurt, a.benchmark, a.confidence):.4f} periods")
    elif a.cmd == "emax":
        print(f"expected maximum {expected_max_sharpe(a.var_sr, a.trials):.6f}")
    elif a.cmd == "mde":
        print(f"MDE {min_detectable_effect(a.sd, a.n, a.alpha, a.power, not a.one_sided):.6f}")
    else:
        r = bh_fdr(a.pvalues, a.q)
        for p_val, rej, adj in zip(a.pvalues, r.rejected, r.adjusted):
            print(f"p {p_val:<10g} adjusted {adj:<10.6g} {'REJECT' if rej else 'keep'}")
        print(f"{r.n_rejected} of {len(a.pvalues)} rejected at q = {r.q}")
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
