# Current version

**Validator:** `packages/current/version-revenue-kb-v1.6/`
**Frozen:** 2026-08-08 (FLOW-641)
**Status:** not accepted — the formal gate has never passed; used for live trials only.

Consolidated into this repository on 2026-08-11 together with v1.5, the two
Official Tabs runs on those bundles, and the first live run on a second case
(`history/run-live-premium-default-v1.6`). v1.4 moved to `history/`. Integrity
after the move: 666 manifest entries, 0 mismatches; the V1.6 linter selftest is
GREEN on 239 checks.

The earlier consolidation was 2026-08-08 (FLOW-636): v1.3, v1.4 and the three
live runs on Official Tabs, 480 manifest entries, 0 mismatches.

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
| `validator_prompt_v1_6.md` | prompt template, two placeholders |
| `README.md` | what this version fixed and why |
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
| V1.5 | rule 13 — every finding names what the reader gets instead of an answer and what it costs, in one of five price units; findings ranked by that price, at most three blocking | live trials only |
| V1.6 | rules 14–16 — the conditional form *if X, grounded in Y, then Z*, one topic per bullet with no duplicate topics, and advice that would fit any experiment moved out of the main answer | live trials only |

## Open defects

**The recurring gate failure.** A one-sided claim about a class of interventions
where the corpus holds outcomes in both directions. A lexical linter cannot close
it — any paraphrase passes. The planned fix is semantic: tag each claim with its
class and compare its sign against a registry (FLOW-611).

**The §2.8 expression scanner breaks on the currency symbol.** Introduced in
V1.4 and untouched since: an arithmetic run written with `$` is not parsed, so a
`[computed]` statement whose operation is shown and correct still fails with
`E_COMPUTED_NO_OPERATION` or `E_COMPUTED_NUMBER_FABRICATED`. It produced 5 of 5
errors in arm A of the Official Tabs V1.6 run and both errors of the
premium-default V1.6 run. Notational, and it needs its own task — it is not part
of rules 14–16.

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
