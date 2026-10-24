from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
old = (root/'v1/Trading_Edge_Master_Prompt.txt').read_text()
adaptive = (root/'v2/Trading_Edge_Adaptive_Master_Prompt.txt').read_text()
old_body = old.split('BEGIN PROMPT\n', 1)[1].split('\nEND PROMPT', 1)[0].strip()
old_parts = re.split(r'^## (\d+)\. ([^\n]+)\n', old_body, flags=re.M)
base = {int(old_parts[i]): old_parts[i+2].strip() for i in range(1, len(old_parts), 3)}
new_parts = re.split(r'^(\d+)\. ([A-Z][^\n]+)\n', adaptive, flags=re.M)
add = {int(new_parts[i]): new_parts[i+2].strip() for i in range(1, len(new_parts), 3)}
runtime, tail = add[10].split('\nMASTER LOOP\n', 1)
master, outcome = tail.split('\nOUTPUT\n', 1)
master = master.replace('On outcome maturity:', 'If no candidate passes, retain the feasible incumbent and record rejection reasons; if the incumbent is infeasible, use the separate recovery policy. If atomic revalidation detects a changed snapshot, policy, limit or reservation version, recompute within the deadline or use a currently valid approved fallback; never commit the stale decision.\nOn outcome maturity:')
metrics = outcome.split('\n\nMeasure claimed intelligence', 1)[1]

base[1] = base[1].replace('Preserve an existing strategy as a frozen baseline.', 'Preserve an existing strategy as a frozen baseline and reproduce it. Freeze a comparable opportunity population, capital convention and evaluation horizon. Record the calendar, funding limits and operational dependencies.')
base[1] = base[1].split('\n\nThis prompt is self-contained.', 1)[0]
base[2] = base[2].replace('Use “arbitrage” strictly for a feasible self-financing payoff with no negative state payoff and a positive payoff in at least one relevant state, under stated assumptions.', 'Use “arbitrage” strictly for a feasible self-financing strategy with nonpositive initial net cost, no negative terminal net payoff almost surely, a positive benefit with positive probability, and financeable interim obligations, under stated assumptions.')
base[3] = base[3].replace('10. **Evidence:** data available, missing, and the cheapest experiment that changes the decision.', '10. **Evidence:** evidence stage, data available, missing, and the cheapest experiment that changes the decision.')
base[2] += '\n\nA controller cannot create an absent economic advantage. Under an actual-measure martingale model with admissible predictable integrable trading and nonnegative costs, expected net trading gains are nonpositive. This conditional model statement is distinct from risk-neutral pricing and does not assert that real markets always satisfy it.'
add[2] += '\n\nAccount for action-dependent transitions and observations: our impact, inventory and fills can change future opportunities and what we learn. A filtering equation does not supply known likelihoods. Stability across environments is a useful falsification test; causal identification still requires structural assumptions.'
base[7] += '\n\nCompare the frozen policy, a simple periodic-refit policy and the proposed adaptive policy on the same as-of opportunities. Charge false alarms, switching, missed fills, computation and maintenance. Evaluate the adaptation rules themselves, not just the final fitted model.'
add[7] += '\n\nDo not replace actual assignment probabilities with empirical action frequencies when routing was deterministic. Weight clipping introduces bias; effective sample size is a diagnostic, not a validity certificate. Unresolved outcomes are neither zero nor absent. Preserve the planned reward horizon, distinguish it from trade closing time, compare mature cohorts and track pending exposure separately.'
runtime += '\n\nTrack cumulative fills, remaining executable quantity, corrections/busts and reconciliation confidence separately from headline order status. A locally unique intent ID does not establish exactly-once external execution. Prioritize account and execution events; bound queues, preserve corrections and reserve deadline budget for mandatory checks and submission. Report end-to-end latency quantiles and deadline misses; do not add component p99 values.\n\nAcceptance tests must cover late/revised data, stale caches, a crash after broker acceptance, a fill after a cancel request, amendments versus cancel/new, concurrent sleeve reservations, unknown positions, expired fallback and execution busts. Replay equivalence and synthetic tests establish specified behavior, not profitability.'
add[4] = add[4].replace('min_{P in Pset}', 'inf_{P in Pset}')
add[4] = add[4].replace('Let W^a be', 'Use infimum for a general distribution set and minimum when attained. Let W^a be')

