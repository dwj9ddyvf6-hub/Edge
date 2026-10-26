# Build sources

The saved PDFs and the root prompt are ready to use. These scripts keep their authoring logic with repository-relative
paths; outputs go to `build/`, which git ignores.

Run from the repository root:

```bash
python scripts/build_unified_prompt.py
python scripts/build_manifest.py --check
python scripts/render_research_study.py
python scripts/render_adaptive_addendum.py
```

- `build_unified_prompt.py` rebuilds the v3.0 prompt, checks it byte for byte against
  `v3/Trading_Edge_Unified_Master_Prompt_v3.0.txt`, and writes the v4.0 prompt: v3.0 plus the Edge Ledger, the workflow
  and the field rules from `skills/engineer-trading-edge/SKILL.md`, without file links. Compare
  `build/Trading_Edge_Unified_Master_Prompt.txt` with the root prompt before committing.
- `build_unified_prompt_v2.py` rebuilds the v2.1 prompt.
- `build_manifest.py` regenerates `manifest.json` from the tracked files; `--check` verifies it instead.
- The PDF renderers also need `matplotlib` and `reportlab` and use the DejaVu fonts bundled with Matplotlib. PDF output
  may differ in metadata or layout across library versions. The archived PDFs were visually reviewed when authored;
  the relocated renderer sources were syntax-checked, not re-rendered.
- The skill's calculators and their tests live in `skills/engineer-trading-edge/scripts/` and need only the standard
  library.
