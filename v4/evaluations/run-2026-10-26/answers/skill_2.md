# E01–E12: decisions under the Trading Edge Lab skill

**SCOPE.** Twelve fictional cases, case facts only; no data, trading or code touched; each ends in a decision whose proof is its next test. Labels: **F** given (SOURCE FACT), **D** DERIVATION, **A** MODEL ASSUMPTION, **H** HYPOTHESIS; no TEST RESULT exists. Statistics: `research_stats.py`; C01–C20 are casebook records.

### E01. The pressure gauge (AUDIT)

**Ledger.** Speed, access, variance: none. Accuracy: second moment only, mean |10-day return| 9.0% against 5.0%, t 7.2 (F), untested against the coins' own volatility history. Direction: none, +0.1% at t 0.3 (F). Payer for direction: none. Execution net, trials: unknown.

**Decision.** Reject it as a long entry trigger. Use it, if at all, for sizing, stop width and option pricing, buying options only when implied volatility is below its forecast (field rule 1, C09).

**Reasoning.**
- Signed SE 0.1/0.3 = 0.33%: direction is ruled out above +0.75% per ten days at 95% (D); +0.1% would not pay a round trip (A).
- Big moves follow both ways, 1.8× normal (D). If absolute return scales with volatility, longs entered on it keep a mean near zero with about 3.2× the variance at fixed notional; volatility sizing cuts them to 0.56× (A, D).
- t 7.2 counts overlapping windows on six co-moving coins; the dependence unit is the date (D). Volatility clusters, so the gauge may add nothing over each coin's own realized volatility; 41% of the desk's volatility claims failed that lens (C01).

**Need.** Inputs and timestamps, correlation with trailing realized volatility, implied volatilities, costs, trial count.

**Next test.** Registered walk-forward, 2023–2025 held out: HAR on 1-, 5- and 22-day realized volatility, with and without the gauge, predicting next-10-day realized volatility; Newey–West with at least 9 lags, clustered by date. If it adds, a paired shadow arm of gauge-scaled sizing, scored in net money per unit of risk (C11).

**Would change it.** If the sleeve's own long signals in top-decile states beat its other entries by at least 1% per ten days net, |t| ≥ 2 by date, on the holdout, test the gauge as an entry filter. If it adds nothing over HAR, don't buy it.

**Verdict.** Buy signal REJECTED; volatility foresight INCONCLUSIVE · RETROSPECTIVE.

### E02. A better score that changes nothing (IMPROVE)

**Ledger.** Accuracy claimed (negative selection). The increment is AUC +0.004 and money −0.01% a month (F). Speed, access, variance: none. Payer: buyers of distressed names (H), mostly vetoed already. Execution net of adding it: negative before data costs (D). Trials: unknown.

**Decision.** Do not add the score. Keep the volatility veto frozen.

**Reasoning.**
- The decision metric, the veto's money gain, fell from +0.31% to +0.30% a month (F). AUC is accuracy, not value (C06); information already in the model adds nothing (C04).
- The score's rank correlation with 60-day volatility is 0.74 (F). ρ² ≈ 0.55, so roughly half its rank variation is volatility the veto already uses (D).
- The standalone −2.1% is against the market, not equally volatile names (F); against plain averages volatility alone passes everything (research protocol §3), so much of it may be volatility (H).
- Balance-sheet fields carry point-in-time traps: filing lags, restatements, delisted firms (C13).

**Need.** The paired standard error of the money difference, name-months, the standalone result against volatility-matched names, filing dates, delisting returns.

**Next test.** Registered. Residualize the score on trailing volatility within volatility quintile and size tier. Test whether the residual's worst decile lags volatility-matched names in 2015–2019 and again in 2020–2023. If it does, run a walk-forward money test of veto plus residual against the veto alone, by tier (small, micro, nano), paired by month with a block bootstrap.

