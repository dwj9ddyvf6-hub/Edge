# Risk warehousing frontier: price the service against the actual balance sheet

Research pass: 24 October 2026, America/New_York. This memo adds seven primary-source projects not present in the v1 or v2 source registers. The literature was searched and the sections specified below inspected; this is not a complete reading of every proof. Search timestamps, upload paths and publication years are not interchangeable.

## Main finding

The screenshot's risk-warehousing idea needs a reservation-price procedure. Willingness to tolerate variance is insufficient. The desk must establish a price at which a defined exposure improves its existing portfolio, can be financed along the whole path, and remains competitive with alternatives. Two claims with identical expected losses and variance can deserve sharply different prices because their losses arrive in different states of the desk's existing wealth.

The highest-value additions are: compute endowment-dependent value; expose the cash and collateral path; distinguish equity capital from funding availability; and test whether another class of intermediaries has already supplied the scarce service. These improve the economic model without requiring another directional indicator.

## New source register

### WR01 — Owen and Žitković (2009), Optimal Investment with an Unbounded Random Endowment and Utility-Based Pricing

- Published: *Mathematical Finance* 19(1), 129–159, DOI 10.1111/j.1467-9965.2008.00360.x. Inspected preprint: arXiv v2, 11 September 2007, 29 pages.
- Primary PDF: https://arxiv.org/pdf/0706.0478
- Author bibliography: https://web.ma.utexas.edu/users/gordanz/publications/index.html
- Inspected: introductory framework; Assumptions 1.4/1.6; permissible strategies; Definition 7.1 and Proposition 7.2.
- Supports: indifference value depends on endowment, admissible trading and utility; technical existence results require market and integrability assumptions.
- Prompt consequence: compare optimized utility with and without the claim under the same feasible trading opportunities. Do not label a subjective reservation value the market's true price. The finite example below is a separate elementary derivation.

### WR02 — Avellaneda and Stoikov (2008), High-Frequency Trading in a Limit Order Book

- *Quantitative Finance* 8(3), 217–224; DOI 10.1080/14697680701381228.
- Author-hosted PDF: https://math.nyu.edu/inmemoriam/avellaneda/HighFrequencyTrading.pdf
- Inspected: inventory focus; reservation bid/ask definitions, equations 6–8; Poisson arrival model; quoting objective.
- Supports: inventory-dependent valuation and quote-arrival tradeoffs within their Brownian-price/CARA model. Its no-additional-trading reservation midpoint is `r = s - q*gamma*sigma^2*(T-t)`.
- Prompt consequence: distinguish a reservation valuation from an executable quote. Calibrate fills separately; the formula does not model arbitrary adverse selection, queue priority, jumps or collateral. Here `sigma` is absolute price volatility, not an unconverted percentage volatility.

### WR03 — Gârleanu and Pedersen (2011), Margin-Based Asset Pricing and Deviations from the Law of One Price

- *Review of Financial Studies*; DOI 10.1093/rfs/hhr027; published PDF, 43 pages.
- Primary PDF: https://pages.stern.nyu.edu/~lpederse/papers/MarginPricingLoOP.pdf
- Inspected: introduction; Proposition 1; empirical qualification around pp. 24–25.
- Supports: margins and scarce capital affect required returns and prices of otherwise closely related claims in the model.
- Contrarian qualification: its simple identification of a capital shadow cost with a quoted borrowing spread does not fit the observed basis magnitude if LIBOR is treated as the true available funding rate. Borrowing access and leverage constraints matter.
- Prompt consequence: estimate the desk's effective financing/constraint cost; do not import a public spread as a universal shadow price.

### WR04 — He and Krishnamurthy (2013), Intermediary Asset Pricing

- *American Economic Review* 103(2), 732–770; DOI 10.1257/aer.103.2.732. Author PDF includes appendices.
- Primary PDF: https://zhiguohe.net/wp-content/uploads/2023/12/he-krishnamurthy-2013-intermediary-asset-pricing.pdf
- Inspected: abstract; equity-capital constraint, equation 5; leverage/exposure and risk-premium mechanism around equations 17–19.
- Supports: intermediary equity scarcity can change risk premia nonlinearly.
- Limit: the modeled constraint is on outside equity capital; it is not interchangeable with a debt-funding limit. No real-time trade signal is established.
- Prompt consequence: name the binding resource. A cheap credit line need not repair depleted risk-bearing equity.

### WR05 — Duffie, Fleming, Keane, Nelson, Shachar and Van Tassel (2023), Dealer Capacity and U.S. Treasury Market Functionality

- Federal Reserve Bank of New York Staff Report 1070; August 2023, revised October 2023; DOI 10.59576/sr.1070. Inspected NY Fed PDF: 70 pages. The BIS version is the same project, not another source.
- Primary PDF: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1070.pdf
- Inspected: introduction, July 2017–December 2022 sample, capacity-proxy construction and measurement limits.
- Supports: high utilization helps explain liquidity deterioration beyond volatility in the studied sample.
- Prompt consequence: the research proxy normalizes by a full-sample maximum and uses dealer-level data unavailable to ordinary public users. A live strategy needs an as-of denominator and genuinely accessible inputs; historical explanatory strength is not prospective implementability.

