All supplied numerical inputs are **MODEL ASSUMPTIONS**; calculations below are **DERIVATIONS**, not empirical trading results. E04 contains research **HYPOTHESES**. E05’s supplied completed pilot is toy **TEST RESULT** evidence. No trades or external actions were performed.

## E01 — Signal and executable price

**Pass.** The appropriate likelihood ratio is conditional on the same public information as the prior: 0.60/0.40 = 1.5. The unconditional sales claim of 4 cannot replace it.

\[
p_+=\frac{0.58(0.60)}{0.58(0.60)+0.42(0.40)}
=\frac{0.348}{0.516}=0.6744186.
\]

Expected net payoff is 0.6744186 − 0.69 − 0.01 = **−0.0255814 per contract**, versus zero for passing. The break-even purchase price before the additional cost is **0.6644186**; buying requires a strictly lower price for positive expectation. The sensor fee is sunk and must not be deducted again.

The three analysts contribute no additional observation and no further Bayesian evidence. They might improve interpretation or error checking in another problem, but paraphrasing this already specified observation cannot multiply its likelihood ratio.

The signal contains outcome information but has zero decision value under this fixed buy/pass menu: the positive result still implies passing, and the negative-result posterior is still lower. The finite-information companion confirms both signal branches select pass.

**Next experiment:** collect a separately sourced observation with original timestamps, retaining its dependence on public information and this sensor. Freeze a price-aware baseline and compare it with the joint-signal model on chronological, untouched opportunities at attainable quotes. After today’s positive sensor, additional conditional likelihood ratio must exceed **1.12644** to cross the 0.70 probability hurdle, assuming the quote and costs remain unchanged. Test calibration around that decision boundary and net value after acquisition, delay and fills. A separate source is not automatically independent; estimate joint conditional likelihoods. Reject the candidate if improved prediction does not produce executable incremental value.

## E02 — Where the risk lands

**Add one unit of B.** After the new fee, A’s payoff is (−14,+12) and B’s is (+12,−14). Both have standalone expected net payoff **−1**. Their identical marginal payoff distributions conceal different coupling to existing wealth.

| Action | Stress wealth | Ordinary wealth | Expected log wealth | Increment over existing portfolio |
|---|---:|---:|---:|---:|
| Nothing | 40 | 100 | 4.14702482 | 0 |
| A | 26 | 112 | 3.98829770 | −0.15872712 |
| B | 52 | 86 | 4.20279551 | +0.05577069 |

For example,
\[
\Delta U_B=\tfrac12\log(52/40)+\tfrac12\log(86/100)=0.05577069.
\]

The extra fee appears once in terminal wealth. Log utility gives an additional dollar greater value when wealth is 40 than when it is 100. B transfers wealth toward that stress state; A worsens it. B therefore improves the stated objective despite lowering expected wealth from 70 to 69. The supplied absence of interim collateral demands makes the terminal comparison sufficient here.

This establishes portfolio-specific hedge value under the toy assumptions. It establishes neither informational superiority nor positive expected profit or benchmark alpha. A resembles supplying stress insurance, but the facts do not show adequate compensation for this desk; B consumes protection. A genuine risk-warehousing claim would require identifying the payer, its unwanted exposure, its willingness to pay, this desk’s reservation compensation and funding capacity. No such empirical claim follows from a favorable utility calculation alone.

## E03 — Related contracts and a repaired bundle

**Reject A+B as guaranteed profit.** If preliminary = 99 and final = 101, both contracts pay zero. Net payoff is **−0.96**. Preliminary = final = 100 also produces zero payout and the same loss. Revision differences and equality each defeat the presumed complementarity. Depending on state, combined payout can be 0, 1 or 2; net payoff can be −0.96, +0.04 or +1.04.

**A+C is a guaranteed-profit bundle under the stated assumptions.** For every possible preliminary value, exactly one of “strictly greater than 100” and “less than or equal to 100” holds. Thus payout is identically 1, including at exactly 100.

All-in acquisition cost is 0.44 + 0.48 + 0.02 = **0.94 per pair**, leaving **0.06 guaranteed profit per pair**. Capacity is min(100,20) = **20 pairs**. Total outlay is **18.80**, payout **20.00**, maximum guaranteed profit **1.20**.

Borrowing 18.80 at the supplied zero interest funds the purchase; settlement repays 18.80 and leaves 1.20 in every state. This is a self-financing sure-profit arbitrage in the toy model. The finite-payoff companion verifies the two exhaustive preliminary-value categories with an explicit financing repayment leg.

