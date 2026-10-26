# Truth gates: reporting strategy work honestly

Adapted, in our own words, from InfinityBlade, the engineering doctrine the owner's desks run under. It governs how an
agent reports work on strategies, sleeves, backtests and desks. Verdicts on claims (CONFIRMED, NULL, REJECTED,
INCONCLUSIVE) are in [research-protocol.md](research-protocol.md#9-verdicts); this file covers the state of the work.

## 1. SCOPE before material work

| Field | For strategy work |
|---|---|
| **Surface** | The strategy, sleeve, data, code or desk component the work may touch |
| **Constraints** | Timing authority, mandate, risk limits, data rights, no real-money action without authority, what must not change |
| **Outcome** | The decision the evidence will change, stated so it can be observed |
| **Proof** | The artifact that would demonstrate it: a registered test on the final code and data, a forward record, a fill |
| **Edges** | Data limits, power, dependencies, other people's systems, deadlines |

## 2. Status words

| Status | Use when |
|---|---|
| **GREEN** | The final artifact shows the outcome: the test ran on the final code and data, or the change is observed live |
| **PARTIAL** | A named part is proven; the rest is listed with the proof it still needs |
| **BLOCKED** | Completion needs access, authority, data or a decision the agent does not have; name the smallest unblocking step |
| **UNVERIFIED** | The work exists, but the outcome-level proof was not obtained; name the missing proof |

Any FAIL, BLOCKED or UNVERIFIED row in an acceptance list keeps the whole report from GREEN.

## 3. Gates

1. **Adjacent proof is not proof.** A backtest is not a forward record. A replay is not live. Simulated fills are not
   real fills. One size tier is not every tier. One era is not every era. A passing unit test is not a deployed
   change.
2. **A failed route is not proof the outcome is impossible.** Classify the failure (wrong hypothesis, defect, missing
   data, permission, tool) and say what it disproves before choosing the next route.
3. **Do not repeat an action that did not reduce uncertainty.** Each action needs an expected discriminating result.
   Rerunning the same search, the same backtest or the same failing command without a new hypothesis is a spiral.
4. **Contradicting evidence stops the line.** When a record contradicts the working hypothesis, reproduce it before
   acting. Record before fixing: the desk's audit premise of a stale feed was falsified by the first recorded pass
   ([C20](field-casebook.md#c20-an-edge-that-never-executes-is-zero)).
5. **Final evidence follows the last change.** Any material change after a test invalidates that test's claim about the
   new artifact.
6. **Do not shrink the task to fit the report.** A narrow subtask can be GREEN only under its own name.
7. **Never invent** data, fills, sample sizes, trial counts or results. If a computation cannot run, deliver its
   specification and report the result as unknown.

## 4. Ledgers and receipts

Keep an evidence ledger while working:

```text
Hypothesis:
Action:
Expected discriminator:
Observed evidence:
Conclusion:
Next uncertainty:
```

End with receipts:

```text
Status: GREEN | PARTIAL | BLOCKED | UNVERIFIED
Tested: what ran, on which artifact (commit, data version)
Expected / observed:
Protected invariants checked:
Missing proof:
Next experiment:
```

## 5. Minimum sufficient change

- Repair the demonstrated failure at its source; leave verified paths and unrelated work alone.
- A demonstrated defect (a bug, stale data, a broken lifecycle, mis-sizing) is fixed directly with a failing test
  first. A change of strategy is an experiment with a rejection rule.
- When a pipeline is slow, measure every stage and repair the dominant one
  ([C18](field-casebook.md#c18-speed-late-opens-stale-prices-and-the-route-stage)).
