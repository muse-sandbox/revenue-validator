# Architecture

Who does what, what a package is, and what the validator can and cannot see.

## The one thing to know first

**The validator talks to nothing.** No tools, no search, no Confluence, no
analytics agent, no database. One run sees exactly two texts: the assembled
prompt (knowledge base + pattern cards) and the experiment card under review.

This is deliberate, not missing work. A run that could reach the outcome of the
experiment it is reviewing would invalidate every blind comparison in this
repository. The isolation is enforced in three places — prompt rule 9,
`docs/runbook.md`, and the launch flags (`--strict-mcp-config` with an empty MCP
config, everything in `--disallowed-tools`).

**The cost of that isolation:** anything requiring data — actual enrolment rate,
real reach, metric maturity, whether a segment is large enough — the validator
cannot check. It can only name the suspicion. Confirming it is a human or
analytics job, done separately.

## Division of labour

Two agents, no channel between them. Handoff is a human carrying a document.

| Stage | Owner | Why |
|---|---|---|
| Was this tried before? | analytics (`hypothesis-librarian`) | The validator has no registry of hypotheses, only a corpus of finished experiments |
| Is the mechanic right, on the right segment, what does the corpus say | **validator** | Its core and only uncontested job |
| First alarm on design, from the card text alone | **validator** | Cheap, caught immediately, no data needed |
| Verify the alarm, recompute bases, real reach, effect size | analytics (`ug-experiment-design-power`) | Needs the warehouse |
| Slot placement, collisions | analytics (`experiment-slot-planner`) | A blocking "add arm B" may be unschedulable |
| Instrumentation, cohort and exposure events | analytics (`experiment-event-audit`) | The validator writes generalities here; the analyst has a checklist |
| Experiment health while running | analytics | Validator not involved |
| Result analysis, slices | analytics | Validator not involved |
| Feed the outcome back into the corpus | **nobody yet** | Known gap |

The analytics agent lives in a separate repository (`claude-ug-manipulator`) with
its own skills. It is not importable from here and holds no credentials this
repository may use.

## What a package is

Every directory under `packages/` is exactly one of four kinds. The kind
determines what may flow into it.

### 1. Version — a frozen validator

Prompt template, knowledge base, pattern cards, evidence policy, linter, and a
`FREEZE_MANIFEST.md` with SHA-256 per file. Runnable on its own.

`revenue-kb-v1` · `revenue-kb-v1.1` · `revenue-kb-v1.2` · `revenue-kb-v1.3` ·
`revenue-kb-v1.4` · `interstitials-kb-v0` · `flow546-clean-input/validator-v0`

### 2. Corpus — cases split for honest evaluation

Three physically separate parts: `knowledge-sources/` feeds a version,
`holdout-blind/` feeds a run, `ground-truth-sealed/` feeds only an evaluation.
Plus an exclusion manifest and a leakage check.

`interstitials-corpus-prep` · `revenue-corpus-prep-v1`

### 3. Run — inference, no judgement

Verbatim answers, the exact inputs, a manifest with checksums of every frozen
file used. A run never opens outcomes and never decides which arm was better.

`interstitials-kb-ab-run` · `revenue-kb-ab-run` ·
`revenue-kb-v1.1-regression-run` · `revenue-kb-v1.2-regression-run` ·
`trial-run-815603314` (+ the `-v1.3`, `-v1.3-run2`, `-v1.4` trials)

### 4. Evaluation — judgement against a pre-registered protocol

Scorecards, metrics, limitations, verdict. This is the only kind allowed to open
sealed outcomes, and only after the run's answers are frozen.

`interstitials-kb-evaluation` · `revenue-kb-evaluation` ·
`revenue-kb-v1.1-regression-evaluation` · `revenue-kb-v1.2-regression-evaluation`

### Two exceptions

`flow546-clean-input` and `flow565-evaluation-input` are named after the task
that produced them rather than their role. Both are assembled inputs for a clean
run — a bundle handed to an isolated agent so it need not touch anything else.
Kept under their original names because manifests of completed runs cite those
paths.

## Flow

```
corpus ──knowledge-sources──> version ──┐
   │                                    ├──> run ──> evaluation
   └──holdout-blind────────────────────-┘             ▲
                                                      │
   └──ground-truth-sealed────────────────────────────-┘
                                    (only here, only after answers are frozen)
```

Reading the diagram backwards is the leak: sealed outcomes must never reach a
version or a run.

## Rules that hold everything together

**Append-only.** A frozen package is never edited. A fix means a new versioned
directory. Manifest paths are relative, so packages must stay siblings.

**One version at a time is current.** `docs/CURRENT.md` names it. Nothing else
does — not this file, not the README, not a Linear issue.

**Naming.** `<area>-<version>[-<role>]`, as in
`revenue-kb-v1.2-regression-evaluation`. The role suffix is what makes the kind
readable without opening the directory.

**Domain rules are input, not code.** `context/rules/` holds how the team
actually decides. Four of its seven files are still TODO, and that gap is the
documented reason the validator scored 2 of 5 on its first live case: it
critiqued a 39-day design while the team stops experiments on day 3.
