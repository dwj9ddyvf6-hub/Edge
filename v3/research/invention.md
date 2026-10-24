# Trading Edge Lab v3: mechanism invention, payoff geometry and transport

Research date: 24 October 2026, America/New_York. This memo adds six primary research entries not present in the existing 80-entry register. It is targeted research with inspection of the sections named below, not exhaustive reading or proof replication. Proposed procedures, examples and candidate strategies are engineering synthesis or elementary derivations; none has a measured live return here.

## What should change in the skill

The existing skill correctly asks who pays and why the opportunity persists. Strengthen it by requiring a constructive answer after the diagnosis: generate a small set of *economic transformations* of the existing strategy, compile the best into a payoff-and-execution specification, and design a decisive test. More obscure terminology does not make that process stronger. Explicitly distinguish a novel candidate, an algebraic payoff guarantee, evidence from simulation, an identified causal effect and realized trading evidence.

Three useful upgrades are: (1) semantic claims become auditable payoff constraints rather than model confidence; (2) forced-flow hypotheses use net obligations and competing liquidity supply rather than gross asset growth; (3) transferring a mechanism between markets requires stating which structural relationships are assumed to survive.

## Six new primary sources

### F01 — Abernethy, Chen and Wortman Vaughan (2013 publication; January 19, 2012 author draft)

*Efficient Market Making via Convex Optimization, and a Connection to Online Learning*. ACM Transactions on Economics and Computation. DOI: https://doi.org/10.1145/2465769.2465777

Inspected author draft: https://www.jennwv.com/courses/W12/markets-long-draft.pdf

**Inspected:** abstract, security/payoff formulation, market-design conditions, convex-hull and relaxation discussion. **Result used:** structured securities can be designed through convex cost functions and payoff geometry; completeness is not required for useful information aggregation and risk transfer. **Limit:** this concerns a specified automated market maker, not a theorem that observed exchange quotes can be collected simultaneously. Assumptions on cost functions, bounded payoffs and feasible price sets matter. **Prompt consequence:** represent contracts as payoffs before choosing a forecasting model; ask whether a cheaper synthetic contract supplies the same service.

### F02 — Kroer, Dudík, Lahaie and Balakrishnan (2016)

*Arbitrage-Free Combinatorial Market Making via Integer Programming*. ACM EC 2016. DOI: https://doi.org/10.1145/2940716.2940767

Inspected v2, June 10, 2016: https://arxiv.org/pdf/1606.02825 ; record https://arxiv.org/abs/1606.02825

**Inspected:** introductory formulation, Proposition 2.4, Frank–Wolfe oracle construction and stopping-condition discussion. **Result used:** integer-program representations and projection methods can make some enormous logical outcome spaces tractable; worst-case hardness remains. **Limit:** an approximate iterate is not automatically a complete certificate, and cost-function-market guarantees do not transfer unchanged to an exchange order book. **Prompt consequence:** use a small typed constraint system, a solver bound and a witness counterexample; return unresolved when proof or computation is insufficient.

### F03 — Shi and Zhai (2026 preprint, v3 revised October 20)

*Combinatorial Arbitrage in Prediction Markets*. Submitted October 16, 2026; latest inspected version v3 October 20. https://arxiv.org/abs/2610.23517 ; exact text https://arxiv.org/html/2610.23517v3

**Inspected:** §§3.1–3.3, logical-relation layers, LLM proposal/audit procedure and execution-replay description. **Result used:** payoff constraints, book depth and semantic auditing can be joined in one discovery pipeline. **Limits:** their defined arbitrage requires strictly positive profit in every modeled state. Their historical return exercise is an ideal displayed-depth replay, conditional on binary settlement, not a live attainable-return guarantee. Independent execution, resolution and relation errors remain material. **Prompt consequence:** separate venue-asserted, mechanically derived and semantic-inferred relations; keep source version and audit evidence. Do not promote a semantic guess to a payoff guarantee. This is a recent preprint, not a settled empirical benchmark.

### F04 — Lou, Yan and Zhang (2013)

*Anticipated and Repeated Shocks in Liquid Markets*. Review of Financial Studies 26(8), 1891–1912. Author manuscript May 2013: https://personal.lse.ac.uk/loud/Shocks.pdf

