# Adaptive learning and evidence: Trading Edge Lab v2 research memo

Research performed 2026-10-24 UTC. Read the current complete SKILL.md, foundations.md, validation.md, and mechanism blueprints. The first version is strong on economic mechanism, execution-conditioned payoff, chronology, search accounting, and survival. Its adaptive layer remains procedural: it calls for sequential inference and monitoring without specifying the estimand, information filtration, admissible learning feedback, or the action support needed to make those claims meaningful.

This memo proposes a concrete evidence and learning layer. It does not establish trading profitability. Source statements below are primary-paper findings; the system design is a proposed engineering synthesis. Nine distinct new sources are identified L01–L09. Paper revisions are not additional corroborating studies. No source is claimed to have been independently reproduced.

## 1. Most consequential additions

1. **Make evidence a typed object.** Every detector must state its null, target, units, support/tail assumptions, filtration, outcome maturity, multiplicity allocation, and permitted consequence. “Confidence: 95%” without these fields should be rejected by the policy-change gate.
2. **Separate three clocks.** Decision time, label maturity, and evaluation-update time differ. A fast engine can make thousands of decisions while possessing only a few resolved opportunities. Unresolved positions must not silently become zero losses or independent observations.
3. **Separate changing context from changing economics.** Data-quality faults, changed opportunity mix, degraded conditional forecasting, worse fills, and changed risk compensation call for different repairs. A single P&L alarm does not identify the cause.
4. **Specify the feedback type before selecting an optimizer.** Full-information forecast comparison, contextual-bandit routing, and stateful portfolio control have different identifiable counterfactuals. They should not share an unquestioned “RL optimizer.”
5. **Keep learning and trading budgets separate.** Exploration consumes cash, capacity, time, and statistical error. Being uncertain does not create permission to spend these budgets. An experiment can be worth performing while its trading strategy is not yet worth deploying.
6. **Treat memory length as a tested policy choice.** Faster forgetting improves responsiveness but increases estimation noise. More frequent retraining is an intervention with costs and a research trial count, not automatic intelligence.

## 2. Primary-source register and verified scope

### L01 — Howard, Ramdas, McAuliffe, Sekhon (2021)

**Time-uniform, nonparametric, nonasymptotic confidence sequences.** Annals of Statistics; inspected author revision dated August 2022. URL: https://arxiv.org/pdf/1810.08240 . Web reference: `turn69view0`; assumptions and discussion `turn73view0`.

**Access:** PDF body, introduction, conditional concentration construction, and discussion of running intersections. **Source claim:** confidence sequences provide simultaneous coverage across observation times under specified conditional tail assumptions. Nonparametric does not mean assumption-free. Their treatment allows time-varying targets; repeatedly intersecting intervals intended for a constant parameter can become inappropriate under drift. **Use:** replace repeated fixed-time significance checks with an explicitly selected sequential method. **Limit:** coverage of an estimand is not a forecast of future profitability, and arbitrary heavy-tailed P&L does not inherit a bounded/sub-Gaussian guarantee.

### L02 — Ramdas, Ruf, Larsson, Koolen (2022)

**Admissible anytime-valid sequential inference must rely on nonnegative martingales.** Inspected November 2022 revision. URL: https://arxiv.org/pdf/2009.03167 . Web reference: `turn81view2`.

**Access:** PDF body, definitions and martingale/e-process framework; not a line-by-line proof audit. **Source claim:** anytime-valid confidence sequences, p-processes, and e-processes are connected to nonnegative martingale methods; the paper characterizes admissibility. **Use:** an evidence process must be justified under its stated null and observation history. **Limit:** an e-value is not the posterior probability of an edge. A test can reject a historical null while providing no protection against a subsequent structural change.

### L03 — Waudby-Smith, Wu, Ramdas, Karampatziakis, Mineiro (2024)

**Anytime-valid off-policy inference for contextual bandits.** URL: https://arxiv.org/pdf/2210.10768 (August 2024 revision); journal DOI https://doi.org/10.1145/3643693 . Web references: `turn69view1`, `turn85view0`, `turn96view1`.

**Access:** PDF data-generation assumptions, support requirement, predictable tuning, and time-varying-value section. **Source claim:** inference can accommodate adaptive logging and dependent changing contexts. Mean-reward results assume bounded rewards; target policy must be absolutely continuous with respect to logging policy. Their time-varying estimand is the average conditional policy value so far. Exogenous context/reward evolution supports interpretation across entire hypothetical action sequences. **Use:** require logged propensities and overlap before off-policy claims. **Limit:** dependence of future conditions on earlier actions changes the counterfactual interpretation; inventory, impact, and funding are not automatically covered by one-step contextual-bandit inference.

