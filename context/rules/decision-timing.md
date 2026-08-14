# Decision timing

How long experiments actually run before they are decided. Derived from the
FLOW-650 answer key: twenty backtested experiments, actual durations read from
`mysql_u_guitarcom.ab_experiment_history` lifecycle events, not from the plan.

## What the twenty show

Actual duration in days, by outcome:

| Outcome | Median | Range |
|---|---|---|
| killed | **4.6** | 1.1 – 42.8 |
| rolled out | **18.5** | 7.1 – 62.9 |
| inconclusive (n=1) | 7.8 | — |
| all twenty | 14.9 | 1.1 – 62.9 |

Five experiments were stopped before day 5 — 7115 (1.1), 5652 (1.7), 7379
(2.0), 7607 (3.7), 6314 (4.6). **All five were killed.** Nothing in this set
was rolled out on the evidence of fewer than seven days.

Planned versus actual, for the 11 experiments whose plan states a single number:

| Ran shorter than planned | Ran at or past plan |
|---|---|
| 3 — 7115 (11% of plan), 6314 (31%), 7241 (39%) | 8 — from 7604 (92%) to 7472 (568%) |

Three experiments state no planned duration at all (5529, 5652, 4881); five
state it per platform, so a single ratio does not apply.

## Rules for the validator

- **Do not critique a design for being short against a textbook duration.**
  The operative comparison is against this team's own practice: a kill decision
  at day 3–5 is normal here, not a defect. This is the specific failure that
  scored the validator 2 out of 5 on its first live case.
- **A short run is a power statement, not a duration statement.** 7115 ran 1.1
  of 10 planned days and collected 2 407 users against a design sample of
  343 020 per variation. Its "ARPU did not move" is absence of data, not
  evidence of no effect. Say that, rather than reading the flat result.
- **Running past the plan is the more common deviation** — 8 of 11. Do not
  assume an overrun was deliberate; the plan is often simply not enforced.
- Where the plan states duration per platform, compare per platform. Do not
  collapse to one number.
- Never fill a missing planned duration with a typical value. Three of twenty
  have none, and that blank is itself the finding.

## Open questions

- Which metric is read at the moment of an early stop, and what size of drop
  triggers it. Not recoverable from the answer key.
- Whether stopping means halting enrollment only or measurement too.
- Whether weekly seasonality is deliberately covered — only 7430 says so
  explicitly (2 computed days extended to 7).

See also [`decision-criteria.md`](decision-criteria.md) for what the decision is
based on, and [`metric-maturity.md`](metric-maturity.md) — still TODO, owned by
analytics — for how long each metric needs before it can be read at all. Those
two are different questions: this file records when the team *does* decide,
not when a metric *may* be read.
