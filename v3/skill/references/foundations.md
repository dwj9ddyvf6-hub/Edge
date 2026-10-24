# Foundations: where an edge comes from, and what it means

## Contents

1. Interpret the two-part insight
2. Separate expected profit, alpha, and utility
3. Identify the marginal counterparty
4. Understand risk compensation
5. Read prices and contract semantics correctly
6. Update beliefs without counting evidence twice
7. Connect information to attainable decisions
8. Derive the information–growth identity
9. Allocate under uncertainty and survival constraints
10. Recognize strict arbitrage
11. Transfer ideas across disciplines
12. Distinguish a persuasive mechanism from evidence

Source identifiers refer to the accompanying source register. Mathematical examples below are hypothetical, with calculations checked independently. Equations labeled **derivation** are analytical translations developed for this skill, rather than quotations or claims of empirical profitability.

## 1. Interpret the two-part insight

Johann Markov's post groups edge into information arbitrage and risk warehousing. The useful insight is to look behind a profitable pattern and ask what scarce contribution earns the return: improving a decision before competitors do, or supplying exposure, immediacy, patience, or capital that others value.

Grossman–Stiglitz explains why costly information need not be completely revealed by equilibrium prices: complete revelation would undermine its production incentive. That leaves room for information rents, but those rents may merely cover acquisition costs [I01]. Risk warehousing has another economic justification: counterparties can rationally pay to reduce an exposure even when everyone agrees about its distribution [R1, R5].

The categories overlap. A liquidity supplier can forecast order flow, bear inventory risk, and earn a service payment simultaneously. Access, market design, mandates, financing, subsidies, execution, and portfolio complementarity also matter [I12, R7, B09, B10]. Some are causes of gross return; others determine whether a particular trader captures it. The post is therefore a powerful organizing lens, not an exhaustive theorem. “Variance” also needs refinement: volatility alone does not establish compensation.

## 2. Separate expected profit, alpha, and utility

Define three distinct claims before evaluating a strategy:

- **Positive expected net profit:** the conditional mean of the complete cash payoff, after relevant costs, is positive. Compare funded investments with their financing and opportunity costs.
- **Alpha:** performance exceeds a specified feasible benchmark or modeled risk exposures. Alpha depends on that benchmark; it does not establish immunity to omitted risks.
- **Incremental utility:** adding the trade improves the owner's objective given existing assets, liabilities, funding, and constraints. This can differ from standalone expected return.

A hedge can have negative expected excess return and improve portfolio utility. A leveraged market exposure can earn positive expected return without forecasting alpha. Better execution can preserve an existing gross edge without creating new information [R1, R10].

**Hypothetical example:** a payoff earns 1 with probability 0.99 and loses 150 otherwise. Its mean is −0.51. Neither the 99% win rate nor a sequence of small profits establishes favorable risk compensation. Conversely, positive expectation does not guarantee attractive utility when losses coincide with the owner's most vulnerable states.

## 3. Identify the marginal counterparty

The relevant competitor is whoever determines the executable price at the intended size and time, not an average participant. Identify the objective behind the opposing order: a hedge, liquidity need, mandate, inventory adjustment, different evidence, or superior knowledge. An apparent seller of cheap risk may be the better-informed party [B06].

Milgrom–Stokey's no-trade result makes this question rigorous under its assumptions: private information does not automatically create mutually acceptable speculation starting from an efficient allocation with appropriate belief and common-knowledge conditions [I04]. Real opportunities require explaining which conditions differ. Aumann similarly makes persistent disagreement a question about evidence, priors, models, and common knowledge—not proof that our estimate is superior [I05].

Execution itself selects information. **Derivation:** for a single-fill order with quantity n,

\[
EV(a)=P(F\mid\mathcal I,a)\,E[n(V_h-P_{fill})-C\mid\mathcal I,a,F]-C_{attempt}.
\]

Here F denotes a fill; C includes applicable exit and holding costs. Expand partial-fill outcomes when necessary. Do not multiply by fill probability again if an empirical payoff series already includes zero-payoff unfilled attempts. Resting orders can receive inventory precisely when their valuation becomes unfavorable: evaluate conditional markouts and cancellation delays [I03].

## 4. Understand risk compensation

Asset pricing expresses a payoff's value as

\[
P=E[mX],\qquad E[R]-R_f=-\frac{\operatorname{Cov}(m,R)}{E[m]},\quad R_f=1/E[m].
\]

Here m is a stochastic discount factor, X a terminal payoff, and R a gross return [R1]. Payoffs delivered when marginal capital is valuable can command high prices and low expected returns. Losses in those states may require compensation. Independent variance alone does not imply a premium.

The unwanted burden may be a crash, unhedgeable jump, uncertain convergence time, margin call, borrow recall, or illiquidity. Option demand can affect prices through residual hedging risks [R5]. Funding losses and widening spreads can reinforce one another [R3]. A terminally correct convergence thesis can fail through interim liquidation [R2].

