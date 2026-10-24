# Information that changes an executable decision

Research pass: 24 October 2026, America/New_York. Six additional primary works are selected below; none appears in the original or adaptive source registers. Blackwell (1953), Sims (2003), market microstructure, and the existing value-of-computation literature remain foundations already counted in earlier passes. This is targeted inspection, not proof-by-proof replication. The formulas and examples labeled derivation are analytical synthesis, not reported market results.

## What should change in the skill

An information edge is relative to a counterparty information set, decision, price, time and feasible action. Require the LLM to name those five objects. A predictive variable can be useless at the available price; a redundant source can appear impressive; a weak standalone signal can become valuable in combination; and an accurate forecast can fail on the subset that actually fills.

Replace “find more informative signals” with a sequence of questions:

1. **Availability:** What fact is newly available to this desk, when, and from which original source? Distinguish information arrival from a model's new computation on an old fact.
2. **Increment:** What does the source add beyond executable price, public context and existing signals at the same timestamp? Use a frozen price/context-only baseline and an augmented baseline.
3. **Interaction:** Is the addition redundant, independently useful or useful only jointly with another observable? A one-variable ablation alone cannot rule out complementarity.
4. **Decision:** Which feasible action changes, at what price/cost threshold, and what regret or utility reduction is expected?
5. **Capture:** Is the information still useful at decision completion and conditional on the resulting execution? Track fills, nonfills, route, size and latency.
6. **Evidence:** Does the increment survive chronological evaluation, candidate search and outcome maturity? State the available sample and uncertainty; do not estimate theoretical quantities from a narrative.

Price is an observable input and executable constraint, not automatically a physical probability or transparent representation of every competitor's information. Comparison against price does not mean assigning it an invented Bayesian prior. Define the prior and likelihood separately; use price/context as additional information where the model supports that conditioning.

## Six new primary-source entries

### IF01 — Matějka and McKay, rational inattention to discrete choices

Filip Matějka; Alisdair McKay. *Rational Inattention to Discrete Choices: A New Foundation for the Multinomial Logit Model*. AER 105(1), 272–298 (2015). Inspected author manuscript explicitly dated January 2013, despite its hosting filename.

- Publication: https://doi.org/10.1257/AER.20130047
- Inspected PDF: https://economics.yale.edu/sites/default/files/matejka-140218.pdf
- Inspected: information-cost formulation, Definition 1, Theorem 1 and interpretation, manuscript pp. 10–13.
- Result and limit: the finite-action problem maximizes expected value minus a Shannon-information charge. Optimal choice probabilities include endogenous unconditional weights; ordinary softmax emerges only in a special case. This is an information-acquisition model with specified prior and utility, not evidence that an LLM's temperature estimates rational uncertainty or that a trader should randomize orders. Use it to ask which uncertainties are worth resolving given the decision stakes.

### IF02 — Bertschinger et al., unique and synergistic information

Nils Bertschinger, Johannes Rauh, Eckehard Olbrich, Jürgen Jost, Nihat Ay. *Quantifying Unique Information*. Entropy 16(4), 2161–2183 (2014); inspected arXiv v2, 16 January 2014.

- https://arxiv.org/pdf/1311.2852
- Publication DOI: https://doi.org/10.3390/e16042161
- Inspected: introduction, operational decision interpretation and marginal-channel construction, pp. 1–5.
- Result and limit: finite variables can contain redundant, unique and synergistic information. The proposed decomposition uses specific axioms and optimization; it is not the only possible information decomposition. Conditional mutual information includes synergy and should not be renamed unique information. Engineering consequence: preserve joint features when useful and test complementary bundles; suppressing every individually uninformative feature can discard an effective combination.

### IF03 — Banerjee et al., channel deficiencies

Pradeep Kr. Banerjee, Eckehard Olbrich, Jürgen Jost, Johannes Rauh. *Unique Informations and Deficiencies*. Allerton 2018; corrected arXiv v3, 9 December 2019.

