# Turn the two-part insight into decisions

## Contents

1. What this procedure must demonstrate
2. Information advantage conditional on the market
3. Price the warehouse for this portfolio
4. Construct an opportunity instead of decorating a signal
5. Compile contract relationships conservatively
6. Make the LLM's contribution observable
7. Master research procedure

This reference translates the original post into explicit work products. It extends the foundations and adaptive-control references; it does not replace their chronology, execution, evidence or portfolio constraints. Equations and examples below are declared finite-model derivations, not measured market results. The companion [frontier source register](frontier-sources.md) distinguishes established results, new preprints and proposed applications. Information sections connect IF01–IF06 to the earlier Blackwell/Sims foundations; reservation pricing uses WR01–WR07; invention and contract compilation use F01–F06. These sources motivate the procedures without proving trading profitability.

## 1. What this procedure must demonstrate

Keep four levels separate: **instructions are present; behavior is observed; an economic advantage is identified; the advantage is captured in a deployable policy**. A correct instruction does not prove adherence. A correct hypothetical answer does not establish a tradable edge. A prompt conditions an LLM through supplied context; saving it does not retrain the model's parameters.

For a proposed strategy, produce a compact decision record:

- **Transfer:** who wants information, immediacy, insurance, funding, inventory or a different payoff; what observable constraint or belief difference creates the demand.
- **Comparison:** whose feasible decision or executable quote is the baseline, at what time, size, horizon and cost.
- **Mechanism:** information, paid risk/service, access/constraint, or an unresolved empirical pattern; identify interactions rather than adding overlapping labels as separate profit terms.
- **Calculation:** an estimand or actual scenario calculation that connects the advantage to a net payoff or portfolio utility change.
- **Experiment:** data availability, a feasible comparator, a rival explanation, a falsifier and the next action that can change the decision.

Do not require certainty before researching a candidate. When measurements are missing, deliver a concrete hypothesis and experiment, keeping its evidence status explicit. Creative generation and adversarial rejection are separate steps; neither should extinguish the other.

## 2. Information advantage conditional on the market

Define Z as public information and the contemporaneous executable market state, S as the proposed extra signal, Y as the contract outcome, and A as the feasible actions. Compare a price-aware baseline using Z with the same model family augmented by S. Match capacity, costs, fitting budget and chronology. Test incremental decision value, not merely raw correlation with Y. A quote is an informative feature and trading constraint; it is not automatically the physical probability of Y.

Write the Bayesian update conditionally:

\[
\frac{P(Y=1\mid Z,S)}{P(Y=0\mid Z,S)}=
\frac{P(Y=1\mid Z)}{P(Y=0\mid Z)}
\frac{P(S\mid Y=1,Z)}{P(S\mid Y=0,Z)}.
\]

Do not insert a raw unconditional likelihood ratio after price has already incorporated that evidence. Estimate or explicitly assume the conditional terms. Record which observations share an upstream source, and retain uncertain lineage rather than declaring independence. Conditional independence of Y and S given Z rules out extra information about Y in that specified model; it does not rule out value for predicting fills, costs or a different horizon.

For a finite experiment with joint probabilities J(s,y), state probabilities p(y)=sum_s J(s,y), and fixed net action utilities u(a,y), compute:

\[
V_0=\max_a\sum_y p(y)u(a,y),\qquad
V_S=\sum_s\max_a\sum_y J(s,y)u(a,y).
\]

The inner sums are unnormalized; zero-probability signals contribute zero. Free optional information with the identical action menu cannot reduce the exact optimum. Acquisition cost, latency, altered prices, mandatory disclosure, or changed feasible actions break that simplified comparison and must enter the actual decision model. Forecast score improvement alone is insufficient.

Test the information unit that the economic mechanism requires. Two individually useless observations can be jointly useful: if independent fair bits X1 and X2 determine Y=X1 XOR X2, neither bit alone forecasts Y, while the pair does. Conversely, ten summaries of one disclosure do not supply ten experiments. Preserve structured evidence and complementary raw features through agent handoffs; averaging final answers can destroy information that only a joint model can use. Do not infer synergy from a searched profitable interaction without prospective confirmation.

