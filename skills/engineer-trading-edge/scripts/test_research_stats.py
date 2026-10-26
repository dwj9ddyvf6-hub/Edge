"""Tests for research_stats.py.

Every expected value comes from a published worked example, a record computed independently, a hand derivation
shown in the test, or an independent implementation (numpy/scipy in v4/research/verify_research_stats.py).
"""

import contextlib
import io
import math
import random
import unittest

import research_stats as rs


def bisect_quantile(p):
    """Standard-normal quantile from math.erfc by bisection, independent of statistics.NormalDist."""
    lo, hi = -12.0, 12.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if 0.5 * math.erfc(-mid / math.sqrt(2.0)) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


class PublishedDeflatedSharpeExample(unittest.TestCase):
    """Bailey and Lopez de Prado (2014), The Deflated Sharpe Ratio, Journal of Portfolio Management 40(5).

    Numerical example: annualised SR 2.5 from 1,250 daily returns (250 a year), N = 100 trials, V[SR_n] = 1/2
    annualised, skewness -3, kurtosis 10: SR0 ~= 0.1132 (daily) and DSR = 0.9004. With N = 46, DSR = 0.9505.
    With normal returns (skewness 0, kurtosis 3), DSR = 0.9505 after N = 88.
    """

    sr = 2.5 / math.sqrt(250)
    var_sr = 0.5 / 250

    def test_sr0_and_dsr(self):
        r = rs.deflated_sharpe(self.sr, 1250, self.var_sr, 100, skew=-3, kurtosis=10)
        self.assertAlmostEqual(r.sr0, 0.1132, delta=5e-5)
        self.assertAlmostEqual(r.dsr, 0.9004, delta=5e-5)

    def test_fewer_trials(self):
        self.assertAlmostEqual(rs.deflated_sharpe(self.sr, 1250, self.var_sr, 46, -3, 10).dsr, 0.9505, delta=5e-5)

    def test_normal_returns(self):
        self.assertAlmostEqual(rs.deflated_sharpe(self.sr, 1250, self.var_sr, 88, 0, 3).dsr, 0.9505, delta=5e-5)

    def test_more_trials_deflate_more(self):
        values = [rs.deflated_sharpe(self.sr, 1250, self.var_sr, n, -3, 10).dsr for n in (2, 10, 100, 1000)]
        self.assertEqual(values, sorted(values, reverse=True))


class PublishedSharpeFrontierExamples(unittest.TestCase):
    """Bailey and Lopez de Prado (2012), The Sharpe Ratio Efficient Frontier, Journal of Risk 15(2).

    Track record of 24 monthly returns, SR 0.458, skewness -2.448, kurtosis 10.164: PSR(0) = 0.982 assuming
    normality, 0.913 with the moments, 0.953 with 36 months. MinTRL for monthly SR 2/sqrt(12) against
    1/sqrt(12), skewness -0.72, kurtosis 5.78, 95%: 59.895 months, where PSR = 0.95. IID normal returns, annual
    SR 2 against 1: 2.73 years daily, 2.83 weekly, 3.24 monthly.
    """

    def test_psr_track_record(self):
        # The paper prints SR to three decimals (0.458; its unrounded value is about 0.4578), so allow 1e-3.
        self.assertAlmostEqual(rs.probabilistic_sharpe(0.458, 24), 0.982, delta=1e-3)
        self.assertAlmostEqual(rs.probabilistic_sharpe(0.458, 24, -2.448, 10.164), 0.913, delta=1e-3)
        self.assertAlmostEqual(rs.probabilistic_sharpe(0.458, 36, -2.448, 10.164), 0.953, delta=1e-3)

    def test_min_track_record_length(self):
        sr, bench = 2 / math.sqrt(12), 1 / math.sqrt(12)
        months = rs.min_track_record_length(sr, -0.72, 5.78, bench)
        self.assertAlmostEqual(months, 59.895, delta=5e-4)
        self.assertAlmostEqual(rs.probabilistic_sharpe(sr, months, -0.72, 5.78, bench), 0.95, places=9)

    def test_normal_frequency_table(self):
        for periods, years in ((252, 2.73), (52, 2.83), (12, 3.24)):
            got = rs.min_track_record_length(2 / math.sqrt(periods), sr_benchmark=1 / math.sqrt(periods)) / periods
            self.assertAlmostEqual(got, years, delta=5e-3)

    def test_no_track_record_proves_a_lower_sharpe(self):
        self.assertEqual(rs.min_track_record_length(0.1, sr_benchmark=0.1), math.inf)