The conclusion requires the same preliminary observation, complementary inclusive/strict boundaries, atomic execution for 20 pairs at the stated prices, complete fees, available financing through payment, and identical certain settlement/counterparty terms. These are supplied assumptions, not verified real-world conditions. Unpaired extra A units add risk and cannot increase guaranteed profit.

## E04 — Construct something new from a small desk

**Two hypotheses worth testing; neither is validated.** Preserve the existing engine’s exclusive authority to admit entries at the first eligible closed hourly bar. Signal readiness cannot advance entry. Use quotes available after admission, and record skips, nonfills and cancellation outcomes. Capital, borrow and impact remain measurement requirements; no live allocation is specified.

**Candidate 1: trade a contradiction between the earnings headline and forward guidance.**

- **Participant/transfer:** marginal headline-reacting investors may underprocess economically linked details. The proposed surplus is residual mispricing after the executable quote already incorporates public information; their mistake is a hypothesis, not an assumption that all counterparties are uninformed.
- **As-of signal:** deduplicate releases by source lineage; compare current guidance with the latest previously published guidance for the same metric and horizon. Jointly encode headline direction, guidance revision, accompanying cash-flow qualifications and the quote response. For example, a weak backward-looking headline combined with improved forward guidance and a falling quote creates a candidate long. This uses no invented analyst consensus or private feed.
- **Action/exit:** the long-only prototype buys only when the augmented forecast’s expected gain through the next session’s close exceeds measured execution and holding costs plus a preregistered economic hurdle. Otherwise pass. Exit at that fixed horizon, with a predefined invalidation rule for correcting disclosures. Short variants require measured, feasible borrow before admission.
- **Persistence/capacity:** reconciling inconsistent disclosures may cost more attention than a small opportunity justifies for large firms. Whether any residual survives the hourly wait is the critical unknown. Depth, impact, competition and opportunity frequency limit scale.
- **Bad state/rival:** apparently improved guidance masks deterioration, or new market-wide news overwhelms it. Strongest rival: ordinary momentum/reversal, rather than the semantic interaction, explains subsequent returns.
- **Decisive experiment:** freeze a quote-aware headline model and an augmented joint-detail model with matched fitting budgets. Replay chronological events at the actual permitted hourly entry and fixed exit. Compare incremental forecast quality, decision-boundary calibration and net opportunity payoff; use duplicated stories and mismatched document pairings as negative controls. Reject the economic claim if adequate confirmation rules out the prespecified net improvement, or if value exists only before permitted entry. Insufficient precision stays inconclusive.

**Candidate 2: bridge inventory for index deletions after netting offsetting migrations.**

- **Payer/service:** benchmark trackers facing a rebalance deadline may pay an execution concession to transfer unwanted inventory and tracking risk. The desk supplies temporary inventory capacity; specific counterparties and forced quantities are not observed directly.
- **As-of signal:** combine yesterday’s public rebalance announcement, its stated effective time, holdings actually disclosed by that date, and current depth/quotes. Estimate a range of deletion-related selling after accounting for observable offsetting additions or migrations. Treat stale or incomplete holdings as uncertainty, not current orders. Filter contemporaneous fundamental news using source timestamps.
- **Action/exit:** research a long-only purchase of pressured deletions at the first eligible hourly bar, conditional on estimated concession exceeding measured costs and portfolio reservation compensation. Exit on the first eligible hourly bar of the next session after implementation; skip if the implementation clock is unavailable or conditions have already normalized. No assumed dealer-position signal is needed.
- **Persistence/capacity:** a documented deadline can create demand for immediacy despite universal awareness. Small, uneven inventories may be unattractive to large providers, but capacity is bounded by competing absorption, depth and the desk’s financeable stress loss.
- **Bad state/rival:** deletion coincides with lasting fundamental decline; market stress delays recovery and funding becomes scarce. Strongest rival: permanent information-based repricing, not temporary selling pressure.
- **Decisive experiment:** replay deletion events using holdings publication lags and the approved clock. Compare generic reversal, gross announced demand and net-demand-plus-news variants at matched exposure. Test whether documented net demand predicts post-implementation recovery after costs, using low-net-demand migrations and non-event dates as controls. Require reservation-value and stress-funding measurements before any promotion. Rejection occurs if compensation disappears after these controls and costs; quote replay alone cannot certify passive fills.

