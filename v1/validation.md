## What was checked

The skill metadata and structure passed the skill-creator validator. All source identifiers used by the references resolve to the source register. The register contains 51 labels for 50 distinct entries; V9 is an explicit alias of B08. Worked numerical examples were independently recalculated. The PDF equations were rendered as mathematical images and the page layouts visually inspected.

Two fresh agents received the skill and supplied hypothetical tasks, without being given the intended answers or prior diagnoses. They produced user-facing solutions to four application cases. The review below checks those outputs against the supplied arithmetic, payoff definitions, and research requirements. This is a small qualitative behavior check; it does not measure superiority over a baseline prompt, prove generalization to every LLM, or validate any market strategy.

| Case | Observed behavior | Review result |
| --- | --- | --- |
| Accurate forecast at bad odds, plus passive-fill selection | Derived -0.06 per contract for p=.60 at price 0.65 plus cost 0.01; derived -.035 per passive fill and -.014 per attempt under fill-only costs; distinguished overall accuracy from conditional probability | Arithmetic and diagnosis matched supplied assumptions |
| Apparent cross-venue weather arbitrage | Enumerated mismatched station outcomes; found the state where both contracts lose and pair P&L is -.90; designed a semantic payoff checker | Rejected the false risk-free claim and gave a constructive implementation path |
| Sharpe 3.1 and 98% win rate selected from 2,000 backtests | Kept the result at unverified research status; identified contaminated dates, unknown search history, midpoint-fill optimism and downside tails; specified an execution audit and shadow workflow | Did not manufacture a corrected significance estimate or live-readiness claim |
| New customer-to-supplier earnings strategy | Specified a long-only, delayed public-information hypothesis with as-of relationships, explicit features, decision clocks, entry/exit rules, baselines, costs and falsifiers | Produced a reproducible research candidate; labeled numerical settings assumptions and returns unmeasured |

## What to invoke

Use the saved skill named engineer-trading-edge, displayed as Trading Edge Lab. A practical starting request is:

"Use $engineer-trading-edge to audit this strategy. Identify its economic source of edge and the main loss of value, then execute accessible research and produce the smallest useful improvement with an explicit experiment and rejection rule."

For a different LLM, paste Trading_Edge_Master_Prompt.txt and append the strategy, available data, instruments, horizon, objective, and constraints. The master prompt is self-contained; this study supplies deeper references and research blueprints. Its purpose is to create and test better hypotheses, not to substitute prose for evidence.

