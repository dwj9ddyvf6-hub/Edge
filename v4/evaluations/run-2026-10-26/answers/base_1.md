**Status: UNVERIFIED for all twelve.** These are decisions on the stated facts and arithmetic only; nothing below has been tested on data.

## E01. The pressure gauge

**Decision:** Reject it as a long trigger. Keep it only as a volatility input for sizing, and only if it beats trailing volatility.

**Reasoning:** The gauge forecasts the size of moves, not their direction: magnitude 9.0% vs 5.0% (t 7.2), direction +0.1% (t 0.3). If ten-day returns are roughly normal, E|r| ≈ 0.8σ, so σ ≈ 11.3% per ten days in the top decile against ≈6.3% otherwise. A long entry there earns about 0.1/11.3 ≈ 0.01 Sharpe per trade, and any round-trip cost above 0.1% makes even the mean negative. At full size the variance drag (σ²/2 ≈ 0.64%) is six times the mean, so the compounded result is a loss. Overlapping windows and six co-moving coins mean even the t of 0.3 overstates precision. The direction is unknown, not "slightly positive". "Big moves follow" sells volatility as drift.

Proper use: as a risk forecast. Scale momentum exposure down when the gauge is high (vol targeting). Momentum often earns less per unit of risk in high-volatility states, so test scaling down, not up. If the coins have listed options, the gauge could also be tested against implied volatility, but that's a separate volatility trade.

**Next test:** out of sample, regress next-ten-day realised volatility on the gauge plus trailing 10- and 30-day realised volatility. Does the gauge add anything? Then run the sleeve with and without gauge-based scaling. Use expanding-window decile cut-offs (no look-ahead) and block-bootstrapped or non-overlapping t-statistics.

**Would change my decision:** momentum's signed, risk-adjusted return proving significantly higher in top-decile states (t > 2 out of sample, after costs, with honest errors). Then the gauge could amplify momentum signals, though it should never trigger buys alone. If it adds nothing beyond trailing volatility, stop paying the vendor.

**Not given:** the gauge's inputs and timestamps, how the deciles and t-statistics were built, costs, the vendor's fee, per-coin results, the shape of the signed-return distribution.

## E02. A better score that changes nothing

**Decision:** Don't add it. Keep the volatility veto as it is.

**Reasoning:** The question isn't whether distress predicts returns. It's whether distress improves the veto, and the pilot answered that. AUC rose by 0.004, probably within noise (a DeLong test will say). The money gain, which is what the veto exists for, slipped from +0.31% to +0.30% a month.

The overlap explains why. A rank correlation of 0.74 means the rankings share ~55% of their rank variance. Under a Gaussian copula (Pearson ≈ 0.76), about two-thirds of the score's worst decile already sits inside the volatility model's worst 15%. With a fixed 15% budget, every name the score adds pushes out a volatility-flagged name, and the pilot says those swaps net to zero. The standalone −2.1%/month (t 4.0) is mostly volatility the veto already captures. An AUC gain can also come from reordering the safe 85%, where the veto takes no action. Adding the score would buy complexity, filing-lag and restatement risk, and another overfitting channel, for no money.

**Next test:**
1. A paired, month-block bootstrap of the pilot, for a confidence interval on the money difference.
2. The score orthogonalised to trailing volatility, with the residual's worst decile re-tested on filing dates, not period-end dates.
3. A regime split: does the score add anything in credit-stress months, where crashes cluster?

**Would change my decision:** a held-out walk-forward in which the combined veto beats the current one by a margin set in advance (e.g. ≥0.05%/month, paired t > 2) after data costs, or a material cut in stress-regime tail losses at an unchanged average. Then I'd add it, perhaps as a separate hard veto on the extreme 2–3%. Whether the residual works as a short or sizing signal is a separate project, gated by borrow costs.

**Not given:** pilot length and standard errors, data cost, whether the balance-sheet data are point-in-time, borrow costs.

## E03. Patience at a price

**Decision:** No. The limit variant earns less per signal. Keep market entries.

**Arithmetic (per signal, idle cash at 0):**
- Market: 400 × 1.1% = 440 points → **+1.10% per signal**.
- Limit: 112 fills × 2.4% = 268.8 points; 288 misses × 0 → **+0.67% per signal**.

The limit gives up 0.43 points per signal, about 39% of the return.

