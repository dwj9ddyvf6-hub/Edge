# Validation: experiments, evidence, and desk handoff

## Contents

1. Decision artifacts
2. CREATE and IMPROVE workflows
3. Availability, fills, and dependence
4. Statistical tools and limits
5. Quantitative precision example
6. Keep, modify, pause, or reject
7. Forward monitoring and deterministic integration

Use this reference to turn the core workflow into an executable research plan. The procedures are an engineering synthesis; source identifiers refer to `sources.md`. An economic explanation directs experiments but does not certify returns. Empirical predictors can remain candidates with unresolved mechanisms; theoretical labels alone do not guarantee durability. [V10, V12]

## 1. Decision artifacts

Complete the following compact Edge Contract before selecting a final candidate. Write `UNKNOWN` where evidence is missing; distinguish a measured value from an assumption.

```text
contract_id / version / research_owner:
mode: CREATE | IMPROVE | AUDIT
decision: what capital or policy decision will this evidence change?
estimand: net expectancy | benchmark excess | portfolio utility | forecast loss
instrument / exact payoff / venue / horizon / eligible universe:
participant segment / objective / constraint:
proposed transfer: information error | paid service/risk | unresolved pattern
our measurable advantage / executable access:
observable state / action / exit / abstention:
information availability / decision deadline / execution policy:
persistence mechanism / capacity limit / adverse state:
strongest rival explanation:
primary observable implication / negative control:
falsifier / missing evidence / cheapest decisive experiment:
benchmark / economic hurdle / error tolerance / risk mandate:
current evidence stage / permitted next stage:
```

Maintain three additional artifacts:

| Artifact | Required fields |
|---|---|
| Experiment card | Hypothesis; one conceptual change; estimand; eligible opportunities; benchmark; training/evaluation dates; outcome horizon; planned contrasts; costs; dependence unit; inference method; power/precision assumptions; promotion/failure rule |
| Append-only trial ledger | Trial and parent IDs; creation time; researcher/agent; rationale; code/config/data hashes; universe and feature versions; parameter values; splits; label definition; execution assumptions; metrics viewed; outcome; rejected variants; holdout-access history |
| Decision record | Evidence stage; completed versus unrun tests; estimates and uncertainty; execution feasibility; stress results; strongest contradiction; selected action; unresolved conditions; next review trigger; approver if required by mandate |

Count agent-generated variants, discarded filters, alternative labels, and changed cost assumptions as research choices. Unknown earlier searches make selection-adjusted inference incomplete. Do not silently record only successful experiments. [V1, V3]

## 2. CREATE and IMPROVE workflows

For **CREATE**, first evaluate whether each proposed mechanism has observable implications and feasible access. Select a small research set with genuinely different mechanisms, then specify a cheap falsification experiment for each. For example, an information-delay thesis predicts weaker returns when entry is delayed; a forced-flow thesis predicts variation with the observable constraint. Check a rival explanation that produces the same pattern. A chart association alone cannot establish the proposed causal transfer. [V10]

Build a minimal policy, freeze its candidate family, and conduct chronological development and validation. Fit preprocessing, feature selection, thresholds, and calibration inside training periods. Reserve a final period that has not informed choices. If the policy adapts, replay the entire learning schedule using only information then available. Test the selected policy prospectively before moving its evidence stage.

For **IMPROVE**, freeze the existing policy and reproduce its outputs first. Attribute the shortfall to forecast quality, opportunity selection, entry/exit, costs, fill quality, exposure, or portfolio interaction. Choose the binding problem and one conceptual intervention; include simplification as a candidate. Compare policies on the same external opportunity stream, calendar, capital convention, and feasible execution assumptions. Include abstentions and missed opportunities rather than comparing only each policy's successful fills.

Use paired differences where appropriate, preserving shared event dependence. Match exposure or explicitly attribute changed beta, volatility, tail loss, and capital usage. Test interactions after evaluating individual changes. A filter that reduces turnover may improve net results without improving forecasting; name the improvement correctly. Additional leverage changes returns without establishing additional edge.

For both modes, select controls that isolate the claim: cash, passive exposure, matched-risk exposure, delayed signal, removed feature, same execution without the new model, or event-time randomization within defensible blocks. Unrestricted shuffling can erase dependence and create an irrelevant null. Keep the benchmark and principal metric fixed through confirmation. Reusing holdout results to choose revisions makes that sample development data. [V1, V2]

## 3. Availability, fills, and dependence

Construct a decision-level evidence table:

```text
opportunity_id, instrument_id, event_id, event_time,
source_publication_time, vendor_receipt_time, revision_id,
feature_available_time, decision_time, information_cutoff,
model_version, forecast, action_or_abstention,
quote_time, bid, ask, executable_size,
order_time, order_id, acknowledgment_time,
fill_time, fill_price, fill_size, fees,
exit_or_settlement_time, realized_payoff, rejection_reason
```

Use immutable instrument identifiers and historical membership; retain delistings, expired instruments, revisions, and missing-data outcomes. Verify that every feature was available by the decision cutoff. Final daily bars, subsequently confirmed pivots, revised releases, and retrospectively named regimes require explicit availability treatment. Trade simulation must begin at an achievable time after the decision.

For passive orders, estimate fill probability and payoff conditional on filling; a fill can select adverse states. Preserve no-fill branches and opportunity cost. For multiple legs, simulate partial execution, hedge/unwind costs, and collateral use. Use executable sides and size rather than treating the midprice as attainable. Report results under plausible spread, impact, financing, and latency stress; missing execution evidence lowers the evidence stage.

Record the true dependence unit. Multiple trades in one event, overlapping holding intervals, securities exposed to one announcement, and repeated labels of the same future move do not constitute independent observations. Purge training labels whose outcome intervals overlap test outcomes. Where future training observations are retained in a resampling design, use justified separation for information carried from the test interval. Select gaps from actual information and holding horizons.

