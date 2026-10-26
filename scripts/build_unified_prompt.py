"""Assemble the standalone root prompt.

v3.0: preserved v2.1 plus the v3 protocol (unchanged logic; checked byte for byte against
v3/Trading_Edge_Unified_Master_Prompt_v3.0.txt). v4.0: v3.0 plus the Edge Ledger, the workflow and the field rules,
taken from skills/engineer-trading-edge/SKILL.md with file links removed so the prompt stays self-contained.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]


def build_v3():
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
    return renumber(base)


def renumber(text):
    counter = [0]

    def heading(match):
        counter[0] += 1
        return f'## {counter[0]}. {match.group(1)}'
    return re.sub(r'^## \d+\. (.+)$', heading, text, flags=re.M), counter[0]


def replace_once(text, old, new):
    assert text.count(old) == 1, old[:70]
    return text.replace(old, new)


def skill_sections():
    """The Edge Ledger, workflow and field rules from SKILL.md, without links to repository files."""
    skill = (root / 'skills/engineer-trading-edge/SKILL.md').read_text()
    start = skill.index('## 1. The Edge Ledger: fill it first')
    end = skill.index('## 4. Evidence and claims')
    text = skill[start:end].strip()
    markov = next(line for line in skill.splitlines() if line.startswith("Johann Markov's two sources"))
    markov = markov.split('. An indicator')[0] + '.'
    text = replace_once(text, '## 1. The Edge Ledger: fill it first\n\n',
                        '## 1. The Edge Ledger: fill it first\n\n' + markov + '\n\n')
    text = replace_once(text, ' Template [assets/edge-ledger.md](assets/edge-ledger.md); check with `python scripts/ledger_lint.py <file>`; diagnostics and archetypes in [references/edge-ledger.md](references/edge-ledger.md).', '')
    text = replace_once(text, 'The ledger extends the edge contract in [references/validation.md](references/validation.md) (game,',
                        'The ledger extends the edge contract below (game,')
    text = replace_once(text, 'Each links to its decision record in [references/field-casebook.md](references/field-casebook.md).',
                        'Each is the lesson of a measured case.')
    text = re.sub(r' \[C\d\d\]\([^)]*\)', '', text)
    text = re.sub(r' \(\[(?:assets|references)/[^\]]*\]\([^)]*\)\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    for word in ('references/', 'assets/', 'scripts/', '](', 'casebook'):
        assert word not in text, word
    return text + '\n\n'


def build_v4(v3_text):
    text = replace_once(v3_text, 'Version 3.0 | Economic edge + adaptive control + explicit information, risk and invention procedures | 24 October 2026 America/New_York',
                        'Version 4.0 | Edge Ledger + field rules from a live desk + economic edge + adaptive control | 26 October 2026 America/New_York')
    text = replace_once(text, 'Suggested request: Apply this entire framework to the material below. Diagnose',
                        'Suggested request: Apply this entire framework to the material below. Fill the Edge Ledger first. Diagnose')
    text = replace_once(text, '## 1. Establish the decision and evidence boundary', skill_sections() + '## 1. Establish the decision and evidence boundary')
    text = replace_once(text, '2. Edge contract and decision record: payer/service or belief wedge,',
                        '2. Edge Ledger, contract and decision record: speed, accuracy, access or warehoused variance; execution net; decisive test and kill rule; payer/service or belief wedge,')
    return renumber(text)


v3_text, _ = build_v3()
assert v3_text == (root / 'v3/Trading_Edge_Unified_Master_Prompt_v3.0.txt').read_text(), 'v3.0 rebuild differs from the preserved prompt'
v4_text, sections = build_v4(v3_text)
assert v4_text.count('\nBEGIN PROMPT\n') == 1
assert v4_text.count('\nEND PROMPT\n') == 1
assert 'references/' not in v4_text
added = len(v4_text.encode()) - len(v3_text.encode())
assert added <= 10_500, added
out = root / 'build/Trading_Edge_Unified_Master_Prompt.txt'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(v4_text)
(root / 'build/Trading_Edge_Unified_Master_Prompt_v3.0.txt').write_text(v3_text)
print(f'{out}\n{len(v4_text.split())} words; {sections} sections; {added} bytes added to v3.0')
