# Live firing audit: prove the desk trades the edge it researched

An edge that never executes is worth zero ([C20](field-casebook.md#c20-an-edge-that-never-executes-is-zero)), and an
edge that executes differently from its research is a different, untested strategy. This reference is the procedure
that proves neither is happening: a run-in-order audit, seven gates with pass lines, and a row template. Numbers are
from one desk's promotion passes and two full audits, 14 to 16 November 2026, about 970 strategy rows on a paper desk
with live quotes. They are that desk's observations, not market-wide estimates.

It assumes the engineering contracts in [desk-runtime.md](desk-runtime.md) and the cost terms in
[execution-edge.md](execution-edge.md); it does not restate them. Arming at real size is
[edge-discovery-protocol.md section 12](edge-discovery-protocol.md#12-amendment-real-size-with-a-floor-instead-of-a-shadow-stage).

## Contents

1. When to run it
2. What the audits found
3. The audit, step by step
4. Gate A: research-to-live parity
5. Gate B: feeds, calendars and corporate actions
6. Gate C: timing windows
7. Gate D: code and controls
8. Gate E: diagnosing a silent strategy
9. Gate F: order path and book consistency
10. Gate G: runtime regressions
11. Audit row template and pass rule

## 1. When to run it

| Trigger | Run |
|---|---|
| A rule is installed, promoted or resized | Gates A–D, then protocol section 12 |
| Zero fires over a window in which the research fired | Gate E, then A–D on the failing rule |
| Two tools report different counts of the same thing | Step 3.3, then Gate E |
| A feed, calendar or hand-entered list is added | Gate B |
| An engine, config or shared module changes | Gate D |
| Scheduled audit (daily before the open; weekly in full) | Section 3, every row |

NEVER answer "is it live?" from a headline state, a smoke test of a few passes, a catalogue or a config file. Answer
only from the gates.

## 2. What the audits found

Every gate below exists because its failure cost this desk fires, a position or a false verdict.

| Failure | Measurement | Gate |
|---|---|---|
| Rule named for a calendar the live engine did not implement | 0 live fires against 59 research entries (Jaccard 0.00) | A1 |
| Rule researched to exit at the close, executed at the next open | z 2.9 → 1.47; not promotable | A4 |
| Live hub kept 420 daily bars; terms ranked over 504 sessions | Three terms failed closed, the rest ranked on a shorter window | A3 |
| Smoke test of 3 passes called 71 routes healthy | A 60-session replay found 12 silently dead | E1 |
| Generated catalogue older than the code | 293 installed strategies missing; 14 reported blocked that were already replaced | 3.1 |
| Two tools on different inputs | 14 paused versus 99 for the same three sessions; true count 0 | 3.3 |
| Hand-entered auction list | Coverage ended 10 days after install | B1 |
| Stale bar on an acquired stock | A momentum rule bought a name acquired for cash two months earlier | B3 |
| Crypto pair without a separator read as an equity | A 24-hour exit held over a weekend | B5 |
| 5-minute entry window under a 5-minute loop | About one monthly window in three missed | C1 |
| Calendar AND with an impossible conjunction | No qualifying date in the next 12 months | C3 |
| Single-name notional cap in config only | Never enforced | D1 |
| Breakdown test whose window included the tested bar | Could never trigger | D2 |
| Engines without a kill switch | 190 modules | D4 |

## 3. The audit, step by step

1. **Enumerate from the live loader.** Load every strategy through the registry path the live process uses and write
   one row each (section 9). If a catalogue is used, compare its timestamp with the newest strategy or engine file
   and regenerate it when older.
2. **Give every row one state:** `fired`, `armed_not_due` (next due date), `waiting_data` (date the data clears),
   `merged` (host id), `blocked` (named blocker and the route trading meanwhile), `not_loaded` or `broken`. "No
   signal" is not a state; it is the question Gate E answers.
3. **Reconcile instruments before numbers.** When two tools disagree, prove they read the same snapshot, sessions and
   latest state before comparing counts. Fix the input path, never the count.
4. **Judge only completed sessions.** Drop the in-progress session and non-trading days from every firing window. An
   N-session rule needs N archived sessions; with fewer, the output is the date the rule can be judged.
5. **Run Gates A–G** on every row that is not `fired` and on every row installed or resized since the last audit.
   Gate G may be run once per process rather than once per row.
6. **Fix and re-run the failed check.** Done means the identical check now passes, the full suite is green, the change
   is committed and the live process runs the committed version. NEVER pause a strategy as a fix: pausing switches
   off the edge and keeps the bug. Repair it, or replace it with a recalibrated copy that trades.
7. **Report** counts by state, every non-`fired` row with its reason and date, and each fix with its commit. Status
   words follow [truth-gates.md](truth-gates.md).

## 4. Gate A: research-to-live parity

**A1. Measure firing parity per term before wiring a rule live.** Replay the live engine over the research window and
compute the Jaccard overlap of its entry dates with the research entries. Pass: ≥ 0.95 per term. A term's name is not
its implementation; the opex term above went from 0.00 to 1.00 once built from the live calendar code.

**A2. Run parity on the calendar the rule actually saw.** A live holiday list that starts recently turns every older
holiday into a session. Patch history with the true exchange calendar to test the logic; verify the forward list
against the exchange separately. Skip this and you misdiagnose: one desk read venue anchors as one session off
(Jaccard 0.45–0.93) and nearly built a date-snapping port; patched, every anchor read 1.00.

**A3. Check live data depth against every window.** List each feature's lookback and rank window and compare with
the bars the live hub keeps, on the live hub, not the replay hub. Pass: depth ≥ the longest window plus warm-up.
Ranks rebuilt for cross-sectional cells MUST use the universe the desk trades (a 33-name live universe, not a
6,000-name research panel).

**A4. Measure execution parity, not only signal parity.** Re-score the rule under the live price convention (signal
close vs next open; exit at the close vs the next open) before promoting. Pass: the live-convention score still
clears the promotion gate. Otherwise build the exit the research assumed, half-day aware, with a late-exit fallback.

**A5. Print component parity beside every composite.** A 16-component count at 0.64 replay parity inside a joint
condition reading 0.86 hides its drift unless printed. Cache features by their dependencies, not their names
([desk-runtime.md section 2](desk-runtime.md#2-data-and-clock-semantics)): a name-only key served test-hub
features to the live hub, a collision only a two-hub test exposes.

## 5. Gate B: feeds, calendars and corporate actions

**B1. Every hand-entered feed MUST carry a coverage end date, and the rule MUST fail closed past it.** Write the
renewal date into the strategy table. Prefer a point-in-time live feed (first_seen before the decision date, refreshed
every few hours) unioned with the research history; a failed fetch NEVER refreshes the freshness stamp. Pass: parity
with the research series on the overlap (the rebuilt auction feed matched 102 of 102).

**B2. Check corporate actions on every held and candidate symbol.** Refuse an equity entry whose newest daily bar is
more than 10 calendar days old, and check mergers, delistings and splits on holdings. A stale price is not a price.

**B3. Meet a provenance gate by qualifying the data, never by skipping the check.** Take the series from a second
source and accept it only if it reconciles: every adjustment day carries a dividend or split event, and the signal
close matches the primary feed. On failure fall back explicitly (total return → price return) and say so in the
manifest.

**B4. Decide 24/7 versus session-only trading from the venue record, not the symbol's shape.** If a heuristic is
unavoidable, run it over every live symbol before trusting it.

**B5. Judge a data gate on recent receipts.** A gate that cleared at 08:20 still dominates the day's earlier receipts.
Count it active only if it appears in the last 6 receipts (about 30 minutes).

**B6. Label a panel built from today's constituents as a survivorship snapshot** ([C13](field-casebook.md#c13-point-in-time-the-leak-and-the-volume-flaw)).
Level correlations of 0.998 with a reference do not remove the bias; keep it at the floor until a point-in-time
membership re-test.

## 6. Gate C: timing windows

**C1. An execution window MUST span at least two loop intervals.** Otherwise the pass lands outside it by
construction. Widen it inside the same allowed sessions (09:35–09:40 became 09:35–10:30) or tighten the loop.

**C2. Every scheduled flatten MUST run while the venue is open,** half-day aware. A 16:00 flatten runs after the close
and carries the position to the next open.

**C3. Replay a calendar expression forward before installing it.** Enumerate qualifying dates over the next 12–24
months. Pass: at least one. The failing case ANDed a pre-event entry with "the prior session is in opex week"; the
fix flipped only that layer to its complement and re-tested it (n 174, t 3.30 against n 44, t −0.09).

**C4. Report not-due as not-due.** A monthly rule outside its window is `armed_not_due` with its next date, plus any
separate blocker. NEVER promise "fires at 09:36" for a rule whose next window is next month, and never call it broken.

Entry prices follow protocol practice 54: never enter at a price the signal has not printed.

## 7. Gate D: code and controls

**D1. A limit in a config file is not a limit until code reads it.** For every cap, name the enforcing line and the
test that fails when it is breached. Pass: both exist.

**D2. A lookback MUST exclude the bar being tested.** `close < min(low[-10:])` is never true, because the bar's own
low is at or below its close; compare with `low[-11:-1]`. After one hit, search every engine:

```bash
rg -n "(min|max)\((low|high|close)\[-[0-9]+:\]\)" --type py
```

**D3. Load every strategy through the real registry in tests.** A subclass missing one default raised inside an
unrelated strategy's stack; a test that constructs the happy case never touches that path.

**D4. Give every strategy a kill switch; one switch can cover all of them.** A named-id list that blocks new entries
and lets exits run covers legacy modules without editing each. Pass: a test shows entries blocked and exits running.

**D5. Keep provisional engines out of the live tree** until committed (protocol practice 45).

## 8. Gate E: diagnosing a silent strategy

**E1. Treat zero fires as a bug report until a replay proves the rule rare.** Replay the live engine over at least 60
sessions without look-ahead. Pass: fires match the research rate, or the rule is shown rare and its next date printed.

**E2. Census the strategy's own reject reasons before judging it.** Read its decision stamps (stood-down flags,
blockers, exception text, quantity below one, quote age), not its headline state. A sleeve that read "no signal" hid a
missing quote door, a host slice of $2k against a $10k design, and a memory bound smaller than its warm-up.

**E3. Chase one candidate through the disposition log until it is admitted.** Gates are stacked, so each fix reveals
the next. Replay one historical signal, fix the first refusal, replay again. One short signal failed in turn on quote
availability, borrow, replay clock alignment and displayed size before admission; a continuous replay then exposed a
stale prior-session reference. Clear the replay journal first, or candidates already disposed are skipped.

**E4. Fix a hosted rule in a private copy that changes only bounds, doors or calendars, never the rules.** Keep the
shared module pinned as the control. When a pinned engine's provenance gate blocks it, call the engine's own pure
decision function on a qualified second feed (B3); three blocked books rebuilt this way fired 48, 37 and 3 times in
120 replay sessions.

**E5. Classify a merged clone as `merged` with its host.** Its parent trades the combined size, so it emits nothing by
design and is otherwise flagged dead forever.

**E6. Load vendored modules by file path under a private name.** A vendored package with a generic top-level name hid
a local module only when another adapter loaded first, so the failure appeared only in the live process order.


## 9. Gate F: order path and book consistency

**F1. A short is a side, not a sign.** If a rule emits a short as a negative quantity, a sizer of the form
min(qty × price, cash) goes negative and refuses the order forever. MUST normalize a negative quantity to side=sell
with the absolute quantity before sizing. Pass: a dry-run through the real order path opens a short for every short
rule.

**F2. Pooled family masks must respect direction.** OR-ing sell-side dates into a long book cancels the effect.
MUST drop opposite-direction terms in the loader. Pass: buy-side and sell-side dates, scored separately, keep their
own signs.

**F3. Dedupe from the live book, not from a side file.** A claims file in a shared temporary path can leak across
test desks and block a legitimate entry. Pass: "does another family member hold this symbol?" is answered from the
desk's own replayed book.

**F4. A never-fired diagnosis needs a rate.** Replay the rule's own condition. Call it miscalibrated only when at
least two fires were expected in the window. NEVER treat every instrument string as belonging to one venue. Pass: the
expected count, the observed count and the venue map are printed beside the verdict.

**F5. Calibrate stops from the rule's own trades** (protocol practice 95). Pass: the stop and any target are computed
from that rule's MAE/MFE and cost at most 5 bp / 2 bp of the time-only mean.

**F6. Twin a calendar on the mechanism instrument** (protocol practice 96). Pass: the parent on the mechanism
instrument is still running, the side was picked on the in-sample half only, and out-of-sample is reported honestly.

## 10. Gate G: runtime regressions

**G1. Track every stage's p50 by day, not only the pass total.** A single headline ("the box slept") can hide a
stage that grew from under a second to tens of seconds over two days. Pass: a per-stage daily p50 is on disk.

**G2. Profile the live process before theorizing.** A short read-only sample of the running process beats a code
review guess. Pass: the named bottleneck came from a profile, not from intuition.

**G3. Parse shared state once per file version** (mtime, size, inode), hand out shallow copies, and prove parity on a
copy of the live file with a fixed clock before going live.

**G4. Skip unchanged expensive work by content signature, with a forced refresh floor** so "unchanged" can never
become "never".

**G5. Do not assume the platform plan; read it from behaviour** (cron count, CPU p99, error rate) and design limits
from that.

**G6. Locks and order intents belong in a strongly consistent store with deterministic order ids.** Eventually
consistent key-value stores are not a lock. The same client order id on every path makes a race produce one order.

**G7. Check the artifact's mtime, not the pass's exit.** A step that returns an error dict instead of raising can
freeze its output while every pass looks green. Match file names with a strict pattern, not a prefix test.

**G8. Compute only what is read; batch whole-file writes; index by the caller's filter key.** Prove byte-identical
outputs after a trim or a batch. After a host or workspace move, verify the runtime (environment, output directories,
write access) before profiling or trusting a green loop. Make routine checks script-first: cheap counts, a saved
cursor, skip when nothing arrived, fail open, and never seed the cursor.

## 11. Audit row template and pass rule


One JSON object per strategy per audit:

```json
{
  "strategy_id": "",
  "state": "fired | armed_not_due | waiting_data | merged | blocked | not_loaded | broken",
  "last_fire": "YYYY-MM-DD | none",
  "next_due": "YYYY-MM-DD | unknown",
  "host": "",
  "blocker": "",
  "route_trading_meanwhile": "",
  "gates": {"A_parity": "pass|fail|n/a", "B_data": "", "C_timing": "", "D_controls": "", "E_silent": "", "F_order": "", "G_runtime": ""},
  "evidence": ["replay or log path"],
  "fix_commit": ""
}
```

**GREEN** only when every row is `fired`, `armed_not_due`, `waiting_data` or `merged` with its date or host, and every
`blocked` row names its blocker and a route already trading. Any `broken` or `not_loaded` row, any zero without a
replay, or any check run on inputs other than the live process's makes the audit **PARTIAL**.

## Source and maintenance

Distilled from one desk's edge-discovery playbook (practices 55–110 and their honesty notes, 15–17 November 2026), its
promotion ledgers, two desk audits and a later correctness and runtime pass. Aggregate facts only; no vendor data, accounts, machine paths or personal
identifiers. Revise when a gate changes and record the revision in PROVENANCE.md.
