# Frontier source register

Research pass: 24 October 2026, America/New_York. These 19 economic/information research projects extend the previous 80 distinct entries. Inspection is limited to the portions stated. A preprint, theoretical result, empirical study and our proposed engineering application have different evidentiary status. Detailed working notes are archived in the Edge repository's v3 research directory. Existing Blackwell, Sims, Kelly, market-microstructure and adaptive-control sources remain applicable and are not counted again.

## Contents

1. Information and decisions — IF01–IF06
2. Portfolio risk and intermediation — WR01–WR07
3. Invention, contracts and transport — F01–F06

## Information and decisions

### IF01 — Matějka and McKay (2015)

*Rational Inattention to Discrete Choices: A New Foundation for the Multinomial Logit Model*. [Publication](https://doi.org/10.1257/AER.20130047); [inspected January 2013 manuscript](https://economics.yale.edu/sites/default/files/matejka-140218.pdf). Inspected information-cost formulation, Definition 1 and Theorem 1. Application: choose information by decision stakes and acquisition cost. Endogenous choice weights matter; LLM sampling temperature is not this economic model.

### IF02 — Bertschinger et al. (2014)

*Quantifying Unique Information*. [Author text, January 2014 v2](https://arxiv.org/pdf/1311.2852); [publication](https://doi.org/10.3390/e16042161). Inspected finite-variable setup and operational interpretation. Application: retain potentially complementary evidence bundles. This is a particular decomposition; conditional mutual information includes synergy and is not simply unique information.

### IF03 — Banerjee et al. (2018; corrected 2019)

*Unique Informations and Deficiencies*. [Corrected v3](https://arxiv.org/pdf/1807.05103); [record](https://arxiv.org/abs/1807.05103). Inspected Definition 7, Proposition 8 and correction. Application: assess whether a summary preserves decision-relevant information. Bounds require specified channels, prior and bounded loss; fitted reconstruction is not a universal certificate.

### IF04 — Noarov et al. (ICML 2025)

*High-Dimensional Prediction for Sequential Decision Making*. [Publication](https://proceedings.mlr.press/v267/noarov25b.html); [inspected earlier author v2](https://arxiv.org/html/2310.17651v2). Inspected protocol, Definitions 2.1–2.9 and event-conditioned prediction. Application: audit calibration on prespecified decision cohorts. Cumulative regret under bounded feedback assumptions does not establish present trading profit.

### IF05 — Kearns, Roth and Ryu (SODA 2026)

*Networked Information Aggregation via Machine Learning*. [Inspected arXiv v2](https://arxiv.org/html/2507.09683v2); [record](https://arxiv.org/abs/2507.09683); [publication](https://doi.org/10.1137/1.9781611978971.173). Inspected DAG protocol, path coverage and function-class restrictions. Application: preserve evidence through agent handoffs and compare with a joint-input model. Structured-learning guarantees do not establish arbitrary LLM ensemble superiority.

### IF06 — Gopalan et al. (STOC 2026)

*Efficient Calibration for Decision Making*. [Inspected November 2025 v1](https://arxiv.org/html/2511.13699v1); [official listing](https://acm-stoc.org/stoc2026/toc.html). Inspected definitions, structured post-processing and i.i.d. learning assumptions. Application: make calibration audits computationally attainable with declared classes. Calibration is weaker than Bayes optimality; omniprediction is relative to specified losses and comparators.

## Portfolio risk and intermediation

### WR01 — Owen and Žitković (2009)

*Optimal Investment with an Unbounded Random Endowment and Utility-Based Pricing*. [Inspected September 2007 v2](https://arxiv.org/pdf/0706.0478); [author record](https://web.ma.utexas.edu/users/gordanz/publications/index.html). Inspected admissibility assumptions and utility-pricing definitions. Application: value risk against existing endowment and the same feasible hedge set. Subjective reservation value is not a unique market price.

### WR02 — Avellaneda and Stoikov (2008)

*High-Frequency Trading in a Limit Order Book*. [Author PDF](https://math.nyu.edu/inmemoriam/avellaneda/HighFrequencyTrading.pdf). Inspected reservation bid/ask and arrival model. Application: inventory-dependent valuation is separate from attainable quoting. Brownian/CARA/Poisson assumptions do not cover arbitrary queue priority, jumps, adverse selection or margin.

### WR03 — Gârleanu and Pedersen (2011)

*Margin-Based Asset Pricing and Deviations from the Law of One Price*. [Author PDF](https://pages.stern.nyu.edu/~lpederse/papers/MarginPricingLoOP.pdf). Inspected Proposition 1 and empirical qualifications. Application: identify actual financing access and collateral constraints. A published borrowing spread need not equal the desk's effective capital shadow price.

### WR04 — He and Krishnamurthy (2013)

*Intermediary Asset Pricing*. [Author PDF](https://zhiguohe.net/wp-content/uploads/2023/12/he-krishnamurthy-2013-intermediary-asset-pricing.pdf). Inspected equity-capital constraint and risk-premium mechanism. Application: distinguish scarce risk-bearing equity from debt-funding access. The equilibrium model does not supply an implemented real-time signal.

### WR05 — Duffie et al. (2023)

*Dealer Capacity and U.S. Treasury Market Functionality*, NY Fed Staff Report 1070, October revision. [Primary PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1070.pdf). Inspected capacity measurement and sample. Application: recreate as-of, accessible predictors. Full-sample normalization and unavailable dealer data cannot be silently imported into live replay.

### WR06 — Kashyap, Stein, Wallen and Younger (2025)

*Treasury Market Dysfunction and the Role of the Central Bank*. [Author record](https://stein.scholars.harvard.edu/publication/treasury-market-dysfunction-and-role-central-bank); [published PDF](https://stein.scholars.harvard.edu/sites/g/files/omnuum5951/files/2025-12/BPEA-SP25_WEB_Kashyap_Stein_Wallen_Younger.pdf). Inspected separate-leg margin and capital/funding distinction. Application: verify account-level collateral deadlines. A terminal hedge does not guarantee interim financeability.

### WR07 — Fleming, Liu and Nguyen (2026 working paper)

*Intraday Price Pressure and Order Flow Around U.S. Treasury Auctions*, Staff Report 1188, July revision. [Record](https://www.newyorkfed.org/research/staff_reports/sr1188.html); [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1188.pdf). Inspected sample, participation construction and conclusions. Application: competing nondealer capacity can attenuate supply pressure. The sample ends July 2024; publication date is not data recency.

## Invention, contracts and transport

### F01 — Abernethy, Chen and Wortman Vaughan (2013)

*Efficient Market Making via Convex Optimization, and a Connection to Online Learning*. [Inspected January 2012 draft](https://www.jennwv.com/courses/W12/markets-long-draft.pdf); [publication](https://doi.org/10.1145/2465769.2465777). Inspected payoff geometry and cost-function design. Application: start with contract payoffs. Automated-market-maker guarantees do not transfer unchanged to independently executing exchange orders.

### F02 — Kroer et al. (2016)

*Arbitrage-Free Combinatorial Market Making via Integer Programming*. [Inspected v2](https://arxiv.org/pdf/1606.02825); [record](https://arxiv.org/abs/1606.02825). Inspected Proposition 2.4, oracle and stopping conditions. Application: demand a valid solver bound or witness. An approximate iterate over incomplete states does not prove the required global payoff condition.

### F03 — Shi and Zhai (October 2026 preprint)

*Combinatorial Arbitrage in Prediction Markets*. [Record](https://arxiv.org/abs/2610.23517); [inspected October 20 v3](https://arxiv.org/html/2610.23517v3). Inspected theory, relation audit and execution replay. Application: separate proposed semantics, checked relations and feasible acquisition. Their strong sure-profit notion differs from standard arbitrage; displayed-depth historical replay is not a live return guarantee.

### F04 — Lou, Yan and Zhang (2013)

*Anticipated and Repeated Shocks in Liquid Markets*. [Inspected May 2013 manuscript](https://personal.lse.ac.uk/loud/Shocks.pdf). Inspected matched-duration construction and dealer-capacity explanation. Application: a public schedule can still create paid inventory service. Revalidate current compensation and compare with substitute-provider evidence in WR07.

### F05 — Greenwood and Sammon (2025)

*The Disappearing Index Effect*. [Publication](https://doi.org/10.1111/jofi.13410); [inspected March 2024 manuscript](https://dash.harvard.edu/server/api/core/bitstreams/647cc3b7-4803-4748-b181-e5ec8b343de7/content). Inspected migrations and demand/liquidity explanations. Application: net obligated flows and competing absorption matter; growing gross indexed assets need not enlarge the rent.

### F06 — Pearl and Bareinboim (2014)

*External Validity: From Do-Calculus to Transportability Across Populations*. [Inspected reprint](https://arxiv.org/pdf/1503.01603); [record](https://arxiv.org/abs/1503.01603). Inspected selection diagrams and transfer assumptions. Application: state what mechanisms change across venues, assets and scale. An LLM-drawn graph is an assumption, not identification of market causality.
