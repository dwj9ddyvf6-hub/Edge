# Trading Edge Lab v2 — control, beliefs, computation, and adaptation

Research memo prepared 2026-10-24 UTC. Scope: existing SKILL.md read in full. This memo proposes an operational addendum; no strategy performance, live trading, or production readiness has been established. Source access below distinguishes inspected body sections from abstract-only access. The proposed master algorithm is a synthesis, not a theorem from any one paper.

## Assessment of v1

The existing core gets the hard economic distinctions right: expected payoff versus alpha versus portfolio utility, a named payer or wedge, executable rather than chart prices, conditional fills, information provenance, bad-state risk, and research-process-aware validation. Retain these foundations. Section 8 is too high-level to make “dynamic” operational: it names monitoring and decisions without defining sufficient state, action semantics, competing policies, belief uncertainty, computation deadlines, or the distinction between adaptation inside an approved policy and changing that policy. The fix is a small controller with explicit contracts and a slow evidence loop, not a default POMDP solver or live agent swarm.

## Primary-source register

### C01 — Boyd et al., Multi-Period Trading via Convex Optimization

- URL: https://web.stanford.edu/~boyd/papers/pdf/cvx_portfolio.pdf
- Bibliography: Foundations and Trends in Optimization 3(1), 1–76, volume dated 2016; manuscript copyright 2017; DOI 10.1561/2400000023.
- Access: inspected abstract and body sections 2.7, 4.3, 5.4–5.5. Entire 79-page PDF accessible, not every page inspected.
- Supports: receding-horizon trading can optimize return, costs, risk, and holding constraints, execute only the first action, and replan. Sparse short/medium/long decision times reduce problem size. Forecast uncertainty may be represented explicitly.
- Limit: the paper expressly leaves forecasting unspecified. Its basic instantaneous trading model requires extension for order-level fills, partial executions, and latency. Convexity depends on the chosen objective and constraints.

### C02 — Hamilton, Regime-Switching Models

- URL: https://econweb.ucsd.edu/~jhamilto/palgrav1.pdf
- Bibliography: author manuscript dated May 18, 2005, prepared for Palgrave Dictionary of Economics; draws on Hamilton's original filtering work.
- Access: inspected formulation and filtering equations (5)–(12), plus discussion of smoothing and parameter identification.
- Supports: represent the unobserved regime with probabilities conditional on data available at time t. The filtering recursion differs from retrospective smoothed probabilities that use later data.
- Limit: a small Markov state model is a specification, not proof markets possess stable named regimes. Few observed transitions make transition estimates weak. Fit parameters using only data available before the forecast; filtering alone does not cure full-sample parameter leakage.

### C03 — Davis and Norman, Portfolio Selection with Transaction Costs (1990)

- URL: https://pubsonline.informs.org/doi/abs/10.1287/moor.15.4.676
- Bibliography: Mathematics of Operations Research 15(4), 676–713, DOI 10.1287/moor.15.4.676.
- Access: publisher abstract and metadata only; a faculty-hosted PDF found in search returned 404.
- Supports: with a fixed-rate bank account, lognormal-diffusion stock, proportional transaction costs and the paper's consumption/investment problem, optimal trading has a no-transaction region bounded by buying/selling boundaries.
- Limit: do not export its exact region to jumps, discrete contracts, fixed fees, unknown alpha, or arbitrary portfolios. Use the economic principle that trading costs can make inaction optimal, then derive the actual desk rule separately.

### C04 — Klenske and Hennig, Dual Control for Approximate Bayesian Reinforcement Learning (2016)

- URL: https://www.jmlr.org/papers/volume17/15-162/15-162.pdf
- Bibliography: JMLR 17(127), 1–30.
- Access: inspected introduction, approximate-controller construction, experiments 6.2–6.4, and conclusion.
- Supports: actions affect both outcomes and future knowledge; useful exploration is about parameters relevant to future decisions, and its timing matters. Their examples contrast structured exploration with indiscriminate uncertainty bonuses.
- Limit: exact Bayesian control is intractable; approximations and substantial numerical work remain. Experiments are simulated dynamical systems, not demonstrated trading profits. A desk needs explicit experiment authorization, downside and resource budgets, and relevance tests before translating the concept to order placement.

