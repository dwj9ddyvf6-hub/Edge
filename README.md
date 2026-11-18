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
  [truth gates](skills/engineer-trading-edge/references/truth-gates.md),
  [edge-find methods](skills/engineer-trading-edge/references/edge-find-methods.md), the
  [edge discovery protocol](skills/engineer-trading-edge/references/edge-discovery-protocol.md), the
  [live firing audit](skills/engineer-trading-edge/references/live-firing-audit.md), strategy
  [archetypes](skills/engineer-trading-edge/references/edge-ledger.md) and a
  [literature map](skills/engineer-trading-edge/references/literature-map.md) of 55 checked references.
- **Field lessons, November 2026:** the [consensus lens](skills/engineer-trading-edge/references/consensus-lens.md) for auditing any object against the consensus it has to beat, the [potential-edge census](skills/engineer-trading-edge/references/potential-edge-census.md) for grading a whole estate by potential edge, [typed lens panels](skills/engineer-trading-edge/references/typed-lens-panels.md) for using a model panel as a lens under governance, and [falsifier integrity](skills/engineer-trading-edge/references/falsifier-integrity.md) for auditing a grading machine before its window runs.
- **`research_stats.py`:** Benjamini–Hochberg, Newey–West, probabilistic and deflated Sharpe ratio, minimum track
  record length, block bootstrap, minimum detectable effect and a random-walk null, standard library only.
- **A behavior test built to avoid the ceiling:** 12 fresh cases with controls for over-applied lessons, frozen
  before any run.
- **A stable skill path:** `skills/engineer-trading-edge/` always holds the current version.

## Evidence

- 88 unit tests pass; the root prompt rebuilds byte for byte ([validation record](v4/validation.md)).
- Behavior test, 2026-10-26, with 2 answers per arm on 12 cases:
  - with the skill, 97 and 97 of 98; without it, 96 and 93;
  - no critical errors in either arm.
  - The gap is smaller than the spread between the two answers without the skill, so it shows no difference. Both
    arms scored near the ceiling ([run](v4/evaluations/run-2026-10-26/), [record](v4/validation.md)).
  - v3's comparison was also at the ceiling in both arms (24/24).
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

## Field record: what the method found (November 2026)

The skill's November references (edge-find methods, the discovery protocol, the consensus
lens, the potential-edge census, typed lens panels, falsifier integrity, the live firing
audit) were distilled from a two-day alpha hunt and the grading program that followed it.
The hunt's own record is 25 method autopsies: every find written up with the framework, the
methods in order, what was done differently, and the reusable rule. The full evidence (the
method ledger, the campaign registers, the census of 198 registered objects: 2 exam-passed,
18 live candidates, 66 leads, 59 watch, 22 avoidance, 31 resolved-against) is held in the
companion evidence repository, [Test](https://github.com/dwj9ddyvf6-hub/Test), under
`research/gestalt/`. This repository carries the method; that one carries the proof.

The headline outcomes, each with its limiting numbers:

- **The overnight Focus-names edge.** The close-to-open leg of a 29-name focus basket:
  DSR 0.99994 at the Wave 3 family count (the Wave 4 reprint at the pre-registered family
  count of 10 is DSR 0.99910), SPA 0.001 against SPY and 0.002 against QQQ, PBO 0.067,
  t 4.97, gross Sharpe 1.67 over 2,229 sessions from 2018 to 2026. The same basket's
  intraday leg is worthless (Sharpe 0.01), and the premium survives only through the
  opening and closing auctions: crossing spreads nets about minus 27 basis points a night,
  the auction form about plus 19.5. Five names carry it after true auction costs (SNDK,
  CRWV, RKLB, NVDA, AMD). Its forward falsifier runs 60 sessions from 16 November 2026:
  demotion if the mean net of 5 basis points is not positive.
- **RND-7, promoted under the fleet exam.** A range-rank gate on the same overnight form:
  DSR 0.989 at the clustered count of 487, PBO 0.022, SPA 0.000 against both SPY and QQQ,
  t 4.61, +20.48 basis points a night, gated Sharpe 1.549 against 1.163 ungated. Under the
  laboratory's raw-count accounting the same object prints DSR 0.007; both accountings are
  on the record, and the 60-session forward falsifier is the arbiter.
- **The failures, kept.** The options expression of the overnight edge was rejected on real
  chains. ON_fit_lo14 as stamped carried look-ahead; its honest point-in-time rebuild
  stands FAIL as written (family PBO 0.222 against a 0.2 bar; leave-one-out median 0.2444
  does not clear it). The insider-cluster build was rejected at DSR 0.579 against a 0.95
  bar. FX-01 was rejected on paper and is carried as a forward watch only. Of the first 17
  graded conversion exams: 1 promotion, 4 kills, 12 rejections. A method that hides its
  kill rate is marketing, not measurement.

Nothing here is shown to be profitable. The two surviving objects are prospective: their
forward falsifiers, not their backtests, will decide them.

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
