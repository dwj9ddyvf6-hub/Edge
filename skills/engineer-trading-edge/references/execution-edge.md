# Execution edge: what survives the trip to the market

An edge is what remains after execution. Measure it at intended size, from the decision to the fill, against the real
touch. Numbers below are from the desk's record (558 paper books on live quotes with simulated fills, four full
sessions) unless marked as a prior desk's study.

## Contents

1. The net-edge identity
2. Measured costs
3. How to measure
4. Fixes that worked
5. Rules

## 1. The net-edge identity

net edge = gross edge − half-spread at the real touch − impact at intended size − fees − adverse drift after the fill
− cost of delay − financing

- Each term is measured, not assumed. A term without a measurement is a hypothesis.
- For passive orders the fill itself selects outcomes: estimate P(fill | state) and the payoff given a fill, and score
  no-fills at their cash value ([C16](field-casebook.md#c16-per-fill-or-per-opportunity)).

## 2. Measured costs

| Cost | Measurement | Source |
|---|---|---|
| Simulator against the real touch | Charged 2.45 bps against the real mid; crossing the real touch costs 5.75 bps (2,004 audited fills) | [C17](field-casebook.md#c17-the-cost-stack) |
| Option half-spreads | $88,218 on 52 fills, 175.9 bps of notional; genuine 0.80-delta LEAPS 0.96% of premium (n 6) against 0.70% assumed | C17 |
| Adverse drift | Mid moved 11.0 bps against the position 30 minutes after equity fills (n 9,838); 6.3 bps side-balanced | C17 |
| Late opening fills | Median fill 5.8–7.5 minutes after 09:30 (2,893 orders); +16.6 bps over the official open after removing QQQ's move (n 1,083) | [C18](field-casebook.md#c18-speed-late-opens-stale-prices-and-the-route-stage) |
| Decision lag | One-hour sleeves decided a median 29 minutes after their bar; +2.0 bps when decided within 30 minutes, +17.0 bps at 30–60 | C18 |
| Stale decision prices | 961 of 11,338 equity fills decided on a price more than 1% off the live quote | C18 |
| Costs above gross | 26 sleeves whose costs exceeded the size of their pre-cost result; 8 turned a pre-cost profit into a net loss | C17 |
| One bar late (prior desk) | A one-hour fill one bar late cost $502.54 a trade (walk-forward t 7.59) | desk research record, 2026-10-18, execution-knowledge review |
| Capacity (prior desk) | A crypto replay returning +51.13% at full cash returned −1.01% when capped at 1% of prior volume | same review |
| Cost assumptions decide verdicts (prior desk) | At a 150 bp round-trip hurdle every small-cap study failed; realistic friction for liquid stocks was 10–20 bps | same review |

## 3. How to measure

- **Touch, not mid:** re-price a sample of fills on the real consolidated quote; compare with what the simulator
  charged. The desk's simulator was better than the real touch in 63.4% of audited cases.
- **Markouts:** the mid 5 and 30 minutes after each fill, signed by side, per session and side-balanced. A one-sided
  book's markout mixes adverse selection with the market's direction; four sessions cannot separate them.
- **Decision-to-fill:** stamp decision, order, acknowledgement and fill times honestly. Virtual and internally crossed
  fills stamped with the decision clock hid the desk's opening delay.
- **Against the reference the strategy assumed:** fills at the open against the official opening print; one-hour fills
  against the next bar's open the research used.
- **Per opportunity:** count skipped and unfilled opportunities at their cash value.
- **Capacity curve:** net value against size, with impact and participation limits; a result at full cash is not a
  result at size.
- **Cost stress:** rerun with costs doubled and tripled; an edge that dies at twice the cost is a cost estimate, not an
  edge.

## 4. Fixes that worked

| Problem | Fix | Proof |
|---|---|---|
| The open's route stage re-measured spreads one paced request at a time (181–241 s, 41–55% of the pass) | Compute the spread book in the idle hour before the open | Replay of one open: 240.5 s → 10.7 s; first order +245.2 s → +17.6 s; 1,648 fills identical |
| A T-bill rate read as 40.7% bought a 0.28-delta call in place of a 0.80-delta one at a 13.5%-wide quote | Refuse decisions on impossible inputs: a rate outside [0, 0.15], or a chosen contract's delta more than 0.25 from the model's | Replaying that day's inputs places no order and raises an alert |
| A data-host error retried 792 times in one outage | Skip the bar and keep the cadence | Merged with tests |
| Fills stamped with the decision clock | Stamp virtual and crossed fills with the route stage's clock | Merged with tests |
| A parent order could be sent after its child's deadline | No parent after the deadline | Merged with tests |
| Late opening entries | A paired shadow arm filled at the official opening print, with a registered rejection rule | Built; its forward sample decides |

## 5. Rules

- Judge entries from the fill, not the signal close: close-to-close studies include an overnight move a desk acting at
  the next open cannot capture.
- Compute everything knowable before the clock starts; the decision window is for what changes inside it.
- A simulator's cost model is a hypothesis to audit against real quotes.
- Bound every input by physical plausibility before it reaches an order.
- Count execution against the capture window: an edge whose half-life is shorter than decision-to-fill is not
  available to this desk.
- Long-dated options as leverage: a prior desk's research put deep in-the-money LEAPS spreads at about 6.3 points a
  year against about 2.5 points of convexity value (desk research record, 2026-10-18, execution-knowledge review).