### C05 — Hansen and Sargent, Robust Control and Model Uncertainty (2001)

- URL: https://larspeterhansen.org/wp-content/uploads/2016/10/Robust-Control-and-Model-Uncertainty.pdf
- Bibliography: American Economic Review 91(2), 60–66.
- Access: inspected introduction, relative-entropy formulation, and time-consistency discussion in the seven-page article.
- Supports: an approximating model can be surrounded by statistically disciplined alternative models; uncertainty aversion is an explicit preference. Recursive constraint formulations need care about how the remaining distortion budget evolves.
- Limit: ambiguity radius and robustness preferences are not probabilities of being wrong. Reusing a date-zero uncertainty budget after each update can change the decision problem. No theorem here makes an unspecified worst-case optimizer calibrated, profitable, or dynamically consistent.

### C06 — Iyengar, Robust Dynamic Programming (2005)

- URL: https://pubsonline.informs.org/doi/abs/10.1287/moor.1040.0129
- Bibliography: Mathematics of Operations Research 30(2), 257–280.
- Access: publisher abstract and author bibliography; not a full proof audit.
- Supports: robust dynamic-programming counterparts rely on a rectangularity property of the uncertainty sets associated with state-action transitions.
- Limit: a collection of arbitrary stress scenarios is not automatically a rectangular ambiguity set. Avoid claiming a robust Bellman guarantee for a finite scenario scorer, or independently choosing a worst transition at every date when uncertainty is about one persistent latent model.

### C07 — Hay, Russell, Tolpin and Shimony, Selecting Computations: Theory and Applications (2012)

- URL: https://people.eecs.berkeley.edu/~russell/papers/uai12-meta.pdf
- Bibliography/metadata: https://proceedings.mlr.press/r10/hay12a.html; UAI 2012.
- Access: inspected metalevel formulation, Theorems 5 and 7, myopic stopping discussion, and assumptions behind computation bounds.
- Supports: computation should be selected for its expected improvement in the eventual decision, not treated as a reward-producing trade. One-step value of information can stop prematurely when several computations are jointly useful.
- Limit: bounded utility, sample assumptions, and stationarity matter for specific bounds. Live markets change during computation; add opportunity decay and deadlines explicitly. This paper establishes no universal compute-budget formula for markets.

### C08 — Gârleanu and Pedersen, Dynamic Trading with Predictable Returns and Transaction Costs

- URL: https://nbgarleanu.github.io/DynTrad.pdf
- Bibliography: Journal of Finance 2013; author manuscript March 2012. Already present as S3 in v1; do not count as a new independent source.
- Access: re-inspected author manuscript abstract, introduction, model equations (1)–(4), and proposition 2.
- Supports: with predictable returns and quadratic trading costs, optimal trading partially adjusts toward a target incorporating future expected portfolios. Predictor persistence matters for the economically useful aim.
- Limit: the closed-form control depends on specified factor dynamics, covariance, costs and preferences. Proportional-cost no-trade boundaries and this quadratic-cost partial adjustment are different model results. “React faster” is not itself an objective.

## Proposed master algorithm: a finite, auditable decision controller

The following is a DESIGN HYPOTHESIS and mathematical specification. It needs contract-specific models, implementation, replay, and evaluation. It is deliberately small enough to implement without reinforcement learning.

### 1. Maintain four kinds of state

