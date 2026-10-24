# Betting, prediction markets, gambling, and adaptive allocation research

Research scope: primary papers and official market documentation, checked 2026-10-23 America/New_York. This memo distinguishes documented findings from original synthesis. The screenshot is an insightful decomposition, not an exhaustive theorem; gambling makes the missing implementation details unusually explicit.

## Source register: 12 primary research/documentation entries

### B01 — Kelly: information has value relative to offered odds

J. L. Kelly Jr. (1956), **A New Interpretation of Information Rate**, Bell System Technical Journal 35(4), 917–926.

- Primary publisher record: https://www.nokia.com/bell-labs/publications-and-media/publications/a-new-interpretation-of-information-rate/
- Original article reproduced with permission: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/7/36891/files/2017/07/Kelly1956-1uwz47o.pdf
- Read source ref: `turn53view4`; publisher `turn45view0`.
- Finding: connects useful information about gamble outcomes to attainable long-run log wealth growth at specified odds. The probability model and wager size are separate inputs: maximizing expected dollars can produce eventual ruin where maximizing expected log growth does not.
- Limits: the ideal betting model does not remove estimation error, costs, changing probabilities, leverage constraints, or limited investment horizons. The result is not “information always makes money.”
- Skill implication: state payoff, odds, beliefs, bankroll fraction, and wealth dynamics explicitly before asserting an edge.

### B02 — Thorp: first discover favorable bets, then allocate capital

Edward O. Thorp (1997, revised May 29, 1998), **The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market**, conference paper.

- Primary text and chapter links: https://sites.oxy.edu/lengyel/M330/thorp/paper.htm
- Allocation chapter: https://sites.oxy.edu/lengyel/M330/thorp/ch3.pdf
- Sports chapter: https://sites.oxy.edu/lengyel/M330/thorp/ch6.pdf
- Read abstract/structure: `turn45view1`. Chapter PDFs retrieved but text extraction returned no text; do not claim full chapter extraction.
- Finding: distinguishes finding positive-expectation opportunities from deciding how much to stake; applies growth-optimal allocation across blackjack, sports betting, and securities.
- Limits: historical success of Thorp is not evidence for a new strategy. Position sizing cannot convert a negative-expectation payoff into a positive-expectation one merely by changing stakes.
- Skill implication: refuse to treat “Kelly sizing,” martingale, or a smoother equity curve as proof of alpha.

### B03 — Gneiting and Raftery: evaluate beliefs with proper scores

Tilmann Gneiting and Adrian E. Raftery (2007), **Strictly Proper Scoring Rules, Prediction, and Estimation**, Journal of the American Statistical Association 102(477), 359–378.

- Author-hosted original: https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf
- DOI: https://doi.org/10.1198/016214506000001437
- Read source: `turn45view2`.
- Finding: strictly proper scores uniquely reward reporting one's true probability distribution in expectation, under their scoring assumptions. The paper connects scoring, entropy, divergences, calibration, and sharpness.
- Limits: a better forecast score does not itself imply better executable returns. A model can improve forecasts in high-liquidity states whose prices already incorporate the information, while worsening the subset actually traded. Do not import the paper's random cross-validation examples into dependent financial time series without chronology controls.
- Skill implication: keep two scoreboards: forecast quality against a market/base-rate benchmark, and net trading utility on actually executable decisions.

### B04 — Wolfers and Zitzewitz: prices are not automatically physical probabilities

Justin Wolfers and Eric Zitzewitz (2006), **Interpreting Prediction Market Prices as Probabilities**, Federal Reserve Bank of San Francisco Working Paper 2006-11 / NBER 12200.

- Landing page: https://www.frbsf.org/research-and-insights/publications/working-papers/2006/04/interpreting-prediction-market-prices-as-probabilities/
- Full paper: https://www.frbsf.org/wp-content/uploads/wp06-11bk.pdf
- Read refs: `turn50view1`, `turn53view5`, `turn57view0`.
- Finding: derives conditions under which prices equal mean beliefs. In its log-utility model, beliefs independent of wealth and no external hedging motive support an unweighted mean interpretation. Correlated wealth and beliefs produce wealth-weighted averages. Alternative utility and belief distributions can create systematic differences.
- Limits: aggregate belief is not necessarily objective truth. Contract costs, endowments, trading restrictions, and external hedges alter economic demand.
- Skill implication: use market probability as a strong benchmark with explicit assumptions; do not equate a displayed price with an oracle or automatically label disagreement as mispricing.

### B05 — Snowberg and Wolfers: preferences versus misperceptions can be tested

