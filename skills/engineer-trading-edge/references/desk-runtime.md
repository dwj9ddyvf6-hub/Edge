# Desk runtime: awareness, speed, and recoverable decisions

## Contents

1. Minimal architecture and decision contract
2. Data and clock semantics
3. Orders, uncertain exposure and reservations
4. Capability-specific degradation
5. Latency and resource efficiency
6. Replay and failure acceptance

Use this reference for autonomous desk design, implementation or auditing. It supplies engineering contracts; no broker capability, latency, or production readiness is implied. O-series sources are in `adaptive-sources.md`. Verify the actual venue's current protocol before implementation.

## 1. Minimal architecture and decision contract

Start with a modular service containing an append-only event journal, deterministic state reducer, incremental features/forecasts, finite action scorer, portfolio reservation authority and order-lifecycle manager. Run outcome evaluation and research asynchronously. The economic policy and safety-critical execution path should not require a synchronous LLM response. Add process boundaries only for demonstrated isolation, throughput or reliability needs [O05, O06].

Every decision needs a reproducible contract:

```text
decision_id, opportunity_id, policy/model/config hashes
as_of_snapshot_id, source/revision/dependency IDs
event/publication/receipt/feature-ready times and clock-error bounds
action-specific required inputs, freshness rules, evidence stage
reconciled positions, cash, pending orders, possible-fill envelope
candidate menu, incumbent continuation, scores, units, rejected reasons
hard limits, joint portfolio reservation version, deadline
intent_id, payload_hash, reservation_id, venue deduplication contract
fallback and recovery policy, expiry/revalidation rules
realized fills/costs/outcomes, corrections, attribution and maturity
```

Produce the cheap feasible baseline before optional refinement. No mandatory risk, contract-semantic or data-integrity check becomes optional merely because its expected dollar value is difficult to estimate. A fast invalid decision is not throughput.

## 2. Data and clock semantics

A feature is usable only after all required source facts have arrived and computation has completed. Event time is not information availability. Preserve publication time, receipt time, revision ID, feed sequence and feature-ready time. Record what the strategy actually saw separately from later corrected truth.

Specify provisional versus finalized bars/windows. Respect a designated closed-bar clock. A watermark represents stream progress under assumptions; it does not prove every relevant observation has arrived. Late data can update future decisions through a declared correction policy, but cannot rewrite a prior decision snapshot [O01]. Missing values, true zeros, stale values and failed extraction are distinct states.

Cache shared features by dependency/revision IDs, code/config/model hashes and relevant cutoff. Invalidate descendants of changed facts, while leaving unrelated calculations alone. Revalidate required freshness and own state at the submission boundary even after a cache hit. Keep terminal/settled contract definitions versioned.

Store physical timestamp uncertainty and causal sequence separately. A deterministic total order is useful for replay, but cannot establish true cross-feed lead-lag or physical causality. Do not claim a 2 ms information lead when clock uncertainty is 5 ms. Prefer server sequence and acknowledgement dependencies where appropriate; the actual clock-quality and venue contract determine interpretation [O07].

## 3. Orders, uncertain exposure and reservations

Represent possible account states when an order outcome is uncertain. Use reconciled positions plus feasible outstanding-fill paths, preserving dependence within order chains. An unacknowledged accepted order can already be exposed. A cancellation request is not a cancellation; a timeout is not a rejection [O02].

For expansion candidate a, check every modeled feasible own-state x and execution path f:

`constraints(next_state(x,a,f)) must hold`.

Use a conservative tractable envelope if exact enumeration is too expensive, document its looseness, and maintain a reconciliation path. This is protection against stated possibilities, not unknown venue behavior. If the incumbent already violates a limit, invoke the separate approved recovery objective; requiring all recovery states to be instantly compliant can deadlock necessary reduction.

**Hypothetical example:** certainly long 40 units, with an additional 60 possibly filled. An 80-unit sell intended to flatten can create a 40-unit short. Under simplified long-only assumptions, selling 40 would leave 0–60 long, but even that requires checking other working orders and current venue rules. Reconcile first; do not assume the midpoint of the uncertainty interval is the position.

Maintain lifecycle, cumulative fill quantity, remaining executable quantity, correction state and reconciliation confidence independently. A high-precedence status label can hide relevant partial fills. Release reservations only after terminal facts and quantities reconcile. Handle execution corrections/busts as explicit events.

For a 100-unit order with 40 filled, a pending reduction to total 70 can still allow the old remaining 60 until accepted. A pending increase to total 150 can allow up to 110 additional units if accepted. An atomic amendment follows one chain; it is not automatically two independent full orders. A separately submitted replacement before cancellation confirmation can expose both. Generate the feasible set from verified protocol semantics, not a generic netting assumption.

Serialize shared capital and risk reservations or use an equivalent atomic coordinator. Two sleeves cannot each consume the same available headroom. Bind intent identity, payload hash, policy/snapshot version and reservation in a durable transaction before sending. Immediately revalidate current dependency versions, limits and expiry. On conflict, recompute; do not commit a stale optimization result.