**Would change it.** The residual raising the money gain by at least 10% net (+0.03% a month, the C04 bar), paired t ≥ 2, in two or more tiers and both eras, on point-in-time filings. Or value in another decision, such as a short book, tested there.

**Verdict.** Increment REJECTED at the pilot · OUT-OF-SAMPLE.

### E03. Patience at a price (IMPROVE)

**Ledger.** Speed, access: none. Accuracy: claimed via a better price. Payer: none; the limit fills when sellers push through it (adverse selection). Execution net: saves the open's spread (unmeasured), forfeits the no-fill branch. Trials: one offset, one window.

**Decision.** No. Keep buying at the next open. The limit is better per fill and worse per opportunity (C16).

**Arithmetic per signal, no-fills at cash** (D):
- Limit: 0.28 × 2.4% + 0.72 × 0% = +0.672%.
- Market: 1.00 × 1.1% = +1.100%.
- Difference −0.43 points a signal (−39%); over 400 signals, 268.8 against 440.
- Break-even: a 45.8% fill rate at +2.4%, or +3.93% per fill at 28%.
- The no-fills were the best signals (+4.0%, F), so the limit skips the runaways.
- On one clock, filled names would have returned (1.1 − 0.72 × 4.0)/0.28 = −6.4% from the open; a fill a few percent lower cannot make that +2.4%, so the limit's ten days probably start at its fill (H). Fills concentrate in falling names.
- A touched limit is not a fill. Queue position makes real fills rarer and worse (H).

**Need.** Both arms on a common clock (signal close to a fixed exit date), costs at the open, whether the fills were simulated, signal overlap.

**Next test.** Replay all 400 signals per opportunity on one clock: open entry; limit; limit then market at the day-3 close if unfilled. Pair by signal, bootstrap by week; then a forward paired shadow arm with real fills.

**Would change it.** A variant beating the open entry per opportunity by more than its costs, paired t ≥ 2 over at least 400 forward signals; for example, a shallow limit that fills 85% or more and saves the spread.

**Verdict.** REJECTED as a selection improvement (CONFIRMED per filled trade only) · RETROSPECTIVE.

### E04. Six point four (AUDIT)

**Ledger.** Speed, accuracy, access, variance: none named; no payer, so a pattern found by search. Execution net: probably negative: midpoint fills, no costs, daily turnover (F). Trials: 4.2 million (F), independent count unknown.

**Decision.** Reject the claim and allocate nothing. Cost the frozen rule, then paper-trade it.

**Calculations** (D; kurtosis read as raw; as excess, nothing changes):
- Daily Sharpe 2.6/√252 = 0.164; naive t 0.164 × √1512 = 6.37.
- Skew −1 and kurtosis 6 widen the Sharpe's error 9.4%: t ≈ 5.8.
- The expected best z of 4.2 million null trials is 5.14; with the cross-trial SD of 0.45, the expected best annualised Sharpe of skill-less combinations is 2.31, which the winner beats by 0.29. Noise alone gives a six-year SD of 0.41, so the search's 0.45 is mostly noise.
- Deflated Sharpe 0.74 < 0.95: selection alone can explain it. It passes only below about 33,000 independent trials.
- A round trip of k bps a day removes 0.0252·k/σ from the annual Sharpe (σ annual volatility, not given): at k = 10 and σ = 10%, 2.6 becomes 0.08 (A).

**Need.** Volatility, gross per unit of turnover, real spreads and impact, the trials' correlation, a point-in-time universe.

**Next test.** Cheapest and decisive: re-price the six years at the real touch plus impact at intended size (C17). If net Sharpe is below 1, drop it, as it fails deflation even at 1,000 effective trials (expected best 1.46, D). Otherwise, six months of forward paper trading at the real touch, code frozen by hash (C15).

**Kill rule.** Six-month forward net Sharpe below 0, which a true 2.6 produces under 5% of the time (SE ≈ 1.55, D).

