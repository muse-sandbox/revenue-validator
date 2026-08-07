# Current version

**Validator:** `revenue-kb-v1.4/` — see the location warning below
**Frozen:** 2026-08-07
**Status:** not accepted — the formal gate has never passed; used for live trials only.

> ⚠️ **v1.3 and v1.4 are not in this repository yet.** They live in a single copy at
> `~/Documents/Codex/2026-08-03/users-elzira-obsidian-ug-ai-infrastructure/outputs/`,
> together with the trial runs `trial-run-815603314-v1.3`, `-v1.3-run2` and `-v1.4`.
> Consolidating them is FLOW-636. Until then `packages/` stops at v1.2.

## Where we are

The money model works. The product judgement half-works. Ranking candidates
against each other has not started.

Current work is the quality of the answer (M3): making critiques name a product
consequence and a price rather than a property of the document. After that comes
the shadow pilot on three live hypotheses, and the freeze happens on its results
— not before. That order was reversed on 6 August because three gate failures in
a row were failures of the formal criterion, not of product usefulness.

Plan and progress: [Linear project](https://linear.app/asteroids-infra/project/ai-revenue-decision-loop-validator-denezhnyh-gipotez-231007a9bbcd)

## Files in a version bundle

| File | Role |
|---|---|
| `validator_prompt_v1_4.md` | prompt template, two placeholders |
| `knowledge_base.md` | source cards, closeness model, generalization classes |
| `pattern_cards.md` | recurring patterns with scope and transfer bans |
| `evidence_policy.md` + `evidence_policy_rules.yaml` | policy, human and machine readable |
| `linter.py` + `linter_selftest.py` + `selftest_fixtures/` | deterministic answer checker |
| `FREEZE_MANIFEST.md` | SHA-256 per file |

## History

| Version | What it fixed | Gate |
|---|---|---|
| V0 | money model and measurability | passed blind backtest |
| KB V0 | knowledge base, interstitials only | useful in 4 of 4 cases |
| V1 | revenue-wide knowledge base, closeness model | formal NO — one evidence-level mislabel |
| V1.1 | fixed level computation | formal FAIL — one over-broad generalization |
| V1.2 | scope annotations, mixed-evidence rule, linter | formal FAIL — the same defect class recurred |
| V1.3 | opened a channel for product knowledge that the base already held but the format never surfaced | live trials only |
| V1.4 | added `[computed]` — claims derived from the reviewed card's own numbers, so a stop-level statement is possible without a close analog | live trials only |

## Open defects

**The recurring gate failure.** A one-sided claim about a class of interventions
where the corpus holds outcomes in both directions. A lexical linter cannot close
it — any paraphrase passes. The planned fix is semantic: tag each claim with its
class and compare its sign against a registry (FLOW-611).

**Review takes 30–55 minutes** against a target of 10. This blocks the shadow
pilot: with that length the team will not read the recommendations, and the pilot
would measure the format rather than the advice (FLOW-609).

**Four of seven `context/rules/` files are still TODO.** The validator scored
2 of 5 on its first live case because of exactly this (FLOW-619).

**No post-rollout causal revenue exists** for any experiment in the corpus. Every
post-rollout figure in these documents is a forecast, not a measurement
(FLOW-605).

## Rule

When the version changes, this file is what gets edited. Not the README, not an
issue description.
