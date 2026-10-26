# Behavior test v4: how to run it

Does an LLM that reads the skill carry the field lessons to fresh problems better than the same model without it?
Twelve fictional cases ([cases.json](cases.json)) and a 98-point rubric ([rubric.json](rubric.json)) were frozen on
26 October 2026, before any solver or grader ran; [freeze.json](freeze.json) holds their hashes and the skill tree
under test. Results go in [../validation.md](../validation.md).

## Design

- **Transfer, not recall.** No case repeats a casebook example's market, numbers or wording.
- **Against the ceiling.** Points need specific moves: computing per-opportunity expectancy, deflating a search,
  counting effective bets, testing against the series' own volatility. Vocabulary earns nothing.
- **Over-application.** E05, E09 and E12 are controls where a lesson does not apply; misapplying it costs 2 points.
- **Creation.** E06 and E07 are CREATE cases graded on payer, mechanism, execution net, decisive test and kill rule.

## Steps

1. `python v4/evaluations/runner.py verify` must print `ok` for every file and `same as frozen` for the skill tree.
2. `python v4/evaluations/runner.py prompts <dir>` writes the two solver prompts. They differ only in their first
   paragraph: the base arm may not read files or the web; the skill arm reads `skills/engineer-trading-edge/SKILL.md`
   and what it points to.
3. Run four fresh agents on the same model and settings: two with the base prompt, two with the skill prompt. Each
   sees only its prompt. Save each answer verbatim as `<answers>/base_1.md`, `base_2.md`, `skill_1.md`, `skill_2.md`.
4. `python v4/evaluations/runner.py blind <answers> <run> --seed 2026` shuffles the answers into `R1`–`R4`, writes
   `<run>/grader_prompt.txt`, and keeps the mapping in `<run>/key.json`.
5. Give a fresh grader agent `grader_prompt.txt` and the four blinded files, never `key.json`. Save its JSON reply as
   `<run>/grades.json`.
6. `python v4/evaluations/runner.py score <run>/grades.json <run>/key.json` prints totals per arm and per case and
   writes `scores.json`.
7. Commit the answers, the blinded files, the grader prompt and reply, the key and the scores under
   `v4/evaluations/run-<date>/`, failures included. Report each arm's scores exactly, with n = 2 answers per arm and
   12 cases, once in `v4/validation.md` and once in the README.

## Reading the result

Two answers per arm on twelve cases is a diagnostic, not a measurement of general improvement or of trading
performance. A difference smaller than the spread between the two answers of the same arm is no difference. Once
these cases are published they are regression material, not an untouched holdout.