**Inspected:** abstract and introduction, duration-matched trade construction, dealer-capacity explanation and measurement caveats. **Result used:** predictable Treasury issuance can accompany temporary price pressure even when the event calendar is public; compensation may concern balance-sheet service rather than superior forecasting. **Limit:** historical auction patterns, funding arrangements and event windows cannot become current parameters by citation. **Prompt consequence:** search scheduled obligations and their marginal absorbers, then test current net compensation. The risk-frontier memo's newer Treasury work provides a useful challenge to transporting this old mechanism unchanged.

### F05 — Greenwood and Sammon (2025 publication; March 2024 author manuscript)

*The Disappearing Index Effect*. Journal of Finance 80(2), 657–698. Publication: https://doi.org/10.1111/jofi.13410

Inspected manuscript: https://dash.harvard.edu/server/api/core/bitstreams/647cc3b7-4803-4748-b181-e5ec8b343de7/content

**Inspected:** introduction, migration/net-demand decomposition, competing explanations and increased-liquidity discussion. **Result used:** the index effect weakened despite expanding index-linked assets; cross-index migrations offset gross flows, while market absorption changed. **Limit:** neither index pressure nor its disappearance is a universal law for every index, event or future period. **Prompt consequence:** model net obligated flow and available competing capacity separately. A bigger payer population need not imply a larger rent for us. This is a productive contrarian check on a superficially compelling forced-buying narrative.

### F06 — Pearl and Bareinboim (2014 publication; March 2015 arXiv reprint)

*External Validity: From Do-Calculus to Transportability Across Populations*. Statistical Science 29(4), 579–595. DOI: https://doi.org/10.1214/14-STS486

Inspected reprint: https://arxiv.org/pdf/1503.01603 ; record https://arxiv.org/abs/1503.01603

**Inspected:** selection-diagram definitions, examples of alternative transfer formulas, Theorem 1 and discussion of mechanism differences. **Result used:** valid transport depends on explicit structural assumptions about what changes between environments; matching distributions alone does not establish it. **Limit:** a graph drawn by an LLM is an assumption, not identified market structure. **Prompt consequence:** when moving a strategy to another asset, size or venue, state which payoff, participant, execution and causal mechanisms change, which remain fixed, and what target-market evidence is required.

## Exact distinctions that prevent an impressive theorem from becoming a bad trade

Let a finite modeled state set be S, let row A_s contain the instrument payoffs in state s, and let h be a feasible portfolio. Define a fully specified terminal net payoff after financed acquisition and operational costs as Z_s(h). For a simplified common settlement date, deterministic cost convention and no interim state dependence, Z_s(h)=A_s h-K(h). K must include the terminal value of cash used, so comparing an undiscounted future payoff with present cost is not silently free financing.

There are several different claims:

1. **Strict sure-profit certificate:** min_s Z_s(h)>0 for a feasible h under an exhaustive, correct state/contract model.
2. **Standard nonnegative-payoff arbitrage:** Z_s(h)>=0 in every possible state and >0 with positive probability, financed with no positive initial net investment after any allowed funding positions. The support and interim financeability matter.
3. **Positive expected value:** sum_s p_s Z_s(h)>0 under a specified probability model. It can lose.
4. **Portfolio improvement:** the trade improves a declared utility or risk objective relative to the incumbent. It may have negative standalone expectation.

For unrestricted signed portfolios, a single price vector and the normalized frictionless model, separation of price from the convex hull of payoff vectors yields a strict sure-profit direction [F01–F03]. Do not reverse that into a universal financial no-arbitrage certificate. A binary payoff taking 0 or 1 and quoted at zero lies on that hull's boundary; buying it for free can still give a nonnegative payoff that is positive in a possible state. Spreads, restrictions and incomplete support also change the relevant theorem. Name which claim a program actually checks.

An enlarged state set makes a worst-case guarantee more conservative. Erroneously deleting a feasible adverse state can manufacture arbitrage. This monotonicity is an elementary property of minimization and provides a direct robustness test: add plausible exceptional settlements, mismatched calendars and unresolved semantic branches before declaring the guarantee. A semantic relation with unknown validity should retain both possibilities, which may eliminate the certificate.