### WR06 — Kashyap, Stein, Wallen and Younger (2025), Treasury Market Dysfunction and the Role of the Central Bank

- *Brookings Papers on Economic Activity*, Spring, 221–296.
- Author publication record: https://stein.scholars.harvard.edu/publication/treasury-market-dysfunction-and-role-central-bank
- Published PDF: https://stein.scholars.harvard.edu/sites/g/files/omnuum5951/files/2025-12/BPEA-SP25_WEB_Kashyap_Stein_Wallen_Younger.pdf
- Inspected: model motivation; separate-leg margin discussion pp. 14–16 of PDF; distinction between capital and funding pp. 35–38.
- Supports: a directionally hedged basis position can face collateral demands on separate legs; capital stress can force unwinds even with repo access.
- Prompt consequence: represent clearing accounts, cash availability and timing. Terminal offsetting payoffs are not a proof that the interim obligations can be met. The policy proposal is not an assumed trading backstop.

### WR07 — Fleming, Liu and Nguyen (2026), Intraday Price Pressure and Order Flow Around U.S. Treasury Auctions

- NY Fed Staff Report 1188; March 2026, revised July 2026; DOI 10.59576/sr.1188; working paper, not presented as a settled causal theorem.
- Primary PDF: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1188.pdf
- Record: https://www.newyorkfed.org/research/staff_reports/sr1188.html
- Inspected: abstract, data/sample, prior-auction participation construction, conclusion, Tables 2–3 and 6. Sample ends July 2024 despite the 2026 paper date.
- Supports: auction-related pressure varies with constraints and demand; greater non-dealer participation can absorb supply and mitigate pressure. The recent-period pressure did not mechanically grow with debt issuance.
- Prompt consequence: test substitution by alternative providers. Explanatory same-window flow is not automatically available at the entry decision; prior-auction shares are a separate, potentially observable predictor.

## Executable reasoning procedure for the skill

For each proposed warehouse, complete the following record before ranking trades:

1. **Service and payer:** identify the inventory, insurance, liquidity, financing or horizon service. Describe the counterparty's plausible objective or binding constraint without requiring their irrationality or knowing their identity.
2. **Exposure:** enumerate payoff states, exercise/assignment, defaults, basis and settlement definitions. Specify quantity and horizon.
3. **Endowment:** include existing portfolio payoffs and liabilities in the same states. The desk's weakest state matters more than the new sleeve's isolated variance.
4. **Hedge menu:** distinguish a fixed hedge from reoptimization of the whole approved portfolio. Apply the same feasible set on both sides of the comparison.
5. **Reservation curve:** calculate or bound the minimum acceptable premium by size and state, net of distinct fees and implementation effects. Where preferences or probabilities are unmeasured, present scenarios rather than invented precision.
6. **Funding path:** verify cash, collateral and transfer availability by account, currency and deadline. Recognize equity capital, borrowing access, collateral eligibility and operating capacity as separate resources.
7. **Market comparison:** compare the offered executable compensation with the reservation curve. A spread can pay fairly for risk without producing benchmark-relative alpha. A negative standalone expected return can still improve an existing portfolio.
8. **Competitive substitution:** ask who else can provide the service now, whether their capacity has changed, and what observable event would erase the proposed rent.
9. **Prospective test:** freeze data availability, population, baseline, economic hurdle and monitoring. Separate modeled utility from achieved returns and physical probabilities from pricing weights.

Use the existing v2 action/risk controller after this record is formed. Do not duplicate costs already in its wealth scenarios.

## Elementary finite-state derivation: identical loss distributions, different minimum premiums

This is a hypothetical algebra check, not a market estimate. There are two equally likely states, one terminal date, zero interest, no additional trading, no fees or path constraints, and CARA utility `U(w) = -exp(-gamma*w)`, where `gamma > 0` has units of inverse currency. A desk begins with terminal wealth `W`; it receives premium `c` and assumes liability `L`.

Its indifference premium solves:

`E[U(W+c-L)] = E[U(W)]`.

Direct substitution and rearrangement give:

`c*(W,L) = log(E[exp(-gamma*(W-L))] / E[exp(-gamma*W)]) / gamma`.

Define the desk's marginal-utility weights:

`Q_i = p_i*exp(-gamma*W_i) / sum_j p_j*exp(-gamma*W_j)`.

Then `c* = log(sum_i Q_i*exp(gamma*L_i))/gamma`. These Q weights describe preferences and endowment in this model; they are not revised physical outcome probabilities. If the exponential moments are infinite, the formula does not produce a finite acceptable premium. A finite scenario grid alone does not prove the real tail is bounded.

Take `W=(100,20)`, `gamma=.05`. The resulting weights are approximately `(0.0179862,0.9820138)`.

