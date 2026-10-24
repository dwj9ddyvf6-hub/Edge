# Evidence, validation, and behavioral edge

Research memo, 2026-10-23. Primary papers and author/publisher copies; source conclusions are distinguished below from proposed engineering rules and original hypotheses. This is a research component for the parent task, not a claim that any strategy has been validated.

## 12 core primary sources

### V1. Halbert White (2000), A Reality Check for Data Snooping
https://www.ssc.wisc.edu/~bhansen/718/White2000.pdf
Econometrica 68(5), 1097–1126. Retrieved/opened as turn44view0.

Supports: selecting a successful model after extensive reuse of one history requires comparison against the full search, not a test that treats the winner as the only attempted model. Reality Check tests whether the best candidate has predictive superiority over a specified benchmark. An illustration changes a naive directional-accuracy p-value of .0036 to a Reality Check p-value of .2040.

Limit: a correction only knows the candidate universe recorded; unreported failed experiments, researcher discretion, and subsequent revisions remain material. A test of predictive superiority is not evidence that the return mechanism is causal or economically large. The inference relies on the sampling/dependence assumptions of the procedure.

### V2. Peter Reinhard Hansen (2005), A Test for Superior Predictive Ability
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=264569
https://reinhardhansen.github.io/research.html
Journal of Business & Economic Statistics 23(4), 365–380. DOI 10.1198/073500105000000063. Author abstract retrieved in turn58search9 and SSRN turn58search3; publisher open was unavailable.

Supports: SPA improves on Reality Check through studentization and a sample-dependent null distribution, making it less sensitive to irrelevant poor alternatives. Test the null that the benchmark is not inferior to any candidate. A global rejection means at least one candidate improves the chosen loss measure; it does not automatically certify the selected individual winner.

Limit: preserve joint dependence in candidate performance when resampling. Do not choose whichever of many statistical tests gives the desired answer. Use a prespecified principal test with diagnostics.

### V3. David H. Bailey and Marcos López de Prado (2014), The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality
https://www.davidhbailey.com/dhbpapers/deflated-sharpe.pdf
Version July 31, 2014. Retrieved/opened turn44view2.

Supports: DSR incorporates trial-selection inflation, return non-normality, track-record length, skewness, kurtosis, and the distribution of attempted Sharpe ratios. The count of effectively independent trials matters; correlated trials are not equivalent to wholly independent trials.

Limit: DSR is a model-based significance diagnostic, not a calibrated posterior probability that a strategy will earn money in production. It cannot repair leakage, unknown trials, stale fills, implementation errors, or structural change. Its inputs and dependence assumptions must be documented; naïve square-root annualization and treating overlapping returns as independent can mislead.

### V4. David H. Bailey, Jonathan M. Borwein, Marcos López de Prado and Qiji Jim Zhu (2015 working version), The Probability of Backtest Overfitting
https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
February 27, 2015 author version. Retrieved/opened turn44view3; rank definition verified at turn56view4.

Supports: PBO concerns the strategy-selection process: how often the configuration selected as best in-sample ranks below the median out-of-sample. CSCV estimates this using combinations of data partitions. PBO is distinct from probability of losing money; being below the candidate median and having negative return are different events.

Limit: combinatorial partitions are a diagnostic of selection instability and do not reproduce every chronology of a live adaptive system. They cannot replace forward chronological validation with all refits, selection decisions, and execution restrictions. Never label 1−PBO as the probability of future profit.

### V5. Andrew W. Lo (2004), The Adaptive Markets Hypothesis: Market Efficiency from an Evolutionary Perspective
https://web.mit.edu/Alo/www/Papers/JPM2004_Pub.pdf
Journal of Portfolio Management, 30th anniversary issue. Retrieved/opened turn44view6.

Supports: market efficiency and strategy profitability can evolve with competitors, capital, institutions, and conditions. A strategy's opportunity set can contract or reappear. The paper explicitly presents a developing framework, not a fully articulated quantitative law.

Limit: an ecological story does not identify the correct regime variable, timing rule, decay rate, or adaptation speed. Those require forecasts and prospective tests. Automatic retuning after each loss can be data mining disguised as adaptation.

### V6. Terrance Odean (1998), Are Investors Reluctant to Realize Their Losses?
https://faculty.haas.berkeley.edu/odean/papers%20current%20versions/areinvestorsreluctant.pdf
Journal of Finance 53(5), 1775–1798. Retrieved/opened turn44view4.

Supports: brokerage records for 10,000 accounts show a preference to realize gains over losses; rebalancing, transaction-cost explanations, and subsequent performance do not adequately explain the pattern in that sample. The paper considers mechanisms by which disposition behavior can slow incorporation of information.

