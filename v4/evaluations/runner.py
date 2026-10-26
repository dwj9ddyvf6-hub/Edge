"""Run the v4 behavior test: build solver prompts, blind the answers, score the grades, verify the freeze.

Standard library only. Run from the repository root.

    python v4/evaluations/runner.py verify
    python v4/evaluations/runner.py prompts OUT_DIR
    python v4/evaluations/runner.py blind ANSWERS_DIR OUT_DIR --seed 2026
    python v4/evaluations/runner.py score GRADES.json KEY.json

ANSWERS_DIR holds one Markdown file per solver, named <arm>_<n>.md with arm "base" or "skill".
blind writes OUT_DIR/blinded/R1.md ... and OUT_DIR/grader_prompt.txt for the grader, and OUT_DIR/key.json, which the
grader must not see. GRADES.json maps each blinded label to its cases:
    {"R1": {"E01": {"items": [2, 0, 2, 1, 1], "penalty": 0, "critical": false, "quotes": ["..."]}, ...}, ...}
"""

import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SKILL = "skills/engineer-trading-edge"

BASE_PREAMBLE = ("Answer from your own knowledge and reasoning. Do not open files in any repository, use skills, or "
                 "search the web.")
SKILL_PREAMBLE = (f"Before answering, read {SKILL}/SKILL.md in this repository and any of the references it points "
                  "to that you need. Do not open v4/evaluations/ or search the web.")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name):
    return json.loads((HERE / name).read_text())


def case_text():
    cases = load("cases.json")
    lines = [cases["instructions"], ""]
    for c in cases["cases"]:
        lines += [f"{c['id']}. {c['title']}", c["task"], ""]
    return "\n".join(lines)


def cmd_verify():
    freeze = load("freeze.json")
    ok = True
    for name, digest in freeze["files"].items():
        now = sha256(HERE / name)
        print(f"{name}: {'ok' if now == digest else 'CHANGED'}")
        ok &= now == digest
    tree = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"HEAD:{SKILL}"], capture_output=True,
                          text=True).stdout.strip()
    same = tree == freeze["skill_tree"]
    print(f"skill tree at HEAD {tree[:12]}: {'same as frozen' if same else 'DIFFERS from frozen ' + freeze['skill_tree'][:12]}")
    return 0 if ok and same else 1


def cmd_prompts(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    body = case_text()
    (out / "solver_prompt_base.txt").write_text(BASE_PREAMBLE + "\n\n" + body)
    (out / "solver_prompt_skill.txt").write_text(SKILL_PREAMBLE + "\n\n" + body)
    print(f"wrote {out}/solver_prompt_base.txt and solver_prompt_skill.txt")
    return 0


def cmd_blind(answers, out, seed):
    answers, out = Path(answers), Path(out)
    files = sorted(answers.glob("*.md"))
    arms = [f.stem.split("_")[0] for f in files]
    if not files or any(a not in ("base", "skill") for a in arms):
        raise SystemExit("answer files must be named base_<n>.md or skill_<n>.md")
    order = list(range(len(files)))
    random.Random(seed).shuffle(order)
    (out / "blinded").mkdir(parents=True, exist_ok=True)
    key = {}
    for label_no, idx in enumerate(order, 1):
        label = f"R{label_no}"
        (out / "blinded" / f"{label}.md").write_text(files[idx].read_text())
        key[label] = {"file": files[idx].name, "arm": arms[idx]}
    (out / "key.json").write_text(json.dumps({"seed": seed, "labels": key}, indent=1) + "\n")
    rubric = load("rubric.json")
    grader = ["You are grading anonymous answers to twelve fictional strategy cases with a frozen rubric.",
              "Grade each answer file independently, in the order given. Do not guess which answers used any aid.",
              rubric["grading"], "", "CASES", case_text(), "RUBRIC", json.dumps(rubric["cases"], indent=1), "",
              "Return JSON only: {label: {case_id: {\"items\": [points per item in rubric order], \"penalty\": "
              "negative points or 0, \"critical\": true or false, \"quotes\": [the sentence earning each point]}}}.",
              "Answers to grade: " + ", ".join(f"R{i}" for i in range(1, len(files) + 1))]
    (out / "grader_prompt.txt").write_text("\n".join(grader))
    print(f"blinded {len(files)} answers into {out}/blinded; key in {out}/key.json (keep it from the grader)")
    return 0


def cmd_score(grades_path, key_path):
    rubric = {c["id"]: c for c in load("rubric.json")["cases"]}
    grades = json.loads(Path(grades_path).read_text())
    key = json.loads(Path(key_path).read_text())["labels"]
    per_arm, rows = {}, []
    for label, cases in sorted(grades.items()):
        total, criticals = 0, 0
        for cid, spec in rubric.items():
            g = cases.get(cid)
            if g is None:
                raise SystemExit(f"{label} has no grade for {cid}")
            if len(g["items"]) != len(spec["items"]):
                raise SystemExit(f"{label} {cid}: {len(g['items'])} item scores, rubric has {len(spec['items'])}")
            for got, item in zip(g["items"], spec["items"]):
                if not 0 <= got <= item["pts"]:
                    raise SystemExit(f"{label} {cid}: item score {got} outside 0..{item['pts']}")
            score = max(0, sum(g["items"]) + min(0, g.get("penalty", 0)))
            total += score
            criticals += bool(g.get("critical"))
            rows.append((label, key[label]["arm"], cid, score, spec["points"]))
        arm = key[label]["arm"]
        per_arm.setdefault(arm, []).append((label, total, criticals))
    print("| answer | arm | total | critical errors |\n|---|---|---|---|")
    for arm, items in sorted(per_arm.items()):
        for label, total, crit in items:
            print(f"| {label} | {arm} | {total}/{sum(c['points'] for c in rubric.values())} | {crit} |")
    print("\n| case | type | " + " | ".join(f"{lab} ({key[lab]['arm']})" for lab in sorted(grades)) + " |")
    print("|---|---|" + "---|" * len(grades))
    for cid, spec in rubric.items():
        cells = [f"{s}/{m}" for (lab, _, c, s, m) in rows if c == cid]
        print(f"| {cid} | {spec['type']} | " + " | ".join(cells) + " |")
    result = {arm: [{"label": l, "total": t, "critical": c} for l, t, c in items] for arm, items in per_arm.items()}
    out = Path(grades_path).with_name("scores.json")
    out.write_text(json.dumps(result, indent=1) + "\n")
    print(f"\nwrote {out}")
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    if cmd == "verify":
        return cmd_verify()
    if cmd == "prompts" and len(args) == 1:
        return cmd_prompts(args[0])
    if cmd == "blind" and len(args) >= 2:
        seed = int(args[args.index("--seed") + 1]) if "--seed" in args else 2026
        return cmd_blind(args[0], args[1], seed)
    if cmd == "score" and len(args) == 2:
        return cmd_score(args[0], args[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