- https://arxiv.org/pdf/1807.05103
- https://arxiv.org/abs/1807.05103
- https://doi.org/10.1109/ALLERTON.2018.8635984
- Inspected: Definition 7, Proposition 8, proof and correction note.
- Result: approximate channel simulation bounds decision loss under specified finite channels, prior and bounded losses. Input and output deficiencies differ. Empirical reconstruction fit is not a universal certificate; use the corrected version.

### IF04 — Noarov et al., forecasts conditioned on downstream decisions

Georgy Noarov, Ramya Ramalingam, Aaron Roth, Stephan Xie. *High-Dimensional Prediction for Sequential Decision Making*. ICML/PMLR 267, 46762–46783 (2025). Inspected the earlier author arXiv v2, 27 October 2023; publication metadata checked separately.

- https://proceedings.mlr.press/v267/noarov25b.html
- https://arxiv.org/html/2310.17651v2
- Inspected: protocol, Definitions 2.1–2.9, event-conditional unbiasedness and predict-then-act formulation.
- Result and limit: prespecified families of events can condition on context and forecasts; the analyzed algorithms support downstream regret guarantees. Assumptions include bounded prediction/outcome domains, specified feedback, utility structure and an adversary independent of current learner randomness. These are cumulative guarantees, not current-profit or fill-counterfactual guarantees. Declare decision-relevant calibration cohorts instead of trusting only aggregate calibration.

### IF05 — Kearns, Roth and Ryu, information aggregation in agent networks

Michael Kearns, Aaron Roth, Emily Ryu. *Networked Information Aggregation via Machine Learning*. SODA 2026. Inspected arXiv v2, whose submission record is 10 October 2025; the rendered body shows a later compilation date, which is not counted as a separate paper.

- https://arxiv.org/html/2507.09683v2
- https://arxiv.org/abs/2507.09683
- Publication DOI: https://doi.org/10.1137/1.9781611978971.173
- Inspected: DAG protocol, Lemma 3.3, path coverage argument, general-function benchmark and finite-sample qualifications.
- Result and limit: under structured regression and feature-coverage assumptions, prediction-passing networks can approach a full-feature benchmark; depth and information allocation matter. The nonlinear benchmark has restrictions, including additive combinations of locally available classes. This is not a theorem about arbitrary conversational LLM ensembles. Compare agent arrangements against a single joint-input baseline, preserving provenance and interaction-bearing evidence.

### IF06 — Gopalan et al., tractable calibration decision loss

Parikshit Gopalan, Konstantinos Stavropoulos, Kunal Talwar, Pranay Tankala. *Efficient Calibration for Decision Making*. STOC 2026; inspected author preprint v1, 17 November 2025.

- https://arxiv.org/html/2511.13699v1
- Official proceedings listing: https://acm-stoc.org/stoc2026/toc.html
- DOI: https://doi.org/10.1145/3798129.3800919
- Inspected: calibration versus Bayes optimality; Definitions 2.3–2.7; structured post-processing; i.i.d. testing/learning assumptions.
- Result and limit: unrestricted calibration decision loss is difficult to estimate; restricting the post-processing family produces tractable cases. Perfect calibration is weaker than Bayes optimality. Omniprediction here is relative to declared losses, post-processings and data assumptions, not every market decision. Keep recalibration classes modest, fit them inside chronological development and validate the selected action policy separately.

## Equations that sharpen the implementation

### A. Information increment and decision increment are different — derivation

Let M denote decision-time public/market context, Z the proposed additional source and Y a finite outcome. With the *true* conditional distributions and natural logs,

`E[log(P(Y|M,Z) / P(Y|M))] = I(Y;Z|M)`.

This is an oracle log-score identity. With estimated models, held-out log-score improvement is model-dependent; it is not a direct measurement of the population conditional mutual information. Neither quantity is cash profit.

For a fixed feasible action set A and a common, integrable payoff function v(a,Y;M), free instant information has ex-ante decision value

`VOI(Z|M) = E_Z[max_a E[v(a,Y;M)|M,Z] | M] - max_a E[v(a,Y;M)|M] >= 0`.

