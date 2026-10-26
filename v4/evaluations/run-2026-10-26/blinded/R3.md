These answers use only the stated facts and my own reasoning; I opened no files, skills or data. Illustrative assumptions are marked. Nothing was tested, so every decision is UNVERIFIED until its next test runs.

## E01. The pressure gauge

**Decision:** Don't use it as a long entry trigger. At most, use it as a volatility input that cuts position size.

**Reasoning:** The gauge forecasts how large moves will be, not their direction. Top-decile readings bring 9.0% average absolute ten-day moves against 5.0%, but the signed return is +0.1% (t 0.3), indistinguishable from zero. Even at face value, any round trip above 10 bps loses money, while risk per trade rises about 1.8 times (9.0/5.0). Big moves follow, but in both directions. The t of 7.2 is probably overstated unless corrected for overlap: daily readings with ten-day windows count each move up to ten times, and six large coins move together. Volatility clustering is real, but free trailing realised volatility captures it too.

**How to use it:** In top-decile states, scale exposure by about 5.0/9.0 ≈ 0.56 to keep risk per trade constant, and widen stops to match. Pay for the gauge only if it beats free volatility measures.

**Need:** point-in-time (not backfilled) history, the formula, how t was computed, our costs, and the gauge's price.

**Next test:**
1. Regress future ten-day absolute returns on the gauge plus trailing realised volatility, with overlap-robust errors.
2. Within top-decile readings, measure signed returns in our momentum direction, out of sample.
3. Compare sizing by the gauge with sizing by realised volatility, on Sharpe ratio and drawdown.

**What would change it:** If top-decile readings that agree with our momentum signal earned more than about 1% per ten days net, with an overlap-robust t above 3 in both halves of the sample, I would use the gauge to filter momentum entries, never as a standalone buy. If it adds nothing beyond realised volatility, drop it.

## E02. A better score that changes nothing

**Decision:** Don't add it. Keep the volatility veto, and test separately the part of the score that volatility doesn't explain.

**Reasoning:** The veto's job is money, and its gain went from +0.31% to +0.30% a month: no change. The AUC rise of 0.004 is tiny. AUC also scores the whole ranking, while the veto acts only on the worst 15%, so re-ranking names in the middle lifts AUC without changing a decision.

The standalone result (worst decile −2.1% a month, t 4.0) answers a different question. At a rank correlation of 0.74, volatility already explains roughly 0.74² ≈ 55% of the score's variation, and volatile small caps are what the veto already removes. What matters is the incremental set: names the combined model vetoes that volatility keeps, and the reverse. The pilot says those swaps net to zero. Meanwhile the score adds lagged, restated balance-sheet data, more moving parts and more room to overfit.

**Need:** the number of crash events for a DeLong test (with a few hundred, 0.004 is probably about one standard error), the money gain's standard error, the pilot's length, and whether the 2015-2023 accounting data were point-in-time.

**Next test:** Orthogonalise the score against trailing 60-day volatility, then:
1. Measure the residual's worst-decile spread.
2. Walk forward on the disagreement set: compare forward returns of newly vetoed and newly released names, at cut-offs of 10%, 15% and 20%.
3. Check stress periods, and names whose histories are too short to measure volatility well.

**What would change it:** Either of two results would justify adding the score, or running it as its own signal:
- newly vetoed names underperforming released ones by enough to lift the veto's gain by at least about 0.05% a month (walk-forward t above 2);
- the residual earning a spread with t above 3 after costs.

## E03. Patience at a price

**Decision:** No. Keep the market entry. The limit variant earns less per signal. Its higher return per fill comes from which trades fill, not from an edge.

**Arithmetic (per signal; cash earns zero):**
- **Market:** 1.00 × 1.1% = **1.10%**, or 440 points of position size over 400 signals.
- **Limit:** 0.28 × 2.4% + 0.72 × 0 = **0.67%**, or 112 fills × 2.4 = 269 points.
- **Shortfall:** 0.43 points per signal (−39%), or 171 in total.
- **Break-even:** a 46% fill rate at 2.4% per fill (1.1/2.4), or 3.9% per fill at a 28% fill rate (1.1/0.28).

**Reasoning:** A bid below the market fills when the price falls, and misses the names that run. The 72% it missed returned +4.0%, the best trades in the set. Comparing per fill uses the wrong denominator, because unfilled signals earn zero. Sizing fills up 3.6 times to use the idle cash fails too: nobody knows which bids will fill, and fills cluster in sell-offs, so leverage would peak at the worst time.

