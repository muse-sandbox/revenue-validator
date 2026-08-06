## 1. Verdict

**Redesign before launch.** The product idea (richer, extensible top-of-discovery surface) is worth testing, but the current design cannot produce a decision-grade read: power is computed from aspirational targets (92%/40% lift) giving 2–4-day runs, exposure is counted at the wrong event, the goal metric mixes monetizing and non-monetizing cards, and the biggest downside risk — reach loss on the demoted Spotify tile — is not what the primary metric watches.

## 2. Predicted outcome

[hypothesis] Total access CR moves little or not at all — far below the 92% (Android) / 40% (iOS) modeled targets — because iteration 1 changes format only, not offers, and attention-format lifts have not translated into purchases on similar App exposure surfaces where measured (T1-09, T2-02, P-03). There is a real chance of a *negative* money read: the Spotify tile converts 8–8.8% of viewers today with guaranteed first-viewport visibility, and in treatment it is visible only after a swipe or 8 seconds of auto-advance — the model assumes its view→click *rises* to 10% while its effective reach collapses (P-01). What would surprise me: a clean, mature, significant ARPU gain inside one week.

## 3. Top risks & failure modes

- **Reach demotion of the highest-CTR component.** Value of an S3–S4 surface scales with reach (P-01, T1-04); the carousel cuts guaranteed visibility of the Spotify offer to ~1-in-4 rotation. The model's flat click→access assumption hides this.
- **Net increment, not gross clicks.** Two of four cards (tuner, courses) monetize nothing directly and will divert taps from the discount card; existing tiles carry real incremental value that does not redistribute when degraded (T2-01, P-02). Read the showcase as net increment vs control across all paywall sources.
- **Power built on the wish, not the decision.** A 2-day Android run detects only a 92% lift; any realistic smaller effect returns an uninterpretable null (P-12 flavor). One week also cannot mature trial→charge for ARPU (P-13).
- **Exposure mis-gated.** Exposure fires at tour-end banner dismiss, not at showcase view — dilution plus an activation mismatch; SRM must be checked at the actual view event (P-11, P-12).
- **Hypothesis–mechanics mismatch.** The +65% ARPU rationale cites personalization, but iteration 1 shows identical static cards to everyone. Attention/engagement gains are not purchase intent (P-03, T1-09); expectations should be reset before launch, not after.

## 4. Analogs

Ranked by closeness. No conflicts between the retrieved analogs.

```yaml
analog:
  source: T2-01 (ab 6293; 2025-07; SRM ok; significant-negative on turn-off; killed — surfaces kept)
  axes:
    flow_stage: exact            # S3–S4 passive exposure on discovery/Explore
    segment: adjacent            # all free vs free new post-tour
    trigger_eligibility: adjacent
    surface: exact               # discovery-screen sale banner/tile area in both
    mechanism: different         # surface OFF (gating) vs tile→carousel format replacement
    offer: exact                 # same seasonal discount offers, unchanged
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: different    # surface existence vs view→click improvement
  platform: exact
  level: L2
  transferable: >
    [fact] Turning off the sale banner + splash significantly reduced ARPU on
    both platforms; conversion did NOT fully redistribute to other surfaces
    (T2-01, significant-negative). [hypothesis] The discount tile being
    replaced is load-bearing; degrading its effective visibility inside a
    four-card rotation risks a net revenue LOSS, not merely a missed gain.
    Warning-level only (L2).
  not_transferable: >
    Magnitudes (ARPU −11.6% iOS / −26% Android, charge CR −38.1% Android) are
    seasonal-sale and config-specific — sizing prior at most. The source
    measured full removal, not partial demotion; harm from demotion is a
    transfer hypothesis. Splash-only-off was n.s., so component values differ.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact            # S3–S4 exposure
    segment: exact               # free new post-tour in both
    trigger_eligibility: adjacent
    surface: different           # interstitial slot vs persistent discovery tile
    mechanism: adjacent          # gamified engagement format vs carousel format change
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact        # both act on the exposure→click/access link
  platform: exact
  level: L3
  transferable: >
    L3 — guardrail and sizing lessons only. [fact] Forcing exposure
    (non-skippable) multiplied engagement and layer revenue but cost Android
    D1 retention significantly, on this same new post-tour segment; relative
    lifts were large while absolute $/day increment was small (T1-07).
    [hypothesis, L3 lesson] Arm C's 8-second auto-advance needs a D1/D7
    retention guardrail and an absolute-$ sizing check, not just relative CR.
  not_transferable: >
    All magnitudes (+26.5% ARPU, D1 −9.15%, +$474/day forecast); interstitial
    dynamics; var2 internal anomalies. Mixed/killed source — no product
    conclusion transfers, and L3 cannot ground a verdict change.
```