Erik Snowberg and Justin Wolfers (2010), **Explaining the Favorite–Long Shot Bias: Is It Risk-Love or Misperceptions?**, Journal of Political Economy 118(4), 723–746.

- Primary working-paper repository: https://www.iza.org/publications/dp/4884/explaining-the-favorite-longshot-bias-is-it-risk-love-or-misperceptions
- NBER PDF: https://www.nber.org/system/files/working_papers/w15923/w15923.pdf (search indexed; direct open denied).
- Read primary abstract: `turn53view3`.
- Finding: uses compound-bet choices alongside ordinary win bets to discriminate explanations of horse-racing favorite–longshot bias; evidence favors misperceived probabilities in that setting.
- Limits: it does not establish that every longshot is overpriced, that favorite bets earn positive net returns after the take, or that the same effect holds in every sport, options market, or prediction platform.
- Skill implication: identify observable predictions that distinguish “people pay for lottery utility” from “people misestimate probabilities.” Relative underpricing need not overcome the house margin.

### B06 — Levitt: the counterparty can combine information edge and inventory risk

Steven D. Levitt (2004), **Why Are Gambling Markets Organised So Differently from Financial Markets?**, Economic Journal 114(495), 223–246.

- Author/university PDF: https://pricetheory.uchicago.edu/levitt/Papers/LevittWhyAreGamblingMarkets2004.pdf
- DOI: https://doi.org/10.1111/j.1468-0297.2004.00207.x
- Read source: `turn45view5`.
- Finding: in the studied sportsbook setting, bookmakers take outcome exposure and exploit bettor biases rather than merely balancing both sides. Price can be selected to maximize profit given customer demand.
- Limits: the 2004 data and market structure do not license universal claims about today's bookmakers or exchange market makers. An observed imbalance is not automatically a hedge need or an uninformed counterparty.
- Skill implication: explain the actual marginal counterparty's objective; assess whether the apparent supplier of variance is better informed than the strategy.

### B07 — Busseti, Ryu, Boyd: constrain drawdown explicitly

Enzo Busseti, Ernest K. Ryu, and Stephen Boyd (2016), **Risk-Constrained Kelly Gambling**, Journal of Investing 25(3), 118–134.

- Author PDF: https://web.stanford.edu/~boyd/papers/pdf/kelly.pdf
- Archive: https://arxiv.org/abs/1603.06183
- Read refs: `turn45view6`, `turn57view1`.
- Finding: gives a tractable conservative restriction on drawdown probability while maximizing log growth. Numerical examples outperform fractional Kelly on the specified growth/drawdown tradeoff.
- Limits: its core repeated-gamble model assumes IID returns. The bound is conditional on the model; unknown dependence and tail states can invalidate an empirical guarantee. Its fixed initial-wealth floor is not automatically a rolling peak-to-trough maximum-drawdown limit.
- Skill implication: distinguish formal modeled risk bounds from simulated or observed drawdown. Put real desk limits on joint wealth, collateral, and tails, not just per-trade stops.

### B08 — Sun and Boyd: uncertainty changes the optimization problem

Qingyun Sun and Stephen Boyd (2018 preprint; revised 2021), **Distributional Robust Kelly Gambling: Optimal Strategy under Uncertainty in the Long-Run**.

- Primary preprint: https://arxiv.org/abs/1812.10371
- Read source: `turn45view7`.
- Finding: chooses a portfolio maximizing worst-case expected log growth over an explicit set of possible distributions; some finite-state uncertainty sets admit tractable convex formulations.
- Limits: robustness is only to the chosen uncertainty set. Omitting a crash, venue failure, or changing dependency from that set leaves that exposure unprotected; excessively broad sets can lead to no trade.
- Skill implication: require sensitivity to probability, slippage, dependency, and adverse regimes. State the ambiguity set rather than applying an unexplained universal half-Kelly multiplier.

### B09 — Hanson: price discovery has a payer

Robin Hanson (2007; author draft January 2002), **Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation**, Journal of Prediction Markets 1(1), 3–15.

- Author draft: https://hanson.gmu.edu/mktscore.pdf
- Published paper: https://www.ubplj.org/index.php/jpm/article/view/417/448
- DOI: https://doi.org/10.5750/jpm.v1i1.417
- Read source: `turn53view0`; publication verified `turn57search9`.
- Finding: market scoring rules combine individual forecasting incentives and group information aggregation. Logarithmic structure supports useful conditional/combinatorial consistency properties.
- Limits: the mechanism's information subsidy is a transfer from the market sponsor; it is not free wealth creation. A posted marginal price changes with order size.
- Skill implication: count information subsidies, promotions, or liquidity rebates separately from persistent trading alpha. Integrate the entire execution price curve, not just the first quote.