intro = '''TRADING EDGE LAB — UNIFIED MASTER PROMPT
Version 2.1 | Original edge framework + adaptive-control addendum | 24 October 2026 UTC

USAGE
Paste everything between BEGIN PROMPT and END PROMPT into the LLM, then append your strategy, desk, sleeve, research objective or available evidence. This is one complete prompt: no separate addendum, installed skill or companion report is required. Use it as a user instruction or in a permitted agent instruction layer; it does not override higher-priority instructions.

Suggested request: Apply this entire framework to the material below. Diagnose the actual economic edge and binding loss of value, execute accessible research, and produce the smallest precise improvement with a decisive validation plan. Distinguish measured results from hypotheses. Preserve my existing timing authority and deployment boundaries.

BEGIN PROMPT

# Trading Edge Lab

Operate as a market economist, probabilistic forecaster, decision researcher, execution engineer and skeptical experimentalist. Convert an appealing idea into a specific opportunity, an executable policy and an attempt to disprove it. Be creative about mechanisms and strict about evidence. Produce useful work when evidence is incomplete; mark hypotheses and execute or specify the next decisive experiment.

Use this governing question:

What scarce information, lawful access, service or risk-bearing capacity do we supply; who values it; why does its price leave us a surplus; and what stops competition, costs, bad-state losses, capital occupation or delay from consuming that surplus?

Do not treat an indicator, high win rate, compelling story or successful backtest as an answer. Optimize feasible decisions and honest learning. A prompt cannot guarantee profitability, make every strategy viable or justify a daily trade quota. Supply auditable reasoning, equations, evidence and decisions rather than hidden reasoning traces or rhetorical confidence.
'''

sections = [
('Establish the decision and evidence boundary', base[1]),
('Name precisely what kind of edge is claimed', base[2]),
('Build the economic map before adding features', base[3]),
('Model beliefs, prices, fills and the full payoff', base[4]),
('Price risk and allocate capital in portfolio context', base[5]),
('Create candidates or repair the weakest link', base[6]),
('Represent what the desk knows', add[2]),
('Define the feasible action menu', add[3]),
('Score complete net outcomes against the incumbent', add[4]),
('Allocate computation by decision value', add[5]),
('Separate execution, belief updates and policy changes', add[6]),
('Design adversarial validation', base[7]),
('Learn only what the data identify', add[7]),
('Make sequential evidence explicit', add[8]),
('Diagnose before retraining', add[9]),
('Execute through a recoverable contract', runtime.strip()+'\n\n'+base[8].split('\n\n')[1]),
('Run the master algorithm', master.strip()),
('Deliver one decision and implementation contract', '''Return the following, proportionate to the task. Produce one integrated answer and preserve explicit unknowns.

1. Verdict: supported, promising but unproven, unsupported or rejected; evidence stage, uncertainty and completed versus unrun work.
2. Edge contract: payer/service or belief wedge, our measurable advantage, persistence, bad state, strongest rival and falsifier.
3. Binding bottleneck and improvement priority: forecast, selection, timing, execution, sizing, portfolio interaction, data or operations; expected incremental benefit, evidence, effort and fragility. Include the simplest adequate version.
4. Exact policy specification: as-of inputs, state representation, entry/exit/no-new-entry logic, feasible actions, update rules, timing authority, execution and sizing constraints, deadlines and contingencies. Distinguish measured values from placeholders.
5. Quantitative economics: executable break-even, full cost/risk decomposition, paired portfolio effect, sensitivity and capacity. Label illustrations and unsupported estimates.
6. Evidence and experiments: dated sources, provenance, completed results, missing data, baselines, negative controls, next decisive experiment and rejection rule.
7. Operational handoff when requested: artifacts, reproducible commands, lifecycle and reconciliation contract, acceptance tests, evidence/promotion/retirement gates and actual deployment status.
8. Measurement plan: baseline, workload, units and uncertainty for every claimed improvement.

Measure claimed intelligence '''+metrics.strip()+'''

End with the highest-value next action. Do not turn “unproven” into a dead end: identify what establishes or refutes the claim, collect accessible evidence and execute authorized research.'''),
('Check the reasoning before finalizing', base[10]),
]

text = intro.strip()+'\n\n'+'\n\n'.join(f'## {i}. {name}\n\n{body}' for i,(name,body) in enumerate(sections, 1))+'\n\nEND PROMPT\n'
text = re.sub(r'\n{3,}', '\n\n', text)
path = root/'build/Trading_Edge_Unified_Master_Prompt_v2.1.txt'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(text)
assert text.count('\nBEGIN PROMPT\n') == 1
assert text.count('\nEND PROMPT\n') == 1
assert 'separate addendum' in text and 'It supplements' not in text
print(f'{path}\n{len(text.split())} words; {len(text.encode())} bytes; {len(sections)} sections')
