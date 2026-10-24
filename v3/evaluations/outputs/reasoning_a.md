# E01–E06: fictional decision-research tasks

All numerical conclusions below follow from the supplied toy assumptions. Research proposals are hypotheses, not evidence of realized returns.

## E01 — Signal and executable price

Let I denote the same public information, including the quote. The relevant likelihood ratio is 0.60/0.40 = 1.5, not the advertised unconditional ratio of 4. Bayes’ rule gives:

P(Y=1 | I, positive) = (0.58 × 0.60)/(0.58 × 0.60 + 0.42 × 0.40) = 0.6744186.

Buying costs 0.69 + 0.01 = 0.70. Expected net payoff is 0.6744186 − 0.70 = **−0.0255814 per contract**. Passing earns zero, so **pass**. The break-even executable purchase price before the additional cost is **0.6644186**. The already-paid sensor fee is sunk and does not enter this decision.

The three analysts provide no additional independent observation. Their paraphrases must not be multiplied as three likelihood updates. They might help check interpretation or arithmetic, but add no specified statistical evidence about Y.

Investigate a second, separately collected observation W with a timestamped prospective sample. Estimate whether W predicts Y conditional on I and Z, rather than merely reproducing Z. Compare held-out calibration and executable net value with and without W at the actual decision time, including its acquisition costs and delay. A positive result would justify a genuinely incremental update; independence need not be assumed.

## E02 — Where the risk lands

After the new fee, A pays (−14,+12), and B pays (+12,−14). Both have standalone expected net payoff **−1**: half the sum of their two payoffs. Before that fee, each expectation was +1.

| Action | Terminal wealth: stress, ordinary | Expected log wealth | Increment over existing portfolio |
|---|---:|---:|---:|
| Do nothing | (40,100) | 4.147025 | 0 |
| Add A | (26,112) | 3.988298 | −0.158727 |
| Add B | (52,86) | 4.202796 | +0.055771 |

For example, B’s increment is 0.5 ln[(52 × 86)/(40 × 100)] = 0.055771. **Choose one unit of B**, which maximizes expected log utility among the stated choices despite its negative standalone expectation.

The two additions have the same marginal payoff distribution, but their association with existing wealth differs. B pays in the desk’s low-wealth state; A worsens it. With log utility, a dollar has greater marginal value when wealth is low. B transfers resources toward that state sufficiently to justify its fee.

This establishes portfolio-specific insurance value under the mandate. It does not establish superior information, mispricing, or a positive expected trading profit. A’s pattern resembles absorbing stress risk, but these assumptions do not establish that its offered compensation is adequate or that the desk should warehouse it. B instead reduces the desk’s existing stress exposure; its counterparty’s motives and portfolio remain unspecified.

## E03 — Related contracts and a repaired bundle

The original A+B bundle is **not** guaranteed profitable. If the preliminary value is 99 and the final revised value is 101, A pays zero and B pays zero. Net payoff is **−0.94 − 0.02 = −0.96**. Both values equaling 100 is another losing state because both inequalities are strict. Preliminary and final values are also different settlement variables, so apparent opposite directions do not create complements.

For repaired A+C, exactly one contract pays one for every preliminary value: A covers values above 100; C covers values at or below 100, including equality. All-in cost is 0.44 + 0.48 + 0.02 = **0.94 per pair**. Guaranteed settlement profit is therefore **0.06 per pair**.

Atomic capacity is min(100,20) = **20 pairs**. Maximum guaranteed profit is **20 × 0.06 = 1.20**, with an initial outlay of 18.80 and settlement receipts of 20. The remaining A capacity cannot form another guaranteed bundle at the supplied C capacity.

The conclusion depends on exhaustive, mutually exclusive payoff conditions using exactly the same preliminary value; certain, identical relevant settlement and counterparty terms; simultaneous execution at the stated prices and capacity; fees of 0.02 per pair; zero-cost financing through settlement; and no omitted obligations or costs. These are expressly supplied assumptions, not claims about a real venue.

## E04 — Two research candidates for a small desk

Both candidates begin as historical and shadow research. The existing timing engine exclusively authorizes entries at its first eligible closed hourly bar. Signal modules may supply estimates but may not accelerate entries. Capital, impact, depth, and any borrow availability or cost must be measured; no dollar capacity or return is presumed.