```yaml
analog:
  source: T1-04 (ab 6359/6416/6428; 2025-07..08; SRM ok; mixed; rolled-out Android)
  axes:
    flow_stage: exact
    segment: adjacent            # free + ex-paid mixed vs free new
    trigger_eligibility: adjacent
    surface: different           # interstitial slot vs discovery tile
    mechanism: adjacent          # replace-slot-with-richer-creative vs reformat existing tiles
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    L3 — measurement/sizing lessons only. [fact] The same treatment was pure
    increment on Android but cannibalized other sources on iOS (segment
    without interstitial accesses −24.7%), because platform inventory context
    differed (T1-04). [hypothesis, L3 lesson] Read platforms separately and
    measure cannibalization of other paywall entry points explicitly.
  not_transferable: >
    All magnitudes (+17–19% Android ARPU); the Android rollout conclusion;
    ad-inventory-specific cannibalization shares.
```

## Non-monetization effects to instrument

- **Engagement, positive side:** tuner and course cards may lift feature adoption and new-user activation (tuner opens, course starts, sessions D1–D7). Instrument per-card downstream engagement, not just clicks.
- **Engagement, negative side:** a moving carousel (arm C) at the top of discovery may distract from core content — instrument song/tab opens from discovery per session vs control.
- **Retention both directions:** better free-tool discovery could *raise* D1/D7; forced motion could *lower* it (T1-07 L3 lesson, same segment). Stop-rule: significant D1 retention drop in arm C.
- **Spotify funnel:** connection-flow entries and completions vs control; stop-rule on a volume floor.
- **Refunds/cancels:** 14-day cancels/refunds on showcase-attributed purchases (impulse-click quality check).

## 6. Design & measurement checklist

- Scope the goal metric to showcase-attributed access and net revenue, with Total ARPU and other-paywall-source volume as guardrails (P-11); don't blend monetizing and non-monetizing cards into one CR.
- Gate exposure/activation on the actual showcase-view event; run SRM at randomization *and* at view (P-12, P-14).
- Re-power on a decision-relevant MDE (10–20% on source access CR, not 92%); run ≥2 weeks and let trial windows mature before any charge/ARPU conclusion or rollout (P-13); no early rollout on interim reads (T2-02 lesson).
- Verify delivery: arm C auto-advance actually firing, both platforms live, per-position shown/hidden flags populated (P-12). Analyze platforms separately (T1-04 L3).
- January launch: confirm the seasonal discount creative is identical and live in all arms for the whole run.
- Keep post-purchase users (switched back to control layout) in intent-to-treat analysis.

## 7. Changes that would most improve expected value

1. **Re-found the power calculation and runtime** on a realistic MDE for showcase-source access CR; the current 2–4-day design mostly guarantees an uninterpretable result.
2. **Protect or explicitly test the Spotify tile's reach:** pin it first-position for a sub-arm, or declare its reach loss a measured question with its own success threshold — don't let the model's flat-conversion assumption absorb it.
3. **Reframe the hypothesis honestly for iteration 1:** a format/throughput test (view→click per position) with a realistic ARPU expectation, deferring the personalization claim to the iteration that actually personalizes.
