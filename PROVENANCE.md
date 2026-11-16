# Archive provenance

This repository collects the Trading Edge Lab work completed on 23–24 October 2026: the original economic-edge research, the adaptive-control extension, and the unified prompt that combines their instructions.

The prior GitHub archive was `dwj9ddyvf6-hub/Silicon`, branch `trading-edge-lab-v2`, path `research/trading-edge-lab/`, at commit `0fd0c817146876b0a0abcfdced76f073ac39ca59`. Its deliverables, skill snapshots, adaptive working research, evaluations and test code were copied here. The repository README and manifest were rewritten for the new root layout.

Additional original v1 working research and application evaluations are included under `v1/research/` and `v1/evaluations/`, with the original validation summary at `v1/validation.md`. Authoring scripts were adapted to relative repository paths under `scripts/`. Generated page previews, transient transfer helpers and Python caches are excluded.

## Which version to use

- **Unified prompt 2.1:** the single self-contained instruction to paste into an LLM. It merges the original prompt with the adaptive addendum, resolves duplicated instructions and includes the corrected arbitrage definition and explicit fallback/revalidation behavior.
- **Skill v2:** the current modular reference package. It includes original foundations and the adaptive-control references, plus the offline arbiter.
- **Skill and prompt v1:** historical snapshots. Their original wording is retained; use the unified prompt or v2 skill for current instructions.
- **Working research and evaluation transcripts:** evidence of the research and review process. They can contain proposed tests or observations about drafts. The final prompt, skill and validation documents take precedence over those intermediate notes.

The v1 skill snapshot derives from saved commit `92c33bbf39c1a6c48aa6442ba18c7006f14f84f9`. The v2 skill was authored at `42953aa` and read back at saved commit `559cb4b4323e01f6d2dd321a1d89a255c56787e9`, with 11 Markdown/Python files verified equal during that save.

`manifest.json` records repository-relative paths, byte sizes, SHA-256 hashes and Git blob SHA-1 hashes for every packaged file except the manifest itself. Publication verification separately checks the manifest's Git blob hash and the destination branch head.

Sources are linked and annotated in the source registers. The repository contains authored synthesis and code, not a redistribution of the complete third-party paper collection.


## Version 3 — 24 October 2026

The third pass adds explicit information-value and risk-reservation procedures, constructive economic transformations, contract-state checks, 26 additional research projects, a finite-model mechanics companion and a recorded exploratory behavior comparison. The root unified prompt is version 3.0; the prior complete prompt is preserved at `v2/Trading_Edge_Unified_Master_Prompt_v2.1.txt`.

The installed skill was saved by push at commit `d322ce6c963171f07924a55a9ff29634ccc8fb88`. The core used in the behavior comparison is identical to the saved core. A numerical precision repair changed the mechanics code and its tests after the evaluation snapshot; `v3/validation.md` records the boundary. The exact pre-repair test context is intentionally retained under `v3/evaluations/skill_under_test/`; use `v3/skill/` for the current implementation.

All earlier study and historical skill files are retained. Root documentation, the current unified prompt, build guide and prompt builder are updated. The source memos give exact versions and access limits. Transient transfer helpers and render caches remain excluded.


## Version 4 — 26 October 2026

The field edition. The current skill now lives at the stable path `skills/engineer-trading-edge/`; the root prompt is
version 4.0; v1, v2 and v3 are unchanged, and v3 gains `v3/Trading_Edge_Unified_Master_Prompt_v3.0.txt`, which
preserves the previous root prompt. The root prompt and the skill path are current; earlier entries describe the archive
as it stood then.

- **Skill:** built from v3 at `ddeab7cc0973a383a7a9ef9718a7e17fde30a94e`. v3's references and calculators were copied
  byte for byte; SKILL.md was rewritten around the Edge Ledger, the CREATE / IMPROVE / AUDIT workflow and twenty field
  rules, keeping v3's rules and equations. New references, templates, `research_stats.py` and `ledger_lint.py` were
  added with tests.