Use economic decision regions to evaluate calibration: buy, sell, hold, route, size, and quote-age regions defined without their future outcomes. Maintain broad proper-score and calibration checks too; selectively choosing regions after seeing results creates another research search. Evaluate forecast error, net policy regret relative to feasible comparators, and actual executable returns as distinct quantities.

## 3. Price the warehouse for this portfolio

Replace 'I can tolerate volatility' with a reservation-price problem. Specify the liability L, existing state-dependent endowment W, allowed hedges, funding path, objective U, and the numeraire/timing of premium pi. With a fixed hedge set and terminal cash units, the minimum acceptable seller premium satisfies:

\[
E[U(W+\pi-L)]\ge E[U(W)].
\]

For exponential utility U(w)=-exp(-gamma*w), gamma>0, and finite supplied scenarios, the equality gives:

\[
\pi_{\mathrm{sell}}=
\frac{\log E[e^{-\gamma(W-L)}]-\log E[e^{-\gamma W}]}{\gamma}.
\]

This depends on the joint distribution of W and L, not only the liability's variance. Gamma and probabilities are inputs, not facts to invent. Constant absolute risk aversion is a useful transparent illustration, not a universal desk objective. Reoptimizing hedges requires solving both the incumbent and candidate with the same hedge rights; otherwise the comparison confounds the liability with extra opportunities.

For small liability size q, the marginal price under differentiable expected utility is E[U'(W)L]/E[U'(W)] when the premium is a constant terminal cash addition. Losses when marginal capital is valuable require more compensation. This is a portfolio-specific marginal valuation, not automatically the market's unique pricing kernel.

Compute terminal utility and path feasibility separately. A utility-acceptable liability can fail because of interim margin, trapped collateral, a borrow recall or forced liquidation. Price at executable size: model what happens to premium, hedge liquidity, capital occupation and payer demand as the position grows. Better stress capacity can be an advantage, but no amount of confidence supplies missing cash.

Identify the opposing party's reservation value where evidence permits. A trade can benefit both parties because their endowments, obligations, information or feasible actions differ. Do not assume every payer is uninformed. Test substitution: a different intermediary, auction design or hedge instrument can remove the premium even while the original demand grows.

## 4. Construct an opportunity instead of decorating a signal

For CREATE or a broad improvement request, generate a small diverse candidate set before ranking. Include an information candidate, a risk/service candidate and a constraint or contract candidate when the available mandate permits. Include one unconventional alternative to the user's initial explanation. These are competing research hypotheses, not simultaneous live deployments.

Use these transformation operators:

| Change one element | Constructive question | Required discriminator |
| --- | --- | --- |
| Information partition | Does joint evidence resolve a state that individual summaries conceal? | Incremental value beyond price-aware baseline; redundant-source and permutation controls |
| Counterparty constraint | Who must act at a known time, and who can now substitute for us? | Flow conditional on the constraint, versus contemporaneous news and competing capital |
| Portfolio endowment | Is a burden expensive for the payer and cheaper for this portfolio? | Joint-state reservation value plus funding path, compared with simply reducing exposure |
| Contract representation | Do exact settlement relationships reveal a cheaper attainable payoff? | Independently audited feasible-state table, executable legs and completion path |
| Action or timing | Can waiting, routing or changing size preserve more of an existing advantage? | Same-signal matched policy comparison including missed fills and decay |
| Scale or service | Is a small opportunity unattractive to larger competitors but valuable here? | Net surplus versus deployed size and fixed operating cost; no linear scale extrapolation |

For every surviving candidate write observable input -> expected market consequence -> executable action -> complete payoff -> falsifier. Name the data acquisition step, first calculation and cheapest decisive experiment. State why this desk could capture the opportunity and the reason competitors might not. 'Complex', 'alternative data', 'AI' and 'contrarian' are descriptions, not explanations of persistence.

Rank candidates separately by potential economic value and value of the next experiment. A bold low-evidence idea can merit inexpensive research; it does not thereby merit a position. Avoid a universal numerical novelty score. Novel combinations are proposed synthesis unless a literature search supports a stronger novelty claim.

## 5. Compile contract relationships conservatively

