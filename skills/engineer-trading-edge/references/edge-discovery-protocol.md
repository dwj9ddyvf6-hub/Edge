# Edge discovery protocol: from "who is forced to trade" to a scored, shadow-tested potential edge

This reference is the executable protocol for hunting **new market edge in price and calendar data**: what to do first,
in what order, with which formulas, thresholds and records. It distils the research rounds one desk ran from 13 to 15
November 2026 (more than two million trials across ETFs, futures, single stocks, intraday bars and modelled options,
plus 32.5 million scored condition combinations) and a measured comparison of the practices behind 69 find
clusters against 99 dead ends.

It is the companion of [edge-find-methods.md](edge-find-methods.md). That file covers mining records a desk **already
holds** (reports, replay streams, rejection logs, constants) with nine structural moves, the autopsy protocol and the
vein map of that hunt. This file covers mining **the market** for mechanisms nobody on the desk has priced yet. The two
share the believability conditions, the autopsy discipline and the rule that a hunt is graded on potential edge found
and armed, never on proven trades. Use this file when the question is "where is new edge and how do I find it"; use
edge-find-methods.md when the question is "what is hidden in what we already have". Both feed CREATE in
[SKILL.md](../SKILL.md).

Honesty boundary: everything here is **potential edge**, ranked by evidence strength and armed only as minimum-size
paper shadows. No strategy in this repository is shown to be profitable. The numbers are one desk's retrospective
measurements, quoted so a reader can check the method, not as forecasts.

> **Amendment, 15 November 2026 (evening): the mechanism question generates hypotheses; it does not score cells.**
> A later pre-registered test overrides any reading of this file that uses a mechanism rating as a per-cell weight.
> Rules: (1) "who is forced to trade, and when" is a **hypothesis generator** (it decides what to test) and a
> **family-level tie-breaker** (it orders whole mechanism families of similar statistical strength); it is **not a
> per-cell scoring weight**. (2) Rank any narrative prior (a rubric, a panel, a red-team score) **within side x
> instrument** before it touches any ranking. (3) Watch for **long-story bias**: raters find stories for buying easier
> to believe than stories for selling. Full evidence and the reconciliation with the practice ranking are in
> [section 11](#11-amendment-the-mechanism-prior-is-a-generator-and-a-family-tie-breaker-not-a-cell-weight); the
> steps below are edited only where they would have contradicted it.

---

## 0. Cold-start checklist (read this first, run it in order)

1. **Start from a payer, not a pattern.** Write one line: *who must buy or sell, when, regardless of price, and how
   much.* If you cannot name a rule, clock, mandate, index, liability or settlement that forces the trade, you are
   about to mine noise (section 2, step 1).
2. **Rate the mechanism blind before you look at any result** with the 0-3 rubric in section 2, step 2, at the
   family level, ranked within side x instrument. Use it to choose what to test and to break ties between families,
   never as a per-cell weight (amendment, section 11). Never show the rater out-of-sample numbers or the in-sample t.
3. **Freeze the plan** before results: splits (in-sample to 2014, out-of-sample 2015 on, late 2024 on, pre-2024, and
   any pre-ETF history), entry convention (delay-1, no look-ahead), cost model, trial family, falsifier.
4. **Build the event calendar from the primary source** (Treasury auction and settlement records, index providers'
   notices, exchange holiday calendars), never from a price pattern.
5. **Residualise before selecting**: score `R - beta * R_bench` with a trailing beta known at the time.
6. **Plant noise**: placebo features and shifted-date copies run through the same pipeline as the real ones.
7. **Score potential (EPS 0-100), do not pass/fail.** Shrink, check persistence across eras and older history, compute
   placebo lift, family BH q and pi0 (section 3).
8. **Race every co-timed explanation and demand a dose-response** before naming the mechanism (section 2, step 8).
9. **Run the fake-edge trap checklist** (section 5) on every candidate you want to arm.
10. **Red-team, gate, then arm near-misses as minimum-lot paper shadows** with a kill switch and a dated first fire.
    Do not kill a near-miss for missing a cutoff; do not size anything from a backtest. Under a real-size policy, arm
    by section 12. Either way, pass Gates A-D of [live-firing-audit.md](live-firing-audit.md) first: an armed rule
    that never fires is worth zero.
11. **Write the find record** (section 9) in the same pass, including what you did differently from your default. A
    find with no record is an open defect.
12. **Dig the vein:** transplant the mechanism to second-order holders, stack one or two conditions, then repeat.

---

## 1. The common thread and the evidence for it

**Every real find started from a forced, non-price reason that a known participant must trade at a known time. None
started from a chart pattern.** The statistics only confirmed what the mechanism predicted. The honesty checks are the
other half: they removed the fake edge that volume search produces in bulk.

### 1.1 Measured practice ranking (69 find clusters vs 99 dead ends)

Each find cluster (a round crossed with a mechanism vein; rows that share event dates count once) and each dead end was
tagged against 20 practices by two independent LLM panels, one normal and one skeptical, and their mean was used
(panel agreement 0.80 to 1.00). Enrichment = P(practice | find) / P(practice | dead end), Laplace-smoothed; Fisher
exact test; Benjamini-Hochberg q over the 20 tests.

| rank | practice | finds | dead ends | enrichment | BH q |
|---|---|---|---|---|---|
| 1 | Mechanism first: who is forced to trade, when, regardless of price | 19/69 | 0/99 | 28.45x | 4.2e-08 |
| 2 | Blind LLM mechanism-strength rubric as a prior | 45/69 | 4/99 | 13.09x | 2.4e-17 |
| 3 | Replicate on independent or pre-ETF history | 17/69 | 1/99 | 12.80x | 3.5e-06 |
| 4 | Cost and delay stress (delay-2, 2x cost, neighbour plateau) | 9/69 | 1/99 | 7.11x | 0.0026 |
| 5 | Placebo controls (shifted dates, circular shifts, matched controls) | 51/69 | 10/99 | 6.72x | 7e-17 |
| 6 | Stacking depth 2-3 (calendar x regime x breadth) | 32/69 | 6/99 | 6.71x | 5.4e-09 |
| 7 | Inversion as a sign check | 12/69 | 2/99 | 6.16x | 0.0016 |
| 8 | Discretionary-flow hypothesis | 3/69 | 0/99 | 5.69x | 0.09 (not significant) |
| 9 | Transplant a mechanism to other assets or second-order holders | 16/69 | 4/99 | 4.84x | 0.00043 |
| 10 | Twin, don't kill: near-misses as minimum-lot paper shadows | 9/69 | 2/99 | 4.74x | 0.012 |
| 11 | Continuous potential-edge scoring (EPS, shrinkage, FDR, pi0) | 38/69 | 19/99 | 2.77x | 8e-06 |
| 12 | Brute-force enumeration of condition combinations | 36/69 | 18/99 | 2.77x | 1.3e-05 |
| 13 | Generative volume (many hypotheses, mutations, 10x trials) | 42/69 | 25/99 | 2.35x | 1.4e-05 |
| 14 | Pre-registration | 34/69 | 31/99 | 1.56x | 0.034 |
| 15 | Confound race (co-timed calendars, dose ladders) | 1/69 | 1/99 | 1.42x | 1 |
| 16 | Options expressions from modelled prices | 1/69 | 1/99 | 1.42x | 1 |
| 17 | New data source (web, government calendars, long yield history) | 3/69 | 4/99 | 1.14x | 1 |
| 18 | Single-indicator scan of popular indicators | 0/69 | 1/99 | 0.71x | 1 |
| 19 | Route unblocking (new adapters, substitute venues) | 0/69 | 2/99 | 0.47x | 0.64 |
| 20 | Pass/fail gate on a t or Bonferroni hurdle | 1/69 | 24/99 | **0.11x** | 2.9e-05 |

### 1.2 What to do with the ranking

- **Do first, always:** ranks 1 to 7, 9 and 10. They are strongly enriched and significant (q below 0.01, or 0.012
  for twinning). Rank 2 is a property of how a round was run (it started from mechanisms), not evidence that a
  per-cell mechanism score predicts persistence; see the amendment in section 11.
- **Use as engines, never as evidence:** ranks 11 to 14. Volume, enumeration and scoring are common in finds *and* in
  dead ends. They are necessary to cover ground and insufficient to find anything on their own. Report a placebo
  selection rate beside every volume funnel.
- **Never default to:** rank 20 (the pass/fail hurdle, the most depleted practice) and rank 18 (single-indicator
  scans).
- **Underpowered, not useless:** confound races (15) produced the most important relabel of the program but fold into
  one vein unit; route unblocking (19) unblocks work but does not itself find edge.
- **Bias caveats:** find units carry richer framework text than dead-end lines, which inflates tag rates on finds;
  finds are post-selection board rows, not independent edges. Treat the table as an ordering of priors, not causal
  proof.

---

## 2. The protocol, step by step

Each step lists its input, the exact actions, the decision rule and the output. Steps 1 and 2 happen before any
statistics. Steps 5 to 9 run inside one frozen, pre-registered pipeline.

### Step 0. Set up the laboratory

**Input:** daily bars for every liquid ETF and future since inception (adjusted *and* raw prices), index levels
before the ETFs existed, long government yield series (constant-maturity yields from the 1960s on), intraday bars
(1- and 5-minute) for the intraday questions, and an official exchange calendar including half-days and foreign
closures.

**Actions:**
1. Fix the splits: in-sample (IS) to 2014; out-of-sample (OOS) 2015 on; OOS-A and OOS-B halves (for example
   2015-2021 and 2022-2026, or 2022-2023 and 2024-2026 when IS ends later); late 2024 on; pre-2024; external (pre-ETF
   indices, yields, other venues). Calendar-ordered only.
2. Fix the entry convention: a signal known at the close of session s enters at the open of s+1 (delay-1). For
   calendar anchors known in advance, enter at the open of the anchor session. Delay-2 (one more session) is a stress
   test, never the headline.
3. Fix the timestamp convention for intraday bars before writing any rule: is the bar labelled by its start or its
   end? (Section 5, trap 1.)
4. Fix the cost model: the desk's real round trip at intended size (about 10 bp for liquid ETFs, 2x that as the
   stress), real-touch spreads for small names.