### L04 — Dudík, Langford, Li (2011)

**Doubly Robust Policy Evaluation and Learning.** ICML. URL: https://arxiv.org/pdf/1103.4601 . Web references: `turn69view2`, `turn85view1`, `turn73view5`.

**Access:** PDF problem definition, estimator, bias theorem, and variance discussion. **Source claim:** combining reward predictions and propensity weighting yields bias depending on errors in both models; correctness of either can eliminate the corresponding estimation bias under the model. Importance weighting can have large variance when behavior and target differ. **Use:** a doubly robust estimator can improve supported routing comparisons. **Limit:** “doubly robust” is not protection against zero support, incorrect payoff semantics, unobserved confounding, temporal leakage, or a wrong causal estimand. Nuisance fitting and policy selection still need honest evaluation.

### L05 — Kazerouni, Ghavamzadeh, Abbasi-Yadkori, Van Roy (2017)

**Conservative Contextual Linear Bandits.** NeurIPS. URL: https://mohammadghavamzadeh.github.io/PUBLICATIONS/nips17.pdf . Web references: `turn69view3`, `turn85view2`.

**Access:** PDF Section 2 assumptions/performance constraint, Algorithm 1, and theorem assumptions. **Source claim:** CLUCB explores while retaining a specified fraction of cumulative baseline expected reward with high probability, under a linear reward model, bounded features/parameters, conditional sub-Gaussian noise, and baseline assumptions. It includes an extension for unknown baseline rewards. **Use:** bounded exploration can be benchmark-relative. **Limit:** the guarantee concerns modeled cumulative expected reward, not realized drawdown, margin safety, or each individual decision. The original nonnegative-reward multiplicative constraint cannot be copied unchanged to signed trading P&L.

### L06 — Besbes, Gur, Zeevi (2014)

**Stochastic Multi-Armed-Bandit Problem with Non-stationary Rewards.** NeurIPS. URL: https://proceedings.neurips.cc/paper_files/paper/2014/file/91ba7292e5388b90b58d0b839a7f19ec-Paper.pdf . Web references: `turn81view0`, `turn96view2`, `turn87view2`.

**Access:** PDF variation-budget definition, regret benchmark, lower bound, restart policy, and unknown-budget discussion. **Source claim:** achievable dynamic regret depends on reward variation; the model exposes a remembering/forgetting tradeoff. In its stated range, a lower bound scales as `(K V_T)^(1/3) T^(2/3)`; variation linear in the horizon prevents sublinear regret against the dynamic oracle. **Use:** adaptation has an information-theoretic cost. **Limit:** regret is relative to the specified comparator and assumptions. Small regret does not imply positive net profit; a rapidly moving best strategy may be untrackable.

### L07 — Joulani, György, Szepesvári (2013)

**Online Learning under Delayed Feedback.** ICML. URL: https://proceedings.mlr.press/v28/joulani13.pdf . Web references: `turn81view1`, `turn87view3`, `turn96view3`.

**Access:** PDF delayed-feedback protocol, assumptions, and stochastic queue algorithm. **Source claim:** delayed feedback changes regret guarantees; particular stochastic assumptions yield additive delay costs, while adversarial analyses behave differently. Results distinguish feedback time from decision time and include restrictions on delay dependence. **Use:** maintain a pending-outcome queue with decision identifiers and maturity rules. **Limit:** trade resolution delay often depends on the outcome or action. Fast winning exits and slow losing exits can bias completed-trade samples; the paper's independent-delay conclusions should not be imported automatically.

### L08 — Li, Chu, Langford, Wang (2011)

**Unbiased Offline Evaluation of Contextual-bandit-based News Article Recommendation Algorithms.** WSDM; inspected March 2012 author revision. URL: https://arxiv.org/pdf/1003.5956 . Web references: `turn81view3`, `turn87view4`.

**Access:** PDF replay algorithm and Theorem 1 assumptions. **Source claim:** matched-action replay is unbiased under its randomized logging and i.i.d. context/payoff setup; uniform logging retains events with action-independent probability. **Use:** distinguish genuine logged-action replay from simulation. **Limit:** replaying historical market prices does not recreate unobserved queue fills, own impact, or alternative inventory paths. Deterministic historical routing is not equivalent to a randomized logging dataset.

### L09 — Choe and Ramdas (2026 accepted manuscript)

**Combining Evidence Across Filtrations.** Accepted JRSS B manuscript, March 2026 revision of a 2024 preprint. URL: https://arxiv.org/pdf/2402.09698 . Web reference: `turn100view0`.