**Data check:** Suppose market entries averaged 1.1% overall and 4.0% on the 288 unfilled signals. Then they averaged (440 − 1,152)/112 = −6.4% on the 112 filled ones, where the limit earned +2.4%. A bid only 1.5% lower can't open an 8.8-point gap unless fills came on big gap-downs, the windows or reference prices differ, or the data are wrong. The decision doesn't rest on this; it follows from each variant's own P&L.

**Need:** paired returns to a common exit date, costs for each entry type, and whether capital is constrained.

**Next test:** Recompute all 400 signals as pairs with identical exit dates. Then test small offsets (0.25-0.5%), and a limit that converts to a market order after one session.

**What would change it:** A limit variant beating the market entry by at least 0.2 points per signal on paired data, with t above 2 out of sample.

## E04. Six point four

**Decision:** The claim is false. Don't license or allocate on this evidence.

**Reasoning:** The naive t is 2.6 × √6 = 6.4. After 4.2 million trials, though, the benchmark is luck's best result.
- **Noise maximum:** The expected best of 4.2 million independent null draws is about 5.1 standard deviations, which at 0.45 dispersion is a Sharpe of about 2.3. The winner beats luck by about 0.3.
- **Deflated Sharpe:** With skew −1 and kurtosis 6 the standard error is about 0.45, so the 0.29 margin is 0.64 standard errors: roughly 74% confidence, against 95% needed. Correlated trials would lower the bar; the effective count isn't shown.
- **Bonferroni:** The 5% hurdle for 4.2 million tests is t ≈ 5.6. Non-normality adds 9% to the standard error, bringing t to about 5.8. That is a bare pass, valid only if 4.2 million counts every variant, and shows "not zero", not "2.6".
- **Shrinkage:** Six years carry sampling noise of 1/√6 ≈ 0.41. So at most (0.45² − 0.41²)/0.45² ≈ 18% of the variance across combinations is real, and the selection-adjusted Sharpe is about 0.18 × 2.6 ≈ 0.5 gross, if the family mean is near zero.
- **Costs:** With full daily turnover, break-even is a daily round trip of SR × σ/252: at an assumed 10% volatility, 10 bps on the claimed Sharpe and 2 bps on the shrunk one. Real spreads erase it, and midpoint fills may be capturing bid-ask bounce.
- **Tails:** Skew −1 and kurtosis 6 are crash risk the Sharpe hides.

**Need:** the distribution of all 4.2 million Sharpes, correlation between trials, spreads, volatility, capacity, and whether the count is complete.

**Next test:** Freeze the rule, then run it on post-search data or a fresh universe at bid and ask with impact. Check that neighbouring parameters form a plateau, not a spike.

**What would change it:** A held-out net Sharpe of at least 2 over one year, or 1.4 over two (t ≥ 2), with real fills and stable neighbours, would earn a small pilot.

## E05. One registered test

**Decision:** Raise the allocation to 2%, with a kill rule and a cost check at the new size.

**Reasoning:** This is the clean case. It was registered before the data, has no free parameters, was tested once with no variants, and trades on real fills net of measured costs. The backtest (t 2.9) and the live record (t 2.6) are independent, giving a combined Stouffer z of (2.9 + 2.6)/√2 ≈ 3.9.

**Live arithmetic:**
- The standard error is 0.31/2.6 ≈ 0.12% per trade, so per-trade volatility is about 0.12 × √46 ≈ 0.81%.
- The 95% interval, +0.08% to +0.54%, excludes zero.
- At roughly 7-8 decisions a year (46 since 2020), that is about 2.2-2.5% a year on notional at about 2.2% volatility. The Sharpe is near 1, with capital in the market about eight days a year.

**Size:** At 2% of capital, per-trade volatility is about 0.016% of the fund, and a 10% gap on a decision day costs 0.2% of capital. The expected gain is about 4-5 bps a year, against 1 bp at 0.5%. The risk is trivial at either size, and the evidence supports the larger one. Anything bigger should wait for more live data and a tail analysis.

**Need:** the in-sample mean and event count (to check for decay), costs at four times the size, correlation with the book on decision days, and the worst decision-day moves.

**Next test:** Execute the first trades at 2% and compare slippage with measured costs. Split 1998-2018 by decade to look for decay, and track live results with a sequential test.