### B10 — Cover: allocation skill need not be directional prediction

Thomas M. Cover (1991), **Universal Portfolios**, Mathematical Finance 1(1), 1–29.

- Original article: https://isl.stanford.edu/~cover/papers/paper93.pdf
- Author-hosted version dated October 23, 1996: https://isl.stanford.edu/~cover/papers/universal_portfolios.pdf
- DOI: https://doi.org/10.1111/j.1467-9965.1991.tb00002.x
- Read version: `turn53view1`; original publication verified `turn57search0`, `turn57search2`, `turn57search14`.
- Finding: an online nonanticipating allocation can asymptotically match the exponential growth rate of the best constant rebalanced portfolio chosen after observing outcomes, for the stated market-sequence model.
- Limits: regret relative to a benchmark is not guaranteed positive absolute return, finite-horizon superiority, or frictionless-to-real-world transfer. Turnover and convergence times matter.
- Skill implication: classify diversification/rebalancing and adaptive allocation benefits separately from new predictive information; evaluate against a feasible allocation benchmark after costs.

### B11 — Brown and Sandholm: strategic safety and exploitation differ

Noam Brown and Tuomas Sandholm (2019), **Superhuman AI for Multiplayer Poker**, Science 365(6456), 885–890.

- Author paper: https://noambrown.github.io/papers/19-Science-Superhuman.pdf
- DOI: https://doi.org/10.1126/science.aay2400
- Read refs: `turn53view2`, `turn57view2`.
- Finding: Pluribus achieved strong performance in six-player no-limit poker. The paper distinguishes equilibrium strategies and opponent exploitation and explains why the special safety properties of two-player zero-sum equilibria do not transfer straightforwardly to multiplayer games.
- Limits: poker has known rules and observable chip accounting; financial markets have changing participants, external utility, endogenous impact, and uncertain payoff processes. Poker success is not evidence that an LLM can find market alpha.
- Skill implication: ask how the counterparty responds after detecting the strategy, and what happens when an exploitable pattern disappears. A robust baseline and an evidence-backed exploit should be evaluated separately.

### B12 — Official contract documentation: the legal payoff is the traded random variable

Kalshi (2026), **Market Rules** and **Market Outcomes**, official help documentation, dated March 17, 2026.

- https://help.kalshi.com/en/articles/13823822-market-rules
- https://help.kalshi.com/en/articles/13823826-market-outcomes
- Fee schedule to refresh for any implementation: https://kalshi.com/docs/kalshi-fee-schedule.pdf
- Read refs: `turn50view2`, `turn50view3`. Fee PDF discovered, not used for a numerical fee claim.
- Finding: each contract has specified resolution criteria and an information source; determination follows those terms and need not coincide with market closure.
- Limits: these are general documentation pages, not the terms of a particular trade. Never infer current fees or payoff equivalence across venues from a headline.
- Skill implication: model contract identity, boundary inclusivity, observation time, authoritative data source, revision policy, void/exception handling, settlement lag, collateral return, and every fee before declaring arbitrage.

## Mathematical examples and deductions

These examples are original calculations using hypothetical inputs, not empirical return claims.

### 1. The key bridge: information value is relative to the market

Assume exhaustive mutually exclusive states, complete frictionless state-contingent bets, normalized strictly positive market prices q_i summing to one, true probabilities p_i, and a fully invested allocation b_i summing to one. A dollar allocated b_i buys b_i/q_i payout units in state i. Then:

`E_p[log wealth multiple] = Σ p_i log(b_i/q_i) = D_KL(p || q) − D_KL(p || b)`.

This elementary identity expresses the edge requirement precisely: the strategy must lose less to model error than it gains from disagreement with market prices. Costs and incomplete contracts reduce or alter realizable growth. It is not a general formula for leveraged equities.

If p=(.60,.40), q=(.50,.50), and the overconfident model allocates b=(.80,.20), the expected log growth is approximately −0.0845 per bet, although it correctly identifies the more likely outcome. Using b=p yields about +0.0201 in the ideal model. Correct direction plus wrong confidence can destroy wealth.

### 2. A betting model must beat the offered price and costs

For decimal odds d, win probability p, and one dollar staked, expected net profit is `p d − 1`. Positive expectation requires `p > 1/d`, not merely `p > .5`. With d=1.91 and p=.56, expectation is .0696 per dollar and ideal binary Kelly is `(p d − 1)/(d−1) ≈ .0765` of bankroll. If p=.525, expectation is only .00275 and ideal Kelly approximately .00302. Small probability error can erase almost the entire opportunity.