**Would change it.** DSR of at least 0.95 net of real-touch costs on a documented trial count, then a forward record long enough to show Sharpe above 0: about 730 days if the truth is 1 (MinTRL, D).

**Verdict.** Claim REJECTED; strategy INCONCLUSIVE · HYPOTHESIS.

### E05. One registered test (AUDIT)

**Ledger.** Variance: a day of index risk into a scheduled decision (H). Shedder, payer: unidentified, so an unresolved pattern kept with stricter monitoring. Speed, accuracy, access: none claimed. Bad state: a surprise decision day. Co-losses: the book's equity exposure that day (not given). Execution net: +0.31% a trade after measured costs, real fills (F). Trials: one (F).

**Decision.** Approve 2%, sized on risk, once a joint stress check passes, with a decay rule registered now.

**Reasoning.**
- The cleanest evidence here: registered before data, no free parameters, one trial, nothing to deflate. Retrospective t 2.9, live t 2.6 on real fills (F); combined z ≈ 3.9 (D). The desk's |t| ≥ 3 discovery bar prices search; there was none.
- Live SE 0.12%, per-trade SD 0.81%, 95% CI +0.08% to +0.54% (D). Size on risk, not on the 0.31% (C11).
- At 2%, a trade's SD is 0.016% of capital and a 10% index fall costs 0.2% (D). About 7 decisions a year (46 in ~6.8 years) earn ~0.04% of capital a year (D): small risk, small gain, cheap to reverse.

**Need.** The book's exposure on decision days, the worst decision-day returns since 1998, slippage against size, the instrument.

**Next test.** (1) Joint stress: the book plus the 2% position on the five worst decision days on record. (2) Slippage at 2% against 0.5% over the next eight decisions.

**Kill rule (fixed now).** P&L needs ~42 decisions to detect full decay at 80% power (D), so check in stages: back to 0.5% if the post-raise mean is at or below 0 after 16 decisions (6% false alarm if the edge holds); retire if so after 24 (3%) (D).

**Would change it.** The joint stress breaching the book's daily loss limit, or slippage at 2% pushing the net mean below +0.2%.

**Verdict.** CONFIRMED · LIMITED LIVE.

### E06. Create: the Kestrel rebalance (CREATE)

**Ledger.** Access: a known clock in names too thin for large arbitrageurs, $3M a day (F, H). Variance: ten days of entrants' risk, held for trackers. Shedder and payer: index trackers, who must buy 9% of free float at the effective close (F) and accept the price because their mandate is tracking, not cost (H). Bad state: pre-positioned rivals, a market fall, deletions on bad news. Co-losses: hedged beta. Execution net: unknown. Trials: none.

**Strategy (H).** From the day after announcement, buy additions over nine days at ≤ 10% of volume, hedged with an index or peer basket; sell all of it into the effective-date closing auction, to the trackers. For deletions, buy in that auction only what five days at 10% of volume can exit (~$1.5M). Skip names with tracker demand under two days' volume or an announcement-day jump above the historical average premium.

**Economics** (D). 10% × $3M × 9 days ≈ $2.7M a name; four a quarter ≈ $11M gross (A). Tracker demand is 0.09 × free float: a $300M float means $27M, nine days' volume in one auction (A). Costs ≈ 25 bps round trip plus impact; require ≥ 50 bps gross per event, surviving doubled costs.

**Could lose.** Rivals buy first and sell to us; trackers trade early; additions leak before announcement; deletions keep falling; 8–20 events a year diversify poorly (A).

**Need.** Free floats, event counts, auction volumes, borrow, a hedge instrument, trackers' habits.

**Cheapest decisive test.** Event study on Kestrel's past rebalances (public lists, daily prices, auction volumes): additions from the open after announcement to the effective close, deletions from the effective close to five days on; excess returns net of 25 bps plus impact at 10% participation, by era, with the announcement-day share. MDE ≈ 2.8 s/√n.

