# The Edge Ledger: Markov's two sources, measured

Johann Markov: "Edge is comprised of: a) information arbitrage (faster and more accurate Bayesian updating and/or
accessing mispriced bets the marginal participant doesn't have access to) and b) risk warehousing (taking on
variance other people don't want to experience)."

The ledger turns each clause into a measurement. Fill it with [the template](../assets/edge-ledger.md) and check it
with `scripts/ledger_lint.py`. A strategy with no payer and no measured part is a pattern, not an edge.

## Contents

1. The four parts
2. The payer and the execution net
3. Archetypes
4. Reading a filled ledger

## 1. The four parts

| Part | Diagnostic questions | Measurement | Typical decay | Capacity | Failure signature |
|---|---|---|---|---|---|
| **Speed** (faster updating) | What do we learn before the price does? Is the lead longer than our decision-to-fill latency? | Lead time against the price's own update and the capture window; a capture curve: the same signals replayed at deliberate delays | Fast: rivals buy the same latency | Small: only the liquidity inside the window | Profit sits in the earliest fills; markouts worsen with delay; a one-bar delay erases it |
| **Accuracy** (more accurate updating) | What do we update better: a model, a data process, evidence the price under-weights? | Incremental decision value over a price-aware baseline, out of sample, net of costs; calibration on the traded cohort | Medium: publication and imitation | Medium | IC rises while money does not ([C06](field-casebook.md#c06-forecast-accuracy-is-not-economic-value)); no increment over the incumbent ([C04](field-casebook.md#c04-nested-information-adds-nothing)); one era only ([C12](field-casebook.md#c12-edges-are-era-bound)) |
| **Access** (bets the marginal participant cannot or will not take) | Which constraint keeps others out: capacity, mandate, attention, venue, size tier, data? Why does it stay open? | The constraint, how often it binds, the edge by size tier, net value against size | Slow while the constraint binds; ends when rules, venues or players change | Small by construction | The edge shrinks as size grows; it lives only in tiers too thin to trade at size ([C03](field-casebook.md#c03-chartslector-warnings-work-in-thin-markets-buy-rules-do-not)) |
| **Risk warehousing** (variance others shed) | Which variance? Who sheds it, and why? What premium, against this book's reservation value? When does it bite? Can the book hold it through the bad state? What else loses then? | Premium net of expected loss; stress loss and margin path at size; joint loss with the rest of the book | Persistent while the risk is real; compressed when capital floods in | Large, bounded by balance sheet and funding | Steady small gains, then losses clustered in one state; losses coincide with the rest of the book; forced exit in the bad state |

- Speed and accuracy can be the desk's own: execution latency is part of the speed edge
  ([C18](field-casebook.md#c18-speed-late-opens-stale-prices-and-the-route-stage)), and negative selection is part of
  accuracy ([C02](field-casebook.md#c02-small-cap-buy-triggers-are-traps-negative-selection-pays)).
- Information about the second moment is accuracy about risk. It belongs in sizing, stops and option pricing
  ([C01](field-casebook.md#c01-volatility-is-the-most-predictable-thing-on-a-chart)).
- Overlap is normal. A market maker is paid for immediacy (warehousing), loses to informed flow (the rival's speed)
  and survives by updating quotes faster (its own speed). Count each part once, by the measurement it needs.

## 2. The payer and the execution net

- **Payer:** the participant whose loss or fee is our gain, and why they accept it: a hedge, a mandate, a deadline,
  a preference for lottery payoffs, slower processing. Name a segment when identity is unknowable. No payer means no
  transfer to capture.
- **Execution net:** gross edge minus half-spread at the real touch, impact at intended size, fees, adverse drift
  after the fill, the cost of delay, and financing. Measure it as [execution-edge.md](execution-edge.md) describes.
- **Decisive cheap test:** the cheapest test whose result changes the decision, with its sample size and minimum
  detectable effect ([research-protocol.md](research-protocol.md)).
- **Kill rule:** the result that retires the strategy, fixed before the data arrive.

## 3. Archetypes

Starting hypotheses for the ledger, not verdicts. Published evidence for each is in
[literature-map.md](literature-map.md#archetypes).

| Strategy | Source of edge | Payer | Bad state | First test |
|---|---|---|---|---|
| Momentum | Accuracy: others update slowly to news arriving in small pieces; some crash risk held | Slow updaters; holders reluctant to sell losers | Sharp rebounds after market declines | Return beyond the market's own trend, by era; loss in rebound months |
| Mean reversion (valuation, pairs) | Risk warehousing of convergence risk, or accuracy on fair value | Holders forced or eager to exit the cheap leg | Divergence that keeps widening; funding pulled before convergence | Half-life and its stability; P&L in stress episodes; carrying cost to convergence |
| Breakouts | Usually none; claimed speed of news diffusion | Often the strategy itself, buying a lottery ticket | False breaks, gap reversals; in small caps the typical trigger lags ([C02](field-casebook.md#c02-small-cap-buy-triggers-are-traps-negative-selection-pays)) | Breakout against random entries measured the same way, volatility-matched, every tier |
| Post-earnings drift | Speed and accuracy in processing earnings news | Inattentive holders | Crowded drift that reverses; thin capacity in small names | Drift from the first tradable price after the report, net, by size tier and era |
| Insider buying | Access: insiders' information, disclosed with a lag; speed in reading filings | Sellers facing informed insiders | Routine (uninformative) trades; filing delays | Returns from the filing time, not the trade date; opportunistic against routine buyers; net of spread |
| Dilution (offerings, at-the-market sales) | Accuracy through negative selection | Issuers who must raise cash; buyers of the issue | Squeezes; borrow recalls for shorts | Returns after the filing by issuer type; for a long-only book, value as a veto |
| Index changes | Risk warehousing for forced flow; access through a known clock | Index trackers trading at the effective date | Pre-positioned rivals; reversal before the close; deletions with bad news | Announcement-to-effective event study by era, net of costs, with rivals' pre-positioning measured |
| Short volatility, variance premium | Risk warehousing | Hedgers buying protection | Crashes, volatility spikes, correlations jumping to one | Premium net of realized loss through crises at intended size; the margin path ([C08](field-casebook.md#c08-fear-priced-above-realized-volatility-paid-the-warehouse)) |
| Carry | Risk warehousing of crash and funding risk | Borrowers and hedgers paying for financing | Global risk-off; funding squeezes | Carry return in risk-off months; correlation with the book's other risks |
| Liquidity provision, short-term reversal | Risk warehousing of immediacy | Impatient traders | News-driven moves that do not revert; stress, when the pay is highest | Split moves by news and no news; returns by volatility regime; net of the bid-ask bounce |
| Merger arbitrage | Risk warehousing of deal-break risk; accuracy on completion | Target holders shedding deal risk | A market crash that breaks deals together | Spread against completion probability; returns in down markets |
| Small-cap illiquidity | Access (too small for large funds); illiquidity held | Forced sellers; those paying for immediacy | Liquidity droughts; delistings | Net of real spreads and impact at size, on a universe that keeps delisted names ([C13](field-casebook.md#c13-point-in-time-the-leak-and-the-volume-flaw)) |
| Overnight gaps | Risk warehousing of overnight risk, or clientele demand at the open | Traders who must act at the open | Gaps on news | Overnight and intraday returns split, net of auction costs, measured from a fill a desk can get |
| Crypto funding (perpetual basis) | Risk warehousing: lending leverage | Leveraged longs paying funding | Crashes, exchange failure, forced deleveraging | Funding minus hedge, fee and venue costs; the liquidation path; venue default |
| Prediction markets | Accuracy (better probabilities) or access (position limits deter large players) | Bettors with preferences; hedgers | Disputed resolution, fees, limits | Calibration against the executable price at size, with exact settlement semantics |
| Market making | Risk warehousing of inventory, defended by speed | Liquidity demanders paying the spread | Informed flow, jumps, toxic periods | Markouts by counterparty and time after the fill; spread captured minus adverse selection minus inventory cost |

## 4. Reading a filled ledger

| Pattern in the ledger | Reading | Next step |
|---|---|---|
| Payer blank | A pattern, not an edge | Name a payer or drop the idea |
| Speed filled, lead time blank | An untested speed claim | Replay at deliberate delays |
| Accuracy without a price-aware baseline | An untested accuracy claim | Fit the baseline with the same budget; measure the increment |
| Access without a reason it stays open | A claim competition has already closed | Find the binding constraint; test the edge by size tier |
| Warehousing without a bad state | Selling insurance without reading the policy | Write the stress path and margin call at intended size |
| Execution net blank | Gross edge only | Price the real touch, impact and delay at intended size |
| Found by search, no trial count | Selection bias unmeasured | Count the trials, deflate (DSR, BH), test forward |
| No kill rule | Cannot fail, so cannot be known | Write the rule before the next data |
