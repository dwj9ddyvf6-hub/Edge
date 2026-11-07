# Information advantage, game theory, and implementable edge

Research memo for the parent synthesis. Accessed October 23, 2026, America/New_York. This memo distinguishes published results from proposed trading research. No empirical strategy test was run here. Source abstracts and available primary PDFs were inspected; several scanned PDFs had no extractable web text, and inaccessible full papers are not represented as fully parsed.

## Central reading of the post

The strongest interpretation of “information arbitrage” is a repeatable advantage in the mapping from available evidence to an **executable, correctly priced payoff**. It need not involve secret information: attention, interpretation, linkage, implementation speed, and permitted access can differ. But disagreement with a quote is not itself an edge, and an informational advantage usually produces risky expected profit rather than literal arbitrage.

The relevant comparison is with the information and constraints of the participants setting the marginal executable price at the relevant size and horizon. It is not with an average social-media trader. One must model why a knowledgeable counterparty still accepts the trade: liquidity need, hedging, inventory, mandate, slow processing, inferior evidence, different beliefs, or superior information that makes our apparent opportunity a trap.

## Twelve primary-source foundations

### I01. Costly information prevents complete revelation

Sanford J. Grossman and Joseph E. Stiglitz (1980), **On the Impossibility of Informationally Efficient Markets**, American Economic Review 70(3), 393–408.

- Author institution: https://academiccommons.columbia.edu/doi/10.7916/D8765R99
- Paper mirror: https://terpconnect.umd.edu/~wermers/ftpsite/FAME/grossman_stiglitz_(1980).pdf
- Web refs: `turn61search0`, `turn30view0`.
- Result: If information is costly, fully revealing prices undermine the incentive to acquire it. Their equilibrium balances information acquisition and residual price informativeness.
- Limit: This is an equilibrium model, not evidence that a particular signal earns excess returns. The benefit can merely repay research and implementation costs.
- Skill implication: Require a **costed information-production advantage** and an explanation of why competitors do not eliminate it. Debit subscriptions, collection, computation, research amortization, and operational failure as well as commissions.

### I02. The price already learns from orders

Albert S. Kyle (1985), **Continuous Auctions and Insider Trading**, Econometrica 53(6), 1315–1335.

- Publisher: https://www.econometricsociety.org/publications/econometrica/browse/1985/11/01/continuous-auctions-and-insider-trading
- Paper mirror: https://people.stern.nyu.edu/lpederse/courses/LAP/papers/Information%2CFundamental/Kyle85.pdf
- Web refs: `turn43search3`, `turn43search49`. Publisher abstract indexed; PDF open failed after redirect.
- Result: A strategic informed trader, noise demand, and competitive market makers interact; prices reveal information through aggregate order flow. Information is monetized subject to endogenous price impact.
- Limit: Stylized assumptions do not describe every modern order book; “insider” is a theoretical information type, not an instruction to acquire unlawful information.
- Skill implication: Price impact and alpha decay are part of signal economics. Scaling the order changes the opportunity; paper midpoint returns are insufficient.

### I03. A fill is information

Lawrence R. Glosten and Paul R. Milgrom (1985), **Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders**, Journal of Financial Economics 14(1), 71–100.

- Author institution: https://business.columbia.edu/faculty/research/bid-ask-and-transaction-prices-specialist-market-heterogeneously-informed-traders
- DOI: https://doi.org/10.1016/0304-405X(85)90044-3
- Web ref: `turn30view3`.
- Result: Superior information produces a positive spread even with a risk-neutral, zero-expected-profit specialist. Observed returns and realizable returns differ because uninformed participants face adverse selection.
- Limit: Spread capture is not pure profit, and informed-flow measures are estimates rather than observable trader identities.
- Skill implication: For a resting buy, estimate value **conditional on being filled**. Track post-fill markouts, quote age, cancellation latency, and partial fills. Do not add a second adverse-selection deduction if it is already inside the conditional payoff model.

### I04. Explain why trade is possible

Paul Milgrom and Nancy Stokey (1982), **Information, Trade and Common Knowledge**, Journal of Economic Theory 26(1), 17–27.

- Author PDF: https://web.stanford.edu/~milgrom/publishedarticles/Information%20Trade%20and%20Common%20Knowledge.pdf
- DOI: https://doi.org/10.1016/0022-0531(82)90046-1
- Web refs: `turn30view2`, `turn61search2`.
- Result: Under an initially Pareto-efficient allocation, appropriate common/concordant belief conditions, and common knowledge of willingness to trade, private information alone does not generate mutually acceptable speculative trade.
- Limit: This does not say real markets cannot trade or all profits require irrationality. Liquidity needs, incomplete markets, constraints, heterogeneous priors, and failures of common knowledge matter.
- Skill implication: Name the assumption that is broken in the proposed opportunity. If the only explanation is “our model is smarter,” the mechanism is unfinished.