**Access:** PDF definitions, financial time-series example, combination discussion, and stated lifting results; not all proofs independently audited. **Source claim:** an e-process valid in a coarse information filtration need not be valid when stopping uses richer information. Processes for the same null in a common filtration can be averaged; otherwise justified adjustment/lifting may be necessary. **Use:** make the information available to each detector and to the stopping controller explicit. **Limit:** do not freely multiply correlated evidence processes or average monitors operating under incompatible information histories. Multi-step forecast evaluation is a specific application.

## 3. Minimal valid evidence engine: elementary derivation

This is a deliberately simple **strong-null test**, not a general test of cumulative average improvement and not a market model. Define resolved increments `X_t` with known bound `-1 <= X_t <= 1`. Let `F_(t-1)` contain all information available before observing increment `t`, including all information used to select the observation or betting fraction. Test:

`H0: E[X_t | F_(t-1)] <= 0 for every t`.

Choose `lambda_t` predictably from `[0,1)`; a constant such as 0.5 suffices for an illustrative implementation. Set:

`E_0 = 1; E_t = E_(t-1) * (1 + lambda_t X_t)`.

Each factor is nonnegative, and under H0:

`E[E_t | F_(t-1)] = E_(t-1) * (1 + lambda_t E[X_t|F_(t-1)]) <= E_(t-1)`.

Thus the process is a nonnegative test supermartingale. Ville's inequality gives `P_H0(sup_t E_t >= 1/alpha) <= alpha`. Store `log E_t` by summing `log1p(lambda_t X_t)` to avoid numerical overflow. Reject only when the specified boundary is crossed. Fixed or past-measurable fractions are essential: selecting lambda after seeing the same increment destroys this derivation. This is a direct elementary specialization of the sequential framework in L01/L02.

For paired net-value difference `D_t` and fixed economic hurdle `h`, use `X_t=(D_t-h)/B` only if `|D_t-h|<=B` is a justified bound, not the largest historical observation. Clipping an unbounded return creates a different bounded target and may hide tail losses. A stop order does not create a hard loss bound. A valid construction for a tail assumption is preferable when no true bound exists.

**Interpretation:** crossing rejects the claim that conditional improvement was never positive throughout this tested sequence. It does not prove the improvement is positive at the next decision, nor that every time was favorable, nor that an arbitrary cumulative-average null was tested. Use the correct weak-null/time-varying construction if that is the intended target; do not relabel this simple product.

**Maturity and ordering:** choose increments from a declared evaluation schedule. Update only when the required outcome is available. Delayed and overlapping outcomes can reveal partial information about each other; the conditional null must hold in the actual update filtration. Merely numbering settled trades in arrival order does not establish this. A conservative implementation can use prespecified nonoverlapping evaluation blocks; otherwise implement a method justified for the specific delayed filtration. Count pending risk separately.

**Multiple detectors and restarts:** assign prospective error budgets `alpha_(j,r)` to detector j and epoch r, with total sum at most `alpha_total`. One transparent allocation is `alpha_(j,r)=alpha_total*w_j/[r(r+1)]`, where r starts at 1 and nonnegative `w_j` sum to at most 1. The union bound then controls a family of valid false rejections without requiring independence. Do not start each new window with another unaccounted 5%. Assign a new test before its new observations, preserve all prior outcomes, and label the new estimand. This allocation is an elementary engineering construction, not an optimality claim.

## 4. Counterfactual support contract

Before claiming an adaptive router improves a strategy, require:

```text
decision_id / policy_version / timestamp / information_cutoff
context_snapshot / candidate_action_set / feasible_action_mask
selected_action / actual_selection_probability / randomization_id
position_and_pending_orders / exposure_before_and_after
outcome_definition / horizon / maturity_time / censoring_reason
net_reward / component_costs / realized_vs_simulated_label
target_policy_version / target_action_probabilities
support_check / maximum_weight / effective_sample_size_diagnostic
impact_and_state_transition_assumptions
```

For discrete supported actions, a familiar doubly robust pseudo-outcome for target policy pi is:

`psi_t(pi) = sum_a pi(a|x_t)*mhat_t(x_t,a) + [pi(a_t|x_t)/b_t(a_t|x_t)]*[r_t-mhat_t(x_t,a_t)]`.

`b_t` is the actual behavior/logging probability, not a retrospective guess chosen to improve results. Fit `mhat_t` on earlier data or use an evaluation design whose sample splitting is valid for the dependence structure. Diagnose large weights and effective sample size; these describe overlap/precision and are not a certification. If `b_t(a|x)=0` where pi assigns positive mass, reject a nonparametric OPE claim for that action. Weight clipping trades bias for variance and must be disclosed.