5. Open a trial ledger: every trial gets an id, its family and a status; errored trials are counted, not dropped.
6. Write the pre-registration: hypotheses, families, thresholds, falsifiers, and the doses you will demand. Hash it.

**Output:** a frozen pre-registration and an empty trial ledger.

### Step 1. Name who is forced to trade, and when

Ask each question below about the market you are studying. Every yes is a candidate anchor.

| Question | Examples that persisted in this program |
|---|---|
| Who must buy or sell because an index changes? | Bond index month-end rebalances (the Bloomberg US Aggregate holds coupon and paydown cash until the last business day, then reinvests it and adds new issues); S&P 500 deletions; MSCI and Nasdaq-100 reviews |
| Who must absorb scheduled supply? | Primary dealers at Treasury auctions and quarterly refunding settlement (15 February, May, August, November) |
| Who rebalances on a clock? | Pension and balanced funds at month and quarter end; leveraged ETFs at the close |
| Who settles or expires on a date? | Options expiry week on large-cap indices; VIX expiry |
| Who faces a closure elsewhere? | Holders of a foreign market's ETF while that market is shut (only when the ETF actually holds the closed market) |
| Whose liabilities or collateral force a trade? | Insurers buying recently added Treasury issues at month end; margin and funding calls after capitulation |

**Decision rule:** if the only story is that "traders tend to" do something (sentiment, discretionary reaction,
momentum chasers, chart levels), mark the hypothesis *discretionary* and expect it to reverse out of sample (section
7). Keep it only as a contrast arm.

**Output:** a list of anchors, each with the forced participant, the date rule, the direction, the expected size and
the instruments that participant actually trades.

### Step 2. Score the mechanism blind, before any statistics

Rate every hypothesis (or every family, when there are thousands of rows) with this rubric. The rater sees only the
rule in words (anchor, offset, hold, instrument, side, conditions). It must never see out-of-sample results, and
should not see the in-sample t either: in one test a rater that saw the in-sample t produced scores that the t alone
predicted with AUC 0.953, so the "prior" was an echo of the statistic.

```text
Rate the strength of a causal mechanism that would make this rule persist out of sample.
0 = none: a price pattern with no identified counterparty.
1 = weak story: a discretionary or sentiment flow that participants are free not to make.
2 = plausible or documented: a known risk premium or published anomaly family; a payer exists but is not forced.
3 = structural forced flow: a rule, clock, mandate, index or settlement forces a named participant to trade at a
    known time regardless of price, with size known or estimable in advance.
Answer with one integer.
```

