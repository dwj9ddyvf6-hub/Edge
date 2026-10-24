# E01 — Signal and executable price

**Pass at this quote.** The relevant likelihood ratio is conditional on the same public information as the prior: 0.60/0.40 = 1.5. Bayes' rule gives

\[
p=\frac{0.58(0.60)}{0.58(0.60)+0.42(0.40)}
=\frac{0.348}{0.516}=0.6744186.
\]

Net expected payoff is 0.6744186 − 0.69 − 0.01 = **−0.0255814 per contract**, versus zero for passing. The break-even purchase price, before the additional cost, is **0.6644186**. The already-paid sensor fee is sunk.

The advertised unconditional likelihood ratio of 4 cannot replace the supplied conditional ratio: it can count information already reflected in the public prior and quote. Three paraphrases of the same observation add no independent evidence and cannot justify multiplying likelihood ratios. They might improve interpretation or error checking, but the stated model already specifies what this observation means.

Investigate a second sensor measuring a different underlying feature. Collect timestamped observations and outcomes, then test whether it improves held-out conditional prediction **given public information, the quote, and the first sensor**. Estimate its joint dependence rather than assume independence, and evaluate improvements at executable prices after its incremental acquisition and trading costs.

# E02 — Where the risk lands

Both original contracts have expected net payoff (−12 + 14)/2 = 1. The new fee reduces each addition's standalone expectation to **−1**. Their identical marginal distributions conceal different relationships to existing wealth.

Baseline expected utility is

\[
U_0=\tfrac12\log40+\tfrac12\log100=4.1470248.
\]

| Action | Net addition, stress/ordinary | Terminal wealth | Expected log utility | Increment over baseline |
|---|---|---|---:|---:|
| Nothing | (0, 0) | (40, 100) | 4.1470248 | 0 |
| A | (−14, +12) | (26, 112) | 3.9882977 | −0.1587271 |
| B | (+12, −14) | (52, 86) | 4.2027955 | +0.0557707 |

For example, B's utility increment is ½ log[(52×86)/(40×100)] = ½ log(1.118). **Choose one unit of B under the stated expected-log-utility mandate.**

B supplies wealth when the desk has less and marginal utility is greater. A worsens that exposure. This is portfolio insurance value, despite B's negative expected standalone payoff; it is not evidence of superior information or positive expected trading alpha. The calculation identifies the desk's preferred risk transfer. It does not establish who pays whom to warehouse risk in an actual market, why the quoted premiums arise, or whether an intermediary earns adequate compensation. At these assumptions this desk is willing to pay expected wealth for B's protection.

# E03 — Related contracts and a repaired bundle

**A+B is not guaranteed profitable.** Suppose the preliminary close is 99 and the final revised close is 101. Neither contract pays, so the net payoff is **−(0.94 + 0.02) = −0.96**. Preliminary and final values both equal to 100 also produce zero payout. The different observation definitions and strict inequalities defeat the proposed complementarity.

For the repaired pair, let x be the same preliminary official value:

\[
1\{x>100\}+1\{x\le100\}=1.
\]

Every pair costs 0.44 + 0.48 + 0.02 = **0.94**, pays exactly 1, and earns **0.06 guaranteed profit**. Capacity is min(100,20) = **20 pairs**, yielding **1.20 maximum guaranteed profit**, with total initial outlay 18.80 and settlement receipts of 20.

This toy conclusion relies on the common reference value, exhaustive and mutually exclusive settlement events including equality, certain identical settlement/counterparty terms, atomic execution at the supplied prices, full stated capacity, and zero financing cost through settlement. Buying more unmatched A does not extend the guarantee. Outside these assumptions, execution, settlement, or financing uncertainty would need evaluation.

# E04 — Two research candidates

These are hypotheses for paper research, not measured profitable strategies. Both submit candidate signals to the existing timing engine; **only that engine authorizes entries at the first eligible closed hourly bar**. Neither research module changes entry timing. Actual quotes at that permitted entry determine feasibility. Position sizes remain unset until capital, borrow, and impact are measured.

**Candidate 1: Trace a new primary-source fact through explicitly documented business relationships.**