**Kill rule.** Drop if the recent half of history's mean net excess is ≤ 0 at doubled costs; in forward shadow, retire after 16 events with mean net ≤ 0.

**Verdict.** HYPOTHESIS → research, then shadow.

### E07. Create: rain (CREATE)

**Ledger.** Variance: one region's drought (F). Shedder and payer: farm cooperatives (F); drought cuts their income and collateral together, so cover is worth more to them than its expected payout (H). Premium: unknown; our reservation price is low because drought is nearly independent of global equities: with CARA, π = (1/γ)·log E[e^{γL}] (D). Accuracy: burn analysis plus month-to-date station data (H). Access: a thin new venue large insurers ignore (H). Bad state: a drought season when several monthly contracts pay. Co-losses: few with equities; venue or settlement failure. Holdable: fully collateralised binaries (A). Trials: none.

**Strategy (H).** Post offers above burn value plus margin; size so a season of every contract paying costs at most 2% of the book, $100k (A); refresh quotes daily from station data. Unconventional: if settlement is the monthly total, a contract whose month-to-date rainfall has passed the threshold cannot pay, so any bid on it is near-riskless to hit, barring revisions or fallback-station rules.

**Calculations** (D). Each calendar month has 30 outcomes; 3 droughts in 30 gives a 95% interval of 3.5%–25.6%. Seller's net = price − p − costs: sell only where the bid clears the upper bound plus costs, or fit daily rainfall to narrow p. A climate trend could make 30 years understate drought (H).

**Could lose.** Understated p, clustered droughts, better-informed buyers, station errors, venue default, no exit.

**Need.** Rulebook (payout form, threshold inclusivity, revisions, fallback, margin, fees), quote and trade history, daily data.

**Cheapest decisive test.** Read the rulebook, then record every quote for two to three months without trading; compare bid-implied probabilities with each contract's upper bound plus costs.

**Kill rule.** No shadow book unless a third of contracts clear; in limited live, retire if payouts over 24 contract-months exceed premium by more than the modelled 95% season loss, or our sold contracts pay at ≥ 1.5× the modelled rate.

**Verdict.** HYPOTHESIS → research and quote recording.

### E08. Locking in gains (IMPROVE)

**Ledger.** Accuracy: momentum (slow updaters; archetype). Payoff: 8% of trades make 120% of profit (F): the mean lives in the right tail. The proposal adds no information, only reshapes the payoff. Execution net: extra exits add cost. Trials: unknown for 2.5 ATR and +15%.

**Decision.** Do not adopt; test it as a paired shadow arm against the plain 40-session hold (field rule 10).

**Reasoning** (D unless marked).
- The top 8% average 15× the mean trade (1.2/0.08). If the mean trade is +1% or more, the +15% target sits at or below the average big winner.
- The other 92% lose 0.2 of total profit (F), so the sleeve stays profitable only if exits remove under one-sixth of the winners' profit (1.2(1 − x) > 0.2), net of what the stop saves elsewhere.
- Win rate is not expectancy: a target turns a few big wins into many small ones. Less time in the market lowers drawdown; a smaller position does so without cutting the tail (H).
- Three years is one era (C12). On the desk's record, 159 of 159 significant trailing-stop and exit results were harmful, and a 1:6R profit cap cost 0.20 points a trade (C10).

**Need.** Net mean per trade and total return for both, average exposure, the top trades' distribution, costs.

**Next test.** Same signals, every available year, one change per arm (trailing stop, target, both) against the plain hold; paired by trade, net of costs, block bootstrap; plus the plain hold scaled to the proposal's average exposure, separating drawdown control from de-risking.

**Would change it.** An arm beating the plain hold in net mean per trade, paired t ≥ 2, at matched exposure, inside and outside 2019–2021. If drawdown is the real constraint, test a smaller size or a wide catastrophic stop the same way.

**Verdict.** Money effect INCONCLUSIVE (unmeasured); the field record predicts harm · RETROSPECTIVE.

