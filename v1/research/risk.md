# Risk warehousing and structural edge: primary-source research memo

Research completed 23 October 2026 (America/New_York). This memo supplies sources and reasoning for a reusable edge-design skill. It does not estimate an investable strategy's edge. Primary papers, their authors' pages, publisher abstracts and institution-hosted manuscripts were opened. The 2022 Gabaix–Koijen manuscript and 2018 Trading Costs manuscript are identified as working-paper versions. Findings below are paraphrases; synthesis and hypotheses are labeled.

## Essential correction to the post

The post's second category is economically productive: someone can pay you to supply immediacy, insurance, patient capital or capacity that they lack. The payment need not come from their ignorance. Their trade can improve their utility while your trade earns positive expected cash profit. But “taking on variance others do not want” is imprecise. Raw volatility is not automatically compensated. The relevant burden can be covariance with bad states, discontinuous losses, illiquidity, funding calls, time without access to capital, benchmark constraints, or an unhedgeable liability. The skill must name the exact burden and explain why this particular trader can bear it more cheaply or reliably.

## Verified source register

### R1 — John H. Cochrane, *Asset Pricing*, revised edition (2005), chapter 1

Author page: https://www.johnhcochrane.com/asset-pricing

Author-hosted sample chapters: https://www.johnhcochrane.com/s/samplechapters-dy5d.pdf

Verified passage: printed pp. 15–18, especially equation (1.12); browser `turn41view4` / `turn52view4`.

The basic relationship is p = E[mX], where m is the stochastic discount factor. For gross returns, E[R] − Rf = −Cov(m,R)/E[m]. A payoff valuable in states of high marginal utility can earn a low or negative expected excess return. Large independent variance does not by itself imply a risk premium. **Skill consequence:** describe the state in which capital is most valuable and whether the proposed strategy loses then; distinguish a premium for bearing that loss from forecasting skill. **Limit:** this identity becomes an empirical explanation only after specifying or estimating the relevant pricing kernel and market assumptions.

### R2 — Andrei Shleifer and Robert W. Vishny, “The Limits of Arbitrage” (1997), *Journal of Finance* 52(1), 35–55

Published-paper PDF: https://web.stanford.edu/~piazzesi/Reading/ShleiferVishny1997.pdf

Author record: https://shleifer.scholars.harvard.edu/publications/limits-arbitrage

Verified body: opening pp. 35–37; browser `turn41view0`.

Convergence trades can need additional collateral before they converge. External investors may withdraw money after losses precisely when dislocations widen. Specialized arbitrage capital therefore need not eliminate extreme mispricing. **Skill consequence:** specify convergence uncertainty, interim mark-to-market losses, redemption terms, and funding. A correct terminal forecast is insufficient if forced liquidation occurs first. **Limit:** persistent spreads do not prove mispricing; contract differences or omitted risks may explain them.

### R3 — Markus K. Brunnermeier and Lasse Heje Pedersen, “Market Liquidity and Funding Liquidity” (2009), *Review of Financial Studies* 22, 2201–2238

Author record: https://markus.scholar.princeton.edu/publications/market-liquidity-and-funding-liquidity

Paper: https://markus.scholar.princeton.edu/document/98

Verified abstract and model/margin sections; browser `turn37view1`, `turn41view5`, `turn55view3`.

Market liquidity and funding capacity can reinforce one another. Losses reduce capital; higher haircuts increase required capital; sales can worsen liquidity and losses. The paper explains commonality across securities through shared funding scarcity. Its model compares profits against margin usage. **Skill consequence:** stress simultaneous price loss, spread widening, haircuts and correlated liquidation; size on stressed capital, not initial broker margin. **Limit:** spirals are conditional model outcomes, not a prediction that every volatility spike causes a funding crisis.

### R4 — Zhiguo He, Bryan Kelly and Asaf Manela, “Intermediary Asset Pricing: New Evidence from Many Asset Classes” (2017), *Journal of Financial Economics* 126, 1–35

Institution-hosted published PDF: https://mfm.uchicago.edu/wp-content/uploads/2020/07/He-et-al_Intermediary-asset-pricing-New-evidence-from-many-asset-classes.pdf

Author's data page: https://zhiguohe.net/data-and-empirical-patterns/intermediary-capital-ratio-and-risk-factor/

