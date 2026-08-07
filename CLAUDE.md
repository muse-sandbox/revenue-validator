# Revenue Validator — working rules

This repository holds the pre-launch validator for revenue experiments: the frozen prompt bundles, the experiment knowledge base, and every evaluation run.

## Before anything else

Read `context/rules/` first. It describes how this team actually works — how long experiments run, who owns which metric, what the company currently optimizes for. Without those rules any critique of an experiment design is formally correct and practically useless.

`packages/current/` holds what the validator uses today — one version, one corpus, one policy. Everything else lives in `packages/history/` unchanged. A new version is a new directory in `current/` while the previous one moves to `history/`; never an edit to either. If `current/` ever holds two versions, something was left half-done.

The current validator here is `packages/current/version-revenue-kb-v1.2/`, but `docs/CURRENT.md` is the authority — v1.4 exists and has not been moved into this repository yet.

## Never do this

Do not read, quote, or pass to any model:

- `packages/current/corpus-revenue-v1/ground-truth-sealed/`
- `packages/history/corpus-interstitials/ground-truth-sealed/`
- `packages/history/input-validator-v0-unblind/ground-truth/`

These hold the actual outcomes of held-out experiments. Every blind comparison in this repository depends on the validator not seeing them before it commits to a recommendation. One leak invalidates the whole evaluation history.

Blind versions of the same cases live in `holdout-blind/` inside those packages and are safe to use as input.

## The package name states its kind

Every directory in `packages/` starts with its kind: `version-`, `corpus-`,
`run-`, `eval-`, `input-`, `policy-`. The prefix tells you what may flow into it
before you open it — a `run-` never reads sealed outcomes, an `eval-` may, and
only after the run's answers are frozen. Full rules: `docs/ARCHITECTURE.md`.

Renamed to this scheme on 2026-08-08. Frozen files still cite the old names and
must not be edited to fix that; `packages/README.md` holds the old→new table.

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
