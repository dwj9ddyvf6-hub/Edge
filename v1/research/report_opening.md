# Trading Edge
## Information, risk, constraints, and the discipline of getting paid

Research synthesis and reusable LLM operating method. Prepared October 23, 2026, America/New_York.

### The realization in the post

Johann Markov's screenshot proposes two origins of edge: superior information or access to favorable bets, and accepting risks other people would rather transfer. The screenshot was inspected directly. An original post permalink was not independently located, so this study interprets the supplied text; it does not attribute additional claims or a complete trading method to its author.

The powerful shift is from looking for a pattern to explaining a transaction. An indicator describes observations. An economic edge explains why a feasible action offers value at its price, why someone else accepts the other side, and why the advantage survives competition. The counterparty may have different information, but may also have a rational reason to pay for insurance, liquidity, immediacy, funding, or relief from a mandate. An expected transfer of cash can coexist with an improvement in both parties' welfare.

The post is a productive research lens rather than an exhaustive theorem. Its two categories overlap: a market maker can both know more and warehouse inventory. Access, execution, contract design, subsidies, and allocation can change attainable returns without fitting neatly into a mutually exclusive taxonomy. A strategy's economics need a payoff model; labeling it does not estimate it.

### The central synthesis

A defensible edge is a repeatable, participant-specific advantage in the conversion of information, services, or risk-bearing capacity into feasible net economic value. This is an operational definition proposed by this study. It deliberately includes three comparisons: against the current price, against competitors' capabilities, and against the investor's actual alternative use of capital.

That definition changes the questions an LLM should ask. What precisely is the traded payoff? Which observations arrive before the decision? What does the price already reveal? What changes when our order fills? Who needs the transaction? What state makes the position painful? How much of the apparent profit pays for that exposure? Which rival strategy can provide the same service more cheaply? What would make us stop believing the claim?

The output of this research is therefore a reusable method for creating and improving hypotheses, with executable specifications and decisive tests. It cannot supply missing observations or turn a mechanism into demonstrated profit. Its purpose is to make the model substantially harder to fool and much better at deciding where to investigate.

### Three refinements that matter most

**Information is valuable relative to a price and a decision.** A 70% chance of an event is a bad purchase at a price requiring 80%. Accurate forecasts on events nobody can trade add little trading value. The relevant question is whether new evidence changes a feasible decision enough to pay for collecting it, interpreting it, and acting before the price moves. Costs and endogenous price impact limit how much of an informational advantage can be collected. [I01, I02, I06, B01]

**Risk is valuable to the seller only at an adequate premium.** Variance alone does not entitle its bearer to compensation. A loss that coincides with a customer's most expensive state can command a premium; an independent avoidable gamble may not. A warehouse must be able to survive the period when collateral requirements rise and liquidity vanishes. Terminal convergence does not pay a margin call today. [R1, R2, R3]

**A credible story and a credible test do different jobs.** The story suggests when an effect should appear, its capacity, and its failure conditions. Measurement determines whether a policy adds value at executable prices. A convincing explanation can accompany a false discovery, while a reproducible empirical effect can exist before its mechanism is fully understood. Both uncertainty and alternative explanations must remain visible. [V1, V10, V12]

### How the disciplines connect

| Discipline | What it contributes | What an LLM must not infer |
| --- | --- | --- |
| Bayesian decision theory | Evidence updates distributions; actions depend on utility and prices | More confident language is a stronger likelihood ratio |
| Information economics | Information is costly; prices partly aggregate it | Public information is automatically useless or automatically mispriced |
| Game theory | Competitors infer, react, and choose under constraints | A profitable historical opponent remains exploitable forever |
| Microstructure | Fills, spreads, queues, impact, and latency select realized opportunities | Every displayed quote can be captured at size |
| Gambling and betting | Odds make break-even, bankroll, and payout asymmetry explicit | High hit rate, Kelly, or stake progression creates edge |
| Prediction markets | Forecasts interact with preferences, wealth, contract rules, and market design | A quoted price equals truth or similarly named contracts are identical |
| Asset pricing and insurance | Bad-state exposure and hedging demand can justify expected returns | Every risk premium is skill, or more variance means more compensation |
| Psychology | Attention, repetition, overconfidence, and disposition can affect behavior | A documented bias necessarily affects the marginal price enough to trade |
| Statistical science | Separate discovery, selection, confirmation, and monitoring | A low p-value after a large hidden search certifies the winner |
| Engineering and control | Preserve causal timing, capital, reproducibility, and correct execution | More complexity or faster polling necessarily improves economic value |

### A concrete illustration of the change in thinking

Suppose a model estimates a binary event probability of 0.56. A contract paying one unit costs 0.52, and deterministic all-in costs are 0.015 per contract. Its modeled expected net payoff is 0.025. That is a hypothesis about a payoff, not a discovered profit stream.

Now suppose passive orders fill mainly during states where the conditional event probability is 0.50. The filled contract has expected payoff -0.035. The original forecast can be reasonably calibrated across all opportunities and still fail where the strategy receives fills. Improving a language model's broad prediction accuracy may do less than measuring this selection effect and changing the execution policy. All numbers here are illustrative, and the conditional probability must be estimated prospectively rather than assumed. [I03; original calculation]

A second hypothetical strategy wins one unit 99% of the time and loses 150 units otherwise. Its expected payoff is -0.51. Calling it risk warehousing does not change that arithmetic. Even a positive premium would require joint tail, liquidity, and capital analysis before it could be considered suitable.

### Designing intelligence that is economically useful

The strongest agentic desk is not the one that thinks hardest about every observation. It is the one that spends the next unit of analysis where it can change the decision before the opportunity disappears. This study proposes testing an adaptive research policy: use a cheap calibrated model first; request additional evidence only when estimated decision improvement exceeds its money and delay costs; stop at a defined decision deadline. Repeated news and multiple agents drawing on one source must count as one evidence lineage. This is an untested design hypothesis, grounded in decision value and attention theory, not a claim of achieved alpha. [I06, I07, I11]

Likewise, the best improvement to a strategy may be a subtraction: remove an unhelpful filter, stop trading opportunities whose costs exceed their forecast advantage, reduce overlapping tail exposure, or eliminate timing leakage. Another improvement may be a different use of the same signal: a slower execution schedule, a more suitable payoff contract, or a smaller position that retains favorable marginal economics. These are candidates to compare against the frozen baseline, not universal prescriptions. [S3, S4]

### Scope and evidence policy

The following chapters combine academic primary papers, author manuscripts, institutional research records, and official contract documentation across the requested disciplines. The source register identifies versions and whether the work was examined through available body text, abstract, or metadata. It does not claim exhaustive access to every book, interview, article, or source on the internet. Historical findings are used to generate and constrain research, not to assert that the same returns remain available today.

The mathematical examples are hypothetical and the research blueprints are untested. No market backtest, broker execution, or live deployment was performed for this study. Formula checks and prompt-behavior evaluations validate the deliverable's internal reasoning and operating instructions; they are not strategy-performance evidence.

Read the foundations for the economic model, the mechanism blueprints for creation and improvement, and the validation protocol for deciding what evidence has actually been earned. The separate master prompt provides the operational instructions in a form that can be pasted into another LLM. The installed skill adds selective access to the full reference material.
