# Field casebook: what our desk measured

Twenty decision records from one research program and one live desk, October 2026. Each gives the claim, the method,
the result with its n, the verdict and the lesson for edge.

- **Research program:** 6,330 US stocks 2016–2026, 944 delisted segments, four size tiers (liquid; small, micro and
  nano by daily dollar volume). Each signal is compared with equally volatile names (same ATR% quintile, session and
  tier). CONFIRMED means discovery 2016–2022 |t| ≥ 3, the untouched 2023–2026 holdout the same sign with |t| ≥ 2, and
  Benjamini–Hochberg q < 0.10 within its family. "Pooled small tiers" is small, micro and nano together.
- **Live desk:** 558 paper books on live quotes with simulated fills, measured over four full sessions. Its numbers
  are observations of that desk, not market-wide estimates.
- **Verdicts:** CONFIRMED (the claim held under the registered test), NULL (no effect above the detectable size),
  REJECTED (the claim failed its test), INCONCLUSIVE (the test cannot decide yet).

## Contents

- Information: [C01](#c01-volatility-is-the-most-predictable-thing-on-a-chart) ·
  [C02](#c02-small-cap-buy-triggers-are-traps-negative-selection-pays) ·
  [C03](#c03-chartslector-warnings-work-in-thin-markets-buy-rules-do-not) ·
  [C04](#c04-nested-information-adds-nothing) · [C05](#c05-widely-watched-public-data-is-in-the-price) ·
  [C06](#c06-forecast-accuracy-is-not-economic-value) · [C07](#c07-the-llm-eye-adds-nothing-beyond-two-numbers)
- Risk and payoff: [C08](#c08-fear-priced-above-realized-volatility-paid-the-warehouse) ·
  [C09](#c09-luck-is-where-the-alpha-is-the-predictable-tail-did-not-pay-the-stock-buyer) ·
  [C10](#c10-exits-that-cut-the-tail) · [C11](#c11-kelly-sizing-on-an-edge-found-in-the-same-history)
- Evidence discipline: [C12](#c12-edges-are-era-bound) · [C13](#c13-point-in-time-the-leak-and-the-volume-flaw) ·
  [C14](#c14-reverse-splits-check-the-composition) · [C15](#c15-the-165-million-filter-rule) ·
  [C16](#c16-per-fill-or-per-opportunity)
- Execution and operations: [C17](#c17-the-cost-stack) · [C18](#c18-speed-late-opens-stale-prices-and-the-route-stage) ·
  [C19](#c19-crowding-many-sleeves-one-bet) · [C20](#c20-an-edge-that-never-executes-is-zero)

## Information

### C01. Volatility is the most predictable thing on a chart

Accuracy, second moment · **CONFIRMED** · desk research record, 2026-10-20 to 2026-10-26, direct-foresight study and
VIX Mood Ring family

| | |
|---|---|
| Claim | Chart components and market-mood readings forecast the next 20 sessions. |
| Method | About 14,000 component × tier cells scored on return and on realized volatility; a robustness lens against each stock's own past volatility (HAR). Mood readings on SPY, QQQ and IWM. |
| Result | Of 6,715 20-session volatility claims, 3,951 (59%) remain foresight beyond the stock's own volatility history. Only 3 of 854 single-signal return cells are in liquid names, and all 3 fail the re-matching lens. ChartsLector's VIX Mood Ring: 13 of 99 rows CONFIRMED, every one about volatility, none about returns; backwardation (VIX ≥ VIX3M) preceded higher SPY volatility, log +0.73 (t 4.6) in discovery and +0.47 (t 3.6) in the holdout, on 9 non-overlapping holdout windows. Market internals: no reading called the index's direction in both eras; weak readings preceded bigger swings. |
| Lesson | Information about the second moment is real and cheap. Route it to sizing, stops and option pricing, never to direction, and beat the stock's own volatility history before calling it foresight. |

### C02. Small-cap buy triggers are traps; negative selection pays

Accuracy, negative selection · buy triggers **REJECTED**, warnings **CONFIRMED** · desk research record, 2026-10-20
and 2026-10-25, component census, confluence holdout and money test

| | |
|---|---|
| Claim | Breakouts, moving-average crosses and indicator buy signals find small-cap winners. |
| Method | More than 100 triggers in every tier; pairs and three-condition rules mined on 2016–2022 and tested once on 2023–2026; a long-only money test that removes the synthesis model's worst tenth (equal weight, entry at the next open, 20 sessions, net of each name's round-trip cost). |
| Result | After a trigger the median small, micro or nano stock lags equally volatile names by 1 to 5 percentile points over 20 sessions (t −4 to −11) while both tails fatten. Pairs: 77 of 150 CONFIRMED, every one an avoid. Rules: small-cap warnings 197 of 200 CONFIRMED (52 beat every sub-rule); buys 158 CONFIRMED, 6 beat their sub-rules and add 0.1% to 0.3%; liquid buys 0 of 200, with 155 flipping sign. Money test: micro +0.53% per 20 sessions (t 5.1, 4 of 4 years), nano +0.66% (t 7.6), small +0.22% (t 1.8), liquid +0.06%. An equal-weight nano book lost 1.45% per 20 sessions; the veto halved the loss. |
| Lesson | The crowd's lottery tickets are easier to name than tomorrow's winners. Negative selection is often the cheaper information edge; it cuts losses rather than making a losing book profitable, so measure it in money on the book you hold, tier by tier. |

### C03. ChartsLector: warnings work in thin markets, buy rules do not

Access, thin attention · warnings **CONFIRMED**, buy rules **REJECTED** · desk research record, 2026-10-20,
ChartsLector family (14 published scripts, 16 hypotheses)

| | |
|---|---|
| Claim | ChartsLector's published scripts and hypotheses carry edge. |
| Method | Each script coded as written and frozen before scoring; every tier; each hypothesis one pre-registered one-sided test, Holm-adjusted. |
| Result | 84 cells CONFIRMED, 68 of them warnings. By tier: nano 36, micro 18, pooled small tiers 20, all tiers 8, small 1, liquid 1 (and that one fails the re-matching lens). Strongest: entering far above the day's low, −2.1 points in the pooled small tiers (t −13.2); his stage-exhaustion event, −7.5 points in nano with 19 more bottom-5% losers per 100. Hypotheses: 1 SUPPORTED (carried by nano), 14 NOT SHOWN, 1 NOT TESTED; his full entry stack showed nothing. |
| Lesson | A practitioner's warnings can encode real experience of losers while his entries carry none. Access edges live where the marginal participant's attention and capacity are thin, so every study covers every size tier, micro and nano included. |

### C04. Nested information adds nothing

Accuracy, increment · **REJECTED** · desk research record, 2026-10-26, SEC-V+ (pre-registered addendum)

| | |
|---|---|
| Claim | Adding ChartsLector's four grade-A warnings to the engine's own-volatility veto (SEC-V) raises its money gain by at least 10%. |
| Method | The incumbent's population (1,858,428 sample rows), walk-forward folds 2018–2022, threshold rule and money test; decision rule registered before the fit. |
| Result | Walk-forward money gain, % per 20 sessions: pooled small tiers 0.091 against 0.103 for the veto alone; nano 0.251 against 0.251. AUC +0.003; veto share unchanged (16.6%, 15.4%). No member, and no refit without one, reached the bar. The incumbent itself earned +0.10% (t 0.7) in the pooled small tiers and +0.25% (t 2.2) in nano walk-forward; its forward test needs 40 screen dates and 200 vetoed name-days. |
| Lesson | A signal confirmed alone can add nothing when its information is already inside the model, here the stock's own volatility. Test the increment over the incumbent on the decision metric. |

### C05. Widely watched public data is in the price

No speed, accuracy or access · **NULL** for large, stable effects · desk research record, 2026-10-25 and 2026-10-26,
families cot, ftd and peer

| | |
|---|---|
| Claim | CFTC positioning, SEC fails-to-deliver and gaps to correlated peers forecast returns. |
| Method | Point in time from public release dates (CFTC reports used from the first session after release; some arrived seven weeks late); the program's rule; power stated. |
| Result | Positioning: 0 of 1,308 rows CONFIRMED. 52 rows reached discovery \|t\| ≥ 3; the same scorer on random-walk prices gave 53. About 76 and 41 non-overlapping 20-session windows, so only \|ρ\| above about 0.34 and 0.31 could pass. Fails-to-deliver: 0 of 30 return cells, none even in discovery; 16 of 24 continuous cells foresee volatility. Peer groups cleaned of twin tickers: 0 of 36; three passed discovery and failed the holdout. |
| Lesson | Scheduled public data that many desks read is priced unless we read it sooner, process it better or hold a bet others cannot. State the smallest effect the test could detect; below it a null is INCONCLUSIVE. |

### C06. Forecast accuracy is not economic value

Accuracy · **REJECTED** as a money improvement · desk research record, 2026-10-25, machine eye 2.0 and the engine
comparison

| | |
|---|---|
| Claim | A three-seed ensemble of the chart network improves the book. |
| Method | Model hashes frozen before any test-era number; decile spreads net of costs on the 2023–2026 holdout. |
| Result | Rank IC rose in every tier (pooled small .110 → .119, nano .178 → .186, micro .097 → .106, liquid .029 → .034); the net decile spread did not (micro +2.65% → +2.82%, nano +3.10% → +2.65%, pooled small +1.94% → +1.85%). In the engine comparison the model with the better AUC (0.757, 0.760) was the worse money screen (+0.031% against +0.095% per 20 sessions in the pooled small tiers; +0.138% against +0.243% in nano). The single network's liquid ranking was real (IC 0.029, t 2.9) and its net decile spread −0.62%. |
| Lesson | Score every model change in money, net of costs, on the decision it changes. IC and AUC can improve where the book cannot collect. |

### C07. The LLM eye adds nothing beyond two numbers

Accuracy, claimed · **NULL**, ruled out above +0.045 · desk research record, 2026-10-20, pooled re-analysis of seven
chart-reading studies

| | |
|---|---|
| Claim | LLM readers see edge in charts that code does not. |
| Method | 3,001 reads by 186 reader agents on 2,642 charts; the readers' rank correlation with the next 20 sessions beyond a two-number baseline (closeness to the 250-day high minus 20-day volatility); week-clustered bootstrap. |
| Result | +0.003 [−0.046, +0.052] on 1,887 random-draw charts. Ten simple price features explain 69% of the readers' ranking; beyond them the readers chase the last one to three months' winners, which did not pay. The readers share one opinion (residual correlation 0.78 to 0.82). On charts dated after the readers' training cutoff the estimate is −0.023 (706 charts). |
| Lesson | An LLM's chart read is simple features plus a momentum habit, and signal on charts it may have seen can be memory. Many LLM agents agreeing is one observation. |

## Risk and payoff

### C08. Fear priced above realized volatility paid the warehouse

Risk warehousing · **CONFIRMED**, few episodes · desk research record, 2026-10-20, market-extremes and
credit-stress studies

| | |
|---|---|
| Claim | When implied variance sits far above realized, index returns are higher over the next one to three months. |
| Method | Top decile of VIX² minus 21-session realized variance; walk-forward 2001–2026; time-shift null. |
| Result | DIA +177 bp over 20 sessions (t 2.4, 20 of 21 years) and +489 bp over 60 (t 5.2, 44 episodes); QQQ +128 and +310 bp; SPY 2017–2026 +183 bp over 20 (shift p 0.01). Financial stress points the same way (ρ +0.19, t 3.0). About three to four independent episodes a year, and the rule was chosen after looking at 1999–2016. A candidate on timing: the first VIX close above 30 (16 events) was followed by DIA −2.4% over 250 sessions against a +6.2% base. |
| Lesson | The premium goes to whoever holds risk after fear is priced and persists, not at the first spike. Name the payer (hedgers buying protection), size for this book's own bad state, and expect years before a forward record confirms it. |

### C09. "Luck is where the alpha is": the predictable tail did not pay the stock buyer

Accuracy on the tail, in fact volatility · **REJECTED** as a stock buy list · desk research record, 2026-10-20,
upside catalog, tail-pay test and exits

| | |
|---|---|
| Claim | Signals that raise the odds of a +50% run pay on average. |
| Method | Registered upside catalog (runner rate raised in both eras); the mean 20-session return of each runner cell; five exit policies per cell; a convex-payoff lens. |
| Result | 582 cells raise the runner rate in both eras, and 86% of them add even more blow-ups. Of 560, the mean return beats equally volatile names in none and lags in 34; the typical stock lags in 536. Better exits halve the shortfall (−0.27% against −0.56% per trade) and never reverse it. A call-like payoff beats equally volatile names in 535 of 560 cells, and a put-like payoff in 550: the signals foresee movement both ways. A model of the chance of a +50% run ranks the typical stock backwards (IC −0.10). |
| Lesson | A predictable tail is a volatility forecast. To be paid by it, hold a payoff shaped like the tail, priced below what the forecast implies; the stock buys both tails and a lagging middle. |

### C10. Exits that cut the tail

Payoff shape · **REJECTED** · desk research record, 2026-10-18, execution-knowledge review of prior desks' studies;
2026-10-20, momentum trade test

| | |
|---|---|
| Claim | Stops, trailing stops, targets and early exits improve daily and weekly holds. |
| Method | Prior desks' train sweeps then out-of-sample tests with BH over 772 tests (figures copied from their reports, not rerun); a tight-stop momentum trade on the 2023–2026 test era, net of each stock's spread. |
| Result | 159 of 159 BH-significant trailing-stop and exit results were harmful; sweeps improved monotonically toward the plain fixed hold. A five-day first-leg exit against a 20-day hold: −1.17 points per trade (t −23.5, n 76,980). A 1:6R profit cap: −0.20 points (t −6.63, n 76,896). The tight-stop momentum trade lost after costs in every bucket; its stop was hit about 80% of the time. |
| Lesson | When a minority of large winners carries the mean, an exit that truncates the right tail can turn a positive expectancy negative. Test every exit against the plain hold on the same signals. |

### C11. Kelly sizing on an edge found in the same history

Sizing · **REJECTED** · desk research record, 2026-10-20, Kelly sizing study

| | |
|---|---|
| Claim | Sizing by estimated edge beats equal weight. |
| Method | Walk-forward comparison against equal weight in both eras; probability of backtest overfitting across settings. |
| Result | Ruled out above +0.65% per 20 sessions in liquid names (about +0.8% in small); a significant loss in 2017–2021 (−1.0%, t −2.4); probability of backtest overfitting 0.70 for any chosen setting. An earlier book's in-sample edge asked for 13.5× leverage, and half of that lost 47.7% a year in 2022–2026. Inverse-volatility weights also trailed equal weight among small-cap momentum picks (−0.73%, t −2.2, and −0.97%, t −2.7, per 20 sessions). |
| Lesson | Size for risk, not for estimated return, and never lever an edge estimated on the history that found it. |

## Evidence discipline

### C12. Edges are era-bound

All sources · **CONFIRMED** · desk research record, 2026-10-20 and 2026-10-25, prototypes, confluence holdout and
robustness lenses

| | |
|---|---|
| Claim | An edge found on 2016–2022 holds on 2023–2026. |
| Method | Discovery and holdout eras scored separately; bear-market, calendar and factor lenses. |
| Result | Chart texture (a few huge volume days dominating three months) and the trade-count surge were weak in 2016–2022 and very strong in 2023–2026 (t −10). Liquid buy rules mined on 2016–2022: 0 of 200 CONFIRMED later, 155 flipped sign. Winner prototypes learned from 2017, 2019 and 2021 became loser shapes (one: −16.7 per 100, t −7.7). Smooth momentum held in every tier and reversed in bear regimes. January flips 91 edges; December at least doubles 99. |
| Lesson | An edge born of one crowd's behavior lasts as long as that crowd. Test by era and regime, prefer edges that hold in both, and register a decay monitor before deployment. |

### C13. Point in time: the leak and the volume flaw

Evidence · leak fenced and flaw immaterial, **CONFIRMED** · desk research record, 2026-10-20 and 2026-10-25, data
hygiene addendum and volume audit

| | |
|---|---|
| Claim | Every input was known at the decision time. |
| Method | Truncate-and-recompute proofs per table; a lineage audit of each column; rerun of models and rules with suspect rows removed. |
| Result | Earnings-anchored VWAPs and sector strength existed only for today's large names, so in small caps they marked future winners; 48 leaky rows were quarantined. Split-adjusted volume rounded to zero before large later reverse splits: 74,962 bars in 227 segments, 0.25% of holdout rows (nano 0.95%). With the flaw removed every model kept its size (network nano IC 0.178 → 0.177), one setup verdict was lost, and the nano veto stayed strong (+0.66% → +0.58%, t 6.4). Earlier audits found a table reading today's index membership, 31 corrupted bars (one call scored 1,337R) and recycled tickers spliced into one series. |
| Lesson | A field that exists only for today's survivors is a time machine. Audit lineage, measure the exposure, rerun without the flaw, and only then trust or discard the result. |

### C14. Reverse splits: check the composition

Evidence · **CONFIRMED** narrowed to repeat splitters · desk research record, 2026-10-25, reverse-split verifiers

| | |
|---|---|
| Claim | After a reverse split, small caps lag. |
| Method | The first coarse score; then re-matching to the ten most similar names by volatility, company-level counts and a test against each stock's own volatility history. |
| Result | First score: −20.1 points in small caps (t −5.4). Finely matched: about −6, mostly repeat splitters (−16; first-timers about −4, not significant). Counting each company once it is weak (t −1.0), and the raw mean gap is not significant (−2.7%, t −0.5) because post-split squeezes offset 14 to 16 more bottom-5% losers per 100. Extra volatility beyond the stock's own history survives only in nano (+0.12 to +0.19 log points, t 4.5 to 7.2). |
| Lesson | A strong headline can be a few repeat names. Count companies as well as events, match finely, and test against the stock's own history before sizing a warning. |

### C15. The 16.5-million-filter rule

Evidence, search · **INCONCLUSIVE** · desk research record, 2026-10-25, CCI correction pullback (idea credited to
@onlybreakouts)

| | |
|---|---|
| Claim | `Lowest(CCI(27), 18) < −100` was the best long-entry filter among 16.5 million tested on NASDAQ. |
| Method | Wrapped in a long-only rule set (trend filter, a CCI trigger, a 2-ATR stop, a 3R target, a 20-bar time stop); not backtested; run as a shadow lane that records forward fills only. |
| Result | No forward record yet. Derivation: 16.5 million independent null trials have an expected best z-score of about 5.4 (`research_stats.py emax --trials 16500000`); correlated filters count for fewer. |
| Lesson | The winner of a large search carries the search's maximum. Get the trial count, deflate, and settle it only on data the search never touched. |

### C16. Per fill or per opportunity

Evidence, selection · **REJECTED** as a selection edge (**CONFIRMED** per filled trade) · desk research record,
2026-10-20, replay of the desk's read; 2026-10-18, execution-knowledge review

| | |
|---|---|
| Claim | Waiting for a pullback beats buying now. |
| Method | Paired replay of the desk's calls in both eras and both universes; per filled trade and per listing. |
| Result | Filled pullbacks beat filled buy-now calls by +0.142R per filled trade [+0.100, +0.184], 10 of 10 years. Only about 31% of pullbacks fill against 91% of buy-now calls; per listing the difference is −0.017R (t −0.6) in liquid names and −0.069R (t −2.0) in small. A structure-free market reproduces the per-fill edge (+0.19R). A prior desk's patient-entry audit: +47.98% on 19 fills became +24.64% per opportunity once its 18 no-fills counted as cash. |
| Lesson | A fill is selected information. Score every policy per opportunity, with no-fills and skips at their cash value. |

## Execution and operations

### C17. The cost stack

Execution net · **CONFIRMED** as measured · desk research record, 2026-10-25, sleeve baselines and options audit

| | |
|---|---|
| Claim | The simulator's costs describe the desk's real costs. |
| Method | Every fill re-priced against the real NBBO where an audit row existed; option fills against the quote mid at submit; post-fill markouts at 5 and 30 minutes. |
| Result | On 2,004 audited fills the simulator charged 2.45 bps against the real mid, where crossing the real touch costs 5.75 bps. Option half-spreads cost $88,218 on 52 fills (175.9 bps of notional). 57% of four LEAPS sleeves' bill came from a data defect: a T-bill rate read as 40.7% moved the 0.80-delta strike to 842, and the sleeves bought a 0.28-delta call at a 13.5%-wide quote. Genuine 0.80-delta LEAPS half-spreads averaged 0.96% of premium (n 6) against 0.70% assumed. In 26 sleeves costs exceeded the size of the pre-cost result, and 8 went from a pre-cost profit to a net loss. The equity mid moved 11.0 bps against the position 30 minutes after fills (n 9,838; −6.3 bps side-balanced). |
| Lesson | A simulator's cost is a hypothesis: price costs at the real touch, bound every input (a 40% T-bill rate is a defect, not a signal), and drop a strategy whose costs exceed its gross. |

### C18. Speed: late opens, stale prices and the route stage

Speed, execution · **CONFIRMED** as measured; route fix verified in replay · desk research record, 2026-10-25 and
2026-10-26, sleeve baselines, equity audit and the open-pass fix

| | |
|---|---|
| Claim | Decisions reach the market while their information is fresh. |
| Method | Decision, order and fill timestamps from the hash-chained ledger; fills against the official open and against the bar the decision used. |
| Result | Orders decided at the open filled a median 5.8 to 7.5 minutes after 09:30 (2,893 orders) and paid +16.6 bps over the official open after removing QQQ's move (n 1,083). One-hour sleeves decided a median 29 minutes after their bar closed; fills cost +2.0 bps when decided within 30 minutes and +17.0 bps at 30 to 60. 961 of 11,338 equity fills had a decision price more than 1% off the live quote. The open's route stage re-measured spreads one paced request at a time (181 to 241 s, 41–55% of the pass); computed the evening before, it took 10.7 s instead of 240.5 s in a replay of one open, the first order left at +17.6 s instead of +245.2 s, and all 1,648 fills were identical. |
| Lesson | Latency is part of the speed edge. Measure decision-to-fill against the capture window, compute what is known before the clock starts, and repair the dominant stage. |

### C19. Crowding: many sleeves, one bet

Portfolio · **CONFIRMED** as measured · desk research record, 2026-10-25, sleeve baselines and the macro and options
audits

| | |
|---|---|
| Claim | Hundreds of sleeves diversify the book. |
| Method | Time-weighted exposure at cost by underlying and direction across all sleeves; identical-fill detection. |
| Result | QQQ long was held by an average of 55 sleeves, 31% of the desk's average gross; Nasdaq-100 and semiconductor beta together were 41%. 47% of gross sat opposite another sleeve's position. 20 groups of 46 sleeves had identical fills; five option clones counted one TQQQ position five times ($218,376 of the "gains given back"). That family's $424k giveback was core leverage held through one Nasdaq drop, not an exit failure. |
| Lesson | Count exposure across the book before adding a strategy. Clones and offsets turn many strategies into one bet and pay the spread twice. |

### C20. An edge that never executes is zero

Operations · defects **CONFIRMED** and fixed with tests · desk research record, 2026-10-26, Edge audit fixes 1 and 2

| | |
|---|---|
| Claim | Every enabled sleeve trades as specified. |
| Method | The Edge audit of all 571 sleeves against the record; each defect reproduced, fixed with a failing test first, and merged after the full suite. |
| Result | 157 sleeves were silent and 81 blocked. Fixed: crypto entries blocked by a stale entry clock; 52 lanes running with their data producer switched off; option decisions dropped after every weekend and holiday (54 failures across 18 sleeves on one Monday; 21% of sessions follow a non-trading day); a factor book deciding months on tapes missing 30 of 550 names; a data-host error retried 792 times in one outage; a scorecard ignoring the marks of open positions. One audit premise was falsified once recorded: a "stale" feed had served same-session bars for 51 decisions. Full suites: 2,276 and 2,282 tests passed. |
| Lesson | Prove a strategy runs as specified on live inputs before judging its edge. A silent sleeve is not a null result, and recording beats assuming: a premise can be wrong. |
