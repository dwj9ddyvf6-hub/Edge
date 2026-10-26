# Research protocol: how the desk tested edges

The protocol behind the [field casebook](field-casebook.md). Each rule exists because a study broke without it.
Calculators: `scripts/research_stats.py`. Templates: [preregistration](../assets/preregistration.md),
[shadow experiment](../assets/shadow-experiment.md).

## Contents

1. Register before any number
2. Eras and the holdout
3. The comparison
4. Multiple testing
5. Dependence
6. Null dry runs
7. Power: when a null means nothing
8. The universe
9. Verdicts
10. The forward registry
11. Paired shadow experiments

## 1. Register before any number

- Write the hypothesis, data, outcome, comparison, test and decision rule before computing anything about them.
- Time-stamp every change as an addendum: "registered at <time>, before any number of X exists".
- Freeze code and tables by hash before the holdout is scored; score the holdout once.
- When a registered rule cannot be followed (it is unbuildable, or a registered market does not exist), register the
  smallest amendment before seeing the number it decides, and say why.
- Report choices made after seeing a result as such. A holdout that informed any design choice is no longer out of
  sample for what that choice built: label its numbers SEEN and judge the build forward.

## 2. Eras and the holdout

- Discovery and holdout eras in calendar order (the desk used 2016–2022 and 2023–2026), with a purge gap at least as
  long as the outcome horizon.