- **Field evidence:** the casebook and field rules come from the desk's research program of 15–26 October 2026 and its
  Edge audit of 558 paper-traded books, read from the desk's own records. Only aggregate statistics appear; no raw
  vendor data, machine paths, accounts or personal identifiers.
- **Literature:** 55 references checked against Crossref or RePEc on 26 October 2026.
- **Prompt:** `scripts/build_unified_prompt.py` rebuilds v3.0 byte for byte and adds the Edge Ledger, the workflow and
  the field rules from SKILL.md to make v4.0.
- **Behavior test:** frozen at commit `c9308f6` before any run; its runs belong under `v4/evaluations/`.
- **Manifest:** regenerated by `scripts/build_manifest.py` with the same fields and rules (every tracked file except the
  manifest itself). `installed_skill_commit` names the last commit that changed the skill.


## Publication privacy update — 7 November 2026

Personal document attribution was removed from the v1 PDF and its renderer. The PDF text and research content are unchanged. `manifest.json` records the current packaged files.


## Field methods addition, 15 November 2026

The current skill gains one reference, `skills/engineer-trading-edge/references/edge-find-methods.md`: the edge-find methods canon distilled from the desk research program's alpha hunt of 14 and 15 November 2026. Its source is the program's edge-find method ledger (25 autopsy entries with geology rows, the methods ranking, the vein map and the negative ledger), held in the desk's research notes at `research_notes/alpha-hunt-chaos-20261115/EDGE-FIND-METHOD-LEDGER.md`. The objects the methods produced are registered in the same program's potential-edge register (198 objects: 2 exam-passed, 18 live candidates, 66 leads, 59 watch, 22 avoidance, 31 resolved-against). Only aggregate statistics appear; no raw vendor data, machine paths, accounts or personal identifiers.

Placement follows this archive's own discipline. The material lives in the current skill at its stable path; v1, v2 and v3 are unchanged. SKILL.md gains one row in its section 9 files table and no other change, so sections 1 to 3 are untouched and the root prompt rebuilds byte for byte as before, verified with `scripts/build_unified_prompt.py`, a byte comparison against the root prompt and the skill's 88 unit tests. `manifest.json` is regenerated in the commit that follows this one, with `previous_edge_commit` naming the head this addition builds on and `installed_skill_commit` naming the commit that changed the skill.


## Discovery protocol addition, 15 November 2026

The current skill gains a companion reference, `skills/engineer-trading-edge/references/edge-discovery-protocol.md`: the executable protocol for hunting new market edge, distilled from the desk research program's edge-discovery work of 13 to 15 November 2026. Its sources are the program's edge-discovery playbook (the master loop, 54 numbered practices and the per-round honesty notes), its discovery log of find records, the practice-enrichment table (69 find clusters against 99 dead ends over 20 practices, two LLM panels, Fisher tests with Benjamini-Hochberg q), the potential-edge board standard that defines the Edge Potential Score, and the round records of rounds 7 to 17 and the full-combination search. These are held in the desk's research archives (`discovery/EDGE_DISCOVERY_PLAYBOOK.md` and `discovery/discovery_log.jsonl` in the research notes; `research/discovery/practice_enrichment.json` and `research/brainstorm/potential_edge_board_2026-11-15.md`, with the round records under `research/brainstorm/r7_2026-11-15` to `r17_2026-11-15`). Only aggregate statistics appear; no raw vendor data, accounts, machine paths or personal identifiers. Internal tool names are replaced by descriptions a reader can reproduce: the paid mechanism judgement is described as a blind LLM mechanism-strength rubric, and the rubric is given in full.

It complements the edge-find methods reference added earlier the same day, which covers mining records an estate already holds; the two files cross-link, and edge-find-methods.md gains one paragraph pointing to its companion and no other change. SKILL.md gains one row in its section 9 files table and one paragraph at the start of CREATE in section 2. Because section 2 feeds the root prompt, the root prompt was regenerated with `scripts/build_unified_prompt.py` (the link is stripped, so the paragraph is self-contained) and the build output was copied to the root, which now matches it byte for byte; the v3.0 rebuild still matches its preserved prompt. README's reference list gains one link. The skill's unit tests pass unchanged. `manifest.json` is regenerated in the commit that follows this one, with `previous_edge_commit` naming the head this addition builds on and `installed_skill_commit` naming the commit that changed the skill.