The crucial decision is the **counterfactual level**:

| Feedback regime | What can be assessed | What remains unobserved |
|---|---|---|
| Shared event outcome and negligible own influence | Alternative precommitted probability forecasts on the same event | Whether an alternative order would fill at the quoted price |
| Randomized supported routing with logged propensities | One-step target-policy reward under stated identification assumptions | Unsupported actions; changed future state distribution |
| Historical quote replay | A simulated policy under execution assumptions | Actual queue priority, impact, and counterparties' response |
| Stateful inventory/funding/control | Full trajectory value under an explicit transition model or suitable causal experiment | A different trajectory cannot be inferred from one-step weights alone |

Shadow orders are valuable engineering observations but not actual fills. More simulated trades do not repair missing empirical support. Use market-impact-aware simulation as a model, then report its validation gap. Do not randomize real-money actions unless already authorized within defined risk and experiment budgets.

## 5. Learning controller to connect to the master algorithm

Maintain three distinct registries:

- **Production policy:** frozen approved rules plus previously validated adaptive parameter ranges.
- **Challengers:** immutable candidate versions evaluated under prospective conditions.
- **Evidence contracts:** detector/estimator configurations tied to the version and estimand.

On each opportunity, the production controller uses only mature features and approved model state. It logs all feasible candidates and abstention. A later learning event attaches newly resolved outcomes to the original versions. The evaluator updates only the matching evidence contract. A strategy does not become a new candidate merely because a running estimate changes within an approved adaptive policy; changing the learning rule, horizon, feature family, reward, or constraint produces a new candidate.

Route an alert by cause before changing a strategy:

| Observation | Initial interpretation | Permitted response to test |
|---|---|---|
| Stale prices, duplicate event, unknown inventory | Operational invalidity | Apply deterministic fail-safe; do not wait for significance |
| Different input distribution, stable conditional scoring | Opportunity mix shift | Reweight/calibrate only with support; inspect coverage |
| Worse scoring on comparable mature events | Forecast/model deterioration candidate | Quarantine feature/model change; evaluate frozen challenger |
| Stable forecast, worse conditional markouts | Capture/execution deterioration candidate | Compare routing/size/latency; retain forecast baseline |
| Similar gross returns, rising common crisis exposure | Portfolio/risk compensation change | Reassess scenario/capital constraints |
| Lower completed-trade returns with changing pending fraction | Possible maturity/censoring selection | Repair cohort evaluation before interpreting edge |

Set different review speeds. Data health and risk limits respond immediately. Mature-outcome statistics update when valid feedback arrives. Policy promotion occurs only on predefined evidence/risk gates. Longer-term mechanism research runs outside the execution path. Speed is obtained by separating these clocks, not by letting every short-term fluctuation rewrite the strategy.

For signed trading rewards, prefer an explicitly denominated experimental loss allowance and hard capital constraints over copying a fraction-of-positive-baseline guarantee. Track expected opportunity cost, realized loss, stress loss, and pending exposure separately. Include cash/abstention and a frozen baseline in the action set. Bandit optimism is a research selection device, not a reason to exceed a desk's survival constraints.

## 6. High-value forward tests for the upgraded skill

These are proposed tests, not completed outcomes:

1. A router's reported +10% uplift comes from deterministic historical routing; all unselected fills are simulated. Require an answer that distinguishes forecast replay from unsupported causal execution claims and proposes the cheapest identifiable follow-up.
2. Five-minute forecasts settle after 30 minutes; a dashboard updates on each closed position and the strategy exits winners early. Require maturity-aware cohort accounting, no fabricated sample independence, and a valid sequential target.
3. Two individually valid monitors operate on odd/even delayed subsequences; the desk switches when their unadjusted average crosses a threshold and also observes full intraday prices. Require the information-filtration mismatch to be recognized before claiming combined validity.
4. A bandit produces low regret against three losing strategies. Require comparison with cash, cost accounting, and refusal to equate regret with edge.
5. An anytime monitor crosses once, resets after every drawdown, and has twenty parallel variants. Require explicit family/restart accounting and no interpretation of the e-value as a posterior probability.
6. A long-lived positive average-value confidence sequence persists after a plausible regime break. Require separation of historical average evidence from current predictive value and an explicit cost-aware review policy.

The principal improvement is an **identifiability-aware adaptive system**: it learns rapidly where observations support learning, keeps uncertainty visible where they do not, and avoids converting repeated observation or computation into fictitious evidence.
