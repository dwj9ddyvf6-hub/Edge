# Paired shadow experiment: <arm name>

The incumbent keeps trading unchanged. This arm runs as a counterfactual on the same signals, the same capital and the
desk's real fills, beside a seeded placebo. Rules: [research-protocol.md](../references/research-protocol.md#11-paired-shadow-experiments).

| Field | Entry |
|---|---|
| Incumbent | Sleeve, version and timing authority |
| What changes | One conceptual change |
| What stays the same | Signals, capital, universe, clock, costs model |
| Expected result if right | Direction and size on the decision metric |
| Rival explanation | What else would produce the same result |
| Placebo | The seeded arm that controls for the rival |
| Metric | Net per opportunity, with no-fills at cash value; markouts; drawdown |
| Rejection rule | For example: rejected if, over at least 200 paired entries, the mean saving net of costs is under 5 bps |
| Minimum sample | Paired observations before any review; descriptive until then, and labelled so |
| Live-path guard | Test that the incumbent's intents and orders are identical with the arm present |
| Review date and owner | Who decides promotion, and when |
