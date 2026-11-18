# Agent instructions: Trading Edge Lab

This repository is the **method canon** for finding, measuring and auditing trading edge: a
repo skill (`skills/engineer-trading-edge/`), a single paste-in prompt
(`Trading_Edge_Unified_Master_Prompt.txt`), and the frozen archive of how both were built
(v1/ to v4/). The **evidence** the method produced (the study library, the edge-find method
ledger with its 25 autopsies, the potential-edge register) lives in the companion repository
[Test](https://github.com/dwj9ddyvf6-hub/Test), chiefly under `research/gestalt/`. This repo
carries method and skills only, never research data or registers.

## Reading order

1. [README.md](README.md): what the lab is, the quick start, and the field record.
2. [skills/engineer-trading-edge/SKILL.md](skills/engineer-trading-edge/SKILL.md): the
   current skill. Fill the Edge Ledger first, then CREATE, IMPROVE or AUDIT, and end with a
   decision and the next experiment.
3. The reference the task needs: start from
   [edge-find-methods.md](skills/engineer-trading-edge/references/edge-find-methods.md) (how
   the recorded finds were actually made) and
   [edge-discovery-protocol.md](skills/engineer-trading-edge/references/edge-discovery-protocol.md)
   (the executable hunt protocol); the full reference map is in SKILL.md section 9.
4. [PROVENANCE.md](PROVENANCE.md) before citing any version's history, and
   [v4/validation.md](v4/validation.md) before citing the behavior test.
5. For the evidence behind any method claim, cross to Test (above). A method statement here
   is a claim; the study record there is its proof or its limit.

## Terminology

- **Edge Ledger:** the per-strategy accounting of where edge comes from (speed, accuracy,
  access; the variance warehoused, who sheds it, the premium, the bad state), plus payer,
  execution net, decisive test and kill rule. No payer and no measured part means a pattern,
  not an edge.
- **Trial count / family count:** the number of variants honestly charged against a result
  before deflation. A Sharpe or DSR quoted without its count is unfinished.
- **DSR / SPA / PBO:** deflated Sharpe ratio, Hansen's SPA test against a named benchmark,
  and the probability of backtest overfitting from combinatorially symmetric cross-validation.
- **Consensus Lens verdicts:** CONSENSUS-ONLY, DIFFERENCE-PLAUSIBLE,
  DIFFERENCE-PROVEN-FORWARD, UNGRADABLE-YET (see
  [consensus-lens.md](skills/engineer-trading-edge/references/consensus-lens.md)).
- **Verdicts:** GREEN is proven on the final artifact; PARTIAL is a bounded portion proven
  with the rest named; BLOCKED names the missing authority, access or input; UNVERIFIED is
  changed but unproven (see
  [truth-gates.md](skills/engineer-trading-edge/references/truth-gates.md)).

## What is proven, prospective and dead (November 2026 field record)

- **Proven on the stated samples, prospective in forward test:** the overnight Focus-names
  edge (DSR 0.99994 at the Wave 3 family count; the Wave 4 reprint at the pre-registered
  family count of 10 is DSR 0.99910; SPA 0.001 against SPY and 0.002 against QQQ, PBO 0.067,
  t 4.97, gross Sharpe 1.67 over 2,229 sessions, 2018 to 2026; the intraday leg is worthless
  at Sharpe 0.01). It is tradeable only through the opening and closing auctions, and its
  60-session forward falsifier runs from 16 November 2026: demotion if the mean net of 5
  basis points is not positive.
- **Promoted under the fleet exam, accruing forward:** RND-7 (DSR 0.989 at the clustered
  count of 487, PBO 0.022, SPA 0.000 against both SPY and QQQ, t 4.61, +20.48 basis points a
  night). Under raw-count accounting the same object prints DSR 0.007; the tension is on the
  record and the forward falsifier, not a chosen number, is the arbiter.
- **Dead or rejected, kept on the record:** the options expression of the overnight edge
  (rejected on real chains); ON_fit_lo14 as stamped (look-ahead in the stamp; its
  point-in-time rebuild stands FAIL as written, family PBO 0.222 against a 0.2 bar, and
  leave-one-out at median 0.2444 does not clear it); the insider-cluster build (rejected,
  DSR 0.579 against a 0.95 bar); FX-01 (rejected on paper, carried as a forward watch only).
  Kills and rejections are part of the method's evidence, not embarrassments to hide.

## Standing cautions

- Never quote a result without its trial count and its falsifier in the same breath.
- External evidence designs a test; it is never the verdict. A kill comes only from the
  object's own resolved sample hitting its registered falsifier.
- The behavior test for this skill showed no difference between arms (both near the
  ceiling); do not cite it as proof the skill improves a model.
- No strategy named here is shown to be profitable. The field record is one desk's research
  and paper trading, graded against SPY and QQQ.

## Repository discipline

- Leave v1/, v2/ and v3/ as historical snapshots; the current skill lives only at
  skills/engineer-trading-edge/.
- Rebuild the root prompt with `python scripts/build_unified_prompt.py` and compare it byte
  for byte before committing; regenerate `manifest.json` with
  `python scripts/build_manifest.py` in the commit that follows any file change.
- Report the state of the work as GREEN, PARTIAL, BLOCKED or UNVERIFIED.