Limit: evidence of individual bias is not by itself a tradable price effect. One must show the biased holders influence marginal price, are identifiable using available data, and generate a sufficiently persistent after-cost opportunity. Historical sample behavior is not an invariant universal fact.

### V7. Brad M. Barber and Terrance Odean (2000), Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors
https://faculty.haas.berkeley.edu/odean/papers/returns/individual_investor_performance_final.pdf
Journal of Finance 55(2), 773–806. Retrieved/opened turn44view5; abstract turn56view6.

Supports: in 66,465 discount-brokerage households during 1991–1996, the most active traders had markedly worse net returns; the findings are consistent with overconfidence and a substantial trading-cost penalty.

Limit: association is not experimental proof that overconfidence caused every trade. Avoid universalizing dated retail transaction costs. For an LLM, confident prose and high activity are not evidence of edge; measure forecast calibration and incremental net utility.

### V8. A. Philip Dawid (1984), Present Position and Potential Developments: Some Personal Views—Statistical Theory: The Prequential Approach
https://academic.oup.com/jrsssa/article/147/2/278/7106293
https://people.csail.mit.edu/jrennie/trg/papers/dawid-prequential-84.pdf
JRSS Series A 147(2), 278–290. DOI 10.2307/2981683. Publisher summary opened turn44view7.

Supports: evaluate inference through sequential probability forecasts of future observations. This motivates a record of forecasts made before outcomes, followed by prospective scoring.

Limit: calibration alone is insufficient for a profitable action policy. A calibrated base-rate forecast can be uninformative; a useful forecast can still be untradeable at the available price. Score forecasts against a market/base-rate benchmark, then separately assess execution and decision value.

### V9. Qingyun Sun and Stephen Boyd (2018), Distributional Robust Kelly Gambling: Optimal Strategy under Uncertainty in the Long-Run
https://arxiv.org/abs/1812.10371
Author paper opened turn44view8.

Supports: when the probability distribution lies in an uncertainty set, optimize the worst-case expected log growth over that set. The problem is convex, and tractable cases are described. The model explicitly represents ambiguity about the return distribution rather than treating a point estimate as truth.

Limit: robustness depends on the choice of uncertainty set, wealth dynamics, and feasibility assumptions. Incorrectly narrow sets offer false protection. Conservative sets can reject worthwhile bets. The mathematical result is not universal protection from market gaps, leverage constraints, or unmodeled settlement losses.

### V10. A. Philip Dawid (2020), Decision-theoretic Foundations for Statistical Causality
https://arxiv.org/abs/2004.12493
Author paper opened turn44view9.

Supports: using observational data to decide an intervention requires justified relationships between observed and decision regimes. Exchangeability and ignorability assumptions have substantive content; statistical fit alone does not provide them.

Limit: predicting a trade's return need not identify every structural causal parameter. However, claiming a particular participant or mechanism causes an opportunity requires stronger identification than a profitable backtest. The act of trading at scale also changes the decision regime through market impact.

### V11. R. David McLean and Jeffrey Pontiff (2016), Does Academic Research Destroy Stock Return Predictability?
https://onlinelibrary.wiley.com/doi/10.1111/jofi.12365
Journal of Finance 71(1), 5–32. First online October 13, 2015. Publisher abstract opened turn56view1.

Supports: for 97 studied cross-sectional predictors, average returns declined 26% out-of-sample and 58% post-publication relative to in-sample. The authors interpret part of the additional decline as publication-informed trading and report increased correlations between predictor portfolios.

Limit: these are sample findings and identification-based interpretations, not a universal 58% haircut. They do not isolate every source of decay or establish that every public strategy is unprofitable. The relevant lesson is to measure opportunity durability and crowding using prospective evidence.

### V12. Andrew Y. Chen, Alejandro Lopez-Lira and Tom Zimmermann (2022 working paper), Does Peer-Reviewed Research Help Predict Stock Returns?
https://arxiv.org/abs/2212.10317
Author paper opened turn56view2; use this explicitly as the retrieved working-paper version, not an asserted latest journal version.

Supports: their data-mined accounting-ratio predictors exhibit post-sample performance comparable to published predictors, and theoretically motivated labels do not reliably establish stronger durability. This is a useful counterweight to storytelling as evidence.

Limit: the finding concerns a defined stock-predictor comparison, not a theorem that mechanisms are useless. Mechanisms remain useful for designing falsifiers, diagnosing failures, anticipating constraints, and specifying where a model may transfer. A polished economic explanation must never replace measurement.

Additional nuance, not needed in the core 12: Andrew Y. Chen (2022), Most Claimed Statistical Findings in Cross-Sectional Return Predictability Are Likely True, https://arxiv.org/abs/2206.15365, opened turn56view3. The paper disputes blanket claims that most published factors are false and emphasizes that non-significance is not equivalent to a false discovery. This is a research debate; do not repeat either side's global claim as established universal fact.