**Operational deduction:** define liquid equity W, required collateral M, and reserve B along each stress path; require W−M−B to satisfy the desk's funding constraint. Do not substitute initial margin or a historical stop distance for this calculation. Examine simultaneous spread widening, losses, haircut changes, and inaccessible collateral. Distinct strategies can warehouse the same crisis exposure despite low ordinary correlations [R4].

## 5. Read prices and contract semantics correctly

A price is a payoff valuation, not automatically a physical probability. For a digital contract paying one unit if A occurs,

\[
P_A=E[m\mathbf1_A]=P(A)E[m\mid A].
\]

With a positive discount factor and bond price B=E[m], P_A/B defines the corresponding risk-neutral probability; it need not equal P(A). Prediction-market probability interpretations also depend on preferences, wealth, beliefs, hedging motives, and restrictions [B04]. Treat prices as an informative benchmark, not an oracle.

For two outcomes offered at decimal odds 1.91, raw reciprocal odds sum to 1.04712. Proportional normalization gives 0.50/0.50, but that assumption does not recover objective probabilities. Different margins and customer demand can distort the mapping [B05, B06].

The traded event must match its contractual definition: measurement source, cutoff, inclusivity, revisions, voids, and settlement delay [B12]. A correct forecast of the headline can be a wrong forecast of the payout.

**Hypothetical example:** a one-dollar binary payoff priced at 0.52 with all-in cost 0.015 and physical probability 0.56 has expected net profit 0.025. If the filled subset instead has probability 0.50, its expectation is −0.035. Price advantage must survive both contract interpretation and execution selection.

## 6. Update beliefs without counting evidence twice

**Derivation:** posterior odds obey

\[
O(H\mid\mathcal I,E_{1:k})=O(H\mid\mathcal I)
\prod_{j=1}^{k}\frac{P(E_j\mid H,\mathcal I,E_{<j})}{P(E_j\mid\neg H,\mathcal I,E_{<j})}.
\]

The conditional terms matter. With prior probability 0.50, one observation carrying likelihood ratio 2 moves the posterior to 2/3. Three copies of that observation still supply one underlying observation. Treating them as independent would falsely produce 8/9. Source lineage, first-publication times, revisions, and shared inputs belong in the evidence model.

Tetlock's research connects stale news to subsequent reversal in its studied sample [I11]. That motivates novelty tracking; it does not imply that repeated information is always irrelevant. Changed context can change an old fact's significance.

Likewise, multiple indicators calculated from one price history and multiple LLMs using one article are not independent experiments. A transformation may improve a bounded model's representation without adding external information [I06]. Estimate likelihoods and calibration from defensible data or models; fluent confidence is not a likelihood ratio. Update on prices too when they reveal additional information, while avoiding circular use of the same signal.

## 7. Connect information to attainable decisions

More accurate prediction can be economically useless when the action stays unchanged, prices already incorporate it, or delivery is late. **Derivation:** the expected sample-information value for experiment Z is

\[
EVSI=E_Z[\max_a E[U(a,\theta)\mid\mathcal I,Z]]-
\max_aE[U(a,\theta)\mid\mathcal I]-c_Z.
\]

Include abstention among feasible actions. This formula assumes the stated posterior and decision model; empirical implementations must estimate attainable value rather than assume an oracle. Blackwell's comparison of experiments provides the decision-theoretic foundation [I06]. Sims supplies a framework for scarce attention [I07].

**Hypothetical example:** choose between buying one binary contract for 0.55 or passing. Prior success probability is 0.50. An experiment produces posterior 0.80 or 0.20 with equal probability while the quote remains available. Buying only after the favorable result yields expected profit 0.5×0.25=0.125; a 0.03 experiment cost leaves 0.095. If the price updates before execution, this value changes or disappears.

Public economic links and competing demands on attention motivate research into delayed interpretation [I09, I10]. Speed must be measured against executable opportunity lifetime: end-to-end latency and order size define a capture surface, not a universal “faster is better” rule [I02, I12].

## 8. Derive the information–growth identity

Assume mutually exclusive exhaustive states, complete frictionless state bets, normalized strictly positive prices q_i summing to one, true probabilities p_i, and a fully invested nonnegative allocation b_i summing to one. Require b_i>0 wherever p_i>0. A unit invested with allocation b pays b_i/q_i in state i. **Derivation:**

\[
E_p[\log(W_1/W_0)]=\sum_i p_i\log(b_i/q_i)
=D_{KL}(p\|q)-D_{KL}(p\|b).
\]

Information relative to market odds creates potential log-growth value; allocation error consumes it. This sharpens Kelly's information connection [B01]. It is a special-model identity, not a universal alpha equation. Incomplete contracts, costs, credit, leverage, and changing prices alter the feasible calculation. Repetition requires suitable assumptions before interpreting the expectation as a long-run growth rate.

