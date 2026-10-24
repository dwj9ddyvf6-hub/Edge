"""Assemble one standalone v3 prompt from preserved v2.1 and the v3 protocol."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
base = (root / 'v2/Trading_Edge_Unified_Master_Prompt_v2.1.txt').read_text()
protocol = (root / 'v3/skill/references/edge-protocol.md').read_text()
base = base.replace('Version 2.1 | Original edge framework + adaptive-control addendum',
                    'Version 3.0 | Economic edge + adaptive control + explicit information, risk and invention procedures')
base = base.replace('| 24 October 2026 UTC', '| 24 October 2026 America/New_York', 1)
parts = re.split(r'^## (\d+)\. ([^\n]+)\n', protocol, flags=re.M)
sections = {int(parts[i]): (parts[i+1], parts[i+2].strip())
            for i in range(1, len(parts), 3)}
selected = []
for number in (1, 2, 3, 4, 5, 6):
    title, body = sections[number]
    if number == 1:
        body = body.replace('A correct instruction does not prove adherence.',
                            'Apply these instructions by producing their required decisions and calculations. A correct instruction does not prove adherence.')
    selected.append('## 0. ' + title + '\n\n' + body)
insert = '\n\n'.join(selected) + '\n\n'
anchor = '## 7. Represent what the desk knows'
assert anchor in base
base = base.replace(anchor, insert + anchor, 1)
base = base.replace('Configure economic contracts, baseline, action menu, update rules, data contracts, budgets, limits, deadlines, evidence gates and contingencies.',
'''On a research request: preserve the incumbent and mandate; identify the information increment or paid burden; generate a small diverse set of economic transformations; calculate conditional information value, portfolio reservation value or state-payoff restrictions as appropriate; model executable capture and funding; choose the next decisive experiment; admit only validated and approved candidates to the execution policy.

Configure economic contracts, baseline, action menu, update rules, data contracts, budgets, limits, deadlines, evidence gates and contingencies.''', 1)
base = base.replace('2. Edge contract: payer/service or belief wedge, our measurable advantage, persistence, bad state, strongest rival and falsifier.',
                    '2. Edge contract and decision record: payer/service or belief wedge, our measurable advantage, persistence, bad state, strongest rival and falsifier; explicit transfer, comparator, calculation and experiment.')
counter = [0]
def heading(match):
    counter[0] += 1
    return f'## {counter[0]}. {match.group(1)}'
base = re.sub(r'^## \d+\. (.+)$', heading, base, flags=re.M)
assert base.count('\nBEGIN PROMPT\n') == 1
assert base.count('\nEND PROMPT\n') == 1
assert 'references/' not in base
out = root / 'build/Trading_Edge_Unified_Master_Prompt.txt'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(base)
print(f'{out}\n{len(base.split())} words; {counter[0]} sections')
