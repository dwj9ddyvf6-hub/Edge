# Trading Edge Lab v2: independent economic audit

Audit date: October 23, 2026, America/New_York. Auditor reviewed all five authored Markdown files in the saved skill: `SKILL.md`, `foundations.md`, `mechanisms.md`, `validation.md`, and `sources.md` (941 lines total). This is a substantive audit of the files, not a claim to have reread every original paper in the v1 register. No skill files were changed by this auditor.

## 1. Verdict and exact corrections

The v1 skill is unusually strong on economic mechanism, executable pricing, point-in-time evidence, selection bias, conditional fills, and honest evidence stages. I found no substantive arithmetic error in its displayed examples or central identities. Its limitation is architecture: the instructions describe a rigorous research process but do not yet specify a complete adaptive decision system. More references alone will not close this gap.

### Priority 0: correct the abbreviated arbitrage definition

The core says: “a feasible self-financing payoff with no negative state payoff and a positive payoff in at least one relevant state.” The detailed foundation correctly adds nonpositive initial cost and positive probability. Make the core equally explicit: **a feasible self-financing strategy with nonpositive initial net cost, no negative terminal net payoff almost surely, and a strictly positive benefit with positive probability, including every interim funding obligation and contractual outcome.** A favorable state of zero probability does not establish conventional arbitrage; omitting the initial investment condition can misclassify a purchased positive payoff.

### Priority 1: distinguish adaptation of state from adaptation of policy

The current “continue, reduce, pause, investigate, retire” language is useful but underspecified. Separate four clocks:

- Refresh observations and reconcile positions as events arrive.
- Update an approved belief state using a fixed update rule.
- Choose actions within a fixed, authorized policy class.
- Propose and evaluate a different policy on a slower research clock.

Only the last is model/strategy promotion. A faster quote update must not quietly become faster live rule mutation. Every adaptive rule, including change detectors and switching thresholds, is itself a strategy that must be replayed and evaluated.

### Priority 1: specify robust incremental action value

V1 has utility, EVSI, and risk constraints, but no precise decision certificate. Add a common numeraire, feasible action set, baseline continuation, joint outcome model, uncertainty set, and measurable difference in utility. Include HOLD, WAIT, REDUCE, CANCEL, and INVESTIGATE as appropriate, rather than reducing the action set to BUY/SELL/PASS. “No new trade” does not mean “liquidate existing inventory.”

### Priority 1: make endogenous feedback explicit

V1 mentions impact and opponent response, yet replay could still be read as if the future outcome path remains invariant when policy changes. Increasing size, changing venue, routing orders, or publishing a signal may change fills, prices, competitors, and the next training dataset. Separate exogenous market change, selection into observed outcomes, and change caused by the desk's own action. Stable retraining is not proof of optimality. [E02, E03]

### Priority 2: quantify capacity before allocating bandwidth

Replace rankings based only on expected return, Sharpe, or “confidence” with constrained incremental desk value. Capital, collateral, inventory, venue capacity, borrow, message rate, compute, and operator attention are separate resources. A trade can have positive standalone EV but negative desk value because it displaces something better. Scarcity prices are estimates from a specified optimization problem, not universal penalty constants.

### Priority 2: add counterfactual portfolio attribution

The current marginal-portfolio requirement needs two distinct comparisons: add a candidate while keeping the rest fixed; and add a candidate while reoptimizing the rest. The second answers resource replacement but combines candidate effect with reallocations. Report both when feasible. Contributions generally do not add up under nonlinear risk, impact, and shared constraints; do not sum standalone sleeve benefits as if independent.

### Priority 2: replace broad “more intelligent” claims with measurement

Define coverage, delay, missed deadlines, stale decisions, decision quality, adaptation lag, false alarms, transaction burden, and economic value per resource unit. Daily operation is feasible as observation/research/risk management; daily profitable entry cannot be required without changing the objective. Fewer trades can be the measurable improvement.

## 2. Additions that create a useful master algorithm

The following is an original engineering synthesis and elementary decision-theoretic derivation. It is not a claimed result of any one source, a market experiment, or a universal profit guarantee.

### A. Decide whether additional intelligence can change an action

Let `I_t` be the information actually available, `s_t` the reconciled portfolio/execution state, `A_t` the feasible action set, `a0` the approved continuation, and `P_t` a documented family of plausible joint distributions. The utility difference must use the same initial wealth, liabilities, horizon, and numeraire:

