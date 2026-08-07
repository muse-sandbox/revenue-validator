---
name: holdout-discipline
description: Rules for keeping evaluations honest — which files must never reach a model, how to prepare a blind case, and what invalidates a run. Use before any evaluation, backtest, regression or A/B comparison in this repository.
---

# Holdout discipline

## Never pass these to a model

- `packages/current/corpus-revenue-v1/ground-truth-sealed/`
- `packages/history/corpus-interstitials/ground-truth-sealed/`
- `packages/history/input-validator-v0-unblind/ground-truth/`

They contain actual outcomes of held-out experiments. Passing them to a
validator run destroys the only property that makes the evaluation meaningful.

Safe inputs are in `holdout-blind/` inside the same packages.

## Order that must hold

1. Reserve the test cases and freeze the list.
2. Build the knowledge base from the remaining cases only.
3. Blind the test cases: remove results, decisions, rollout status, outcome
   hints in titles, and post-launch edits.
4. Run inference. Freeze the answers and their checksums.
5. Only then open the outcomes.

Building the knowledge base first and choosing the holdout afterwards
invalidates everything downstream.

## What makes a run invalid

- Checksums of frozen inputs do not match the manifest.
- The prompt or the knowledge base changed after freezing.
- Outcomes were readable during inference.
- The same context both generated the answers and judged them.
- The arms differ by anything other than the presence of the knowledge context.

## Repeated runs are not independent tests

Re-running a fixed version on the same holdout is a regression test of the fix,
not a fresh measurement of usefulness. Each repetition leaks a little more of
that holdout into the prompt. After two rounds of fixes on the same cases,
treat them as a development set.

## Separate contexts

Build, blind inference, and unblind evaluation run in three separate contexts.
A context that has seen outcomes never produces answers afterwards.