### I05. Disagreement is a diagnostic, not proof

Robert J. Aumann (1976), **Agreeing to Disagree**, Annals of Statistics 4(6), 1236–1239.

- Author institution: https://cris.huji.ac.il/en/publications/agreeing-to-disagree/
- PDF mirror: https://www.haverford.edu/sites/default/files/Aumann1976.pdf
- DOI: https://doi.org/10.1214/aos/1176343654
- Web refs: `turn59view1`, `turn54search48`, `turn30search3`.
- Result: Bayesian agents with a common prior cannot have different posteriors for an event when those posteriors are common knowledge.
- Limit: Actual prices are not transparent posterior probabilities; wealth, risk preferences, mandates, and market structure affect them. The theorem does not tell us who is correct when assumptions fail.
- Skill implication: Audit disagreements by differing evidence, priors, likelihood models, payoff definitions, and constraints. Several LLMs agreeing after sharing the same source are not independent confirmations.

### I06. Information has value through decisions

David Blackwell (1953), **Equivalent Comparisons of Experiments**, Annals of Mathematical Statistics 24(2), 265–272.

- Publisher: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full
- DOI: https://doi.org/10.1214/aoms/1177729032
- Web refs: `turn30search1`, `turn43search14`; publisher page returned iframe. The economic/statistical equivalence is also explicitly stated in Jacques Crémer's original proof: https://www.sciencedirect.com/science/article/pii/0022053182900400 (`turn54search31`).
- Result: The comparison of information structures by garbling is equivalent to comparison by attainable expected payoff across decision problems, under the theorem's conditions.
- Limit: This is a partial ordering. More data is not necessarily more useful for one trading task, and information can be costly.
- Skill implication: Measure incremental decision value. A deterministic transformation of the same observations cannot manufacture new external evidence; it can still improve a bounded model's representation and decisions.

### I07. Attention is a scarce resource

Christopher A. Sims (2003), **Implications of Rational Inattention**, Journal of Monetary Economics 50(3), 665–690.

- Author institution: https://collaborate.princeton.edu/en/publications/implications-of-rational-inattention/
- DOI: https://doi.org/10.1016/S0304-3932(03)00029-1
- Web ref: `turn38view2`.
- Result: A finite Shannon-capacity constraint between observations and actions can generate behavior resembling signal-extraction frictions or adjustment costs.
- Limit: A general decision/control model is not direct proof of an exploitable equity anomaly. The capacity/cost specification must fit the application.
- Skill implication: Prioritize evidence by expected effect on the action. The opportunity may be neglected because the potential dollar profit is too small for a large firm; this can favor a small specialist without implying universal inefficiency.

### I08. Winning can reveal that your estimate was too optimistic

Paul R. Milgrom and Robert J. Weber (1982), **A Theory of Auctions and Competitive Bidding**, Econometrica 50(5), 1089–1122.

- Author-hosted/coauthor-hosted PDF: https://cramton.umd.edu/market-design-papers/milgrom-weber-a-theory-of-auctions-and-competitive-bidding.pdf
- University PDF: https://www.cs.princeton.edu/courses/archive/spr10/cos444/papers/milgrom_weber82.pdf
- DOI: https://doi.org/10.2307/1911865
- Web refs: `turn38view3`, `turn61search27`.
- Result: Interdependent values and affiliated information make rivals' behavior informative; auction format and information disclosure alter bidding. Conditional valuation handles the winner's-curse problem.
- Limit: Auction findings require the specified value and signal structure; not every order is a common-value auction.
- Skill implication: Ask what selecting the apparent best opportunity, obtaining the fill, or winning allocation reveals. Re-estimate on the selected subset rather than relying on unconditional prediction quality.

### I09. Public links can be underprocessed

Lauren Cohen and Andrea Frazzini (2008), **Economic Links and Predictable Returns**, Journal of Finance 63(4), 1977–2011.

- Author institution record: https://www.hbs.edu/faculty/Pages/item.aspx?num=31700
- Coauthor research page: https://www.aqr.com/Insights/Research/Journal-Article/Economic-Links-and-Predictable-Returns
- DOI: https://doi.org/10.1111/j.1540-6261.2008.01379.x
- Web refs: `turn38search5`, `turn47view1`.
- Result: The paper documents return predictability across customer–supplier links, consistent with limited attention to economically connected firms. Links were public, rather than privileged information.
- Limit: Historical findings do not establish a profitable current implementation, and link knowledge must be dated to when it became public.
- Skill implication: Investigate slower **semantic propagation** of news through economic relationships, with point-in-time graphs and controls for own momentum, industry, liquidity, and shared factors.