**Actions:**
1. Ask two panels: a normal one and a skeptical one ("assume most calendar effects are data-mined; rate only what a
   skeptic would grant"). Use the mean, m in [0, 3].
2. If you also run pairwise comparisons, run every pair in both orders: position A won 64 to 72 percent of duels
   regardless of content.
3. Validate the rubric once on your own history before trusting it: rank IS-only items by the rubric and correlate
   with their OOS outcome, clustered by mechanism. In this program the mechanism-strength question was the only design
   whose OOS correlation was cluster-robust (Spearman rho +0.113, 95 percent CI [0.041, 0.191], about four times the
   |IS t| baseline of +0.028); counterparty, persistence, red-team and pairwise questions were not. That test ranked
   1,251 hand-designed mechanism hypotheses and was not checked within side; a later test over 24.4 million
   combination cells found no per-cell information within side (section 11).
4. Check the validated score on a scale-free outcome too (OOS t or sign, not only basis points). One later variant
   correlated with OOS basis points at rho 0.12 to 0.22 and with OOS t at about 0: it was selecting volatile
   combinations, not persistent ones. Fit any weight on one OOS half and test it on the other.

**Use:** the rubric generates and orders hypotheses and breaks ties between families. Inside the score it enters only
as a family-level value ranked within side x instrument (section 3), never as a per-cell weight, never a gate and never
a ranking of in-sample strength (amendment, section 11).

### Step 3. Build the calendar from primary sources

**Actions:**
1. Pull dates from the producing institution: the Treasury's securities records for auctions, refunding announcements
   and settlements; index providers' notices for announcement and effective dates; the exchange's own calendar for
   half-days (detect from the official list or a last print by 13:30, then truncate the session to 13:00; last-bar
   detection is wrong in both directions).
2. Record the announcement date *and* the effective date of every event. Single-name index effects live in the
   announcement-to-effective window; effective-date-only studies conclude the effect is gone (section 6, example 5).
3. Filter to events where the forced trade is real: for index deletions, keep continuing, tradable names and drop
   mergers, take-privates, bankruptcies and delistings.
4. Compute the **event-time profile** (mean return at each offset k from -10 to +10 sessions) for each anchor and
   instrument before choosing any window. The profile shows whether the flow is front-run (the month-end bond bid
   lives at k = -2 and -1, not on the last day).

**Output:** a dated event table with provenance per row and an event-time profile per anchor.

### Step 4. Enumerate the space and count every trial

Cells are anchor x offset k (for example -7 to +3) x hold h (1, 2, 3, 5, 8, 10, 20) x instrument x side x up to two
conditioning layers (regime, breadth, rate trend, volatility rank, quarter-end in or out, refunding month in or out).

**Actions:**
1. Include in the same battery: placebo features (random series), seeded random-month layers, and inverted rules. They
   are the noise floor.
2. Count errored trials per chunk before selecting anything. A broken data link once silently errored 10,351
   conditioned trials; fixing it changed which rows reached the top tier.
3. Keep depth at 2 or 3. Single-variable cells are mined out; depth 4 and 5 multiply trials faster than signal.

**Output:** a trial table with trial counts by family, error counts and placebo counts.

### Step 5. Residualise before you select

Score every trial on the residual return `e_t = R_t - beta_t * R_bench,t`, with beta from a trailing 252-session
regression known at t; the benchmark is TLT for duration instruments and SPY otherwise (benchmark-class instruments
keep raw returns). For off-Treasury bond transplants also require a Treasury-duration-neutral residual above zero.

**Why:** across rounds, a quarter to two thirds of raw "edge" was benchmark beta (5,318 raw IS selections, of which only
3,962 survived on residuals; in another round 2,340 of 6,860).

### Step 6. Compute the statistics per cell

- **Lift:** mean residual return on event trades minus the instrument's own unconditional mean over the same split,
  in basis points per trade, in the candidate direction.
- **t:** clustered by the independent unit (the event date, not the symbol-day). Report the number of clusters beside
  every t; refuse verdict language with fewer than about 10 date clusters.
- **z by split:** z_IS, z_OOS-A, z_OOS-B, z_OOS, z_late (2024 on), z_pre24, z_ext (independent history).
- **Selection screen (volume families only):** |IS lift t| >= 2 and n >= 12 events, then family BH q and pi0. A
  mechanism-first, pre-registered hypothesis is scored whatever its IS t: the best single-stock find of the program
  had IS t 0.91.

### Step 7. Run the guard stack

Apply every guard to every candidate that will be scored, and record each outcome.

| Guard | Test | Typical bar |
|---|---|---|
| Shifted-date placebo | Same rule on dates shifted +-10 and +-20 sessions, or 100-200 circular shifts | Real beats at least 80 percent of shifts (`shift_beat >= 0.80`) |
| Other-month placebo | Same day-of-month in non-event months | Event months clearly stronger (TLT refunding t 4.70 vs other-month settlement t 0.01) |
| Layer DiD | DiD = [z(event and layer) - z(event)] - the same on shifted dates; also vs seeded random-month layers | DiD > 0 is a hard gate for any conditioning layer |
| Delay-2 | Enter one session later | Effect degrades gracefully, does not flip |
| Cost 2x | Net of twice the real round trip | Net stays positive |
| Plateau | Neighbouring k and h | Neighbours same sign; an isolated spike is a fit |
| Independent history | Pre-ETF index levels, long yield series, raw NAV of old funds | Same sign; one-sided t >= about 2.5 pre-registered |
| Futures sanity | Drop trades whose window holds a roll-sized gap; rerun on a live ETF proxy | Proxy agrees in sign; otherwise kill |
| Live path | Can the live system compute every input at decision time? Does the trade exit before ex-dates? | Exit by the month-end close for bond ETFs that go ex on the first business day |

### Step 8. Race the confounds, then demand a dose-response

1. **List every co-timed calendar** that could explain the same dates (13F filing deadline vs refunding settlement;
   2-, 5- and 7-year auctions vs month end; post-holiday vs Monday; pre-holiday+1 vs post-holiday+0, which are the same
   dates). Run each label alone on the days where they diverge, and on separate intraday windows where they cannot
   diverge by date.
2. **Measure overlap** (Jaccard of event windows) with every rule already live; above 50 percent window overlap in the
   same sector is a clone, not a find.
3. **Dose-response:** name the quantity that should scale the effect if the mechanism is true and test that the effect
   is monotone in it. Duration for a Treasury supply story (1 bp in a 2-year fund to 156 bp in a 27-year fund);
   membership for an index story (members vs non-members); exposure for a foreign-closure story (only ETFs that hold
   the closed market); flow divided by average volume for a deletion story.
4. **Decision rule:** a flat or reversed dose kills the *named* mechanism, not necessarily the effect. Report the effect
   under the mechanism the doses support ("index reinvestment and duration demand into ME-2/-1", not "bigger extension,
   bigger edge"), and name the most likely alternative when a dose is flat.

### Step 9. Score potential (EPS) and the family

Compute the Edge Potential Score for every candidate and the family statistics for every family (section 3). Count
veins, not rows: rows that share event dates are cluster-mates.

### Step 10. Red-team, gate, arm and record

1. **Red team:** give a strong reviewer the rule, the mechanism, the doses, the guard results and the family
   statistics, and ask for keep, demote or kill-exact-row per candidate, with the likeliest alternative explanation.
   The red team is a reviewer, never the selector. In one round it demoted 8 of 10 top-tier rows.
2. **Gates for a shadow twin (the tier A of this program):** EPS >= 62 when interim; OOS halves the same sign; family
   BH q <= 0.20; placebo lift >= 1.5; K > 0; `shift_beat >= 0.80`; layer DiD > 0; residual z > 0 against the dominant
   beta; OOS raw lift at least the desk round trip (10 bp for ETFs); for futures, cash proxy agrees; live inputs
   computable; not a clone; one new twin per economic family or sector; red team not kill.
3. **Arm:** a minimum-lot paper shadow behind a per-round kill switch, with its first fire date printed and a falsifier
   (for example, demote if the mean net over the first 20 fires is not positive). Generate the live rules only after
   the red team, outside the live tree until committed. Under a real-size policy, arm by section 12 instead. Nothing
   is armed until it passes Gates A-D of [live-firing-audit.md](live-firing-audit.md).
4. **Record** the find (section 9) and append the practices that worked and the honesty notes to the round's log.
   The round is not done until every find record is complete.

### Step 11. Dig the vein

When a find lands: transplant the anchor to second-order holders (country and broad ETFs for index events, IG credit,
MBS and TIPS for Treasury flows, shorter tenors for duration flows); mutate offset and hold; stack one regime or
breadth layer under the DiD gate; invert as a sign check. Mutants inherit their parent's dates, so they are
corroboration, not independent confirmation. Then return to step 1 with the next anchor.

---

## 3. The Edge Potential Score (EPS) method

EPS ranks candidates by **potential**: how likely the effect is real and persistent, weighted by cost robustness and
mechanism, on a 0-100 scale. It replaces the pass/fail hurdle.

### 3.1 Components

`EPS = H * (25 E + 15 C + 10 P + 10 R + 15 M + 10 K + 5 N + 5 S + 5 X)`, each component in [0, 1].

| Component | Weight | Formula |
|---|---|---|
| E, shrunk effect | 25 | Empirical-Bayes posterior mean of the effect in the candidate direction, treating z_IS and z_OOS as two measurements of theta with prior N(0, tau^2): `theta = max(0, (z_IS + z_OOS) * tau^2 / (1 + 2 tau^2))`; tau^2 = the family's cov(z_IS, z_OOS) shrunk toward a pooled 0.077 with weight n/(n+200). `E = clip(theta / 1.2, 0, 1)`. Without a family: OOS t x 0.35, x 0.2 if prices are a proxy, x 0.12 if the only sample is 2024 on; add 0.175 x z_ext when an independent replication exists |
| C, sign consistency | 15 | Over the available splits (IS, OOS-A, OOS-B, external): `sum(1[z > 0] * min(1, abs(z))) / number of splits`. Cap at 0.5 for short-sample or proxy items |
| P, placebo | 10 | `lift / (1 + lift)`, where lift = the rate at which real cells reach this cell's abs(t_IS) divided by the rate for placebo cells in the same family; or the date-shuffle permutation percentile when available |
| R, persistence ratio | 10 | `clip(z_OOS / z_IS, 0, 1.2) / 1.2`; 0.5 if z_IS <= 0 or unknown |
| M, mechanism prior | 15 | `0.5 * (m / 3) + 0.5 * clip(family cov(z_IS, z_OOS) / 0.5, 0, 1)`, m = blind rubric mean in [0, 3]; m defaults to 1.5 until scored |
| K, cost robustness | 10 | L = OOS mean lift in bp per trade in the trade direction, c = the stress cost: `K = clip((L - c) / L, 0, 1)` if L > 0, else 0. Liquid ETFs: 0.5 x the form with c = 20 bp + 0.5 x the form with c = 6 bp; single stocks: c = twice the real round trip (176 bp for a 0.88 percent round trip) |
| N, novelty | 5 | Decorrelation from rules already live; 0.5 until scored |
| S, sample | 5 | `min(1, log10(n_OOS) / 2.5)` |
| X, expressibility | 5 | Option convexity or other expression; 0.5 until scored |
| H, fragility haircut | multiplier | `1 - 0.2 * P(single-regime artefact)`; 0.9 at the default 0.5 |

Per the amendment (section 11), m is the **family-level** rubric score, ranked within side x instrument and mapped
back to [0, 3]; a cell with no family score keeps the neutral 1.5. Because M carries the rubric at weight
15 x 0.5 x H, a rubric answer moves EPS by
`EPS = eps_stat + 2.25 m - 3.375` (eps_stat = the score with m at its neutral 1.5), so the rubric can move a row by at
most +-3.4 points. Two consequences: (1) a cell needs eps_stat >= 46.625 to reach EPS 50 even with m = 3; (2) paid
mechanism judgements are worth buying only for rows within 3.4 points of a tier line (section 8, practices 26 and 37b).

### 3.2 Family statistics

- **pi0 (Storey, lambda 0.5):** `pi0 = #{p > 0.5} / (0.5 * m_tests)`; estimated true signals = (1 - pi0) x number
  selected. Compute on one-sided p of IS-selected cells, clustered so each mechanism x symbol counts once. Example: 951
  IS-selected signals with pi0 0.885 imply about 109 true ones, which a t-hurdle would mostly discard.
- **Empirical null (Efron):** estimate the null spread from the interquartile range, sigma0 = IQR(z) / 1.349 (0.888 in
  the first board), and compute p against it, not against N(0, 1).
- **BH q** within the family (family = mechanism or order x horizon; market-only cells are a separate family).
- **Family persistence:** cov(z_IS, z_OOS) across the family's cells. Forced-flow families ran 0.33 to 0.66; generic
  calendar families near 0; discretionary families negative (section 7).

### 3.3 Tiers and value of information

- **EVOI** (expected value of the next experiment) `= 4p(1-p) * payoff * resolving_power / cost_class * 100`, with
  `p = 0.5 * P(survives, from the rubric) + 0.5 * Phi(theta - 0.5)` and `payoff = (0.5 + 0.5 K)(0.5 + 0.5 capacity)`.
  It is highest for candidates near 50/50 with a large payoff and a cheap decisive test.
- **Tier B, targeted experiment:** EPS >= 58, or EVOI >= 12 with family q <= 0.20.
- **Tier A, shadow twin:** passes every gate in step 10 and the red team.
- **Tier C, watch:** everything else, kept on the board with its next experiment named.

### 3.4 What the score is not

EPS is a ranking of potential under one desk's priors, not a probability of profit. Its weights are a design choice,
checked only by whether the board's top rows persisted better than its bottom rows; a reweighting must be fitted on one
OOS half and tested on the other. Paid or inherited scores are labelled by source (row-scored, family-inherited,
model-predicted), and an inherited score is never treated as row evidence.

---

## 4. Your default failure modes as an LLM, and how to override each

These are the habits the record shows an unsteered LLM falls into. Every find came from overriding one or more of them.

| Default habit | What it cost in the record | Override |
|---|---|---|
| Scan popular indicators one variable at a time | 0 finds; the single-variable layer is mined out | Start from step 1. Indicators enter only as a layer under a forced-flow anchor |
| Grade against a t or Bonferroni cutoff and kill the near-misses | The most depleted practice (0.11x); the best single-stock find had IS t 0.91 | Score potential (EPS); arm near-misses as shadows |
| Accept the first calendar label that clears the bar | The "13F deadline" winner was Treasury refunding | Race every co-timed calendar; demand a dose |
| Grade the winner and stop | Transplants and stacks found most later rows | Mutate, transplant, invert, stack (step 11) |
| Stop at "blocked" when a route fails | Blocked items stayed blocked until rerouted | A failed route is a route result; try the next route ([edge-find-methods.md](edge-find-methods.md), method 2) |
| Trust a score from another model | A mechanism score that saw the in-sample t echoed it (AUC 0.953) | Blind rubric; validate against OOS t, not bp |
| Believe the better story | Mechanism ratings averaged 0.62 on longs vs 0.49 on shorts; 80 percent of a mechanism-weighted top 1 percent were longs, while shorts persisted more often (60 vs 47 percent) | Rank every narrative prior within side x instrument; use it as a generator and family tie-breaker only |
| Treat volume as rigor | 1,021,230 trials with placebos selected at 3.80 percent vs 3.61 percent for real features | Report the placebo selection rate; volume finds cells, not edge |
| Count rows as discoveries | 590 tier-B rows were mostly cluster-mates sharing event dates | Count veins (round x mechanism), not rows |
| Read raw returns | A quarter to two thirds of raw edge was beta | Residualise before selecting |
| Trust bar labels, adjusted prices and continuous futures | Look-ahead, payout and roll artefacts posed as edge (section 5) | Audit timestamps, use raw prices around payouts, use dated contracts or ETF proxies |
| Narrate a mechanism after the fact | Pension and extension-size stories failed their doses | Name the dose before the data; report the mechanism the doses support |
| Put OOS numbers in the prompt of any judge | Leaky judgements look like skill | Judges see IS-only facts, or nothing numeric |
| Optimise the obvious bottleneck | A "rate-limited" queue was its own spend check re-reading an 18 MB log per call | Measure every stage before fixing any (practice 20) |

---

## 5. Fake-edge trap checklist

Run every row before arming anything. Each trap is a real case from the program with the test that caught it.

| # | Trap | Real example | Test that catches it |
|---|---|---|---|
| 1 | **Look-ahead from bar labels** | SPY 10-minute downside opening-range breakout continuation: OOS t 4.57, n 489, +15.8 bp. Bars were start-labelled; the 10:30 bar closes at 10:40, so entering at the 10:30 open leaked that bar (+10.98 bp). Post-signal remainder +0.62 bp; the honest next-bar rule had IS z -0.20 | Write the timestamp convention down; enter only at a price printed after the signal is known; split P&L into the leaked signal bar and the post-signal remainder |
| 2 | **Continuous-futures roll jumps** | Live-cattle futures around Japan's Golden Week: all 23 trades crossed a roll. Natural-gas turn-of-month fell to z 0.86 with gaps excluded. Payroll-minus-5 in bond futures: residual OOS t 3.17, but the TLT proxy was -0.41 | Drop trades whose window holds a roll-sized overnight gap; rerun on the cash ETF proxy; use dated contracts |
| 3 | **Benchmark beta** | 2,340 of 6,860 raw selections survived residualising in one round; refunding transplanted to equities was mostly stock-bond beta (SPY residual -1.5 bp) | Residualise before selecting; fingerprint event bp against each instrument's beta (rho 0.776) and read the residual |
| 4 | **Spread units** | Micro-cap post-quarter loser reversal: OOS +100 bp gross. The spread estimate was stored in percent (median micro 0.89 meaning 0.89 percent); twice the median spread is about 185 bp, more than the gross | Read the unit of every cost field; price net of 2x real spread at intended size |
| 5 | **Payout booked on the event day** | Adjusted closes of an old Treasury fund booked the monthly payout on month-end day: a fake +77 bp at t 12.96 | Use raw prices or NAV around ex-dates; exit bond ETFs by the month-end close |
| 6 | **Co-timed calendar relabel** | The 13F filing deadline and refunding settlement fell 0 or 1 session apart on all 134 events; 2-, 5- and 7-year auction rows were a month-end relabel (one row with EPS 79.7 killed) | Race labels on divergent days and separate intraday windows; Jaccard against existing rules |
| 7 | **Weekday concentration** | SPY last 30 minutes after a holiday: z 3.11 in aggregate, but it was post-holiday Mondays (+20 bp); post-holiday Tuesdays were flat (+0.18 bp) | Split every holiday or event effect by weekday |
| 8 | **Half-day calendar errors** | Last-bar detection marked early sessions that ended 13:15-13:25 and missed official half-days that printed 16:00 bars | Use the official half-day list or a last print by 13:30; truncate at 13:00 |
| 9 | **Exposure mismatch** | Foreign-closure effects had the same mean abs(OOS t) on own-venue, regional and unrelated ETFs (0.808 / 0.818 / 0.819) | Keep only ETFs that hold the closed market; the exposure is the dose |
| 10 | **Placebo layers riding a real base** | Random-month layers were selected at 8.13 percent vs 7.67 percent for real layers; in another round placebos beat real features 10.43 vs 5.14 percent | Score each layer by DiD against shifted and random-month copies; DiD > 0 is a gate |
| 11 | **Silent errored trials** | A broken data link errored 10,351 trials without a message | Count errors per chunk before selecting |
| 12 | **Era-mismatched base rate** | Equity turn-of-month in index futures looked strong against an "other days" base from a different era; residual ES OOS t 0.81, late -0.60 | Compare against the same era's base; read late and pre-2024 separately |
| 13 | **Proxy membership** | A point-in-time cap-rank proxy for Russell reconstitution recalled about 10 percent of real adds and 3 percent of deletes | Use official lists; measure proxy recall before using it |
| 14 | **Untradable events** | All-named S&P 500 deletions looked top-tier until mergers, take-privates and bankruptcies were removed | Keep only events where a continuing, tradable name is forced through the index |
| 15 | **Regime decay** | SPY close-momentum dose fell from rho 0.7 (2000-16) to 0.3 (2017-26); the 2024-26 transplant reversed (IWM -8.6 bp, t -3.09) | Read the dose in the current regime before building an engine |
| 16 | **Mutants as confirmation** | Transplanted anchors inherited their parent's dates; their low pi0 was inherited signal | Count a mutant as corroboration of the parent, not a new find |
| 17 | **Dense composites** | Summing 25 shrunk calendar profiles into one daily pressure: OOS Sharpe 0.62 vs 0.73 for equal weight (IS 4.44); 21 of 25 components beat it | Keep composites sparse; weight by shrunk IS Sharpe |
| 18 | **Annual anchors** | Annual events give about 12 OOS observations; red teams killed rows with 11-12 events and shift-fragile placebos | Treat as shadows only; never size from them |

---

## 6. Worked examples

Five finds and three kills, traced step by step. Numbers are as measured; "z" is a date-clustered statistic on residual
returns unless marked raw.

### Example 1. The 13F-to-refunding relabel (a confound race)

1. **Found:** a pre-registered 85,534-trial sweep surfaced "13F filing deadline +3, long TLT, hold 5": OOS +83.4 bp
   vs +9.6 bp in the other eight months. The red team flagged that it could not tell 13F from Treasury refunding.
2. **Who is forced:** two candidates. Institutional managers filing 13F holdings (discretionary, weak) and primary
   dealers absorbing quarterly refunding supply that settles on the 15th of February, May, August and November
   (structural, forced).
3. **Race:** built a refunding calendar from the Treasury's own securities records (187 events, 168 other-month
   settlements). Anchoring on 13F gave TLT t 4.58; anchoring on settlement gave t 4.70 (n 97). The two anchors were 0
   sessions apart on 24 events and 1 session apart on 110: **zero divergent events**, so exact timing is not
   identified, and the record says so.
4. **Placebos:** settlement-day rule in non-refunding months: TLT t 0.01 (+0.1 bp); the 14th of other months t 0.15.
   The bid is specific to refunding months.
5. **Dose:** duration ladder (example 2) Spearman 1.0 across Treasury ETFs; auction size dose flat (rho -0.137,
   reported, not hidden).
6. **Equity check:** after the 13F deadline, megacap and index ETFs were negative (SPY -32.7 bp, MSFT t -3.16): the
   13F equity story was not supported.
7. **Intraday second race, two days later:** on days that were refunding-only, SPY's last 30 minutes kept z 2.57
   (+11.1 bp); on 13F-only days z -0.35. The next-day close-to-close bid lived in 13F-only days and did not persist late
   (z_late 0.33), so it was not armed.
8. **Result:** relabelled as a refunding-month duration bid; ZROZ and EDV became top-tier shadows (EPS 80.0 and 79.7).
   **Reusable rule:** two calendars that fall on the same dates are one observation until you find days that separate
   them; the mechanism with a working dose wins the label.

### Example 2. The refunding dose ladder and its fingerprint (dose-response)

1. **Prediction stated first:** if dealers must warehouse long-duration supply, the effect must scale with duration.
2. **Ladder (refunding window, OOS raw bp per trade, t):** SHY (1.9 years) 1.0 bp, t 0.63; IEI (4.5) 10.4, t 2.12; IEF
   (7.5) 22.2, t 2.92; TLH (13) 49.8, t 3.76; TLT (16.5) 76.2, t 4.70; EDV (24) 137.3, t 4.64; ZROZ (27) 156.3, t 5.19.
   Credit carries it only through duration: LQD (8.5) 20.1, VCLT (13.5) 53.4, HYG (3.5) 0.1.
3. **Fingerprint before transplanting:** event bp against each instrument's TLT beta, Spearman 0.776 (p 4e-21). After
   removing that beta: Bunds -5 bp, gilts -14, JGBs -6.5, munis t 0.81, equities about 0 (XLK +4, SPY -1.5). Verdict: a
   US-supply duration effect, not global duration demand; "new soil" mostly re-exposed the same beta.
4. **Transplant that failed:** Treasury futures after residualising TLT beta are dead (bond futures settle+2 residual
   OOS t -0.12) although the cash ETFs are top tier.
5. **Reusable rule:** a mechanism earns its name only when the effect is monotone in the quantity the mechanism says
   should drive it; then residualise that quantity out before calling anything a transplant.

### Example 3. IEF month-end (independent history and the mechanism found later)

1. **Found:** mechanism-first structural mining (220 mechanisms, 17,616 variants): "long IEF over the last 5 sessions of
   the month, hold 5" scored EPS 78.4 (z IS 2.42 / OOS 3.52 / late 1.28 / external 5.56; family q 0.02, about +20 bp).
   A sibling (last 2 sessions) had the best q of all signals (0.005) and had been dropped by a one-per-family rule; it
   was resurrected.
2. **Independent history, pre-registered:** a long-Treasury mutual fund's raw NAV 1986-2002, t 2.74; eight bond ETFs
   pooled on raw prices, clustered t 5.27; combined Stouffer z 3.88.
3. **Artefact caught on the way:** the adjusted-close series booked the monthly payout on month-end day (fake +77 bp at
   t 12.96). All bond tests moved to raw prices; the artefact row stayed in the record labelled not-used.
4. **Mechanism read later from methodology:** the Bloomberg US Aggregate holds coupon and paydown cash until the
   last-business-day rebalance and adds new issues only then; insurers are net buyers of recently added issues; a
   published study finds the last-day effect in duration-scaled futures.
5. **Timing dose:** OOS k-1 +4.8 bp (t 3.0), k-2 +4.3 bp (t 2.2), last day +2.1 bp (and -6.2 bp in 2024 on): buyers
   front-run into ME-2/-1.
6. **Tenor transplant:** the same calendar persists in 3-7 year rates (IEI) with a stronger quarter-end dose; the
   equity turn-of-month in index futures does not (residual ES late -0.60).
7. **Reusable rule:** older independent history is the cheapest rigor there is; read the index methodology to find who
   is forced, then let the timing dose tell you when.

### Example 4. MBB month-end (transplant to a second-order holder, gated)

1. **Origin:** a 99,508-trial mutation pass transplanted the Treasury month-end anchor to sibling instruments; MBB
   (agency mortgage-backed securities, an Aggregate component) appeared at EPS 68.9.
2. **Pre-registered doses for the month-end vein (237,045 trials, 0 errors):** timing pass; duration ladder pass;
   Aggregate members vs non-members, residual t 3.53 vs 1.93 (Treasury-neutral 3.31 vs 1.67), partial pass; inverse
   and leveraged ETFs with the right signs, pass; extension size (rho OOS 0.3, 2024 on -0.6), fail; rate-volatility
   tercile, mixed. The vein was named "index reinvestment and duration demand", not "bigger extension".
3. **Gates added:** OOS raw >= 10 bp; Treasury-neutral residual z > 0 off-Treasury (so a transplant is not just more
   duration); one new twin per sector; > 50 percent window overlap with a live same-sector rule is a clone; inputs
   computable live; exit before the first-business-day ex-date.
4. **The row:** long MBB from ME-4, hold 5, non-quarter months only. Residual z IS 2.75 / OOS 5.24 / 2024 on 2.56;
   Treasury-neutral OOS z 3.97; OOS raw +25.9 bp per trade over 95 trades. Red team: keep, because the mechanism reaches
   the instrument directly (monthly pool paydowns and index maintenance), unlike a generic bond fund.
5. **Counterweights printed beside it:** two sibling transplants (TIPS, long credit) had Treasury-neutral z of about 2
   or less and were demoted; the TLT-beta residual does not neutralise breakevens or credit spread duration.
6. **Reusable rule:** transplant a proven anchor to holders the forced participant actually trades, and require a
   residual that removes the parent's exposure before calling it new.

### Example 5. S&P 500 tradable deletions, announcement window (single names)

1. **Earlier verdict:** an effective-date-only study found the classic index effect gone: additions earned -21 bp on
   the forced-close day OOS (t -1.21) and drifted -124 bp over 20 sessions, consistent with published work.
2. **Who is forced, re-asked:** index funds must sell a deleted name, but the trade is public from the announcement.
   So the window to test is announcement+1 open to the effective close, not the close.
3. **Calendar work:** announcement dates recovered from public sources; events filtered to continuing, tradable names
   (mergers, take-privates, bankruptcies and delistings dropped).
4. **Statistics:** residualised against trailing SPY beta *before* selection; t clustered by date. Short tradable
   deletions: OOS +221 bp per trade over 20 date clusters (74 names, 39 dates); residual z IS 0.91 / OOS 1.85 / 2024 on
   2.59; shifted-date placebos beaten 4 of 4; EPS 71.5. The forced-close window was weaker (OOS +83 bp, t 1.72) and dead
   late (t 0.36).
5. **Honest weaknesses kept on the record:** IS t 0.91 over 18 dates (a t >= 2 rule would have killed it); the
   forced-direction dose (indexer flow over volume) is flat (OOS rho -0.09), so the likeliest alternative is that the
   deletion label tags names already deteriorating. The S&P 600 version was killed (shift_beat 0.25); additions stay
   dead.
6. **Reusable rule:** for single-name index events, recover the announcement date and filter to tradable events before
   concluding anything about the effect.

### Kill 1. The opening-range breakout that was ten minutes of hindsight

A round reported SPY 10-minute downside opening-range breakout continuation at OOS t 4.57 (n 489, +15.8 bp), late t
2.54, also 2017-23 t 3.43, and recommended building an intraday engine. The next round built the engine and replicated
the number on the same tape, then audited the bar convention: bars were labelled by their start, so the 10:30 bar
closed at 10:40, and the rule entered at the 10:30 open using a signal not known until 10:40. The leaked bar carried
+10.98 bp; after the signal was known the remainder was +0.62 bp raw; the look-ahead-free next-bar rule failed in-sample
(z -0.20). Killed as a methodology error, not a cost haircut. **Rule:** never enter at a price the signal has not
printed; always split the signal-bar P&L from the post-signal remainder.

### Kill 2. Calendar edge that was a futures roll

The top raw hit of one round was a Golden Week rule in live-cattle futures; every one of its 23 trades crossed a
contract roll. Natural-gas turn-of-month dropped to z 0.86 with gaps excluded; 2- and 5-year note futures at quarter
end disagreed with their ETF proxies (-0.09 and 0.03). Later, payroll-minus-5 in bond futures (residual OOS t 3.17,
late 2.28, not a month-end relabel) was killed because the TLT proxy ran the other way (OOS t -0.41). **Rule:** a
continuous-futures calendar hit is an artefact until it survives roll exclusion and agrees with a cash proxy or dated
contracts.

### Kill 3. Small-cap reversal eaten by the spread

Micro-cap losers after quarter end reversed by +100 bp OOS (t 1.65), EPS 59.4. The spread estimate in the cache was in
percent: median micro spread 0.89 meaning 0.89 percent, so twice the median spread is about 185 bp, larger than the
gross. Killed on cost. A misread of the unit as a fraction would also have killed it, for the wrong reason. **Rule:**
read the unit of every cost field and price at twice the real spread at intended size before believing a small-cap
effect.

---

## 7. Mechanism vein map: what persists and what reverses

Family persistence from the first potential-edge board (cov(z_IS, z_OOS) and mean OOS t in the IS direction across
each family's cells), updated with later rounds.

| Class | Families | Evidence |
|---|---|---|
| **Persists: structural forced flow** | Treasury auctions and refunding (cov 0.66); month-end bond index reinvestment (Treasury, IG, MBS, TIPS; sector pi0 0.39-0.55); pension and quarter-end rebalancing (cov 0.54); VIX expiry (cov 0.47, highest mean OOS t 0.50, small n); options-expiry week on large-cap indices (pre-ETF indices clustered t 3.79; null before listed index options, 1970-82, as the dealer mechanism predicts); index reviews via second-order holders (small n); S&P 500 tradable deletions, announcement window | Same sign IS -> OOS -> pre-2024, beat placebos, doses mostly pass |
| **Persists weakly or narrowly** | Capitulation (1990s index t 2.60, n 20); crypto lead into Monday equities; buybacks; dealer gamma; foreign closures only where the ETF holds the closed market | Small n or single dose; shadow only |
| **Noise at the family level, a few sharp cells** | Generic equity turn-of-month (pi0 0.93), generic opex (0.82), quad witching (1.0), payday, day of week, lunar, geomagnetic | Family persistence about 0; trust only a cell with its own mechanism and dose |
| **Reverses out of sample: discretionary flow** | FOMC (mean OOS t -0.19), CTA trigger levels (-0.29), turn of year (-0.28), sunspot, rates-reaction rules | Negative family persistence |
| **Dead in the current regime** | Equity turn-of-month in index futures; SPY close momentum and leveraged-ETF gamma continuation; S&P 500 addition close premium; first-hour fade; altcoin-vs-bitcoin long-lookback momentum after 2024 (was crypto beta); refunding in Treasury futures after beta | Residual and late splits negative or zero |

**Reading:** forced flows persist because the participant cannot decline the trade; discretionary flows reverse because
they are crowded and optional. The pension story is the honest exception: its effect persisted in ETFs but failed on
pre-ETF fund history (t -0.13) and its spread dose failed, so the month-end credit lift was credited to index
reinvestment instead.

---

## 8. The practice catalogue (numbered practices 1 to 92)

The program numbered its practices as rounds ran; parallel rounds reused 29-30 and 37-43, so practices 1-54 fill 63
entries (the reused ones are marked a, b and c; 41c-43c come from the amendment in section 11). Practices 55-92 came
from the promotion passes and desk audits of 15-16 November 2026: the research-side ones (59, 64-66, 68) are listed
below; the rest are gates in [live-firing-audit.md](live-firing-audit.md) and section 12. One line each, grouped by
use. Evidence for each sits in the source program's round records.

**Mechanism and search design**
1. Ask who is forced to trade, when, regardless of price; forced-flow families persist and discretionary ones reverse.
3. Use a blind mechanism-strength rubric as a prior; never feed OOS to the judge; run pairwise both ways. Amended:
   family level and within side x instrument only, never a per-cell weight (41c-43c).
4. Stack conditions to depth 2-3; the single-variable layer is mined out.
7. Generate at volume (hypotheses, mutations, inversions), then apply hard guards.
9. Race co-timed calendars; then dose ladder, other-month placebo and event-time profile.
10. Transplant a forced-flow anchor to second-order holders; mutants inherit dates, so they corroborate only.
14. LLM mechanism-first priors rank OOS outcomes (rho 0.499, n 47) but do not beat IS search on same-sign rate; use as
    prior and generator, not filter.
15. Fingerprint a mechanism with a dose ladder plus beta residuals before transplanting.
16. Race every new calendar against the calendars it overlaps before twinning; freeze the removal in the
    pre-registration.
18. Use supply size as a dose within the calendar; calendar weeks without high supply were negative.
25. Foreign-market closures are new soil for holiday calendars; annual anchors give about 12 OOS events, so shadows only.
32. Exposure dose is the cheapest test of a cross-venue calendar story.
33. A named mechanism needs its own dose, not the calendar's (credit the index cycle, not pensions).
41. When digging a live vein, gate by economic family against what is already installed.
46. At the single-name level, recover announcement dates, not just effective dates.
47. Filter tradable index events; drop mergers, take-privates, bankruptcies and delistings.
48. Official index lists beat point-in-time cap-rank proxies; measure proxy recall first.
66. Test a prospect on its own soil and against what is installed; a cell that passes on a proxy but overlaps a
    live strategy (entry Jaccard 0.67) is a clone, not a new edge.

**Scoring and statistics**
2. Score potential (EPS, shrinkage, persistence, placebo lift, FDR, pi0) instead of pass/fail.
5. A real date effect must beat shifted-date placebos.
12. Tighten interim tiers with placebo lift >= 1.5 and K > 0.
13. Weight a calendar composite by shrunk IS Sharpe, never by stacking or concentration.
17. Judge a regime layer by a placebo difference-in-differences, not by its own t; positive DiD is a hard gate.
19. Dead end: a dense forced-flow composite lost to its components; keep composites sparse.
21. Residualise before selecting.
23. Dose-response is a cheap kill switch for a forced-flow story.
29b. Validate a new score against a scale-free OOS outcome, fitting on one OOS half and testing on the other.
31. Multiplying trials multiplies noise unless the placebo selection rate falls; report it beside every funnel.
42. Score a layer against a seeded random-month split, not only shifted copies.
43. A named dose can fail while the base effect holds; report the vein under the doses that pass.
38b. A surrogate can be good on average and weak at the top; report recall at budget, not only rank correlation.
39b. Test an upper-bound ranking trick before using it (quantile ranking was worse than the point estimate).
41c. Pre-register a lens and its pass rule, then let it fail; a mechanism-weighted lens below its shuffle null is a
     clean negative, kept only as a prospecting map.
42c. Neutralise mechanism priors within side x instrument; raters prefer long stories.
43c. "Mechanism helps for forced flows" failed at the cell level (family rho 0.012); use the family rubric only as a
     weak family-level tie-breaker. Rank prospecting maps on complete populations only.
64. Never report the best row of a wide in-sample grid; report K and the OOS pass rate of IS picks (IS z 3-5 fell
    to 0.45-1.99 out of sample).
65. Use the split that fits each asset class's history; a crypto run on an equity split selected on no in-sample data
    and showed OOS z 3-4.5. Void, re-run and disclose both runs.

**Honesty and artefacts**
11. Count errored trials per chunk before selecting.
22. Continuous futures carry roll jumps that look like calendar edge.
24. Published single-name forced-flow close effects are gone; do not re-mine them without announcement dates.
34. Check intraday transplants in the current regime before building an engine.
35. Residualise crypto against its own beta.
37a. A live ETF calendar does not automatically transplant to the matching future.
38a. Equity turn-of-month in index futures is a raw-return artefact once residualised and read late.
39a. A continuous-futures hit the cash proxy fails is killed, not relabelled.
40a. Intraday, test continuation and fade as rival hypotheses and require a current-regime dose.
44. Check the live data path (lookback lengths, ex-dates, point-in-time inputs) before calling a layer twinnable.
49. Read spread units before twinning small and micro-cap reversals.
50. Close-of-day flow needs an intraday engine; build it before testing the story.
51. Detect half-days from the official calendar, then truncate to 13:00.
52. Race a holiday effect against the weekday.
53. Race overlapping mid-month labels on each window separately.
54. Never enter at a price the signal has not printed; split leaked signal-bar P&L from the remainder.
68. A panel built from today's constituents is a survivorship snapshot even at level correlation 0.998; label it
    and re-test on point-in-time membership.

**Arming and operations**
6. Twin, don't kill: near-misses go live as minimum-lot paper shadows with kill switches.
8. Route failure is not impossibility; new routes turned 31 blocked items green.
20. Measure the bottleneck before blaming the obvious suspect.
29a. Treat zero fires as a bug report until a replay proves the rule is rare.
30a. When hosting someone else's rule, read its own decision stamps, not its headline state; fix bounds in a private
     copy, never the rules.
45. Never let an uncommitted engine sit in the live tree while other workers reload.
59. The red team is an overlay, not the selector: apply a verdict only when it is more conservative than the
    pre-registration; override only a factually wrong reason, recorded before any live result.
29a, 30a, 45 and 55-92 (parity, feeds, timing, controls, silent strategies): run them as the gates of
    [live-firing-audit.md](live-firing-audit.md); 72-76 are the arming rules of section 12.

**Spending on paid LLM judgements**
26. Before buying judgements, compute from the scoring formula what each answer can change; ask only where it can move
    a tier (one plan cost $0.43 instead of about $419 and captured every changeable cell).
27. Test whether a free feature already predicts the paid answer; if it does, the answer is not independent evidence.
28. Before skipping a stratum, sample it at random (n 2,000 with zero hits bounds the rate at 0.0015).
30b. Find the cost floor of a paid API before optimising it; asking fewer questions is the only real lever.
36. Under a hard cap, cover every row by inheritance and pay only where an answer can move status; label coverage by
    source.
37b. Bound the payoff before building a model: with the rubric capped, no unscored cell below eps_stat 46.625 could
     reach EPS 50.
40b. Spend the last dollars of a cap on validation where errors matter (the cells nearest the line).

---

## 9. Per-find record template and the completion gate

Append one record per find (one JSON object per line) in the same pass that reports it. A round is **not done** until
every find in it has all eleven required fields; a script should exit non-zero otherwise.

```json
{
  "find_id": "round:anchor:offset:instrument:hold[:layer]",
  "date": "YYYY-MM-DD",
  "round": "rNN",
  "eps": 0.0,
  "tier": "A (shadow twin) | B (targeted experiment) | C (watch)",
  "vein": "mechanism family, e.g. refunding_cycle",
  "depth": "single anchor | anchor x layer | anchor x layer x layer",
  "soil": "data substrate, span and count, e.g. daily raw closes 2002-2026, 97 events",
  "cluster": "events or dates shared with other finds",
  "tool_chain": "calendar source -> enumeration -> residualise -> stats -> guards -> doses -> EPS -> red team",
  "framework": "the stance that organised the work, one or two sentences",
  "technique": "the steps as run, with counts at each stage",
  "mindset": "the belief that made the steps obvious",
  "what_was_different_from_default": "the default habit (section 4) and the deviation that produced the find",
  "steer_that_caused_it": "the instruction or question that started it",
  "dead_ends_before_it": "what was tried and failed first",
  "falsifier": "forward count and line, fixed before the first fire",
  "first_fire": "YYYY-MM-DD or none",
  "evidence_paths": ["files with the numbers"],
  "sha": "commit holding the evidence"
}
```

Required for the gate: vein, depth, soil, tool_chain, framework, technique, mindset, what_was_different_from_default,
steer_that_caused_it, evidence_paths, sha. Each round also appends to its practice log the practices that actually
worked and its honesty notes (trial count, errors, placebo selection rate, pi0, what the red team demoted or killed,
what was not done).

---

## 10. Limits of this protocol

- It was built on US-listed ETFs, futures and stocks, 2000-2026, with daily bars plus a short intraday window. It says
  nothing tested about other venues' microstructure.
- The practice ranking is observational and tagged by LLM panels; it orders priors.
- Survivorship: the stock panels were current-listing universes unless stated; delisting-aware reruns were not done.
- Options conclusions in the program rested on modelled prices or n of 8 or fewer real trades per edge; no options
  result here is real-chain grade.
- Shadows armed under this protocol have a few days of forward life at the time of writing. Their forward record, not
  this document, decides them.

## 11. Amendment: the mechanism prior is a generator and a family tie-breaker, not a cell weight

Added 15 November 2026, evening, after a pre-registered test. It overrides any reading of sections 0 to 10 that puts a
mechanism rating on individual cells.

**The test.** A lens weighting mechanism priors at 40 percent was pre-registered, with its pass rule written first, and
run over 24.4 million condition-combination cells. On the sign of 2024-26 returns it scored AUC 0.490, worse than the
in-sample abs(t) alone (0.529) and the pre-2024 EPS (0.520), and below its own stratified shuffle null (95th
percentile 0.500). The pass rule was fixed in advance, so this is a clean negative, not something to tune.

**Why it failed.**
- **Long-story bias.** Mechanism ratings averaged 0.62 on long cells and 0.49 on short cells; 80 percent of the lens's
  top 1 percent were longs. In 2024-26 longs persisted 47 percent of the time and shorts 60 percent. Most of the
  failure is this side confound.
- **No information within a side.** Within longs and within shorts the per-cell mechanism AUC was 0.499 and 0.508:
  noise, not harm.
- **No help even for forced flows.** Forced-flow cells had mechanism AUC 0.484. Across families the correlation between
  the mechanism rating and persistence was 0.012 for forced-flow families, 0.145 for the rest, 0.077 overall and 0.056
  after controlling for abs(t).

**Reconciling this with the practice ranking (section 1.1).** Both results can be true, and they measure different
things.
- The ranking measures **process**: rounds that *started* by asking who is forced to trade and used a mechanism rubric
  were far more often the rounds that produced find clusters (13.09x for the rubric, 28.45x for forced-flow framing).
  The mechanism question chose *which hypotheses existed*: refunding, index reinvestment, index deletions. Those
  families were then confirmed by doses, placebos and older history, not by the rating.
- The lens measures **scoring**: given millions of generic feature combinations with no named counterparty, does a
  narrative rating of each cell predict which persist? It does not.
- The ranking was also built from LLM-panel tags on post-selection find clusters. Rounds that used the rubric also used
  placebos, independent history and doses, so its 13x is entangled with those practices, and find records carry richer
  framework text than dead-end lines. It never showed that the rubric added information per cell.
- The earlier blind validation (rho +0.113 over 1,251 hand-designed mechanisms, section 2, step 2) ranked distinct
  mechanisms, where the rating had real differences to see, and was not checked within side. It supports at most a
  weak family-level ordering.

**What changes in practice.**
1. Ask "who is forced to trade, and when" first, as before: it is still the strongest generator of hypotheses on the
   record. Its job is deciding what to test.
2. Rate mechanisms at the **family** level (one anchor and mechanism across its instruments and offsets). Use the
   rating to order families of similar statistical strength and to pick which family to dig next.
3. Before any narrative prior touches a ranking, convert it to a rank **within side x instrument**. Report long and
   short counts in every top list.
4. In EPS, m is the family-level, side-neutralised rating, or the neutral 1.5. A per-cell rating is never used.
5. Statistical persistence, placebos, independent history and dose-response decide a cell. A good story does not
   rescue a cell that fails them, and a poor story does not sink one that passes.
6. Rank any prospecting map on complete populations only: cells kept because they passed an OOS rule have persistence
   1.0 by construction and will crowd the top of any map.

## 12. Amendment: real size with a floor instead of a shadow stage

Added 16 November 2026 by operator order. Where an operator adopts it, it replaces checklist item 10 and step 10.3
(minimum-lot shadows); everything else, the gates of step 10.2 included, still applies. Record in each find record
which arming policy was used.

**Why.** A one-share shadow cannot produce evidence anyone can act on, and it is easy to leave in place forever. In one
conversion pass 78 of 84 armed candidates were shadows at about one share per leg. An edge that never executes at
meaningful size is worth zero ([C20](field-casebook.md#c20-an-edge-that-never-executes-is-zero)).

**Procedure.**
1. **Compute N_full for risk, not for edge** ([C11](field-casebook.md#c11-kelly-sizing-on-an-edge-found-in-the-same-history)):
   `N_full = min(0.004 * book / sigma_trade, 0.25 * book, 0.005 * ADV20)`. Quarter-Kelly is a cap only where the
   research estimated it positive; a non-positive Kelly estimate never zeroes a rule, because that is a shadow by
   another name.
2. **Set the floor.** Every armed rule trades at least `0.125 * N_full`. A rule that would step below the floor is
   recalibrated, never paused.
3. **Merge clones before summing risk** ([C19](field-casebook.md#c19-crowding-many-sleeves-one-bet)): rules whose
   replay entry masks overlap at Jaccard >= 0.4 within one economic family trade as one unit through a parent at
   combined size. One book's 223 rules collapsed to 144 units. Never fold a diversified ETF bet into a single stock.
4. **Cap risk at the book.** Deployed 1-sigma risk per family <= 0.6% of book; gross <= the book cap. Apply one
   proportional ex-ante scale so the p95 concurrent day fits, a per-pass proportional factor, and a hard clip at entry;
   log every clip.
5. **Print concurrency.** Replay the entry masks and report maximum and p95 concurrent gross. One book's calendar
   rules alone reached 1.93x the gross cap on a month-end plus Thanksgiving cluster and 1.0x at p95 before scaling;
   month-end and pre-holiday anchors pile up.
6. **Turn red-team verdicts into size.** Demote = half the floor; kill-exact-row = not installed.
7. **Print the falsifier beside the size.** A size from backtest sigma is still a backtest number: the first 20 fires
   per unit are the evidence (for example, recalibrate if their mean net is not positive). Audit that falsifier
   with [falsifier-integrity.md](falsifier-integrity.md) before the first fire.
8. **Wire a kill switch** for every unit (Gate D4) and run [live-firing-audit.md](live-firing-audit.md) before the
   first fire.

## Source and maintenance

Distilled from one desk's edge-discovery playbook, discovery log and practice-enrichment table of 13-15 November 2026,
its potential-edge board standard, and the round records of rounds 7 to 17 and the full-combination search. Only
aggregate statistics appear; no raw vendor data, accounts, machine paths or personal identifiers. New practices append
to the source playbook first; this reference is revised when the protocol, the ranking or the vein map changes, and the
revision is recorded in PROVENANCE.md.
