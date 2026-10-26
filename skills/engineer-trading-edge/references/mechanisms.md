# Mechanism research blueprints

## Contents

- [How to use these blueprints](#how-to-use-these-blueprints)
- [Mechanism and discipline map](#mechanism-and-discipline-map)
- [1. Novel information through economic links](#1-novel-information-through-economic-links)
- [2. Calibration conditional on execution](#2-calibration-conditional-on-execution)
- [3. Forced flow versus fundamental news](#3-forced-flow-versus-fundamental-news)
- [4. Risk complementarity across the desk](#4-risk-complementarity-across-the-desk)
- [5. Capital occupation and convergence time](#5-capital-occupation-and-convergence-time)
- [6. Exact contracts and payoff constraints](#6-exact-contracts-and-payoff-constraints)
- [7. Hedging versus simply trading less](#7-hedging-versus-simply-trading-less)
- [8. Adaptive research expenditure](#8-adaptive-research-expenditure)
- [9. Latency and capacity together](#9-latency-and-capacity-together)
- [10. Opponent response and opportunity decay](#10-opponent-response-and-opportunity-decay)
- [Example: improving an indicator strategy](#example-improving-an-indicator-strategy)

## How to use these blueprints

Every blueprint below is an **untested research hypothesis**, an original synthesis for this skill, and a starting specification. None establishes current profitability, historical performance, or priority of discovery. Source identifiers refer to `sources.md`. Their findings motivate questions; they do not validate the proposed policies.

Select the blueprint that matches an observable mechanism and available data. Replace symbolic thresholds with values selected inside training periods under a declared mandate. Freeze the candidate family, benchmark, principal outcome and rejection rule before confirmation. Follow `validation.md` for chronological testing, dependent observations, trial accounting and prospective logging. Retain abstention as an action. A falsifier defeats the specified claim; insufficient power leaves it unresolved.

## Mechanism and discipline map

| Blueprint | Economic object | Connected discipline |
|---|---|---|
| 1 | Underprocessed new evidence | Bayesian inference; attention |
| 2 | Selection into realized trades | Auction theory; calibration |
| 3 | Compulsory demand | Institutional finance; causal inference |
| 4 | State-dependent marginal risk | Insurance; portfolio utility |
| 5 | Occupied collateral | Queueing intuition; capital allocation |
| 6 | Exact state payoffs | Logic; linear programming |
| 7 | Cost of risk removal | Insurance pricing; optimization |
| 8 | Value of another observation | Decision theory; bounded rationality |
| 9 | Value decay under impact | Microstructure; optimal control |
| 10 | Strategic response | Game theory; adaptive markets |

## 1. Novel information through economic links

**Anchors:** [I01], [I07], [I09], [I11]. **Hypothesis:** genuinely new information can reach a customer's price before a less-followed supplier's price because interpreting the economic connection consumes attention. Syndicated repetitions should not create additional Bayesian evidence.

**As-of data:** first-public timestamps, source lineage, document revisions, previously disclosed customer exposure, contemporaneous quotes, news load and sector returns. Freeze each relationship to its public disclosure date.

**Minimal policy:** map a new event into a signed exposure estimate; trade a bounded position only when the estimated residual payoff clears executable costs and a predeclared uncertainty hurdle. Use a fixed holding horizon or information invalidation; skip ambiguous exposure and stale news.

**Rival:** common industry shocks, ordinary momentum or retrospectively chosen relationships explain the effect. **Experiment/baseline:** compare a market-and-sector model, a simple customer-return model and the semantic model on identical chronological events; add matched unlinked firms and irrelevant-event placebos.

**Falsifier:** no incremental net value, or gains require later-known links. **Implementation risk:** incorrect entity resolution, stale contracts, duplicate stories, and arrival latency can convert apparent insight into already-priced information.

## 2. Calibration conditional on execution

**Anchors:** [I03], [I08], [B03], [V8]. **Hypothesis:** forecast quality can deteriorate precisely when a resting order receives a fill. Counterparties select when to trade, so unconditional calibration over all timestamps need not describe inventory actually acquired.

**As-of data:** submitted price, observed quotes, volatility, order age, acknowledgements, partial fills, cancellations and subsequent markouts. Log every attempt, including zeros and rejects.

**Minimal policy:** estimate both fill probability and payoff distribution conditional on each execution outcome. Choose passive, marketable or skip by expected net utility, including nonfill opportunity cost; cancel under a predefined stale-quote rule.

**Rival:** a change in signal quality or market state explains poor fills, rather than adverse selection. **Experiment/baseline:** hold forecasts and position limits fixed; compare immediate crossing, naive passive execution and conditional execution. Report scores within execution-state bins and outcomes over all attempts.

**Falsifier:** conditional routing adds no held-out net benefit or relies on impossible queue fills. **Implementation risk:** cancellation requests are not acknowledgements; partial inventory remains exposed. Avoid subtracting adverse selection twice when conditional payoff estimates already include it.

## 3. Forced flow versus fundamental news

**Anchors:** [R6], [R9], [R11], [V10]. **Hypothesis:** observable compulsory transactions can create temporary pressure, while information-driven transactions can justify lasting repricing. A profitable reversal policy must distinguish them before entry.

**As-of data:** announced index rules and changes, public auction information, dated holdings, actual publication lags, quotes, earnings/news timestamps and contemporaneous risk exposures. A falling price alone does not establish forced selling.

**Minimal policy:** estimate pressure from a documented obligation; enter only when estimated mechanical demand is large relative to available liquidity and competing news does not invalidate the valuation anchor. Define a maximum holding period and loss/capital limits.

**Rival:** sellers anticipate deteriorating fundamentals; the supposed pressure measure proxies for bad news. **Experiment/baseline:** compare ordinary reversal, pressure-only and pressure-plus-news policies on matched events with sector, liquidity and momentum controls. Seek externally determined rule changes for stronger identification.

**Falsifier:** the proposed pressure interaction adds no executable reversal or vanishes after point-in-time controls. **Implementation risk:** incomplete holdings, front-running competitors and long convergence delays can make an economically plausible effect inaccessible.

## 4. Risk complementarity across the desk

**Anchors:** [R1], [R3], [R4], [B07]. **Hypothesis:** a compensated exposure can be more valuable to one desk than another because their existing liabilities and crisis exposures differ. The comparative advantage may reside in the portfolio rather than superior prediction.

**As-of data:** synchronized sleeve returns, current positions, liabilities, collateral terms, cash reserves and scenario sensitivities; include unavailable marks and funding calls.

**Minimal policy:** allocate only if a candidate improves a declared portfolio objective after costs while satisfying joint loss and collateral constraints. Evaluate a candidate's incremental exposure, not its standalone Sharpe. Allow zero allocation despite positive expected profit.

**Rival:** apparent complementarity reflects short samples, stale prices or calm-period correlation. **Experiment/baseline:** compare equal-capital allocations, matched-risk allocations and the proposed scenario-aware policy using chronological and resampled crisis scenarios. Include a cash allocation alternative.

**Falsifier:** improvement disappears when common funding shocks or plausible tail dependence are included. **Implementation risk:** multiple brokers may not recognize economic offsets for margin; correlated withdrawals can destroy presumed liquidity. This blueprint improves suitability and capital use; it does not create new gross alpha.

## 5. Capital occupation and convergence time

**Anchors:** [R2], [R3], [R9], [B01]. **Hypothesis:** ranking opportunities by headline spread misallocates scarce capital when funding duration and interim collateral needs differ. Faster release can be valuable, but only if replacement opportunities actually exist.

**As-of data:** executable spreads, contractual maturities, resolution histories including failures, borrow/funding terms, haircut schedules and the contemporaneous opportunity set.

**Minimal policy:** estimate joint distributions of net payoff, convergence time and peak capital demand. Select a feasible portfolio maximizing the stated horizon objective against a maturity-matched cash alternative; prohibit assumed unlimited rollover.

**Rival:** shorter trades merely hide larger tail or reinvestment risk. **Experiment/baseline:** compare gross-spread ranking, simple expected-return ranking and duration-aware selection at identical liquid capital and stress limits. Replay the opportunity stream without future knowledge.

**Falsifier:** duration estimates provide no incremental utility or gains depend on unrealistic reuse of released cash. **Implementation risk:** settlement delay, borrow recall and margin expansion can extend the occupation window. Expected profit per capital-day is a screening statistic, not a complete objective or reliable annualized return.

## 6. Exact contracts and payoff constraints

**Anchors:** [B04], [B09], [B12], [R2]. **Hypothesis:** related contract prices can be inconsistent once their exact state payoffs are represented correctly; alternatively, precise semantics may explain an apparent inconsistency completely.

**As-of data:** contract wording and revisions, authoritative outcome source, boundary inclusivity, observation clock, void rules, executable depth, fees, collateral and settlement terms.

**Minimal policy:** create a complete relevant state set and payoff matrix A. Represent each permitted long/short leg with its own executable cost and quantity bound. Search by linear programming for a portfolio x whose net state payoffs meet a specified floor after funding, or minimize cost for an exactly matched target payoff. Claim arbitrage only if every permitted outcome and financing path supports it; otherwise classify a risky spread.

**Rival:** mismatched definitions, unavailable shorting or stale quotes generate the apparent gap. **Experiment/baseline:** compare headline matching with audited semantic matching and replay full executable bundles.

**Falsifier:** no feasible positive surplus survives complete states and costs. **Implementation risk:** atomic execution may be unavailable; unfilled legs, disputed resolution and cross-venue collateral cannot be removed by an algebraic proof.

## 7. Hedging versus simply trading less

**Anchors:** [R1], [R5], [R8], [B08]. **Hypothesis:** a hedge can improve portfolio utility when it removes a costly shared exposure more efficiently than reducing all profitable positions. Insurance may also consume the entire premium.

**As-of data:** executable hedge surfaces, full portfolio scenarios, physical payoff forecasts, risk-neutral prices, financing and margin rules. Keep horizons and units consistent when comparing implied and forecast variance.

**Minimal policy:** choose among unhedged smaller exposure, bounded exposure plus a specified hedge, and cash. Include hedge premium, renewal, basis, exercise and stressed liquidation in the joint objective.

**Rival:** the attractive equity curve results solely from lower exposure or an omitted insurance cost. **Experiment/baseline:** compare fixed hedging, state-aware hedging and simple deleveraging under equal capital and comparable tail constraints; freeze the hedge menu before testing.

**Falsifier:** the hedge offers no incremental utility beyond lower size after realistic prices and stress dependence. **Implementation risk:** protection can expire before the loss, fail on basis, or be unavailable during stress. A cheaper option is not necessarily cheaper protection against the relevant state.

## 8. Adaptive research expenditure

**Anchors:** [I06], [I07], [B03], [V1]. **Hypothesis:** scarce research time is best spent where another observation can improve a feasible decision before its opportunity expires. More analysis can reduce value through cost, delay and correlated evidence.

**As-of data:** sequential source arrivals, acquisition/computation costs, model versions, forecast snapshots, retrieval failures, action changes and quote changes during analysis.

**Minimal policy:** start with a calibrated inexpensive model. Estimate incremental decision value for each available research action; purchase the most valuable observation only while its conservative estimated benefit exceeds money and delay cost. Stop at the deadline or retain the baseline action.

**Rival:** apparent benefits arise from hindsight selecting which cases deserved deeper analysis. **Experiment/baseline:** train routing on earlier events; compare shallow, uniformly deep, simple threshold routing and learned routing at matched budgets. Evaluate the entire sequential policy.

**Falsifier:** routing adds no prospective net utility or fails after charging latency. **Implementation risk:** LLM fluency can masquerade as information gain; ten agents repeating one source supply one evidence lineage. Record routing variants in the trial ledger.

## 9. Latency and capacity together

**Anchors:** [I02], [I12], [R10], [V8]. **Hypothesis:** a signal's usefulness is a surface over delay, size and execution mode. Faster infrastructure matters only when additional captured value exceeds its cost; larger orders may erase the signal through impact.

**As-of data:** exchange/event, vendor-arrival, decision, submission, acknowledgement and fill timestamps; observed depth, actual participation, fees and benchmark prices. Audit clock alignment.

**Minimal policy:** estimate net value V(delay, quantity, mode); choose the feasible combination subject to uncertainty, deadline and capital limits. Integrate depth across the complete order rather than pricing every unit at the best quote.

**Rival:** measured latency decay is timestamp error, revised data or execution selection. **Experiment/baseline:** replay the same frozen signals at deliberate delays and size grids; compare simple marketable execution and a slower low-cost system. Confirm key regions with prospective shadow records.

**Falsifier:** positive value exists only below attainable latency, at unavailable size, or before total infrastructure costs. **Implementation risk:** exchange priority, queue cancellation and transient depth defeat naive replay; infrastructure speed cannot rescue an incorrect payoff forecast.

## 10. Opponent response and opportunity decay

**Anchors:** [B06], [B11], [I04], [V5], [V11]. **Hypothesis:** an exploitable behavior can weaken when counterparties learn, capital enters or venue rules change. A stable fallback and bounded exploitation may outperform permanent commitment to one observed weakness.

**As-of data:** dated rule/fee changes, spreads, markouts, participant proxies, forecasts, capacity and strategy versions. Treat counterparty identity and intent as uncertain unless directly documented.

**Minimal policy:** retain a feasible benchmark policy; permit a bounded deviation when prospective evidence supports incremental value. Review on a declared schedule or valid sequential detector; choose continue, reduce, pause or retire without unconstrained retuning.

**Rival:** ordinary sampling variation or exposure changes mimic strategic adaptation. **Experiment/baseline:** compare frozen exploit, frozen benchmark and prespecified adaptive policy; replay every review decision chronologically and examine forecast deterioration separately from capture deterioration.

**Falsifier:** adaptation fails to improve net utility or false alarms dominate avoided losses. **Implementation risk:** reacting to every loss mines noise, and switching itself incurs cost. Poker equilibrium analogies do not guarantee financial profitability; counterparties may rationally accept negative cash expectation for hedging utility.

## Example: improving an indicator strategy

Suppose an existing rule buys a closed-bar breakout when volume exceeds a threshold. Preserve its original entry clock, universe, size, stops and exits as the frozen baseline. The indicator describes an event; it does not yet identify the payer or mechanism.

Propose two competing explanations: new public information is still propagating, or temporary compulsory demand is exhausting itself. Use blueprint 1 to construct a first-publication novelty variable and blueprint 3 to identify independently documented mechanical-flow events. Do not label high volume itself as either mechanism.

Run a small, registered comparison: baseline; baseline plus novelty; baseline excluding documented flow events; and the combined rule. Measure all eligible opportunities, including skipped trades. Match capital and exposure so a filter cannot win merely by trading less. Use chronological event splits and charge actual observation-to-entry delay; a close-confirmed signal cannot assume an earlier closing fill.

Apply blueprint 2 if gross prediction survives but passive fills lose money. Compare the same forecasts under immediate crossing and fill-conditioned execution before adding indicators. Apply blueprint 7 only if portfolio tail exposure remains the binding problem.

Report where improvement occurs: forecasting, selection, capture, cost or portfolio utility. If the novelty variable adds no prospective value, remove it. If all benefit is reduced market exposure, describe that accurately. Respect any designated timing authority: research filters and execution changes must not silently replace the approved entry engine. No experiment here has been run; the output is a reproducible improvement plan with explicit alternatives.
