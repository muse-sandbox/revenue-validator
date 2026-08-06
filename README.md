# Revenue Validator

Pre-launch validator for revenue experiments at Ultimate Guitar. It reviews an experiment card before the team spends one of its limited experiment slots and returns a recommendation: launch, revise, or deprioritize.

> **Internal repository.** Contains real revenue figures, conversion rates, experiment outcomes and links to internal Confluence. Do not mirror, fork outside the organization, or paste contents into external services.

## Start here

| If you want to | Read |
|---|---|
| understand the rules an agent must follow | `CLAUDE.md` |
| run the validator on an experiment | `.claude/skills/validator-run/` |
| run an evaluation without breaking it | `.claude/skills/holdout-discipline/` |
| know how this team actually works | `context/rules/` |
| see a worked example | `packages/trial-run-815603314/` |

## ⚠️ Sealed outcomes

Three directories hold the actual results of held-out experiments and must never reach a model:

- `packages/revenue-corpus-prep-v1/ground-truth-sealed/`
- `packages/interstitials-corpus-prep/ground-truth-sealed/`
- `packages/flow565-evaluation-input/ground-truth/`

Every blind comparison in this repository depends on the validator not seeing them before committing to a recommendation. Blind versions of the same cases, safe as input, are in `holdout-blind/` inside those packages.

## Layout

```text
CLAUDE.md              rules for any agent working here
context/
  rules/               how this team decides, what it owns, what the company optimizes for
.claude/skills/        procedures: running the validator, keeping evaluations honest
docs/                  runbook and version pointer
packages/              versioned, frozen, append-only artifacts
worktree-recovered/    files that existed only inside isolated task worktrees
```

### packages/

Current validator: **`revenue-kb-v1.2/`** — prompt, knowledge base, pattern cards, evidence policy, linter.

| Package | What it is |
|---|---|
| `revenue-kb-v1.2/` `revenue-kb-v1.1/` `revenue-kb-v1/` | validator versions, newest first |
| `interstitials-kb-v0/` | first knowledge base, interstitials only |
| `revenue-corpus-prep-v1/` `interstitials-corpus-prep/` | holdouts: blind cards, sealed outcomes, evaluation protocol |
| `revenue-kb-ab-run/` `interstitials-kb-ab-run/` | blind A/B runs |
| `revenue-kb-v1.1-regression-*` `revenue-kb-v1.2-regression-*` | regression runs and their evaluations |
| `flow546-clean-input/` `flow565-evaluation-input/` | Validator V0 and its blind backtest |
| `revenue-evidence-policy-v1/` | evidence policy |
| `trial-run-815603314/` | first run on a live, not-yet-launched experiment |

Packages are append-only and their checksum manifests use relative paths, so they must stay siblings. A new version means a new directory, never an edit.

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

Every frozen package carries a manifest with SHA-256 per file. The last full verification covered 9 manifests and 185 entries with no mismatches.