class DeskRecordCrossCheck(unittest.TestCase):
    """The desk's research record of 2026-10-16 computed these for ~550 forward-tested sleeves (daily, 252 a year,
    normal returns, 95%): MinTRL 10.8 / 2.7 / 1.2 / 0.7 years for annual SR 0.5 / 1 / 1.5 / 2, an expected-maximum
    multiplier of 3.08 for N = 550, and a best skill-less annual SR of about 3.1, 2.2 and 1.8 after 1, 2, 3 years."""

    def test_min_trl_table(self):
        for annual, years in ((0.5, 10.8), (1.0, 2.7), (1.5, 1.2), (2.0, 0.7)):
            got = rs.min_track_record_length(annual / math.sqrt(252)) / 252
            self.assertAlmostEqual(got, years, delta=0.05)

    def test_best_of_550_skill_less_sleeves(self):
        multiplier = rs.expected_max_sharpe(1.0, 550)
        self.assertAlmostEqual(multiplier, 3.08, delta=0.005)
        for years, best in ((1, 3.1), (2, 2.2), (3, 1.8)):
            self.assertAlmostEqual(multiplier / math.sqrt(years), best, delta=0.05)


class ExpectedMaximumBySimulation(unittest.TestCase):
    def test_matches_monte_carlo(self):
        # Independent computation: the mean maximum of N standard normals, simulated.
        rng = random.Random(42)
        n_trials, reps = 100, 3000
        mean_max = sum(max(rng.gauss(0, 1) for _ in range(n_trials)) for _ in range(reps)) / reps
        # The paper reports the analytic value overstates the simulated one by less than 0.05 for small N.
        self.assertLess(abs(rs.expected_max_sharpe(1.0, n_trials) - mean_max), 0.05)

    def test_single_trial_has_no_selection(self):
        self.assertEqual(rs.expected_max_sharpe(1.0, 1), 0.0)


class BenjaminiHochberg(unittest.TestCase):
    # Benjamini and Hochberg (1995), JRSS B 57(1): 15 p-values from a thrombolysis trial; at q = 0.05 the step-up
    # rejects 4 (Bonferroni rejects 3). Adjusted values as published in scipy's documentation of the example.
    ps = [0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0459, 0.3240, 0.4262, 0.5719, 0.6528,
          0.7590, 1.000]
    adjusted = [0.0015, 0.003, 0.0095, 0.035625, 0.0603, 0.06385714, 0.06385714, 0.0645, 0.0765, 0.486, 0.58118182,
                0.714875, 0.75323077, 0.81321429, 1.0]

    def test_published_example(self):
        r = rs.bh_fdr(self.ps, q=0.05)
        self.assertEqual(r.n_rejected, 4)
        self.assertEqual(r.rejected, [True] * 4 + [False] * 11)
        for got, want in zip(r.adjusted, self.adjusted):
            self.assertAlmostEqual(got, want, places=7)

    def test_input_order_is_preserved(self):
        r = rs.bh_fdr([0.5, 0.6, 0.1, 0.001], q=0.05)
        for got, want in zip(r.adjusted, [0.6, 0.6, 0.2, 0.004]):
            self.assertAlmostEqual(got, want, places=12)
        self.assertEqual(r.rejected, [False, False, False, True])

    def test_hand_example_step_up(self):
        # Sorted 0.01, 0.03, 0.04, 0.2 against k q / m = 0.025, 0.05, 0.075, 0.1: the largest passing rank is 3.
        r = rs.bh_fdr([0.04, 0.2, 0.01, 0.03], q=0.10)
        self.assertEqual(r.rejected, [True, False, True, True])

    def test_edges(self):
        self.assertEqual(rs.bh_fdr([]).n_rejected, 0)
        self.assertEqual(rs.bh_fdr([1.0, 1.0]).rejected, [False, False])
        with self.assertRaises(ValueError):
            rs.bh_fdr([1.2])