### Candidate 1: independent factual changes propagated through public holdings

**Marginal participant:** Investors who update slowly when a release contains economically conflicting clauses or when its implications reach securities through disclosed holdings. Their existence and exploitable delay are hypotheses.

**Mechanism:** Extract changes in factual claims from earnings/news releases relative to prior available releases. Group syndicated copies by source lineage so repetition does not masquerade as confirmation. Combine genuinely distinct factual changes, publicly known holdings exposures, and the current quote to predict the residual price response after the hourly entry gate. The bold hypothesis is that causal exposure mapping and contradiction resolution retain useful information after direct price reactions.

**As-of signal:** A frozen release corpus and source graph available before each gate; holdings with their actual publication timestamps, rather than retroactively known holdings dates; current quotes/depth; and a model trained only on earlier outcomes. Its output is expected post-entry return conditional on the contemporaneous quote and common price movement.

**Action and exit hypothesis:** In shadow mode, buy positive residual predictions or model short positions only where borrow can eventually be verified. Enter exclusively through the timing engine. Test a prespecified four-hour holding horizon and a separately predefined invalidation rule based on a new contradictory release; do not choose exits after seeing outcomes.

**Persistence/capacity reason:** Repeated interpretation work across many disclosed relationships might be costly for participants. Capacity is limited by exposed instruments’ executable depth and the fraction of information still unpriced after an hour; neither is measured yet.

**Bad state:** An apparently favorable clause is offset by a financing or demand deterioration elsewhere in the release; stale holdings map the news to the wrong instrument. The signal then loads into correlated adverse moves.

**Strongest rival:** A simple quote/momentum/exposure model explains everything, with interpretation adding only a narrative after prices have adjusted.

**Decisive first experiment:** Run a time-ordered, issuer/event-clustered held-out comparison of the quote-only baseline against the lineage-and-exposure model at identical hourly gates and exits. Deduplicate related releases across folds. Require incremental predictive value and positive net value under conservative executable cost estimates, with sensitivity to unobserved fills; reject if the gain vanishes after quote conditioning or lineage deduplication.

### Candidate 2: temporary inventory for publicly announced rebalance demand

**Payer:** Benchmark-constrained funds that may rationally pay for timely execution around an announced rebalance. Their actual orders and quantities are unobserved; announcements identify potential demand, not guaranteed flow.

**Mechanism:** Supply inventory against temporary one-sided pressure: buy deletions from sellers, and potentially sell additions to buyers using verified inventory or borrow. Earn a concession for carrying inventory and adverse-selection risk until pressure subsides. Do not infer dealer positions from the announcement.

**As-of signal:** Previous-day public rebalance announcements, published implementation details and weight changes where available, holdings as then publicly known, and quotes/depth showing price concessions relative to a prespecified matched reference. The desk’s logs estimate its execution experience, with explicit adjustment for selection in which orders it previously attempted.

**Action and exit hypothesis:** At the first engine-authorized hourly bar, shadow an inventory acquisition opposite the announced demand only if an estimated concession covers measured costs and risk. Predefine exit at the first eligible hourly gate after implementation plus a fixed maximum holding period. Bound inventory using measured capital, liquidity and borrow constraints before proposing any live version.

**Persistence/capacity reason:** Some investors value benchmark tracking and execution certainty more than the concession. Inventory providers must absorb uncertain flow and losses during stressed markets. Available capacity is finite and event-specific.

**Bad state:** The deletion reflects durable deterioration, pressure continues beyond implementation, or available liquidity disappears while borrowed inventory becomes expensive or unavailable.

**Strongest rival:** Rebalance announcements reveal permanent valuation changes, while competing arbitrageurs already capture any temporary concession before this desk’s hourly gate.

**Decisive first experiment:** Conduct a matched event study of signed concessions and subsequent reversals at permissible entry times, separating announcement and implementation periods. Compare affected names with prespecified matched controls, and then replay only achievable sizes using historical depth and conservative fill assumptions informed by own logs. A reversal in midpoint prices without realizable net proceeds fails the test.

**Contrarian alternative:** Even if delayed interpretation or compelled rebalance trading exists, providing liquidity may be unattractive. Crowded anticipation can eliminate concessions by the hourly gate, while rare non-reversals concentrate losses precisely when capital is most valuable. Existing fast specialists may rationally leave only trades whose apparent premium compensates for risks this desk cannot afford.