Verified paper pp. 1–3; browser `turn41view1`.

Innovations in primary-dealer equity capital ratios explain cross-sectional expected returns across several asset classes in the study. The findings support intermediary marginal wealth as a relevant pricing factor. **Skill consequence:** evaluate whether supposedly different strategies all depend on healthy dealer balance sheets. **Limit:** explanatory cross-sectional evidence does not establish a reliable real-time timing signal. Accounting data release lags, changing dealer composition and estimation uncertainty matter.

### R5 — Nicolae Gârleanu, Lasse Heje Pedersen and Allen M. Poteshman, “Demand-Based Option Pricing” (2009), *Review of Financial Studies* 22(10), 4259–4299

Author repository (January 2006 manuscript): https://archive.nyu.edu/handle/2451/26791

Manuscript PDF: https://archive.nyu.edu/bitstream/2451/26791/2/S-DRP-06-01.pdf

Publication record: https://www.aqr.com/Insights/Research/Journal-Article/DemandBased-Option-Pricing

Verified manuscript theorem 2 and hedging-risk sections; browser `turn41view6` / `turn52view5`.

Under the model, demand raises an option's price in proportion to unhedgeable variance and affects other contracts through covariance of residual hedging risk. Discrete hedging, jumps and stochastic volatility prevent complete replication. **Skill consequence:** option premium can pay for residual risk even with accurate pricing; distinguish that compensation from an unusually favorable price relative to the same risks. **Limit:** observable volume or open interest alone does not identify net customer demand or dealer inventory; a model's residual-risk covariance is not directly observed.

### R6 — Joshua Coval and Erik Stafford, “Asset Fire Sales (and Purchases) in Equity Markets” (2007), *Journal of Financial Economics* 86, 479–512

Published PDF: https://www.hbs.edu/ris/Publication%20Files/Asset%20Fire%20Sales%20in%20Equity%20Markets_24af6e8c-8417-48a3-a384-053b90473e78.pdf

Verified abstract and discussion; browser `turn52view1` / `turn55view0`.

The published paper examines mutual-fund flow-driven transactions over 1980–2004. Large flows lead funds to change existing holdings, producing price pressure in overlapping positions and opportunities for liquidity suppliers. **Skill consequence:** search for a measurable obligation to trade, rather than calling every price decline a forced sale. Build the signal from information actually released before entry. **Limit:** the final published sample differs from older working-paper abstracts (1980–2003). Slow disclosure and endogenous flows limit simple live replication.

### R7 — Andrea Frazzini and Lasse Heje Pedersen, “Betting Against Beta” (2014), *Journal of Financial Economics* 111, 1–25

Author-hosted published PDF: https://pages.stern.nyu.edu/~afrazzin/pdf/Betting%20Against%20Beta%20-%20Frazzini%20and%20Pedersen.pdf

DOI: https://doi.org/10.1016/j.jfineco.2013.10.005

Verified introduction and propositions summary; browser `turn41view3`.

Leverage-constrained investors can bid up high-beta assets. The paper's low-beta long/high-beta short construction earns positive average risk-adjusted returns in its samples but performs poorly as funding constraints tighten. **Skill consequence:** identify who cannot hold the economically equivalent alternative; a mandate or balance-sheet restriction can sustain pricing differences without irrationality. **Limit:** “market neutral” does not mean funding neutral or tail neutral; financing, short access and beta estimation matter.

### R8 — Tim Bollerslev, George Tauchen and Hao Zhou, “Expected Stock Returns and Variance Risk Premia” (2009), *Review of Financial Studies* 22(11), 4463–4492

Publisher primary abstract: https://academic.oup.com/rfs/article-abstract/22/11/4463/1565787

DOI: https://doi.org/10.1093/rfs/hhp008

Verified author list, year, abstract; browser `turn37view7`. Full paper not read in this pass.

The paper connects an implied-versus-realized variation measure to subsequent aggregate returns, strongest at intermediate quarterly horizons in its setting. Its reported result depends on model-free implied volatility and accurate high-frequency realized variation. **Skill consequence:** distinguish a risk-neutral option-implied expectation from a physical forecast; never treat the full difference as forecast error. **Limit:** the abstract is not evidence for daily short-option profitability or 0DTE implementation, and a realized-variance proxy contains forecast error as well as the intended premium.

