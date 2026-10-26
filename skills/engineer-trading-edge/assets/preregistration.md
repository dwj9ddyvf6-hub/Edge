# Pre-registration: <study name>

Registered <UTC time>, before any number of this study exists. Amend only by a dated addendum written before the number
it decides. Rules and tools: [research-protocol.md](../references/research-protocol.md), `scripts/research_stats.py`.

| Field | Entry |
|---|---|
| Question | The decision this study changes |
| Hypothesis | Direction and size, with the Edge Ledger part it tests (speed, accuracy, access, warehousing) |
| Data | Sources, as-of rules, universe with delisted names, every size tier, known flaws |
| Unit and outcome | What one observation is; the outcome and its horizon; entry at a time the desk can trade |
| Comparison | Price-aware baseline or matched controls (for stocks: same volatility, session and tier); the own-history baseline |
| Eras | Discovery and holdout dates; purge gap; walk-forward schedule for fitted parts |
| Family and trials | Every variant in the family; trials already run before this registration |
| Test | Statistic; Newey–West lags or block length; clustering; multiple-testing rule (BH q) |
| Pass rule | For example: discovery \|t\| ≥ 3, holdout same sign with \|t\| ≥ 2, BH q < 0.10 |
| Power | Independent observations; minimum detectable effect; what a null will and will not rule out |
| Null dry run | The whole pipeline on random walks or resampled data; acceptable false-positive rate |
| Robustness lenses | Company-level counts, fine matching, factor-neutral, bear windows, next-open timing, duplicates removed |
| Frozen artifacts | Code, tables and spec with their SHA-256, recorded before the holdout is scored |
| Decision | What each verdict (CONFIRMED, NULL, REJECTED, INCONCLUSIVE) will trigger |
