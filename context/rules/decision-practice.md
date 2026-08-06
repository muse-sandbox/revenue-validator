# How decisions are actually made

> **TODO.** This file is empty and it is the single largest gap in the
> validator's context. Fill it before the next live run.

## What must be answered here

- How many days an experiment actually runs before the first decision.
- Which metric is read at that moment, and what counts as a drop bad enough
  to stop early.
- What happens on growth: how much longer it runs and what is decided then.
- Whether stopping means stopping enrollment only, or stopping measurement too.
- Which metrics are guaranteed to be immature at decision time.
- Whether exceptions to the rule exist, and who approves them.

## Already known

In experiment 7622 the early read gave ARPU +17.25% while mature reads gave
+22.8% and +24.2%. On funnels with a trial step, an early read understates the
effect by roughly a third. This is a known error of the stopping rule, not a
reason to abandon it.

## Why the validator needs this

So it can say "under your stopping rule this metric will not produce an answer"
instead of recomputing power for a design that will never run.