## Discovery protocol amendment, 15 November 2026 (evening)

`edge-discovery-protocol.md` gains a labelled amendment (a notice under its introduction and a new section 11) after the desk's pre-registered mechanism-weighted lens over 24.4 million condition-combination cells failed (AUC 0.490 against 0.529 for the in-sample t alone, below its shuffle null), traced to long-story bias in narrative ratings and no per-cell information within a side. The source is the research program's lens study and its playbook practices on it (`research/gestalt/accel/lens` in the program's research store). The amendment reconciles the result with the practice ranking: the mechanism question stays the strongest hypothesis generator and becomes a family-level tie-breaker ranked within side and instrument, never a per-cell weight. Only the lines that would contradict it were edited (checklist item 2, the ranking guidance, step 2's validation and use, the EPS note on m, one failure-mode row, the practice catalogue's practice 3 and three added lens practices); everything else is unchanged. SKILL.md's CREATE paragraph was reworded to match, so the root prompt was regenerated with `scripts/build_unified_prompt.py` and matches the build byte for byte; the skill's unit tests pass. `manifest.json` is regenerated in the commit that follows.

## Revision — 16 November 2026: live firing audit and the real-size amendment

- Added `skills/engineer-trading-edge/references/live-firing-audit.md`: practices 55-92 of the source desk's
  edge-discovery playbook (promotion passes and two desk audits, 15-16 November 2026) as a run-in-order audit, Gates
  A-E with pass lines and measured costs, and an audit row template. A same-day curation pass cut restatements of
  `desk-runtime.md`, `execution-edge.md`, C11, C13, C19 and protocol practices 45 and 54 in favour of cross-references.
- `edge-discovery-protocol.md`: section 8 covers practices 1-92 (59, 64-66 and 68 as lines; the rest point to the
  audit); checklist item 10 and step 10.3 point to the audit; new section 12 records the operator's amendment replacing
  minimum-lot shadows with real size at a floor under book-level risk caps, as an eight-step procedure.
- `SKILL.md`: one CREATE clause, one section 7 bullet and one Files row; the root prompt was rebuilt with
  `scripts/build_unified_prompt.py` and the manifest regenerated.

## Field lessons completion, 16 November 2026

The current skill gains four references, completing the placement of the desk research program's November 2026
edge-finding lessons in skill form. `skills/engineer-trading-edge/references/consensus-lens.md` packages the
consensus-circumvention examination (the eight tests, the twelve-field Lens Card and the four verdicts) from the
program's consensus lens examination plan and master trial register of 14 and 15 November 2026.
`potential-edge-census.md` packages the potential-edge measure and the E/M/D/A/S rubric from the program's
potential-edge census of 15 November 2026 and its register of 198 objects. `typed-lens-panels.md` packages the
governed creative use of a typed model layer (seven-lens panels, connection hunting, adversarial nulls,
extraction and counterfactual reads, with the graduation rule for seats) from the census's panel record and the
program's lens study. `falsifier-integrity.md` packages the falsifier audit procedure and its seven defect
classes from the fifth wave of the program's alpha hunt of 14 and 15 November 2026. Only the methods and their
aggregate evidence appear; the underlying registers, lane records and research artifacts remain in the desk's
research notes and are not part of this repository, which holds skills for finding and creating edge and nothing
else. Placement follows this archive's own discipline: the material lives in the current skill at its stable
path; v1, v2 and v3 are unchanged. SKILL.md gains four rows in its section 9 files table and no other change, so
sections 1 to 3 are untouched and the root prompt rebuilds byte for byte as before. README's list gains one
bullet. `manifest.json` is regenerated in the commit that follows, with `previous_edge_commit` naming the head
this addition builds on and `installed_skill_commit` naming the last commit that changed the skill.
