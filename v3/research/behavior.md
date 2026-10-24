# From an edge thesis to observable LLM behavior

Audit and research date: 2026-10-24. This document audits the v2 baseline and specifies a falsifiable evaluation of a proposed v3. It does not report a completed market experiment or claim that a prompt creates profitable forecasts.

## 1. What the existing skill actually contains

The audit covered `v2/skill/SKILL.md`, all eight reference files (`foundations`, `mechanisms`, `validation`, `sources`, `adaptive-control`, `adaptive-learning`, `desk-runtime`, `adaptive-sources`), both Python files, and `Trading_Edge_Unified_Master_Prompt.txt`. The reference lists were inspected as part of the artifact; this is not a claim that every underlying cited paper was reread in this behavioral audit. The additional primary literature inspected for this document is listed below.

**Finding:** The screenshot's ideas are operational instructions in v2, not merely a list of fashionable topics. The missing link is strong evidence that this particular instruction package reliably changes a particular model's decisions, followed by separate evidence that those decisions produce an executable economic advantage.

| Screenshot concept | Existing requirement in the baseline | What the requirement makes the model produce | What has not thereby been established |
|---|---|---|---|
| Information advantage | SKILL §§2–4; foundations §§3, 5–8 | A price-setting participant, a specific information difference, as-of inputs, an executable break-even condition, and competing explanations | That a proposed signal contains information beyond the market's information set |
| Faster updating | SKILL §§4, 9; adaptive-control research allocation; desk-runtime latency contracts | Signal decay, costs of delay, deadlines, a feasible fallback and end-to-end latency requirements | Measured production latency or a profitable speed advantage |
| More accurate Bayesian updating | SKILL §4; foundations §6 | Prior odds and defensible conditional likelihood ratios; explicit avoidance of correlated-source double counting | Correctly estimated likelihoods, calibrated forecasts or independent evidence from multiple agents |
| Access unavailable to the marginal participant | SKILL §§2–3, 6; mechanisms §§5–6, 9 | The constraint, lawful access difference, capacity and persistence of the wedge | Actual executable access, borrow, settlement equivalence or a financeable path |
| Risk warehousing | SKILL §5; foundations §§4, 9; mechanisms §§4–5, 7 | Paid service, adverse state, capital occupation, margin, liquidity, portfolio overlap and willingness to bear the loss | A sufficiently large premium, accurate tail model or adequate live balance sheet |
| Taking variance others dislike | SKILL §§2, 5; foundations §§2, 4 | A correction: raw variance is insufficient; evaluate state dependence and marginal portfolio utility | That all volatile strategies earn a premium, or that positive carry is alpha |

The distinction between expected profit, exposure-adjusted alpha, portfolio utility and statistical evidence is particularly valuable. It allows a useful hedge with negative standalone expected return, while preventing a risky premium from being relabeled as information superiority. The skill also explains how counterparties can both gain utility from risk transfer. This is more precise than a universal “someone else must be stupid” account of trading.

The ten mechanism blueprints already support constructive research, including information transmission, fill-conditioned calibration, forced flows, risk complementarity, capital occupation, contract semantics, research expenditure, latency/capacity and strategic response. A fair audit therefore should not claim that v2 lacks creativity. The improvement is to make creativity and successful identification of a feasible opportunity explicitly measurable, alongside rejection of false opportunities.

## 2. Four different meanings of “encode”

1. **Represent the principles in an artifact.** This is established by inspecting the prompt and references. The rules exist and specify outputs.
2. **Condition a model to use the principles.** A loaded prompt can influence an inference session. Whether the model actually performs the intended operations is an empirical question. Brown et al. demonstrate task conditioning through supplied text without gradient updates; that mechanism is different from changing model weights [B01].
3. **Develop a reliable capability.** Reliability requires unseen tasks, repeated runs, meaningful scoring, robustness to phrasing and follow-up changes, and a comparison condition. It is not established by self-description or one persuasive answer.
4. **Acquire an economic advantage.** This requires appropriate data, feasible actions, forecast and execution comparisons, realistic costs and prospective evidence. Reasoning correctly about a toy payoff is useful evidence about reasoning, not evidence of a market surplus.