### R9 — Darrell Duffie, “Presidential Address: Asset Price Dynamics with Slow-Moving Capital” (2010), *Journal of Finance* 65(4), 1237–1267

Author-hosted published PDF: https://www.darrellduffie.com/uploads/1/4/8/0/148007615/duffieafapresidentialaddress2010.pdf

Verified abstract and initial framework; browser `turn52view0`.

Supply or demand shocks can cause sharp reactions followed by extended reversals when capital cannot reach opportunities instantly. Search frictions and capital-raising delays help shape this trajectory. **Skill consequence:** express an opportunity in both price and time; identify the mechanism and expected speed of capital arrival. **Limit:** slow-capital reversals are not a blanket justification to fade news, and convergence timing is uncertain.

### R10 — Andrea Frazzini, Ronen Israel and Tobias J. Moskowitz, “Trading Costs” (August 2018 working paper)

Institution-hosted manuscript: https://spinup-000d1a-wp-offload-media.s3.amazonaws.com/faculty/wp-content/uploads/sites/3/2021/08/Trading-Cost.pdf

Author submission: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3229719

Verified abstract and execution/measurement sections pp. 11–18; browser `turn52view2`, `turn55view1`.

The study uses institutional executions across 21 developed markets, estimating costs and impact. Implementation shortfall includes trading costs and missed-trade opportunity costs. Its dataset's trades were almost always completed; its cost estimates exclude stock-lending fees. **Skill consequence:** estimate costs at intended size and urgency; quote-based friction estimates must account for nonfills, selection and borrow. **Limit:** one institutional execution process cannot be copied as a universal cost schedule, especially for retail options, tiny stocks or fast-decaying signals.

### R11 — Xavier Gabaix and Ralph S. J. Koijen, “In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis” (May 12, 2022 manuscript)

Institution-hosted manuscript: https://cowles.yale.edu/sites/default/files/2022-10/SSRN-id3686935.pdf

NBER record: https://www.nber.org/papers/w28967

Verified abstract and identification/robustness passages; browser `turn52view3`, `turn55view2`.

The framework studies market-level price responses when institutional demand is relatively inelastic. Portfolio mandates can inhibit offsetting responses to flows. **Skill consequence:** estimate the elasticity of the marginal counterparties and distinguish permanent allocation changes from temporary liquidity shocks. **Limit:** aggregate flow multipliers are estimation-dependent and cannot be applied as universal intraday or individual-stock impact constants. The paper discusses identification difficulties and measurement assumptions.

## Mathematical and operational synthesis (our derivations)

1. **Positive expected return is not automatically abnormal profit.** In a model with pricing kernel m, a risky return can have E[R] > Rf because Cov(m,R) < 0. Therefore report three different quantities: expected net cash P&L, excess return versus a specified risk benchmark, and incremental portfolio utility. A factor-adjusted alpha is model-dependent, not proof that all risk has been removed.

2. **Variance premium requires two measures, not two adjectives.** An ex-ante variance premium can be defined as E_Q[RV] − E_P[RV] for the same horizon and variance convention. E_Q[RV] − subsequent RV is an ex-post realization; it contains an innovation. Option implied volatility minus trailing historical volatility mixes square roots, horizons and forecast error. Define units and timing before estimation. Selling options requires full pathwise P&L including jumps, hedging, fees and liquidation.

3. **A private comparative advantage can be on the balance sheet.** Two traders who agree on a payoff distribution can rationally make opposite trades if their existing exposures, obligations, funding or preferences differ. The research task is to identify the counterparties' objective and demonstrate that the proposed trader has the required complementarity. Merely accepting discomfort is not evidence of a favorable price.

4. **Survival is a path constraint.** Let W_t be liquid equity after mark-to-market and M_t required collateral. A strategy must satisfy W_t − M_t − operational_reserve_t ≥ 0 along a stress path; positive terminal E[P&L] does not ensure this. Simulate joint loss, margin expansion, collateral haircut, basis widening, financing repricing and delayed exit. Avoid assuming instant cross-margining between brokers or legal entities.

5. **Capacity is part of the edge, not a post-processing detail.** Let expected dollar value at size q be V(q)=q·a−C(q)−F(q)−L(q), where a is per-unit expected gross value, C execution/impact cost, F funding/borrow and L other expected losses. Do not count the same loss twice. Under a concave objective, increasing size ceases to help when marginal expected gross value equals marginal total cost. Tail constraints can bind earlier. Estimate the entire feasible size curve and its uncertainty, not only an average trade return.