**Why:** adverse selection. The bid fills when the price falls, which happens mostly in signals that are failing. The signals that run away never fill, and they're the best (+4.0%). On the market-entry basis, the filled subset must have returned (440 − 288 × 4.0)/112 ≈ −6.4%, so the fills select the losers. Setting "+2.4% per fill" against "+1.1% per trade" compares a subset with the whole. The three figures also can't share one basis, because a ~1.5% better price can't turn −6.4% into +2.4% over the same ten days. The windows need auditing; on a common basis the limit probably looks worse still.

Break-even: at +2.4% per fill the limit needs a fill rate above 1.1/2.4 ≈ 46%. At a 28% fill rate it needs +3.9% per fill.

One exception: if capital binds and surplus signals queue, the right metric is return per deployed capital-day, not per signal. Even then, fills cluster in sell-offs, which correlates entries, so judge it at portfolio level.

**Next test:** re-run all 400 signals on one basis (from the signal date, over the same ten-day window, with misses held as cash), with a paired bootstrap. Then test variants that don't skip winners: a shallow limit (0.25–0.5%) good for one session, then a market order.

**Would change my decision:** a variant earning more than 1.1% per signal out of sample (paired t > 2), or a portfolio backtest showing higher Sharpe for the limit because capital really is constrained.

**Not given:** whether capital binds, per-trade dispersion, exact return windows, commissions, opening spreads.

## E04. Six point four

**Decision:** The claim is false. No allocation on this evidence.

**Reasoning:**
- Naive t: 2.6 × √6 ≈ 6.4. Correcting for skew −1 and kurtosis 6 (daily SR 0.164; variance factor 1 + 0.164 + 1.25 × 0.027 ≈ 1.20) gives ≈5.8.
- Luck: a zero-skill six-year SR has sampling error 1/√6 ≈ 0.41, so the observed 0.45 implies a true dispersion of only √(0.45² − 0.41²) ≈ 0.19. About 83% of the variation is noise.
- Selection: the expected best of 4.2M independent noise draws is ≈5.14 × 0.45 ≈ 2.3. The winner beats it by ~0.7 standard errors, a deflated-Sharpe probability of Φ(0.64) ≈ 0.74, short of 0.95. Bonferroni needs t ≈ 5.6. The adjusted 5.8 scrapes past it before costs (family-wise p ≈ 0.02, not 10⁻¹⁰), which only shows that some combination isn't pure noise.
- Shrinkage: an empirical-Bayes weight of 0.19²/0.45² ≈ 0.18 puts the winner's expected true SR near 0.45 before costs, if the family mean is near zero.
- Costs: at an assumed 10% annual volatility the edge is ≈10 bps a day. Replacing the book daily (≈200% traded) breaks even at ≈5 bps per side before impact, and midpoint fills hide this.
- Tails: with skew −1 and fat tails, one crash day can erase months.

**Next test (cheapest decisive):** get the results grid and code. Re-run the winner and its neighbours with measured spreads and impact; a broad plateau is believable, an isolated spike isn't. Then run the frozen rule on data the search never saw, and paper-trade it. A year forward can falsify a true 2.6 (it would show t ≈ 2.6) but can't confirm a modest SR.

**Would change my decision:** the frozen rule earning net SR ≥1 on untouched data, with a deflated probability >0.95 at the true trial count and a stable neighbourhood. Then a small pilot.

**Not given:** volatility, the turnover definition, costs, the family's mean SR, the effective number of independent trials.

## E05. One registered test

**Decision:** Approve the rise to 2%. The evidence would bear more, but grow further only after the checks below.

**Reasoning:** This is about as clean as evidence gets: a rule fixed before the data, no parameters, one backtest (t 2.9), and an independent live replication with real fills (t 2.6). Live SE = 0.31/2.6 ≈ 0.12% per trade, so the 95% interval is about +0.07% to +0.55%, with per-trade SD ≈ 0.12 × √46 ≈ 0.81%. The two samples combined give z ≈ 3.8, assuming ~8 decisions a year (~168 in the backtest). That's ≈ +2.5% a year on the capital deployed, with SD ≈ √8 × 0.81% ≈ 2.3%, a standalone Sharpe of ≈1.1.

Exposure stays tiny. At 2% notional, a −5% index day costs 0.1% of the fund, and expected income is ≈5 bps a year. Kelly (μ/σ² ≈ 47× notional) puts 2% nowhere near aggressive.

Residual risks:
1. The idea probably came from research on the same 1998–2018 history, so the live record is the clean evidence.
2. Fund-level multiple testing applies if the 2019 registry held many hypotheses.
3. The effect may depend on the policy cycle.
4. A few big days may carry the mean.

