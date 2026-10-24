# Validation record — Trading Edge Lab v3

Completed 24 October 2026, America/New_York. This record distinguishes artifact verification, numerical behavior, observed LLM answers and market evidence.

## Numerical implementation

The final skill contains the unchanged adaptive arbiter plus the new mechanics companion. Running the combined suite passes **43 test methods**: 20 arbiter tests and 23 mechanics tests. The new tests cover finite information value, information with no decision value, redundant/garbled observations, XOR complementarity, portfolio-state risk pricing, payoff semantics, explicit financing, probability support and invalid inputs.

```bash
python -m unittest discover -s v3/skill/scripts -p 'test_*.py' -v
python v3/research/check_mechanics_precision.py
```

An independent review found an accepted-input numerical defect in the initial CARA implementation: very large correlated wealth and liability could cancel after probability information had been rounded away. The case `p=(.5,.5), W=(0,1e16), L=(0,1e16), gamma=1` returned about 1.0986 rather than log(2). The final implementation centers net wealth before adding log probabilities and preserves supplied float differences through exact rational arithmetic. The failure, repair and source hashes are retained in [final_review.md](research/final_review.md).

The repaired kernel passes **1,200 deterministic comparisons with an independent 80-digit Decimal reference**, with maximum normalized error approximately `5.90e-14`, plus four correlated cancellation cases. The final source SHA-256 is `2f649523515a8d9e7a53fcd9124df769ddcf9a8440579a92c9484785a863f81a`. The reproducible script, seed 1871 and before/after results are archived. A conservative guard rejects some valid but ill-conditioned near-zero premiums and requires higher precision; this limitation is explicit.

These tests verify arithmetic and specified behavior on supplied models. They do not establish realistic probabilities, exhaustive settlement semantics, correct utility preferences, live execution, market profitability or production latency.

## Exploratory behavioral comparison

Six fictional tasks covered conditional information and duplicated evidence; portfolio utility; false and repaired contract baskets; constructive strategy invention; counterfactual identification; and computation/latency/capacity choice. Each case had four prespecified binary criteria, 24 per session. Two fresh sessions received only the task instructions and supplied inputs; two received the frozen v3 skill as well. All sessions had a 2,500-word answer cap and calculation tools. No solver received the rubric or other answers.

The candidate author froze the skill core before reading the exact evaluation tasks. The independent case author knew the existing framework and research objective, so the benchmark is purpose-built rather than externally independent. All sessions inherited the same parent model configuration with no requested override; exact served-model identifier, random seeds and sampling parameters were not exposed. Available skill metadata may have been visible to both conditions, while baseline instructions prohibited loading the skill body. Filesystem isolation was instructional, not enforced. No complete independent tool-access audit is claimed.

Two graders received anonymous response IDs without the condition mapping; the second processed answers in reverse order. Both used the frozen rubric and checked arithmetic. Answer content could still reveal its condition. The primary author checked the numerical targets and the only noted semantic gray area: the baseline answers expressed source separation and rejection tests less explicitly, but their proposed prospective conditional comparisons satisfied the rubric. No rescoring was introduced to manufacture an improvement.

| Session | Condition | Grader A | Grader B | Critical errors |
| --- | --- | ---: | ---: | ---: |
| reasoning_a | No skill body | 24/24 | 24/24 | 0 |
| reasoning_b | No skill body | 24/24 | 24/24 | 0 |
| skill_a | Frozen v3 skill | 24/24 | 24/24 | 0 |
| skill_b | Frozen v3 skill | 24/24 | 24/24 | 0 |

**Observed difference: zero on this rubric.** The skill-assisted sessions performed the required operations, including accepting beneficial opportunities where justified. The baseline sessions did too. This comparison therefore demonstrates no incremental accuracy gain from the skill on these six cases. It also does not prove equivalence, universal reliability or a lack of benefit on other tasks. The small shared case set has a ceiling effect; four sessions are not 24 independent prompt-effect experiments.

The useful evidence is the preserved behavior, calculations and identified limits. Any stronger causal or general-performance claim requires a larger independently authored task population, controlled repetitions, resource accounting and prospective scoring. Once published, these cases are regression material, not a future untouched holdout.

### Frozen artifacts and revision boundary

- Cases SHA-256: `ff3c9939262b8713c179c0186978559d633d46b0f7ce1f5492c8deba97bc6d09`.
- Rubric SHA-256: `95a15ffd054093d5afc9855d8310ae1b2990286b9b61d615dbffd38cc40b7e8e`.
- Skill core SHA-256: `7303d8b456813bcfac4c5457b30d60be190a4c4dd23f03598e54433b63104c58`.
- [All frozen skill-file hashes](evaluations/skill_snapshot_hashes.json), [exact skill under test](evaluations/skill_under_test/), [cases](evaluations/cases.json), [rubric](evaluations/rubric.json), [answers](evaluations/outputs/), [grading A](evaluations/grade_a.json), [grading B](evaluations/grade_b.json) and [condition mapping](evaluations/condition_map.json) are retained.

The precision repair occurred after the behavioral snapshot. Only `scripts/edge_mechanics.py` and its test file changed in the installed skill after that snapshot; the core and references remained identical. The frozen directory preserves the pre-repair calculator for evaluation provenance and must not be used as the current implementation. Use `v3/skill/scripts/` for the corrected code. The numerical revalidation is a separate result, not a rerun of the behavioral comparison.

## Artifact checks and current scope

The skill metadata validator passes. Local reference paths resolve. The unified prompt has one instruction boundary and one output contract; its builder reproduces the saved text exactly. The original v1/v2 studies and historical code are retained. The current root prompt combines the earlier framework and addendum with the v3 procedures; no second prompt is required.

No new market-data backtest, prospective probability-forecasting trial, real-money order, production integration or measured trading-return improvement was performed. The deliverables are research, explicit procedures, tested finite-model tools and a transparent behavioral record.
