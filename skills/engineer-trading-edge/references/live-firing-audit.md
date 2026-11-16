# Live firing audit: make every research rule trade as specified

This reference is a tool. Run it when a rule moves from research to a live or paper desk, when any strategy is silent,
and on every scheduled desk audit. It turns field rule 20 ([C20](field-casebook.md#c20-an-edge-that-never-executes-is-zero))
into gates you can pass or fail: **an edge that never executes is worth zero, and an edge that executes differently
from its research is a different, untested strategy.**

It distils one desk's promotion passes and two full desk audits of 14 to 16 November 2026, which covered about 970
strategy rows. Every lesson below cost that desk a missed fire, a phantom position, a cap nobody enforced or a
false alarm before it was written down. Examples are anonymised and kept to one line. Use
[edge-discovery-protocol.md](edge-discovery-protocol.md) to find and score the edge, and this file to make sure the
desk actually trades it. Use [desk-runtime.md](desk-runtime.md) for the engineering contracts it assumes.

## Contents

0. Triggers: when you MUST run this file
1. The audit, step by step (run in order)
2. Gate A: research-to-live parity
3. Gate B: data feeds, calendars and corporate actions
4. Gate C: timing windows and exits
5. Gate D: code, configuration and controls
6. Gate E: diagnosing a silent strategy
7. Gate F: sizing and arming at real size
8. Audit row template and pass rule
9. Anti-patterns this file exists to stop

---

## 0. Triggers: when you MUST run this file

Run it, in full, when any of these is true. Each is a point where the desk silently stops trading its edge.

| Trigger | Run |
|---|---|
| A research rule is being installed, promoted or resized | Gates A, B, C, D, F |
| A strategy has zero fires over a window where its research fired | Gate E first, then A-D |
| Two tools report different counts for the same thing (paused, live, fired) | Step 1.3 and Gate E |
| A data feed, calendar file or hand-entered list was added | Gate B |
| An engine, config file or shared module changed | Gate D, then the test in D6 |
| A scheduled audit (daily or weekly) | Section 1, all steps |

Never answer "is it live?" from a headline status, a smoke test of a few passes, or a config file. Answer only from
the gates below.

## 1. The audit, step by step (run in order)

1. **Enumerate from the live loader, not a list.** Load every strategy through the same registry path the live
   process uses and write one row per strategy (template in section 8). A generated catalogue is a snapshot: compare
   its timestamp with the newest strategy or engine file and regenerate it if older.
   *Why:* one desk's catalogue missed 293 strategies installed after it was written and still reported 14 as blocked
   that had already been replaced.
2. **Classify each row with one state:** `fired`, `armed_not_due` (with the next due date), `waiting_data` (with
   the date the data clears), `merged` (with the host that trades it), `blocked` (with the named blocker and the route
   being built), `not_loaded`, or `broken`. "No signal" is not a state; it is a question.
3. **Reconcile instruments before reconciling numbers.** When two tools disagree, first check that they read the
   same inputs (same snapshot, same sessions, same latest document). Fix the input path, not the count.
   *Why:* a census said 14 paused and a guard said 99 for the same three sessions only because one tool was not
   passed the latest live state; both read 14, then 0 once fed the same inputs.
4. **Judge only completed sessions.** Exclude the in-progress session and every non-trading day from any firing
   window, and require the window's full length of archived sessions before applying an N-session rule. If only 3 of
   5 sessions exist, the honest output is the date the rule can be judged, not a verdict.
5. **Run Gates A-F** on every row that is not `fired`, and on every newly installed or resized row.
6. **Fix, then re-run the same check.** A fix is done only when the identical check that failed now passes, the test
   suite is green and the change is committed. Never pause a strategy as a fix; repair it or replace it with a
   recalibrated copy that trades.
7. **Report** one table: counts by state, every non-`fired` row with its reason and next date, and the fixes with
   commits. Status words follow [truth-gates.md](truth-gates.md).

## 2. Gate A: research-to-live parity

**A1. You MUST measure firing parity per term before wiring a rule live.** Replay the live engine over the research
window and compute the Jaccard overlap of entry dates with the research entries. PASS: Jaccard >= 0.95 per term.
*Why:* a name is not an implementation. *Example:* a "monthly opex" term the live engine did not implement fired 0 times
against 59 research entries (Jaccard 0.00) until it was built from the live calendar code (1.00).

**A2. You MUST run parity on the calendar the rule actually saw.** If the live holiday list starts recently, every
older holiday reads as a session and parity fails for reasons unrelated to the rule. Patch history with the true
exchange calendar to test the logic, then separately verify the forward calendar against the exchange.
*Why:* a desk withdrew a correct venue anchor and nearly built a needless date-snapping port for an
"off-by-one" that was only a calendar artefact.

**A3. You MUST check live data depth against every lookback and rank window.** List each feature's window (for
example a 504-session rank, 252-session drawdown, 200-day average) and compare with the bars the live hub keeps.
PASS: depth >= longest window plus warm-up, measured on the live hub, not the replay hub. *Why:* a hub that keeps 420
bars made 504-session ranks fail closed or rank on a shorter window, silently changing the rule.

**A4. You MUST build cross-sectional ranks from the live universe.** Rebuild the components on the universe the desk
actually trades before judging a cross-sectional cell. *Why:* ranks from a 6,000-name research panel do not transfer
to a 33-name live universe.

**A5. NEVER let a cache key omit the data.** Key every feature cache on the inputs (a content hash or checksum), not
just the feature name. Test with two different data hubs. *Why:* a name-only key served test-hub features to the
live hub, a parity bug no single-hub test can see.

**A6. You MUST print component parity beside any composite.** A count or score rebuilt from N components is only as
good as each component. *Example:* a 16-component activity count reached 0.64 replay parity while its joint condition
read 0.86; print the drift with the strategy instead of hiding it in the joint number.

**A7. You MUST measure execution parity, not only signal parity.** Compare the research entry and exit price
convention with what the live engine can do (signal close vs next open, close vs next-session open). Re-score the rule
under the live convention before promoting. *Why:* a rule researched to exit at the close but executed at the next
open fell from z 2.9 to 1.47. Build the exit the research assumed, or do not promote.

## 3. Gate B: data feeds, calendars and corporate actions

**B1. Every hand-entered feed MUST carry a coverage end date, and the desk MUST fail closed past it.** Write the
renewal date into the strategy table; past it, return no signal, never a stale one. Prefer a point-in-time live feed
(first_seen < decision date) unioned with the research history. *Why:* a hand-entered auction list ran out 10 days
after install; nobody would have noticed until the rule stopped firing.

**B2. A seeded feed is seed + live refresh + fail-closed.** A failed fetch MUST NOT refresh the freshness stamp; past
a staleness limit the feed returns nothing. PASS: parity with the research series on the overlap.

**B3. You MUST check held and candidate symbols for corporate actions, not only prices.** Refuse entries whose newest
bar is older than a staleness limit (for daily equities, 10 calendar days is a workable bound) and check for mergers,
delistings and splits on every held name. *Why:* a momentum rule bought a stock acquired for cash two months earlier
because the last stale bar still ranked well; the desk carried a phantom position.

**B4. A provenance gate is met by qualifying the data, never by skipping the check.** When a pinned engine refuses
data it cannot verify, take the series from a second source and accept it only if it reconciles (every adjustment
day carries a dividend or split event; the signal close matches the primary feed). On failure fall back explicitly
(for example to price return) and say so in the manifest.

**B5. Venue rules MUST NOT be keyed on symbol shape alone.** Decide 24/7 versus session-only trading from the
instrument's venue record. If a heuristic is unavoidable, test it against every live symbol. *Why:* a crypto pair
without a separator was read as a session-only equity; its 24-hour exit was held over a weekend.

**B6. Judge a data gate on recent receipts, not the day's count.** A gate that cleared at 08:20 still dominates the
day's earlier receipts. Count a gate as active only if it appears in the last N receipts (about 30 minutes).

**B7. A panel built from today's constituents is a survivorship snapshot.** Label breadth and cross-sectional terms
built this way, keep them at the smallest size, and re-test on point-in-time membership before promoting. Level
parity does not remove the bias.

## 4. Gate C: timing windows and exits

**C1. An execution window MUST be at least two loop intervals wide.** *Why:* a 5-minute entry window under a
5-minute evaluation loop misses whenever the pass lands just outside it: about one month in three for a monthly rule.
Widen the window inside the same allowed sessions, or tighten the loop.

**C2. A scheduled flatten MUST run while the venue is open.** Check that every time-based exit falls before the
close, half-day aware, with a late-exit fallback and a backstop. *Why:* a 16:00 flatten runs after the close and
carries the position to the next open.

**C3. NEVER enter at a price the signal has not printed.** Check whether bars are start- or end-labelled before
writing any entry. Split leaked signal-bar P&L from the post-signal remainder (protocol practice 54).

**C4. Report not-due as not-due.** A rule outside its allowed sessions is `armed_not_due` with its next date and any
separate blocker. Never report "will fire at 09:36" for a rule whose next window is next month, and never call a
not-due rule broken.

**C5. You MUST replay a calendar expression forward before trusting it.** Enumerate the next 12-24 months of
qualifying dates. PASS: at least one qualifying date in the horizon the rule claims. *Why:* a rule ANDed a pre-event
entry with "the day before is in opex week"; no event through the next year satisfied both, so it could never fire.
The fix flips only the failing layer to its complement and re-tests it, keeping everything else.

## 5. Gate D: code, configuration and controls

**D1. A limit in a config file is not a limit until code reads it.** For every cap in config, find the line that
enforces it and a test that fails when it is breached. *Why:* a single-stock notional cap sat in config while
nothing enforced it.

**D2. A lookback window MUST exclude the bar being tested.** `close < min(low[-10:])` can never be true because the
bar's own low is at or below its close; compare against the prior bars (`low[-11:-1]`). Once found, search every
engine for the same pattern:

```bash
rg -n "(min|max)\((low|high|close)\[-[0-9]+:\]\)" --type py
```

**D3. Load every strategy class through the real registry in tests.** A missing default in one subclass raised
inside an unrelated strategy's stack in production. Constructing the happy case in a test does not exercise the
path that broke.

**D4. Every strategy MUST have a kill switch, and one switch can cover all of them.** A universal named-list switch
(stop new entries for these ids, let exits run) gives legacy modules a switch without editing each one. Test that
it blocks entries and leaves exits running.

**D5. NEVER leave an uncommitted engine in the live tree while other workers reload.** Generate rules only after the
red team, outside the live code path, and commit before the next reload.

**D6. After any change, run the full test suite and re-run the specific failed check.** PASS: both green, change
committed, live process restarted on the committed version and verified by version stamp.

## 6. Gate E: diagnosing a silent strategy

**E1. Treat zero fires as a bug report until a replay proves the rule is rare.** Replay the live engine over at least
60 sessions without look-ahead. PASS: replay fires match the research rate, or the rule is shown rare with its next
expected date. *Why:* a three-pass smoke called 71 routes green; a 60-session replay found 12 silently dead.

**E2. Read the strategy's own decision stamps, not its headline state.** Census the reject and block reasons
(stood-down flags, blockers, exception text, quantity-below-one, quote-age refusals) before calling it broken or
healthy.

**E3. Chase ONE candidate through the disposition log until it is admitted.** Gates are stacked, so each fix reveals
the next. Pick one historical signal, replay it, fix the first refusal, replay again, and repeat until the candidate
is admitted. *Example:* one short signal failed, in order, on quote availability, borrow, replay clock alignment, and
displayed size before it was admitted; then a continuous replay exposed a stale session reference. Clean the harness
too: a replay that reuses an old journal skips candidates already disposed.

**E4. Fix a hosted rule in a private copy that changes only bounds, doors or calendars, never the rules.** Keep the
shared module pinned so the original stays the control. When a provenance gate in a pinned engine blocks it, call the
engine's own pure decision function on a qualified second feed instead of editing the engine.

**E5. A merged clone is hosted, not silent.** A clone whose parent trades the combined size emits nothing by design.
Classify it `merged` with its host, or it will be flagged dead forever.

**E6. Watch for namespace shadowing and order-dependent loads.** A vendored package with a generic top-level name hid
a local module only after another adapter loaded first, so the failure appeared only in the live process order. Load
by file path under a private name.

## 7. Gate F: sizing and arming at real size

Use this gate when the operator's policy is that installed edges trade at real computed size rather than as
minimum-lot shadows (see [edge-discovery-protocol.md section 12](edge-discovery-protocol.md#12-amendment-real-size-with-a-floor-instead-of-a-shadow-stage)).

**F1. Size for risk, not for estimated edge.** `N_full = min(vol_target_pct * book / sigma_trade, max_book_pct * book, adv_pct * ADV20)`.
Fractional Kelly is only a cap, applied where the research estimated it positive. A non-positive Kelly estimate
MUST NOT zero a strategy; that is a shadow stage by another name ([C11](field-casebook.md#c11-kelly-sizing-on-an-edge-found-in-the-same-history)).

**F2. Set a floor, not a shadow.** Every armed edge trades at no less than a floor fraction of N_full (one desk used
12.5%). A step-down below the floor means recalibrate the rule, not park it.

**F3. Control risk at the book level.** Cap deployed 1-sigma risk per economic family, cap book gross, and apply one
proportional scale ex ante (so the p95 concurrent day fits), a per-pass proportional factor and a hard clip at entry.
Log every clip.

**F4. You MUST report concurrency with every real-size book.** Replay entry masks and print maximum and p95
concurrent gross. *Why:* calendar strategies pile up on the same anchors; one book's calendar sleeves alone reached
roughly twice its gross cap on a month-end-plus-holiday cluster.

**F5. Count exposure and merge clones.** Strategies whose entry masks overlap heavily within one economic family
(Jaccard >= 0.4 is a workable line) trade as one unit through a parent at combined size ([C19](field-casebook.md#c19-crowding-many-sleeves-one-bet)). Never fold a diversified ETF bet into a single-stock position.

**F6. A red-team verdict becomes a sizing haircut, not a stage.** Demoted means a smaller multiple of the floor;
kill-exact-row means not installed.

**F7. The first 20 fires per unit are the evidence.** Size from backtest sigma is a paper-book size; print the
falsifier (for example, mean net over the first 20 fires not positive means recalibrate) beside the size.

## 8. Audit row template and pass rule

Write one row per strategy, one JSON object per line:

```json
{
  "strategy_id": "",
  "state": "fired | armed_not_due | waiting_data | merged | blocked | not_loaded | broken",
  "last_fire": "YYYY-MM-DD or none",
  "next_due": "YYYY-MM-DD or unknown",
  "host": "parent id when merged",
  "blocker": "named reason when blocked or waiting",
  "route": "the fix or alternative route being built",
  "parity": {"signal_jaccard": 0.0, "execution_convention_matched": true, "data_depth_ok": true},
  "data": {"feed_valid_to": "YYYY-MM-DD", "stale_guard": true, "corporate_actions_checked": true},
  "timing": {"window_ge_2_loops": true, "exit_before_close": true, "forward_dates_exist": true},
  "controls": {"kill_switch": true, "caps_enforced_in_code": true, "loaded_via_registry_test": true},
  "size": {"n_full": 0, "floor_fraction": 0.125, "family_risk_ok": true},
  "evidence": ["replay or log path"],
  "commit": ""
}
```

**Pass rule:** the audit is GREEN only when every row is `fired`, `armed_not_due`, `waiting_data` or `merged`, each
with a date or host, and every `blocked` row has a named blocker and a route already trading in its place. Any
`broken` or `not_loaded` row, any unexplained zero, or any check run on a different input than the live process
makes the audit PARTIAL.

## 9. Anti-patterns this file exists to stop

| Anti-pattern | What it costs | Gate |
|---|---|---|
| "No signal" accepted as healthy | Edges that never trade; C20 says they are worth zero | E1, E2 |
| Status read from a list, catalogue or config | Missing and phantom strategies, unenforced caps | 1.1, D1 |
| Pausing a strategy as a "fix" | The edge is switched off and the bug stays | 1.6 |
| Trusting a rule's name over its fires | 0 fires against 59 research entries | A1 |
| Parity tested on the replay hub only | Live features silently on a shorter window | A3 |
| Hand-entered lists with no end date | Rule stops firing when the list runs out | B1 |
| Prices without corporate actions | Phantom positions in delisted names | B3 |
| Window narrower than the loop | One missed month in three | C1 |
| Lookback that includes the tested bar | A breakout that can never trigger | D2 |
| Reporting a verdict before the window exists | False "dead" calls and wasted recalibrations | 1.4 |

## Source and maintenance

Distilled from one desk's edge-discovery playbook (practices 55-92 and their honesty notes, 15-16 November 2026),
its promotion ledgers and two desk audits. Only aggregate facts appear; no vendor data, accounts, machine paths or
personal identifiers. New lessons append to the source playbook first; revise this file when a gate changes and
record the revision in PROVENANCE.md.
