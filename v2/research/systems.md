# Trading Edge Lab v2: systems audit and operational intelligence

Research date: 2026-10-24 UTC. This memo audits the core skill and its foundations, mechanism blueprints, validation, and source register. It proposes engineering additions; no market experiment, broker integration, or production speed benchmark has been run. Source findings and original design deductions are separated below. Seven distinct additional primary sources are registered as O01–O07. Boyd et al. is a cross-reference to the control research team's source, not an eighth new item.

## Audit verdict

Version 1 is economically careful and already requires point-in-time data, realistic fills, deterministic risk checks, replay, reconciliation, and versioned policy changes. Its strongest missing layer is the contract between those ideas. “Reject stale inputs,” “submit idempotently,” and “reconcile positions” are intentions, not sufficient implementation specifications. A desk can obey those sentences superficially and still trade a revised bar early, duplicate a timed-out order, release risk during a pending cancellation, or disable its only risk-reduction route because an unrelated news feed failed.

The upgrade should therefore add a **decision contract**, a **set of possible own-account states**, and an **action-specific capability map**. Faster cognition means fewer unnecessary computations and fewer unknown dependencies in the decision path; it does not mean having an LLM reconsider its entire strategy on each tick. Greater awareness means knowing what information is fresh, what remains uncertain, which actions remain justified, and how close the opportunity is to expiring.

## Primary-source register

The following compact summaries report inspected material, not claims of end-to-end paper replication. Keep each source's literature summary separate from the original synthesis that follows.

### O01 — Akidau et al. (2015), The Dataflow Model

Original paper: https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf

Author page: https://research.google/pubs/the-dataflow-model-a-practical-approach-to-balancing-correctness-latency-and-cost-in-massive-scale-unbounded-out-of-order-data-processing/

Access: original 12-page PDF retrieved; introduction, windowing/triggers, watermarks, late-data examples inspected. Web refs: `turn79view0`, `turn82view2`.

Finding: event time, processing time, window semantics and result emission are separate concepts. Watermarks can progress before missing data arrives or lag because of a slow source. Incremental outputs and later corrections offer different correctness/latency/cost tradeoffs. Limitation: this is a stream-processing model, not proof that a watermark certifies a trading feature's availability. A historical correction can refine a research dataset but cannot retroactively become information available to a prior trading decision.

### O02 — FIX Global Technical Committee (July 2020, EP258), Order State Changes

Official specification: https://www.fixtrading.org/wp-content/uploads/download-manager-files/Order-State-Changes.pdf

Official landing page: https://fixtrading.org/packages/fix-latest-specification-order-state-changes/

Access: 56-page official PDF retrieved; version cover, cancellation scenarios B.1, replacement scenarios C, sequencing D inspected. Web refs: `turn79view1`, `turn91view0`.

Finding: pending cancellation or replacement does not establish completion. Executions can arrive while cancellation is pending; a fully executed order can generate a cancel rejection. `OrdStatus` precedence can conceal partial-fill status, so status labels cannot replace quantity accounting. Replacement chains retain explicit identifiers. Limitation: the document is dated July 2020 despite “latest” in its title. Each target venue's actual protocol/version, corrections and reconnect rules must be verified; do not assume every broker implements the whole FIX state machine identically.

### O03 — Malcolm Featonby, Making Retries Safe with Idempotent APIs

Official engineering article: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/

Access: article body inspected, including token semantics, atomic mutation, semantically equivalent responses, late requests and token lifetime. Publication date not established from the inspected page; accessed 2026-10-24 UTC. Web refs: `turn79view2`, `turn82view3`, `turn91view1`.

Finding: a caller-supplied request token can express retry intent. Token recording and mutation need atomic treatment, and the contract must define repeated tokens, changed arguments and late arrivals. Limitation: a client-generated identifier alone does not make an arbitrary broker API idempotent. The server must enforce a compatible contract. When the venue cannot prove deduplication, an ambiguous submission requires lookup/reconciliation rather than a fresh-ID blind retry.

### O04 — Russell and Wefald (1989), On Optimal Game-Tree Search Using Rational Meta-Reasoning

Original proceedings paper: https://www.ijcai.org/Proceedings/89-1/Papers/053.pdf

Access: original 7-page PDF retrieved; value-of-computation formulation, action selection, time cost and single-step assumption inspected. Web refs: `turn79view5`, `turn82view7`, `turn91view5`.

Finding: computations themselves can be selected by expected improvement in the eventual action after computational/time cost. A tractable one-step approximation can miss complementary computations whose value appears only as a sequence. Limitation: their demonstrated setting is game-tree search, not financial alpha or LLM confidence. A desk needs prospective estimates of decision improvement and delay loss; a model cannot declare its own deeper answer valuable merely because it sounds better.

