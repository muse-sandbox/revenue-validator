# MAIN

## Verdict
**Redesign before launch** — the mechanic is worth running, but as sized the run cannot adjudicate its own guardrail, has no arm for the "preserve B" half of the goal, and enrolls on an unresolved exposure event.

## Findings

- **[stop]** [topic: retention-guardrail-noninferiority] The guardrail returns a pass for any retention loss up to 1.0 pp — twice the margin it is meant to police.
  `If:` the −0.5 pp working margin is approved and the readout uses the table's sizing.
  `Mechanism:` [computed] the guardrail row detects −2.37% of a 42.14% baseline, i.e. `42.14% × 2.37% ≈ 1.0 pp`, at 38,147/variation; halving that to 0.5 pp scales the sample by `(1.0/0.5)² = 4` → `38,147 × 4 ≈ 152,588` per variation and `39 × 4 ≈ 156` days.
  `Consequence:` a non-significant guardrail is compatible with a −0.9 pp loss; the pass is unfalsifiable.
  `Price:` decision impossible — the binding metric cannot fail at the threshold it is judged on.
  `Fix:` pre-register a non-inferiority rule on the CI lower bound and adopt 1.0 pp as the margin, or fund the 4× sample.

- **[stop]** [topic: missing-variation-b-arm] The "hold the B level" question ends up answered against a historical reading instead of a live arm.
  `If:` open decision 2 resolves as two arms.
  `Mechanism:` [computed] the card's own two mature ARPU readings for the same B differ by `24.2% − 22.8% = 1.4 pp`, and the design baseline `$0.68` differs from the control it is compared with, `$0.66`, by `$0.02`.
  `Consequence:` any ARPU between control and B is unattributable — demo dampening or drift.
  `Price:` experiment slot — the run answers the retention half only.
  `Fix:` add the B arm and re-size.

- **[stop]** [topic: exposure-event-split-enrollment] The population you size on and the population you read out end up different.
  `If:` the admin start event and the reach definition stay split (open decision 4).
  `Mechanism:` [computed] the guardrail is sized on a 42.14% retention baseline while the control it is compared against reads 37.58% — a `42.14 − 37.58 = 4.56 pp` gap, larger than the 1.0 pp the run must detect.
  `Consequence:` SRM checks and the #7622 baselines both stop being comparable.
  `Price:` experiment slot.
  `Fix:` fix one canonical event, rebuild reach and sizing on its denominator.

- **[improve]** [topic: chords-branch-dilution] The retention recovery shrinks to the share of the arm that actually sees a demo.
  `If:` nothing changes and both branches sit in one goal metric.
  `Mechanism:` [computed] at most `78% × (1 − 27%) ≈ 57%` of exposed users see the demo including Simplify, `22% × 7,700 ≈ 1,694` users/day get exactly variation B, and a 1.0 pp detectable change on everyone means `1.0 / 0.78 ≈ 1.28 pp` among treated users.
  `Consequence:` a real Chords-branch recovery reads as a smaller, likely non-significant arm-level number.
  `Price:` share of the expected effect — ~22% of the arm can only dilute it.
  `Fix:` pre-register the Chords branch as primary and re-size on it.

- **[improve]** [topic: arpu-regression-late-detection] A regression to control ARPU costs a full run before the guardrail reveals it.
  `If:` the demo dampens paywall pressure and only the 14d guardrail gates the run.
  `Mechanism:` [computed] `$0.77 − $0.66 = $0.11` per exposed user, over 38,147 exposed ≈ `$4,196`.
  `Consequence:` the loss is small in money, so speed — not cost — is the reason to stop early, and nothing stops it early.
  `Price:` money — ≈$4,196 at full regression.
  `Fix:` interim look on Retention 1d/7d and demo failure rate.

- **[improve]** [topic: retention-maturity-readout-lag] Day 39 in the design summary reads as the decision date, and the decision arrives on day 53.
  `If:` enrollment runs 39 days and Retention 14d is read on the last cohort.
  `Mechanism:` [computed] `39 + 14 = 53`.
  `Consequence:` slot and roadmap dates slip two weeks.
  `Price:` days to decision — 14 days.
  `Fix:` publish the readout date as enrollment stop + 14.

