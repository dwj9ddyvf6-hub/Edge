# Build sources

The saved PDFs and unified prompt are ready to use. These scripts preserve their authoring logic with paths adapted to this repository. Outputs go under `build/`, leaving the archived deliverables unchanged.

Run from the repository root:

```bash
python scripts/build_unified_prompt.py
python scripts/render_research_study.py
python scripts/render_adaptive_addendum.py
```

The prompt builder uses the Python standard library. The PDF renderers also require `matplotlib` and `reportlab`; they use the DejaVu fonts bundled with Matplotlib. PDF output may differ in metadata or layout across library versions. The archived PDFs were visually reviewed when authored; the relocated renderer sources have been syntax-checked, not rerendered for this copy.

The v3 combined prompt rebuilt from these sources was compared byte-for-byte with `Trading_Edge_Unified_Master_Prompt.txt` before publication.

The offline decision arbiter and its tests live separately under [`v3/skill/scripts/`](../v3/skill/scripts/). They do not depend on the PDF packages.

The previous prompt assembly is preserved in `build_unified_prompt_v2.py`; it rebuilds `build/Trading_Edge_Unified_Master_Prompt_v2.1.txt`. The current builder combines that preserved prompt with the v3 protocol. The original PDF renderers still build the archived v1/v2 studies; v3 research is provided as Markdown with its sources and evaluation artifacts.
