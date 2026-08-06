# Synthetic answer — all three L2 branches valid (selftest)

1. **Verdict** — launch with changes. Synthetic rationale.

## Analogs

Branch A: mechanism exact, surface different.

```yaml
analog:
  source: T9-01 (synthetic)
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: exact
    surface: different
    mechanism: exact
    offer: exact
    behavior: exact
    metric: exact
    money_chain: exact
    guardrails: exact
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [hypothesis] Synthetic hypothesis-or-warning transfer.
  not_transferable: >
    Invented magnitudes; surface-specific reach figures.
```

Branch B: surface+flow_stage exact, mechanism different.

```yaml
analog:
  source: T9-02 (synthetic)
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: exact
    surface: exact
    mechanism: different
    offer: adjacent
    behavior: exact
    metric: exact
    money_chain: exact
    guardrails: exact
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [hypothesis] Synthetic same-surface different-mechanism warning.
  not_transferable: >
    Invented magnitudes; mechanism-specific conclusions.
```

Branch C, segment variant: L1 conditions except monetization state.

```yaml
analog:
  source: T9-01 (synthetic)
  axes:
    flow_stage: exact
    segment: different
    trigger_eligibility: exact
    surface: exact
    mechanism: exact
    offer: exact
    behavior: exact
    metric: exact
    money_chain: exact
    guardrails: exact
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [hypothesis] Synthetic cross-segment hypothesis.
  not_transferable: >
    Segment-state-specific conclusions; invented magnitudes.
```

Branch C, platform variant: L1 conditions except platform.

```yaml
analog:
  source: T9-02 (synthetic)
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: exact
    surface: exact
    mechanism: exact
    offer: exact
    behavior: exact
    metric: exact
    money_chain: exact
    guardrails: exact
  segment_monetization_state: exact
  money_chain_link: exact
  platform: different          # platform-specific mechanism
  level: L2
  transferable: >
    [hypothesis] Synthetic cross-platform hypothesis.
  not_transferable: >
    Platform-specific mechanics; invented magnitudes.
```

## Non-monetization effects to instrument

- Engagement may rise or fall; instrument feature usage; stop-rule invented.
- Upper-funnel could improve (positive side-effect); instrument tab visits.
