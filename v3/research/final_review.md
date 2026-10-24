# Independent mathematical and implementation review

Reviewed on 2026-10-24. Scope: `SKILL.md` section 2a, `references/edge-protocol.md`, `references/frontier-sources.md`, `scripts/edge_mechanics.py`, and `scripts/test_edge_mechanics.py` under `/root/.codex/skills/remote-skills/skill-6adbf874c518819199faa0d9b89784f2`.

No evaluation tasks or outputs were accessed. No network, trading, or external write actions were taken. Implementation was not edited. The reviewed mechanics source SHA-256 was `1c8b5bcee68b7c8826642b18397e80597547cccf4e129f72d7ec194f7c62f32d`.

**Final status:** the one numerical defect found below has been corrected in the staging kernel and independently reverified. The original finding remains in this record for auditability. See the remediation note at the end.

## Material finding

**P2 — Cancellation of the probability term can materially overstate a CARA premium at large scaled wealth ranges.** In `seller_reservation_premium`, the large-exponent branch constructs the candidate exponent by adding `scaled liability` to an already rounded `log_base`. When wealth and liability cancel economically, probability information previously lost in `log_base` is not recovered.

Reproduction:

```python
seller_reservation_premium([.5, .5], [0, 1e16], [0, 1e16], 1)
# Actual: 1.0986122886681096
# Correct: log(2) - log1p(exp(-1e16)) = 0.6931471805599453
```

Here both candidate states have terminal wealth before premium `W-L=0`. Therefore the numerator expectation is exactly 1 and the original expectation is `(1+exp(-1e16))/2`. The returned premium is 58.5% too high. The second state's `log(.5)-1e16` rounds to `-1e16`; adding `1e16` creates a numerator log weight of 0 instead of `log(.5)`.

This is an extreme numerical conditioning boundary, not evidence of an ordinary-scale financial-model error. The same family produces an absolute error of approximately `1.60e-5` at wealth/liability `1e12` and `9.52e-10` at `1e8`, with gamma 1. Nevertheless the API accepts these finite inputs and returns a confident finite value instead of rejecting a loss of precision. A premium offer between the correct and reported values changes the acceptance decision in the supplied model.

Suggested repair: form/stabilize the candidate's net-wealth exponent before adding the log-probability term, avoiding cancellation of independently scaled wealth/liability terms after the probability term has been rounded away. Add this correlated `W=L` family to regression tests. Check both the existing rare-tilted-state regression and tiny-gamma cases after the change. Reject unsupported precision ranges if a stable calculation is unavailable.

## Verified checks

- All 20 existing added mechanics tests passed via `python -m unittest discover -s <skill>/scripts -p 'test_edge_mechanics.py' -v`.
- Ran 1,200 deterministic differential CARA calculations against an independent 80-digit Decimal evaluation, seed 1871. State counts were 2–6; probability weights were sampled log-uniformly from `1e-12` to 1 then normalized; wealth/liability scale was log-uniform from `1e-6` to `1e12`; signed wealth/liability draws were uniform within each scale; gamma was log-uniform from `1e-18` to 10. No comparison exceeded `abs(actual-expected)/max(1,abs(expected)) > 1e-10`; maximum error was `5.65e-14`. Independent wealth/liability draws do not exercise the correlated cancellation defect above.
- The complete reproducible review script, parameters, source hash and adversarial analytic cases are in `check_mechanics_precision.py` next to this review. It exits nonzero when the numerical boundary remains unresolved; the random differential sample itself passed.
- The finite information-value formula correctly uses unnormalized joint-probability contributions, the same feasible action menu, and optional use of the signal. The decision-threshold example, impossible signal handling, garbling example and XOR example are mathematically correct.
- The CARA formula, liability sign convention and portfolio coupling are correct. The derivative of the reservation price for an infinitesimal liability is `E[U'(W)L]/E[U'(W)]` under the stated constant terminal cash premium convention. Existing hedge rights and interim feasibility are explicitly kept outside the simple calculation.
- The payoff checker distinguishes nonnegative payoff with a possible positive benefit from strict sure profit. It correctly keeps unknown probability support as `None`, permits benefit at negative initial cost, excludes zero-probability losing states only from the almost-sure condition, and preserves all supplied states for the sure-profit condition. Upfront cost is not double-counted in terminal cash flows. Explicit financing legs are required by the contract.
- The source register contains 19 labeled entries. Its application summaries consistently separate model assumptions, source findings and proposed engineering use. No internal mathematical contradiction or claim of proven live profitability was identified in the reviewed text.

## Scope and evidentiary limits

The actual companion implementation has three finite-model calculators. It does not estimate likelihoods or probabilities, optimize hedges, enumerate contract semantics, solve a global arbitrage search, evaluate LLM adherence, or establish executable profit. The reviewed protocol accurately states those boundaries and delegates empirical identification and execution validation to further work. The instructions/observed behavior/economic advantage/deployable capture distinction is appropriate.

The public source documents, publication metadata, prior-source count and claimed inspection depth were not independently fetched during this offline review. Therefore this review verifies internal consistency and numerical derivations, not external bibliographic authenticity or research completeness. Passing mathematical examples and tests provides no evidence of market edge, prospective model behavior or capture.

## Remediation verification

The kernel maintainer corrected the large-exponent calculation by anchoring the numerator on net wealth `W-L` before adding log probabilities. Exact rational differences preserve the supplied float values through net-wealth subtraction. The resulting formula has the correct cash anchor and difference of centered log-expectations. Existing tiny-gamma and rare-state recovery branches continue to pass.

Independently checked final staging source `/workspace/scratch/f5c1e77ad2df/edge_v3/kernel/edge_mechanics.py`, SHA-256 `2f649523515a8d9e7a53fcd9124df769ddcf9a8440579a92c9484785a863f81a`: all 23 unit-test methods passed; all 1,200 deterministic Decimal comparisons passed, maximum normalized error `5.90e-14`; the four correlated boundary cases at `1e6`, `1e8`, `1e12` and `1e16` returned `log(2)` with zero float discrepancy. Before/after output is preserved in `precision_before_fix.json` and `precision_after_fix.json`.

The corrected implementation also rejects a severely cancelling cash anchor and adjustment (residual below `1e-8` of component scale) with a higher-precision `ValueError`. This is a conservative numerical-domain limitation: a mathematically valid near-zero premium may be rejected. It avoids presenting that unresolved precision case as an exact zero. The function's public docstring now states that limitation. The final ratio-form guard avoids underflow in a multiplied tolerance.

Per the parent task's provenance record, this kernel revision occurred after the behavior-task snapshot was frozen. Core instructions and frozen behavior tasks were not changed by this review or the numerical repair. The mechanics revalidation must not be described as rerunning or improving the frozen behavior evaluation.