**What would change it:**
- If the next 24 decisions average zero or less, cut to 0.5% and review. With a true edge of 0.31%, that happens only about 3% of the time (the standard error is 0.81/√24 ≈ 0.17%).
- If costs at 2% exceed about 0.1% a trade, or decision-day losses coincide with the book's worst days, size by tail contribution instead.

## E06. Create: the Kestrel rebalance

**Decision:** Promising and cheap to test. Commit capital only after the event study passes.

**Strategy:** Supply liquidity to forced index trades.
- **Additions:** after the announcement, buy entrants at up to 10% of daily volume, resting inside the spread. Sell everything into the effective-date closing auction, where trackers buy.
- **Deletions:** buy in that close as trackers sell; exit over five days.

Both legs are long-only (no borrow). Hedge beta with the index future.

**Sizing:** Tracker demand is 9% of free float, which is not given. An illustrative $200M float means $18M, six days' volume in one auction. Cap each name at about $3M (10% of volume for ten days) or a quarter of tracker demand, whichever is less, and keep gross at most about $8M.

**Who pays and why:** Trackers and their investors. They must match the index at the effective-date close, so they trade at that price regardless. We are paid for holding inventory ten days and supplying liquidity when they must trade.

**What could make it lose:**
- Crowding: the price jumps on announcement and reverses by the effective date.
- Predictable changes, so the move precedes the announcement.
- Trackers trading early, sampling or crossing internally.
- Thin auctions, single-stock news, rule changes.
- Spread plus impact, a hurdle of roughly 25-50 bps per event.

**Need:** entrants' float, changes per quarter, dispersion of tracker ownership, auction volumes, past event returns, and futures availability.

**Cheapest decisive test:** An event study on public prices for every past change. Measure abnormal returns from announcement to effective close and over the next five days, and regress them on tracker demand in days of volume. Check pre-announcement drift and compare early with recent rebalances. Then paper-trade one rebalance for slippage.

**Kill rule:** Don't launch if the last eight rebalances' net abnormal return is zero or less, or its t is below 2. Once live, stop if net return per event over eight rebalances falls below 10 bps, or impact takes over half the gross move.

## E07. Create: rain

**Decision:** Underwrite drought at small size once the pricing check passes.

**Strategy:** Sell rainfall-deficit contracts to cooperatives when the bid exceeds fair value plus a model-error margin. Hold to settlement, and spread risk across contract months.

**Fair value:** For a binary payout, fair value is P(rainfall < threshold). Thirty years give only 30 observations per calendar month: at a 10% rate, three droughts, with a standard error of √(0.1 × 0.9/30) ≈ 5.5 points. Tighten it with pooled gamma fits, nearby-station records, and adjustments for trend and seasonal outlook. Sell only above the upper 90% bound.

**Size:** Every contract on a station-month pays at once and dry months cluster, so cap the season's worst-case payout at about 2% of the $5M book ($100k).

**Who pays and why:** Farm cooperatives. Drought wrecks their revenue, so like any insurance buyer they pay above expected loss to cut variance, and few capital providers sell weather risk on a new, thin exchange.

**Fit:** Regional drought should be nearly uncorrelated with our long global equities (check across 360 months). Unlike selling equity puts, this premium diversifies the book.

**What could make it lose:**
- A drying trend that history understates, or multi-month droughts.
- Adverse selection: better-informed buyers (soil moisture, forecasts) buying before dry months.
- Station relocation or measurement error.
- Exchange or clearing failure, margin calls, or positions we can't exit.

**Need:** payout formula, contract size, quote and trade history, margin and clearing rules, and station metadata.

**Cheapest decisive test:** A desk study. Price each threshold from history with bootstrap intervals, and compare with quotes and trades so far. Bids above our upper bound mean a premium exists. Then pilot one or two lots a month.

**Kill rule:**
- Don't trade unless bids exceed our upper bound.
- Once live, stop and reprice if payouts outrun the model (at a 10% rate, six or more in 24 contract-months has about a 3% chance).
- Stop if buyers' volume predicts payouts, or losses exceed two years of expected premium.

## E08. Locking in gains

**Decision:** Reject the +15% target. Don't adopt the trailing stop on this evidence either; test it alone, on the right measures.

