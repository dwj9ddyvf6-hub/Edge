All inputs are supplied toy assumptions. Arithmetic below is **DERIVATION**; E04 contains **HYPOTHESES**; E05 reports estimates from the supplied completed pilot. None establishes a live trading edge or authorizes trades.

**E01 — Pass at the current ask.**

Let \(I\) include all public information and the quote. The relevant likelihood ratio is \(0.60/0.40=1.5\), giving

\[
p=P(Y=1\mid I,Z+)=
\frac{0.58(0.60)}{0.58(0.60)+0.42(0.40)}
=\frac{0.348}{0.516}=0.674419.
\]

Buying has expected net payoff \(0.674419-0.69-0.01=-0.025581\) per contract; passing yields zero. The break-even purchase price before the additional cost is \(p-0.01=\mathbf{0.664419}\); strictly positive expectation requires a lower price. The purchased sensor fee is sunk and no further sensor fee should be deducted.

The unconditional likelihood ratio of 4 is inappropriate after conditioning on the same public information. Nor is the ask itself the physical-probability prior: the supplied validated prior is 0.58.

Three paraphrases supply one underlying observation, not three independent likelihood ratios. They might check extraction or arithmetic, but add no statistical evidence in this stipulated model.

**Next experiment:** prospectively record a second sensor measuring a distinct underlying feature, with original timestamps and lineage. Compare the price-aware model already containing the first sensor against the augmented model; estimate conditional likelihoods without assuming independence, and test joint features where complementary. Freeze chronological evaluation and the buy-threshold cohort. Require incremental net value after acquisition cost, delay and attainable quotes. A useful forecast improvement can still fail this economic test.

**E02 — Add one unit of B.**

The extra fee changes A's payoff to \((-14,+12)\) and B's to \((+12,-14)\). Both have standalone expected net payoff \((-14+12)/2=\mathbf{-1}\); before the new fee each had mean \(+1\).

| Action | Terminal wealth: stress, ordinary | Expected log wealth | Increment over existing portfolio |
|---|---:|---:|---:|
| Nothing | (40, 100) | 4.147025 | 0 |
| A | (26, 112) | 3.988298 | −0.158727 |
| B | (52, 86) | 4.202796 | +0.055771 |

For example,

\[
\Delta U_A=\tfrac12\log\frac{26\cdot112}{40\cdot100},\qquad
\Delta U_B=\tfrac12\log\frac{52\cdot86}{40\cdot100}.
\]

B maximizes the stated expected-log objective. Its gain arrives in the desk's poor state and its loss in the richer state. Thus identical standalone payoff distributions have different value through their coupling with existing wealth. The stress state's initial marginal utility is \(1/40\), versus \(1/100\) ordinarily; these are utility weights, not different physical probabilities.

This demonstrates portfolio complementarity, not information advantage or positive standalone expected profit. Here the desk pays an expected cost for protection. A makes the desk absorb more stress risk, but its compensation is inadequate for this objective. Claiming an actual risk-warehousing rent would additionally require evidence about a payer's demand, competing providers and compensation relative to the desk's reservation value. Interim financing is expressly assumed away in this example.

**E03 — Reject A+B; the repaired A+C bundle guarantees profit under the supplied terms.**

For A+B, take preliminary close 99 and final revised close 101. Both contracts pay zero, so the bundle loses \(0.94+0.02=\mathbf{0.96}\). Both values equaling exactly 100 also produces zero payout. Different observations and strict inequalities do not make these contracts complementary.

For A+C, the same preliminary observation is either \(>100\) or \(\le100\), including the boundary. Exactly one leg pays 1 in every admissible state.

\[
\text{cost per pair}=0.44+0.48+0.02=0.94,\qquad
\text{certain net payoff}=1-0.94=\mathbf{0.06}.
\]

Capacity is \(\min(100,20)=20\) pairs. Total cost is 18.80, settlement proceeds are 20, and **maximum guaranteed profit is 1.20**.