**First research step:** Build and audit the common as-of event table—publication time, lineage, known holdings, announcement/implementation time, and engine-authorized entry quote. Then prioritize the rebalance event study because its externally dated demand hypothesis offers a particularly concrete first falsification. No real-money action is authorized.

## E05 — What the routing data identify

The older log does not identify the causal advantage of always-A. Route and context are perfectly confounded, and neither route has overlap within the other context. Simulated unchosen fills at displayed touch do not recreate queue priority, fill probability, cancellations, adverse selection, or impact. The stated **22%** is unsupported as a causal policy improvement; its exact denominator is also unspecified.

The randomized pilot has overlap and, under its stipulated assumptions, supports direct policy-value estimates:

- Always-A: 0.5(0.14) + 0.5(0.04) = **0.09**.
- Old rule, P in calm and A in volatile: 0.5(0.10) + 0.5(0.04) = **0.07**.
- Difference: **0.02 per opportunity**, or **28.57%** of the estimated old-rule value.

The improvement comes entirely from switching calm orders: half the target weight times a calm treatment difference of 0.04. Volatile routing stays A. For context, always-P estimates to 0.04; the volatile A−P difference is 0.06.

These are pilot point estimates, not established population guarantees. The given randomization and consistency make them meaningful estimates without relying on synthetic fills. Without reward variances and dependence estimates, we cannot compute a defensible confidence interval, significance level, required sample size, or probability that always-A is truly better. They also do not establish behavior under different context mixtures, market regimes, larger size, or inventory feedback absent from the pilot.

Keep the 50 unresolved outcomes explicitly pending. Do not record them as zero or combine a selectively matured subset with the completed pilot. Report the completed cohort separately; use the newer cohort after its fixed outcome horizon is fully observed, retaining route propensities and inclusion rules. Investigate missing outcomes separately from ordinary delay.

Next, continue a prespecified context-stratified randomized research pilot with event-level rewards and dependence identifiers. Estimate uncertainty, especially for the calm-route difference that drives this policy comparison, and monitor context weights, net costs and temporal drift. Predefine evaluation dates and stopping criteria rather than repeatedly stopping at a favorable estimate.

## E06 — Faster intelligence at finite capacity

For an eligible mode and positive q, write b = a0 exp(−d/4) − 0.01. Profit is bq − 0.0004q² − K, so its unconstrained maximum occurs at q = b/0.0008. Cap this at 60, then compare its profit with skipping, which pays zero without computation cost.

| Mode | Deadline eligible? | Edge after delay | Unconstrained q | Best feasible positive q | Net expected profit |
|---|---|---:|---:|---:|---:|
| SIMPLE | Yes: 1 second | 0.0934561 | 104.320 | 60 | 2.567366 |
| DEEP | No: 3 seconds | — | — | — | Infeasible |
| FAST-DEEP | Yes: 0.25 seconds | 0.1690944 | 198.868 | 60 | 3.105661 |
| Skip | Yes | — | — | 0 | 0 |

At 60 contracts, impact is 0.0004 × 60² = 1.44. SIMPLE earns 60(0.0934561 − 0.01) − 1.44 − 1 = 2.567366. FAST-DEEP earns 60(0.1690944 − 0.01) − 1.44 − 5 = 3.105661.

**Select FAST-DEEP at q = 60**, improving expected profit over SIMPLE by approximately **0.538295**. Modes share capacity; they cannot be stacked. DEEP is excluded by the hard deadline regardless of its economics.

Scaling 10,000-fold is outside the model’s feasible set: 600,000 contracts exceeds capacity 60. Fund wealth does not create executable liquidity. Even without the cap, the supplied quadratic impact grows with the square of size and defeats linear profit extrapolation. Repeated opportunities would require evidence of their number, independence, shared liquidity and capital recycling.

A real deployment experiment must measure signal calibration and its decay with end-to-end latency; deadline misses and fallback behavior; actual computation expense; fill probability, spread, fees, depth and impact versus size; information leakage and adverse selection; dependence across concurrent opportunities and modes; inventory and financing needs; and downside outcomes. Begin with shadow operation using the same decision timestamps, followed only with separate authorization by a bounded randomized execution pilot to measure real fills and impact. The toy optimum is exact within its assumptions, not an empirical sizing recommendation.