1. **Physical state x:** holdings, cash, liabilities, open orders, fills, available margin, current limits, venue status, calendar, and timestamps. Maintain projected exposure from both current positions and orders that can still fill. A cancel request is not a confirmed cancellation.
2. **Economic state b:** predictive distribution or scenario weights over outcomes, liquidity, costs, and mechanism survival. If regimes are useful, keep probabilities, not a single label. If a fitted regime model does not beat a simple continuous state representation out of sample, remove it.
3. **Evidence state e:** source availability, data quality, model support, calibration, research evidence stage, drift monitors, and policy/model versions. Data corruption and an adverse market regime are different events.
4. **Resource state r:** capital, tail-risk headroom, liquidity, computation budget, order-rate budget, time to deadline, and remaining authorized experimental budget.

The “belief state” need not be a huge probability distribution over every market variable. Start with the smallest state needed to rank approved actions and evaluate constraints. Compression is acceptable if relevant lost information is measured. Prefer an interpretable low-dimensional distribution over a confident but brittle regime name.

### 2. Distinguish three forms of change

- **State response:** an already approved policy changes its position because current observations changed. No new strategy is invented.
- **Parameter update:** a predeclared update rule changes posterior weights, calibration, or a bounded parameter. Its update cadence, forgetting, bounds, fallback, and stopping conditions are part of the frozen policy and must be tested as such.
- **Policy promotion:** new features, actions, optimization objectives, model families, constraints, universes, or update rules create a new policy version. Run the evidence loop; do not label this routine adaptation.

A daily best-backtest selector is itself a complex trading policy. Evaluate its selection history using only information available at each date. Do not splice hindsight winners.

### 3. Build an approved finite action set

For each sleeve, enumerate practical alternatives at the native decision clock: retain the current approved plan; cancel/replace eligible working orders; reduce; exit; hedge; enter/add at approved sizes and routes; defer to a specified next event. The “retain plan” baseline includes its existing exits and risk handling, not an assumption that the existing position is frozen forever. “Flat” and “no new orders” are not equivalent.

A modest candidate lattice is often sufficient: a few sizes, order styles, and horizons. Consolidate mutually inconsistent orders across sleeves before evaluation. Include the total desk book in every candidate's outcomes. Remove infeasible candidates first; never make a risk limit just another soft score the optimizer can pay to violate.

For delayed candidates, define when and under what information the next action happens. Waiting until a new observation arrives is a conditional policy, not a trade at today's unchanged quote after a delay.

### 4. Score complete net outcomes in one common unit

Let a denote a candidate policy or short conditional plan, a0 the current approved baseline, and omega a joint future path. Let W_T(a,omega) be terminal desk wealth after actual cash flows, trading costs, funding, borrow, settlement, taxes if in scope, and the declared terminal valuation or liquidation convention. Intermediate constraints must be checked along the path, not just at T.

Choose one preference formulation explicitly. A general robust incremental-utility form is:

    J_t(a) = inf_{P in U_t} E_P[ u(W_T(a)) - u(W_T(a0)) | I_t ]
    a* = argmax_{a in A_feasible} J_t(a)

Here U_t is either a singleton posterior-predictive distribution or an explicitly documented ambiguity set. u may be linear for expected net wealth with separate risk constraints, or a chosen concave utility reflecting the mandate. Compare wealth on identical market paths where possible. If u is log, wealth must stay strictly positive under modeled paths; log utility does not replace margin constraints.

Do not automatically add an “uncertainty penalty” to a worst-case expectation already addressing that same uncertainty. Do not subtract trading costs again when W_T already includes them. Do not add CVaR, variance, and arbitrary drawdown penalties together without stating which preferences or constraints each represents. A risk-adjusted score has units; a number of dollars, a probability, and a Sharpe ratio cannot be summed unscaled.

There are two different conservative comparisons: min_P E_P[U(a)-U(a0)] and min_P E_P[U(a)] - min_P E_P[U(a0)]. They are not generally equal. The first requires improvement under each shared model in U; the second compares separately pessimistic levels and can favor an action without robust pairwise dominance. Choose deliberately. The proposed incremental test uses the first; it may sacrifice upside for conservatism.