Use a stable client intent ID for retries only when the venue enforces compatible idempotency and retention semantics. Reusing an ID with changed arguments may be invalid; a new ID may create another order. If submission outcome is ambiguous and deduplication cannot be proved, lookup/reconcile rather than blindly resend. Local exactly-once processing is not exactly-once external execution [O03].

## 4. Capability-specific degradation

Build an action-to-dependency map. Partial failure need not disable unrelated capabilities, but any fallback must already be an evaluated policy with valid inputs.

| Failure | Response under the approved contract |
|---|---|
| Optional language model is late | Use the approved simpler policy if still valid; never silently impute its missing feature |
| Required entry feed is stale | Disable affected new entries; keep valid reconciliation/protection routes |
| Position or order state is unknown | Retain reservations, query, reconcile; use only explicitly justified recovery |
| Optimizer misses deadline | Revalidate the feasible fallback or abstain from expansion; never send an expired target |
| Current limit is breached | Run the specific risk-reduction contingency; ordinary hysteresis cannot delay it |
| Statistical evidence weakens | Follow the declared review rule; do not rewrite live policy in response to a story |

Track distinct states: READY, LIMITED_CAPABILITY, RECONCILING, RISK_RECOVERY, and DISABLED_FOR_EXPANSION. Define entry and recovery conditions for each. These states are not interchangeable with portfolio positions. A state disabling new entries can coexist with active position management. Restoring data connectivity does not by itself prove account reconciliation or authorize resuming risk.

## 5. Latency and resource efficiency

Prioritize execution events and risk reconciliation over optional research. Bound queue lengths and define backpressure. Coalesce redundant market updates only when strategy semantics permit; never silently discard fills, cancellations or corrections. Maintain maximum observation age as well as processing speed.

Measure publication-to-receipt, receipt-to-feature, feature-to-decision, decision-to-reservation, submit-to-ack and ack-to-fill, with clock uncertainty. Report end-to-end p50/p95/p99, deadline misses, queue age, and executable economic capture at size. Do not sum component percentiles and call the result the system percentile. Fan-out and shared-resource contention can make tail performance worse despite a faster average model [O05].

Give optional computation a deadline budget derived from opportunity decay, plus time for mandatory validation and submission. Never use hedged duplicate **mutating order** requests as a casual transfer of redundant read-request techniques. Restrict parallel work to independent read/research tasks or properly coordinated state changes.

Remove unused features, models and branches when held-out incremental value fails to cover latency, data licensing, testing, monitoring and maintenance. A small shared feature store with clear lineage can outperform independent per-agent recomputation. Avoid multiplying identical evidence through redundant models. Track who consumes each input and which policies depend on it [O06].

## 6. Replay and failure acceptance

Replay must reproduce decisions using the original available data, policy versions, update schedule, tie rules and numeric tolerances. Corrections produce new events; they do not mutate the past. Matching replay is an operational requirement, not evidence of profitable prediction.

Inject at least these failures in a sandbox adapter before live integration:

1. An early exchange timestamp arriving after the decision cutoff.
2. A revised input with an old dependent cache entry.
3. Acceptance followed by a crash before acknowledgement.
4. Fill after cancel request; cancel rejection after complete execution.
5. Upward/downward amend, crossed replies, and separate cancel/new order.
6. Concurrent sleeves competing for the same collateral/reservation.
7. Unknown [40,100] position and an unsafe 80-unit flatten instruction.
8. Optional model outage with valid protection and account feeds.
9. Optimizer delay, queue overload and a fallback that has itself expired.
10. Execution correction/bust after apparent terminal completion.

Acceptance means expected state transitions, conserved quantity/cash accounting under the venue model, no duplicate semantic intent, and no unauthorized expansion. Test the real adapter protocol; a pure selector's unit tests cannot establish these distributed-system properties. Reconcile after restart before claiming restored readiness. Measure any speed improvement on representative workloads and compare economic outcomes at matched capital, not only microbenchmarks.

## Offline kernel contract and use

Run the synthetic invariant tests with `python -m unittest discover -s scripts -p test_adaptive_arbiter.py -v` from the skill directory. Import `select` and frozen dataclasses from `scripts/adaptive_arbiter.py`; call `select(policy, incumbent, candidates, now=..., decision_deadline=...)`. Inputs use integer UTC epoch seconds and named utility/constraint units. Test fixtures show minimal synthetic construction.

Bind policy/action IDs externally to immutable definitions and authenticated input snapshots. The module cannot authenticate a supplied evidence flag or prove that utilities correspond to an action. Utilities must account for all execution branches consistently with the supplied portfolio scenarios. Constraints use additive loads and conservative Cartesian combinations of outstanding-order alternatives; this can overreserve mutually exclusive order chains. Use a validated joint-state evaluator for nonlinear margin or exact chain semantics.

The pure function checks deadlines against supplied time, without enforcing wall-clock completion or atomic external reservation. Its combination cap bounds one dimension of work, not total runtime. Malformed inputs raise ValueError: the caller must fail closed to alpha expansion and continue the separate recovery path. Repeated calls yield the same proposal; downstream order deduplication, persistence, synchronization and reconciliation remain unimplemented. These are deliberate prototype limits, not completed production capabilities.
