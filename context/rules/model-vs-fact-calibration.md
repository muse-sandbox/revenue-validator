# Model vs fact calibration

How far the planned effect has historically stood from the measured one, and
what the validator may therefore do with a number taken from a model. Derived
from the FLOW-650 answer key: twenty backtested experiments, block 3
`plan_vs_fact_by_metric`.

## Coverage first

| Plan↔fact pairs across the twenty | 81 |
|---|---|
| pairs where a fact exists at all | 23 (28%) |
| pairs comparable numerically (numeric plan **and** fact) | 21 (26%) |

Three quarters of what the documents plan was never measured against a fact.
Any statement about calibration rests on 21 pairs, not on twenty experiments.

## What the 21 comparable pairs show

Of the 21, five state a plan of exactly `0.0` ("no effect expected"). The
remaining **16 carry a directional prediction**:

| | Count |
|---|---|
| direction predicted correctly | **6 of 16** |
| direction wrong (moved the opposite way) | 10 of 16 |

Magnitude, split by what was predicted:

- **11 pairs predicted growth. None reached it.** The closest was 7379 Android
  ARPU at +9.5% against a planned +28% — 34% of the model. The furthest was
  7379 iOS ARPPU at +1.3% against a planned +120%, overstated ~93×. Five of the
  eleven (all of 4806) moved *down* while the model predicted +50% to +75%.
- **4 pairs predicted a decline.** Two fell further than planned (5193 Android
  ARPU −13.5% vs −6.6%; 7034 ARPU −8.9% vs −5.0%), two rose instead (5193 iOS,
  7115 ARPU +4.5% vs a planned −5.0%).
- **5 pairs predicted nothing** (`0.0`) and moved between −7.7% and +7.0%.

## Rules for the validator

- **A planned lift is not a prediction and must never be quoted as one.** On
  this evidence it gets the direction right in fewer than half of the cases
  that state a direction, and has never once reached a predicted growth figure.
- **Overstatement is the norm and it is large.** Treat a model's growth number
  as an upper bound with at least an order of magnitude of slack, and say so
  explicitly whenever the number is used for sizing.
- **A model predicting `0.0` does not license "no effect".** Those five pairs
  still moved several percent in both directions.
- **Never compute a plan↔fact delta where the fact is missing** — that is 58 of
  81 pairs. `actual_source: "не рассчитано"` means no comparison exists, not
  zero.
- Compare per platform. Where a plan is stated per platform (4806, 7379, 7607)
  iOS and Android diverged in both size and sign.
- Units do not travel with the number. `planned_lift_pct` in the answer key
  holds percentages, percentage points, plain strings and per-variation objects;
  read the unit from the source text before comparing anything.

## Open questions

- Why growth models overstate so consistently — audience dilution, an optimistic
  baseline, or the model period never matching the run. Not separable here.
- Whether the six correct-direction cases share anything (all but one are ARPPU
  or a decline prediction; n is too small to call).
- No calibration exists for money-per-day forecasts: `plan_vs_fact_money_per_day`
  carries the string `"см. block2"` as its actual value in every file examined.

See also [`closeness-model.md`](closeness-model.md) — its hard rule that effect
magnitudes never transfer as predictions is the same rule seen from the analog
side; this file is the measured backing for it.