### O05 — Dean and Barroso (2013), The Tail at Scale

Author paper: https://www.barroso.org/publications/TheTailAtScale.pdf

Author research record: https://research.google/pubs/the-tail-at-scale/

Access: original 7-page article retrieved; shared-resource/queueing causes, fan-out example and service-class discussion inspected. Web refs: `turn79view3`, `turn91view4`.

Finding: a small fraction of slow components can dominate aggregate response time when completion waits for many branches. Mean component latency therefore misses an important system-level bottleneck. Limitation: Web-service results are not trading-system latency measurements. Hedged read requests may be useful in some systems; duplicate mutating order submissions must not inherit that pattern. Measure the actual trading deadline distribution under realistic load before choosing more parallelism.

### O06 — Sculley et al. (2015), Hidden Technical Debt in Machine Learning Systems

Original paper: https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf

Access: original 9-page PDF retrieved; boundary entanglement, data dependencies, feedback loops, dead branches, typed metadata and configuration examples inspected. Web refs: `turn79view4`, `turn82view5`, `turn91view2`.

Finding: production learning systems accumulate dependencies and feedback beyond the fitted model. Undeclared consumers, experimental branches and configuration differences can defeat apparently modular improvements. Limitation: this is an engineering analysis, not an empirical guarantee that simplification improves trading returns. It motivates explicit dependency ownership, immutable configuration, and incremental net-value tests for added components.

### O07 — Lamport (1978), Time, Clocks, and the Ordering of Events in a Distributed System

Author-hosted original: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Time-Clocks-and-the-Ordering-of-Events-in-a-Distributed-System.pdf

Access: original 8-page PDF retrieved; happened-before definition, logical-clock condition, total ordering and limits inspected. Web refs: `turn103view0`, `turn103view1`.

Finding: communication induces a partial order; logical clocks can extend it to a consistent total order. Logical-clock order does not prove physical-time order or causation in the converse direction. Limitation: ordering messages for deterministic replay does not repair wrong market timestamps or prove an economic lead-lag relationship. A causal dependency sequence and a measured physical clock error are different pieces of evidence.

### Cross-reference — Boyd et al. (2017), Multi-Period Trading via Convex Optimization

https://web.stanford.edu/~boyd/papers/pdf/cvx_portfolio.pdf

Coordinate with the control team's C-series identifier; do not count again. Inspected original sections on transaction costs, holding/trading constraints, multi-period objective, dynamics approximation and execution of only the first planned action (`turn82view0`, `turn91view3`). The paper explicitly excludes producing the forecasts themselves. Use it to support portfolio control, not a claim that optimization manufactures predictive advantage.

## Proposed operational contracts — original engineering synthesis

### 1. Represent the desk's knowledge, not just the market estimate

At decision time t maintain:

`S_t = (market_snapshot, belief_version, feasible_account_states, live_orders, reservations, capability_map, deadlines, policy_version)`.

The market forecast is only one component. An unacknowledged order creates uncertainty about what the desk already owns. Represent that uncertainty with a feasible state set X_t, preserving dependencies between order chains. Do not replace it with an arbitrary point estimate or a probability invented by an LLM.

For a proposed action a, let F_t(a) be the set of feasible execution paths under the verified venue contract. The new-action check is:

`for every x in X_t and f in F_t(a): constraints(next_state(x, a, f)) hold`.

Use a conservative tractable envelope if exact scenario enumeration is too expensive; document its looseness. This is a safety model over stated possibilities, not a proof against unknown broker behavior. If a current state already violates a boundary, use a separately approved recovery objective that reduces the violation without creating forbidden new exposures; demanding that every intermediate recovery state be inside a breached limit can deadlock recovery.

Illustration: a long-only account certainly holds 40 units and may hold as many as 100 because the remaining 60 could have filled. Sending an 80-unit sell to “flatten” can create a 40-unit short. A 40-unit sell, under the simplified single-asset assumptions, leaves between 0 and 60 units; the broader action still needs liquidity, order-interaction and venue checks. Reconciliation is the first information action. No universal “on uncertainty, flatten” instruction is valid.

### 2. Make cancellation and replacement reserve actual possible risk

Maintain independent dimensions for order lifecycle, filled quantity, remaining executable quantity, and reconciliation confidence. A pending-cancel label cannot zero the remaining exposure. Retain the reservation until terminal facts and cumulative quantity reconcile. Handle execution corrections explicitly rather than assuming cumulative quantities can never change.

