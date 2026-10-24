# Build sources

The saved PDFs and unified prompt are ready to use. These scripts preserve their authoring logic with paths adapted to this repository. Outputs go under `build/`, leaving the archived deliverables unchanged.

Run from the repository root:

```bash
python scripts/build_unified_prompt.py
python scripts/render_research_study.py
python scripts/render_adaptive_addendum.py
```

The prompt builder uses the Python standard library. The PDF renderers also require `matplotlib` and `reportlab`; they use the DejaVu fonts bundled with Matplotlib. PDF output may differ in metadata or layout across library versions. The archived PDFs were visually reviewed when authored; the relocated renderer sources have been syntax-checked, not rerendered for this copy.

The combined prompt rebuilt from these sources was compared byte-for-byte with `Trading_Edge_Unified_Master_Prompt.txt` before publication.

The offline decision arbiter and its tests live separately under [`v2/skill/scripts/`](../v2/skill/scripts/). They do not depend on the PDF packages.
