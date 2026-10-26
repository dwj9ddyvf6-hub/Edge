import json
import os
import unittest

import ledger_lint as ll

TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "edge-ledger.md")

COMPLETE = """
- **Access:** index trackers must buy at the effective-date close; positions this size are too small for large desks
- **Why it stays open:** capacity under $2M per event; mandate forces the trade at a known time
- **Variance:** inventory held from announcement to effective date
- **Shedder:** trackers who prefer certain execution at the close to tracking error
- **Premium:** 40 bps median per event in the replay, against a 25 bps reservation value
- **Bad state:** competitors front-run and the price reverses before the close; market drawdowns during the hold
- **Holdable:** yes, 3% of capital per event, no leverage
- **Co-losses:** the book's long-beta sleeves lose in the same drawdowns
- **Payer:** index trackers paying for immediacy at the close
- **Execution net:** 40 bps gross minus 12 bps spread and impact at the intended size
- **Evidence:** one pre-registered event study, no variants tried
- **Searched:** no
- **Decisive test:** forward shadow record of the next 30 events, paired against buying at the close
- **Kill rule:** retire if the mean net capture over 30 events is below 10 bps
"""


def codes(text):
    return {f.code for f in ll.lint(ll.parse(text))}


class Lint(unittest.TestCase):
    def test_complete_ledger_is_clean(self):
        self.assertEqual(codes(COMPLETE), set())

    def test_missing_payer(self):
        text = COMPLETE.replace("- **Payer:** index trackers paying for immediacy at the close", "- **Payer:** unknown")
        self.assertIn("E1", codes(text))

    def test_pattern_without_source(self):
        self.assertIn("E2", codes("Payer: momentum traders\nKill rule: x\nDecisive test: y\n"))

    def test_speed_without_lead_time(self):
        self.assertIn("E3", codes(COMPLETE + "\n- Speed: we read filings before the market\n"))
        self.assertNotIn("E3", codes(COMPLETE + "\n- Speed: filings\n- Lead time: 40 s before the price moves\n"))

    def test_risk_without_bad_state(self):
        text = COMPLETE.replace("- **Bad state:** competitors front-run and the price reverses before the close; "
                                "market drawdowns during the hold", "")
        self.assertIn("E4", codes(text))

    def test_searched_without_trials(self):
        self.assertIn("E5", codes(COMPLETE.replace("- **Searched:** no", "- **Searched:** yes")))
        searched_text = COMPLETE.replace("one pre-registered event study, no variants tried",
                                         "best of a grid over 400 settings")
        self.assertIn("E5", codes(searched_text))
        self.assertNotIn("E5", codes(searched_text + "\n- Trials: 400\n"))

    def test_kill_rule_and_test_required(self):
        text = COMPLETE.replace("- **Kill rule:**", "- Note:").replace("- **Decisive test:**", "- Note:")
        self.assertTrue({"E6", "E7"} <= codes(text))

    def test_no_counts_as_an_answer_for_holdable(self):
        text = COMPLETE.replace("- **Holdable:** yes, 3% of capital per event, no leverage", "- **Holdable:** no")
        self.assertNotIn("W4", codes(text))

    def test_warnings(self):
        self.assertIn("W1", codes(COMPLETE + "\n- Accuracy: better earnings model\n"))
        self.assertIn("W2", codes(COMPLETE.replace(
            "- **Why it stays open:** capacity under $2M per event; mandate forces the trade at a known time", "")))
        self.assertIn("W3", codes(COMPLETE.replace(
            "- **Execution net:** 40 bps gross minus 12 bps spread and impact at the intended size", "")))

    def test_json_input(self):
        data = {"payer": "hedgers", "Variance": "short index puts", "bad state": "crash", "kill_rule": "x",
                "decisive_test": "y", "execution net": "2 bps", "holdable": "yes", "co-losses": "long beta"}
        self.assertEqual({f.code for f in ll.lint(ll.parse(json.dumps(data)))}, set())

    def test_template_labels_are_all_recognised(self):
        with open(TEMPLATE, encoding="utf-8") as fh:
            rows = [line for line in fh if line.startswith("| ") and not line.startswith("| Field")]
        self.assertEqual(len(rows), 20)
        for row in rows:
            label = row.strip("|\n").split("|")[0]
            self.assertIsNotNone(ll._key(label), label)

    def test_unfilled_template_fails(self):
        with open(TEMPLATE, encoding="utf-8") as fh:
            found = codes(fh.read())
        self.assertTrue({"E1", "E2", "E6", "E7"} <= found)

    def test_filled_table_row(self):
        text = "| Payer | Who pays us? | trackers at the close |\n| Kill rule | ? | net < 10 bps over 30 events |"
        fields = ll.parse(text)
        self.assertEqual(fields["payer"], "trackers at the close")
        self.assertEqual(fields["kill_rule"], "net < 10 bps over 30 events")


if __name__ == "__main__":
    unittest.main()
