"""Lint a filled Edge Ledger (Markdown or JSON) for the omissions that most often pass for an edge.

Markdown: one field per line, as "Field: entry", "- **Field:** entry" or a table row "| Field | ... | entry |"
(the last cell is the entry).
JSON: an object whose keys are the field names. Labels are matched case-insensitively (see FIELDS).

Errors (exit status 1):
  E1 no payer: a pattern, not an edge
  E2 no source of edge: speed, accuracy, access and warehoused variance are all empty
  E3 a speed claim with no lead time in numbers
  E4 a risk-warehousing claim with no bad state
  E5 a searched result (searched: yes, or search words in the evidence) with no trial count
  E6 no kill rule
  E7 no decisive test
Warnings:
  W1 an accuracy claim with no price-aware baseline
  W2 an access claim that does not say why it stays open
  W3 no execution net
  W4 a risk-warehousing claim that does not say whether the book can hold it or what else loses with it

Usage: python ledger_lint.py LEDGER.md [--json]
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass
from typing import Dict, List

FIELDS = {
    "speed": ("speed", "what we learn sooner"),
    "lead_time": ("lead time", "speed lead time"),
    "accuracy": ("accuracy", "what we update better"),
    "baseline": ("baseline", "price-aware baseline", "incremental value", "incremental decision value"),
    "access": ("access", "the bet others cannot take"),
    "why_open": ("why it stays open", "why open", "stays open"),
    "variance": ("variance", "warehoused variance", "which variance"),
    "shedder": ("shedder", "who sheds it", "who sheds it and why"),
    "premium": ("premium",),
    "bad_state": ("bad state", "when it bites"),
    "holdable": ("holdable", "can the book hold it", "hold through the bad state"),
    "co_losses": ("co-losses", "co losses", "what else loses"),
    "payer": ("payer", "who pays"),
    "execution_net": ("execution net", "net of execution"),
    "decisive_test": ("decisive test", "decisive cheap test", "first test"),
    "kill_rule": ("kill rule", "rejection rule"),
    "evidence": ("evidence", "evidence so far", "result"),
    "searched": ("searched", "found by search"),
    "trials": ("trials", "trial count", "variants tried"),
    "evidence_stage": ("evidence stage", "stage"),
}
_ALIASES = {re.sub(r"[^a-z0-9 ]", "", alias.replace("-", " ")).strip(): key
            for key, aliases in FIELDS.items() for alias in aliases + (key.replace("_", " "),)}
_PLACEHOLDER = {"", "-", "\u2014", "tbd", "todo", "?", "..."}
_NOT_CLAIMED = _PLACEHOLDER | {"n/a", "na", "none", "unknown", "not claimed", "no"}
_SEARCH_WORDS = re.compile(r"\b(optimi[sz]ed|grid|sweep|scan(ned)?|mined|searched|best of|tuned|screened)\b", re.I)


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    message: str


def _key(label: str):
    label = re.sub(r"[*_`]", "", label).replace("-", " ").lower()
    label = re.sub(r"[^a-z0-9 ]", "", label)
    label = re.sub(r"\s+", " ", label).strip()
    return _ALIASES.get(label)


def parse_markdown(text: str) -> Dict[str, str]:
    """Collect recognised "Field: entry" lines and two-column table rows; unknown labels are ignored."""
    out: Dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and not set(cells[0]) <= set("-: "):
                key = _key(cells[0])
                if key:
                    out[key] = cells[-1]
            continue
        m = re.match(r"^[-*+]?\s*\**([^:*]{1,60}?)\**\s*:\s*\**\s*(.*)$", line)
        if m:
            key = _key(m.group(1))
            if key:
                out[key] = m.group(2).strip()
    return out


def parse(text: str) -> Dict[str, str]:
    stripped = text.lstrip()
    if stripped.startswith("{"):
        data = json.loads(text)
        out = {}
        for label, value in data.items():
            key = _key(label) or (label if label in FIELDS else None)
            if key:
                out[key] = "" if value is None else str(value)
        return out
    return parse_markdown(text)


def _norm(value: str) -> str:
    return value.strip().strip(".").strip().lower()


def _filled(fields: Dict[str, str], key: str) -> bool:
    """A claim is made: not blank, not a placeholder, not "none" or "unknown"."""
    return _norm(fields.get(key, "")) not in _NOT_CLAIMED


def _answered(fields: Dict[str, str], key: str) -> bool:
    """A question is answered, even with "no" or "none"."""
    return _norm(fields.get(key, "")) not in _PLACEHOLDER


def lint(fields: Dict[str, str]) -> List[Finding]:
    f = fields
    out: List[Finding] = []
    if not _filled(f, "payer"):
        out.append(Finding("E1", "error", "no payer: a pattern, not an edge. Name who pays and why they accept it."))
    sources = [k for k in ("speed", "accuracy", "access", "variance") if _filled(f, k)]
    if not sources:
        out.append(Finding("E2", "error", "no source of edge: fill speed, accuracy, access or warehoused variance."))
    if _filled(f, "speed") and not re.search(r"\d", f.get("lead_time", "")):
        out.append(Finding("E3", "error", "speed claim with no lead time in numbers (against the price's own update "
                                          "and the capture window)."))
    risk = any(_filled(f, k) for k in ("variance", "shedder", "premium"))
    if risk and not _filled(f, "bad_state"):
        out.append(Finding("E4", "error", "risk-warehousing claim with no bad state: say when it bites and how hard."))
    searched = _norm(f.get("searched", "")) in {"yes", "y", "true"} or bool(_SEARCH_WORDS.search(f.get("evidence", "")))
    if searched and not re.search(r"\d", f.get("trials", "")):
        out.append(Finding("E5", "error", "searched result with no trial count: record every variant tried, then "
                                          "deflate (DSR, BH)."))
    if not _filled(f, "kill_rule"):
        out.append(Finding("E6", "error", "no kill rule: state the result that retires it, before the data arrive."))
    if not _filled(f, "decisive_test"):
        out.append(Finding("E7", "error", "no decisive test: name the cheapest test that changes the decision."))
    if _filled(f, "accuracy") and not _filled(f, "baseline"):
        out.append(Finding("W1", "warning", "accuracy claim with no price-aware baseline."))
    if _filled(f, "access") and not _filled(f, "why_open"):
        out.append(Finding("W2", "warning", "access claim that does not say why it stays open."))
    if not _filled(f, "execution_net"):
        out.append(Finding("W3", "warning", "no execution net: spreads, impact, adverse drift and latency."))
    if risk and not (_answered(f, "holdable") and _answered(f, "co_losses")):
        out.append(Finding("W4", "warning", "risk claim that does not say whether the book can hold it through the "
                                            "bad state or what else loses with it."))
    return out


def main(argv: List[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        findings = lint(parse(fh.read()))
    if "--json" in argv:
        print(json.dumps([asdict(x) for x in findings], indent=1))
    else:
        for x in findings:
            print(f"{x.code} {x.severity}: {x.message}")
        print("clean" if not findings else f"{sum(x.severity == 'error' for x in findings)} errors, "
                                           f"{sum(x.severity == 'warning' for x in findings)} warnings")
    return 1 if any(x.severity == "error" for x in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