## Practical synthesis: evidence levels must remain separate

Use four independent records, never a single confidence adjective:

1. Mechanism evidence: documented incentives, constraints, market rules, information timing, and counterparty behavior. Label a mechanism as identified, supported, plausible, or unknown. A vivid story is not identification.
2. Prediction evidence: timestamped probabilities or return distributions before outcomes, benchmark-relative loss, calibration, resolution, and stability.
3. Capture evidence: executable bid/ask, conditional fills, latency, queue, fees, borrow, financing, impact, rejected orders, and collateral paths.
4. Economic suitability: after-cost returns relative to relevant exposures and capital usage, portfolio marginal contribution, funding survivability, and tail loss under stress.

A strategy can pass one record and fail another. An empirically supported but unexplained signal can remain a candidate; it should carry greater model uncertainty and more demanding transfer tests, not be rejected automatically because an LLM cannot tell a story. A convincing mechanism with no prospective effect remains a hypothesis.

## Actionable research protocol

The following is an original engineering synthesis informed by the sources, not a procedure quoted from any single paper.

A. Define the claim before looking at results. State instrument, participant paying, information or constraint, action, horizon, time of observation, execution assumptions, unit of independent evidence, and what would disprove it. Name the estimand: forecast improvement, total net return, factor-adjusted return, or incremental portfolio utility. These are different questions.

B. Keep an append-only trial ledger. Register every feature, universe screen, parameter variation, label, stop/target variant, execution assumption, data revision, agent suggestion, and discarded model that could affect selection. LLM-generated strategy batches count as trials. Record code/data hashes, timestamps, and test access. If prior search is unknown, label selection-adjusted inference incomplete and prefer new prospective evidence.

C. Audit causal availability. Join data using the first time it was truly available; keep revisions and reporting lags. Include delisted securities, expired contracts, bankruptcies, missing observations, and rejected executions. Distinguish event time, exchange timestamp, vendor delivery, processing, and decision time. An indicator calculated after a bar closes cannot trade at an unavailable earlier close.

D. Make splits reflect the deployment. Use chronological outer evaluation. Within each training period, perform fitting, feature selection, hyperparameter choice, thresholding, and probability calibration without touching outer outcomes. When labels span intervals, remove training observations whose information/label interval overlaps test outcomes; use an appropriate separation where retained future training data would otherwise carry test information. Determine gaps from label horizon and dependencies, not a magic percentage. Reproduce scheduled online refits exactly.

E. Respect dependence. Overlapping trades, common event outcomes, clustered securities, and shared market shocks reduce independent evidence. Resample blocks or event clusters at the relevant level while keeping candidate return vectors aligned. Cross-sectional rows on the same date cannot be assumed independent. Show sensitivity to plausible block lengths. Autocorrelation adjustments do not repair nonstationarity by themselves.

F. Separate exploration from confirmation. Freeze one principal benchmark, loss/return measure, test family, cost model, and decision threshold before confirmation. Apply a search-aware method such as SPA/Reality Check where its assumptions fit; use DSR/PBO as complementary diagnostics rather than votes whose average creates certainty. If using repeated interim looks, employ a valid prespecified sequential procedure or account for repeated testing. Reusing a final holdout after a failure turns it into training data.

G. Use null strategies that isolate the claim. Include cash, static market exposure, a matched-risk/factor portfolio, matched holding-period and turnover controls, delayed signals, randomized event times inside defensible blocks, feature ablations, and the same executor without the disputed feature. Choose nulls appropriate to the mechanism; arbitrary shuffling can destroy the dependence one needs to preserve. For a proposed filter, evaluate all eligible opportunities, including abstentions, so selection does not hide opportunity cost.

H. Test whether improvements survive the full system. Compare old and new variants on identical external decision opportunities, with identical capital and feasible execution. Attribute the difference to forecast quality, selection, execution, position size, hedging, or cost. Do not call leverage-induced returns improved edge. Check whether an added filter simply reduces exposure or removes inconvenient historical losses.

I. Stress economic capture. Use observed spreads where available, conservative executable sides, fill-conditioned adverse selection, costs during stress, financing/margin changes, fee changes, and smaller available size. Calculate the break-even cost and capacity curve. A result that only exists at unachievable fills fails regardless of statistical significance.

J. Run prospective shadow evaluation. Log probabilities, proposed actions, abstentions, orders, feasible fills, and invalidations before results. Freeze promotion and retirement rules. Diagnose forecast deterioration separately from fill deterioration and changes in risk price. Refit only on a documented schedule or a prespecified detector with its own false-alarm control.

## Hard gates without arbitrary universal thresholds

