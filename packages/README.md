# packages/

Здесь лежит **только запускаемый валидатор**: текущая замороженная версия и
policy, на которую она ссылается.

| Директория | Тип | Что это |
|---|---|---|
| `version-revenue-kb-v1.6/` | version | промпт, база знаний, карточки паттернов, evidence policy, линтер, манифест заморозки |
| `policy-revenue-evidence-v1/` | policy | замороженные правила работы с доказательствами |

Корпус (`corpus-`), прогоны (`run-`), оценки (`eval-`), входные пакеты (`input-`)
и все прошлые версии живут в рабочей папке вне репозитория —
`VALIDATOR_WORK_DIR`, по умолчанию `revenue-validator-work` рядом с ним.
Таблица переименований пакетов от 2026-08-08 (замороженные файлы ссылаются на
старые имена) лежит там же, вместе с пакетами, которых она касается.

---

## Прежнее описание (до разделения репозитория и рабочей папки)

# Packages

Two directories. `current/` is what the validator uses today. `history/` is
everything that led here and must not be edited.

```
packages/
  current/     3 packages — the validator, its corpus, its policy
  history/    25 packages — older versions, and every run and evaluation
```

## current/

| Package | Kind | What it is |
|---|---|---|
| `version-revenue-kb-v1.6` | version | prompt, knowledge base, pattern cards, evidence policy, linter |
| `corpus-revenue-v1` | corpus | the 24-experiment inventory split into base and holdout |
| `policy-revenue-evidence-v1` | policy | what an analog gives you the right to claim |

v1.3, v1.4 and the three live Official Tabs runs were consolidated here on
2026-08-08 (FLOW-636); v1.5, v1.6 and three more live runs on 2026-08-11.
Nothing of this project now exists in a single copy outside git.
`docs/CURRENT.md` remains the authority on which version is current.

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

The corpus cards record the *conditions* of each decision and only two of the 18
quote the team verbatim — but that is an artefact of how the cards were built.
FLOW-635 went back to the source pages: 16 of 18 state the grounds for the
decision explicitly, 13 also explain the mechanism. The reasoning was there and
was lost when the conclusions section was compressed to one line.

Verbatim sections, the quality assessment and the corrected fifteen-rule set:
`analysis/flow635-decision-rationales/`. Folding those rules into the knowledge
base is FLOW-644.

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
| `version-revenue-kb-v1` · `-v1.1` · `-v1.2` · `-v1.3` · `-v1.4` · `-v1.5` | earlier validators |
| `version-interstitials-kb-v0` | the first knowledge base, interstitials only |
| `corpus-interstitials` | the corpus it was built on |
| `input-validator-v0-backtest` · `input-validator-v0-unblind` | V0 and its blind backtest |
| `run-interstitials-kb-ab` · `run-revenue-kb-v1-ab` | blind A/B runs |
| `run-revenue-kb-v1.1-regression` · `run-revenue-kb-v1.2-regression` | regressions |
| `run-live-official-tabs-v1.2` | the first run on a live experiment |
| `run-live-official-tabs-v1.3` · `-v1.3-run2` · `-v1.4` · `-v1.5` · `-v1.6` | later runs on the same live case |
| `run-live-premium-default-v1.6` | the first run on a second live case, arm B only |
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

File contents were never touched. Integrity check after the rename, the split and
the consolidation of v1.3/v1.4: **480 manifest entries, 0 mismatches** — manifests
hash file contents and list paths relative to their own package, so neither the
rename nor the move entered a checksum.

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
| `revenue-kb-v1.2` | `history/version-revenue-kb-v1.2` |
| `revenue-kb-ab-run` | `history/run-revenue-kb-v1-ab` |
| `revenue-kb-evaluation` | `history/eval-revenue-kb-v1-ab` |
| `revenue-kb-v1.1-regression-run` | `history/run-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.1-regression-evaluation` | `history/eval-revenue-kb-v1.1-regression` |
| `revenue-kb-v1.2-regression-run` | `history/run-revenue-kb-v1.2-regression` |
| `revenue-kb-v1.2-regression-evaluation` | `history/eval-revenue-kb-v1.2-regression` |
| `trial-run-815603314` | `history/run-live-official-tabs-v1.2` |
| `revenue-kb-v1.3` | `history/version-revenue-kb-v1.3` |
| `revenue-kb-v1.4` | `current/version-revenue-kb-v1.4` |
| `trial-run-815603314-v1.3` | `history/run-live-official-tabs-v1.3` |
| `trial-run-815603314-v1.3-run2` | `history/run-live-official-tabs-v1.3-run2` |
| `trial-run-815603314-v1.4` | `history/run-live-official-tabs-v1.4` |

## Consolidated, 2026-08-11

v1.5 and v1.6 and the runs made on them, until then the last artefacts of this
project living in a single copy outside git.

| Old name, in `…/outputs/` | Now |
|---|---|
| `revenue-kb-v1.5` | `history/version-revenue-kb-v1.5` |
| `revenue-kb-v1.6` | `current/version-revenue-kb-v1.6` |
| `trial-run-815603314-v1.5` | `history/run-live-official-tabs-v1.5` |
| `trial-run-815603314-v1.6` | `history/run-live-official-tabs-v1.6` |
| `trial-run-828875488-v1.6` | `history/run-live-premium-default-v1.6` |

`current/version-revenue-kb-v1.4` moved to `history/` on the same day, per the
rule below. `__pycache__` directories were not copied; nothing else was touched.

Integrity across every manifest in `packages/`: **666 entries, 0 mismatches**.
22 manifest lines name a path that does not resolve — 8 are the virtual
`KNOWLEDGE_CONTEXT` concatenation, which is a hash of two files joined in
memory and never a file on disk, and 14 are the same class of stale sibling
cross-reference the rename left behind: a `run-live-*` manifest points at its
bundle as `../revenue-kb-v1.5/…` or `../revenue-kb-v1.6/…`. Read those as
`../../history/version-revenue-kb-v1.5/…` and
`../../current/version-revenue-kb-v1.6/…`. The frozen files stay unedited.

## When a new version arrives

1. Build it as `current/version-<area>-v<n>`.
2. Move the previous version to `history/`.
3. Update `docs/CURRENT.md` — it names the current version, nothing else does.

A version in `current/` never becomes two. If `current/` holds two versions,
something was left half-done.