**Reasoning:** The edge is the right tail: 8% of trades make 120% of profit, and the other 92% lose 20%. A +15% target caps exactly the trades that pay for everything. If those winners average G, the target removes (G − 15)/G of their 120%. At an illustrative G of 45%, that is 80% of total profit, which the stops must recover elsewhere just to break even. A 2.5-ATR trailing stop on 40-session holds will also shake out future big winners on ordinary pullbacks.

The reported measures mislead:
- **Win rate** rises mechanically when small gains are banked and big ones capped, while the payoff ratio falls.
- **Drawdown** falls with less time invested. The original at 70% size also cuts it by 30%, at the same Sharpe ratio.
- **Missing:** total return, Sharpe ratio, and average win and loss.
- **Period:** 2019-2021 likely overlaps the three years behind the idea, so the test is probably in sample, and one crash could produce the whole drawdown result.

**Need:** return, Sharpe and payoff ratio for both versions, the top 8%'s peak gains, re-entry rules, and the extra trading costs.

**Next test:**
1. Replay the top-8% trades under the proposal, and count how many are capped or stopped before their peak.
2. Run four variants walk-forward over the full history beyond 2019-2021: original, stop only, target only, and both.
3. Compare each with the original scaled to equal drawdown, on Sharpe ratio, return, skew and share of profit from top-decile trades.

**What would change it:** Adopt the stop if, by itself, it raises the Sharpe ratio by about 0.2 or more, or raises return at matched drawdown. It must do so out of sample across regimes, without cutting top-decile capture. The target needs evidence that gains beyond +15% are usually given back, which the 8%/120% split argues against.

## E09. Protecting the put seller

**Decision:** Reject the 3× stop. If the sleeve continues, convert it to 5%/10% put spreads sized to a fixed weekly loss budget, and review whether it belongs in a long-equity book at all.

**Reasoning:** Selling crash insurance on top of long equities loses most when the book is already losing, and two years of steady premium say nothing about the tail.

**The stop fails twice:**
1. **Gaps:** crashes arrive overnight or within one session. A one-week put can jump from 1× to 20× premium without trading at 3×, and buy-backs happen at peak volatility and spreads. It fails exactly when needed.
2. **Whipsaw:** near expiry, a 2-3% dip with rising volatility can triple the put's price before it reverts. Each trigger books a loss of twice the premium on puts that would often have expired worthless: a crude imitation of a long put, paid for on every false alarm.

**The spread:**
- **Capped loss:** at most the 5-point strike width minus net credit, whatever the gap, with nothing to execute in a panic.
- **Cost:** part of the premium. Skew makes the 10% put rich in volatility terms.
- **Still exposed:** losses between −5% and −10%, where equities fall too. The book's own tail is untouched.
- **Sizing:** notional × (5% − net credit) ≤ about 1-2% of NAV per week.

**Need:** premiums for both strikes, implied against realised volatility over a long history including crashes, notional, margin, and the book's beta.

**Next test:** Backtest 20+ years of option quotes at bid and ask for naked, stop (realistic gap fills) and spread versions. Compare worst week, 1% CVaR and P&L in the book's ten worst weeks, and count how often a put hit 3× and then expired worthless.

**What would change it:** Close the sleeve if the spread's net credit falls below its expected loss, or if it deepens the book's worst weeks beyond budget. Only reliable near-3× fills through crash weeks, which is unlikely, would rescue the stop.

## E10. The thirteenth sleeve

**Decision:** Don't add it now. Fix the book first: measure exposures across sleeves on a look-through basis, and admit new sleeves by their marginal contribution.

**The book:** Twelve sleeves at Sharpe 1.0 with ρ = 0.62 give √12/√(1 + 11 × 0.62) = 3.46/2.80 ≈ 1.24. Independent sleeves would give 3.46. The effective number of bets is 12/7.82 ≈ 1.5. Seven sleeves share three stocks and 10 of 12 lost on one day, so this is roughly one mega-cap-tech bet, and correlations rise in stress. Limits belong on names and factors, not sleeves.

**The candidate:** Semiconductor momentum almost certainly loads on the same tech and momentum factor. A sleeve helps only if SR_new > ρ(new, book) × SR_book. With an illustrative correlation of 0.7 to each sleeve:
- ρ(new, book) = 12 × 0.7/√93.8 ≈ 0.87.
- The hurdle is 0.87 × 1.24 ≈ 1.07.
- At equal weight, a true Sharpe of 1.3 lifts the book only from 1.24 to 1.26.

