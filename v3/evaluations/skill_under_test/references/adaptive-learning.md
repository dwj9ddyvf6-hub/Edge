# Adaptive learning: evidence that survives the feedback loop

## Contents

1. Evidence contracts and feedback types
2. Counterfactual support
3. Sequential evidence and its information clock
4. Drift, delayed feedback, and retirement
5. Experiments and acceptance gates

Use with `adaptive-control.md`. The following is a research and engineering synthesis. L-series citations refer to `adaptive-sources.md`. Statistical validity depends on the stated data-generating assumptions; it is not guaranteed by naming an estimator.

## 1. Evidence contracts and feedback types

Before learning, specify **what quantity is identifiable** from the available observations. A strategy may forecast a common outcome for every candidate, yet reveal executions only for submitted orders. One-step routing rewards and full inventory trajectories are different targets.

Every evidence object must carry:

```text
policy/version and candidate family
estimand, units, economic hurdle, null and alternative
eligible population, opportunity-generation rule and benchmark
decision, publication, receipt, observation and outcome-maturity times
information available to detector AND to stopping/routing controller
conditional dependence/tail assumptions and support requirements
estimator, nuisance fitting, tuning and missingness rules
false-decision budget, repeated looks, resets and multiplicity plan
maximum sample/horizon if applicable; detectable economic change
permitted consequence: investigate / reduce / promote / retire
```

Reject confidence claims without this contract. Do not combine a Bayesian posterior, an ambiguity-set minimum, a fixed-time confidence interval and a stress percentile into one confidence score. A drift detector is an alert for a specified change, not a diagnosis of its economic cause.

Keep production, challenger and evidence registries distinct. Production includes a frozen adaptive update rule and its tested ranges. Challenger versions are immutable. Each evidence contract belongs to a specific estimand/version and records every outcome inspected. Changing a reward, target policy, learning rate, reset rule or horizon is a research choice that may require a new evaluation.

## 2. Counterfactual support

Distinguish these feedback regimes:

| Data available | Permitted comparison | Missing counterfactual |
|---|---|---|
| Common resolved event with negligible own influence | Preissued forecasts against the same outcome | Alternative execution price and fill |
| Supported randomized route with known selection probabilities | One-step policy reward under identification assumptions | Unsupported actions; changed future inventory state |
| Quote/order-book replay | Policy performance in the specified simulator | True queue priority, impact, response to unplaced orders |
| Stateful portfolio actions | Trajectory value under an identified transition model or suitable experiment | Alternative trajectories from one-step weights alone |

For discrete actions, let b_t(a|x) be the actual logging probability and pi(a|x) the target probability. Require pi(a|x)>0 only where b_t(a|x)>0 for relevant contexts, plus the causal/consistency assumptions of the evaluation. Known propensities do not fix unobserved confounding or action-induced future-state change [L03, L08].

A standard doubly robust pseudo-outcome is:

\[
\psi_t(\pi)=\sum_a\pi(a\mid x_t)\widehat m_t(x_t,a)+\frac{\pi(a_t\mid x_t)}{b_t(a_t\mid x_t)}[r_t-\widehat m_t(x_t,a_t)].
\]

Fit reward models on earlier data or use a dependence-valid honest evaluation design. The robustness concerns particular nuisance-model errors under the model; it cannot recover an action with zero support. Examine overlap, extreme weights and sensitivity. Weight clipping changes bias; an effective-sample-size diagnostic is not a validity certificate. Do not reconstruct propensities from observed frequencies when the actual assignment mechanism was deterministic or different [L04].

Log context, feasible menu, action, actual propensity, randomization ID where applicable, own-state snapshot, policy version, reward definition, maturity, costs, and observed/simulated provenance. Preserve rejected opportunities, including no trades and nonfills. A deterministic log choosing passive only in quiet markets and aggressive only in volatile markets does not identify their comparison in either market through importance weighting. A model can extrapolate, but must report its additional assumptions.

Specify three portfolio counterfactuals separately:

- Freeze other sleeves and add/change the candidate: marginal contribution under fixed peers.
- Reoptimize peers under the same shared limits: replacement value plus reallocation effects.
- Change execution/size enough to alter prices or future state: deployment-dependent value requiring impact/transition assumptions.

Do not sum standalone sleeve improvements when nonlinear risk, competition for capital, or impact makes them nonadditive. Common shocks used for paired simulation improve comparability only when the action-dependent simulator defines both paths coherently.

Choose the least costly identifiable experiment. Shadow observation is useful for data, timing and forecast checks; it is not proof of hypothetical fills. A randomized real-money experiment requires explicit authorization and bounded risk/exposure, design, assignment and abort rules. Research permission alone does not supply it.

## 3. Sequential evidence and its information clock

Fixed-time tests generally cannot be repeatedly checked at nominal significance without an appropriate sequential or multiplicity design. Confidence sequences and e-processes provide tools under explicit conditional assumptions [L01, L02]. Record the target: constant mean, cumulative average conditional value, recent-window mean, or change since an epoch. A lower bound for average value since inception does **not** establish present or future edge after deterioration.

**Elementary derivation, deliberately limited.** Let resolved increments satisfy -1<=X_t<=1 and test the strong null E[X_t|F_(t-1)]<=0 for every t, where F is the full information used to select observations and stopping decisions. Choose lambda_t in [0,1) measurably before X_t. Define:

\[
E_0=1,\qquad E_t=\prod_{i=1}^t(1+\lambda_i X_i).
\]

The factors are nonnegative and conditional expectation cannot increase E_t under the null. Thus it is a nonnegative test supermartingale, and the chance it ever reaches 1/alpha under that null is at most alpha. Use log1p for stable computation. This derivation is an illustrative specialization, not the recommended universal trading test.

