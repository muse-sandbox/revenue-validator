# Synthetic answer — same conflict, declared as mixed evidence (selftest)

1. **Verdict** — launch with changes. Synthetic rationale.

[interpretation] Widget nudges have never lifted purchases in this corpus
[scope: widget nudges of any flavour; ids: T9-01, T9-02; not covered:
glow-button restyles, retention or engagement goals]. For this class the
evidence is mixed: the pull-down flavour did not earn money (T9-01, T9-02)
while one nudge with a changed offer did (T9-03), so the transfer boundary is
the offer change, not the nudge itself.

## Analogs

No direct analogs. The sources below are weak signals only.

```yaml
analog:
  source: T9-03 (synthetic; a widget nudge that earned money)
  axes:
    flow_stage: different
    segment: adjacent
    trigger_eligibility: different
    surface: different
    mechanism: different
    offer: different
    behavior: different
    metric: exact
    money_chain: different
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: different
  platform: different
  level: L3
  transferable: >
    [fact] Synthetic L3 sizing signal.
  not_transferable: >
    Any product conclusion; invented magnitudes.
```

## Non-monetization effects to instrument

- Retention both directions; instrument D1/D7; stop-rule invented.
