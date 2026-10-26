# Validation record — Trading Edge Lab v4

Completed 26 October 2026. This record separates what was checked, what was measured and what is still open.

## Tests

```bash
python -m unittest discover -s skills/engineer-trading-edge/scripts -p 'test_*.py' -v
python v4/research/verify_research_stats.py
```

- **88 tests pass** at the skill path: 20 for the adaptive arbiter and 23 for the mechanics calculator (both carried
  from v3 unchanged), 32 for `research_stats.py` and 13 for `ledger_lint.py`. The v3 snapshot's 43 tests and its
  precision check still pass at `v3/skill/`.
- **Published worked examples reproduced** by `research_stats.py`:

  | Source | Published | Computed |
  |---|---|---|
  | Bailey and López de Prado (2014), DSR example (N 100, V 1/2, T 1,250, skew −3, kurtosis 10) | SR0 ≈ 0.1132, DSR 0.9004 | 0.113172, 0.900397 |
  | Same, N 46 / normal returns at N 88 | 0.9505 / 0.9505 | 0.950502 / 0.950491 |
  | Bailey and López de Prado (2012), PSR of a 24-month record (SR 0.458) | 0.982 normal, 0.913 with moments, 0.953 at 36 months | 0.9817, 0.9134, 0.9535 (the paper prints SR to three decimals) |
  | Same, MinTRL (SR 2/√12 vs 1/√12, skew −0.72, kurtosis 5.78) | 59.895 months, where PSR = 0.95 | 59.8951 months, 0.95 |
  | Same, IID normal MinTRL, annual SR 2 vs 1 | 2.73 / 2.83 / 3.24 years (daily / weekly / monthly) | 2.731 / 2.829 / 3.240 |
  | Benjamini and Hochberg (1995), 15 p-values at q = 0.05 | 4 rejections; adjusted values as published | 4 rejections; equal to 7 decimals |

- **The desk's own record:** its 2026-10-16 MinTRL table (10.8 / 2.7 / 1.2 / 0.7 years for annual SR 0.5 / 1 / 1.5 / 2)
  and best-of-550 multiplier (3.08) reproduce as 10.83 / 2.71 / 1.21 / 0.69 and 3.081.
- **Independent implementation:** numpy and scipy recompute BH, Newey–West (as a matrix quadratic form), PSR, MinTRL,
  SR0 and the Wilson interval; every difference is at machine precision
  ([research_stats_crosscheck.json](research/research_stats_crosscheck.json)). On 2,000 random inputs the desk's own
  statistics module gives identical PSR, MinTRL and SR0, and identical BH rejections in 300 of 300 sets.
- **Null calibration:** on 200 simulated random walks of 500 steps, a 5% t-test on overlapping 20-period returns fired
  67.5% of the time, Newey–West with 19 lags 11.5%, and non-overlapping windows 5.0%.

## Unified prompt

- `scripts/build_unified_prompt.py` rebuilds v3.0 byte for byte against `v3/Trading_Edge_Unified_Master_Prompt_v3.0.txt`
  and v4.0 byte for byte against the root prompt.
- v4.0 is 55,497 bytes in 28 sections: 7,487 bytes more than v3.0, for the Edge Ledger, the workflow and the field
  rules.

## Skill and repository checks

- `SKILL.md`: 177 lines; valid frontmatter (name, 546-character description).
- Every relative link and heading anchor in the skill, the root documents and this folder resolves.
- v1, v2 and v3: all 100 files from the previous manifest are byte-identical; v3 gains only the preserved v3.0 prompt.
- Field casebook: 20 cases; every number was read from the desk's records for this release, and each case cites its
  record by date and study.
- Literature map: 55 references, each checked on 26 October 2026 against Crossref metadata (54) or the RePEc record (1).
- Public safety: a pattern scan for secrets, tokens, keys, account identifiers, e-mail addresses, hosts, IP addresses
  and machine paths found nothing in the added or edited files. GitHub's secret scanning could not run: the
  repository does not have GitHub Advanced Security enabled.

## Behavior test

Frozen at commit `c9308f6` before any run: 12 fictional cases ([evaluations/cases.json](evaluations/cases.json)),
a 98-point rubric ([evaluations/rubric.json](evaluations/rubric.json)), a runner and
[freeze.json](evaluations/freeze.json), which pins the cases, rubric, runner and the skill tree under test.

| Arm | Answers | Score |
|---|---|---|
| Without the skill | 0 of 2 | not run |
| With the skill | 0 of 2 | not run |

**Status: UNVERIFIED.** No arm has run; [RUNNER.md](evaluations/RUNNER.md) gives the steps, and the scores will
replace this table with n = 2 answers per arm. v3's comparison scored 24 of 24 in both arms, which showed nothing about
the skill's effect; the v4 cases are built to avoid that ceiling.

## Scope

No market backtest, forward record or live order was produced by this release. The casebook's live-desk numbers
describe one desk's paper trading on live quotes with simulated fills, over four full sessions.
