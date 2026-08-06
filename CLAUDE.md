# Revenue Validator — working rules

This repository holds the pre-launch validator for revenue experiments: the frozen prompt bundles, the experiment knowledge base, and every evaluation run.

## Before anything else

Read `context/rules/` first. It describes how this team actually works — how long experiments run, who owns which metric, what the company currently optimizes for. Without those rules any critique of an experiment design is formally correct and practically useless.

The current validator is `packages/revenue-kb-v1.2/`. Older versions stay in `packages/` unchanged; a new version means a new directory, never an edit to an existing one.

## Never do this

Do not read, quote, or pass to any model:

- `packages/revenue-corpus-prep-v1/ground-truth-sealed/`
- `packages/interstitials-corpus-prep/ground-truth-sealed/`
- `packages/flow565-evaluation-input/ground-truth/`

These hold the actual outcomes of held-out experiments. Every blind comparison in this repository depends on the validator not seeing them before it commits to a recommendation. One leak invalidates the whole evaluation history.

Blind versions of the same cases live in `holdout-blind/` inside those packages and are safe to use as input.

## Frozen packages are append-only

Every package carries a manifest with SHA-256 per file. Do not edit files inside a frozen package, do not move packages relative to each other — manifest paths are relative and siblings must stay siblings.

If a fix is needed, build a new versioned package and record what changed.

## Running the validator

See `docs/runbook.md`. In short: assemble the prompt template with a knowledge context and an experiment card, run it in a clean context with no search tools, then lint the answer.

Two rules that are easy to break:

- The run must not have access to the outcome of the experiment under review.
- Both arms of a comparison must use a byte-identical prompt; the only difference is presence of the knowledge context.

## Evidence discipline

These rules are enforced by the linter and must survive any change to the prompt:

- every claim about a past experiment cites a source ID that exists in the knowledge base;
- closeness level is computed from the analog's axis values, never chosen;
- only sign and mechanism transfer, and only from close analogs; magnitudes never transfer as predictions;
- when no close analog exists, the answer says so instead of promoting a weak one;
- a statement about a whole class carries an explicit scope annotation;
- when cited cases point in conflicting directions, the answer says the evidence is mixed and names the boundary.

## Known state

The validator is not frozen. The formal gate failed three times on one class of defect: one-sided generalizations over classes where the corpus evidence is mixed. Product usefulness was confirmed in all three runs, so the decision was to validate on live cases rather than keep iterating on the historical holdout.

Post-rollout causal revenue is missing for every experiment in the corpus. Any post-rollout figure in these documents is a forecast, not a measurement.