Borrowing 18.80 at the stipulated zero interest produces zero initial net investment and 1.20 terminal profit in every state: this is a financed sure-profit arbitrage in the toy model. The conclusion relies on exact shared settlement semantics, exhaustive thresholds, equal payout units/timing, atomic execution of both legs at stated prices and size, complete fees, financing through settlement, and certain identical settlement/counterparty terms. It is not a claim about an independently verified market opportunity.

**E04 — Two distinct research candidates.**

**Information candidate: infer interactions hidden inside an earnings release.** The hypothesis is that a joint configuration—such as cash conversion, guidance and reported operating results—can reveal implications missed by headline-only interpretation, even when each component alone adds little.

- **Participant and transfer:** investors with limited attention may price the prominent headline before its interacting details. Our proposed advantage is better interpretation of public information; no participant's mistake is assumed proven.
- **As-of signal:** preserve original publication/receipt times, revisions and source lineage. Deduplicate reports; extract prespecified factual relationships only from supplied releases and condition on contemporaneous quotes, depth and the already-observed price reaction. Missing necessary facts trigger abstention.
- **Action and exit:** begin with a long-only research rule for favorable joint configurations. Entries remain exclusively at the timing engine's first eligible closed hourly bar, using executable quotes afterward. Buy only when estimated remaining payoff exceeds measured costs and a preregistered uncertainty hurdle. Test exit at the following session's close, with a predefined invalidating-correction exit.
- **Persistence/capacity:** difficult interactions and small opportunities may receive less competitive attention; depth and post-hourly-bar signal survival limit size. These are hypotheses, not established barriers.
- **Bad state and strongest rival:** the supposed contradiction reflects valid accounting context, or the model is simply repackaging momentum, cheap sentiment or common market exposure.
- **Decisive experiment:** freeze chronological event splits and compare a price-aware baseline, individual-feature augmentation, and joint-feature augmentation with matched fitting budgets, entry clock and execution assumptions. Include source-deduplication as a simple repair, duplicate-source controls and dependence-preserving feature controls. Measure proper forecast scores and incremental net payoff on all eligible opportunities; cluster by shared event/date. Reject the capture claim if adequate precision rules out the required incremental benefit at the permitted entry time.

**Service candidate: absorb index-deletion inventory around a public deadline.** Benchmark-constrained holders may rationally accept a concession to transfer inventory and timing risk.

- **Participant and transfer:** sellers implementing the announced rebalance pay indirectly through price concession for someone else to hold the unwanted exposure.
- **As-of signal:** use prior-day announcements, disclosed effective dates, holdings publicly known then, quotes/depth and first-public news. Holdings are an uncertain pressure proxy, not observed orders; do not invent dealer positions.
- **Action and exit:** at the unchanged first eligible closed hourly bar, buy announced deletions only if estimated residual selling pressure relative to depth offers compensation above measured execution costs and this portfolio's reservation value. Test exit at the first session close after the effective rebalance, with a frozen maximum holding rule and no mandatory trade.
- **Persistence/capacity:** small, fragmented inventory needs may fit a small desk, while competing absorption, depth, correlated deletions and capital occupation cap value.
- **Bad state and strongest rival:** deletion reflects lasting deterioration; selling persists beyond the deadline or liquidity disappears. Apparent recovery may be ordinary reversal or market exposure.
- **Decisive experiment:** compare pressure-plus-news selection with pressure-only selection, ordinary reversal and no trade on chronological matched events. Test whether outcomes vary with the pressure proxy around effective dates and whether comparable non-event dates exhibit the same pattern. Audit news exclusions as-of. Estimate complete holding/exit costs, joint portfolio loss scenarios and funding needs; use own logs only within their observational support. Displayed-touch simulations cannot certify passive fills.

**Contrarian alternative:** both economic stories may be true while both trades are unattractive: semantic specialists finish repricing before the hourly bar, and competing inventory providers absorb anticipated demand before entry. Gross indexed holdings need not imply residual uncompensated demand.

**First research step:** build an audited event-to-quote timeline and run the information-model ablation at the permitted clock. Its potential payoff is unresolved; its experiment is attractive because the supplied data can directly test whether any useful capture window remains. Measure capital, borrow where needed, and impact before sizing either strategy. These are proposed combinations, with no claimed historical novelty or measured returns.

