# How decisions are actually made

The interview half of the picture: what the owner of the decision says the rule
is. Source — UMN-12837, answered 2026-08-18 and 2026-08-20, plus the A/B
registry pull UG-328 (n = 54, app only, six months to 2026-08).

The measured half lives in [`decision-criteria.md`](decision-criteria.md) and
[`decision-timing.md`](decision-timing.md), derived from the FLOW-650 answer
key. Where the two do not line up, see "Reading this against the twenty" below.

## What is read at the moment of an early stop

Not the target metric. Proxies that predict revenue:

- access conversion;
- access mix — which products or plans the accesses land on;
- average access price.

They are compared against the model written before launch. The question asked at
that moment is *can this variation still win*, not *is this significant*.

**Significance is an input to the decision, not the criterion.** A rise that is
only close to significance ships when the impact forecast clears the money
threshold; the higher error probability is accepted explicitly rather than
argued away.

This explains the anomaly recorded in `decision-criteria.md` — an experiment
whose stated ARPU guardrail was formally intact and which was killed on access
conversion anyway. The document guardrail is not what is read. These three
proxies are.

## What counts as a drop bad enough to stop early

A loss larger than **$500 per platform per day scaled to full rollout**, judged
in the moment.

The threshold is monetary, not temporal. The day an experiment ends is a
consequence of how quickly that loss becomes visible at the traffic share in
use — which is why no fixed number of days appears anywhere in the answer.

The scaling formula from observed delta to full-rollout dollars is not defined
(Open questions). It is the single quantity that converts this rule into a date.

## What happens on growth

If the proxies track the model and the revenue upside is visible, the experiment
runs to its original plan. But a stable effect is also grounds to stop early:
*"we always traded power for the chance to roll out sooner and start earning."*

So the horizon is compressed in both directions — on a drop to stop losing
money, accepting false-negative risk, and on a rise to start earning sooner.
Nothing in the answer describes holding to the planned sample for accuracy.

## After the decision

| Outcome | Options |
|---|---|
| not a success | drop the idea, or run an improved iteration |
| success | roll out the winner and stop, or run another iteration to maximise the effect |

The improvement hypothesis in both branches comes from comparing the pre-launch
model against the fact — where the assumptions were wrong and what can be fixed.
That makes the quality of the original model an input to the next iteration
rather than paperwork; see
[`model-vs-fact-calibration.md`](model-vs-fact-calibration.md).

A fifth outcome is observed but not stated as a rule: **hypothesis confirmed,
not shipped** — results split across platforms plus a product constraint on one
of them.

**Iterations before an idea is dropped:** no formal limit, empirically about
three unsuccessful ones.

## What is guaranteed to be immature at decision time

Maturity is treated as binary. Either the decision is taken immediately — and
then none of the window metrics have matured — or it is taken after the whole
experimental cohort has matured. There is no described middle state where part
of the set is readable.

Not mature on a 3–8 day window: cancellations, trial-to-charge conversion,
alive14d, retention 7d and 14d.

Known error of reading early: on funnels with a trial step the early read
understates the effect by roughly a third — a mature ARPU read came out 1.3–1.4×
the early one in experiment 7622. That is one experiment, and the frequency of
such misses has never been measured: asked whether an early stop was ever known
to kill a working idea, the answer was *"we never asked ourselves that"*. Treat
the multiplier as the only available order-of-magnitude estimate, not as a
coefficient. Quantitative horizons per metric belong in
[`metric-maturity.md`](metric-maturity.md), still owned by analytics.

## Reading this against the twenty

The registry says the median experiment runs 7.5 days (8.0 adjusted for
restarts), P25–P75 4–12, and that 10 of 54 were stopped within three days. The
FLOW-650 twenty say the median is 14.9. Both are right, and the difference is
the useful part:

| Source | What it measures |
|---|---|
| UG-328, n = 54 | the marginal distribution — all app experiments in six months |
| FLOW-650, n = 20 | the same thing conditional on outcome, on a set selected roughly 50/50 killed and rolled out |

Duration is a function of the outcome, not a constant. Kills land around day
4–5; experiments that end in a rollout run several times longer. Selecting the
twenty half-and-half by outcome oversamples the long tail, which is why their
median is roughly double the registry's.

The operative shape for the validator is therefore two gates, not one number:

1. **The early kill screen**, days 3–5. Roughly one experiment in five does not
   survive it. Read by proxies against the model and by the $500 threshold.
2. **The full run**, for whatever gets past the screen and looks like a winner —
   two to three weeks, not one.

Add about four days on top for the gap between stop and rollout decision; the
full cycle to a shipping decision is around twelve days at the median.

## Rules for the validator

- **Predict the horizon from the outcome the design is aiming at.** Quoting a
  single median at a design that hopes to win is wrong in both directions:
  too long for the kill case, too short for the win case.
- **Name the three proxies explicitly** and check the experiment's tracking
  actually produces them. If it does not, the decision will be taken on the
  document guardrail or on nothing — that is a blocker, not a remark.
- **If the primary metric is in the immature list, say so in those words** —
  under this stopping rule that metric will not produce an answer — and name
  the proxy that will be read instead. Do not recompute power for it and stop
  there.
- **Classify what success means before judging the design.** Some experiments
  here are shipped on *not getting worse than the model allowed* — visual
  unification, technical replacement, reduced monetization pressure. Demanding
  an uplift from a non-inferiority experiment is a category error, and the
  design's own model states which case it is.
- **State the scaling assumption when using the $500 threshold**, since the
  formula is undefined. Never fold an unstated coefficient into a date.
- **Show the gap rather than hide it.** Report what a textbook power
  calculation would require alongside the horizon this team will actually give,
  and let the difference be the finding.

## Open questions

Five of these are open because they were never put to product — they dropped out
when FLOW-620 was transferred into UMN-12837 — not because an answer was
refused. All five close with one short follow-up.

| Question | Status |
|---|---|
| How many days until the first look, as distinct from the stop | never asked |
| Whether stopping halts enrollment only or measurement too | never asked |
| The formula scaling an observed delta to full-rollout dollars | never asked; see above |
| Who formally takes the decision | never asked; see [`team-ownership.md`](team-ownership.md) |
| How an exception is declared and who approves it | never asked |
| How often an early stop killed a working idea | answered "we never asked ourselves that" |

Exceptions exist but are described only as *"experiments with potential over a
longer horizon"*. There is no membership test for that class and no approval
path. The validator may propose that an experiment belongs to it, and must mark
the proposal as an assumption.