`Delta_P(a,a0) = E_P[U(W_H^a) - U(W_H^a0) | I_t, s_t]`.

Execution, future funding, and the effect of the action on outcomes belong inside `W_H^a`. Treat a paired historical replay as an approximation whose interference assumptions must be stated.

A robust improvement test is

`L_t(a,a0) = inf_{P in P_t} Delta_P(a,a0)`.

Deploy the action only if it is feasible, within the evidence stage, and its predeclared lower-value criterion clears the hurdle. If selecting among many candidates, use a simultaneously valid uncertainty procedure or a selection-aware evaluation; the best of many ordinary pointwise lower bounds is not automatically a valid lower bound for the selected winner. An ambiguity-set minimum is also not automatically a frequentist confidence bound. Label which one is being used.

For runtime efficiency, certify a cheap action if uncertainty cannot change its identity. In a finite action menu with valid bounds `[L(a), U(a)]`, an action dominates the alternatives if `L(a*) > max_{b != a*} U(b)` after the chosen switching cost/hurdle. If this is not true, do not infer that deeper computation must help: estimate whether the remaining uncertainty is reducible in time and whether any feasible action can improve. This gives three useful states: **decisive**, **decision-sensitive**, and **unresolvable before deadline**.

Raw predictive entropy is a poor escalation trigger. For a one-dollar binary contract with all-in purchase cost 0.60 and a long-or-pass action set, every defensible probability in `[0.50,0.55]` implies passing; uncertainty about the exact probability is irrelevant to this action. An interval straddling 0.60 can be action-sensitive. Conversely, a very low-probability state can be important because its loss is enormous. Evaluate expected decision improvement, not uncertainty alone.

### B. Separate a forecast from the control score

Decision-focused training can weight errors according to their effect on downstream decisions [E01]. Preserve separate records for a calibrated predictive distribution and a policy score. A score optimized to improve an allocation objective is not automatically an honest probability. Keep proper scoring, fill-conditioned diagnostics, and policy economics side by side. Train a small registered set of decision losses and compare chronologically; do not tune to historical P&L until a desired answer emerges.

### C. Give scarce capital a price without charging it twice

For illustration, let the desk choose a final position vector `q` from current `q0` under a one-period certainty-equivalent model:

`maximize mu' q - (gamma/2) q' Sigma q - C(q-q0)`

`subject to A q <= b` and instrument/operational bounds.

All terms must share currency/utility units; `gamma` is a declared preference parameter, `Sigma` is the joint uncertainty model, and `C` includes only costs not already in `mu`. The Lagrange multiplier `lambda_j` is the model-implied marginal increase in optimized objective from relaxing resource `b_j` locally. Under differentiability/regularity, interior trade changes balance expected marginal value, portfolio risk, impact, and scarce-resource use.

Use this in one of two consistent implementations: a joint optimizer enforces shared constraints; or subordinate sleeves receive resource prices from a coordinator. Do not subtract `lambda'Aq` again from realized P&L or call it a broker cost. It is a decision/opportunity-cost device. Likewise, do not deduct a capital opportunity penalty if a dynamic continuation value already accounts for displaced future opportunities. Report capacity curves, not a single “maximum size”: changing size changes return, impact, and sometimes the information environment. [E04]

### D. Diversify the causes of forced action

Ordinary return correlation misses common owners, collateral providers, borrow sources, venues, clearing dependencies, and the same urgent exit clock. Build a dependency map: sleeve -> instruments -> liquidity/financing/settlement resource -> failure scenario. Unknown dependencies remain unknown, not zero. Test whether all apparently different models need the same market depth at the same time. Ownership-based fragility provides a specific empirical precedent, but its historical covariance estimates and reporting lags cannot be imported as current intraday signals. [E05]

### E. Model WAIT as a real action

At an eligible moment, compare the executable value of immediate action with an attainable continuation policy that may acquire evidence, receive a better quote, or redeploy capital. Waiting changes the opportunity: the quote may disappear, the event may resolve, competitors may act, and current inventory continues to carry risk. Never compute the value of waiting by learning the future while retaining today's quote. Real-options theory motivates this distinction, but a quoted security is usually more reversible and more competitive than the irreversible project in that literature. [E06]

