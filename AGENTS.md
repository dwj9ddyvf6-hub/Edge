# Agent instructions

Any strategy, sleeve, backtest or trading-desk work in or with this repository follows
[skills/engineer-trading-edge/SKILL.md](skills/engineer-trading-edge/SKILL.md): fill the Edge Ledger first, then CREATE,
IMPROVE or AUDIT, and end with a decision and the next experiment.

- Report the state of the work as GREEN, PARTIAL, BLOCKED or UNVERIFIED
  ([truth gates](skills/engineer-trading-edge/references/truth-gates.md)).
- Leave v1/, v2/ and v3/ as historical snapshots; the current skill lives only at skills/engineer-trading-edge/.
- Rebuild the root prompt with `python scripts/build_unified_prompt.py` and compare it byte for byte before committing.
