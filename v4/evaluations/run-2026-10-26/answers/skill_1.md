# E01–E12: decisions

I read `skills/engineer-trading-edge/SKILL.md` and its casebook, truth gates, ledger, research protocol, execution, foundations, mechanisms and validation references. Figures come from the case facts; DSR, MinTRL and power from the skill's `scripts/research_stats.py`. Tags: [D] derived, [A] my illustrative assumption, [H] hypothesis; "rule n" and "Cnn" cite the skill's field rules and casebook. Nothing traded, no market data fetched.

## E01. The pressure gauge

**Decision:** not a long entry trigger. At most a volatility input for sizing and stops, worth its fee only if it beats the coins' own volatility history.

**Ledger:** speed none; accuracy on the second moment only (t 7.2, no baseline); direction none; no payer for a direction bet. **Verdict as a buy signal:** NULL (ruled out above about +0.75% per ten days), RETROSPECTIVE.

**Reasoning [D]:**
- Signed +0.1% at t 0.3: standard error ≈ 0.33%, 95% interval −0.55% to +0.75% per ten days; detectable effect ≈ +0.9% at 80% power. "Big moves follow" is size, not sign (rule 1, C01).
- For roughly normal, zero-mean returns [A], σ ≈ 1.25 × mean absolute return: 11.3% in the top decile against 6.3%, 3.2× the variance. A long trigger buys 1.8× the swing for +0.1%; costs (not given) make it negative.
- Use: scale exposure by about 5.0/9.0 ≈ 0.56 in top-decile periods to hold risk constant; set stops in volatility units; buy option movement only where implied volatility is below the gauge's forecast (rule 9).
- The t of 7.2 likely rests on overlapping windows across six correlated coins: at most about 25 non-overlapping top-decile windows per coin.

**Next test:** walk-forward, non-overlapping: next-ten-day realized volatility on the gauge plus a HAR baseline (1-, 7-, 30-day). Then a paired shadow arm: same signals, gauge-scaled against current size, scored on net P&L per unit of risk and drawdown.

**Would change it:** direction: a registered holdout where top-decile entries add signed net return to the sleeve's own entries (|t| ≥ 2, same sign as discovery). Sizing: no increment over HAR means drop it and save the fee.

**Need:** formula, point-in-time history, vendor's trial count, costs, implied volatility.

**Status:** PARTIAL. Arithmetic done; HAR test and shadow arm not run.

## E02. A better score that changes nothing

**Decision:** do not add it; keep the volatility veto frozen.

**Ledger:** accuracy claimed, no increment over the incumbent; payer unchanged (the losers the veto already avoids); ratios tried unknown. **Verdict:** REJECTED as an addition, OUT-OF-SAMPLE (walk-forward pilot).

**Reasoning [D]:**
- Money is the decision metric (rule 6): the veto's gain went from +0.31% to +0.30% a month, −0.01 points (−3%). AUC +0.004 is a forecast score the book did not collect (C06).
- Rank correlation 0.74 with 60-day volatility puts about 55% (0.74²) of the score's rank variance in the volatility the veto already uses (rule 4, C04).
- The standalone −2.1% a month is against the market, not equally volatile names; a score this close to volatility passes that comparison on volatility alone.
- Adding it buys balance-sheet data with filing lags and restatements (point-in-time risk, C13) and another input to maintain, for no measured gain.

**Next test (if the researcher continues):** residualize the score on trailing volatility and the incumbent's crash probability; test whether the residual's worst decile lags volatility-matched names, by size tier, discovery and holdout apart. Then rerun the walk-forward veto under a rule registered before the fit: adopt only if money gain rises at least 10% (≥ +0.03% a month), paired t ≥ 2 across folds, net of costs.

**Would change it:** that rule passing, or the residual earning money where the veto is blind (low-volatility distressed names) or on another decision, such as position size.

**Need:** standard error of the money-gain difference, folds, tiers, ratios tried, filing dates.

**Status:** PARTIAL. Decision follows from the pilot as reported; residual test not run.

## E03. Patience at a price

**Decision:** no. Keep the market entry; the limit earns less per signal.

**Ledger:** the per-fill gain is selection by the fill, not information (rule 16, C16). **Verdict:** REJECTED per opportunity (CONFIRMED only per fill), RETROSPECTIVE.