When different legs can fill separately, validate the exposure after *every reachable partial-fill path*. A terminal basket certificate is conditional on owning that basket. An attractive completed-basket payoff does not make the acquisition path risk-free. Keep that failure mode distinct from forecast error.

## Generative search operators

Apply these to an existing strategy or create a small candidate set. Change one economic element, then recompute the whole payoff and experiment; do not simply add indicators.

| Operator | Constructive question | Required artifact |
| --- | --- | --- |
| Counterparty substitution | Which participant needs the same transaction for a different reason? | Objective, binding constraint, observable obligation, plausible price-setting channel |
| Contract substitution | Can a combination of claims provide the same payoff at a lower complete cost? | Typed payoff table, feasible states, acquisition and settlement path |
| Clock substitution | Who must trade by a deadline that we can avoid? | Public/as-of clock, holding window, inventory and delay costs |
| State substitution | Can the desk supply protection in a state where its existing book is comparatively strong? | Joint endowment/payoff stress table and reservation premium |
| Net-flow cancellation | Which opposite mandated flows erase an apparent imbalance? | Net rather than gross flow estimate, uncertainty and supply-of-liquidity estimate |
| Complexity substitution | Can reusable parsing or a constraint cache reduce a competitor's fixed research cost? | Verified reuse unit, invalidation rule, amortized cost and capacity |
| Mechanism transport | Where does the same constraint exist with different contracts or competition? | Source/target differences, assumed invariants, target evidence and falsifier |
| Mechanism reversal | What would make the strategy's familiar signal stop working or reverse? | Competing directional prediction, prospective discrimination test |

Use novelty as a research allocation criterion, not a truth score. Keep one unconventional candidate, one simple repair and one cheap falsification experiment in the candidate set. Spend research effort where the combination of possible economic value and a decisive accessible experiment is strongest. If the data reject a candidate, preserve the reusable mechanism model and search a different feasible transformation.

## Four concrete research hypotheses

These are proposed combinations, not claims of literature priority or established alpha. Named instruments are examples of contract classes, not current recommendations.

### H1 — Settlement-aware implication baskets

**Mechanism and payer:** fragmented trading in related event contracts may leave a cheaper synthetic payoff because relation discovery, resolution interpretation and capital locking are costly. The residual is paid through inconsistent executable terms, not through predicting the outcome better.

**Construction:** if audited semantics establish that event D implies event M, buy YES(M) and NO(D). For feasible (D,M) states (0,0), (0,1), (1,1), the basket pays 1,2,1. Hypothetical asks .42 and .53 yield a minimum gross surplus .05 per completed basket before financing and all fees. If (1,0) is possible, the basket can pay zero and the guarantee disappears. A daily close exceeding a threshold and a monthly maximum exceeding it illustrate a candidate implication only when observation sources, adjustments, calendars, inequality conventions and resolution rules align.

**Data/timing:** dated full contract rules and revisions, quotes with depth and timestamps, settlement states, available funding and cross-leg execution capabilities. Detect only after relation audit; recompute after rule or quote changes.

**Costs/bad state:** fees, gas if applicable, partial-fill unwind, capital occupation, dispute delay, nonbinary settlement or oracle mismatch; portfolio may cluster on one resolver or funding channel.

**Falsifier/first experiment:** prospectively audit a small frozen contract family, enumerate exceptional states, then quote-replay with measured delays and partial fills. Reject the guarantee if any admissible state violates it; reject the implementation if attainable cost removes the margin. Separate witnessed executions from simulated ones.

### H2 — Migration-adjusted rebalance liquidity

**Mechanism and payer:** benchmark-constrained investors may pay for timing and balance-sheet service. A conspicuous index addition can conceal offsetting forced sales from another index, so the opportunity is conditional on net obligations and competitors' inventory capacity.

**Data/timing:** public announcement and effective times, point-in-time constituent weights, fund assets, known cross-index migrations, spreads/depth and lawful public auction/imbalance data. Estimate net required shares from the sum of each fund's AUM times weight change divided by price; attach uncertainty rather than treating all funds as mechanical replicators.