**Next test:** stress the 46 live trades: median, share positive, mean without the best three, by year, hiking versus easing. Review the whole 2019 registry. Confirm fills at 2% size.

**Would change my decision:** the mean becoming indistinguishable from zero without the best three trades, or the registry showing this was the best of ten or more ideas. Then I'd stay at 0.5–1%. Set the monitoring rule now:
- If the next 24 decisions average below zero net (≈3% likely if the edge is real), go back to 0.5%.
- If the cumulative live t falls below 1.5, stop.

**Not given:** the 2019 registry, trade-level P&L, the cost model, how the rest of the book moves on decision days.

## E06. Create: the Kestrel rebalance

**Decision:** Build it if the archive test passes. Start at ≤$3M a name.

**Strategy:** Supply liquidity to the trackers. After each announcement, buy additions (and short deletions where borrow exists) over the ten days with passive orders. Exit with market-on-close orders into the trackers' effective-date flow. Hedge with paired shorts or index futures, if any. Without borrow, buy deletions in the effective-date auction and sell as the pressure fades.

**Who pays and why:** the trackers, and through them their investors. They must own 9% of each new member's float at one closing price. The index itself "trades" at that price, so the premium never shows up as tracking error and they have no reason to avoid it. In days of volume their demand is 0.09 × float ÷ $3M ADV. At 0.5–1% daily float turnover (float isn't given), 9–18 days of volume cross in one auction.

**Sizing and costs:** about one day's ADV per name (~$3M at ≤10% participation over ten days); a few changes a quarter fits $20M. Entry costs a 12.5 bps half-spread (less if passive) plus our impact. The auction exit pays no spread.

**What could make it lose:** arbitrageurs front-running the announcement; trackers pre-positioning; an early peak and reversal; a crowded close; revised or cancelled changes; hard-to-borrow deletions; idiosyncratic news; only four events a year. Never trade to move the close: supplying liquidity is legitimate, marking the close is not.

**Cheapest decisive test:** an event study on the exchange's archive. For each past change, measure the abnormal return from announcement to effective close, the next-open reversal, and auction volume against predicted tracker demand, net of 25 bps plus impact, quarter-clustered.

**Kill rule:** don't launch unless historical net capture on additions is ≥50 bps with t ≥ 2 over ≥40 events. Live: stop if net P&L per event is ≤0 after eight quarters, or if auction volume falls below half the predicted tracker demand.

**Not given:** free floats, changes per quarter, auction and short-sale rules, futures, competing arbitrageurs.

## E07. Create: rain

**Decision:** Run a small, capped insurance-selling book once the burn test and settlement review pass.

**Strategy:** Be the insurer. Sell drought contracts to the cooperatives above a conservative payout probability, posting offers inside the wide quotes. Price each month from its own history, adjusted for trend and any seasonal outlook. Cap total payout sold per season at, say, 5% of the book ($250K), because dry months cluster.

**Who pays and why:** the cooperatives. Drought wrecks their income, so like any insurance buyer they pay more than the expected loss to shed it, and the wide quotes say risk capital is scarce. Regional weather risk should be roughly uncorrelated with the book's long global equities, so the premium diversifies rather than adds equity beta.

**Calculations (illustrative):** each calendar month has only 30 observations. A 15% historical frequency has an SE of √(0.15 × 0.85/30) ≈ 6.5 points, putting its upper 80% bound at ≈20%. Selling at 25¢ per $1 of payout clears that bound and earns ≈10¢ against a ≈36¢ SD. That's ≈0.28 Sharpe per contract, or ≈1.0 a year if months were independent; persistence lowers it.

**What could make it lose:** a drying trend that history understates; better-informed buyers (soil moisture, forecasts) buying before droughts; one bad season hitting several months; station relocation, gaps or revisions; a new exchange's clearing and credit; margin calls; no exit before expiry; too little open interest to matter.

**Cheapest decisive test:** a burn analysis on the public 30 years (payout frequency by month and threshold, raw and detrended, with confidence bounds), set against the prices and depth at which buyers actually trade. Audit the station record and settlement rules. Then pilot small offers, logging who buys and when.

**Kill rule:** don't trade unless prices exceed the upper 80% bound plus costs. Stop if realised payouts statistically exceed the priced probability (binomial p < 0.05), if fills cluster ahead of droughts, or if settlement or credit fails.

**Not given:** payout size, thresholds, quotes, depth, fees, margin, clearing and settlement terms.

## E08. Locking in gains

