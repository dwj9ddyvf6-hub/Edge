"""Independent cross-check of skills/engineer-trading-edge/scripts/research_stats.py.

Uses numpy and scipy (not needed by the skill itself) to recompute every function by a different route:
- Benjamini-Hochberg against scipy.stats.false_discovery_control;
- Newey-West as a matrix quadratic form e' W e / n^2 with Toeplitz Bartlett weights;
- PSR, MinTRL and SR0 with scipy.stats.norm, following the published reference code;
- the Wilson interval against scipy.stats.binomtest(...).proportion_ci("wilson");
- the moving-block bootstrap's standard error of a mean against its large-sample formula.
Optionally (--desk PATH) it also compares PSR, MinTRL, SR0 and BH with a second implementation of the same formulas.

Run from the repository root:  python v4/research/verify_research_stats.py [--desk PATH] [--out FILE]
"""
import argparse
import importlib.util
import json
import math
import random
import sys
from pathlib import Path

import numpy as np
from scipy import stats as ss

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "skills" / "engineer-trading-edge" / "scripts"))
import research_stats as rs  # noqa: E402

EULER = 0.5772156649015329


def nw_matrix(x, lags):
    x = np.asarray(x, float)
    n = len(x)
    e = x - x.mean()
    idx = np.arange(n)
    dist = np.abs(idx[:, None] - idx[None, :])
    w = np.where(dist <= lags, 1.0 - dist / (lags + 1.0), 0.0)
    var_mean = e @ w @ e / n ** 2
    return x.mean(), math.sqrt(var_mean)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desk", help="path to a second implementation (module with psr, min_trl, expected_max_sr, bh)")
    ap.add_argument("--out", default=str(ROOT / "v4" / "research" / "research_stats_crosscheck.json"))
    a = ap.parse_args()
    rng = random.Random(20261026)
    out = {"seed": 20261026}

    # Benjamini-Hochberg
    worst = 0.0
    agree = 0
    for _ in range(300):
        m = rng.randint(1, 60)
        p = [rng.random() ** rng.choice([1, 2, 4]) for _ in range(m)]
        mine = rs.bh_fdr(p, 0.10)
        ref = ss.false_discovery_control(p)
        worst = max(worst, float(np.max(np.abs(np.asarray(mine.adjusted) - ref))))
        agree += list(ref <= 0.10) == mine.rejected
    out["bh"] = {"sets": 300, "max_abs_adjusted_diff": worst, "rejection_sets_equal": agree}

    # Newey-West
    worst_se = 0.0
    fixed = []
    for k in range(200):
        n = rng.randint(5, 400)
        lags = rng.randint(0, min(30, n - 1))
        x = [rng.gauss(0.001, 0.02) for _ in range(n)]
        r = rs.newey_west_t(x, lags)
        mean, se = nw_matrix(x, lags)
        worst_se = max(worst_se, abs(r.se - se) / se)
    gen = random.Random(7)
    x7 = [gen.gauss(0.0005, 0.01) for _ in range(250)]
    for lags in (0, 5, 19):
        mean, se = nw_matrix(x7, lags)
        fixed.append({"series": "random.Random(7).gauss(0.0005, 0.01) x 250", "lags": lags, "mean": mean, "se": se,
                      "t": mean / se})
    out["newey_west"] = {"series": 200, "max_rel_se_diff": worst_se, "fixed_cases": fixed}

    # PSR, MinTRL, SR0 against scipy.stats.norm
    w_psr = w_trl = w_sr0 = 0.0
    for _ in range(2000):
        sr = rng.uniform(-0.3, 0.6)
        n = rng.randint(12, 3000)
        skew = rng.uniform(-3, 1)
        kurt = rng.uniform(3, 12)
        bench = rng.uniform(-0.1, 0.2)
        q = 1 - skew * sr + (kurt - 1) / 4 * sr * sr
        if q <= 0:
            continue
        ref = ss.norm.cdf((sr - bench) * math.sqrt(n - 1) / math.sqrt(q))
        w_psr = max(w_psr, abs(rs.probabilistic_sharpe(sr, n, skew, kurt, bench) - ref))
        if sr > bench:
            reft = 1 + q * (ss.norm.ppf(0.95) / (sr - bench)) ** 2
            w_trl = max(w_trl, abs(rs.min_track_record_length(sr, skew, kurt, bench) - reft) / reft)
        trials = rng.randint(2, 10 ** 6)
        var = rng.uniform(0.0001, 2)
        ref0 = math.sqrt(var) * ((1 - EULER) * ss.norm.ppf(1 - 1 / trials) + EULER * ss.norm.ppf(1 - 1 / (trials * math.e)))
        w_sr0 = max(w_sr0, abs(rs.expected_max_sharpe(var, trials) - ref0))
    out["sharpe"] = {"cases": 2000, "max_abs_psr_diff": w_psr, "max_rel_mintrl_diff": w_trl, "max_abs_sr0_diff": w_sr0}

    # Wilson interval
    wil = []
    for hits, n in ((5, 100), (0, 50), (37, 200), (200, 200), (13, 60)):
        ci = ss.binomtest(hits, n).proportion_ci(confidence_level=0.95, method="wilson")
        mine = rs.wilson_interval(hits, n)
        wil.append({"hits": hits, "n": n, "scipy": [float(ci.low), float(ci.high)], "max_abs_diff": max(abs(mine[0] - ci.low), abs(mine[1] - ci.high))})
    out["wilson"] = wil

    # Bootstrap: standard error of the mean on iid data with block 1 against s / sqrt(n)
    g = random.Random(11)
    x = [g.gauss(0, 1) for _ in range(400)]
    sd = float(np.std(x, ddof=0))
    b = rs.block_bootstrap_ci(x, block=1, n_boot=4000, seed=3)
    out["bootstrap"] = {"se_bootstrap": b.se, "se_formula": sd / math.sqrt(len(x)), "ratio": b.se / (sd / math.sqrt(len(x)))}

    if a.desk:
        spec = importlib.util.spec_from_file_location("desk_evidence", a.desk)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        d_psr = d_trl = d_sr0 = 0.0
        bh_equal = 0
        for _ in range(2000):
            sr = rng.uniform(0.01, 0.5)
            n = rng.randint(20, 3000)
            skew = rng.uniform(-2, 1)
            kurt = rng.uniform(3, 10)
            if 1 - skew * sr + (kurt - 1) / 4 * sr * sr <= 0:
                continue
            d_psr = max(d_psr, abs(rs.probabilistic_sharpe(sr, n, skew, kurt) - mod.psr(sr, n, skew, kurt)))
            d_trl = max(d_trl, abs(rs.min_track_record_length(sr, skew, kurt) - mod.min_trl(sr, skew, kurt)))
            var = rng.uniform(0.0001, 1)
            trials = rng.randint(2, 5000)
            d_sr0 = max(d_sr0, abs(rs.expected_max_sharpe(var, trials) - mod.expected_max_sr(var, trials)))
        for _ in range(300):
            p = {i: rng.random() ** 2 for i in range(rng.randint(1, 40))}
            mine = rs.bh_fdr(list(p.values()), 0.10).rejected
            bh_equal += mine == [mod.bh(p)[k] for k in p]
        out["desk_module"] = {"cases": 2000, "max_abs_psr_diff": d_psr, "max_abs_mintrl_diff": d_trl,
                              "max_abs_sr0_diff": d_sr0, "bh_sets_equal_of_300": bh_equal}

    Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