### I10. Attention can vary with the release environment

Stefano DellaVigna and Joshua M. Pollet (2009), **Investor Inattention and Friday Earnings Announcements**, Journal of Finance 64(2), 709–749.

- Author institution: https://experts.illinois.edu/en/publications/investor-inattention-and-friday-earnings-announcements/
- Author manuscript: https://sdellavi.com/pdf/earnfr080204.pdf
- DOI: https://doi.org/10.1111/j.1540-6261.2009.01447.x
- Web ref: `turn43view1`.
- Result: In their sample, Friday announcements showed weaker immediate responses, stronger delayed responses, and lower volume, supporting an attention account of delayed incorporation.
- Limit: Release timing can be selected by firms; the historical result is not an instruction to trade Fridays mechanically. Current costs and publication decay require testing.
- Skill implication: Model attention relative to news load, release timing, and competing events; treat calendar labels as proxies with a falsifiable mechanism.

### I11. Repetition is not independent evidence

Paul C. Tetlock (2011), **All the News That's Fit to Reprint: Do Investors React to Stale Information?**, Review of Financial Studies 24(5), 1481–1512.

- Author institution: https://business.columbia.edu/faculty/research/all-news-thats-fit-reprint-do-investors-react-stale-information
- DOI: https://doi.org/10.1093/rfs/hhq141
- Web ref: `turn59view0`.
- Result: Textual similarity identifies stale stories; price moves around stale news predict later reversal, especially where individual-investor activity is higher. The evidence is consistent with overreaction to repeated information.
- Limit: Text similarity is not a complete measure of semantic novelty; a repeated fact can become relevant under a changed context. Historical reversal does not establish current net alpha.
- Skill implication: Maintain event provenance, first-publication timestamps, revisions, and a novelty score. Update on new facts and changed conditional relevance; do not multiply likelihoods for syndicated copies.

### I12. Speed rents depend on market design

Eric Budish, Peter Cramton, and John Shim (2015), **The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response**, Quarterly Journal of Economics 130(4), 1547–1621.

- Author page: https://ericbudish.org/publication/the-high-frequency-trading-arms-race-frequent-batch-auctions-as-a-market-design-response/
- DOI: https://doi.org/10.1093/qje/qjv027
- Web ref: `turn47view0`.
- Result: Continuous serial processing can produce mechanical arbitrage rents even when information is publicly and symmetrically observed. Their model and evidence motivate frequent batch auctions that shift competition toward price.
- Limit: This is not a promise that a generic internet-connected bot can capture such rents; access and speed competition are central. Claimed opportunity size must be distinguished from attainable fills.
- Skill implication: Record event, observation, decision, submission, acknowledgement, and fill times. Compare signal lifetime with end-to-end latency before buying faster infrastructure.

## Mathematical operating rules — synthesis and elementary derivations

These formulas are proposed operational translations, not claims that all the cited authors state them in this form.

1. **Sequential Bayesian evidence.** For hypothesis H and information already known F, posterior odds after observations E1…En are prior odds multiplied by conditional likelihood ratios:

   O(H | F,E1…En) = O(H | F) × product_k P(Ek | H,F,E<k) / P(Ek | not-H,F,E<k).

   The conditioning prevents double-counting correlated stories, indicators, and model outputs. Likelihoods require empirical or defensible generative estimation; an LLM's confident wording is not a measured probability. Market prices belong in F when they reveal relevant evidence, but do not automatically equal the physical-event prior.

2. **Decision value, not prediction accuracy alone.** For action a including abstention, payoff U, existing information F, candidate experiment Z and its cost c:

   EVSI(Z) = E_Z[max_a E[U(a,theta) | F,Z]] − max_a E[U(a,theta) | F] − c.

   Compare this with acquisition delay and missed-trade value. For a model with imperfect calibration, estimate the attainable improvement through held-out decisions, not an oracle calculation pretending the posterior is known.

3. **Fill-conditioned net value.** For quantity q and order action a:

   EV(a) = P(fill | F,a) × E[q(V_h − P_fill) − variable_costs | F,a,fill] − fixed_attempt_costs.

   Add multiple partial-fill outcomes explicitly when needed; for shorts, reverse the payoff sign. Include exit execution and financing in variable costs. This expression can be positive or negative even when unconditional E[V_h | F] exceeds the current midpoint. Never multiply by a fill probability after already estimating P&L over all attempts including zeros.