**Action:** research a small inventory-provision window around effective rebalancing, with exposure-matched hedge where actually accessible; trade only when the estimated residual obligation and executable compensation exceed a prespecified hurdle. Include a zero-net-flow control and a simple no-change baseline.

**Costs/bad state:** spread, impact, borrow, financing and model error; news may coincide with the change, arbitrage inventory can crowd, and multiple events share market/liquidity risk.

**Falsifier/first experiment:** freeze the net-flow model and test whether signed price pressure or paid spread survives outside development events after costs, beyond gross-flow and announcement-only models. If gross flows grow while net flows or marginal compensation vanish, reject rather than add leverage.

### H3 — Capacity-conditioned auction intermediation

**Mechanism and payer:** institutions must absorb scheduled issuance; compensation can arise when inventory absorption temporarily exceeds accessible balance-sheet capacity. Public knowledge of an auction is compatible with a paid service opportunity, but cannot by itself establish one.

**Data/timing:** official as-of auction schedules and sizes, comparable instrument prices, rate-factor exposures, executable funding/borrow, and release-lagged participation/capacity proxies. Do not use auction results to enter before the result release.

**Action:** study a matched-duration relative-value position only in a frozen capacity-stress subset; compare it with unconditional calendar trades and with not adding risk. Require explicit unwind time and interim margin budget.

**Costs/bad state:** repo changes, basis/convexity risk, macro news, early financing withdrawal and crowding; duration neutrality does not remove balance-sheet stress.

**Falsifier/first experiment:** test whether current compensation is concentrated where predicted absorption is weak, using held-out auctions and alternative explanations. New nondealer participation that absorbs supply without persistent pressure defeats the old story. The recent auction research in the companion risk memo is a required competing hypothesis, not optional historical decoration.

### H4 — Shared contract compilation for small opportunities

**Mechanism and payer:** some small, heterogeneous opportunities may be ignored because individualized interpretation costs exceed the dollars available. A reusable, audited contract schema could lower our fixed research cost while preserving careful settlement semantics. That is a hypothesis about production cost and attainable capacity, not about superior private facts.

**Data/timing:** a prospectively selected family sharing issuer/venue template, official resolution source, timestamped rules and quotes, retained exceptions and audit labels. Cache only stable semantics; bind them to exact rule hashes and invalidate on amendments.

**Action:** apply one verified schema to a narrow family, then run H1-type payoff checks or a separate forecast model. Schedule deep analysis only for exceptions or marginal decisions; keep mandatory checks on every contract. Capture small positive opportunities at feasible size rather than forcing them into a large-capacity mandate.

**Costs/bad state:** initial auditor/engineering cost, per-contract review, compute, fees, competing automation and correlated schema error. One faulty template can invalidate an entire family; hold out source/template families, not random rows alone.

**Falsifier/first experiment:** predefine an eligible family and compare per-opportunity research cost, semantic false positives, deadline completion and attainable net value against individualized analysis. Lower cost with higher semantic failures is not improvement. If audited surplus never exceeds amortized costs, reject the workflow as an edge source even if its software is fast.

## A compact invention procedure for the prompt

1. Freeze the incumbent and mandate. Extract the proposed payoff, participant constraint, as-of information and feasible actions.
2. Generate a small diverse set using the operators above; include a simple repair, an unconventional mechanism and a hypothesis that would reverse or destroy the apparent edge.
3. For each, state the payer/service or information wedge, economic transfer, competition/capacity, adverse portfolio state and exact falsifier.
4. Compile the best candidate into point-in-time data fields, rules, a state/payoff representation, all costs and an acquisition/exit path. Mark every unresolved semantic or identification assumption.
5. Use algebra or a solver where the claim is algebraic; use properly identified data and prospective evaluation where it is empirical. Keep those proof burdens separate.
6. Choose the cheapest accessible experiment that can change the decision. Record rejected candidates and search effort. Advance measured value, not eloquence.

This makes the LLM generate testable economic designs as well as critique existing ones. It does not depend on pretending to hold elite credentials or treating confidence as capital.