Select governance parameters before evaluation: economic hurdle h, maximum acceptable false-promotion probability alpha, research family, maximum capital loss L, liquidity/collateral buffer B, and allowable model dependence. Derive them from costs, mandate, horizon, capital, and consequences of a wrong deployment. If unknown, present parameterized gates and remain at research/shadow status; do not invent desk permissions.

Reject or hold the candidate if ANY of the following fails:

- Availability: every decision-critical input is point-in-time valid, or the unresolved discrepancy is explicitly excluded from the experiment.
- Executability: the intended access, instrument, data, fee, size, and settlement assumptions can be met. A favorable market midprice without feasible execution is insufficient.
- Evidence: under the prespecified valid inference procedure, the lower confidence bound for the specified net benefit exceeds h. If evidence is insufficient, classify it as inconclusive, not proven false. A global test rejection requires appropriate candidate-specific follow-up before promoting one model.
- Robustness: the candidate meets the mandate under the predetermined relevant scenario set and plausible costs. It need not win in every regime; losses in the very states it is paid to insure may be expected, but must be explicitly capitalized.
- Survival: collateral and liquidity remain adequate under the agreed stress set; loss limits are defined and operationally testable. Historical maximum drawdown is not a bound on future loss.
- Incrementality: any claim of improvement is supported against the frozen existing strategy under matched risk and capital; any claim of alpha is assessed relative to the relevant exposure benchmark.
- Reproducibility: a replay can regenerate decisions from the pinned inputs and code, and prospective logs confirm the implemented policy matches the tested one.

These are decision gates, not universal statistical constants. Do not demand a fixed win rate, Sharpe, 100 trades, p<.05, DSR>.95, or 30 days for every strategy. Determine sample sufficiency from effect size, dependence, tails, event frequency, and the error cost. Passing a gate establishes bounded evidence under assumptions, not certainty of future profit.

## Mathematical correction: uncertainty does not automatically mean fractional Kelly

For a binary bet with net win odds b>0 and fraction f, expected log growth is
G(f,p)=p log(1+bf)+(1-p)log(1-f).

If p has a Bayesian posterior and this is the complete one-period model, E_p[G(f,p)]=G(f,E[p]). The optimizer uses the posterior mean probability. Parameter variance alone does not algebraically create fractional Kelly. A prior can shrink the posterior mean; drawdown aversion, model ambiguity, constraints, and multi-period learning objectives can justify different allocations.

For an ambiguity interval p in [p_L,p_U] and a long-only bet, worst-case expected log growth uses p_L because log(1+bf)>log(1-f) for f>0. The robust fraction is max(0,(b p_L-(1-p_L))/b), subject to f<1 and other portfolio constraints. If the conservative probability does not clear the executable break-even probability 1/(b+1), hold cash. This example is algebraic, not a trading recommendation.

## Three testable new synthesis hypotheses

1. Edge decay can be diagnosed by a forecast–capture decomposition. Hypothesis: a strategy's post-publication deterioration first appears in conditional fill quality and execution delay for some markets, while forecast scores remain stable. Test fixed timestamped forecasts, tradeable prices at multiple delays, and fill-conditioned outcomes before/after a documented competition change. Reject if forecast deterioration alone explains performance or no interaction survives held-out testing. This can distinguish a speed/access bottleneck from a failed information model; it is not evidence that the hypothesis already holds.

2. Behavioral edge requires a price-setting transmission test. Hypothesis: a disposition-based signal predicts returns only when estimated reference-point concentration interacts with constrained or low-liquidity holder demand. Test the interaction against each component, exposure controls, plausible alternative flow mechanisms, and matching designs with genuinely exogenous changes if available. Reject if the signal does not strengthen in the proposed transmission conditions. This converts a vague 'people are irrational' story into a falsifiable market mechanism.

3. The most efficient research allocation may maximize expected decision improvement per scarce research hour. Hypothesis: after the forecast is modestly informative, reducing execution uncertainty or eliminating leakage creates more out-of-sample utility than adding further correlated indicators. Randomly assign comparable research tasks to signal additions, cost measurement, and causal-data cleanup; freeze evaluation and compare incremental prospective net utility per unit of effort. Reject if additions consistently dominate under matched budgets. Treat data quality and capture as economically valuable research targets, while keeping them conceptually distinct from gross alpha creation.

## Instructions to the final skill author

Make the LLM say which status it has earned: proposed mechanism; historically supported signal; executable after-cost candidate; forward-supported policy; or deployed and monitored system. Never jump from prose to the last category. Retain creativity in hypothesis generation and skepticism in evaluation. Ask what compensates the trade and what prevents competition from removing it, but never allow the answer to those questions to substitute for a timestamped, after-cost test.