class NeweyWest(unittest.TestCase):
    def test_hand_example(self):
        # x = 1, 2, 3, 4: deviations -1.5, -0.5, 0.5, 1.5; g0 = 5 / 4 = 1.25; g1 = 1.25 / 4 = 0.3125.
        # Lag 1 (weight 1/2): S = 1.25 + 2 * 0.5 * 0.3125 = 1.5625; se = sqrt(1.5625 / 4) = 0.625; t = 4.
        r = rs.newey_west_t([1, 2, 3, 4], lags=1)
        self.assertAlmostEqual(r.mean, 2.5, places=12)
        self.assertAlmostEqual(r.se, 0.625, places=12)
        self.assertAlmostEqual(r.t, 4.0, places=12)
        # Lag 0: se = sqrt(1.25 / 4).
        self.assertAlmostEqual(rs.newey_west_t([1, 2, 3, 4], lags=0).se, math.sqrt(1.25 / 4), places=12)

    def test_matches_matrix_form(self):
        # Values from v4/research/verify_research_stats.py: e' W e / n^2 with numpy, Toeplitz Bartlett weights.
        gen = random.Random(7)
        x = [gen.gauss(0.0005, 0.01) for _ in range(250)]
        expected = {0: 0.0006440180944688094, 5: 0.0006158055829998652, 19: 0.00047686286965058076}
        for lags, se in expected.items():
            self.assertAlmostEqual(rs.newey_west_t(x, lags).se, se, delta=1e-15)

    def test_constant_series(self):
        r = rs.newey_west_t([0.01] * 10, lags=2)
        self.assertEqual(r.se, 0.0)
        self.assertEqual(r.t, math.inf)

    def test_rejects_bad_lags(self):
        with self.assertRaises(ValueError):
            rs.newey_west_t([1, 2, 3], lags=-1)


class RandomWalkNull(unittest.TestCase):
    """The harness on a known mistake: a plain t-test on overlapping 20-period returns of random walks."""

    @staticmethod
    def plain_t(r):
        n = len(r)
        m = sum(r) / n
        sd = math.sqrt(sum((v - m) ** 2 for v in r) / (n - 1))
        return m / (sd / math.sqrt(n))

    def test_overlap_inflates_false_positives(self):
        naive = rs.random_walk_null(lambda p: abs(self.plain_t(rs.overlapping_returns(p, 20))) > 1.96,
                                    n_paths=200, n_steps=500, seed=1)
        hac = rs.random_walk_null(lambda p: abs(rs.newey_west_t(rs.overlapping_returns(p, 20), 19).t) > 1.96,
                                  n_paths=200, n_steps=500, seed=1)
        disjoint = rs.random_walk_null(lambda p: abs(self.plain_t(rs.overlapping_returns(p, 20)[::20])) > 1.96,
                                       n_paths=200, n_steps=500, seed=1)
        self.assertGreater(naive.rate, 0.40)  # nominal 5%
        self.assertLess(hac.rate, naive.rate)
        self.assertLess(hac.rate, 0.25)
        self.assertLess(disjoint.rate, 0.12)

    def test_trivial_tests(self):
        self.assertEqual(rs.random_walk_null(lambda p: False, n_paths=20, n_steps=10).rate, 0.0)
        self.assertEqual(rs.random_walk_null(lambda p: True, n_paths=20, n_steps=10).rate, 1.0)

    def test_wilson_matches_scipy(self):
        # scipy.stats.binomtest(k, n).proportion_ci(method="wilson"), from v4/research/verify_research_stats.py.
        for hits, n, low, high in ((5, 100, 0.021543679154367973, 0.11175046923191914),
                                   (37, 200, 0.13730192800616045, 0.24457062761151752),
                                   (0, 50, 0.0, 0.07134759913335872)):
            got = rs.wilson_interval(hits, n)
            self.assertAlmostEqual(got[0], low, places=12)
            self.assertAlmostEqual(got[1], high, places=12)