**Decision:** Don't adopt it as proposed. The +15% target caps the sleeve's source of profit. Test the trailing stop alone.

**Reasoning:** This is a right-tail business: 8% of trades made 120% of profit, and the other 92% lost 20% net. Any rule that trims winners has to be judged on that tail. Illustration (the winners' average isn't given): if the top 8% averaged +40%, a +15% cap would cut their 120 units to 45. The other trades would then have to swing from −20 to +55 just to match today's total, and no stop will do that.

The metrics are the wrong ones. A profit target raises win rate mechanically (more small wins) and says nothing about expectancy. Drawdown falls whenever exposure falls; simply trading smaller would do the same. Missing: total return, Sharpe, average win and loss, time in market, turnover and costs, and the re-entry rule after a stop-out. The test also covers 2019–2021, not the live years, and its 2.5 ATR and 15% were probably chosen after looking.

The trailing stop alone might help. Trend strategies suffer sharp reversals, and stops can trim those. Whether 2.5 ATR saves more than it loses on whipsawed winners is an empirical question.

**Next test:** an ablation on the longest history plus the three live years, with costs and an explicit re-entry rule, comparing baseline, stop only, target only, and both. Compare each with a baseline scaled to the same exposure, and report how much of the top-8% profit each keeps. Sweep ATR from 2 to 4 and targets of 10–30% or none, looking for a plateau, not a spike.

**Would change my decision:** a variant beating the exposure-matched baseline out of sample by ≥0.2 Sharpe while keeping ≥85% of the right-tail profit. Adopt the combination if both parts pass; if only the stop passes, adopt the stop alone.

**Not given:** trade-level P&L and maximum favourable excursion, a backtest on the live period, costs, the re-entry logic.

## E09. Protecting the put seller

**Decision:** Reject the stop. Prefer the put spread if its net credit still pays; otherwise close the sleeve. Either way, size it so the whole book survives a crash week.

**Reasoning:** Selling 5% OTM weekly puts is selling crash insurance on top of a long-equity book, so the sleeve loses exactly when everything else does. Two quiet years (~104 weeks) say little about a once-in-several-years loss. Steady premium isn't evidence of edge.

*Stop at 3× premium.* In an orderly fall it caps the loss near 2× premium, so the sleeve stays positive only if fewer than one week in three stops out ((1−f)p > 2fp → f < ⅓), before slippage. It fails when it's needed. The index gaps through it overnight or over weekends. Volatility spikes trigger it on modest moves. Stressed spreads mean buying back at the ask at the worst moment. And many stopped puts would have expired worthless. It realises paper losses and keeps the gap risk.

*Long 10% OTM put (a 95/90 spread).* The maximum weekly loss becomes 5% of notional minus the net credit, guaranteed by contract, not by an order. In a −20% week the naked loss is ≈15% of notional; the spread's is at most 5%. The cost is the wing's premium, possibly much of the credit if deep puts are rich. A run of −5% to −10% weeks can still lose the full width repeatedly.

**Next test:** replay all three on the longest history with crashes and real option prices, modelling gap fills and stressed spreads for the stop. Measure mean weekly P&L, worst week, worst four weeks, CVaR, and P&L on the book's worst equity days.

**Would change my decision:** a replay with realistic fills in which the stop beats the spread on both tail loss and net P&L, which I doubt. If the wing makes the spread's expected net ≤0 after costs, close the sleeve rather than hedge it.

**Not given:** premium levels, notional against book size, prices at both strikes, margin, long return history.

## E10. The thirteenth sleeve

**Decision:** Don't add it now. The book's problem is concentration, and semiconductor momentum most likely adds more of it.

**Reasoning:** For N sleeves of Sharpe s and average correlation ρ, portfolio SR = s√(N/(1+(N−1)ρ)). Here 1 + 11 × 0.62 = 7.82, giving 12/7.82 ≈ 1.5 effective bets and SR ≈ 1.0 × √1.53 ≈ 1.24, not the √12 ≈ 3.5 that "independent" implies. The equal-weight book carries ≈81% of a single sleeve's volatility. Seven sleeves hold the same three stocks and 10 of 12 lost on one day, so stress correlation runs above 0.62. This is one or two tech bets in twelve wrappers.

A new sleeve improves the book only if its Sharpe exceeds its correlation with the book times the book's Sharpe. Semiconductor momentum will plausibly correlate 0.6–0.8 with this book (to be measured), so the hurdle is ≈0.75–1.0. The 1.3 is a backtest; a 30–50% haircut leaves 0.65–0.9, at or below the hurdle. Even at face value with ρ = 0.7, the optimal mix lifts SR only from 1.24 to ≈1.38, and it deepens the same bad day.