An installed skill is external procedural knowledge made available to the model. Reading it does not demonstrate parameter training or permanent internalization. A skill can fail to be loaded, be only partly followed, or interact poorly with other context. Conversely, a strong base model may already solve a task without the skill. Both possibilities must remain visible in the evaluation.

The useful claim is: **the package specifies, supports and tests disciplined edge research.** A stronger claim must identify the model, version, operating context, measured task family and observed effect. Persona titles, verbosity, source count and confidence do not supply that evidence.

## 3. What the included code proves and does not prove

The finite-menu `adaptive_arbiter.py` consumes supplied model outcomes, utility differences, evidence flags, timestamps, limits, positions and possible pending fills. It evaluates feasibility and paired robust improvement, and returns an action or a recovery-oriented result. Its synthetic tests cover meaningful hazards such as inconsistent timing, expiry, malformed inputs, duplicate identifiers, unknown own state, correlated exposure and pending execution.

Those checks help establish internal behavior of that reference implementation under supplied inputs. They do not establish that an evidence flag is true, that forecast scenarios are calibrated, or that a proposed utility model is appropriate. The script does not discover information, estimate risk compensation, synthesize strategies, route real orders or provide a complete durable reservation/reconciliation service. The baseline explicitly describes it as offline; v3 should preserve that boundary.

There are therefore separate test suites:

- **Artifact checks:** references, required instructions, reproducibility and version consistency.
- **Behavioral checks:** the model reaches the right actionable conclusion from supplied evidence and explains the relevant limits.
- **Model/economic checks:** probabilities, counterfactual estimates and net portfolio values survive appropriate comparisons.
- **Operational checks:** the implemented system respects constraints during stale data, partial execution, retries, restarts and uncertain state.

Passing one suite cannot substitute for the others.

## 4. Material improvements recommended for v3

### Make incremental information the unit of research

The baseline already says to compare with information in prices. Promote this into an explicit operation: define the common information set, define the new observation, estimate its conditional contribution, and test the decision at the executable quote. A signal can be predictive unconditionally but redundant once public information and the market state are known. Several agents repeating the same source are still one observation. Measure calibrated improvement and decision value in prospectively defined price, horizon and liquidity buckets.

Do not automatically treat a price as a physical probability. State any de-vigging, risk-neutral-to-physical adjustment or modeling assumption. “The market is wrong” must have an identified payoff, conditional information and a plausible competition story.

### Make portfolio state coupling explicit

For a warehouse, write the joint scenarios of existing wealth, proposed payoff, funding demand and liquidation capacity. Show a reservation-value or utility comparison when inputs permit. Two contracts can have the same standalone distribution and very different portfolio value because they pay in different states. This gives the screenshot's intuition a computable decision rule while avoiding the claim that raw variance earns compensation.

### Test constructive ability, not just caution

Require a small set of diverse feasible candidates, a comparison, and the next decisive authorized research step. Evaluate whether the model can recognize a valid positive opportunity under explicit assumptions, repair a failed construction when feasible, and design an informative experiment. An answer that always says “insufficient evidence” should fail cases where the supplied data identify a useful result.

Separate an original combination from a demonstrated literature novelty claim. A useful research proposal need not be unprecedented; it must expose a mechanism, data path, rival explanation, actionable implication and way to fail.

### Turn instructions into observable obligations

For each important principle, specify a minimum observable artifact: a posterior calculation, a state-by-state payoff table, a cost-adjusted action, a constraint-preserving candidate, or a valid statement of what cannot be identified. Score the substance. Mentioning “Bayes,” “Kelly,” “robust,” or “counterfactual” is not a pass.

Keep the core prompt compact enough to make these obligations salient; use references for derivations and alternative methods. More text can increase coverage without increasing adherence. Measure both.

### Keep memory, confidence and authority separate

At the start of a substantial continuation, reconstruct the active objective, latest constraints, approved policy, evidence state and unresolved questions. A prior research suggestion must not become execution authority through repetition. Model confidence is a claim about an answer; a physical event probability needs its own elicitation and validation. Research on self-evaluation finds task/format dependence and difficulties transferring calibration [B06].

### Attribute improvements to the right component

Record the prompt, base model, retrieval, tools, data version, aggregation and any training separately. Published forecasting systems can combine several of these components; their performance cannot be credited to a role prompt alone [B04]. Compare against an equally resourced simple baseline. Add an ablation only when it answers a useful attribution question.