A useful Bellman-style comparison is `V_t(s,b) = max_a {r_t(s,b,a) + E[V_{t+1}(s',b') | s,b,a]}` with feasible actions and explicit horizon/discounting. This is a specification, not an algorithm that can be solved without models of transitions, beliefs, execution, and constraints. A short-horizon approximation with conservative terminal values may be preferable to an unidentifiable large model.

### F. Define coverage honestly

Measure operational coverage as **eligible opportunities receiving a valid decision by their deadline divided by all eligible opportunities in an independently defined feed**. Publish the opportunity-generation rule before outcomes. This metric includes abstentions and does not claim profitable opportunity recall. Separately report coverage by economic mechanism, contract, horizon, and shared risk driver; more instruments or model agents do not imply more independent opportunities.

Wider opportunity menus create additional research selection and maintenance costs. Add a sleeve when its incremental feasible portfolio value justifies those costs, not to manufacture daily activity. A desk can be perceptive every day while finding no adequately supported paid risk or mispricing today.

## 3. A compact impossibility boundary worth adding

**Finite-horizon derivation under explicit assumptions:** suppose discounted tradable gain increments (including dividends) obey `E[Delta S_(t+1) | F_t] = 0` under the actual probability law, and an admissible predictable strategy `h_t` has the integrability needed for conditional expectation. With nonnegative trading costs,

`E[G_T] = E[sum_t h_t Delta S_(t+1) - Costs_T] = -E[Costs_T] <= 0`.

Adaptive sizing, timing, model ensembles, and stopping do not create positive expected profit in that specified world. This statement uses the **physical** probability law and a finite, integrable setup; a risk-neutral martingale alone does not rule out physical risk premia. Infinite doubling violates the relevant admissibility/funding conditions. The constructive objective is to find where the assumptions fail in a measurable, capturable way, or to improve costs/risk/utility even if alpha remains absent.

This boundary is enough to reject the request's literal universal-edge guarantee without dismissing the useful engineering ambition. A controller can improve the quality and efficiency of decisions, and can correctly retire a strategy that cannot earn the required premium.

## 4. New primary-source register (six distinct sources)

### E01 — Elmachtoub and Grigas, Smart “Predict, then Optimize”

