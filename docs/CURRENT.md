# Current version

**Validator:** `packages/revenue-kb-v1.2/`
**Frozen:** 2026-08-06
**Status:** not accepted — the formal gate failed; used for live trials only.

## Files

| File | Role |
|---|---|
| `validator_prompt_v1_2.md` | prompt template, two placeholders |
| `knowledge_base.md` | source cards, closeness model, generalization classes |
| `pattern_cards.md` | recurring patterns with scope and transfer bans |
| `evidence_policy_rules.yaml` | machine-readable policy |
| `linter.py` | deterministic answer checker |
| `FREEZE_MANIFEST.md` | SHA-256 per file |

## History

| Version | What changed | Gate |
|---|---|---|
| V0 | first validator: money model and measurability | passed blind backtest |
| KB V0 | knowledge base, interstitials only | useful in 4 of 4 cases |
| V1 | revenue-wide knowledge base, closeness model | formal NO — one evidence-level mislabel |
| V1.1 | fixed level computation | formal FAIL — one over-broad generalization |
| V1.2 | scope annotations, mixed-evidence rule, linter | formal FAIL — the same defect class recurred |

The defect class that keeps failing: a one-sided claim about a class of
interventions where the corpus holds outcomes in both directions. A lexical
linter cannot close it — any paraphrase passes. The planned fix is semantic:
tag each claim with its class and compare its sign against the registry.