### E09. Protecting the put seller (IMPROVE)

**Ledger.** Variance: a week of index crash risk (F). Shedder and payer: hedgers buying protection. Premium: steady two years (F); this book's reservation value is high, as its bad state is the equity book's. Bad state: a week below −5%, frequency unknown. Holdable: margin rises then. Co-losses: the whole book (F).

**Decision.** Reject the 3× stop: only the wing bounds the loss. Adopt spreads if their net premium beats a one-third-size naked sleeve and the book's reservation premium; else shrink or close the sleeve.

**Reasoning.**
- Two calm years say little: at a 1% or 2% weekly loss chance, 104 clean weeks happen 35% or 12% of the time (D).
- A gap jumps the stop, so it bounds nothing, yet it fires on ordinary dips (a one-week put can triple on a 2% fall as implied volatility rises; illustrative Black–Scholes, A), buying insurance back at its dearest, 2× the premium plus spread, in weeks that would have expired worthless.
- The wing caps the loss at 5% of notional less net premium, with no gap or path risk (D); its far out-of-the-money put is rich under steep skew (H).
- Hedge or trade less (mechanism 7): a third of the naked size loses the same 5% in a −20% week, less in a −10% week (1.7% against 5%), more only beyond −20% (D). The spread earns more only if the wing costs under two-thirds of the premium.

**Need.** Notional against capital, premiums, the 10% put's price, margin rules, book beta, crash-era option history.

**Next test.** Replay every crash and gap week on record at real bid and ask for four arms (naked, matched-stress naked, 3× stop, spread): weekly net premium, worst week, joint loss with the book in its worst 1% of weeks, margin path.

**Would change it.** Spread net premium below the book's reservation premium for the −5% to −10% band: close the sleeve.

**Verdict.** Stop REJECTED; spread INCONCLUSIVE · LIMITED LIVE (calm weeks only).

### E10. The thirteenth sleeve (AUDIT)

**Ledger (book).** Twelve sleeves, one bet (C19). Seven hold the same three mega-caps, the average correlation is 0.62, and 10 of 12 lost on one day (F). Co-losses: nearly total. Execution net: clones pay the spread repeatedly (H). New sleeve: accuracy (momentum archetype), payer slow updaters, likely co-losses with mega-cap technology (H), Sharpe 1.3 backtested only (F).

**Decision.** Do not add it now. Fix the book first: merge clones into one exposure budget, cap names and factors at book level, then judge the 13th by marginal value.

**Calculations** (D; equal weights and volatilities, A):
- Book Sharpe 1.0 × √(12/(1 + 11 × 0.62)) = 1.24, from 12/7.82 = 1.5 independent bets; twelve independent sleeves would give 3.46.
- A new sleeve helps only if its Sharpe exceeds its correlation with the book times 1.24. With correlation ρ to each sleeve, the hurdle is 1.53ρ: 0.95 at ρ = 0.62, 1.23 at 0.80.
- At equal weight with a true 1.3, the book reaches 1.27 (ρ 0.62) or 1.25 (ρ 0.80). With a true 0.65 at ρ 0.80, it falls to 1.18.
- Average correlation understates crash dependence: 10 of 12 lost together.

**Need.** Positions by name and factor, sleeve P&L, out-of-sample Sharpe ratios, the 13th's correlation on the book's worst days.

**Next test.** An exposure census: time-weighted gross and net by name, sector, technology beta and semiconductor beta, with identical-fill detection. Then the 13th's correlation with the book on the book's worst 5% of days.

**Would change it.** Correlation with the book below 0.3, overall and on bad days, plus an out-of-sample Sharpe above its 1.53ρ hurdle: then add it at risk-based size inside a book-level technology cap.

**Verdict.** "Independent" REJECTED (≈1.5 bets); the 13th INCONCLUSIVE · RETROSPECTIVE.

