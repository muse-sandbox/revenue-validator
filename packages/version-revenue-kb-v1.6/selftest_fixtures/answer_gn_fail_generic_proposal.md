# MAIN

## Verdict
Redesign before launch. Synthetic rationale for the selftest.

## Findings

- **[stop]** [topic: guardrail-margin-synthetic] We spend the slot and come back with a guardrail read that cannot clear this launch. *If:* nothing changes and the guardrail keeps the approved margin. *Mechanism:* [computed] the guardrail resolves 4.2 pp while the margin the team approved is 1.5 pp, so 4.2 / 1.5 = 2.8 times that margin. *Consequence:* a non-significant guardrail stays compatible with almost three times the loss the team said it would accept, so the guardrail condition cannot be declared met on any outcome. *Price:* decision impossible — the question this design was built to settle stays open whatever the numbers say. *Fix:* re-size the guardrail on the approved 1.5 pp margin before launch.

- **[stop]** [topic: widget-dilution-hidden-branch] We lose most of the effect before it reaches the measurement. *If:* the goal metric stays the invented metric over the whole arm. *Mechanism:* [computed] 64% × (1 − 25%) ≈ 48% of the test arm can actually reach the widget, so a true +30% on those users arrives in the overall metric as 48% × 30% ≈ 14%. *Consequence:* the read lands near the 3 pp this design resolves, so a null would not tell the team the widget did nothing. *Price:* share of the expected effect — half of the lift never reaches the metric the decision is made on.

- **[improve]** [topic: maturity-horizon-retention] The team waits two extra weeks before it can act on the read. *If:* the retention guardrail is read at the same time as the primary metric. *Mechanism:* [hypothesis] the synthetic retention guardrail needs a maturity horizon of 14 days that the current plan does not schedule. *Consequence:* the decision slides into the next planning cycle. *Price:* days to decision — calendar only, the answer itself is unchanged.

## What you decide

- **[product owner]** Whether a guardrail that cannot clear the launch is
  still worth the slot this quarter.
- **[analyst]** Whether the guardrail is re-sized on the approved margin, or
  the margin is changed openly instead.

## Product proposals

- **[mechanic]** [topic: passive-toast-synthetic-surface] *If:* we make the invented widget more visible on the 64% branch. *Grounds:* [interpretation] T9-01 (L1 card below) read its own lift as coming from the passive form rather than from the offer. *Then:* the invented metric moves up on the exposed users.
- **[segment]** [topic: synthetic-cohort-readout] *If:* the synthetic cohort is read out separately before any rollout, against the 3 pp this design resolves. *Grounds:* [fact] P-90 covers this synthetic surface and records the same split. *Then:* the goal metric is unchanged, the readout is cleaner.

## Non-monetization effects to instrument

- [topic: retention-both-directions] Retention could shift in either
  direction; instrument D1/D7; stop-rule at a significant D1 drop.
- [topic: refunds-after-widget] Refunds could fall (positive side-effect) or
  rise; instrument refund 14d.

## Closest analogs

- T9-01 is the closest synthetic source: the same invented mechanism on the
  same invented surface, differing only in platform.

## Predicted outcome

[hypothesis] The invented metric moves up slightly against control, with wide
uncertainty in both directions.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T9-01 (synthetic; SRM ok; significant-positive)
  axes:
    flow_stage: exact
    segment: adjacent
    trigger_eligibility: exact
    surface: adjacent
    mechanism: exact
    offer: exact
    behavior: adjacent
    metric: exact
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L1
  transferable: >
    [fact] Synthetic source moved the invented metric up. [hypothesis] The
    new synthetic case may move in the same direction.
  not_transferable: >
    All invented magnitudes; anything outside the synthetic transfer bounds.
```

## B. Design & measurement checklist

- Synthetic checklist item for the selftest.

## D. Findings without a price

- The activation event is not named in the document; ask for it before the
  first user is bucketed.
