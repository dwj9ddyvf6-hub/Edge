# Edge Ledger: <strategy or sleeve name>

Fill every row in the Entry column before anything else. Write numbers with units and n. Leave a row blank only when the
strategy makes no such claim. Check it with `python scripts/ledger_lint.py <this file>`.

| Field | Question | Entry |
|---|---|---|
| Speed | What do we learn before the price does? | |
| Lead time | How far ahead of the price's own update, against the capture window (seconds, sessions)? | |
| Accuracy | What do we update better than the price? | |
| Baseline | Incremental decision value over a price-aware baseline, net, out of sample? | |
| Access | Which mispriced bet can the marginal participant not or not want to take (capacity, mandate, attention, venue, size tier, data)? | |
| Why it stays open | Why has competition not closed it? | |
| Variance | Which variance do we hold? | |
| Shedder | Who sheds it, and why? | |
| Premium | What does it pay, against this book's reservation value? | |
| Bad state | When does it bite, how often, how deep? | |
| Holdable | Can this book hold it through the bad state (margin path, funding, exit liquidity)? | |
| Co-losses | What else in the book loses at the same time? | |
| Payer | Who pays us, per trade, and why do they accept it? | |
| Execution net | What remains after spreads, impact, adverse drift and latency, at intended size? | |
| Evidence | What has been measured so far, how, with n? | |
| Searched | Was this found by searching variants (yes or no)? | |
| Trials | How many variants were tried, in total? | |
| Decisive test | The cheapest test that changes the decision (design, n, minimum detectable effect)? | |
| Kill rule | The result that retires it, fixed before the data arrive? | |
| Evidence stage | HYPOTHESIS, RETROSPECTIVE, OUT-OF-SAMPLE, FORWARD SIMULATION or LIMITED LIVE? | |