A desk-wide expected-wealth formulation may instead optimize expected net P&L subject to stress, leverage, margin, and concentration constraints. If shadow prices allocate scarce resources, estimate them from that resource allocation problem or a declared policy. A capital charge and a financing cost are distinct only when they price distinct burdens. Do not deduct a shadow price for a constraint and then claim it is an additional realized cash loss.

For arbitrary nonlinear portfolios and execution, finite scenarios are a model approximation. A worst result across K selected scenarios is a scenario stress score, not a proven lower bound on all market outcomes. A confidence bound is a statistical object, not simply a pessimistic scenario.

### 5. Use a no-change region and asymmetrical urgency

Change the ordinary trading plan only when its improvement clears implementation cost already modeled in outcomes plus any separate, predeclared hysteresis threshold. The threshold must reflect estimation, switching, or operational stability concerns and be validated. Do not call an arbitrary threshold statistically significant.

A simple independent derivation explains the economics. For one asset, choose next holding h near current h0 to maximize

    f(h) = mu*h - (gamma/2)*sigma^2*h^2 - k*abs(h-h0).

With gamma>0, sigma^2>0, proportional cost k>=0, and no other constraints, h0 is optimal exactly when

    abs(mu - gamma*sigma^2*h0) <= k.

At h0, the marginal benefit lies inside the transaction-cost subgradient. Outside, trade toward the relevant boundary, not necessarily the frictionless target mu/(gamma*sigma^2). This is a one-period illustrative derivation, not the Davis–Norman continuous-time theorem. Fixed fees, nonlinear impact, asymmetric costs, discrete sizes, and funding alter the region.

Use different policies for ordinary switching and danger: a hard limit, corrupted required feed, or infeasible projected exposure triggers the approved emergency procedure immediately. Do not let a dwell timer delay necessary risk reduction. Conversely, resuming risk after a fault requires reconciliation and defined recovery evidence. This asymmetry improves stability without making the system slow to genuine danger.

### 6. Allocate computation to unresolved decisions

Maintain action-value estimates and error descriptions. When comparable values satisfy certified numerical or statistical bounds Q(a) in [L(a), U(a)], and L(a*) exceeds every rival's U(a), more precision is unnecessary for the present ranking under those bounds. The guarantee concerns the modeled value and stated bounds; model misspecification remains.

A useful deterministic derivation: if all value estimates have absolute error <=epsilon, and the estimated top-to-runner-up gap exceeds 2epsilon, the top action is unchanged by any such errors. Epsilon must be a valid error bound, not the standard deviation of P&L or an invented confidence score. Correlated value errors may permit tighter paired bounds.

Before each expensive computation c, estimate its chance of changing a consequential action and the value of the corrected action. A heuristic prioritization is

    expected decision improvement - computation cost - delay/opportunity loss.

Its inputs require measurement. A quoted expected improvement is a hypothesis until validated. Batch complementary computations where one-step VOI would stop too early. Never consume the execution deadline estimating an exact VOI that costs more than the decision.

Keep the fast path deterministic: fresh required inputs, small candidate set, cached exposures, candidate scores, hard checks, order intent, journal. The slow path can research, refit, stress, and propose. Use incremental feature updates and recompute only affected candidates. Cache only with explicit version and freshness keys. A timeout returns a predeclared feasible fallback; it must not submit a half-checked stale intent. Measure p50/p95/p99 end-to-end latency and deadline misses against signal lifetime, not merely model inference speed.

### 7. Treat learning as a scarce intervention

Separate observational learning from actions intended to learn. Record eligible but rejected opportunities, predicted fills, subsequent quotes, and outcomes where observable. This can reveal missed value without spending capital, although simulated fills are not actual fills.

An experiment that deliberately changes routes, sizing, timing, or inventory can alter both data and risk. Require a declared experiment, assignment/logging, objective, maximum loss/exposure, time budget, and abort rule within the existing authorization. Do not add a generic uncertainty reward to the live trade score. A high-uncertainty arm may be uninformative for future profitable decisions or dangerous to sample.