## 5. Frozen exploratory behavioral evaluation

The accompanying `evaluations/cases.json` contains six self-contained cases. `evaluations/rubric.json` contains the separate scoring rules. The builder is an authoring artifact, not solver input. The cases require no market research, real-money action or unavailable observations. They include numerical decisions and constructive research design. Answers are deliberately not repeated here.

The cases and rubric were frozen before disclosure to the v3 author. The author was instructed to finalize the candidate core before reading evaluation contents. A SHA-256 digest of each frozen file was communicated separately. This reduces direct adaptation to the items; it does not create external independence, since the benchmark designer knew the baseline and the research objective.

### Protocol

1. Freeze the candidate prompt/skill and record its content hash. Record model identifier and sampling settings when exposed; otherwise mark them unknown.
2. Run two fresh sessions with generic task instructions and no Edge artifact, and two fresh sessions with the frozen v3 artifact. Each session receives the same six cases and a total 2,500-word response cap. Neither condition receives the rubric, builder, other answers or evaluation findings.
3. Use the same base model, available tools and operating constraints. Specify precisely which artifact the skill condition receives. If skill metadata is already present in both environments, disclose that; a no-body baseline is not a completely unaware baseline.
4. Restrict solver reading to the specified material. Shared storage and instruction-only restrictions are weaker than enforced isolation; report any observed deviation. Preserve complete outputs and access records available from the environment.
5. Score four binary criteria per case, 24 per session. Recalculate numerical answers independently. For open-ended proposals, require the rubric's economic and experimental properties without demanding the author's preferred narrative. Record quoted support, omissions and critical errors separately.
6. Where feasible, anonymize condition and answer order for the grader. An LLM judge can assist, but cannot replace explicit numerical verification or adjudication of disputed semantic criteria. LLMBar gives a direct reason to examine whether appealing prose misleads a judge [B03].
7. Report case-level and item-level results, all critical errors and the actual condition difference. If both conditions reach the ceiling, report no demonstrated gain on these cases. Do not alter the rubric to produce a desired outcome.

### Identification limits

Four sessions over six shared cases yield 24 case responses, not 24 independent estimates of a prompt effect. Answers share a model, tasks and session context; the sample is small and purpose-built. There is no justified estimate of a population-wide improvement, no evidence of orders-of-magnitude gains, and no profitable-trading claim. Inability to control seeds, sampling, latent model changes or environment details further limits interpretation.

The comparison is a diagnostic of whether specified operations appear in the observed outputs. It can expose important failures and establish that the task is solvable. A favorable result remains exploratory. After the cases or rubric are published, use them as regression checks; a later confirmatory evaluation requires new tasks that were not used to revise the skill.

For a stronger subsequent study, preregister a larger task population, independent case authors, repeated runs, equivalent resource budgets, paraphrases, changed numbers and multi-turn constraint updates. Include beneficial-action cases as well as rejection cases. Predeclare failure costs and the primary metric. Use appropriate clustered uncertainty, retain all runs, and report task-family heterogeneity. Test a compact core against the full package to measure whether reference length adds benefit.

## 6. Forecast and market evaluation after behavioral testing

A behavioral benchmark should lead to a separate prospective ledger: event definition, available information, forecast timestamp, probability, executable quote, action set, costs, fill status, policy/model version and eventual resolution. Pending labels remain pending. Resolution rules must be fixed before outcomes. ForecastBench's future-event design is relevant to preventing known resolutions from contaminating submission-time forecasting [B05]; it does not remove every source of selection bias or imply trading profitability.

Evaluate proper scores against timely baselines, then evaluate whether improvements matter near feasible action thresholds and conditional on execution. Separate the value of information from the value of inventory, risk transfer, cheaper execution and changing exposure. Avoid converting a better forecasting score into a return claim without the payoff and fill mapping.

The complete evidence chain is:

**specified instruction → observed task behavior → prospective predictive evidence → executable portfolio value → operationally controlled deployment.**

Each arrow is an experiment or an implementation task. None is supplied by rhetorical confidence.

## 7. Additional primary-source register

Access date for all entries: 2026-10-24. The listed versions, not an assumed current leaderboard, support the statements above. The proposed evaluation protocol is an original application to this skill, not a protocol validated by these papers.

### B01 — Brown et al., Language Models are Few-Shot Learners

