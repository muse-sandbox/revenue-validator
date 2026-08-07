# Revenue Validator

Pre-launch validator for revenue experiments at Ultimate Guitar. It reviews an experiment card before the team spends one of its limited experiment slots and returns a recommendation: launch, revise, or deprioritize.

> **Internal repository.** Contains real revenue figures, conversion rates, experiment outcomes and links to internal Confluence. Do not mirror, fork outside the organization, or paste contents into external services.

**Plan and progress live in Linear:**
[AI Revenue Decision Loop — валидатор денежных гипотез](https://linear.app/asteroids-infra/project/ai-revenue-decision-loop-validator-denezhnyh-gipotez-231007a9bbcd)

## Start here

| If you want to | Read |
|---|---|
| know where the project stands right now | `docs/CURRENT.md` |
| understand who does what, and what a package is | `docs/ARCHITECTURE.md` |
| see what is planned and in progress | the Linear project linked above |
| understand the rules an agent must follow | `CLAUDE.md` |
| run the validator on an experiment | `.claude/skills/validator-run/` |
| run an evaluation without breaking it | `.claude/skills/holdout-discipline/` |
| know how this team actually works | `context/rules/` |
| see a worked example | `packages/history/run-live-official-tabs-v1.2/` |

## ⚠️ Sealed outcomes

Three directories hold the actual results of held-out experiments and must never reach a model:

- `packages/current/corpus-revenue-v1/ground-truth-sealed/`
- `packages/history/corpus-interstitials/ground-truth-sealed/`
- `packages/history/input-validator-v0-unblind/ground-truth/`

Every blind comparison in this repository depends on the validator not seeing them before committing to a recommendation. Blind versions of the same cases, safe as input, are in `holdout-blind/` inside those packages.

## Layout

```text
CLAUDE.md              rules for any agent working here
context/
  rules/               how this team decides, what it owns, what the company optimizes for
.claude/skills/        procedures: running the validator, keeping evaluations honest
docs/                  runbook and version pointer
packages/
  current/             the validator in use, its corpus, its policy
  history/             older versions, and every run and evaluation
worktree-recovered/    files that existed only inside isolated task worktrees
```

### packages/

Current validator: see `docs/CURRENT.md` — it is the single place that names the
current version. As of 2026-08-08 that is **v1.4**, which has not been moved into
this repository yet (FLOW-636); `packages/` here stops at `version-revenue-kb-v1.2/`.

Two directories, and the name of each package starts with its kind:

```text
packages/
  current/    the validator in use, its corpus, its policy — 3 packages
  history/    older versions, and every run and evaluation — 15 packages
```

| Prefix | Kind |
|---|---|
| `version-` | a runnable frozen validator |
| `corpus-` | cases split for honest evaluation |
| `run-` | inference only, no judgement |
| `eval-` | judgement against a pre-registered protocol |
| `input-` | a bundle handed to an isolated agent |
| `policy-` | frozen evidence rules |

What `current/` holds and what the corpus is made of: `packages/README.md`.
What may flow into what: `docs/ARCHITECTURE.md`.

Packages are append-only. A new version means a new directory in `current/` and
the previous one moving to `history/` — never an edit to either.

## Project state

| Part | Status |
|---|---|
| Money model and measurability check | **Works.** Verified blind on 8 completed experiments: material risks found in all 3 unsuccessful cases, no successful idea rejected |
| Product assessment from experiment history | **Partial.** Reliably improves experiment design; predicting whether an idea will make money is weakly supported so far |
| Ranking candidates against each other | **Not started.** Needs a business threshold for slot value and simultaneous comparison of hypotheses |

Not frozen. The formal gate failed three times on one class of defect — one-sided generalizations over classes where the corpus evidence is mixed. Product usefulness was confirmed in all three runs, so the decision was to validate on live cases instead of iterating further on the historical holdout.

## Known gaps

- **`context/rules/` is half empty.** Four files are marked TODO. The validator was rated 2 out of 5 on its first live case because of exactly this: it critiqued a 39-day design while the team stops experiments on day 3.
- **Review takes 30–55 minutes** against a target of 10. The output format needs restructuring, not only shortening.
- **Analog cards are machine-readable**, which the linter needs and a human does not.
- **Recommendations carry no expected effect size**, so it is unclear which of them matter.
- **Post-rollout causal revenue is missing** for every experiment in the corpus: after a 100% rollout no control group remains. Every post-rollout figure here is a forecast, not a measurement.

## Integrity

Every frozen package carries a manifest with SHA-256 per file. Last full verification: 2026-08-08, **377 entries, 0 mismatches** — run after the packages were renamed and split, to prove neither touched a file.