Fix the book first. Aggregate holdings across sleeves. Cap net exposure to each name and to the tech factor book-wide. Budget risk by marginal contribution, treating the seven overlapping sleeves as one bucket. Seek low-correlation additions: other asset classes, horizons, market-neutral designs.

**Next test:** the semiconductor sleeve's daily P&L correlation with the book, over the full period and on the book's worst 5% of days; its holdings overlap with the three stocks; its marginal contribution to Sharpe and to the last drawdown. Also compare the twelve sleeves' live Sharpes with their backtests.

**Would change my decision:** a market- or sector-neutral version with correlation to the book under ~0.3, stress days included, and out-of-sample SR ≥0.8. Then add it, at a risk weight set by marginal contribution.

**Not given:** live sleeve P&L, holdings, the new sleeve's construction, the stress correlation matrix.

## E11. Loud chief executives

**Decision:** Don't launch the short sleeve. The finding is unconfirmed, and most likely a few firms, one year and high volatility in disguise.

**Reasoning:**
- **Clustering.** About 2,100 of the 3,400 events come from 14 firms. A chief executive who posts more than ten times a week for months generates dozens of overlapping one-month windows that share the same future returns. With 70% of events in 2021, one speculative episode and its unwind may be the whole result. The t of −6.1 assumes an independence the data lack. If the effective sample is a few dozen observations at ~30% monthly volatility, |t| would be nearer 1.5–2.
- **Benchmark.** "Lags the market" isn't risk-adjusted. Stocks with three times the median volatility often lag for reasons unrelated to posting: lottery demand, high beta in a falling market, retail crowding. The test needs controls matched on volatility, size, momentum and industry.
- **Implementation.** These names are volatile and crowded, so borrow is costly and recallable, and squeezes are violent. A short's loss is unbounded and its gain capped. Fees of 10–30% a year (≈0.8–2.5% a month) and squeeze losses come straight out of the edge.

**Next test (cheap and decisive):** drop the 14 heavy firms and all of 2021, and keep only the first event per firm per quarter. Then run a monthly calendar-time short portfolio against matched controls, with firm- and month-clustered errors.

**Would change my decision:** in that cleaned sample, underperformance against matched controls of ≥3% a month with t ≥ 3, in both up and down markets and net of actual borrow fees. Then a small paper short sleeve with per-name squeeze limits. A cheaper first use would be a veto for long books, which needs no borrow.

**Not given:** the event list with firm identifiers, the posting definition and timestamps, how the t was computed, borrow availability and fees, factor exposures.

## E12. Half a second

**Decision:** Keep trading at current size and assume decay. Measure latency sensitivity before buying speed. Don't scale up.

**Reasoning:** The edge is speed on public, scheduled data: the desk reads at 450 ms and the price takes ~3 s to adjust. The record is good. SE = 6/4.1 ≈ 1.5 ticks, so per-release SD ≈ 1.5 × √60 ≈ 11 ticks, a Sharpe of ≈0.5 per release, on real fills.

But the payer is whoever is slower: stale quotes and slow traders in the first seconds. Once the two competitors parse in tens of milliseconds, the price will have moved before our 450 ms, and we'll be picking up what's left. Latency races are close to winner-take-all, and second place earns little. P&L won't warn us in time either. The gap between the first-30 and last-30 means has an SE of ≈11 × √(2/30) ≈ 2.9 ticks, so even a halved edge would barely register.

Operational risk: a parser or format error can fire a large wrong-way order. The desk needs sanity bounds, position caps and an automatic kill switch.

**Next test:** build a latency decay curve.
- From tick data around past releases, compute what the desk would have earned acting at 100, 450, 1,000 and 2,000 ms.
- Track the price-adjustment half-life release by release. If it's shrinking, the competitors are arriving.
- Price a sub-50 ms upgrade against the edge's likely remaining life.
- Separately, test a speed-independent edge: drift or reversal in the minutes after release, keyed to the surprise against consensus.

**Would change my decision:** a decay curve showing a large gain from lower latency, with payback under ~6 months. Then buy speed. Retire the strategy when the rolling 12-release mean falls below ~1 tick net, or when ≥90% of the move completes before our fills. If the minutes-scale test shows t > 3, move capital there.

**Not given:** tick value, contracts per release, releases per year, slippage history, upgrade costs.
