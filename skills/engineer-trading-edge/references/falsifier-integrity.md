# Falsifier integrity: audit the grading machine before the window runs

This reference is the audit a forward falsifier must pass before its first session accrues. It distils the fifth
wave of the 2026-11-14/15 alpha hunt, which took the estate's flagship forward falsifier, a 60-session overnight
accrual registered the day before, and audited the accrual itself: code read end to end, a dry run in scratch,
one full row reproduced by an independent hand computation, and the scheduling read back twice from the
definition. The falsifier survived; two of the claims inherited around it did not, and both corrections were
printed in the wave report where they belonged, not smoothed.

Read this file whenever a falsifier, shadow accrual or grading script is registered, whenever an accrual's first
verdict is about to be believed, and whenever a number printed by a grading machine is quoted in a decision. A
falsifier is a measuring instrument; an unaudited instrument's verdict is a rumor with a date on it.

## The governing claim

**The registered leg must be faithful, and everything around it must be labeled as what it is.** Most falsifier
failures are not statistical; they are clerical: a cost leg computed as the mean where the report cites the
median, a proxy quietly standing in for the print it names, a missing session silently stretching a one-night
leg into a three-day leg inside an overnight mean. Each one is small, clerical and fully capable of reversing a
verdict at session 60, when it is too late to rerun the window. The audit is cheap on day one and impossible on
day sixty.

## Procedure

1. **Read the accrual code end to end.** Not the docstring: the code. List what each leg actually computes,
   in order, with the exact statistic (mean or median, of what, over which population).
2. **Dry-run in scratch.** Run the instrument against already-known sessions and confirm it appends the expected
   rows in the expected shape, and that a second pass appends nothing (idempotency by date or key).
3. **Reproduce one row by an independent path.** Hand-compute one full session from the raw inputs with separate
   code and require exact agreement. In the founding audit, an independent computation over all 29 legs of the
   dry-run session reproduced the accrual's gross figure exactly (-61.921bp); that equality, not the code read,
   is what licensed trust.
4. **Check the registered definition leg by leg.** The verdict rule (which leg, net of what, over how many
   sessions, demotion line where, the zero case assigned to which side) must match the registration text exactly.
   Then prove the costing defects you find do NOT touch the registered leg, or the registration is void until
   amended.
5. **Verify the schedule from the definition, twice.** Read the job's own definition file and the scheduler's
   view; confirm enabled state, cadence, timezone and next run. An accrual that never fires is a falsifier that
   reads zero forever and calls it patience.
6. **Print every defect where it belongs.** Defects are named, numbered and carried to a named cure wave. Cures
   land as dated amendments to the instrument, never as silent edits: the record of what the early sessions were
   graded by is part of the evidence.

## The defect classes (check each one, by name)

- **D1, Mislabeled statistic.** A leg cites one statistic and computes another. Founding case: the crossing-cost
  leg computed the MEAN of per-name median costs (+46.08bp) while the report and docstring cited the MEDIAN of
  those medians (+41.25bp); the stress leg was 4.8bp harsher than labeled. The registered leg did not touch it,
  so the falsifier stood and the label was corrected.
- **D2, Proxy standing in for a print.** A series named as one thing is another. Founding case: the design
  premise held that the daily bar's open and close ARE the auction prints. Measured against official prints over
  60 name-sessions: bar close matched the closing auction print 60 of 60 exactly; bar open matched the opening
  auction print only 4 of 60, pooled gap +5.44bp, systematic in one name at +28.77bp mean. The bar-based
  definition stood (it is the same series the historical exam graded, and consistency with the exam is a real
  argument), but the print-based truth was measured and printed beside it: the carry basket's true-print auction
  cost a median +5.85bp per session against the bar-based -0.63bp, which moved the registered 5bp from
  conservative to about right.
- **D3, No consecutive-session check.** A missing bar silently turns a name's next leg into a multi-day leg
  inside a single-period mean.
- **D4, Silent session skips.** Sessions below a minimum name count skipped with no gap marker in the ledger:
  the accrual's denominator quietly differs from the calendar's.
- **D5, Counts without names.** Records carry how many names formed a leg, not which; a composition change is
  invisible after the fact.
- **D6, No stop at the registered n.** The verdict recomputes over any sessions past the registered count, so
  the checkpoint that was supposed to decide becomes a moving average of indecision.
- **D7, Crash-loses-the-session.** A missing key or feed gap throws, the run reports failure, and the session is
  simply absent from the ledger: a fail-open instrument converting its own errors into missing evidence.

## Checks

- If the independent reproduction disagrees with the accrual by any amount, the accrual does not run until the
  difference is explained to the last basis point. "Close" is a verdict about a trade, not about arithmetic.
- Every defect found gets one of three dispositions, printed: cured now (as a dated amendment), carried to a
  named wave with a date, or accepted with the reason stated. A defect that is only mentioned is not dispositioned.
- The audit's own typed-seat or reviewer read, if one is taken, is advisory and labeled with its confidence; it
  never substitutes for the hand computation.

## Evidence

The founding audit's net effect was the opposite of destructive: the registered falsifier leg was proven faithful
(sessions built strictly after the anchor date, legs from previous close to open per name, the verdict rule
exactly as registered, the ledger idempotent), the schedule was proven live for the Monday open, and the two
corrected claims made the eventual verdict MORE believable, not less: when session 60 prints, the estate will
know the number was produced by the instrument it registered, graded on the definition it chose, with its known
defects priced and printed. That is the entire value of a forward window, and it is bought here, in advance, for
the price of one careful read.
