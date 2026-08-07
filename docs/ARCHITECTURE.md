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

Every directory under `packages/` is exactly one kind, and its name starts with
that kind. The prefix determines what may flow into it.

### 1. Version — a frozen validator

Prompt template, knowledge base, pattern cards, evidence policy, linter, and a
`FREEZE_MANIFEST.md` with SHA-256 per file. Runnable on its own.

`version-revenue-kb-v1` · `version-revenue-kb-v1.1` · `version-revenue-kb-v1.2` ·
`version-interstitials-kb-v0` · `input-validator-v0-backtest/validator-v0`

Not here yet: v1.3 and v1.4, still outside the repository (FLOW-636). They arrive
as `version-revenue-kb-v1.3` and `version-revenue-kb-v1.4`.

### 2. Corpus — cases split for honest evaluation

Three physically separate parts: `knowledge-sources/` feeds a version,
`holdout-blind/` feeds a run, `ground-truth-sealed/` feeds only an evaluation.
Plus an exclusion manifest and a leakage check.

`corpus-interstitials` · `corpus-revenue-v1`

### 3. Run — inference, no judgement

Verbatim answers, the exact inputs, a manifest with checksums of every frozen
file used. A run never opens outcomes and never decides which arm was better.

`run-interstitials-kb-ab` · `run-revenue-kb-v1-ab` ·
`run-revenue-kb-v1.1-regression` · `run-revenue-kb-v1.2-regression` ·
`run-live-official-tabs-v1.2` (+ the `-v1.3`, `-v1.3-run2`, `-v1.4` trials)

### 4. Evaluation — judgement against a pre-registered protocol

Scorecards, metrics, limitations, verdict. This is the only kind allowed to open
sealed outcomes, and only after the run's answers are frozen.

`eval-interstitials-kb-ab` · `eval-revenue-kb-v1-ab` ·
`eval-revenue-kb-v1.1-regression` · `eval-revenue-kb-v1.2-regression`

### 5. Input — a bundle handed to an isolated agent

`input-validator-v0-backtest` · `input-validator-v0-unblind`

Assembled so a clean-room agent needs to touch nothing else: everything it may
read, and nothing it may not. Each carries its own README stating what is
forbidden inside it — the unblind bundle, for instance, contains ground truth and
is therefore off limits to any run.

### 6. Policy — frozen evidence rules

`policy-revenue-evidence-v1`

Referenced by versions rather than copied into them, so a policy change is
visible as its own event.

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

**Naming — the kind comes first.** `<kind>-<area>-<version>[-<what>]`, as in
`eval-revenue-kb-v1.2-regression`. Six kinds: `version-`, `corpus-`, `run-`,
`eval-`, `input-`, `policy-`. Reading the prefix tells you what may flow into
that directory without opening it. Packages were renamed to this scheme on
2026-08-08; `packages/README.md` holds the old→new table, because frozen files
still cite the old names and may not be edited.

**Domain rules are input, not code.** `context/rules/` holds how the team
actually decides. Four of its seven files are still TODO, and that gap is the
documented reason the validator scored 2 of 5 on its first live case: it
critiqued a 39-day design while the team stops experiments on day 3.