class BlockBootstrap(unittest.TestCase):
    def test_constant_series(self):
        r = rs.block_bootstrap_ci([0.02] * 50, block=5, n_boot=200)
        self.assertAlmostEqual(r.low, 0.02, places=12)
        self.assertAlmostEqual(r.high, 0.02, places=12)

    def test_iid_standard_error(self):
        # Independent formula: the standard error of a mean of iid data is sd / sqrt(n).
        g = random.Random(11)
        x = [g.gauss(0, 1) for _ in range(400)]
        m = sum(x) / len(x)
        sd = math.sqrt(sum((v - m) ** 2 for v in x) / len(x))
        r = rs.block_bootstrap_ci(x, block=1, n_boot=4000, seed=3)
        self.assertLess(abs(r.se / (sd / math.sqrt(len(x))) - 1.0), 0.06)

    def test_blocks_widen_the_interval_under_autocorrelation(self):
        g = random.Random(5)
        x, prev = [], 0.0
        for _ in range(600):
            prev = 0.8 * prev + g.gauss(0, 1)
            x.append(prev)
        iid = rs.block_bootstrap_ci(x, block=1, n_boot=1500, seed=1)
        moving = rs.block_bootstrap_ci(x, block=30, n_boot=1500, seed=1)
        stationary = rs.block_bootstrap_ci(x, block=30, n_boot=1500, seed=1, kind="stationary")
        self.assertGreater(moving.high - moving.low, 1.8 * (iid.high - iid.low))
        self.assertGreater(stationary.high - stationary.low, 1.8 * (iid.high - iid.low))

    def test_reproducible(self):
        x = [math.sin(i) for i in range(100)]
        self.assertEqual(rs.block_bootstrap_ci(x, 5, seed=9), rs.block_bootstrap_ci(x, 5, seed=9))


class Power(unittest.TestCase):
    def test_closed_form_with_independent_quantiles(self):
        z = bisect_quantile(0.975) + bisect_quantile(0.80)
        self.assertAlmostEqual(rs.min_detectable_effect(1.0, 100), z / 10.0, places=9)
        z1 = bisect_quantile(0.95) + bisect_quantile(0.90)
        self.assertAlmostEqual(rs.min_detectable_effect(2.0, 64, power=0.90, two_sided=False), z1 * 2.0 / 8.0,
                               places=9)

    def test_simulated_power(self):
        # Independent check: a true effect equal to the MDE is detected about 80% of the time.
        n, sd = 50, 1.0
        effect = rs.min_detectable_effect(sd, n)
        rng = random.Random(3)
        hits = 0
        reps = 4000
        for _ in range(reps):
            m = sum(rng.gauss(effect, sd) for _ in range(n)) / n
            hits += abs(m / (sd / math.sqrt(n))) > 1.959963984540054
        self.assertLess(abs(hits / reps - 0.80), 0.03)

    def test_required_n_inverts_mde(self):
        n = rs.required_n(rs.min_detectable_effect(0.05, 300), 0.05)
        self.assertAlmostEqual(n, 300.0, places=6)


class Quantiles(unittest.TestCase):
    def test_normal_quantile_is_independent_of_implementation(self):
        for p in (0.6, 0.8, 0.95, 0.975, 0.999, 1 - 1 / 550):
            self.assertAlmostEqual(rs.norm_ppf(p), bisect_quantile(p), places=9)


class CommandLine(unittest.TestCase):
    def test_runs(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(rs._main(["emax", "--trials", "100"]), 0)
            self.assertEqual(rs._main(["bh", "--q", "0.1", "0.01", "0.2"]), 0)
        self.assertIn("1 of 2 rejected", out.getvalue())


if __name__ == "__main__":
    unittest.main()