For a $1 binary payout bought at q=.52 with all-in hypothetical cost c=.015, p=.56 gives expected profit .025 per contract. If the orders that actually fill occur in states where conditional p=.50, realized expected profit is −.035. Evaluate `P(event | signal, execution state, fill)` rather than only `P(event | signal)`. This selection correction is a research requirement, not a claim that every fill changes p by this amount.

### 3. De-vigging is a benchmark transformation, not proof

Two complementary outcomes at decimal odds 1.91 have raw implied probability sum `2/1.91 ≈ 1.04712`. Normalization produces .50/.50, but only under a proportional-margin assumption. It does not recover the objective probabilities or account for differential bettor demand, longshot bias, or asymmetric limits.

With executable odds 2.10 and 2.05 on exactly complementary outcomes, the reciprocal sum is about .96400; ideal equal-payout dutching yields roughly 3.73% return on total stake. Actual arbitrage additionally requires simultaneous executable size, identical event definitions, compatible voids, and all settlement/fees/funding outcomes. A headline match is inadequate.

### 4. Capital time can dominate a nominal spread

A hypothetical position locks $980 to receive a genuinely guaranteed $1,000 in one year: gross return 2.04%. If the accessible matched-horizon alternative earns 4%, the apparently sure spread has negative opportunity value before additional costs. Compare maturity-matched and collateral-matched alternatives, not annualized percentages alone; timing of early release also matters.

### 5. Hit rate is not the payoff distribution

A hypothetical strategy earns +1 with probability .99 and loses 150 with probability .01: mean is −.51 per trade. More “successful” trades and frequent small profits do not prove either information edge or adequately compensated risk warehousing. Model loss severity and clustering, not just win frequency.

## Creative connections worth testing, not claimed discoveries

1. **Contract-semantic advantage.** Forecast the exact settlement variable better than headline traders. Compare paired contracts only after normalizing measurement source, cutoff, revision policy, and settlement clock. Test whether semantic discrepancies predict net pricing residuals; failure condition is disappearance after exact payoff matching or costs.
2. **Fill-conditioned calibration.** Partition probability scoring by marketable fills, passive fills, rejected orders, and queue/volatility states. Test whether an apparently superior predictor becomes inferior exactly when the execution engine receives inventory. A latency or quoting fix may improve monetization without any new signal.
3. **Utility separation experiment.** Use behavior across related simple and compound contracts to distinguish probability error from demand for lottery-like payoffs. Design different strategy responses: information correction for the former; capacity/tail-budgeted supply for the latter. Do not assume either explanation from a popular narrative.
4. **Benchmark-relative forecast research.** Rank new information by its incremental out-of-sample score against contemporaneous market forecasts in the actionable subset, then map it to net utility. This prevents spending research effort on already priced facts or irrelevant high-confidence predictions.
5. **Bankroll as inventory of future options.** Value liquidity retained for tomorrow's better opportunities. Compare a high-margin long-lockup trade with a smaller short-lockup trade under joint scenario simulation and liquidity constraints. Expected dollars per capital-day is a screening statistic, not a sufficient decision rule because risks and reinvestment opportunities differ.
6. **Two-layer strategic adaptation.** Keep a cost-aware robust baseline; allow explicit, bounded deviations only when recent out-of-sample evidence supports a counterparty-specific exploitable behavior. Track decay and counter-adaptation. Do not mistake equilibrium-inspired safety for guaranteed positive trading returns.

## High-value instructions to inject into the final skill

- Force every candidate to name the payoff, payer, economic reason, marginal counterparty, information set, executable price, capacity, and failure state.
- Separate probability forecasting, contract construction, execution, allocation, and portfolio utility. Improvement in one is not proof of improvement in the others.
- Label risk premium, informational alpha, subsidy, structural constraint transfer, and implementation savings distinctly; they may coexist.
- Ask what newly available evidence changes the action. Collecting more data that does not change a feasible decision has little instrumental value.
- Use the market as a benchmark, not as either an omniscient oracle or a fool. Ask why the signal is unpriced and what prevents competitors from closing it.
- Model joint bets and shared risk drivers; summing separate Kelly bets ignores dependence and shared collateral.
- Demand a full conditional payoff distribution and net wealth trajectory. Stops, win rate, and Sharpe alone cannot identify ruin or settlement risk.
- Make no-trade a valid optimized action when conservative net value is not positive, data are insufficient, or contract equivalence is unproven.
- Never turn a derivation, a published historical effect, or a persuasive causal story into an invented backtest or claimed deployable edge.