- Source: [arXiv:2005.14165](https://arxiv.org/abs/2005.14165), submitted 2020-05-28; v4, 2020-07-22.
- Access: abstract and version metadata.
- Contribution: demonstrates task specification through text/examples without task-specific gradient updates in the studied system.
- Application: distinguish inference-time context from parameter training. This does not establish adherence, permanence, financial forecasting ability or the behavior of every later model.

### B02 — Zhou et al., Instruction-Following Evaluation for Large Language Models

- Source: [arXiv:2311.07911v1](https://arxiv.org/html/2311.07911v1), 2023-11-14.
- Access: introduction, instruction/prompt construction, metric definitions, results and limitations.
- Contribution: evaluates verifiable instructions using explicit checking; discusses strict and relaxed criteria and checking errors.
- Application: replace topic-name recognition with observable requirements. Format compliance alone does not measure financial reasoning; the proposed numerical and semantic rubric extends the idea rather than inheriting a validated finance benchmark.

### B03 — Zeng et al., Evaluating Large Language Models at Evaluating Instruction Following

- Source: [arXiv:2310.07641v2](https://arxiv.org/html/2310.07641v2), revised 2024-04-16; ICLR 2024.
- Access: abstract, benchmark construction, evaluator strategies and experimental results.
- Contribution: LLMBar tests evaluation on answer pairs where superficially attractive responses can violate instructions; the paper examines evaluator behavior and prompting strategies.
- Application: score actual requirements, verify arithmetic independently, blind condition where possible and inspect order sensitivity. The paper does not establish reliability of an arbitrary judge on this benchmark.

### B04 — Halawi et al., Approaching Human-Level Forecasting with Language Models

- Source: [arXiv:2402.18563v1](https://arxiv.org/html/2402.18563v1), 2024-02-28.
- Access: retrieval/reasoning/aggregation design, fine-tuning and optimization, ablations and limitations.
- Contribution: studies a forecasting system using multiple components and ablates parts of that system. The evidence concerns the evaluated forecasting task and system, not a standalone instruction that guarantees forecasting gains.
- Application: version and compare prompt, retrieval, aggregation and training separately. Historical probability-forecasting performance cannot be transferred directly to executable trading returns or current model rankings.

### B05 — Karger et al., ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities

- Sources: [inspected full-text v3](https://arxiv.org/html/2409.19839v3), 2024-12-02; [version record](https://arxiv.org/abs/2409.19839), latest listed v5, 2025-02-28.
- Access: question construction, submission/resolution/scoring design and conclusions in v3; version metadata for v5. No claim of a full-text v5 review.
- Contribution: constructs regularly refreshed forecasting questions whose outcomes are unresolved at submission.
- Application: use prospective timestamps, fixed resolution rules and mature outcomes. Future resolution protects against a particular form of answer leakage; it is not a universal guarantee against contamination, dependence or selection bias. No current leaderboard conclusion is asserted here.

### B06 — Kadavath et al., Language Models (Mostly) Know What They Know

- Source: [arXiv:2207.05221v4](https://arxiv.org/abs/2207.05221), 2022-11-21.
- Access: abstract and introductory framing.
- Contribution: studies self-evaluation probabilities, elicitation formats and transfer; reports limitations in calibration on new tasks.
- Application: distinguish confidence in an answer from a calibrated probability of a market event. A self-reported confidence number requires task-specific evaluation; the title is not permission to treat model certainty as measurement.

### B07 — Laban et al., LLMs Get Lost In Multi-Turn Conversation

- Source: [arXiv:2505.06120v1](https://arxiv.org/html/2505.06120v1), 2025-05-09.
- Access: simulation design, single-/multi-turn comparison, limitations and qualitative failure analysis.
- Contribution: examines reliability when task information arrives over multiple turns and identifies persistence of premature assumptions in the studied tasks and models.
- Application: reconstruct the active constraint set and test follow-up changes explicitly. The reported performance drop is not an estimated effect for Edge, trading, or every current model. Consolidation is a proposed design response requiring its own evaluation.

## Status at preparation

Baseline audit completed; seven additional primary sources inspected at the access depth stated; six challenge tasks and separate rubric frozen. Behavioral scores and economic results are not asserted in this document. Any completed comparison belongs in a separately dated run report with artifact hashes and preserved answers.