## What you decide
- **[product owner]** [topic: guardrail-margin-approval] Accept 1.0 pp as the margin this run can adjudicate, or pay for the 0.5 pp version.
- **[product owner]** [topic: third-arm-slot-cost] Decide whether "preserve B" is really the question; if yes, buy the third arm and the longer enrollment.
- **[analyst]** [topic: primary-population-chords] Fix the primary analysis population before launch: all exposed, or the Chords branch.
- **[analyst]** [topic: canonical-exposure-alignment] Pick the one exposure event and rebuild reach, sizing and SRM on it.

## Product proposals
`no grounded product proposal`
- **[ungrounded]** [topic: tabs-branch-untouched-segment] Whether the Tabs branch needs its own in-tab context (Smartscroll/Autoscroll) is unresearched here — the direction for that segment would have to be established first.
- **[ungrounded]** [topic: forced-tap-vs-skippable-demo] Whether a forced-tap demo beats a skippable one on retention is unestablished; the card's own note that Variation C's added information did not help leaves the mechanism open.

## Non-monetization effects to instrument
- [topic: tab-view-60s-post-paywall] Engagement can move both ways: a user who already knows the controls may cross 60s faster, or the 8-second Play may consume the novelty before the paywall. Instrument Tab View 60s by branch and by demo completion; stop-rule if the Chords branch falls below control on this transition.
- [topic: forced-step-frustration-signals] Disabled taps, play_interrupt and short dwell read as frustration or as confident speed. Instrument the dwell distribution, the fast-clicker slice, and app-background/kill during the demo (currently uncaptured); stop-rule on demo abandonment.
- [topic: refunds-after-demo-unlock] The temporary unlock may either set expectations that retain buyers or produce "features disappeared" refunds. Instrument refunds, cancellations and support tickets split by demo_unlock = 1/0.

## Predicted outcome
[hypothesis] ARPU lands between control and B, closer to B; retention recovers partially, most plausibly between −1.6 pp and −0.5 pp versus control — i.e. inside the noise band this design can resolve, so the guardrail likely reads "not significant" either way. It would surprise me to see retention at parity with control, or ARPU above B.

# APPENDIX

## B. Design & measurement checklist
- Goal metric vs touched surface: ARPU/exposed is measured on all exposed, but the intervention exists only in the Chords branch — declare the branch-level estimand explicitly.
- Exposure gate: reconcile "gift-offer close" with the App Experiment Start conditions (never subscribed, trial-eligible, tour not skipped); the eligible denominator differs.
- Reach vs duration consistency: 38,147 per variation over 39 days implies ≈978/variation/day, against a stated reach of ≈7,700/day — state the traffic allocation.
- SRM on the canonical event, plus an A/A window before the readout.
- Maturity: no Retention 14d readout before last-enrollment + 14 days; freeze the enrollment stop date.
- Comparability check: confirm the 78/22 format split is stable across arms (it is post-exposure and must not move).
- Guardrails to add: demo failure rate (`fallback = 'error'`), backing-track download failure, session abandonment inside the demo, refunds on demo_unlock purchases.
- Stop-rules: interim Retention 1d/7d; demo error rate above a pre-set threshold; ARPU below control at the first interim look.

## C. Design changes that would most improve expected value
1. Convert the retention guardrail to a pre-registered non-inferiority test with an approved margin, and align the sample to that margin (see [topic: retention-guardrail-noninferiority]).
2. Add the concurrent variation-B arm and re-size; without it the primary claim has no comparator (see [topic: missing-variation-b-arm]).
3. Pre-register the Chords branch as the primary analysis population with the Tabs branch as a declared A/A-style check (see [topic: chords-branch-dilution]).

## D. Findings without a price
- The doc states 39 days for the binding two-arm guardrail and ≈31 days for a three-arm version — the three-arm figure should be larger, not smaller; one of the two is stale.
- `from_tour` is not implemented on any app event today; the analytics spec depends on it for the whole demo funnel.
- The fast-clicker threshold on `dwell_ms` is left as "e.g."; it must be fixed before unblinding to avoid a post-hoc slice.
- The share of songs with none of the three features available is not stated, so the size of the fully-skipped sub-branch is unknown.
- `fallback = 'error'` vs `'unavailable'` must be separable in the readout, otherwise silent failures are counted as legitimate skips.

## E. Generic suggestions
- Freeze the analysis plan and decision rules before enrollment starts.
- Run an A/A on the new activation event before trusting the first readout.
- Keep the demo's feature unlock client-side only, and verify in QA that it never writes to user rights.