- **Marginal participant and mechanism:** Investors may absorb a company's earnings headline before tracing a specific new demand or cost fact to another company. The hypothesis is delayed cross-company inference. A counterparty need not be irrational; processing costs, mandates, or disagreement may explain its trade.
- **As-of signal:** Deduplicate news by source lineage. Use only releases available before the decision and relationships explicitly documented in earlier public releases. Identify a genuinely new fact, its plausible signed implication for a related company, and whether that implication adds information beyond contemporaneous quotes and depth. A later relationship discovery cannot enter an earlier signal.
- **Action and exit:** Paper-buy a related company after a positive implication, or paper-short after a negative implication only once borrow feasibility is measured, at the engine-permitted entry. Preregister an exit four closed hourly bars later, with a separately specified exit on explicit factual invalidation. This horizon is an experimental choice.
- **Persistence and capacity:** Sparse, difficult-to-map relationships may be costly to interpret repeatedly; widely followed relationships may offer none. Capacity is limited by depth, correlated exposures, and how quickly the interpretation becomes common knowledge.
- **Bad state:** A positive customer announcement instead reflects supplier substitution, margin compression, or demand pulled forward; the inferred beneficiary falls. General market exposure can also masquerade as successful inference.
- **Strongest rival:** The quote already incorporates the fact, or the relationship is stale and economically immaterial. Any apparent predictability may disappear by the allowed hourly entry.
- **Decisive first experiment:** Freeze a lineage-clean event sample and public relationship map as of each date. In a chronological held-out period, compare a quote/depth baseline with the same model plus the inferred fact, grouping uncertainty by underlying event. Test incremental prediction and paper returns at the permitted bar, net of measured execution costs. Ablate duplicate headlines and relationship features. Reject if the feature adds no held-out value or its value disappears at executable entry.

**Candidate 2: Supply inventory against temporary index-rebalance pressure.**

- **Payer and mechanism:** Index trackers may rationally accept execution concessions to meet tracking objectives around a rebalance. The desk hypothesizes compensation for holding inventory while that concentrated demand passes. Publicly known holdings suggest exposure; they do not reveal actual orders, dealer inventories, or compelled flows.
- **As-of signal:** Start with announcements published the previous day and holdings available then. At engine-eligible decision times, look for a predeclared quote/depth dislocation in the direction suggested by additions or deletions. Normalize against contemporaneous common price moves. Treat projected demand as uncertain rather than known volume.
- **Action and exit:** Paper-buy deletion-related selling pressure and, where measured borrow permits, paper-short addition-related buying pressure. Supply passive liquidity only through orders released at the engine's authorized entry. Exit on a preregistered partial reversal of the observed dislocation or after two trading sessions, whichever comes first. Use conservative execution bounds until fills can be identified credibly.
- **Persistence and capacity:** Calendar concentration and tracking constraints can recur. Compensation depends on scarce balance sheet and willingness to bear inventory risk; competitors, spread compression, correlated rebalances, and shallow depth constrain capacity.
- **Bad state:** The index change coincides with lasting fundamental deterioration or durable demand, so the supposed temporary displacement continues. Adverse selection, failed borrow, and persistent exposure can overwhelm spread income.
- **Strongest rival:** Announcements let other traders pre-position, leaving no concession at the hourly entry. Alternatively, the move is permanent repricing rather than inventory pressure.
- **Decisive first experiment:** Reconstruct announcement-known events and matched non-events with comparable contemporaneous market moves and liquidity. Test whether eligible-bar dislocations reverse unusually after the rebalance, and whether that relationship survives measured costs and conservative queue/fill assumptions. Use the desk's logs to calibrate execution uncertainty; displayed touch alone is not an executable passive counterfactual. Reject if reversals are absent, predate permitted entry, or cannot cover costs under credible fills.

**Contrarian alternative:** Even if slow inference and deadline-driven demand exist, informed competitors may exploit them sooner, while the remaining opportunities are precisely the dangerous inventory states. Research may then favor reducing exposure around those events or improving execution of existing orders rather than opening positions.

**First research step:** Build one point-in-time, source-lineage event table joined to quotes/depth and the timing engine's actual eligible entry timestamps. Run Candidate 1's incremental-information ablation first: it directly tests whether useful information remains after the mandatory delay. Keep Candidate 2 in research until inventory, borrow, and fill uncertainty are bounded. No real-money execution is authorized.