**Per opportunity, no-fills at cash (0%) [D]:**
- Limit: 0.28 × 2.4% + 0.72 × 0 = +0.672% a signal (112 fills × 2.4 = 268.8 points over 400 signals).
- Market: 1.0 × 1.1% = +1.10% a signal (440 points).
- Difference: −0.43 points a signal, −39%.
- Break-even: at 28% fills the limit needs +3.93% a fill; at +2.4% a fill, 45.8% fills.
- The 72% that never fill are the winners (+4.0%). Check: 1.1 = 0.28x + 0.72 × 4.0 gives x = −6.4% for filled signals bought at the open. For +2.4% on the same exit date the bid would have to fill about 8.6% below the open, not near 1.5% under the close, so the arms probably used different windows or price bases; rebuild both on common dates before reusing these numbers.
- Idle cash earns nothing. Only if capital, not signals, binds does return per capital-day matter, and then the bid's three days of reserved buying power count.

**Next test:** paired replay of the 400 signals with a common exit date, both arms at the real touch (market pays the open's spread, the limit earns it), plus a "limit, then market on day 3" arm, logged as a trial.

**Would change it:** a limit policy beating market entry per opportunity, paired t ≥ 2 over at least 200 forward signals net of costs; or proof that capital binds and return per capital-day is higher.

**Need:** touch costs, each arm's return window, whether capital binds.

**Status:** PARTIAL. Arithmetic done; common-window replay not run.

## E04. Six point four

**Decision:** the claim fails. No purchase or allocation on this backtest. Get the trial log, re-price at real costs, settle only on data the search never saw (rule 15).

**Ledger:** speed, accuracy, access, variance blank; no payer; execution net blank (midpoint, no costs, daily turnover); trials 4.2 million. A pattern, not an edge. **Verdict:** claim REJECTED; strategy INCONCLUSIVE, RETROSPECTIVE.

**Calculations [D]:**
- Daily Sharpe 2.6/√252 = 0.164; naive t = 0.164 × √1,512 = 6.37. Skew −1 and kurtosis 6 widen the Sharpe's error by √1.197 = 1.094: t ≈ 5.8.
- Expected best of 4.2 million skill-less trials at the observed spread: 0.45 × 5.14 = Sharpe 2.31. The winner is 0.29 above it: DSR 0.74 < 0.95, so selection alone can explain it.
- Pure noise over 1,512 days gives a spread of about 0.41 (≈ 1/√6); the family's 0.45 is nearly all noise.
- DSR reaches 0.95 only if the combinations count as fewer than about 33,000 independent trials.
- Costs: daily mean = 0.164 × daily volatility; at an assumed 10% annual volatility [A], 10.3 bps a day. About 10 bps of cost per day of full turnover removes the edge; each bp a day costs 0.25 Sharpe.

**Next test:** (1) every trial's parameters and P&L, to estimate effective trials; (2) the frozen winner at real-touch costs and impact at our size, 1×, 2×, 3×; (3) if anything is left, a forward shadow with real fills; if the claim were true, MinTRL is 122 sessions.

**Kill rule:** drop if re-priced net Sharpe ≤ 0, or forward net Sharpe ≤ 0 after 126 sessions (about 5% likely if the claim were true).

**Would change it:** effective trials under ~33,000 with net Sharpe still high, then a forward record with PSR(0) ≥ 0.95.

**Need:** volatility, costs, capacity, trial correlations, data survivorship.

**Status:** PARTIAL. Deflation computed; costs and forward test not run.

## E05. One registered test

**Decision:** raise to 2%, stepping through 1% while costs at size are measured, with a kill rule fixed now. The cleanest evidence in this set, at small added risk.

**Ledger:** variance: index risk across the decision; payer possibly holders shedding that event risk beforehand [H], else an unresolved pattern under stricter monitoring; execution net measured on real fills; trials 1. **Verdict:** CONFIRMED, LIMITED LIVE.

**Calculations [D]:**
- Live: SE 0.31/2.6 = 0.12%, per-trade SD ≈ 0.81%, 95% interval +0.08% to +0.54%.
- Two independent registered samples: Stouffer z = (2.9 + 2.6)/√2 = 3.9. One parameter-free rule owes no deflation for its own search.
- About 6.8 decisions a year. If allocation is unlevered notional [A], 0.5% adds about 1 bp a year to the fund, 2% about 4 bps; at 2% a one-day SD is 1.6 bps of capital and a 5% adverse day costs 10 bps.
- Kelly (μ/σ² ≈ 47×) is meaningless; size for risk (rule 11).
- P&L cannot show decay soon: detecting a halved mean at 80% power takes about 214 decisions, roughly 30 years.

**Before raising (next test):** (1) costs and impact at 2% from the depth at past decision times, since +0.31% is net at 0.5%; (2) leave-two-out: does t survive dropping the two best trades; (3) the book's other long-index exposure on decision days (co-loss).

**Kill rule:** back to 0.5% if the 24 decisions after the raise average ≤ 0 net (3% likely if the true mean is +0.31%).

**Would change it:** costs at 2% eating over a third of the edge; the mean resting on one or two trades; decision-day co-losses breaking the stress limit; a change in how the bank announces.

**Need:** fund size, instrument, costs at size, the book's index exposure.

**Status:** PARTIAL. Record reviewed; costs at 2% and leave-two-out not run.

## E06. Create: the Kestrel rebalance

**Strategy [H]:** forced-flow liquidity. Buy additions over the ten-day notice at ≤ 10% of volume, hedged with the index or a member basket; sell into trackers' buying at the effective close. Buy deletions from forced sellers at that close; hold a fixed short window. Later: predict changes from the published rules.

**Who pays, and why:** index trackers' investors: the mandate pushes 9% of each entrant's free float through one known close at any price; deviating costs tracking error, so they accept a worse print, spread thin across their assets. We supply immediacy and inventory (warehousing); $20M fits capacity large funds ignore.

**Size and cost [D, A]:** demand = 0.09 × free-float value: at an assumed $300M float [A], $27M, nine days of the $3M volume in one auction. Ten percent of volume for nine days builds about $2.7M a name. Round trip: 25 bps spread plus impact and hedge; break-even run-up roughly 30–50 bps [A].

**What makes it lose:** rivals pre-positioning (run-up priced at the first open, a close crowded with sellers); trackers trading early; news, common in deletions; rule or notice changes; a poor hedge; demand small against volume.

**Cheapest decisive test:** event study of every past Kestrel change, point-in-time membership: abnormal return from the first open after announcement to the effective close and over the next ten sessions, net of 25 bps and size-scaled impact, clustered by rebalance date, split by era, plus pre-announcement drift (front-running).

**Decision:** research (stage HYPOTHESIS); no position before the event study.

**Kill rule:** drop if mean net capture per name ≤ 0, or positive only before the last eight rebalances; live, retire if the first eight live rebalances average ≤ 0 net.

**Would change it:** net capture above break-even, t ≥ 2 in the recent era: paper-trade the next two rebalances.

**Need:** free floats, changes per quarter, volatility, hedge instrument, announcement history.

**Status:** UNVERIFIED. A design; no data examined.

## E07. Create: rain

**Strategy [H]:** sell drought protection where the bid, net of fees, beats a conservative payout probability from the 30-year station record; hold to settlement; cap the worst loss.

**Who pays, and why:** farm cooperatives pay above expected payout to shed drought risk; a thin new venue is too small for reinsurers (access). Drought is plausibly unrelated to global equities [H], so it costs this book less than it costs the cooperatives, whose income falls with it.

**Pricing [D, A]:** seller's net per $1 payout = bid − p − fees. If the month fell below the threshold in 6 of 30 years [A], p̂ = 0.20, 95% interval 0.10–0.37 (Wilson); a seasonal gamma fit with trend, on all 360 monthly totals, narrows it. Loss per contract ≤ 1 − bid; droughts persist, so cap payouts over any three months at 2% of the book, $100k [A].

**What makes it lose:** a multi-month drought; a drying climate the history understates; informed buyers who see soil moisture and forecasts; contract semantics (station outage, revisions, threshold inclusivity); venue failure or margin calls; no exit at wide quotes.

**Cheapest decisive test:** before any trade, price each listed contract against the station history: loading (bid − fees)/p̂ with its interval by month, a trend check (last ten years against the first twenty), and payouts after heavy cooperative buying.

**Decision:** research (stage HYPOTHESIS), then sell small and capped where the margin clears; a forward record confirms nothing quickly (twelve months a year), so the margin and the cap carry the decision.

**Kill rule:** never sell where bid − fees is below the upper 95% bound of p; live, stop and re-estimate if 24-month payouts exceed the model's 95% upper count, or settlement or margin rules fail audit.

**Would change it:** bids clearing the bound with room start the program; bids below it end it.

**Need:** thresholds, quotes, depth, fees, contract terms, margin, the region's link to equities.

**Status:** UNVERIFIED. A design; no data examined.

## E08. Locking in gains

**Decision:** do not adopt. Reject the +15% target outright; run the trailing stop only as a paired shadow arm against the plain hold.

**Ledger:** exits change the payoff, not the forecast; the mean rides the right tail (8% of trades, 120% of profit). **Verdict on the proposal:** INCONCLUSIVE, RETROSPECTIVE; it reports win rate and drawdown, not money.

**Reasoning [D]:**
- With total profit P, the top 8% make +1.2P and the other 92% −0.2P. If exits remove a fraction κ of the winners' profit and save S on the rest, profit changes by S − 1.2κP. Cutting a sixth of the winners' profit needs S = 0.2P: the entire aggregate loss of the other 92%.
- A +15% cap on 40-session momentum trades hits exactly those winners (rule 10, C10).
- Win rate rising from 41% to 55% is what capping winners and banking small gains does; it says nothing about expectancy.
- A 30% smaller drawdown can come from less time in the market; the plain hold at 70% size cuts drawdown 30% too.
- If 2019–2021 also motivated the proposal, the backtest is in-sample.

**Next test:** paired replay on the same signals and capital: plain hold, stop only, target only, both; per opportunity, net of the extra exits' costs, on an era not used for design. Score net P&L, expectancy with its interval, Sharpe, drawdown at matched exposure, and the top trades' contribution per arm. Then the stop arm as a forward shadow, minimum 200 paired trades.

**Would change it:** an arm beating the plain hold on net P&L per opportunity (paired t ≥ 2) in both eras, or cutting drawdown more than the exposure-matched hold at equal net return.

**Need:** net P&L and expectancy under the proposal, costs, the design era, the winners' distribution.

**Status:** PARTIAL. Decomposition derived; paired replay not run.

## E09. Protecting the put seller

**Decision:** reject the stop. Move to the put spread now, sized so its maximum loss plus the book's equity loss in the same fall fits the stress budget; close the sleeve if the spread does not earn its keep.

**Ledger:** variance: weekly crash risk; shedder: hedgers buying protection; bad state: a sharp weekly fall, when the long-equity book also loses (co-loss); margin path unknown. Two calm years say nothing about the tail: +1 at 99% and −150 at 1% has mean −0.51. **Verdict:** INCONCLUSIVE, RETROSPECTIVE.

**The 3× stop [D, A]:**
- Nominal loss 2× premium, but no bound: a gap or 10% week makes the 5%-OTM put worth at least 5% of notional, 25× an assumed 0.2% premium [A]; the stop fills near 25×.
- High gamma: a 2–3% dip can triple a one-week put, so the stop fires on dips that expire worthless, buying back at peak implied volatility, where the premium is richest (C08).

**The put spread [D]:**
- Maximum loss per pair = 5% of notional − net credit, in any gap: a true bound.
- Cost: the 10%-OTM put is the most demanded protection and may eat much of the premium (quotes not given); losses from −5% to −10% still land in the book's bad state.

**Next test:** replay on historical option quotes over eras with crash weeks: naked, stop (filled at the next real quote), spread, and simply less equity (blueprint 7); score premium minus loss, worst week, margin path, and the book's worst ten weeks with and without the sleeve. Optional arm: sell only when implied variance is well above realized (C08).

**Would change it:** stop fills near 3× in crash weeks at low whipsaw cost (reconsider the stop); spread premium ≤ expected loss (close the sleeve); joint stress loss over the limit (cut size).

**Need:** premiums, quotes, implied and realized history, margin rules, sleeve size against the book.

**Status:** PARTIAL. Mechanics derived; replay not run.

## E10. The thirteenth sleeve

**Decision:** reject the thirteenth as proposed; fix the book first. It is about one and a half bets, mostly mega-cap tech.

**Ledger (book):** co-losses dominate: seven of twelve hold the same three stocks; ten of twelve lost on one day. The candidate adds the same factor (semiconductors, momentum) [H]. **Verdict:** diversification claim REJECTED; candidate INCONCLUSIVE, RETROSPECTIVE.

**Calculations [D]** (equal risk, Sharpe 1.0 each, ρ 0.62):
- Effective independent bets = 12/(1 + 11 × 0.62) = 1.53.
- Book Sharpe = 1.0 × √1.53 = 1.24; any number of such sleeves caps at 1/√0.62 = 1.27.
- Adding a 1.3 sleeve at equal risk: book Sharpe 1.27 at correlation 0.62, 1.25 at 0.8, no gain from about 0.85. Semiconductor momentum on a tech-heavy book may well sit there [H].
- These are backtested Sharpes; search and costs lower them (rule 15), and stress correlation exceeds the average.

**The book (rule 19, C19):** measure time-weighted exposure by name and factor across sleeves; find clones and identical fills paying the spread twice; merge the seven overlapping sleeves or cap exposure to the three names and tech beta; allocate by marginal contribution to book risk and stress loss, not standalone Sharpe.

**Next test:** on the same history, regress the candidate's daily P&L on the book's P&L and a tech factor: correlation, book-hedged Sharpe out of sample, P&L on the book's 20 worst days, and the book's stress loss with and without it.

**Would change it:** correlation with the book below about 0.3, hedged Sharpe ≥ 0.5 out of sample, flat or positive on the book's worst days: then admit at a small risk budget inside a factor cap.

**Need:** the candidate's P&L and trial count, the twelve's live Sharpes, sizes and exposures.

**Status:** PARTIAL. Portfolio arithmetic derived; candidate's correlations not measured.

## E11. Loud chief executives

**Decision:** no short sleeve. The headline looks like a few companies, one year and volatility.

**Ledger:** accuracy claimed; payer unnamed (attention-driven buyers? [H]); execution net blank (borrow, recalls, squeezes at three times market volatility); trials unknown (why "more than ten"?). **Verdict:** INCONCLUSIVE, RETROSPECTIVE.

**Reasoning [D]:**
- 62% of 3,400 = 2,108 events from 14 companies, about 150 each (rule 14, C14).
- Consistency check: as company-weeks, the 14 supply at most 14 × 53 = 742 events in 2021, so at least 1,366 fall in 2022–2024, which hold only 1,020 events. Distinct company-weeks cannot produce these counts; events must overlap (rolling seven-day counts taken daily, or one executive across several tickers). Either way 3,400 hides far fewer independent observations.
- 70% of events are from 2021: one era (rule 12).
- Lagging the market proves little for names three times as volatile; compare with equally volatile names (research protocol §3, C02).
- The t of −6.1 treats events as independent; if clustering cut the effective sample to a tenth, t would be about −1.9 [illustration].

**Next test:** re-score with (1) volatility-matched controls (same volatility decile, size tier, month); (2) one count per company, errors clustered by company and month; (3) the 14 names removed; (4) 2021 apart from 2022–2024; (5) point-in-time post counts, deleted posts included; (6) borrow cost and availability at each event.

**Would change it:** a lag surviving all six, say −2% a month or worse against matched names, |t| ≥ 3 in 2021–2022 and the same sign with |t| ≥ 2 in 2023–2024, outside the 14, net of borrow: then a small shadow short, or, cheaper, a veto for long books (no borrow; rule 2).

**Need:** event definition, company list, matched results, borrow data, the threshold search.

**Status:** PARTIAL. Composition arithmetic done; re-scoring not run.

## E12. Half a second

**Decision:** keep trading at current size, cut latency where cheap, and run it as a decaying speed rent under a kill rule; buy faster parsing only if a delay replay shows the extra capture repays it within a short life.

**Ledger:** speed: the parser acts 450 ms into a ~3 s adjustment (15% of the window); payer: slower traders and stale resting quotes; persistence: an arms race, two rivals investing; execution measured on real fills. **Verdict:** CONFIRMED, LIMITED LIVE.

**Calculations [D]:**
- 6 ticks, t 4.1, n 60: SE 1.46, per-release SD 11.3, 95% interval 3.1–8.9 ticks.
- Decay will not show in P&L soon: first 30 against last 30 releases detects only a drop of about 8 ticks, more than the edge; monitor the mechanism.
- Once rivals act first the price adjusts at their speed: capture depends on our latency against the fastest rival.
- Annual value = 6 ticks × tick value × contracts × releases a year; none given, so no speed budget yet.

**Actions:** precompute the order for every possible report value, leaving parse, lookup and send inside the clock (rule 18); bound parsed values so a misread places no order.

**Next test:** capture curve from the 60 releases' tick data: replay at 150, 300, 450, 600, 900 ms; markouts at 1, 3, 10 s; per release, time to first price change and share of the move left at our first fill.

**Kill rule:** pause and review if the first price change precedes our order on most of six consecutive releases, the share of the move left at our fill halves, or the rolling 12-release mean net capture is ≤ 0.

**Would change it:** an attainable faster latency worth more than its cost over a one-to-two-year life (invest); capture near zero at 450 ms against rivals' new speed (retire).

**Need:** release frequency, size, tick value, the cost of speed, rivals' latency.

**Status:** PARTIAL. Live record reviewed; delay replay not run.

**Overall status: PARTIAL.** Decisions rest on the case figures and the derivations shown; [A] numbers are illustrations; no test here has run. Highest-value next action: E09. Convert the naked weekly puts to spreads and run the crash-week replay; that sleeve can lose many times its premium in the same week the rest of the book loses.
