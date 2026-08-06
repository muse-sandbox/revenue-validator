# Revenue Validator

Pre-launch validator for revenue experiments at Ultimate Guitar. It reviews an experiment card before the team spends one of its limited experiment slots, and returns a recommendation: launch, revise, or deprioritize.

This repository is the consolidated archive of the project: frozen validator bundles, the experiment knowledge base, evaluation runs and their results.

> **Internal repository.** Contains real revenue figures, conversion rates, experiment outcomes and links to internal Confluence. Do not mirror, fork outside the organization, or paste contents into external services.

---

## ⚠️ Before you use anything here with an AI agent

Two directories must never be passed to a validator run:

| Path | Why |
|---|---|
| `artifacts/revenue-corpus-prep-v1/ground-truth-sealed/` | actual outcomes of the holdout experiments |
| `artifacts/interstitials-corpus-prep/ground-truth-sealed/` | same, for the interstitials test |

The whole evaluation design depends on the validator never seeing outcomes before it commits to a recommendation. Feeding these files to an agent invalidates every blind comparison in this repository.

The blind versions of the same cases — safe to use as input — are in `holdout-blind/` inside those packages.

---

## What state the project is in

The validator is designed in three parts.

| Part | Status |
|---|---|
| Money model and measurability check | **Works.** Verified blind on 8 completed experiments: material risks found in all 3 unsuccessful cases, no successful idea rejected |
| Product assessment from experiment history | **Partial.** The knowledge base reliably improves experiment design and measurement. Predicting whether the idea itself will make money is weakly supported so far |
| Ranking candidates against each other | **Not started.** Requires a business threshold for slot value and simultaneous comparison of several hypotheses |

Not frozen yet. The formal gate failed three times on a single class of defect — one-sided generalizations over a class where the corpus evidence is mixed. Product usefulness was confirmed in all three runs, so the decision was to stop iterating on the historical holdout and validate on live cases instead.

**Known limitation.** Post-rollout causal revenue is missing for every experiment in the corpus: once a change is rolled out to 100% there is no control group left. Every post-rollout number in these documents is a forecast, not a measurement.

---

## Layout

```
artifacts/
  revenue-kb-v1.2/              current validator: prompt, KB, pattern cards, policy, linter
  revenue-kb-v1.1/              previous version
  revenue-kb-v1/                first revenue-wide knowledge base
  interstitials-kb-v0/          first knowledge base, interstitials only
  revenue-corpus-prep-v1/       stratified holdout, blind cards, sealed outcomes, protocol
  interstitials-corpus-prep/    same for the interstitials test
  revenue-kb-ab-run/            blind A/B on 6 held-out cases
  revenue-kb-v1.1-regression-*/ regression run and its evaluation
  revenue-kb-v1.2-regression-*/ regression run and its evaluation
  interstitials-kb-ab-run/      blind A/B on 4 held-out cases
  interstitials-kb-evaluation/  human-readable evaluation of that test
  flow546-clean-input/          frozen Validator V0 and its blind input pack
  flow565-evaluation-input/     V0 blind outputs and sealed outcomes
  revenue-evidence-policy-v1/   evidence policy
  trial-run-815603314/          first run on a live, not-yet-launched experiment

worktree-recovered/
  files that existed only inside isolated task worktrees and were not published
  anywhere else — stage reports, extraction outputs, Confluence snapshots
```

Package paths inside checksum manifests are relative, so packages must stay siblings of each other.

---

## Running the validator

The prompt is a template with two placeholders.

```
artifacts/revenue-kb-v1.2/validator_prompt_v1_2.md
    {KNOWLEDGE_CONTEXT}   ->  knowledge_base.md + pattern_cards.md
    {EXPERIMENT_CARD}     ->  the experiment document under review
```

Assemble one file, run it in a clean context with no search tools and no access to the outcome of the experiment under review, then check the answer:

```bash
python3 artifacts/revenue-kb-v1.2/linter.py ANSWER.md \
  --kb artifacts/revenue-kb-v1.2/knowledge_base.md \
  --patterns artifacts/revenue-kb-v1.2/pattern_cards.md
```

Add `--no-kb-arm` when the run had no knowledge context. The linter recomputes closeness levels from the answer's own analog cards and flags unqualified generalizations.

A worked example — inputs, outputs and manifest — is in `artifacts/trial-run-815603314/`.

---

## Integrity

Every frozen package carries a manifest with SHA-256 for each file. The last full verification covered 9 manifests and 185 entries with no mismatches.

Frozen packages are append-only: a new version means a new directory, never an edit of an existing one.

---

## Known open issues

- Review of one answer takes 30–55 minutes against a target of 10. The output format needs restructuring, not only shortening.
- The validator has no knowledge of how the team actually decides: experiments are held 3 days and stopped on revenue, 7 days if growing. Its critique assumes a textbook design that does not exist in practice.
- Analog cards are written in a machine-readable format that a human cannot read comfortably.
- Recommendations are not tied to an expected effect size, so it is unclear which of them matter.
