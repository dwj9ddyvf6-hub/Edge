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