The inequality follows because the informed policy can ignore Z and retain the old action. It does not establish a positive *net* value: acquisition cost, delay, changing quotes, restricted actions and implementation errors must be modeled. Define them in complete policy wealth paths before comparison, as v2 requires. More data can reduce entropy yet leave every feasible action unchanged.

### B. Compression bound — elementary finite-state specialization

Let K(s,z) be rich observations, L(s,r) a summary, pi the prior and T(r,z) a reconstruction kernel. Define

`epsilon_TV = sum_s pi(s) TV(K(s,.), (L T)(s,.))`.

For loss in `[0,B]`, simulating the rich policy from the summary adds at most `B * epsilon_TV` Bayes loss. With average KL at most epsilon nats, Pinsker/Jensen give `epsilon_TV <= sqrt(epsilon/2)`. These are model-conditional bounds, not empirical deployment guarantees. Unbounded P&L does not qualify. Practically, test summary versus full-input decisions chronologically; do not label estimated reconstruction a proved certificate.

### C. Two adversarial examples — constructed, not market estimates

**Complementarity:** A and B are independent fair bits; Y is their XOR. Each alone predicts Y with probability 1/2. Together they determine Y. Two agents that each transmit only the standalone posterior transmit `(1/2,1/2)` and destroy the interaction. Passing the relevant source facts lets a joint model recover it. This is a reason to test bounded feature bundles, not to keep every datum forever. If the execution price already compensates for that joint information, the result still supplies no trade.

**Selection breaks aggregate trust:** a model always reports 0.60. Half the population has true event probability 0.90 and half 0.30, so it is perfectly calibrated in aggregate. A router selects only the second half. For a unit-paying binary contract priced at 0.58 with cost 0.01, selected expected payoff is `0.30 - 0.58 - 0.01 = -0.29`, despite the unselected aggregate suggesting +0.01. A calibration claim only over the forecast output does not cover decisions using richer routing information. Prespecify relevant context/action cohorts and separately model fill selection.

## Two inventive combinations to test

### Hypothesis H-IF1: decision-boundary novelty routing

Combine source provenance, a price/context-only forecast, a small set of additional evidence bundles and the current executable break-even surface. Reserve expensive extraction for cases where defensible action-value bounds straddle that surface. Route only the bundle expected to alter the feasible action before expiry; retain cheap baseline decisions elsewhere. This combines informational distinctness with decision value rather than generic sentiment novelty.

Test on an identical, independently specified opportunity stream against price/context-only, always-deep and fixed-budget random-review policies. Freeze bundle selection and cost accounting. Measure net utility per opportunity, missed profitable opportunities under an explicit simulator, live-observed capture where available, calibration in selected cohorts, tail latency and compute dollars. Falsifier: gains disappear after source timestamps, selection, missing outcomes or total costs are corrected. Do not claim shadow quotes identify real counterfactual fills.

### Hypothesis H-IF2: synergy-preserving evidence relay

Give specialists complementary bounded evidence sets. Require each message to include source IDs, timestamp, typed observations, important interactions, uncertainty and a prediction. Let one integrator access the specific joint facts needed for the hypothesis. Compare this with conclusion-only voting and a single joint-input model under the same token/time budget. Add a prespecified XOR-like synthetic fixture and realistic contract/filing interaction fixtures.

The hypothesis is that provenance-preserving communication improves decision accuracy and reduces duplicate evidence without paying for unrestricted fan-out. Falsifier: no improvement over the matched-cost single model, or added latency consumes the effect. The networked-learning papers motivate an information-bottleneck test; they do not certify this LLM architecture. Keep the surviving design as small as measured results permit.

## Search boundary and discarded lead

The search located *Optimal Rates for Agentic Networked Information Aggregation*, arXiv:2609.05318, dated 4 September 2026. Its indexed primary abstract was visible, but direct primary full-text retrieval failed. It is a useful follow-up lead, not counted among the six inspected sources and not used to promise rates for this skill. Similarly, the six works above do not establish profitable trading or persistent encoding in model weights. They justify sharper instructions and testable behavior contracts.