4. **Relative information test.** Compare a market-only baseline using timestamp-correct quote/order-book/state data against the identical model plus candidate evidence. Test the incremental out-of-sample proper-score improvement **and** net policy value on the actual selected trade subset. A lower overall Brier score can coexist with worse P&L if improvement occurs where no trade is taken or losses are larger.

5. **Latency frontier.** Treat alpha(delay,size) as an estimated surface, rather than a fixed number. Net captured value equals executable value at measured delay/size minus execution and infrastructure costs. Faster decisions matter only where this surface is steep enough and confidence is not degraded excessively.

## Three creative, falsifiable research programs

### A. An attention map of the marginal price setter

**Hypothesis:** Public information travels quickly to heavily watched securities but more slowly through low-salience economic links when the market's attention is saturated. A small desk may specialize in the residual window.

**Construction:** Form a point-in-time customer/supplier or contractual-exposure graph from dated filings. For each genuinely new event, compute direct and second-order cash-flow exposure, publication time, novelty, simultaneous news load, baseline liquidity, and analyst/ownership attention proxies. Predict residual returns after standard factor and own-momentum controls. Do not call a correlation a causal relationship.

**Test:** Freeze links as they were known then; walk forward by event date; compare linked versus matched unlinked firms; use irrelevant-event and pre-event placebo windows. Evaluate actual entry delay, spread, borrow, turnover, and capacity. Compare graph interpretation against a simple signed customer-return baseline.

**Kill criterion:** No incremental net benefit out of sample, sensitivity to later-revised links, benefit only at impossible timestamps, or performance entirely explained by industry/momentum exposure.

### B. Treat execution as a second evidence channel

**Hypothesis:** An apparently cheap order that fills unusually quickly can be adverse information; apparent alpha should update after fill/queue events rather than remain frozen at submission.

**Construction:** Estimate both P(fill | state,price,queue proxy) and the distribution of horizon markouts conditional on fill. Compare passive, aggressively priced, and skip actions. Use observed order-event logs; full queue reconstruction is optional but assumptions must be stated. Distinguish an actual cancellation acknowledgement from a request to cancel.

**Test:** Replay against timestamped quotes with conservative queue assumptions; shadow-log all attempts including unfilled orders. Evaluate prediction calibration within fill-time bins and stress cancellation lag and stale quotes. Run a simple immediate-crossing baseline to identify whether prediction or execution creates value.

**Kill criterion:** Paper alpha disappears after conditional markouts or latency, or improvement depends on counterfactual fills that were not obtainable. This is a research design, not proof that rapid fills always signal toxicity.

### C. Budget research by value of information

**Hypothesis:** A sequential evidence policy can outperform a uniformly expensive analysis by spending computation only near decision boundaries where a new observation changes the optimal action before the opportunity decays.

**Construction:** Start with a calibrated inexpensive baseline; estimate the probability that an additional source/model changes the selected action and the conditional value of that change. Acquire the next source with highest estimated incremental utility net of money and delay. Deduplicate evidence by event provenance. Stop when the best further experiment has nonpositive estimated value or a deadline arrives.

**Test:** On fully logged historical event streams, compare fixed shallow analysis, fixed deep analysis, and the adaptive policy using equal all-in budgets. Train the routing policy on earlier periods only; evaluate the entire route and policy on held-out events. Count failed retrievals, source lag, and computation costs. Force ablations removing extra agents to check whether they add evidence or merely repeat a narrative.

**Kill criterion:** Routing gains vanish against a simpler threshold, estimated value is miscalibrated, or extra analysis arrives after prices move. This is a bounded-rationality engineering proposal; no theorem guarantees net trading returns.

## Precise instructions recommended for the final skill

- Require an edge sentence: “Under state S, participant P accepts payoff price Q because mechanism M; evidence E available by time T gives us advantage A; we monetize through action X before decay D; competitor response C would erase it.”
- Demand a complete payoff definition, executable quote/size, settlement or exit rule, clock, cost model, and a null hypothesis.
- Separate evidence novelty from persuasive fluency; keep source lineage and avoid treating correlated indicators or LLM votes as independent experiments.
- Derive both the bullish and bearish interpretations of the same fill or price move; identify what observable data would distinguish them.
- Use historical findings to generate hypotheses, never to certify current alpha.
- Record the mechanism that limits competition and the counterparty's objective; do not assume the counterparty is foolish.
- Permit NO EDGE / INSUFFICIENT EVIDENCE / NOT IMPLEMENTABLE as successful analytical outcomes. A good skill creates and tests opportunities; it cannot decree their existence.