Represent exact payout rules before reasoning about headline correlations. Preserve the measurement source, time zone, cutoff, strict/inclusive threshold, revision policy, void state, settlement currency and payment timing. An LLM may propose a relationship; admission to the feasible-state model requires independently checked contractual evidence.

Enumerate or constrain all admissible settlement states. An incorrect restriction can manufacture a guarantee by removing a losing state. A conservative superset of states can miss a real opportunity but avoids that particular false guarantee, provided costs and execution are also conservative. Keep unknown relationships unknown.

For supplied state payoffs X and signed holdings h, inspect every modeled terminal payoff Xh and the actual bid/ask/depth-dependent acquisition cost. Distinguish strictly positive profit in every modeled state from standard arbitrage: nonpositive initial net cost, nonnegative terminal net payoff almost surely and a positive benefit with positive probability, with financeable obligations. A convex-hull test for strong sure profit under unrestricted single-price trading is not a universal no-arbitrage certificate. A zero-priced binary payoff can lie on the hull boundary while offering nonnegative payoff and positive benefit in a possible state.

Searching only a subset of adverse states gives an optimistic bound on a maximin guarantee. Require a valid worst-case oracle or certified lower bound for the proposed portfolio across the complete admissible model; a feasible iterate, timeout or missing state is not proof.

Treat a payoff certificate as conditional on its state and contract model. Verify feasible shorting, fees, funding, counterparty performance and leg completion separately. Passing a supplied-state numerical check neither validates semantics nor establishes a live executable trade.

## 6. Make the LLM's contribution observable

Require the model to produce the decision record and calculation, not merely repeat the two categories. Use deterministic calculation for finite examples and a trace from each claimed edge to data or an explicit assumption. Separate a schema-complete answer from a factually or economically correct answer.

Evaluate on fresh tasks with a frozen rubric and no access to intended answers. Include arithmetic, wrong-state risk, redundant information, missing joint information, false contract relationships, identification failures, and constructive invention. Compare matched tasks with and without the new instructions when feasible. Retain all outputs and failures; report counts, model/context setup and evaluator limits. Small qualitative comparisons are diagnostic, not causal proof of general improvement or trading performance.

Use metamorphic checks where appropriate: changing dollars to cents should preserve the economic decision after every unit is converted; permuting state order should preserve value; relabeling the same source should not multiply evidence; moving a liability into the portfolio's bad state should change its reservation value; adding an admissible losing state should invalidate a supposed guarantee. Conditions and objectives must remain consistent in each transformation.

## 7. Master research procedure

1. Freeze the incumbent, mandate, as-of information, economic objective and eligible opportunity population.
2. Trace the information advantage or paid burden to a specific marginal participant and feasible action.
3. Generate a small diverse candidate set using the transformation operators; preserve rival explanations.
4. Calculate incremental information value, portfolio reservation value or contract payoff restrictions as appropriate; distinguish supplied-model calculations from identified estimates.
5. Model executable capture, costs, latency, scale, state dependence and path funding. Reject arithmetic or semantic contradictions; keep unresolved candidates as research.
6. Choose the next experiment by its ability to change a consequential decision within the research budget. Fit and evaluate the entire selection/adaptation policy chronologically.
7. Promote only according to the evidence stage. Feed approved candidates to the existing adaptive controller; maintain its separate recovery policy and three clocks.
8. Log predictions, rejected opportunities, actual/simulated provenance and mature outcomes. Diagnose which economic, statistical or execution link changed before redesigning it.

The output is a strategy-specific, falsifiable economic design and evidence record. The numerical companion checks supplied finite models; the existing arbiter chooses among supplied actions. Neither supplies missing market facts or creates an advantage by naming it.


## Numerical companion

`../scripts/edge_mechanics.py` contains three pure finite-model functions: `finite_value_of_information(joint_probabilities, action_utilities)`, `seller_reservation_premium(probabilities, wealth, liabilities, gamma)`, and `finite_payoff_check(payoffs, quantities, initial_cost, probabilities=None)`. The first holds actions/prices/horizon fixed; the second holds additional hedging fixed; the third checks only supplied payoff states and explicit cash/financing legs. None infers inputs or validates external facts. Use the separate adaptive arbiter for supplied-action selection and reserve external execution to an authorized lifecycle manager.
