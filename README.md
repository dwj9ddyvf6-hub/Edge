# Trading Edge Lab

**A research framework and reusable LLM prompt for creating, improving and auditing trading strategies, sleeves and trading desks.**

Start with the **[Unified Master Prompt](Trading_Edge_Unified_Master_Prompt.txt)**. It combines the original economic-edge framework and the adaptive-control addendum into one self-contained instruction. No separate addendum or installed skill is required to use it.

## What it is for

Trading Edge Lab helps turn an idea into a precise economic hypothesis, an executable decision policy and a credible test. Use it to:

- Create a strategy by identifying who pays, what advantage is supplied and why competition has not removed the opportunity.
- Improve an existing strategy by finding the largest loss of value in forecasting, selection, timing, execution, sizing or portfolio interaction.
- Audit a backtest, betting rule, prediction-market trade, arbitrage claim or trading desk for unsupported assumptions and implementation gaps.
- Design an adaptive controller that updates beliefs, allocates computation, manages shared constraints and responds to changing evidence without silently rewriting its policy.

The starting insight is that returns can arise from **information advantages** and **paid risk bearing**. The research expands this into a practical framework for information, lawful access, participant constraints, liquidity and other services, executable prices, adverse selection, capital, validation and portfolio utility. It distinguishes a forecast advantage from a risk premium, a portfolio improvement and a statistical finding.

The central question is: **What scarce information, access, service or risk-bearing capacity do we supply; who values it; and what remains after competition, costs, adverse states and delay?**

## Quick start

1. Open [Trading_Edge_Unified_Master_Prompt.txt](Trading_Edge_Unified_Master_Prompt.txt).
2. Copy everything between `BEGIN PROMPT` and `END PROMPT` into your LLM.
3. Append your strategy or desk specification, available data, instruments, horizon, objective and constraints.

For example:

> Apply this entire framework to the strategy below. Preserve its existing baseline and timing authority. Diagnose the economic source of edge and the binding loss of value. Execute accessible research, propose the smallest useful improvement, and specify the experiment that would establish or reject it. Separate measured results from hypotheses.

The expected result is an evidence-status verdict, an edge contract, precise policy rules, quantitative economics, prioritized improvements, decisive experiments and an operational handoff where requested.

For a skill-capable agent, the current skill snapshot is [v2/skill/SKILL.md](v2/skill/SKILL.md), named `engineer-trading-edge` and displayed as **Trading Edge Lab**. Keep its relative references, scripts, metadata and assets together when installing it. The `v1/skill/` directory preserves the earlier version.

## What the adaptive layer adds

The master algorithm maintains separate information, belief, account, policy, learning and resource states. It compares feasible actions against the incumbent portfolio after costs, spends computation where it can change a valuable decision before the deadline, and separates routine execution from belief updates and promotion of changed policies.

Its action menu includes entering, holding, waiting, reducing, hedging and gathering information. It handles delayed outcomes, unsupported counterfactuals, pending orders, ambiguous submissions, shared capital and stale state. Historical evidence and current opportunity remain separate questions. Trading every day is not an objective by itself.

## File guide

| File or directory | Purpose |
| --- | --- |
| [Trading_Edge_Unified_Master_Prompt.txt](Trading_Edge_Unified_Master_Prompt.txt) | Recommended entry point: the original prompt and adaptive addendum merged into one prompt. |
| [v1/Trading_Edge_Research_Study.pdf](v1/Trading_Edge_Research_Study.pdf) | Original 30-page research synthesis, economic foundations, mechanisms and validation framework. |
| [v2/Trading_Edge_Adaptive_Addendum.pdf](v2/Trading_Edge_Adaptive_Addendum.pdf) | 26-page second-pass audit and extension covering adaptive control, learning and desk operations. |
| [v1/Trading_Edge_Master_Prompt.txt](v1/Trading_Edge_Master_Prompt.txt), [v2/Trading_Edge_Adaptive_Master_Prompt.txt](v2/Trading_Edge_Adaptive_Master_Prompt.txt) | Original separate prompts retained for provenance. Use the unified file for a single instruction. |
| [v2/skill/](v2/skill/) | Current skill package, detailed references and offline reference implementation. |
| [v1/skill/](v1/skill/) | Historical skill snapshot. |
| [v2/audit-findings.md](v2/audit-findings.md), [v2/validation.md](v2/validation.md) | Audit findings, completed checks, limitations and promotion guidance. |
| [v1/research/](v1/research/), [v1/evaluations/](v1/evaluations/), [v1/validation.md](v1/validation.md) | Original research memos, report introduction, application outputs and validation record. |
| [v2/research/](v2/research/), [v2/evaluations/](v2/evaluations/) | Research working memos, independent review and qualitative application outputs. |
| [scripts/README.md](scripts/README.md) | Instructions for rebuilding the reports and assembling the unified prompt from repository sources; generated files go into `build/`. |
| [PROVENANCE.md](PROVENANCE.md) | Version history, source snapshots and archive conventions. |
| [manifest.json](manifest.json) | File inventory with content hashes for checking the saved archive. |

The original source register contains **50 distinct entries**; the adaptive extension adds **30 distinct primary-source entries**. Consult the [original source register](v2/skill/references/sources.md) and [adaptive source register](v2/skill/references/adaptive-sources.md) for links, versions, relevance and access limitations. These are annotated research sources, not a claim that every paper was read exhaustively. Working memos may contain proposed tests or pre-fix observations; final validation records and current skill instructions take precedence for implementation status.

## Reference implementation and tests

The [offline adaptive arbiter](v2/skill/scripts/adaptive_arbiter.py) is a dependency-free Python reference kernel. It selects among supplied actions using paired robust value, evidence and freshness gates, deadlines, scenario constraints and possible pending fills. It returns a decision or recovery requirement.

Run its 20 synthetic test methods from the repository root with Python 3.10 or later:

```bash
cd v2/skill
python -m unittest discover -s scripts -p test_adaptive_arbiter.py -v
```

The kernel does not contain market feeds, a broker adapter, live order submission, a learned forecasting model or production reservation infrastructure. The research specifies how those components should be integrated and tested. Synthetic tests establish specified behavior; the qualitative LLM application cases check reasoning on fictional problems.

## Evidence and scope

This is a research, prompt and reference-code repository. It does not establish a profitable trading strategy, a production-ready trading desk, measured live latency improvements or orders-of-magnitude returns. No new market-data backtest, forward trading record or live execution was produced by the adaptive addendum. Any strategy built with it needs its own point-in-time data, realistic execution, costs, portfolio constraints and prospective validation.

Existing timing authority and deployment boundaries remain explicit inputs to the workflow.

Prepared October 2026. The original archive was developed in [Silicon](https://github.com/dwj9ddyvf6-hub/Silicon/tree/trading-edge-lab-v2/research/trading-edge-lab); this repository gives Trading Edge Lab a dedicated home.