6. **Risk diversification is state-dependent.** Several attractive premiums may all sell liquidity in crisis states. Group by common failure mechanism—equity crash, volatility jump, funding withdrawal, borrow recall, settlement interruption—rather than ticker or strategy name. Expected shortfall attribution and joint scenario P&L are more informative than calm-period correlations alone. This is a design recommendation, not a claim those estimators remove uncertainty.

7. **Insuring the bad state can consume the entire premium.** A hedge is a priced asset, not a free safety switch. Evaluate strategy plus hedge jointly: residual tails, basis risk, premium drag, turnover and margin. Hedging all economically remunerated risk can remove the reason the trade paid in the first place.

## Five creative research hypotheses, explicitly unproven

### H1 — Match the desk's liabilities to the market's unwanted risk

**Mechanism:** a premium is more attractive to a desk whose other assets earn in that strategy's bad states. **Experiment:** match candidate sleeves on standalone estimated net return and expected shortfall; rank by incremental portfolio expected utility under resampled joint scenarios. **Falsifier:** incremental advantage disappears out of sample or under crisis dependence. **Needed data:** synchronized P&L, liability and collateral requirements. This changes portfolio selection, not the underlying expected payoff.

### H2 — Price opportunities by capital occupation, not headline spread

**Mechanism:** a modest, short-lived dislocation can outperform a larger spread that occupies scarce collateral for an uncertain duration. **Experiment:** compare equal-risk policies using posterior convergence-time distributions and stressed capital-time usage; include reinvestment uncertainty. **Falsifier:** timing estimates add no held-out utility after costs. **Needed data:** timestamped executable spreads, funding terms, resolution dates and failed convergence episodes. Do not annualize tiny historical spreads mechanically.

### H3 — Separate forced-flow reversals from information-driven declines

**Mechanism:** predicted mechanical trades can transiently move prices, but information shocks can justify persistent repricing. **Experiment:** predefine publicly observable constraint/flow variables and competing information variables; compare matched events and use a no-trade region when classification is ambiguous. **Falsifier:** the flow classification does not predict additional executable reversal after factor, event and liquidity controls. **Needed data:** point-in-time mandates/holdings/rebalances, news timestamps and quotes. A price drop itself is not a flow instrument.

### H4 — Hedge the cheapest common catastrophe, retain the compensated inventory

**Mechanism:** the desk may improve utility by buying protection against shared funding/tail exposure while retaining otherwise uncorrelated premiums. **Experiment:** compare fixed hedge, state-aware hedge and reduced-position alternatives using identical budgets; include actual option bid/ask and stress margin. **Falsifier:** benefits vanish after hedge costs or are matched by simply reducing exposure. **Needed data:** joint paths, hedge surfaces, funding and realistic fills. This is a search over portfolio design, not an assertion of cheap insurance.

### H5 — Build an opportunity map from participant constraints

**Mechanism:** the same market statistic can mean different things when the marginal trader changes—for example benchmark rebalancers versus informed traders. **Experiment:** preregister participant/constraint states and test whether they improve conditional net payoff forecasts beyond prices and volatility alone. **Falsifier:** incremental predictability fails nested time-series validation or disappears at executable prices. **Needed data:** decision-time indicators of mandates, auctions, financing and available inventory. Treat inferred identities as uncertain; do not claim access to unobserved dealer books.

## Mandatory questions for the downstream skill

- Who pays, and what rational objective or constraint makes paying sensible?
- Is the strategy earning information rent, a risk premium, a service fee, a constraint rent, or a mixture?
- What is the exact bad state, who is harmed then, and why can this desk bear it?
- What kills the trade before its expected value can be realized?
- Are apparent diversifiers the same crisis exposure in different contracts?
- Which return survives conservative executable costs, funding and realistic size?
- What is the cheapest simpler alternative: cash, lower size, broad beta, a passive premium or a direct hedge?
- What evidence distinguishes superior forecasting from merely taking a more unpleasant payoff distribution?
- What observable change in competition, funding or mandates removes the mechanism?
- What observation would make the correct recommendation “do not deploy”?