**E05 — The old 22% claim is unidentified; the pilot estimates an absolute gain of 0.02.**

The old log confounds route with context: it contains no calm-A or volatile-P assignments. Target actions lack support in relevant contexts. Adjusting for context or using inverse-propensity weights cannot create those missing outcomes. Simulated touch fills are model outputs, not observed counterfactual executions. Therefore that log does not establish the claimed causal 22% improvement.

In the randomized pilot, equally weighting contexts gives

\[
\widehat V(\text{always A})=\tfrac12(0.14)+\tfrac12(0.04)=\mathbf{0.09},
\]
\[
\widehat V(\text{old rule})=\tfrac12(0.10)+\tfrac12(0.04)=\mathbf{0.07},
\]
\[
\widehat\Delta=\mathbf{0.02}\ \text{per opportunity}.
\]

Only calm routing changes relative to the old rule, so the same difference is \(0.5(0.14-0.10)\). This is a 28.6% relative point estimate against 0.07, not confirmation of 22%.

Known 0.5 assignment probabilities and the supplied consistency, exogenous-context and no-carryover assumptions support this one-step policy-value comparison. Costs are already included. The results favor always-A on the observed means. Without reward variances and event-dependence information, no standard error, confidence interval, significance claim or defensible required sample size can be supplied. The pilot does not establish future stability, larger-size capacity or a benefit when routing changes inventory/future contexts.

Keep the 50 unresolved outcomes in a separate pending ledger linked to original assignments, horizons and policy versions. Do not assign them zero reward or select only quick completions. Incorporate them under the prespecified maturity rule; investigate informative delay/censoring and separately track pending exposure.

**Next step:** retrieve opportunity-level rewards and event identifiers, estimate dependence-aware uncertainty, and predeclare a confirmation/review design targeting net improvement over the old rule. Continue supported within-context assignment only within an authorized experimental setting; specify an economic hurdle and fixed review or valid sequential error budget. Monitor mature context-specific performance and changing context mix.

**E06 — Choose FAST-DEEP at 60 contracts.**

For any feasible mode and positive size, define \(b=a_0e^{-d/4}-0.01\). Then

\[
\Pi(q)=bq-0.0004q^2-K,\qquad
q_{\rm interior}=\frac{b}{0.0008}.
\]

Clip to \([0,60]\), then compare the result with skipping, whose profit is zero without paying \(K\).

| Mode | Delay | Delayed gross edge/contract | Interior size | Best admissible positive size | Net expected profit |
|---|---:|---:|---:|---:|---:|
| SIMPLE | 1 s | 0.093456 | 104.320 | 60 | 2.567366 |
| DEEP | 3 s | 0.085026 | 93.782 | Infeasible | Excluded |
| FAST-DEEP | 0.25 s | 0.169094 | 198.868 | 60 | 3.105661 |

For FAST-DEEP, \(60(0.169094351-0.01)-0.0004(60)^2-5=3.105661\). SIMPLE gives \(60(0.093456094-0.01)-1.44-1=2.567366\). Both exceed zero. DEEP misses the hard two-second deadline; its hypothetical 60-contract profit of 0.061559 cannot make it admissible.

FAST-DEEP wins by **0.538295 per opportunity**. Choose that single mode; shared capacity prohibits stacking modes.

A 10,000-fold expansion to 600,000 contracts violates the stated 60-contract capacity. Even outside that constraint, quadratic impact forbids linear profit scaling. Fund wealth does not expand available depth or preserve the opportunity.

**Highest-value next deployment research:** freeze these modes and measure the real net-value surface by delay and feasible size on matched opportunities. Record publication-to-fill latency and its tails, deadline misses, signal decay, depth, actual fill/partial-fill and cancellation outcomes, adverse selection, compute cost, impact, holding/exit costs, capital occupation and portfolio stress. Separate simulated execution from observed fills; test whether competitors and own impact change the opportunity as size rises. Shadow work can validate timing and data, while actual execution effects require separately authorized bounded experiments. No live deployment has occurred.