### E11. Loud chief executives (AUDIT)

**Ledger.** Accuracy claimed: heavy posting flags promotional management (H). Payer: buyers of attention stocks (H). Speed, access: none. Variance for a short: squeezes, in names at 3× market volatility (F). Execution net: unknown; borrow fees and recalls are not in the result. Trials: unknown, and the ten-post threshold looks chosen.

**Decision.** Do not start a short sleeve. A few companies, one year and volatility carry the finding.

**Reasoning** (D unless marked).
- Composition (C14): 2,108 of 3,400 events come from 14 companies, about 150 each in roughly 209 weeks, so the flag is a trait, not news. Weekly events with one-month outcomes overlap about four to one, so t −6.1 counts the same months repeatedly.
- Era (C12): 2,380 events fall in 2021, so the result may describe one year.
- Comparison: the benchmark is the market, not equally volatile names (F). Against plain averages, volatility alone passes everything (research protocol §3).
- A short in names with 3× volatility owns their right tail.

**Need.** Per-company results, events by year, borrow costs, point-in-time post histories (deleted posts, delisted firms), how the threshold was chosen.

**Next test (registered).** Re-score from the next open against volatility-matched names (same volatility quintile, tier and session). Take the first event per company per month, count each company once, drop the 14, and split 2021 from 2022–2024. Net out borrow.

**Would change it.** A volatility-matched, company-level lag of at least 3% a month with |t| ≥ 3 outside the 14, the same sign with |t| ≥ 2 in 2022–2024, and a positive result after borrow. Then a small shadow short book; a veto for long books is a cheaper first use (C02), with no borrow or squeeze risk.

**Verdict.** INCONCLUSIVE · RETROSPECTIVE.

### E12. Half a second (AUDIT)

**Ledger.** Speed: we read at 450 ms; the price adjusts over ~3 s (F), a lead of ~2.5 s, shrinking. Accuracy: our report-to-price map (H). Payer: slower traders and stale resting quotes. Execution net: +6 ticks a release after fees, real fills (F). Bad state: a misparse or agency correction.

**Decision.** Keep trading at current size as a decaying speed rent: fix cheap latency, fund no arms race until a capture curve prices it, fix the kill rule now.

**Calculations** (D). SE 6/4.1 = 1.46 ticks; per-release SD 11.3; 95% CI 3.1–8.9 ticks. Detecting a fall to 3 ticks needs ~112 releases at 80% power, so P&L warns late: monitor the mechanism.

**Reasoning.**
- The edge is against the fastest rival, not publication: a rival at 100 ms takes the early move and leaves us the tail (H).
- 450 ms is long for a machine-readable file: time each stage (publication, receipt, parse, decision, order, acknowledgement, fill), repair the dominant one, and pre-compute what is known in advance: schema, consensus, a surprise-to-order table (C18).
- Faster hardware pays only if the value captured per saved millisecond exceeds its cost (mechanism 9).

**Need.** Release frequency, tick value and contracts, latency breakdown, capture by release over time, rivals' latencies, infrastructure cost.

**Next test.** Replay the 60 releases' tick data at deliberate delays (50, 150, 300, 450, 900 ms) for the capture curve; regress capture on release number for decay so far.

**Would change it.** Capture concentrated in the first ~200 ms, with that speed costing more than the remaining expected P&L: plan retirement. A flat curve from 150 to 900 ms means interpretation drives it: keep, and invest in accuracy.

**Kill rule.** Retire if the last 12 releases average ≤ 1 tick net, or our fills land after 80% of the adjustment on three releases in a row.

**Verdict.** CONFIRMED · LIMITED LIVE.

### Receipt

**Status: UNVERIFIED.** Nothing ran on data; only the cases' arithmetic was checked; the missing proof is each case's next test. **Highest-value next action:** E10's exposure census (the book is one bet; positions already exist), then E12's delay replay before rivals finish their parsers.
