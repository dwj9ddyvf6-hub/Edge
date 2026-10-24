# Trading Edge Lab v3: from the edge thesis to observable decisions

Research and development: 24 October 2026, America/New_York.

The original post identifies two sources of advantage: better use of information and accepting risks that other participants will pay to transfer. Trading Edge Lab already contained both, with requirements for conditional Bayesian updates, executable prices, adverse selection, marginal participants, capital and bad-state exposure. This pass asks a harder question: what calculations, candidate designs and observable behavior should those instructions produce?

The result is a deeper operating procedure, a revised single-file prompt, an updated skill, three numerical tools and a recorded behavioral comparison. The main contribution is a more explicit bridge from an economic idea to a decision and experiment. It is not a claim that a prompt can make every strategy profitable.

## 1. What was present, and what needed work

The [behavioral audit](research/behavior.md) maps each part of the screenshot to the original skill and references. It distinguishes four achievements:

| Level | What establishes it | Status of this work |
| --- | --- | --- |
| Instructions exist | Read the actual artifact and its dependencies | The two mechanisms are explicit; v3 adds required calculations and outputs |
| A model uses them | Fresh tasks, preserved outputs and a declared rubric | Evaluated in a small controlled comparison; see the run report |
| An economic advantage exists | Identified data, executable prices, costs, valid comparisons and prospective evidence | Must be established for each strategy |
| A desk captures the advantage | Implemented data/execution/risk lifecycle and observed operation | The included kernels are offline references |

Loading a skill provides procedural context. It does not itself change the model's learned parameters. The practical goal is to make the desired behavior explicit, calculable and testable, while retaining the model's ability to propose useful new hypotheses.

## 2. Information is valuable relative to a decision

The most useful additional question is: **What does this observation change after conditioning on the information already available at the executable quote?** A good predictor may add nothing beyond price. A genuinely new observation may arrive too late. A more accurate forecast may leave the feasible action unchanged.

Let Z be the public/market context, S the additional observation and Y the contract outcome. The relevant update is conditional on Z:

\[
O(Y=1\mid Z,S)=O(Y=1\mid Z)
\frac{P(S\mid Y=1,Z)}{P(S\mid Y=0,Z)}.
\]

The quote belongs in the decision context; it is not automatically a physical-probability prior. Repeated interpretations of the same evidence do not multiply its likelihood ratio. The skill now asks for source lineage, a price/context-only comparator and a test of incremental decision value.

For a finite joint signal/state distribution J(s,y) and common action utilities u(a,y), the numerical companion evaluates:

\[
V_0=\max_a\sum_y p(y)u(a,y),\qquad
V_S=\sum_s\max_a\sum_y J(s,y)u(a,y).
\]

The gross value V_S−V_0 is nonnegative when information is free, optional and the same actions and prices remain available. That mathematical property does not survive unchanged when obtaining information consumes the quote, changes the opportunity or imposes costs.

Three further distinctions matter:

- **Complementarity:** two individually useless signals may jointly reveal an outcome. The supplied XOR example tests this directly. A process that discards each feature on a standalone score can lose the useful pair.
- **Selected decisions:** aggregate calibration may conceal bad forecasts in the region actually traded. Define relevant cohorts before seeing their outcomes, while retaining broad scoring checks.
- **Agent communication:** a summary or final probability can omit the facts needed for a joint decision. Compare a source-preserving relay with a single model receiving the same evidence at a comparable resource budget.

The [information memo](research/information.md) connects these procedures to unique information, channel deficiency, rational inattention, decision-conditioned prediction and 2026 work on calibration and networked learning. The guarantees in those papers are limited to their specified statistical models. Their application here is a research design, not a theorem about arbitrary LLM conversations.

## 3. A warehouse needs a reservation price

Risk bearing becomes economically precise when the desk computes the price at which a defined liability improves its existing portfolio. Let W be state-dependent terminal wealth, L a liability, pi a deterministic terminal premium and U the declared utility. With other trading opportunities fixed, the seller's indifference price solves:

\[
E[U(W+\pi-L)]=E[U(W)].
\]

For the illustrative exponential utility U(w)=−exp(−gamma*w), gamma>0:

\[
\pi^*=\frac{\log E[e^{-\gamma(W-L)}]-\log E[e^{-\gamma W}]}{\gamma}.
\]

The calculation uses the joint relationship between W and L. It does not price the new sleeve in isolation. Probability, utility and hedge assumptions remain explicit inputs.

**Constructed example.** Two states are equally probable. Existing wealth is (100,20), gamma=.05, with zero interest, no fees, no additional hedging and no interim funding requirements.

| Liability | State 1 loss | State 2 loss | Expected loss | Variance | Minimum premium |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 20 | 0 | 10 | 100 | 0.608748 |
| B | 0 | 20 | 10 | 100 | 19.771308 |

At premium 12, each has standalone expected profit 2. Only A improves the stated seller's expected utility. A different participant with opposite existing wealth can value the protection enough to pay that premium willingly. This is a concrete source of mutually beneficial risk transfer without an assumption that one side is foolish or has a better directional forecast.

The [risk memo](research/risk.md) derives the buyer's corresponding value and connects the procedure to utility-based pricing, market making and intermediary capital. The skill separately requires cash and collateral by account and deadline. A terminal offset does not pay an interim margin call when the offsetting gain is trapped elsewhere.

## 4. Contrarian research changes the competition story

Two apparent shortcuts fail: growing demand does not necessarily enlarge the available premium, and a public event does not necessarily eliminate it. Net obligations and the supply of competing balance sheets determine the opportunity.

The source search deliberately included evidence that challenges attractive stories. The index-effect research examines offsetting migrations and changing absorption. Recent Treasury auction work examines nondealer participation rather than assuming issuance growth mechanically increases dealer compensation. These are reasons to test the proposed payer and substitute providers, not reasons to declare all forced-flow strategies dead.

The resulting instruction is constructive: identify the public or otherwise available constraint, estimate net flow using information available at entry, compare against a simpler calendar/news explanation, and test whether competing liquidity supply removes the executable surplus. A historical mechanism transported to a new asset, venue or scale needs target-specific evidence about what changed.

## 5. Exact contract meaning can be the scarce resource

A newer research direction combines contract interpretation with payoff geometry and constrained optimization. The October 20, 2026 combinatorial-arbitrage preprint is included as a recent, inspected primary source, with its replay and definition limits retained.

The operational pipeline is:

1. Extract the exact settlement rules and preserve their versions.
2. Propose logical relationships using parsers or an LLM.
3. Independently check each relationship against the rules.
4. Construct an admissible state set, retaining unresolved alternatives.
5. Find a candidate basket and verify its worst-case payoff under that model.
6. Check prices, size, fees, financing, settlement and every reachable partial-fill path.

For example, if an independently verified event D implies event M, YES(M)+NO(D) pays at least one unit. If that implication is merely plausible, a missing state can destroy the conclusion. Researching meaning can therefore be valuable, but semantic confidence is not a financial guarantee.

The distinction between strong sure profit and standard arbitrage is preserved. Under the appropriate frictionless model, prices outside a payoff convex hull admit a strong sure-profit direction. Hull membership alone is not a universal no-arbitrage certificate: a boundary price of zero for a possible positive binary payoff illustrates the difference. Solver bounds, short restrictions, probability support and financing assumptions matter.

## 6. A procedure for invention

The revised skill explicitly generates a small set of candidate transformations. It can change the information partition, counterparty constraint, contract representation, timing, existing exposure, scale or implementation cost. Each candidate must state an observable input, expected consequence, attainable action, full payoff and falsifier.

The research produced the following proposals; none is claimed to be a new discovery or demonstrated alpha:

| Candidate | Proposed advantage | Decisive first test |
| --- | --- | --- |
| Decision-boundary evidence routing | Spend extraction effort where extra evidence can change an attainable action | Same opportunity stream against price-only, fixed-budget and always-deep alternatives |
| Synergy-preserving evidence relay | Preserve complementary facts through specialist handoffs | Matched-cost joint-input model versus conclusion-only and source-preserving messages |
| Settlement-aware implication baskets | Reduce contract-discovery cost for logically related payouts | Audit a frozen contract family, then enumerate exceptions and realistic acquisition paths |
| Migration-adjusted rebalance service | Supply inventory against net, rather than headline, benchmark obligations | Held-out events against gross-flow and announcement-only comparators |
| Capacity-conditioned auction service | Supply temporary inventory when available compensation exceeds full burden | As-of participation/capacity proxies, matched exposure and competing-provider hypotheses |
| Collateral-aware implementation | Preserve an exposure with lower total funding or forced-liquidation cost | Feasible routes under account-level cash deadlines and residual-risk comparison |
| Reusable audited contract compilation | Amortize interpretation cost over small opportunities | Held-out template families; measure cost, semantic errors and executable value together |

The [information](research/information.md), [risk](research/risk.md) and [invention](research/invention.md) memos specify data, timing, bad states and rejection rules. Some proposals overlap; their benefits must not be added as independent return sources.

## 7. The integrated master procedure

The unified prompt now connects research to the existing adaptive runtime:

**Research:** preserve baseline and mandate; trace the information increment or paid burden; construct candidates; calculate the appropriate value or payoff restriction; model capture and funding; choose a decisive experiment; admit approved candidates at the supported evidence stage.

**Execution:** ingest and reconcile; route hard faults to a separate recovery policy; update beliefs under the frozen rule; compare feasible actions; refine only when information is worth its delay and cost; atomically revalidate and reserve; execute only through an authorized lifecycle; journal actual outcomes.

**Learning:** attach outcomes to original versions; keep unresolved labels pending; evaluate identified comparisons; diagnose the changed layer; test a challenger; promote policy changes separately from routine belief updates.

The action set includes productive entry and risk taking when justified, as well as holding, waiting, hedging, reducing and researching. A procedure that always refuses would fail the positive-opportunity challenge cases. A procedure that always trades would fail the economic comparison.

## 8. What was actually evaluated

See [validation.md](validation.md) for numerical tests, the independent precision audit and the exploratory LLM comparison. Six tasks and a 24-item rubric were frozen before the candidate author read the task contents. Two fresh sessions used ordinary reasoning; two used the frozen skill. The same word cap and toy inputs were used. Two independent graders received anonymized responses, with reversed response order in the second pass.

This is a small diagnostic, with shared tasks, one inherited model family, instruction-based isolation and incomplete control of sampling. It cannot estimate a general prompt effect or market performance. If both groups solve the tasks, the correct conclusion is demonstrated reasoning on these cases and no measured advantage for the skill on that benchmark. The archived run report records the actual outcome rather than assuming that longer instructions must win.

## 9. Reuse the work

- Start with the root [Unified Master Prompt](../Trading_Edge_Unified_Master_Prompt.txt); it remains one complete prompt.
- Use [v3/skill/SKILL.md](skill/SKILL.md) for the modular skill and its references.
- Read [edge-protocol.md](skill/references/edge-protocol.md) for the detailed decision procedure.
- Read [frontier-sources.md](skill/references/frontier-sources.md) for the 19 added economics/information projects and [behavior.md](research/behavior.md) for seven additional LLM/evaluation sources. Access depth and manuscript versions are explicit.
- Inspect [kernel-notes.md](kernel-notes.md) before using the finite-model functions.

The previous 80 source entries remain available in the original and adaptive registers. The additional 26 projects are selected for specific changes to the procedure; source count is not a measure of proven edge. The studies contain authored synthesis and links, not a redistribution of complete third-party papers.