- Fit preprocessing, thresholds, selection and calibration inside the discovery era only.
- A fitted composite is judged walk-forward (fit through year Y−1, score year Y) and then forward.
- Results that hold in only one era are era-bound until shown otherwise
  ([C12](field-casebook.md#c12-edges-are-era-bound)).

## 3. The comparison

- Compare against what the price already knows. For stock signals the desk compared each event with equally volatile
  names (same ATR% quintile, session and size tier); against plain averages, volatility alone passes everything.
- Then test against the stock's own volatility history (a HAR model of 1-, 5- and 22-session realized volatility):
  41% of the desk's volatility "foresight" claims did not survive it
  ([C01](field-casebook.md#c01-volatility-is-the-most-predictable-thing-on-a-chart)).
- Robustness lenses the desk ran: fine re-matching on the ten most similar names, counting each company once,
  removing duplicate tickers, factor-neutral (momentum, recent return, size), bear-market windows, and timing from the
  next open instead of the signal close.
- Measured from the next open, many 1–5 session effects disappear: of 375 edges that peaked at 1–5 sessions close to
  close, 194 still did from the next open. A desk acts at the next open; score from there.

## 4. Multiple testing

- Count every trial: variants, filters, thresholds, horizons, tiers, discarded ideas, LLM-generated candidates.
- Control the false-discovery rate across the registered family with Benjamini–Hochberg (`bh_fdr`), q = 0.10 in the
  desk's rule. Under arbitrary dependence divide q by the harmonic number of the family size.
- Deflate a selected strategy's Sharpe ratio by the number of independent trials (`deflated_sharpe`). The best of
  550 skill-less sleeves shows an annual Sharpe ratio of about 3.1 after one year (desk research record,
  2026-10-16); the best of 16.5 million null trials shows a z-score of about 5.4
  ([C15](field-casebook.md#c15-the-165-million-filter-rule)).
- The desk's CONFIRMED rule: discovery |t| ≥ 3, holdout the same sign with |t| ≥ 2, and BH q < 0.10 within the family.

## 5. Dependence

- Overlapping outcomes are not independent. For h-period returns sampled every period use Newey–West errors with at
  least h − 1 lags (`newey_west_t`); the desk used lag h, and lag 8 when sampling every fifth session with 20-session
  outcomes.
- Newey–West is still optimistic with few independent windows. On simulated random walks, a 5% test on overlapping
  20-period returns fired 67.5% of the time with plain errors, 11.5% with Newey–West, and 5.0% on non-overlapping
  windows (200 paths of 500 steps; `test_research_stats.py`). Report the count of non-overlapping windows.
- Resample in blocks (`block_bootstrap_ci`) or by session, and cluster by company: several desk effects were strong by
  session and vanished by company, because a few repeat names carried them
  ([C14](field-casebook.md#c14-reverse-splits-check-the-composition)).

## 6. Null dry runs

- Run the whole pipeline (features, selection, test, verdict) on data with no edge before trusting it on real data
  (`random_walk_null`). The desk's positioning study produced 52 large discovery t's on real data and 53 on random
  walks ([C05](field-casebook.md#c05-widely-watched-public-data-is-in-the-price)).
- Validate the null itself. The desk found nulls that were wrong (desk research record, 2026-10-20, method audit):
  - a block-shuffle null that kept each name's drift passed 21–67% of settings;
  - a session-mean comparison rejected 25–43% of random-date draws;
  - "chance" estimated as found × 2.5% understated the measured false-positive rate of 7–10% on persistent series.
- A reader or indicator that fires as often on random walks as on real prices adds nothing; the desk did not ship one
  that fired on 14.0% of random walks against 7.9% of real names.

## 7. Power: when a null means nothing

- State the minimum detectable effect for every test (`min_detectable_effect`, `required_n`), counting independent
  observations.
- A null below the detectable size is INCONCLUSIVE. Examples from the desk: the positioning study could pass only
  correlations above about 0.31–0.34; 160 charts from one 11-week regime could detect only an IC of about 0.20;
  confirming an IC of 0.05 at 80% power needs about 2,600 forward charts.
- Write "ruled out above X" for a powered null, never "no effect".

## 8. The universe

- Point in time: every value at session d from data dated d or earlier, proven by recomputing on truncated data.
- Keep delisted names. The desk's vendor universe dropped names delisted to over-the-counter trading; that
  understates avoid edges and can overstate buy edges.
- Cover every size tier, micro and nano included: most confirmed edges lived there
  ([C03](field-casebook.md#c03-chartslector-warnings-work-in-thin-markets-buy-rules-do-not)).
- Audit lineage for columns that exist only for today's survivors, recycled tickers, duplicate tickers, corrupted bars
  and adjustment errors ([C13](field-casebook.md#c13-point-in-time-the-leak-and-the-volume-flaw)).

## 9. Verdicts

| Verdict | Meaning |
|---|---|
| CONFIRMED | The registered test passed, in every required era, after multiple-testing control |
| NULL | No effect above the stated detectable size |
| REJECTED | The registered test failed, or the effect has the wrong sign |
| INCONCLUSIVE | The test cannot decide: underpowered, not yet run forward, or broken |

Evidence stages advance HYPOTHESIS → RETROSPECTIVE → OUT-OF-SAMPLE → FORWARD SIMULATION → LIMITED LIVE. A verdict
names the stage it reached.

## 10. The forward registry

- Ideas found after a holdout was seen cannot be confirmed by the past. Fix each rule, its data and its code by hash,
  and judge it only on sessions after the freeze.
- Give each rule its statistic, its minimum sample and its pass condition before the first scored date.
- Report counts only until the minimum sample exists; append scores with the date and sample; never re-cut a rule
  after its numbers.

## 11. Paired shadow experiments

- The incumbent keeps trading. Each candidate runs as a counterfactual arm on the same signals, the same capital and
  the desk's real fills, beside a seeded placebo.
- Each arm states what changes, what stays the same, the expected result if the idea is right, a rival explanation,
  a rejection rule and the minimum sample before review. It stays descriptive until the sample exists, and says so.
- A test asserts that the live sleeves' intents and orders are identical with the arm present.
- Example rule (desk research record, 2026-10-26, opening-print arm): rejected if, over at least 200 paired entries,
  the mean saving net of a 2 bps auction cost is under 5 bps.
- Promotion needs the evidence and the owner's approval; a demonstrated defect is fixed directly, with tests.
