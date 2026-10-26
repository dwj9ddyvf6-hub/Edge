# Adaptive-control source register

Research checked October 24, 2026 UTC. This pass adds **30 distinct primary-source entries** to the earlier 50-entry register. C08 is an explicit alias of earlier S3 and is not new. Sources include papers, author manuscripts, one official protocol specification, and official engineering articles. Alternate versions/URLs are not independent confirmations. This was targeted research and substantive inspection of specified sections, not an exhaustive literature review or proof-by-proof replication.

Controller design, examples, resource contracts and proposed experiments are original engineering synthesis or elementary derivations. A source's theory or historical result does not validate a proposed trading implementation. Where only abstracts were accessible, the entry says so. Verify current venue capabilities separately from historical specifications.

## Contents

- Control and computation: C01–C08
- Adaptive inference and learning: L01–L09
- Economics and feedback: E01–E06
- Runtime and distributed systems: O01–O07
- Causal transfer: X01

## Control and computation

### C01 — Boyd, Busseti, Diamond, Kahn, Koh, Nystrup and Speth

*Multi-Period Trading via Convex Optimization*. Foundations and Trends in Optimization 3(1), volume dated 2016, manuscript copyright 2017. [Author PDF](https://web.stanford.edu/~boyd/papers/pdf/cvx_portfolio.pdf). DOI 10.1561/2400000023.

**Inspected:** abstract and sections on omitted features, forecast error, multi-period use and computation. **Supports:** constrained planning with costs/risk, followed by first-action execution and replanning. **Limit:** explicitly does not produce the forecasts; basic trading assumptions require extension for partial fills, queueing and latency. Convexity is a property of a particular formulation, not every desk problem.

### C02 — Hamilton (2005)

*Regime-Switching Models*, author manuscript May 18, 2005 for Palgrave. [Author PDF](https://econweb.ucsd.edu/~jhamilto/palgrav1.pdf).

**Inspected:** model, filtering equations, smoothing and identification discussion. **Supports:** probabilities over unobserved states conditional on current information differ from retrospective smoothed probabilities. **Limit:** states and transition dynamics are model assumptions. Full-sample fitted parameters still leak future information even when the filtering recursion looks causal. Sparse transitions weaken estimates.

### C03 — Davis and Norman (1990)

*Portfolio Selection with Transaction Costs*. Mathematics of Operations Research 15(4), 676–713. [Publisher](https://pubsonline.informs.org/doi/abs/10.1287/moor.15.4.676).

**Inspected:** publisher abstract/metadata; full-paper retrieval unsuccessful. **Supports:** a no-transaction region in the paper's consumption/investment model with proportional costs. **Limit:** do not import its boundaries into jumps, discrete contracts or arbitrary portfolios. The simple one-period derivative condition in the addendum is a separate elementary derivation.

### C04 — Klenske and Hennig (2016)

*Dual Control for Approximate Bayesian Reinforcement Learning*. JMLR 17(127), 1–30. [Primary PDF](https://www.jmlr.org/papers/volume17/15-162/15-162.pdf).

**Inspected:** introduction, controller construction, experiments 6.2–6.4 and conclusion. **Supports:** actions can influence payoff and future information; relevance and timing of learning matter. **Limit:** approximate control of simulated dynamical systems is not demonstrated financial alpha. Exact Bayesian control is difficult; an uncertainty bonus alone is not its solution or an authorization to experiment live.

### C05 — Hansen and Sargent (2001)

*Robust Control and Model Uncertainty*. American Economic Review 91(2), 60–66. [Author PDF](https://larspeterhansen.org/wp-content/uploads/2016/10/Robust-Control-and-Model-Uncertainty.pdf).

**Inspected:** introduction, relative-entropy model uncertainty and time-consistency discussion. **Supports:** deliberate model-uncertainty preferences and constrained distortions around an approximating model. **Limit:** an ambiguity radius is not a posterior error probability. Resetting a whole-horizon distortion budget at every step can change the objective. Robustness only addresses the specified alternative models.

### C06 — Iyengar (2005)

*Robust Dynamic Programming*. Mathematics of Operations Research 30(2), 257–280. [Publisher](https://pubsonline.informs.org/doi/abs/10.1287/moor.1040.0129).

**Inspected:** publisher abstract and author bibliography; not full proofs. **Supports:** rectangular uncertainty structure enables the analyzed robust dynamic-programming counterpart. **Limit:** a finite scenario scorer or arbitrary persistent-model uncertainty does not inherit those guarantees. Independently selecting each period's worst transition can construct incoherent paths.

### C07 — Hay, Russell, Tolpin and Shimony (2012)

*Selecting Computations: Theory and Applications*. UAI. [Author PDF](https://people.eecs.berkeley.edu/~russell/papers/uai12-meta.pdf); [proceedings record](https://proceedings.mlr.press/r10/hay12a.html).

**Inspected:** metalevel formulation, stopping results and assumptions. **Supports:** allocate computation by expected decision improvement; myopic evaluation can miss complementary sequences. **Limit:** specific bounds assume their stated utility/sampling model. Markets evolve during computation; no universal trading compute budget follows.

### C08 — Alias of earlier S3

Gârleanu and Pedersen, *Dynamic Trading with Predictable Returns and Transaction Costs* (2013; inspected March 2012 author version). [Author PDF](https://nbgarleanu.github.io/DynTrad.pdf).

**Re-inspected:** model and partial-adjustment proposition. Predictable signals with quadratic costs motivate gradual trading toward a forward-looking target. Proportional-cost no-trade regions are a different result. This is one existing source, not an additional confirmation.

## Adaptive inference and learning

### L01 — Howard, Ramdas, McAuliffe and Sekhon (2021)

*Time-uniform, nonparametric, nonasymptotic confidence sequences*. Annals of Statistics; inspected author revision August 2022. [Primary PDF](https://arxiv.org/pdf/1810.08240).

**Inspected:** conditional concentration construction, introduction and discussion. **Supports:** simultaneous coverage over time under specified conditional tail assumptions. **Limit:** nonparametric does not mean assumption-free; arbitrary heavy-tailed P&L is not bounded. Running intersections for a constant parameter cannot be blindly reused for changing targets. Coverage is not a promise about future profit.

### L02 — Ramdas, Ruf, Larsson and Koolen (2022)

*Admissible anytime-valid sequential inference must rely on nonnegative martingales*. Inspected November 2022 author revision. [Primary PDF](https://arxiv.org/pdf/2009.03167).

**Inspected:** definitions and martingale/e-process framework. **Supports:** foundations connecting admissible anytime-valid procedures with nonnegative martingale methods. **Limit:** validity needs the null and actual information history. E-values are not posterior probabilities. The addendum's bounded-product example is an elementary specialization, with a deliberately strong conditional null.

### L03 — Waudby-Smith, Wu, Ramdas, Karampatziakis and Mineiro (2024)

*Anytime-valid off-policy inference for contextual bandits*. [Primary PDF, August 2024 revision](https://arxiv.org/pdf/2210.10768); [DOI](https://doi.org/10.1145/3643693).

**Inspected:** data assumptions, support, predictable tuning and time-varying values. **Supports:** adaptive logging and changing/dependent contexts under stated conditions; time-varying average conditional policy-value inference. **Limit:** target support and bounded reward requirements matter. Average value so far is not instantaneous edge. Endogenous future context from inventory or impact changes the interpretation of one-step comparisons.

### L04 — Dudík, Langford and Li (2011)

*Doubly Robust Policy Evaluation and Learning*. ICML. [Primary PDF](https://arxiv.org/pdf/1103.4601).

**Inspected:** estimator, bias result and variance discussion. **Supports:** combining propensity weighting with reward prediction can reduce bias under the specified nuisance-model conditions. **Limit:** zero support, confounding, leakage or wrong payoff definitions are not repaired. Large weights may dominate uncertainty. Keep nuisance fitting and candidate selection honest under dependence.

### L05 — Kazerouni, Ghavamzadeh, Abbasi-Yadkori and Van Roy (2017)

*Conservative Contextual Linear Bandits*. NeurIPS. [Author PDF](https://mohammadghavamzadeh.github.io/PUBLICATIONS/nips17.pdf).

**Inspected:** assumptions, performance constraint, algorithm and theorem conditions. **Supports:** exploration with a modeled cumulative expected-reward baseline constraint under linear, bounded and conditional-noise assumptions. **Limit:** this is not a realized drawdown or collateral guarantee. Multiplicative constraints for nonnegative rewards cannot be copied directly into signed trading P&L.

### L06 — Besbes, Gur and Zeevi (2014)

*Stochastic Multi-Armed-Bandit Problem with Non-stationary Rewards*. NeurIPS. [Primary PDF](https://proceedings.neurips.cc/paper_files/paper/2014/file/91ba7292e5388b90b58d0b839a7f19ec-Paper.pdf).

**Inspected:** variation budget, regret benchmark, lower bound and restart policy. **Supports:** achievable tracking depends on reward variation and the balance between memory and forgetting. **Limit:** comparator regret is not absolute profit. Fast-enough changes can preclude sublinear dynamic regret in the model. Financial feedback and costs need separate treatment.

### L07 — Joulani, György and Szepesvári (2013)

*Online Learning under Delayed Feedback*. ICML. [Primary PDF](https://proceedings.mlr.press/v28/joulani13.pdf).

**Inspected:** feedback protocol, delay assumptions and stochastic queue approach. **Supports:** feedback delays change learning guarantees. **Limit:** favorable delay conclusions need their stated assumptions. Trade duration may depend on action and payoff; quick-winner/slow-loser completion creates selection that cannot be ignored.

### L08 — Li, Chu, Langford and Wang (2011)

*Unbiased Offline Evaluation of Contextual-bandit-based News Article Recommendation Algorithms*. WSDM; inspected March 2012 author revision. [Primary PDF](https://arxiv.org/pdf/1003.5956).

**Inspected:** replay algorithm and theorem assumptions. **Supports:** matched-action replay under randomized logging and the stated i.i.d. setting. **Limit:** market-price replay is a simulator, not equivalent randomized logged executions; absent queue positions and impact remain unobserved. More replay cannot supply missing support.

### L09 — Choe and Ramdas (2026 accepted manuscript)

*Combining Evidence Across Filtrations*. March 15, 2026 revision of 2024 preprint; accepted JRSS B per author record. [Primary PDF](https://arxiv.org/pdf/2402.09698); [version record](https://arxiv.org/abs/2402.09698).

**Inspected:** definitions, financial example, combination and lifting results. **Supports:** coarse-history validity need not survive stopping using richer information; justified adjustment can lift processes across filtrations. **Limit:** arbitrary products or combinations across incompatible histories are invalid. Common-null, common-filtration averaging has different conditions from such combinations.

## Economics and feedback

### E01 — Elmachtoub and Grigas (2022)

*Smart “Predict, then Optimize”*. Management Science 68(1), 9–26; inspected November 19, 2020 arXiv v5. [Primary full text](https://arxiv.org/html/1710.08005v5); [DOI](https://doi.org/10.1287/mnsc.2020.3922).

**Inspected:** losses, framework and consistency assumptions. **Supports:** train predictions using downstream decision loss in a specified optimization problem. **Limit:** the consistency argument has continuity, symmetry and feasible-set conditions; unknown impact or drift is not automatically covered. A decision score is not necessarily a calibrated probability. Keep independent forecast and policy evaluation.

### E02 — Perdomo, Zrnic, Mendler-Dünner and Hardt (2020)

*Performative Prediction*. PMLR 119. [Primary PDF](https://proceedings.mlr.press/v119/perdomo20a/perdomo20a.pdf).

**Inspected:** definitions, convergence and assumptions. **Supports:** deployment can change the distribution being predicted. **Limit:** convergence requires model regularity and sufficiently weak distributional sensitivity in the analyzed result. Stability and optimality differ; an externally changing market need not follow a fixed deployment-to-distribution map.

### E03 — Miller, Perdomo and Zrnic (2021)

*Outside the Echo Chamber: Optimizing the Performative Risk*. PMLR 139. [Primary PDF](https://proceedings.mlr.press/v139/miller21a/miller21a.pdf).

**Inspected:** constructive counterexample, assumptions and optimization discussion. **Supports:** stable retraining can be very suboptimal for deployment-dependent outcomes. **Limit:** improving induced outcomes requires more structure than ordinary loss minimization. The result motivates evaluation against deployed consequences, not unrestricted live exploration.

### E04 — Berk and Green (2004)

*Mutual Fund Flows and Performance in Rational Markets*. Inspected author manuscript October 15, 2002. [Primary manuscript](https://users.nber.org/~confer/2002/apf02/berk.pdf); [author institution](https://www.gsb.stanford.edu/faculty-research/research/publications/mutual-fund-flows-performance-rational-markets).

**Inspected:** opening argument and increasing-cost/decreasing-return model. **Supports:** ability can coexist with limited persistent investor abnormal return as capital competes and scale changes efficiency. **Limit:** delegated-management equilibrium assumptions are not an estimated desk capacity curve. Distinguish captured dollars, return per dollar, fees and scarce-capital surplus.

### E05 — Greenwood and Thesmar (2011)

*Stock Price Fragility*. Journal of Financial Economics 102(3), 471–490. [Article PDF](https://tevgeniou.github.io/EquityRiskFactors/bibliography/Fragility.pdf); [DOI](https://doi.org/10.1016/j.jfineco.2011.06.003).

**Inspected:** fragility/co-fragility construction, sample and endogeneity cautions. **Supports:** common ownership and correlated liquidity needs can relate to volatility/comovement. **Limit:** historical US 1990–2007 ownership evidence is incomplete and lagged; comovement interpretations have endogeneity concerns. Use it to motivate shared-dependency analysis, not a current trading parameter.

### E06 — McDonald and Siegel (1986)

*The Value of Waiting to Invest*. Quarterly Journal of Economics 101(4), 707–727; earlier NBER 1019 (1982). [NBER record](https://www.nber.org/papers/w1019); [author institution](https://www.kellogg.northwestern.edu/academics-research/research/detail/1986/the-value-of-waiting-to-invest/).

**Inspected:** primary abstracts and publication record; full PDF denied. **Supports:** uncertainty and irreversibility can give waiting value beyond a positive-NPV rule. **Limit:** no paper-specific numerical threshold is imported; tradable securities differ from irreversible projects. Waiting must charge competition, quote loss and existing-position risk.

## Runtime and distributed systems

### O01 — Akidau et al. (2015)

*The Dataflow Model*. PVLDB. [Primary PDF](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf).

**Inspected:** event/processing time, triggers, windows and watermarks. **Supports:** explicit correctness/latency/cost tradeoffs for unbounded out-of-order streams. **Limit:** watermark progress does not establish a trading fact's prior availability. Corrections cannot retroactively inform an old decision.

### O02 — FIX Global Technical Committee (July 2020, EP258)

*Order State Changes*. [Official specification PDF](https://www.fixtrading.org/wp-content/uploads/download-manager-files/Order-State-Changes.pdf); [official landing page](https://fixtrading.org/packages/fix-latest-specification-order-state-changes/).

**Inspected:** version, cancel, replace and sequencing matrices. **Supports:** pending cancellation/replacement still permits execution; quantities and identifiers matter beyond headline status. **Limit:** the inspected document is dated 2020 despite “latest” in the page title. Verify each actual broker/venue protocol, corrections and reconnect behavior before coding an adapter.

### O03 — Featonby, Making Retries Safe with Idempotent APIs

[Official AWS Builders' Library article](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). Publication date not established; accessed October 24, 2026 UTC.

**Inspected:** tokens, atomic mutation, semantic equivalence and late requests. **Supports:** idempotency is a server/client contract with identity and retention semantics. **Limit:** assigning a UUID locally does not make an arbitrary broker endpoint idempotent. Ambiguous outcomes may require reconciliation rather than new-ID retries.

### O04 — Russell and Wefald (1989)

*On Optimal Game-Tree Search Using Rational Meta-Reasoning*. IJCAI. [Primary PDF](https://www.ijcai.org/Proceedings/89-1/Papers/053.pdf).

**Inspected:** value-of-computation, action selection and approximation assumptions. **Supports:** computations can be selected by expected improvement after time/cost. **Limit:** demonstrated game search is not financial alpha; LLM confidence is not measured information value. A one-step approximation may miss useful sequences.

### O05 — Dean and Barroso (2013)

*The Tail at Scale*. [Author PDF](https://www.barroso.org/publications/TheTailAtScale.pdf); [author research record](https://research.google/pubs/the-tail-at-scale/).

**Inspected:** queueing/shared resources and fan-out latency. **Supports:** tail delays can dominate systems waiting for many branches. **Limit:** web-service results are not measured trading latency. Redundant read-request techniques cannot justify duplicating mutating orders. Benchmark the actual end-to-end workload.

### O06 — Sculley et al. (2015)

*Hidden Technical Debt in Machine Learning Systems*. NeurIPS. [Primary PDF](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf).

**Inspected:** data dependencies, entanglement, feedback and configuration. **Supports:** operational complexity extends beyond the fitted model. **Limit:** simplicity does not automatically create profit; compare incremental value against maintenance and failure burden. Explicit ownership and dependencies make changes reviewable.

### O07 — Lamport (1978)

*Time, Clocks, and the Ordering of Events in a Distributed System*. [Author-hosted PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Time-Clocks-and-the-Ordering-of-Events-in-a-Distributed-System.pdf).

**Inspected:** happened-before, logical clocks and total order. **Supports:** consistent ordering from communication dependencies. **Limit:** logical order does not establish physical-time order in the converse direction. Deterministic replay cannot repair clock error or prove an economic lead-lag relation.

## Causal transfer

### X01 — Peters, Bühlmann and Meinshausen (2016 publication)

*Causal inference by using invariant prediction: identification and confidence intervals*. JRSS B 78(5), 947–1012. [Author preprint record](https://arxiv.org/abs/1501.01332); [inspected PDF](https://arxiv.org/pdf/1501.01332).

**Inspected:** invariance assumption, Proposition 1, Theorem 1, hidden-variable and target-intervention qualifications. Record identifies November 2015 v3; retrieved PDF displays a later compilation date, not treated as a new study. **Supports:** invariance across appropriate environments can restrict causal predictors under structural assumptions. **Limit:** restrictions on interventions affecting the target and confounding matter. Stable backtest bins do not establish causality; an empty identified set can be the honest result.
