# Audit and second-pass findings

The original Trading Edge Lab succeeds at the difficult first task: separating a story about profitable trading from an economically plausible, executable and testable advantage. Its strongest requirements remain intact: identify who values what the desk provides; compare beliefs with executable prices; condition on fills; price joint bad-state exposure; preserve chronology; and account for strategy search.

The missing layer was an explicit adaptive controller. The first version required monitoring, reconciliation and evidence gates but left substantial freedom in how those components interact. That freedom can produce an impressive-looking system that retrains on selected outcomes, confuses historical evidence with current opportunity, or changes an order while forgetting exposure that can still fill.

The upgrade is a practical control-and-learning addendum. It makes awareness a set of observable states, intelligence a decision-quality objective, adaptability a tested update rule, and speed an economic deadline. It does not claim that a controller can make every strategy profitable or produce an orders-of-magnitude return improvement without measurement.

## What was reviewed and changed

All five authored v1 Markdown files were reviewed: core instructions, foundations, ten mechanism blueprints, validation and the 50-entry source register. This was a review of their full content; it was not a fresh complete reading of every v1 paper. Four independent research tracks then examined control theory, adaptive inference, economics and system behavior. The new register adds 30 distinct primary sources, with access scope and limitations stated individually. One re-examined source is explicitly retained as an alias, not counted again.

| Area | Finding in v1 | Change in v2 |
|---|---|---|
| Economic foundations | Main distinctions and displayed identities remain sound in this review | Preserve them; make the core arbitrage definition match the fuller initial-cost and positive-probability conditions |
| Dynamic decisions | Response choices named, control contract underspecified | Explicit state, budgets, feasible action menu and common-model portfolio comparison |
| Adaptation | Monitoring and refitting mentioned | Separate action response, approved learning and promotion of new rules |
| Evidence | Chronology and repeated testing recognized | Typed estimands, support checks, delayed labels, full information history and reset/error budgets |
| Awareness | Freshness/reconciliation intentions | Revision semantics, possible fills, atomic reservations and capability-specific degradation |
| Speed | Latency recognized as a cost | Deadline-aware computation and end-to-end tail measurement |
| Scope | Research framework | Research framework plus a small tested offline decision kernel, with explicit unimplemented runtime boundaries |

## The deepest additional insight

The scarce object is not a prediction. It is a **feasible action whose advantage survives uncertainty, competition, execution, capital constraints and delay**. This changes the system's priorities.

An uncertain forecast can be sufficient when every plausible value leads to the same action. A precise forecast can be useless at the offered price. A high-quality signal can lose its edge through selected fills. A good sleeve can reduce desk value by occupying collateral needed for a better opportunity. More information can arrive too late. An adaptive rule can improve its training score while changing its environment for the worse.

The master algorithm therefore allocates five budgets: capital, liquidity, time/compute, information acquisition and statistical error. It preserves each budget's meaning rather than combining unlike quantities into a confidence score. It also distinguishes three clocks: execution, belief updates and policy promotion.

## Connections that change the design

| Connection | Useful consequence | Boundary |
|---|---|---|
| Partial observability | Retain probabilities over market conditions and sets of possible own-account states | A regime label is not truth; a filter with full-sample fitted parameters leaks |
| Robust decision theory | Compare candidate and incumbent under the same plausible model | A scenario minimum is not a confidence interval |
| Rational metareasoning | Spend computation where it can change a valuable action before expiry | LLM certainty and longer reasoning are not measured information value |
| Sequential inference | Monitor continuously with a declared null and information history | Historical average evidence is not a current-edge forecast |
| Causal/off-policy evaluation | Learn from actions the data can actually support | Simulated fills cannot supply missing action probabilities or real executions |
| Performative prediction | Model how deployment and size change later observations | Stable retraining need not optimize deployed outcomes |
| Resource economics | Allocate shared funding, inventory and capacity by marginal portfolio value | Local shadow prices are not extra realized fees |
| Distributed systems | Preserve causal ordering, retry identity and uncertain order exposure | Local idempotency does not prove exactly-once broker execution |

These connections are synthesized into operational rules in the following chapters. They are not claimed as novel academic discoveries. Several are deliberately conservative because the cost of a false action and the cost of a missed action differ by mandate; the chosen balance must be explicit and evaluated.

## What the master algorithm actually does

At each eligible event it validates what the desk knows, reconciles what it might already own, updates approved beliefs, constructs a small action menu, evaluates full portfolio consequences, and performs only worthwhile additional computation. It chooses an admissible action or retains the feasible incumbent, reserves resources, and records a reproducible intent. It routes integrity failures to an independent contingency path.

When outcomes mature, it scores the decisions that were actually issued, separates prediction from capture and portfolio effects, and updates a prespecified evidence process. A new rule must outperform a frozen feasible baseline through an honest experiment before promotion. This prevents rapid learning from becoming rapid unrecorded search.

The most useful daily output may be an entry, a hold, a reduction, a hedge, a reconciliation request, a research experiment or no new exposure. The goal is useful coverage of opportunities and reliable management of existing risk, rather than a required number of trades.

## How to implement this leanly

Begin with the finite approved candidate menu and one shared portfolio arbiter. Keep the event journal, state reducer, scoring, reservations and order manager modular but close together. Run research and evidence analysis asynchronously. Add sophisticated latent-state models, dynamic solvers or distributed services only after a simpler baseline reveals a measured limitation they can address.

The included reference kernel computes one deliberately small part: the paired robust improvement gate with supplied scenarios, evidence flags, freshness, deadlines and additive load constraints. It has no market feeds, broker integration, learning, durable event store or order submission. Its executable tests check mathematical and control invariants; they do not validate a trading edge. The runtime chapter specifies the additional failure tests required for a real adapter.

Use the updated skill with: “Use $engineer-trading-edge to audit this strategy, identify its binding loss of value, and apply the adaptive-control addendum. Preserve its approved timing authority, define the smallest useful controller, and run the next decisive experiment.”

The standalone prompt accompanying this report can be supplied to another LLM. The full skill remains preferable when its references and scripts are available: it loads deeper material only when needed and retains the original economic foundations.
