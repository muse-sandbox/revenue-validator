# Metric maturity

> **TODO.** Likely filled by analytics.

## What must be answered here

- Days after entry before each metric can be read: trial conversion,
  trial to charge, ARPU, retention 7d and 14d, refunds, reconversion.
- Share of charges still pending at 3, 7 and 14 days.
- How much an early read distorts each metric, and on which funnel shapes
  the distortion is largest.
- Whether maturity differs between iOS and Android.
- At what share of pending charges a result becomes usable for a decision.

## Already known

Experiment 7622: ARPU read early +17.25%, read mature +22.8% and +24.2% —
a mature-to-early ratio of 1.3–1.4 on a funnel with a trial step.

Product treats maturity as binary: either the decision is taken immediately and
nothing in the window has matured, or it is taken after the whole cohort has.
Not mature on a 3–8 day window: cancellations, trial-to-charge, alive14d,
retention 7d and 14d. Source and caveats in
[`decision-practice.md`](decision-practice.md). What is still missing here is
the quantitative part — days per metric, pending share at 3/7/14 days, and
whether any of it differs between iOS and Android.

## Why the validator needs this

So it can say which metric will still be immature when the decision is taken,
and by how much the early read is expected to be wrong.
