# Synthetic answer — four grounded proposals (selftest)

1. **Verdict** — launch with changes. Synthetic rationale.

## Product proposals

- **[mechanic]** Passive toast instead of an interrupt — grounded in T9-01.
  Expected direction: invented metric up.
- **[segment]** Split the readout by synthetic cohort — grounded in T9-02.
  Expected direction: cleaner readout, no goal-metric change.
- **[offer]** Keep the offer unchanged and move the surface — grounded in
  P-90. Expected direction: invented metric flat.
- **[mechanic]** Delay the widget by one screen — grounded in T9-01 and
  P-90. Expected direction: invented metric up.

## Analogs

```yaml
analog:
  source: T9-01 (synthetic; SRM ok; significant-positive)
  axes:
    flow_stage: exact
    segment: adjacent
    trigger_eligibility: exact
    surface: adjacent          # imaginary banner vs imaginary toast
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

```yaml
analog:
  source: T9-02 (synthetic; SRM ok; significant-negative)
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: exact
    surface: different         # imaginary plan menu vs imaginary toast
    mechanism: exact
    offer: adjacent
    behavior: adjacent
    metric: exact
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Synthetic source moved the invented metric down. [hypothesis] A
    warning of the same sign for the new synthetic case.
  not_transferable: >
    All invented magnitudes; the synthetic menu context.
```

## Non-monetization effects to instrument

- Retention could shift in either direction; instrument D1/D7; stop-rule at
  a significant D1 drop.
- Refunds could fall (positive side-effect) or rise; instrument refund 14d.