# E05 — What the routing data identify

The older log does **not identify** the claimed 22% causal improvement. Route and context were perfectly confounded: there was no calm-A or volatile-P support. Simulated fills at displayed touch do not recover missing outcomes, queue priority, adverse selection, or execution costs. The denominator and uncertainty behind “22% better” are also unspecified.

The randomized, completed pilot supplies overlap and comparable mature rewards. With equal target context weights:

\[
V(\text{always A})=\tfrac12(0.14)+\tfrac12(0.04)=\mathbf{0.09},
\]
\[
V(\text{old rule})=\tfrac12(0.10)+\tfrac12(0.04)=\mathbf{0.07}.
\]

The estimated improvement is **0.02 net reward per opportunity**. Relative to the old rule it is about **28.57%**, not 22%; the absolute difference is the clearer primary result. The policies differ only in calm contexts, where A−P = 0.04. In volatile contexts both policies choose A; the pilot's separate A−P contrast there is 0.06.

Given randomization, consistency, exogenous contexts, and no effects on future inventory or contexts, these are valid point estimates for the stated target mixture. They favor always-A within this pilot, but no variances or dependence estimates are available, so statistical significance, confidence intervals, and a reliably positive population advantage cannot be computed. The toy result does not establish performance at other sizes, context mixtures, horizons, or market regimes.

Keep the 50 unresolved outcomes marked pending, with assignment and context preserved. Do not assign zero rewards, cherry-pick resolved winners, or combine them with mature outcomes as though comparable. Wait for the same fixed horizon and apply a predefined missing-data policy if some never mature.

Next, recover individual mature pilot rewards and event grouping, then continue a preregistered paper or simulated randomized comparison within contexts, reporting fixed-horizon net rewards, fill failures, uncertainty, and context drift. Estimate dependence-aware uncertainty when the data support it. Any later live experiment requires its own authorization. If routing affects future inventory in deployment, evaluate complete inventory-aware policies rather than extrapolate this one-step estimand.

# E06 — Faster intelligence at finite capacity

For a feasible mode and positive q, define b = a0 exp(−d/4) − 0.01. Profit is bq − 0.0004q² − K. Its unconstrained maximizer is q* = b/0.0008, clipped to [0,60]; then compare the result with skipping at zero cost.

| Mode | Deadline feasible? | Decayed gross edge | Unconstrained q* | Best permitted positive q | Net expected profit |
|---|---|---:|---:|---:|---:|
| SIMPLE | Yes: 1 second | 0.0934561 | 104.3201 | 60 | 2.5673656 |
| DEEP | No: 3 seconds | 0.0850260 | 93.7825 | Infeasible | Infeasible |
| FAST-DEEP | Yes: 0.25 second | 0.1690944 | 198.8679 | 60 | 3.1056611 |
| Skip | Yes | — | — | 0 | 0 |

At q = 60, impact is 0.0004×60² = 1.44. Thus SIMPLE earns 60(0.0934561−0.01)−1.44−1 = 2.5673656, while FAST-DEEP earns 60(0.1690944−0.01)−1.44−5 = 3.1056611. **Select FAST-DEEP at 60 contracts**, an advantage of about 0.5383 per opportunity. DEEP cannot be selected regardless of its hypothetical profit; shared capacity prevents stacking modes.

Scaling this position 10,000-fold to 600,000 contracts violates the model's 60-contract limit. Fund wealth does not create executable capacity, and quadratic impact also prevents linear profit scaling. Applying the quadratic formula outside its domain would not be a valid forecast. Nor are 10,000 independent equivalent opportunities established.

A real paper deployment experiment should measure incremental calibrated signal quality, edge decay at actual decision/execution delays, latency tails and deadline misses, computation charges, executable depth, fill probability, spread/slippage, size-dependent impact, borrowing/funding/collateral needs where relevant, and opportunity overlap or competition. Compare complete mode-and-size policies on matched or randomized eligible opportunities, include failed attempts and costs, and estimate net-profit uncertainty and capacity before any authorized live sizing. The numerical winner above is solely a consequence of the supplied toy assumptions.
