# Packages

Two directories. `current/` is what the validator uses today. `history/` is
everything that led here and must not be edited.

```
packages/
  current/     3 packages — the validator, its corpus, its policy
  history/    15 packages — older versions, and every run and evaluation
```

## current/

| Package | Kind | What it is |
|---|---|---|
| `version-revenue-kb-v1.2` | version | prompt, knowledge base, pattern cards, linter |
| `corpus-revenue-v1` | corpus | the 24-experiment inventory split into base and holdout |
| `policy-revenue-evidence-v1` | policy | what an analog gives you the right to claim |

> **v1.4 is the real current version** and is not in this repository yet — it
> still lives in a single copy outside git (FLOW-636). v1.2 is the newest
> version present here. `docs/CURRENT.md` is the authority on which is which.

## The current corpus, and what it is made of

`current/corpus-revenue-v1` starts from the FLOW-577 inventory: **24 completed
revenue experiments**, each verified against its Confluence page on 2026-08-04.

They split three ways by closeness to the anchor (the UG App monetization
interstitials family):

| Stratum | Meaning |
|---|---|
| type 1 | same surface and mechanic |
| type 2 | same user-flow stage, different surface |
| type 3 | same money metric, different flow or mechanic |

**6 went to the holdout, 18 went into the knowledge base.** The split was frozen
*before* the base was built — two most recent cases per stratum, chosen by launch
date alone, never by outcome.

### The 18 in the knowledge base

`T1-01` `T1-02` `T1-03` `T1-04` `T1-07` `T1-08` `T1-09` `T1-10`
`T2-01` `T2-02` `T2-05` `T2-06` `T2-07`
`T3-01` `T3-02` `T3-03` `T3-05` `T3-06`

Nine killed, eight rolled out, one stopped as inconclusive. From these 18 the
base also carries **14 pattern cards** (`P-01`…`P-14`) — recurring findings with
their scope and their transfer bans.

What the corpus records well: the *conditions* of each decision. What it barely
records: the *reasons*. Only two of the 18 quote the team verbatim. Closing that
is FLOW-635.

### The 6 in the holdout

`RH-01`…`RH-06`, blind versions in `holdout-blind/`, actual outcomes sealed in
`ground-truth-sealed/`. Source keys: `T1-05` `T1-06` `T2-03` `T2-04` `T3-04`
`T3-07`.

Four earlier cases — `T1-07`…`T1-10` — were deliberately *not* eligible for this
holdout: they had already served as the interstitials holdout and so had become a
development set. Reusing them would have measured memory, not judgement.

## history/

Older versions, the corpora they were built on, and every run and evaluation.
Kept because each evaluation verdict only means something next to the exact
inputs that produced it.

| Package | Kind |
|---|---|
| `version-revenue-kb-v1` · `version-revenue-kb-v1.1` | earlier validators |
| `version-interstitials-kb-v0` | the first knowledge base, interstitials only |
| `corpus-interstitials` | the corpus it was built on |
| `input-validator-v0-backtest` · `input-validator-v0-unblind` | V0 and its blind backtest |
| `run-interstitials-kb-ab` · `run-revenue-kb-v1-ab` | blind A/B runs |
| `run-revenue-kb-v1.1-regression` · `run-revenue-kb-v1.2-regression` | regressions |
| `run-live-official-tabs-v1.2` | the first run on a live experiment |
| `eval-*` | the verdict for each run above |

## The prefix is the kind

| Prefix | May read | May never read |
|---|---|---|
| `version-` | corpus knowledge sources | any holdout, any sealed outcome |
| `corpus-` | — | — |
| `run-` | a version + blind cards | sealed outcomes |
| `eval-` | everything, sealed outcomes included | — but only after run answers are frozen |
| `input-` | itself only | whatever its own README forbids |
| `policy-` | — | — |

Order: `corpus` → `version` → `run` → `eval`. Sealed outcomes enter at the last
step and never earlier.

## Renamed and split, 2026-08-08

Two changes on the same day: packages were renamed so the kind leads the name,
then split into `current/` and `history/`.

File contents were never touched. Integrity check after both changes: **377
manifest entries, 0 mismatches** — manifests hash file contents and list paths
relative to their own package, so neither the rename nor the move entered a
checksum.

What did go stale: prose cross-references inside frozen READMEs and manifests
pointing at a sibling by its old name and old place, such as
`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`. Those files are append-only
and were left unedited on purpose. Resolve them here.

| Old name | Now |
|---|---|
| `flow546-clean-input` | `history/input-validator-v0-backtest` |
| `flow565-evaluation-input` | `history/input-validator-v0-unblind` |
| `interstitials-corpus-prep` | `history/corpus-interstitials` |
| `interstitials-kb-v0` | `history/version-interstitials-kb-v0` |
| `interstitials-kb-ab-run` | `history/run-interstitials-kb-ab` |
| `interstitials-kb-evaluation` | `history/eval-interstitials-kb-ab` |
| `revenue-corpus-prep-v1` | `current/corpus-revenue-v1` |
| `revenue-evidence-policy-v1` | `current/policy-revenue-evidence-v1` |
| `revenue-kb-v1` | `history/version-revenue-kb-v1` |
| `revenue-kb-v1.1` | `history/version-revenue-kb-v1.1` |
| `revenue-kb-v1.2` | `current/version-revenue-kb-v1.2` |
| `revenue-kb-ab-run` | `history/run-revenue-kb-v1-ab` |
| `revenue-kb-evaluation` | `history/eval-revenue-kb-v1-ab` |
| `revenue-kb-v1.1-regression-run` | `history/run-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.1-regression-evaluation` | `history/eval-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.2-regression-run` | `history/run-revenue-kb-v1.2-regression` |
| `revenue-kb-v1.2-regression-evaluation` | `history/eval-revenue-kb-v1.2-regression` |
| `trial-run-815603314` | `history/run-live-official-tabs-v1.2` |

## When a new version arrives

1. Build it as `current/version-<area>-v<n>`.
2. Move the previous version to `history/`.
3. Update `docs/CURRENT.md` — it names the current version, nothing else does.

A version in `current/` never becomes two. If `current/` holds two versions,
something was left half-done.