**Contrarian alternative:** the index selling story may be entirely true while migrations cancel net demand and competing providers absorb the rest before the hourly entry. Similarly, the earnings contradiction may be real but fully priced already. Complexity and headline plausibility do not create capture.

**First research step:** build one immutable release-to-hourly-entry event table and replay Candidate 1 against the cheap quote-aware baseline. This cheaply tests the binding timing constraint without estimating hidden order flow. Economic upside of the two candidates is unranked pending measurements; Candidate 1 has the better-defined first experiment. Keep a trial ledger and untouched confirmation period.

## E05 — What the routing data identify

**The old 22% claim is unidentified from that log.** Calm contexts never used A, so the always-A target lacks support there. Route and context are confounded; ordinary importance weighting cannot repair zero action probability. Displayed-touch simulated fills are model outputs, not observed counterfactual executions, and omit uncertain queue selection and impact unless separately justified.

The randomized pilot supplies overlap and, under its explicit causal assumptions, identifies one-step policy values for the equally weighted target contexts:

\[
\widehat V(\text{always A})=\tfrac12(0.14)+\tfrac12(0.04)=\mathbf{0.09},
\]
\[
\widehat V(\text{old rule})=\tfrac12(0.10)+\tfrac12(0.04)=\mathbf{0.07}.
\]

Estimated improvement is **0.02 net reward per opportunity**, entirely from replacing P with A in calm contexts. Relative to 0.07 it is about **28.6%**, a toy point estimate rather than confirmation of the old 22% claim. The positive estimates support always-A as a challenger for this population, not automatic deployment.

Without reward variances or event-dependence information, no standard error, confidence interval, significance or power claim is justified. Randomization establishes identification under the assumptions; it does not eliminate finite-sample uncertainty. Nothing here establishes performance under changed contexts, inventory feedback, larger size or future market conditions.

Keep the **50 unresolved outcomes pending**, attached to their original assignments, versions and fixed maturity horizons. Do not assign zero, exclude eventual slow losers, or enlarge the mature denominator. Track pending risk separately; investigate informative delay or censoring before pooling cohorts.

**Next step:** obtain the pilot’s individual rewards and event identifiers, estimate dependence-aware uncertainty, and predeclare a confirmation/monitoring rule for the 0.02 improvement against an economic hurdle. Preserve route propensities and mature-cohort accounting. A further randomized routing pilot would require its own execution authorization; shadow fills remain simulation evidence. Repeated monitoring needs an explicit error budget and reset policy, not repeated unadjusted tests.

## E06 — Faster intelligence at finite capacity

For an entered opportunity, let \(e=a_0e^{-d/4}\). Then
\[
\Pi(q)=q(e-0.01)-0.0004q^2-K,\qquad
q^*=\min\{60,\max[0,(e-0.01)/0.0008]\}.
\]

The second derivative is −0.0008, so the positive-size optimum is unique unless clipped. Compare that optimum separately with skipping at zero profit, which incurs no computation cost.

| Mode | Deadline feasible? | Decayed gross edge | Unconstrained size | Allowed optimum | Net expected profit |
|---|---|---:|---:|---:|---:|
| SIMPLE | Yes, 1 second | 0.0934561 | 104.3201 | 60 | 2.567366 |
| DEEP | No, 3 seconds | 0.0850260 | 93.7825 | Infeasible | Excluded |
| FAST-DEEP | Yes, 0.25 seconds | 0.1690944 | 198.8679 | 60 | 3.105661 |
| Skip | Yes | — | — | 0 | 0 |

**Choose FAST-DEEP, 60 contracts.** Its improvement over SIMPLE is **0.538295 per opportunity**, after its larger computation cost. DEEP would yield only 0.061559 at 60 if the deadline were ignored, but cannot enter the feasible comparison. Shared capacity prohibits stacking modes.

A 10,000-fold position would be **600,000 contracts**, violating the stipulated capacity by 10,000-fold. Fund wealth does not expand executable depth. Even extrapolating the quadratic formula outside its valid domain would make impact grow 100 million-fold while gross payoff grows only 10,000-fold; that extrapolation is not a deployment forecast.

**Highest-value deployment experiment:** first benchmark end-to-end timing and economics in forward simulation against SIMPLE at matched opportunities and sizes. Measure initial forecast edge, actual delay decay, tail latency and deadline misses, computation charges, fills/nonfills, spread, impact versus size, adverse selection, funding needs and shared portfolio exposure. Validate a simple fallback and mandatory checks within the deadline. Real executable capacity then needs authorized bounded experimentation; no simulated fill or fund-size argument supplies that evidence.
