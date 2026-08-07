# Packages

The prefix is the kind. Read it before opening anything.

| Prefix | Kind | May read | May never read |
|---|---|---|---|
| `version-` | a runnable frozen validator | corpus knowledge-sources | any holdout, any sealed outcome |
| `corpus-` | cases split for honest evaluation | — | — |
| `run-` | inference only, no judgement | a version + blind cards | sealed outcomes |
| `eval-` | judgement against a pre-registered protocol | everything, incl. sealed outcomes | — but only after run answers are frozen |
| `input-` | an assembled bundle handed to an isolated agent | itself only | whatever its own README forbids |
| `policy-` | frozen evidence policy | — | — |

Order: `corpus` → `version` → `run` → `eval`. Sealed outcomes enter at the last
step and never earlier.

## Current contents

| Package | Kind | What it is |
|---|---|---|
| `version-interstitials-kb-v0` | version | first knowledge base, interstitials only |
| `version-revenue-kb-v1` | version | revenue-wide base, closeness model |
| `version-revenue-kb-v1.1` | version | fixed closeness-level computation |
| `version-revenue-kb-v1.2` | version | scope annotations, mixed-evidence rule, linter |
| `corpus-interstitials` | corpus | interstitials split: sources, blind, sealed |
| `corpus-revenue-v1` | corpus | revenue-wide stratified holdout |
| `policy-revenue-evidence-v1` | policy | evidence policy V1 |
| `input-validator-v0-backtest` | input | V0 + 8 blind cards for the clean backtest |
| `input-validator-v0-unblind` | input | blind answers + ground truth for the unblind |
| `run-interstitials-kb-ab` | run | A/B on 4 interstitials holdout cases |
| `run-revenue-kb-v1-ab` | run | A/B on 6 revenue holdout cases |
| `run-revenue-kb-v1.1-regression` | run | regression after the level fix |
| `run-revenue-kb-v1.2-regression` | run | regression after the scope fix |
| `run-live-official-tabs-v1.2` | run | first run on a live, not-yet-launched experiment |
| `eval-interstitials-kb-ab` | eval | verdict on the interstitials A/B |
| `eval-revenue-kb-v1-ab` | eval | verdict on the revenue A/B |
| `eval-revenue-kb-v1.1-regression` | eval | verdict, formal FAIL |
| `eval-revenue-kb-v1.2-regression` | eval | verdict, formal FAIL, same defect class |

Missing here and still outside the repository: `version-revenue-kb-v1.3`,
`version-revenue-kb-v1.4`, and three live runs on Official Tabs. See
`docs/CURRENT.md` — moving them is FLOW-636.

## Renamed 2026-08-08 — old paths inside frozen files

Packages were renamed so the kind is readable without opening them. File
contents were not touched: every SHA-256 in every manifest still matches, because
manifests hash file contents and list paths relative to their own package.

What did become stale: prose cross-references inside frozen READMEs and manifests
that point at a sibling by its old name, such as
`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`. Those files are append-only
and were deliberately left unedited. Use this table to resolve them.

| Old name | New name |
|---|---|
| `flow546-clean-input` | `input-validator-v0-backtest` |
| `flow565-evaluation-input` | `input-validator-v0-unblind` |
| `interstitials-corpus-prep` | `corpus-interstitials` |
| `interstitials-kb-v0` | `version-interstitials-kb-v0` |
| `interstitials-kb-ab-run` | `run-interstitials-kb-ab` |
| `interstitials-kb-evaluation` | `eval-interstitials-kb-ab` |
| `revenue-corpus-prep-v1` | `corpus-revenue-v1` |
| `revenue-evidence-policy-v1` | `policy-revenue-evidence-v1` |
| `revenue-kb-v1` | `version-revenue-kb-v1` |
| `revenue-kb-v1.1` | `version-revenue-kb-v1.1` |
| `revenue-kb-v1.2` | `version-revenue-kb-v1.2` |
| `revenue-kb-ab-run` | `run-revenue-kb-v1-ab` |
| `revenue-kb-evaluation` | `eval-revenue-kb-v1-ab` |
| `revenue-kb-v1.1-regression-run` | `run-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.1-regression-evaluation` | `eval-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.2-regression-run` | `run-revenue-kb-v1.2-regression` |
| `revenue-kb-v1.2-regression-evaluation` | `eval-revenue-kb-v1.2-regression` |
| `trial-run-815603314` | `run-live-official-tabs-v1.2` |

New packages use the prefixed form from the start; this table stops growing.