| Liability | Loss in state 1 | Loss in state 2 | Expected loss | Loss variance | Minimum premium |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | 20 | 0 | 10 | 100 | 0.608748 |
| B | 0 | 20 | 10 | 100 | 19.771308 |

At premium 12, both have standalone expected profit 2. A improves expected utility; B reduces it. A pays its loss in the desk's rich state and reduces the endowment gap, while B deepens the poor state. The difference is economically invisible to standalone mean, variance and win rate.

Now give the insurance buyer wealth `(20,100)` and let coverage pay `(20,0)`. Under the same utility and probabilities, its maximum purchase price is:

`b* = -log(E[exp(-gamma*(W_b+L))] / E[exp(-gamma*W_b)]) / gamma = 19.391252`.

The seller's ask is 0.608748 and the buyer's bid is 19.391252. Premium 12 can benefit both in expected utility even though their transfer cashflows cancel. This supplies a concrete answer to “who pays and why?” without requiring superior prediction or a foolish counterparty. Real costs and constraints narrow or eliminate this interval.

With hedging, use `V(W)=sup_{theta in A} E[U(W+G(theta))]` and solve `V(W+c-L)=V(W)` under the same approved admissible set and economic costs. Do not reuse the no-trading closed form after adding an optimized hedge. Different risk preferences or constraints require their own value function; CARA is an illustration, not a mandatory desk objective.

All displayed arithmetic was recomputed in Python using the supplied probabilities and states. This checks the equations, not the plausibility of those inputs.

## A terminal hedge can still be infeasible

Hypothetical path: at an interim deadline one leg owes 40 units of variation margin, while the offsetting leg has a 40-unit gain that is not transferable until later. Only 30 units of cash are available at the paying account. Net marked value is zero, but the account has a 10-unit funding shortfall. Netting the two marks would approve an infeasible strategy.

Require cash-flow timing and enforceable netting/transfer rights before aggregation. Stress increased initial margin separately from variation margin. A risk-weighted capital or expected-utility surplus does not satisfy a legal cash obligation by itself.

## Two implementable research hypotheses

### H-W1: predictable inventory service conditional on substitute providers

**Hypothesis, not claimed discovery:** auction inventory service may be attractive only when observable pre-auction conditions suggest demand exceeds available intermediation capacity. Construct a candidate using public auction timing and lagged participation, timestamped quotes, cost estimates and a fixed risk budget. Compare calendar-only, volatility-only and participation-conditioned versions on the same opportunities. Do not put contemporaneous explanatory order flow into a predictor before it exists. Choose action/exit windows only inside development data.

The payer is an investor or intermediary valuing temporary inventory transfer. The advantage is available capital and execution at a sufficiently compensated price, not knowledge of the bond's ultimate direction. Test whether substitute buyers attenuate the spread enough to remove after-cost value. Use neighboring tenors or matched non-auction days as prespecified controls. Reject the claimed incremental conditioning benefit if it does not survive held-out costs, comparable duration exposure and the declared uncertainty threshold.

### H-W2: collateral-aware exposure implementation

**Hypothesis, not claimed discovery:** a desk may improve an existing exposure by changing its lawful implementation across genuinely available contracts or clearing arrangements, with no stronger directional forecast. Compare the incumbent route with feasible alternatives using total executable costs, basis/settlement differences, collateral demand and transfer timing. Preserve the exposure objective and compare residual risks explicitly; an ETF, future and cash position are not exact substitutes by assertion.

The potential benefit is reduced implementation cost or less forced liquidation, not a new additive alpha term. Test fixed-portfolio and reoptimized-portfolio comparisons separately. Use actual instrument/venue constraints and ex-ante margin schedules; stress unmodeled changes. Reject an apparent saving that disappears after financing, slippage, basis risk or missed execution. Never infer clearing/netting privileges from a correlation coefficient.

## Compact instruction to inject into the skill

For risk warehousing, construct a portfolio-specific reservation price or value interval by quantity. State the payer's service demand, our existing state exposures, feasible hedges, premium, costs and each cash/collateral deadline. Compare the executable offer with the value of adding the exposure to the actual portfolio, not isolated variance. Keep physical forecasts separate from marginal-utility or state-price weights. Test whether substitute liquidity providers have erased the rent. If inputs cannot identify the value, return bounds and the decisive data acquisition or experiment, while still producing concrete candidate designs.

## Suggested adversarial evaluation cases

- Present the A/B liabilities above with identical mean/variance and ask which to warehouse. Success depends on using the incumbent wealth state, not merely cautioning about tails.
- Offer an apparently hedged positive-carry trade with offsetting marks but asynchronous collateral deadlines. A valid answer computes the cash shortfall and proposes a feasible route or rejects the implementation.
- Claim a larger macro supply necessarily increases an inventory-service return. A valid answer constructs a substitute-provider hypothesis and a measured test.
- Supply a dealer-capacity feature normalized to the final sample maximum. A valid answer identifies the availability problem and designs an as-of denominator without claiming it reproduces the original measure exactly.
