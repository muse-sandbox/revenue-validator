# Decision criteria

What actually decides an experiment's fate here, as opposed to what the design
template asks for. Derived from the FLOW-650 answer key: twenty backtested
experiments, 2024-07 to 2026-05.

## What the twenty show

| Outcome | Count |
|---|---|
| rolled out | 10 |
| killed | 9 |
| inconclusive | 1 |

Where the decision is recorded — the two sources are not interchangeable:

| Source | Count | What it means |
|---|---|---|
| `admin rollout-variation` | 8 | a variation is flagged live in the admin; the document may say nothing |
| document verdict | 12 | a Decision section names the outcome, anchored on the experiment id |

A numeric guardrail was stated in **13 of 20**. The remaining 7 carried only a
qualitative one ("no measurable impact expected") or none at all.

A rationale was recorded in **19 of 20**. The exception, 4881, was rolled out to
all users with no fact recorded anywhere in the document and no reason given —
the Decision section was left as template text.

## Rules for the validator

- **Read the outcome from the admin flag, the rationale from the document.**
  They answer different questions. The flag is what happened; the document is
  what the team says it decided. Never infer one from the other.
- **A stated guardrail is not a decision rule.** In this set the guardrail is
  breached and the experiment still ships, or is untouched and the experiment
  is still killed — 7115 is the clean case: ARPU moved −0.06% against a −5%
  guardrail, formally intact, and it was killed on access conversion instead.
- **Absence of a numeric guardrail is a finding, not a formatting gap.** Seven
  of twenty had none. Say so; do not supply a typical threshold.
- **A decision without a recorded rationale is reportable on its own**,
  regardless of how the metrics moved.
- Do not rank options on a metric the Results section never measured. In 7430
  the design's own target metric was never computed, so plan and fact cannot be
  compared for it at all.

## Open questions

- What happens when the admin flag and the document verdict disagree. No case
  in the twenty settles it.
- Who is entitled to kill an experiment early, and whether that differs by team.
- Whether a breached guardrail ever blocked a rollout. Not observed here.

See also [`decision-timing.md`](decision-timing.md) for when the decision is
taken, and [`decision-practice.md`](decision-practice.md), which this file
supersedes for the criteria half of that TODO.