Crossing rejects the claim that conditional improvement was never positive over the tested sequence. It does not test an arbitrary average-mean null, prove the current mean is positive, or produce a posterior probability of future profit. For an intended cumulative-average or time-varying target, use a construction valid for that target [L03]. If D_t is a net improvement and h a hurdle, X_t=(D_t-h)/B requires a defensible bound abs(D_t-h)<=B; a historical maximum or stop order does not establish it. Clipping creates a different estimand and can conceal tail loss. For unbounded P&L, use justified conditional-tail assumptions or a method designed for them; do not fake boundedness.

Information timing is part of validity. An e-process justified when the observer sees a coarse history may be invalid when a richer-history controller decides when to stop. Delayed multi-horizon forecasts, partial outcomes and intraday prices can enlarge the actual information set. Validity must hold in that full decision filtration, or a justified adjustment is required. Fixed weighted averages can combine valid e-processes for the same null in the same filtration; arbitrary products, hindsight-selected weights, and different filtrations need additional justification [L09].

Allocate error across monitors and epochs prospectively. For detector weights w_j>=0 with sum_j w_j<=1 and restart epoch r=1,2,..., one transparent allocation is alpha_(j,r)=alpha_total*w_j/[r(r+1)]. The total is at most alpha_total, so a union bound controls the family of individually valid false rejections without requiring independence. This is conservative accounting, not an optimal allocation. It does not repair invalid individual tests or retrospective epoch selection. A reset after failure does not erase the failed history.

The best among many ordinary pointwise lower bounds is not automatically a valid bound for the selected candidate. Use simultaneous/selection-aware inference or independent confirmation. Anytime validity for one stream does not eliminate strategy-search bias, multiple detectors, or model misspecification.

## 4. Drift, delayed feedback, and retirement

Attach outcomes to the original decision version. Maintain pending labels with planned horizon, resolution rule, censoring reason, and informative-delay flags. Never treat unresolved outcomes as zero or score only quick winners. A position's closing time and its evaluation horizon may differ. Compare mature cohorts under the frozen definition, including appropriate mark-to-market outcomes and separately accounted pending risk. Delayed-feedback results require their own assumptions; trade duration is often action- and outcome-dependent [L07].

Overlapping outcomes are not independent updates. Numbering trades by settlement time does not establish a conditional-mean null. Use a defensible delayed-observation method or prespecified evaluation blocks with suitable dependence/tail assumptions. Retain partial information available to the controller in the evidence contract. Fewer, honestly identified opportunities can be more informative than thousands of overlapping timestamps.

Route alerts by the layer that failed:

| Signal | First diagnostic | Candidate response |
|---|---|---|
| Missing sequence, stale quote, unknown inventory | Operational integrity | Disable affected expansion; reconcile immediately |
| Inputs change but conditional forecast scores hold | Opportunity mix/support | Review coverage and supported reweighting |
| Mature comparable forecasts deteriorate | Forecast/model stability | Examine calibration, feature lineage and challenger |
| Forecast stable, filled markouts worsen | Execution/capture | Inspect queue, latency, spread, size and selection |
| Gross payoff stable, shared stress rises | Compensation/portfolio suitability | Reprice capital, scenario risk and size |
| Completed outcomes improve as pending losses grow | Maturity selection | Repair evaluation before attributing edge |
| Size/routing changes precede changed outcomes | Policy feedback | Compare deployment cohorts and impact hypotheses |

Operational intervention need not wait for statistical significance. An evidence alert usually calls for investigation or a prespecified reduction, not an automatic new strategy. The counterfactual cost of false alarms, delayed detection, missing opportunities, and switching belongs in the whole-policy evaluation.

Forgetting has a cost. Short windows adapt quickly but discard evidence; long windows gain precision but react slowly. Nonstationary-bandit theory makes this dependence on variation explicit, under its setting. Regret against the best available arm is relative: all arms can lose money, and arbitrary rapid change can defeat tracking [L06]. Preserve cash and a feasible incumbent benchmark. A conservative-bandit bound on cumulative expected reward is not a realized-loss, margin, or drawdown guarantee. Signed trading rewards also do not inherit a nonnegative-reward multiplicative baseline constraint unchanged [L05].

Treat recent-window length, reset threshold, ensemble weights and learning rates as parameters of the evaluated policy. No universal setting is best for every market. Prefer a small preregistered family and mechanism-grounded shifts to a large daily winner search. Evidence of no useful benefit can justify retirement; insufficient precision is a separate conclusion.

## 5. Experiments and acceptance gates

Compare at least the frozen baseline, a simple periodic-refit baseline, and the proposed adaptive policy, replaying every forecast, update, reset, resource reservation and switch chronologically. Charge data, computation, latency, missed fills, turnover, funding and maintenance where relevant. Preserve the original opportunity population and common evaluation horizon.

Test these failure cases before trusting an adaptive claim:

- Zero-propensity target actions, simulator-only fills, or an unlogged action menu.
- Strong historical average evidence followed by a change in present economics.
- Overlapping delayed labels, quick-winner completion and outcome-dependent censoring.
- Multiple monitors, resets and holdout reuse without declared error/search accounting.
- Full-sample fitted regimes despite apparently causal filtering.
- Low regret against losing arms, or positive gross returns erased by switching.
- Distinct sleeves failing together through one liquidity or collateral dependency.

Promote only when candidate-specific economic evidence, realistic execution, portfolio constraints and operational replay pass their declared gates. If the data cannot identify the desired improvement, name the missing counterfactual and the least expensive experiment that can. An honest inability to identify an advantage is useful information; a more elaborate model is not automatically the remedy.