Backtested Sharpe ratios usually shrink live. A one-third haircut gives 0.87, below the hurdle, and the sleeve adds to the single-day tail.

**Need:** live Sharpe ratios, aggregate holdings and factor loadings, the candidate's correlation with the book (overall and on its worst 5% of days), and the depth of the last drawdown.

**Next test:** Regress the candidate's daily P&L on the book's P&L and on market, tech and momentum factors. Measure alpha and t, correlation on down days, and the marginal effect on the book's Sharpe ratio and CVaR. In parallel, decompose the 12 sleeves by factor and merge the seven that overlap.

**What would change it:** If the candidate's correlation with the book is about 0.3 or less, including on down days (a hurdle near 0.37), and its residual alpha has t ≥ 2 out of sample, add it, sized by its risk contribution.

## E11. Loud chief executives

**Decision:** Don't launch the short sleeve. This looks like a few stocks falling, mostly in 2021, not a repeatable signal.

**Reasoning:**
- **Concentration:** 62% of events (about 2,108) come from 14 firms, so the effective sample is nearer 14 price paths than 3,400 events.
- **Overlap, from the counts:** if events were firm-weeks, the 14 firms could supply at most 14 × 52 = 728 of 2021's 2,380 events. That leaves at least 1,652 for other firms, which have only 1,292 in total. So events must be counted on rolling (probably daily) windows, each month's return enters many times, and the t of −6.1 is inflated several-fold.
- **Time:** 70% of events fall in 2021, so one episode dominates. The honest statistic is a calendar-time portfolio over 48 months, with errors clustered by firm and month. 2022-2024 will be thin.
- **Risk:** volatility three times the median puts these among lottery-like stocks, which tend to lag anyway. Measure the 9% against peers matched on volatility, size, momentum and sector, not the market.
- **Shorting:** squeezes, costly and recallable borrow, and gaps. At three times market volatility, one squeeze can erase months of a 9% edge.

**Need:** the exact event definition and timestamps, the firm list, borrow history, delisting returns, and point-in-time post data (if deleted posts are missing, that is look-ahead).

**Next test:**
1. Re-estimate as a calendar-time portfolio against volatility-matched peers, with clustered errors.
2. Drop the 14 firms, and separately drop 2021.
3. Use 2025-2026, which the study never touched, as a clean holdout.

**What would change it:** I would pilot a small, diversified, volatility-scaled short, with squeeze stops and borrow limits, if all of these held:
- every cut shows abnormal returns against matched peers of about −3% a month or worse after borrow;
- the clustered t is −3 or lower;
- returns are negative in most years;
- the holdout agrees.

## E12. Half a second

**Decision:** Keep trading at current size and harvest this latency edge while it lasts. Monitor microstructure, not P&L, and fund faster parsing only if the economics show we can stay ahead.

**Reasoning:** The edge is real today: 60 live releases, 6 ticks net, t 4.1. But it is a race on public information. The 6 ticks are what a three-second adjustment leaves after 450 ms. Faster rivals will trade earlier in that window, moving the price before we arrive and leaving the second-fastest with stale or adverse fills. Second place can lose money.

P&L is too slow an alarm:
- The standard error is 6/4.1 ≈ 1.46 ticks, so one release varies by about 1.46 × √60 ≈ 11 ticks.
- A twelve-release average has an error of about 11/√12 ≈ 3.3 ticks, so it can't tell 6 ticks from 2.
- By the time P&L proves decay, the edge is gone.

**Need:** releases per year, contracts and tick value, infrastructure cost, rivals' likely latency, and safeguards against parser errors (a wrong parse at speed is the tail risk).

**Next test:** From tick data on the 60 releases, build a capture curve by entry time, simulating P&L at 100, 250, 450, 1,000 and 2,000 ms. It shows what a faster rival would take, and whether part of the edge comes after one second, which would make it interpretation rather than speed. From now on, log for each release the share of the move completed before our order lands, and the time of the first aggressive trade.

**What would change it:**
- **Cut or stop:** if that share rises, or capture falls below about 2 ticks over a few releases, cut size. Stop if the rolling mean turns negative.
- **Keep, maybe scale:** if most of the 6 ticks come after one second, since rivals' speed then matters less.
- **Invest:** if an upgrade that beats rivals' expected latency costs less than about a year of expected P&L.