Hypothetical quantity examples (one order, total quantity conventions): with 40 filled of an original 100, a pending reduction to total 70 still permits the original remaining 60 before acceptance. A pending increase to total 150 requires modeling up to 110 additional units if accepted. An actual atomic amend follows one chain; do not automatically count the old and new total quantities as two independent orders. In contrast, a cancel followed by a separately submitted new order before cancel confirmation can expose both orders simultaneously. The venue semantics determine the feasible set.

Reserve portfolio resources **atomically before submission**, including accepted-but-unacknowledged intents. Two sleeves must not independently consume the same remaining risk or cash budget. A serialized portfolio arbiter is often simpler than many local locks. Journal intent ID, payload hash, snapshot version and reservation together. A changed payload is a new semantic intent and requires a new risk decision; retries preserve the original intent identity according to the venue's verified deduplication rules.

### 3. Specify data availability and correction semantics

For every required input record publication time, local receipt time, processing completion, source sequence, revision identity, clock-quality bound and validity horizon. A feature becomes available only after its required inputs and computation are available. Event time alone is insufficient. Preserve both the original decision snapshot and later corrected research truth.

Use feed-specific completeness and freshness contracts. A watermark indicates progress under that source's assumptions; it is not a certificate that every relevant fact has arrived. Explicitly choose whether a decision uses provisional windows, waits for a close-confirmed window, or abstains. Respect an existing strategy's closed-bar authority. Late records update future state through a declared correction path and never mutate the recorded past action.

Cache keys should include dependency IDs, revision IDs, feature-code/config hashes, model version and relevant cutoff. Invalidate only descendants of changed dependencies, but re-run every mandatory gate before an order. A cache hit is an optimization, not evidence of current validity. When physical clock-error intervals overlap, do not claim a measured cross-feed lead smaller than that uncertainty. Replay ordering can be deterministic without inventing physical causality.

### 4. Degrade by capability, not with one global panic switch

Build a dependency map from each action to the data and services it needs. Examples:

| Impairment | Potentially permitted behavior | Behavior needing separate proof |
|---|---|---|
| Optional news model late | Use an approved price-only policy if its validity conditions hold | Silently fill a missing semantic feature with zero |
| Required entry feed stale | Disable affected new entries; continue reconciliation and valid protection | Assume every unrelated sleeve must stop |
| Account state ambiguous | Query and reconcile; retain reservations; apply approved robust recovery actions | Blind resend, full flatten, or release capital |
| Optimizer deadline exceeded | Revalidate a predefined fallback against current state | Send an old target because it was valid earlier |
| Statistical evidence weakens | Apply the prespecified review/reduction rule | Rewrite the strategy after the last losing trade |

No new trade is not the same as no risk: existing positions still require monitoring. Conversely, a risk-reducing hedge can have negative standalone expectancy. The action taxonomy should include keep, reduce, hedge, cancel, reconcile, observe, research, enter and retire, with separate authorization and preconditions.

### 5. Separate the fast decision path from research

Use three clocks: event-driven operations, scheduled evidence review, and research/promotion. In the fast path, update incremental features, ingest fills, check capability and reserved risk, and apply only an approved policy. In the review path, mature labels, update prescribed diagnostic statistics and assess drift. In research, generate new models, re-estimate models and run controlled comparisons. A research output becomes executable only after versioned promotion; it does not mutate the current policy by being persuasive.

Research and observability work should not compete unpredictably with risk reconciliation. Bound queue sizes and set backpressure policies. Coalesce redundant market updates only where the strategy's semantics permit it; never silently drop execution events. Define exactly which missing optional branch can be skipped. Avoid a synchronous “consult every agent” barrier for an opportunity that expires faster than the slowest agent.

Measure `event→receipt`, `receipt→feature`, `feature→decision`, `decision→risk reservation`, `submit→ack`, and `ack→fill`, including clock uncertainty. Report end-to-end quantiles, deadline misses, queue age and economic capture, not merely average model inference time. The target latency comes from measured opportunity decay at feasible quantity, not an impressive universal millisecond number.

### 6. Allocate computation where it can change the action

Extend v1's value-of-information blueprint into a measurable router. For optional computation c use a prospective estimate of:

`VOC(c) = E[value(best feasible action after c at t+delay_c)] - value(best feasible action now) - compute_cost(c)`.

The future action must use expected future executable prices and remaining opportunity. Do not subtract a separate delay penalty if the future-value term already includes it. Add metacontroller runtime and estimation error when evaluating the router. Route based on a lower-confidence or ambiguity-aware estimate if required by mandate; do not label an arbitrary numerical haircut a confidence bound.

Often the cheapest discriminating question is whether a calculation could plausibly reverse the decision. If conservative action-value intervals identify the same winner under every admissible parameter, further precision has no immediate decision value. Conversely, expensive checks of contract semantics or hidden order exposure can be valuable even when the market signal is strong. Never skip mandatory data/risk checks merely because their expected monetary value is hard to estimate.

