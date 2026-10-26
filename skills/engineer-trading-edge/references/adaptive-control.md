# Adaptive control: the master algorithm

## Contents

1. Objective and limits
2. State, beliefs, and five budgets
3. Feasible actions and portfolio value
4. Decision boundaries and the value of computation
5. Receding-horizon planning and restrained adaptation
6. Master procedure
7. Research opportunities and falsification
8. Minimal implementation and measurement

This addendum extends the economic and validation workflow. Its controller is an **engineering synthesis**, not a theorem that creates positive returns. Source IDs C, E, L, O, and X refer to `adaptive-sources.md`; earlier IDs retain their original meanings. Read `adaptive-learning.md` for inference and `desk-runtime.md` for execution. Use only the layers needed for the actual problem.

## 1. Objective and limits

Optimize a feasible decision using current evidence, executable payoffs, existing inventory, scarce resources, and the cost of changing course. Preserve the edge contract: identify what earns compensation before optimizing how to capture it. A control system cannot supply an absent economic advantage.

**Elementary no-universal-edge result.** In a finite-horizon model, let discounted price S be a martingale under the actual probability measure P and the desk's full information. For a predictable integrable strategy h with admissible gains, E[sum h_t (S_(t+1)-S_t)]=0. Deduct nonnegative trading costs and expected net gains are nonpositive. Faster computation, dynamic allocation, and adaptive indicators cannot overturn those assumptions. An equivalent martingale measure used in no-arbitrage pricing is different: it need not be P and does not imply zero physical expected risk premia. This example disproves a universal-profit promise; it does not assert that actual markets satisfy the example.

Use two objectives distinctly:

- **Policy objective:** maximize the desk's stated net portfolio utility subject to constraints. It can favor a hedge with negative standalone expected P&L.
- **Change criterion:** require a proposed intervention to earn its complexity, switching costs, and uncertainty relative to a frozen feasible incumbent.

Improve daily *opportunity coverage*: inspect more feasible, economically distinct opportunities before their deadlines. Do not target a daily trade quota, activity, or a guaranteed positive day. Include doing nothing, retaining a position, reducing it, and buying information as distinct decisions. Abstention from a new order is not liquidation.

## 2. State, beliefs, and five budgets

Maintain a decision snapshot with these components:

| Component | Required contents |
|---|---|
| Information | As-of observations, source lineage, revisions, feature availability, quote age, missingness, uncertainty in clock offsets |
| Market belief | Conditional payoff/fill/cost distributions; latent-state probabilities; model alternatives; coverage gaps |
| Own state | Reconciled positions, cash, liabilities, pending orders, reservations, possible fills, collateral by venue |
| Policy state | Immutable policy/model/config IDs, approved actions, evidence stage, incumbents, elapsed holds and deadlines |
| Learning state | Matured outcomes, pending labels, trial ledger, estimands, test budgets, deployment history |
| Resources | Risk and funding headroom, executable capacity, compute budget, information acquisition budget, remaining opportunity time |

Spend five separate budgets: capital/loss capacity, liquidity/market impact, time/compute, information acquisition, and statistical false-decision tolerance. Money is not interchangeable with statistical error probability. Express monetary comparisons in a common currency/horizon; keep hard limits separate from utility penalties.

Model a latent state z using a **filtered** belief b_t(z)=P(z_t=z | information actually available at t). In a specified state-space model, update via predictive transition followed by the new observation's likelihood. For example:

\[
b_t(z)\propto p(y_t\mid z,a_{t-1})\sum_{z'}p(z\mid z',a_{t-1})b_{t-1}(z').
\]

Include actions in transitions or observation models when they affect impact, inventory, fills, or future opportunity. The equation specifies a model; it does not make its likelihoods known. Check predictive calibration, sensitivity to state definitions, and a simpler nonregime baseline. Fit state definitions, transition parameters and every preprocessing step only on data then available; causal filtering with full-sample fitted parameters still leaks. Do not use future-smoothed states, retrospectively named regimes, or hard classification confidence as historical live knowledge [C02].

Prefer uncertainty over *action value* to uncertainty over narrative labels. Two plausible market explanations may recommend the same small trade; one confident regime label may still leave execution value unresolved. Distinguish:

- outcome randomness, which may be paid risk;
- parameter/model uncertainty, requiring sensitivity or a defensible ambiguity set;
- data/clock uncertainty, invalidating some inputs;
- own-state uncertainty, requiring reconciliation or set-valued risk checks;
- identification failure, where observed data cannot answer the counterfactual at all.

Do not compress these into one model-confidence number. A Bayesian credible interval, sampling confidence bound, stress scenario, and ambiguity set have different meanings.

## 3. Feasible actions and portfolio value

Construct a small approved menu: continue the incumbent; skip a new entry; change size within approved bounds; select execution mode; reduce or hedge existing risk; request a useful observation; or invoke a contingency. The menu must respect existing entry-clock authority. Candidate generation cannot silently authorize new instruments or live exploration.

For each candidate policy pi, model complete net portfolio wealth paths W(pi), including open-order outcomes, fees, spreads, impact, financing, collateral, holding/exit costs, and instrument semantics. Compare identical initial wealth, calendar, and external scenarios. Represent each material cash cost once. If a conditional fill payoff already includes adverse selection, do not subtract a second adverse-selection penalty.

An illustrative robust planning objective is:

\[
J_t(\pi)=\inf_{P\in\mathcal P_t}E_P[U(W_{t+H}^{\pi})\mid\mathcal I_t].
\]

Choose U and the feasible path set from the mandate, with explicit interim capital, liquidity, concentration, turnover, and operational constraints. If using expected P&L minus a separate risk penalty, specify that as an alternative objective with consistent units. Do not add unexplained variance, entropy, Sharpe, confidence, and dollars. Include terminal liquidation or residual inventory value so a short planning horizon cannot hide costs beyond its endpoint. No modeled scenario set guarantees protection against all real-world losses [C01, C05].

For a **conservative improvement gate** against feasible incumbent pi0, evaluate the same-model paired difference:

\[
G_t(\pi;\pi_0)=\inf_{P\in\mathcal P_t}E_P[U(W^{\pi})-U(W^{\pi_0})\mid\mathcal I_t].
\]

Select an action only when G exceeds a declared hurdle and all evidence, timing, and feasibility gates pass. The hurdle covers a required economic margin or additional policy-change friction **not already charged** in W. It is not an arbitrary number claimed to be learned. Statistical uncertainty can define a justified set or a separate evidence gate; distinguish that from economically adverse outcomes.

Do not substitute min_P E[U(W^pi)] minus min_P E[U(W^pi0)]. Their worst cases can differ. **Checked illustration:** with two scenarios, candidate utilities (5,1), incumbent (0,4), and ambiguity allowing either scenario with certainty, separate minima give +1, while the paired robust difference is min(5,-3)=-3. The candidate improves worst-case *levels* but does not dominate the incumbent across models. Both objectives can be legitimate; name which was selected. The paired gate is deliberately conservative and may reject useful risk redistribution. It is not universal optimality.

Treat the entire desk jointly. Two acceptable sleeve additions may violate a common funding or tail limit when combined. Reserve resources atomically before submission. If proposing marginal allocations, recompute shared constraints after each accepted action, or solve a joint batch. Opposing uncertain orders cannot be assumed to cancel each other before fills.

Use capital shadow prices only when the underlying optimization supports them. For differentiable concave net value g_i(q_i) and shared linear resource limits A q <= b, an interior optimum satisfies marginal benefit g_i'(q_i)=(A^T lambda)_i. The multipliers price scarce resources **locally within that model**. With nonconvex lots, discontinuities, nonlinear margin, or uncertain liquidity, use finite perturbations and explicit feasible comparisons instead of false precision. Capacity changes the opportunity, not only position size [E04, E05].

## 4. Decision boundaries and the value of computation

Prioritize research where uncertainty could change the best feasible action before its deadline. High entropy about an irrelevant fact deserves no extra work; a narrow uncertainty interval around break-even may deserve immediate attention. This is a decision-theoretic principle, not permission to invent an information-value estimate.

For an optional computation or observation c taking time tau, estimate:

\[
VOC(c)=E[V_{t+\tau}^{after\ c}]-V_t^{act\ now}-K_c.
\]

Use the same terminal date and continuation rights: acting now may still allow learning later. Both values include attainable execution, market evolution during delay, and comparable portfolio utility. K_c must be in matching utility units; for nonlinear U, put monetary compute/acquisition costs inside wealth or justify the conversion instead of subtracting raw dollars. Do not charge delay loss again if it is already inside the future value. Evaluate against *acting now*, not only against waiting without computing. Estimate routing benefits from earlier cases, then test the complete routing policy prospectively [O04, C07].

Use an anytime pipeline: compute the cheapest admissible baseline; retain its feasible action; refine only while conservative estimated decision improvement exceeds cost and a worst-case completion time fits the deadline. Stop early when defensible action-value bounds establish the same choice across relevant uncertainty, or no affordable computation can change the action. Heuristic intervals are not mathematical certificates. A negative one-step VOC does not rule out valuable complementary computations; evaluate a small affordable bundle menu when warranted. Bound the controller's own analysis cost: recursively debating computation can consume the entire opportunity.

**Hypothetical arithmetic:** candidate A has scenario incremental utilities (8,-3), and probability of scenario 1 lies in [0.45,0.60]. Worst mean improvement is 1.95. If the uncharged change hurdle is 2, keep the incumbent. Candidate B has (4,1), giving worst mean 2.35; if feasible, it passes that illustrative gate. This favors robustness of the decision, not the most vivid forecast. No market measurements are implied.

Forecast scoring remains necessary even with decision-focused training. Training only against trading P&L can learn simulator quirks, omit untraded observations, or hide miscalibration. Compare proper forecast scores, decision regret on a defined feasible problem, and realized net-policy utility separately [E01].

## 5. Receding-horizon planning and restrained adaptation

Use three clocks:

1. **Execution clock:** validate data and own state, select among approved actions, reserve resources, submit and reconcile. Honor a hard deadline.
2. **Belief clock:** update forecasts, costs, fill models, and filtered state within a frozen, tested update rule. Trigger only on materially new information or prescribed reviews.
3. **Policy clock:** propose a new rule, state representation, model family, adaptation rate, or action universe; replay and validate it before promotion.

An approved policy may adapt every event. That does not authorize rewriting it after every loss. A rollback, learning window change, reset, or new ensemble weight rule is itself a consequential research choice. Keep adaptation within explicit bounded envelopes; changes outside them become new versions.

When inventory or costs couple decisions over time, plan over H steps but execute only the first action, then replan from reconciled state. Keep horizon, terminal inventory treatment, uncertainty model, and fallback fixed during evaluation. Scenario-tree decisions cannot use future branch identities before those observations arrive. A deterministic open-loop plan is an approximation, not full contingent control [C01].

Avoid unnecessary churn. Let transaction costs, uncertainty, and existing positions create a no-trade region. For the one-asset objective F(x+delta)-k*abs(delta) with differentiable concave F and no other constraints, zero change is optimal when abs(F'(x))<=k; constraints alter the condition. Quadratic costs often imply gradual adjustment rather than an exact no-trade band. A cooldown or separate entry/exit hurdle is a policy choice to test, not a substitute for the actual cost model [C03; earlier S3].

Use robust dynamic programming only with its required ambiguity assumptions. In particular, stagewise adversarial choices can create impossible combinations when uncertainty is coupled across time. Rectangularity supports specific recursive formulations; otherwise retain coherent path/model uncertainty and avoid claiming a Bellman optimality guarantee [C06].

Recognize dual control: an action can earn payoff and reveal information. Passive paper observation is preferable when it answers the question, but it cannot reveal actual queue fills or market impact. Any live experiment must be separately within user authorization and mandate, have bounded capital and a prespecified design, and account for future-state effects. No information bonus overrides hard risk limits. Approximate dual-control theory is not an unrestricted reinforcement-learning license [C04].

## 6. Master procedure

Apply the following procedure to a desk, strategy, or sleeve. Unknown quantities become explicit research dependencies; do not hallucinate inputs to complete the algorithm.

```text
CONFIGURE once per approved version:
  freeze economic contracts, incumbent, objective and benchmark
  define instruments, action menu, timing authority and budgets
  define as-of data rules, update rules, scenarios and hard limits
  define evidence gates, deadlines, fallback and contingency policies
  define learning estimands, label maturity and error spending

ON an eligible information, market, timer, or own-state event:
  1 ingest/deduplicate; retain publication and receipt history
  2 reconcile own state; update all possible open-order exposures
  3 if hard integrity/risk conditions fail:
      block alpha expansion; invoke approved specific contingency
      persist cause; RETURN from alpha path or enter risk-only mode
      do not infer flat positions or blind-liquidate
  4 update filtered beliefs using only presently available evidence
  5 build a small feasible, approved menu including the incumbent
  6 compute cheap fill-aware, portfolio-aware net action values
  7 remove unsupported, stale, expired or infeasible candidates
  8 refine only where estimated value of computation justifies delay
  9 compare paired improvement, uncertainty, hurdle and constraints
 10 if a candidate passes, atomically revalidate current dependencies,
    policy, own state and limits; reserve resources and log intent
    on version conflict recompute; never commit the stale decision
    else retain feasible incumbent and record why no change passed
 11 execute through deterministic lifecycle; recheck expiry and all
    required pre-send validity conditions at the submission boundary
 12 reconcile fills/cancels; update reservations from actual events
 13 append decision, alternatives, information and policy versions

ON an outcome-maturity or learning event:
  14 score forecasts and all eligible decisions; track censored labels
  15 update prespecified evidence monitors with valid information set
  16 attribute changes to forecasts, capture, costs, risk or mechanism
  17 route to continue/reduce/pause/investigate/retire per approved rules
  18 create a new challenger only for an identified, testable bottleneck
  19 evaluate the entire adaptive policy against frozen alternatives
  20 promote only to the next authorized evidence stage; retain rollback
```

If the incumbent is infeasible, the alpha comparison is no longer the decision. Invoke the appropriate risk/operational contingency. Risk reduction may rationally have negative expected profit. Maintain separate emergency authority, available reliable data, and execution limits.

## 7. Research opportunities and falsification

These are proposed combinations, not verified new discoveries or proven trades:

| Hypothesis | Minimal discriminating experiment | Failure criterion |
|---|---|---|
| Spend analysis on decision-boundary cases | Compare cheap, always-deep, and budgeted refinement on identical as-of events | Added utility fails to cover compute and latency |
| Separate information decay from capture decay | Hold forecast fixed; compare execution modes and delayed entries | Improvement vanishes with attainable fills and costs |
| Allocate by shared capital scarcity | Replay joint portfolio with endogenous reservations versus independent sleeve caps | Gain disappears under common stress and collateral constraints |
| Preserve liquidity for later opportunities | Compare full deployment with a trained reserve rule on the actual future opportunity stream | Gain depends on future knowledge or assumed unlimited reinvestment |
| Adapt to observable mechanisms, not outcome labels | Compare frozen, calendar-refit, and evidence-triggered policies | Detection delay, false alarms and switching erase benefit |
| Use simpler actions when uncertainty is irrelevant | Compare action-gap routing with entropy-only routing | No budget-matched benefit or fragile threshold dependence |

Waiting has option value when commitment is costly or irreversible and useful learning/opportunities may arrive. It also has decay and missed-fill cost; a positive waiting value in one investment model is not a universal reason to delay trades [E06].

Test transfer across environments only after defining environments independently of favorable outcomes. Stable relations can still be confounded; causal invariance results require structural assumptions, including restrictions on interventions affecting the target [X01]. Treat invariance tests as falsification tools unless identification assumptions are justified. Competition can change the target relation itself.

Trading can alter its own training distribution through impact, information leakage, inventory and opponent reaction. Distinguish external market drift from policy-induced change; log policy versions and sizes as state. Stable repeated retraining is not necessarily the best deployed policy, and may converge poorly or fail under violated assumptions [E02, E03].

## 8. Minimal implementation and measurement

Start with one event log, one deterministic state reducer, one small candidate scorer, one portfolio-risk/reservation authority, one order manager, and one replay/evaluation worker. Use a modular process before introducing distributed services. Cache shared features with version and availability keys; invalidate dependencies when their facts change. Add richer latent-state models, solvers, or parallelism only after a measured bottleneck justifies them.

The bundled `scripts/adaptive_arbiter.py` is an offline finite-menu reference kernel for the paired robust gate and scenario constraints. It consumes supplied utilities, beliefs and load scenarios; it neither estimates them nor submits orders. Its tests validate specified control invariants using synthetic inputs. Read its module contract before using it. It is not the whole master procedure, a certified risk engine, or empirical proof of edge.

Measure improvement on a declared baseline:

| Requested quality | Operational measurement |
|---|---|
| Intelligence and accuracy | Proper forecast scores, decision errors near thresholds, net portfolio utility with uncertainty |
| Awareness | Data/clock lineage coverage, unresolved-state age, reconciliation mismatches detected before action |
| Responsiveness | Event-to-valid-decision latency and change-detection delay at a fixed false-alarm budget |
| Speed and bandwidth | Tail latency, deadline misses, feasible opportunities evaluated per unit compute, capacity after cost |
| Precision | Calibration in action-relevant bins, fill-conditioned markouts, reservation and settlement correctness |
| Dynamism | Held-out utility of the entire adaptive policy after turnover, false alarms, retraining and switching |
| Efficiency | Net value per bounded resource plus total value; avoid maximizing ratios that sacrifice useful scale |
| Edge | After-cost expected advantage over the stated benchmark and constraints, with evidence stage |

Report percentage or multiple improvements only for measured metrics with numerator, denominator, workload and uncertainty. A faster synthetic function is not a more profitable strategy. A broad research procedure can improve the quality of any assessment; some assessments should end with repair, replacement, or no trade.
