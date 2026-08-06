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

Experiment 7622: ARPU read early +17.25%, read mature +22.8% and +24.2%.

## Why the validator needs this

So it can say which metric will still be immature when the decision is taken,
and by how much the early read is expected to be wrong.
