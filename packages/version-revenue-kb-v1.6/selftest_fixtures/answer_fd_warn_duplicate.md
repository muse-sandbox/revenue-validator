# MAIN

## Verdict
Redesign before launch. Synthetic rationale for the selftest.

## Findings

- **[stop]** We spend the slot and come back with a guardrail read that cannot clear this launch. *Mechanism:* [computed] the guardrail resolves 4.2 pp while the margin the team approved is 1.5 pp, so 4.2 / 1.5 = 2.8 times that margin. *Consequence:* a non-significant guardrail stays compatible with almost three times the loss the team said it would accept, so the guardrail condition cannot be declared met on any outcome. *Price:* decision impossible — the question this design was built to settle stays open whatever the numbers say. *Fix:* re-size on the approved margin before launch.

- **[stop]** We lose most of the effect before it reaches the measurement. *Mechanism:* [computed] 64% × (1 − 25%) ≈ 48% of the test arm can actually reach the widget, so a true +30% on those users arrives in the overall metric as 48% × 30% ≈ 14%. *Consequence:* the read lands near the 3 pp this design resolves, so a null would not tell the team the widget did nothing. *Price:* share of the expected effect — half of the lift never reaches the metric the decision is made on.

- **[improve]** The team waits two extra weeks before it can act on the read. *Mechanism:* the synthetic retention guardrail needs a maturity horizon of 14 days that the current plan does not schedule. *Consequence:* the decision slides into the next planning cycle. *Price:* days to decision — calendar only, the answer itself is unchanged.

## What you decide

- **[product owner]** Whether a guardrail that cannot clear the launch is
  still worth the slot this quarter.
- **[analyst]** Whether the guardrail is re-sized on the approved margin, or
  the margin is changed openly instead.

## Product proposals

no grounded product proposal — nothing in the synthetic base covers this
mechanic closely enough.

- **[ungrounded]** Whether an invented toast placed after the synthetic
  surface would keep the metric is not covered by any source here; it needs
  its own test rather than a recommendation.

## Non-monetization effects to instrument

- Retention could shift in either direction; instrument D1/D7; stop-rule at
  a significant D1 drop.
- Refunds could fall (positive side-effect) or rise; instrument refund 14d.
- The read lands near the 3 pp this design resolves, so a null would not tell the team anything; instrument the branch share.

## Closest analogs

There are no direct analogs for this synthetic case.

## Predicted outcome

[hypothesis] The invented metric moves up slightly against control, with wide
uncertainty in both directions.

# APPENDIX

## B. Design & measurement checklist

- Synthetic checklist item for the selftest.

## D. Findings without a price

- The activation event is not named in the document; ask for it before the
  first user is bucketed.