Myopic routing can reject two complementary computations that are valuable together. Permit a small registered menu of bundles in research, and compare it prospectively against shallow-only, uniformly-deep and simple-threshold routing at matched total budgets. This is bounded metareasoning, not a recursive invitation to reason forever about reasoning.

### 7. Coordinate sleeves through common resources and failures

Evaluate all sleeves against the same capital, collateral, funding currency, issuer/underlying, venue and feed failure inventory. Ordinary return correlation is not the whole dependency map. Separate accounts may share a financing source or depend on the same market-data vendor. Economic hedge offsets may not be available for margin across brokers.

Use marginal portfolio utility after joint costs and constraints when ranking actions. A capital shadow price is meaningful only for a specified, reasonably calibrated optimization problem and local conditions. Do not turn it into an extra fee if the same capital scarcity is already fully charged through the objective or constraint representation. Preserve a simple rule-based allocator as a benchmark.

## Minimal integration pseudocode

```text
on market/order/timer event e:
    append e to the durable journal; validate identity, sequence and schema
    update only affected state; retain raw revisions and prior decision snapshots
    reconcile execution facts; rebuild possible positions and outstanding reservations
    recompute action-specific capability map
    process mandatory risk/recovery events before optional research

    if e is not an approved decision trigger:
        log state transition; return

    snapshot = freeze current state, dependencies, clocks, policy and deadline
    actions = approved actions feasible under capability and mandate
    include position maintenance and approved recovery, not just entry/cash
    evaluate the simple approved policy first
    perform optional computation only if registered router justifies it before deadline
    select by incremental portfolio value, with switching and execution costs counted once

    at submission boundary:
        verify snapshot dependencies and deadline again
        atomically reserve all plausible incremental risk across live-order scenarios
        append immutable intent ID + payload hash + reservation + policy hash
        submit using verified venue semantics
        if outcome ambiguous: retain reservation; reconcile; never assume rejection

on matured outcome/review:
    score the forecasts and actions issued before that outcome
    distinguish prediction, selection, fill, cost, capacity and operational errors
    execute only the predeclared review rule; produce a new candidate version for repairs
```

## Acceptance tests that can falsify the implementation

These are test specifications; none was executed here.

1. **Late data:** replay an event whose exchange timestamp precedes the decision but whose local receipt follows it. The prior decision must not change; the later state may change under the declared correction policy.
2. **Wrong revision:** mutate a source revision after feature caching. A dependent cache hit must fail validation; unrelated features need not recompute.
3. **Ambiguous submit:** crash after broker acceptance but before local acknowledgement. Restart must recover the existing intent without inventing a second exposure.
4. **Pending cancel:** inject a partial fill after cancel request and before acknowledgement. Filled holdings and remaining reservation must reflect it.
5. **Pending replace:** test both upward and downward amendments and a separate cancel/new sequence. Reservations must match each protocol's possible fills, including crossed acknowledgements.
6. **Concurrent sleeves:** race two individually permitted orders against one shared remaining limit. Combined accepted reservations must stay feasible.
7. **Unknown position:** simulate the [40,100] long position interval and an 80-unit flatten request under a long-only mandate. The system must diagnose the possible short rather than treating “flatten” as automatically safe.
8. **Partial degradation:** stall optional NLP while valid quotes and account state remain available. Only actions requiring NLP should fail, unless a global policy dependency genuinely exists.
9. **Deadline:** inject optimizer/LLM delays and bursty event load. The controller must revalidate its fallback, report misses, and never submit an expired intent.
10. **Replay:** compare live-decision and replay snapshots, actions and reservation transitions using declared numeric tolerances. Deterministic replay does not establish profitable decisions, but disagreement disproves reproducibility.
11. **Selection feedback:** omit fills on declined actions from observed-policy outcomes; never label shadow marks as actual counterfactual fills. Preserve the opportunity stream for separate execution research.
12. **Economic speed:** compare policies on matched opportunities and size with actual infrastructure cost, signal decay and missing opportunities. A lower latency percentile earns promotion only if it improves the specified economic or operational objective.

## Concise additions recommended for the core skill

Require an action-specific decision contract: valid data/revisions, current-position uncertainty, outstanding-order reservations, deadline, approved fallback and explicit failure response. Treat operational uncertainty as part of the feasible state, not merely a warning. Reconcile before assuming a timeout or cancellation changed exposure. Gate speed and added computation by measured incremental decision value. Score prediction, capture, risk and operational failures separately. Preserve a small core and load this operational reference only for autonomy, dynamic routing, execution, or desk-integration work.
