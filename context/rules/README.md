# Domain rules

How this team actually works. The validator reads these files to judge an
experiment against reality rather than against a textbook design.

| File | Status | Owner |
|---|---|---|
| `decision-criteria.md` | filled | — |
| `decision-timing.md` | filled | — |
| `model-vs-fact-calibration.md` | filled | — |
| `decision-practice.md` | filled | — |
| `company-priorities.md` | **TODO** | product |
| `team-ownership.md` | **TODO** | product |
| `metric-maturity.md` | **TODO** | analytics |
| `closeness-model.md` | filled | — |
| `evidence-policy.md` | filled | — |
| `transfer-classes.md` | filled | — |

A file marked TODO is a known gap, not an oversight. The validator was rated
2 out of 5 on its first live case precisely because these rules did not exist:
it critiqued a 39-day design while the team stops experiments on day 3.

The three files at the top are backed by measurement rather than by interview:
all three are derived from the FLOW-650 answer key, twenty backtested
experiments spanning 2024-07 to 2026-05. Each one separates what the twenty
show from what the validator should therefore do, and closes with the questions
that evidence cannot settle. `decision-practice.md` holds the other half, the one the
backtest cannot reach: what is read at the moment of an early stop, and what
size of loss triggers it. It comes from the product interview UMN-12837
(2026-08-18 and 2026-08-20) and the registry pull UG-328, and it reconciles the
two duration figures — the registry median of 7.5 days and the twenty's 14.9 —
as one distribution seen marginally and conditionally on outcome.

Still unanswered there: who formally decides, and how an exception to the
stopping rule is approved. Both were simply never put to product and close with
one follow-up; `team-ownership.md` remains the file that owns the first.