**Hypothetical example:** p=(0.60,0.40), q=(0.50,0.50), b=(0.80,0.20). Market divergence is 0.020136 nats; allocation error is 0.104650; expected log growth is −0.084514. Using b=p instead gives +0.020136 in this ideal model. Knowing the more likely outcome is insufficient when confidence and stakes are wrong.

Proper scoring rules evaluate forecast distributions [B03]. Keep forecast score and economic results separate: improvements outside the traded subset need not improve realized utility.

## 9. Allocate under uncertainty and survival constraints

For a binary bet with net win odds d−1, probability p, and wealth fraction f,

\[
G(f,p)=p\log(1+(d-1)f)+(1-p)\log(1-f),
\qquad f^*=\frac{pd-1}{d-1}.
\]

For long-only betting, constrain the solution to the feasible set, including zero. At p=0.56 and d=1.91, expected profit per dollar staked is 0.0696 and ideal f*=0.07648. These are hypothetical known-model results, not recommended stakes [B01, B02].

Parameter uncertainty alone does not algebraically imply half-Kelly. Because G is linear in p, averaging this one-period objective over a posterior uses its mean: E_p[G(f,p)]=G(f,E[p]). Shrinkage can change that mean. Drawdown preferences, model ambiguity, correlation, and funding constraints introduce additional reasons to change allocation [V9].

For a long-only ambiguity interval p∈[0.52,0.60], the worst-case probability is 0.52; at odds 1.91 it implies no favorable bet. This robustness protects only against the specified uncertainty set [B08]. Risk-constrained Kelly supplies modeled drawdown restrictions, whose assumptions and initial-wealth floor must not be confused with universal protection or a rolling maximum-drawdown guarantee [B07]. Optimize joint wealth, not isolated per-trade fractions.

## 10. Recognize strict arbitrage

In a specified frictional model, strict arbitrage requires a feasible self-financing position with nonpositive initial cost, no adverse future payoff across the relevant states, and a strictly positive benefit somewhere with positive probability. Every contingent cash requirement must be financeable. A positive mean, likely convergence, or attractive relative valuation does not meet that definition.

**Hypothetical example:** exactly complementary outcomes have executable decimal odds 2.10 and 2.05. Their reciprocal sum is 0.963995. Allocating 493.9759 and 506.0241 from a 1,000 stake equalizes the payout at 1,037.3494, a 3.73494% ideal return before costs. This conclusion fails if legs cannot be executed together, quantities differ, outcomes overlap, void rules differ, or a venue does not pay.

Real research must establish payoff identity, simultaneous executable capacity, settlement and counterparty assumptions, fees, and financing. Market structure can create mechanical opportunities while intense competition makes them inaccessible to a particular desk [I12]. A scarce-access rent and a universally available arbitrage are different claims.

## 11. Transfer ideas across disciplines

| Discipline | Useful transfer | Boundary |
|---|---|---|
| Gambling | Separate favorable odds from bankroll allocation [B02]. | House take and limits can consume apparent advantage. |
| Prediction markets | Model exact event semantics and benchmark probabilities [B04, B12]. | Price aggregates incentives as well as beliefs. |
| Poker/game theory | Distinguish robust play from opponent exploitation [B11]. | Market rules, competitors, and external utility evolve. |
| Insurance | Identify the liability someone pays to transfer [R5]. | Rare losses and dependence determine capital needs. |
| Psychology | Translate bias into observable demand and price effects [V6, V7]. | Individual bias alone does not establish market alpha. |
| Statistical learning | Evaluate prospective forecasts and search-adjusted evidence [V1, V8]. | Predictive fit does not establish capture or causality. |

These connections suggest a productive research question: where can this desk supply information, inventory, patience, or implementation at lower all-in cost than the marginal alternative? They do not authorize assuming that it already can.

## 12. Distinguish a persuasive mechanism from evidence

An economic mechanism guides falsification, transfer, and failure diagnosis. It cannot replace measurement. Research comparing theoretical and mechanically generated predictors cautions against using an appealing explanation as a certificate of durability [V12]. Conversely, a reproducible unexplained signal can remain a candidate with greater uncertainty.

Maintain separate judgments about mechanism, forecast quality, executable capture, and portfolio suitability. Register all explored variants; preserve chronology and dependence; compare feasible benchmarks; and log decisions before outcomes [V1, V2, V8]. DSR and PBO diagnose particular selection problems, not the probability of future profitability [V3, V4].

Competition and capital can change the opportunity after discovery [V5, V11]. The skill's achievement is therefore to produce a falsifiable candidate and an honest evidence status. Its strongest output may be a precisely identified bottleneck—or a demonstrated absence of edge at the available price.
