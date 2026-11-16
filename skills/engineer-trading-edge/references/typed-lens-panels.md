# Typed lens panels: use a model panel as a lens, never as a judge

This reference governs the creative use of a typed model layer (a Decisions-style API that returns probability
vectors, not prose) inside a research program. It distils the panel work of the 15 November 2026 potential-edge
census, where one governed request of 104 questions (22,974 input tokens) read a twelve-candidate board through
seven professional lenses and a set of adversarial seats, and the estate's separate lens study, which measured
what happens when narrative ratings are allowed to score cells directly: over 24.4 million condition-combination
cells the mechanism-weighted ranking scored AUC 0.490 against 0.529 for the in-sample t alone, below its own
shuffle null. The panel is a powerful lens and a proven failure as a judge; this file keeps it in the first role.

Read this file when a candidate set needs its mechanisms read from several professional viewpoints at once, when
a corpus needs connection hunting across objects nobody has related, when a find needs its null priced by an
adversary, and whenever anyone proposes letting model ratings rank, gate, veto or size anything.

## The seven lenses

Ask the same question of seven typed seats, each a working professional's viewpoint: **hedge fund manager**,
**professional swing trader**, **game theorist**, **professional gambler**, **prediction-markets analyst**,
**data analyst**, **quant**. Each seat returns a probability that the mechanism under review is a plausible,
repeatable edge. The seats are lenses on the same object, not votes: seven correlated readings of one question
are one observation wearing seven hats, and the file treats them that way.

## The five uses

1. **Seven-lens panels.** Rate mechanism plausibility per candidate. Record every seat's number, the mean and
   the SPREAD. The spread is the information: a wide spread names the exact disagreement the next test must
   resolve; a narrow one names a shared assumption worth attacking.
2. **Connection hunting.** Put pairs and triples of objects from different programs in front of the panel and ask
   what would make them one mechanism. Gestalt combinations are candidates in their own right, not only audit
   subjects; a connection the panel surfaces enters the normal pipeline as a generated hypothesis with no
   privilege.
3. **Adversarial nulls.** For each serious candidate, state the strongest null in one sentence ("generic global
   overnight premium plus beta; no basket or auction component") and have a seat price the probability that the
   null is essentially correct. A candidate whose null prices high is not killed; it is told exactly what its
   forward test must separate it from.
4. **Extraction.** Use the layer to pull structured facts (counts, dates, denominators, named conditions) out of
   prose corpora at scale, with the extraction checked against the source on a sample. Extraction output is data
   with an error rate, never a citation.
5. **Counterfactual reads.** Ask what the board would look like if a named condition were reversed (costs doubled,
   the window halved, the strongest name removed). Counterfactuals design stress tests; they are not evidence.

## Governance: the hard rules

- **Seats rate plausibility only, never the ranking.** In the census rubric
  ([potential-edge-census.md](potential-edge-census.md)) the arithmetic takes numbers printed in the object's
  own source file; seat output enters none of it.
- **Disagreement is preserved, never averaged away before scoring.** Print the per-seat vector. The census board's
  most useful single datum was a disagreement: on the entry-location gate the swing trader (0.70) and the hedge
  fund manager (0.67) priced tape feel the quant refused at 0.23, a spread of 0.47, the widest on the board.
- **A seat graduates only on measured excess.** A lens or panel that wants authority beyond a disagreement flag
  must earn it the way any signal does: a sealed forward sample on which its ratings beat the base rate and the
  mechanical rubric. Until then it never gates, vetoes or sizes.
- **Narrative priors are generators and tie-breakers, never per-cell weights.** The lens study's failure (AUC
  0.490, below shuffle) traced to two causes: raters find stories for buying easier to believe than stories for
  selling (long-story bias), and a narrative rating carries no per-cell information within a side. Rank any
  narrative prior within side and instrument before it touches anything, and use it to order whole families of
  similar statistical strength, never to reweight cells. See the amendment in
  [edge-discovery-protocol.md](edge-discovery-protocol.md), section 11.
- **One governed request, recorded.** Panel work runs as a named, versioned request bank with its spend printed.
  Unrecorded panel reads are folklore.

## Procedure

1. Fix the candidate set and the exact question per use (plausibility, connection, null, extraction,
   counterfactual). Write the nulls before seeing any ratings.
2. Run one governed request; save the full vectors, the bank version and the spend beside the work.
3. Print per-seat numbers, means and spreads in the deliverable, with the two or three disagreements that matter
   interpreted in prose: what is each side pricing that the other refuses?
4. Convert outputs to work, not verdicts: each wide spread becomes a named test; each high null becomes the
   falsifier's separation target; each connection becomes a generated hypothesis in the normal queue.
5. Log the panel's own forward record from day one, so its graduation can one day be measured instead of argued.

## Evidence

On the census board the panel earned its keep three times in one run. It found the board's widest disagreement
(the entry-location gate, spread 0.47) and thereby named the next experiment. It produced the board's most
honest tension: the variance-selling candidate the seven lenses rated nearly unanimously (mean 0.591, spread
0.05, the highest mean on the board) carried an adversarial null of 0.64, the panel simultaneously believing the
mechanism and disbelieving the implementation, which is precisely the joint design the estate then ran. And on
the sealed-slice candidate six lenses sat at 0.50 to 0.51, a printed coin flip, with only the quant dissenting
down at 0.34: the panel correctly reporting that the sealed data, not opinion, would decide that one in four
days. A lens that can say "this is not ours to call" is worth its cost; a judge that cannot is worth nothing.