Resample blocks or event clusters while keeping competing policies aligned. Examine plausible block-length choices and cross-sectional clustering. Fit any learned transformations within the relevant training fold. Dependence correction does not eliminate regime change or repair leakage.

## 4. Statistical tools and limits

Choose methods for the question, not for a desired verdict:

| Tool | Appropriate interpretation | Incorrect interpretation |
|---|---|---|
| Reality Check | Tests whether the searched family contains predictive superiority over the benchmark, accounting for the recorded search | Proves the winning economic mechanism or repairs unrecorded searches [V1] |
| SPA | Studentized comparative test less sensitive to poor alternatives; global rejection indicates at least one superior candidate | Certifies whichever individual strategy is subsequently selected [V2] |
| DSR | Selection- and non-normality-aware Sharpe diagnostic using trial and distribution information | Posterior probability of live profitability; substitute for valid costs or dependence assumptions [V3] |
| PBO/CSCV | Estimates instability of a specified selection process: in-sample winners ranking below the candidate median out-of-sample | Probability of a monetary loss; replacement for chronological deployment replay [V4] |

Predeclare one principal decision procedure and use other methods as diagnostics. Do not average incompatible statistics into a fictitious probability. Explain conflicting results. Candidate-specific promotion after a global test requires suitable follow-up inference. Distinguish insufficient evidence from evidence of no economically useful effect. Repeated interim looks need a valid sequential design or explicit multiplicity adjustment.

Score prospective forecasts against timestamp-matched base-rate and market forecasts. Evaluate calibration and discrimination separately from decision economics: a calibrated base rate may offer no useful discrimination, while improved scoring may occur outside tradable states. [V8]

## 5. Quantitative precision example

**Hypothetical illustration, not a backtest or allocation recommendation.** A binary bet pays decimal odds `d = 1.90`; deterministic additional cost is `c = 0.02` per unit stake. Expected net payoff is `1.90p − 1.02`; break-even probability is `1.02 / 1.90 ≈ 0.53684`. An estimated `p = 0.56` implies estimated net expectancy `0.044` per unit stake. It does not establish that the true probability exceeds break-even.

Suppose the experiment prospectively chooses approximate 95% two-sided probability precision of ±0.02. Under independent, identically distributed Bernoulli outcomes, a conservative normal-approximation calculation gives

`n ≈ 1.96² × 0.25 / 0.02² = 2,401`.

If that sample actually produced an estimate near 0.56, its approximate lower endpoint near 0.54 would narrowly exceed the original break-even probability. Raising cost to 0.04 moves break-even to `1.04 / 1.90 ≈ 0.54737`, eliminating that confidence-bound conclusion.

This is a precision illustration, not a power calculation, a measured confidence interval, or a universal trade requirement. For planning power against a specific alternative, also choose the acceptable miss probability and calculate the corresponding sample requirement. Use suitable exact/score intervals when appropriate. Correlated outcomes, changing probabilities, selected bets, and repeated strategy search invalidate the simple independent calculation; cluster-aware precision and selection correction may require substantially more data. Variable payoffs require inference on net payoff or utility rather than win probability alone.

## 6. Keep, modify, pause, or reject

Before confirmation, define economic hurdle `h`, false-promotion tolerance, principal test family, capital-loss limit, collateral buffer, acceptable model uncertainty, and stress scenarios. Derive them from the objective and cost of a wrong decision. Do not impose universal Sharpe, win-rate, trade-count, or calendar-duration gates.

- **Keep:** the existing policy remains within mandate, implementation is valid, and review evidence does not trigger a prespecified change. Keeping is not a claim of certainty.
- **Promote:** valid candidate-specific evidence supports net benefit above `h`, execution is feasible, relevant stress fits capital constraints, and replay reproduces the policy. Promotion is limited to the next authorized stage.
- **Modify:** attribution identifies a repairable bottleneck and a specific experiment can distinguish improvement from a rival explanation. Create a new version; preserve prior results.
- **Pause:** data, reconciliation, settlement, collateral, or execution validity fails, or a prescribed risk boundary is crossed. Investigate the operational cause before interpreting P&L.
- **Reject/retire:** a preregistered falsifier is observed, credible costs consume the opportunity, the policy violates mandate, or adequate evidence rules out the required economic benefit.
- **Inconclusive:** uncertainty remains too large. State what additional information would change the decision and whether obtaining it is worthwhile.

A risk warehouse need not profit during every stress; its adverse states must be understood and capitalized. Historical maximum drawdown is not a future loss bound. Avoid forced retraining after ordinary losses: adaptation can become hidden repeated search. [V5, V11]

## 7. Forward monitoring and deterministic integration

Write forecasts and intents before outcomes. Monitor forecast score/calibration, eligible-opportunity coverage, fill probability, fill-conditioned markouts, realized costs, latency, exposure, collateral, and net attribution. Separate forecast deterioration from capture deterioration. Track the mechanism's observable driver alongside P&L; publication and competition can alter opportunity and correlation. [V8, V11]

Specify review cadence, sequential evidence rules, retraining windows, rollback versions, and independent operational kill conditions. Keep hard execution deadlines and risk checks deterministic. Persist the input snapshot, model/config versions, intent identifier, broker acknowledgments, and reconciled state. Make submission idempotent, reconcile after restart, and reject stale inputs or unknown position state. Test partial fills, duplicate events, outages, and restored state against the approved policy.

LLMs may produce research candidates and structured explanations; policy changes require the same versioned replay and acceptance process as other changes. End the handoff with actual evidence and deployment status, reproducible commands, unresolved dependencies, and the single next experiment most likely to alter the decision.