Published *Management Science* 68(1), 9–26 (2022); inspected arXiv v5 dated November 19, 2020. [Primary full text](https://arxiv.org/html/1710.08005v5). [DOI](https://doi.org/10.1287/mnsc.2020.3922).

**Access:** introduction, framework, loss definitions, and exact consistency assumptions inspected. **Limit:** the inspected consistency theorem needs central symmetry, continuity, a nonempty feasible interior, and its stated optimizer conditions. Its objective has unknown linear cost coefficients and a specified feasible set. These results do not certify trading under unknown impact, feedback, tails, or drift. **Use:** compare decision-focused training with ordinary predictive training, while separately checking calibration and real execution. Fix tie-breaking; favorable hindsight tie resolution can produce degenerate apparent performance.

### E02 — Perdomo, Zrnic, Mendler-Dünner, and Hardt, Performative Prediction (2020)

*PMLR* 119, 7599–7609. [Primary paper](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf).

**Access:** definitions, causal interpretation, repeated risk minimization, assumptions, and convergence theorem inspected. **Finding:** the deployed predictor can affect the distribution it predicts. Retraining convergence requires sufficient smoothness, strong convexity, and weak-enough distributional sensitivity in the analyzed result. **Limit:** its fixed map from deployed parameter to outcome distribution does not automatically describe independently changing markets. Stability and performative optimality are distinct. **Use:** log size and deployment as possible causes of measured deterioration; do not label every feedback problem exogenous “regime change.” The paper supplies a mathematical lens, not a ready-made trading controller.

### E03 — Miller, Perdomo, and Zrnic, Outside the Echo Chamber: Optimizing the Performative Risk (2021)

*PMLR* 139. [Primary paper](https://proceedings.mlr.press/v139/miller21a/miller21a.pdf).

**Access:** introduction, Proposition 2.1 and its constructive example, convexity assumptions, and optimization discussion inspected. **Finding:** stable retraining can be arbitrarily suboptimal; in a constructed model it can maximize the deployment-dependent risk. Optimizing induced outcomes requires additional structure. **Limit:** convexity of the ordinary loss is insufficient; structural assumptions on the distribution map matter. **Use:** judge adaptation by prospective deployment value against a frozen feasible baseline, not whether parameters converge or the training score improves. Do not infer that unconstrained exploration of a live market is justified.

### E04 — Berk and Green, Mutual Fund Flows and Performance in Rational Markets

2004 publication, inspected author manuscript October 15, 2002. [Primary manuscript](https://users.nber.org/~confer/2002/apf02/berk.pdf). [Author institution record](https://www.gsb.stanford.edu/faculty-research/research/publications/mutual-fund-flows-performance-rational-markets).

**Access:** opening argument and model's increasing-cost/decreasing-return assumptions inspected. **Finding:** with competition for capital and declining scale efficiency, genuine managerial ability can coexist with no persistent investor abnormal return. **Limit:** this is an equilibrium model of delegated management with stated information, fee, and risk assumptions; it does not prove any desk's capacity curve. **Use:** distinguish skill, captured dollar value, return per dollar, and the surplus left after fees/costs/capital entry. Estimate how expansion affects those quantities instead of extrapolating a small experiment linearly.

### E05 — Greenwood and Thesmar, Stock Price Fragility (2011)

*Journal of Financial Economics* 102(3), 471–490. [Primary article PDF](https://tevgeniou.github.io/EquityRiskFactors/bibliography/Fragility.pdf). [DOI](https://doi.org/10.1016/j.jfineco.2011.06.003).

**Access:** abstract, opening construction, US 1990–2007 empirical setting, co-fragility extension, and stated endogeneity cautions inspected. **Finding:** concentrated ownership and correlated liquidity needs can predict nonfundamental volatility and comovement. **Limit:** the authors describe stronger endogeneity concerns for the comovement interpretation; observed mutual-fund ownership is an incomplete view of ownership. **Use:** extend risk mapping without treating historical ownership relationships as current information.

### E06 — McDonald and Siegel, The Value of Waiting to Invest (1986)

*Quarterly Journal of Economics* 101(4), 707–727; NBER 1019 (1982). [Primary NBER abstract and publication record](https://www.nber.org/papers/w1019). [Author institution record](https://www.kellogg.northwestern.edu/academics-research/research/detail/1986/the-value-of-waiting-to-invest/). [DOI](https://doi.org/10.2307/1884175).

**Access:** primary abstracts and institutional publication record; full NBER PDF returned 403. **Finding:** uncertain, irreversible investment has a waiting option omitted by a simple positive-NPV rule. **Limit:** no numerical threshold or project-specific formula is imported into trading; full paper was not read here. **Use:** treat waiting as a valued continuation action, while explicitly accounting for competition, lost quotes, reversibility, and finite opportunity lifetime.

## 5. Minimal implementation changes and forward-test cases

Keep the core short: repair the arbitrage sentence; add one “adaptive control” section with state/policy clocks and mandatory reference loading; move equations, state contracts, and examples into one addendum reference. Do not duplicate v1's entire source register or turn each response into a 30-step essay. Preserve the valuable distinction between mechanism, evidence, capture, and portfolio suitability.

Recommended raw task tests:

1. A strategy's global probability score improves but decisions are unchanged, costs rise, and time-to-decision doubles. Does the skill demand decision value and identify a cheaper equivalent action?
2. A model retrains to stable parameters while its size triples and fill-conditioned markouts deteriorate. Does it separate feedback, selection, and forecast change rather than blindly retrain?
3. Two independent-looking sleeves have low ordinary correlation but share the same financing provider and emergency liquidation venue. Does it identify joint resource failure and compare smaller exposure?
4. A positive-EV short-lived opportunity ties up collateral across a known future auction. Does it consider replacement/continuation value without inventing profitable reinvestment or double charging a shadow price?
5. A desk asks for a trade every day although all candidate lower bounds are below the hurdle. Does it retain useful daily monitoring/research while refusing to fabricate an edge or relax the evidence criterion silently?
6. A robust forecast set implies the same action throughout, but an entropy-based router wants expensive deeper reasoning. Does it stop early or redirect research to a decision-sensitive opportunity?

These are proposed tests, not completed test outcomes. The proposed controller's economic quality remains untested until the complete policy is evaluated against a frozen feasible baseline with actual data and costs.