For the default desk design, keep exploratory alternatives in shadow and make promotion a separate evidence decision. Full dual control is optional only when the effects of experiments on future information are modeled well enough, economically important, and worth the operational complexity.

### 8. Replan only when material facts change

Events include approved clock ticks, fills, cancellations, material new public evidence, quote/volatility changes beyond the configured relevance threshold, approaching deadline, margin changes, and data-quality transitions. Each event carries availability time, identity, and version. Deduplicate and order them consistently.

Optional MPC plans a short horizon but executes only its first decision and then re-evaluates. Use sparse economic decision points where appropriate, not an enormous homogeneous grid. Forecasts farther out often become less useful; they may be represented by coarse scenarios or terminal conditions. Increasing horizon is justified only when it changes actions enough to beat its forecast and computation errors.

Do not present a finite candidate controller as optimal POMDP control. Do not present independently worst-case future transitions as a calibrated persistent-model belief. If full robust DP is used, specify uncertainty structure and time-consistency assumptions; otherwise accurately label the design receding-horizon scenario optimization.

## Suggested core pseudocode

    on eligible_event(event):
        update_deduplicated_asof_state(event)
        reconcile_fills_orders_positions()
        if hard_fault_or_limit_breach():
            execute_approved_risk_procedure(); journal(); return
        if not approved_decision_time_or_material_trigger(): return
        freeze_snapshot_and_versions()
        baseline = current_approved_plan()
        candidates = generate_approved_candidates(baseline)
        candidates = exclude_infeasible_projected_paths(candidates)
        beliefs = update_using_predeclared_rule(snapshot)
        score_complete_net_desk_outcomes(candidates, beliefs)
        refine_only_if_decision_relevant_and_before_deadline()
        choose_best_supported_candidate_or_baseline()
        apply_ordinary_hysteresis_without_blocking_hard_risk_action()
        revalidate_freshness_exposure_and_order_state_before_submit()
        persist_idempotent_intent_then_execute_if_authorized()
        journal_all_candidates_estimates_rejections_and_versions()

    on slow_evidence_cycle():
        diagnose_data_forecast_execution_risk_and_mechanism_separately()
        evaluate_whole_adaptive_policy_against_frozen_baseline()
        propose_one_binding_bottleneck_change()
        replay_with_point_in_time_inputs_and_full_costs()
        perform_registered_out_of_sample_and_forward_checks()
        promote_new_version_only_through_existing_gates()

## Decisive validation cases

1. Regime filter uses only t data but full-sample parameters: detect leakage; redo walk-forward fitting.
2. Three sleeves individually pass limits but simultaneous pending fills breach desk exposure: reject combined intent.
3. Current position is profitable to hold, new entry is not: choose retain; do not confuse no-new-risk with liquidation.
4. Marginal forecast fluctuates around a trade boundary: compare net turnover and delayed response under prospective hysteresis.
5. Hard risk breach occurs during minimum dwell: emergency rule takes precedence.
6. One candidate dominates across valid numerical bounds: stop optional compute, retain model-risk caveat.
7. Small uncertainty individually but jointly correlated model failures: paired desk scenario loss should expose concentration.
8. Cost in W_T plus separate cost subtraction: fail accounting check.
9. Robust pairwise comparison and difference of robust levels disagree: use declared objective, report choice.
10. Better strategy score arrived after its deadline: discard the intent and use feasible fallback; latency belongs in the comparison.
11. Route experiment changes data distribution: evaluate the full adaptive selection process, not only lucky chosen trades.
12. No supported eligible opportunities today: no new exposure is a valid optimum; measure readiness and opportunity coverage separately from activity.

## Strongest synthesis

A desk becomes more perceptive when it knows which uncertainty can change its next feasible decision; more agile when it updates that state cheaply and acts before economic value decays; more adaptive when the update rule is itself evaluated; and more intelligent when it spends risk and computation only where they have decision value. These are measurable design properties. They are not a promise that any strategy can be transformed into an economically profitable one.
