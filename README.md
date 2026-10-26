# Trading Edge Lab

A repo skill and a single prompt that make an LLM create, improve and audit trading strategies by measuring where
their edge comes from.

## The idea

> "Edge is comprised of: a) information arbitrage (faster and more accurate Bayesian updating and/or accessing
> mispriced bets the marginal participant doesn't have access to) and b) risk warehousing (taking on variance other
> people don't want to experience)" — Johann Markov

Trading Edge Lab turns each part into a measurement: **speed**, **accuracy** and **access** for information; for
risk, the variance held, who sheds it, the premium, the bad state and whether the book can hold it. Every strategy
also names its **payer**, its **execution net**, a **decisive test** and a **kill rule**. A strategy with no payer and
no measured part is a pattern, not an edge.

## Quick start

- **Prompt:** open [Trading_Edge_Unified_Master_Prompt.txt](Trading_Edge_Unified_Master_Prompt.txt), paste
  everything between `BEGIN PROMPT` and `END PROMPT` into the LLM, and append the strategy, data and constraints.
- **Skill:** copy [skills/engineer-trading-edge/](skills/engineer-trading-edge/) into a skills directory (for Claude
  Code, `~/.claude/skills/`) with its folders intact. Agents working inside this repository follow it through
  [AGENTS.md](AGENTS.md), which [CLAUDE.md](CLAUDE.md) imports.

Example request:

> Fill the Edge Ledger for the strategy below, then improve it from its largest measured loss of value. End with a
> decision, the decisive test and the kill rule.

## What v4 adds

- **The Edge Ledger first:** each of Markov's parts is a line to measure, checked by `scripts/ledger_lint.py`.
- **A creating workflow:** CREATE starts from the payer, IMPROVE from the measured loss of value, AUDIT from the
  search behind the claim; each ends in a decision and the next experiment.
- **Twenty field rules** from our desk's research program (6,330 US stocks, 944 delisted segments, four size tiers,
  2016–2026) and its audit of 558 paper-traded books, each backed by a decision record in the
  [field casebook](skills/engineer-trading-edge/references/field-casebook.md).
- **References** for the [research protocol](skills/engineer-trading-edge/references/research-protocol.md),
  [execution edge](skills/engineer-trading-edge/references/execution-edge.md),
  [truth gates](skills/engineer-trading-edge/references/truth-gates.md), strategy
  [archetypes](skills/engineer-trading-edge/references/edge-ledger.md) and a
  [literature map](skills/engineer-trading-edge/references/literature-map.md) of 55 checked references.
- **`research_stats.py`:** Benjamini–Hochberg, Newey–West, probabilistic and deflated Sharpe ratio, minimum track
  record length, block bootstrap, minimum detectable effect and a random-walk null, standard library only.
- **A behavior test built to avoid the ceiling:** 12 fresh cases with controls for over-applied lessons, frozen
  before any run.
- **A stable skill path:** `skills/engineer-trading-edge/` always holds the current version.

## Evidence

- 88 unit tests pass; the root prompt rebuilds byte for byte ([validation record](v4/validation.md)).
- Behavior test: not run yet (0 of 2 answers per arm). v3's comparison scored 24/24 in both arms and showed no effect
  of the skill.
- No strategy in this repository is shown to be profitable. The field rules record one desk's research and paper
  trading.

## Files

| Path | Contents |
|---|---|
| [Trading_Edge_Unified_Master_Prompt.txt](Trading_Edge_Unified_Master_Prompt.txt) | The prompt, version 4.0 |
| [skills/engineer-trading-edge/](skills/engineer-trading-edge/) | The current skill: SKILL.md, references, scripts, templates, agent metadata |
| [v4/](v4/) | Validation record, behavior test ([cases, rubric, runner](v4/evaluations/RUNNER.md)), statistics cross-check |
| [AGENTS.md](AGENTS.md), [CLAUDE.md](CLAUDE.md) | Instructions for agents working in this repository |
| [scripts/](scripts/README.md) | Prompt builder, manifest tool, PDF renderers |
| [v3/](v3/), [v2/](v2/), [v1/](v1/) | Earlier versions, unchanged: studies, prompts, skills, evaluations |
| [PROVENANCE.md](PROVENANCE.md), [manifest.json](manifest.json) | History; file sizes and hashes |

## Run the checks

Python 3.10 or later, from the repository root:

```bash
python -m unittest discover -s skills/engineer-trading-edge/scripts -p 'test_*.py' -v
python scripts/build_unified_prompt.py && cmp build/Trading_Edge_Unified_Master_Prompt.txt Trading_Edge_Unified_Master_Prompt.txt
python scripts/build_manifest.py --check
python v4/evaluations/runner.py verify
```

Prepared October 2026. The original archive was developed in
[Silicon](https://github.com/dwj9ddyvf6-hub/Silicon/tree/trading-edge-lab-v2/research/trading-edge-lab);
[PROVENANCE.md](PROVENANCE.md) gives the history.
