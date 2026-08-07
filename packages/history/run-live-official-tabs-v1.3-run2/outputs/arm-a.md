# MAIN

## Verdict
**Redesign before launch** — both success criteria are defined relative to Variation B, which is not in the design, and the binding guardrail is powered at half the resolution of its own decision threshold.

## Predicted outcome
Transfer hypothesis, explicitly ungrounded (no evidence base supplied). ARPU/exposed: lands between control and B, roughly +8–18% vs control, because the demo softens paywall pressure and reaches only the Chords branch. Retention 14d: partial recovery vs B but still below control — my guess −0.7 to −1.5 pp, i.e. outside the working −0.5 pp margin. What would surprise me: retention at or above control (that would contradict the team's own reading that Variation C added information and choice without improving retention — fact from the card), or ARPU above B (the card does not claim this either).

## Product proposals
No KNOWLEDGE CONTEXT was supplied, so nothing product-level can be grounded in past experiments.

no grounded product proposal

no direct analogs

- **[ungrounded]** Check whether the harmed slice is even reachable: harm concentrates in Intermediate iOS users, but the demo only reaches Chords choosers (78%). Cross-tab Level × Format before building — if Intermediate skews Tabs, this mechanic cannot touch the loss it targets.
- **[ungrounded]** The −1.79 pp loss sits in non-purchasers, which points at the paywall wall rather than an awareness gap. A paywall-side arm (dismiss path, gift/trial framing, second-paywall timing) deserves research as a competing mechanic.
- **[ungrounded]** Whether coercion is load-bearing: a skippable version of the same demo would separate content value from forced interaction.

## Top risks & failure modes
- **Dose dilution.** Exposure fires at gift-offer close; treatment exists only in the Chords branch (78%), and only when the song has features (Simplify missing on ~27% of songs). Sizing assumes a full dose, so both goal and guardrail are materially underpowered on-exposed.
- **Guardrail mis-specified.** Sized to detect −1.0 pp but decided at −0.5 pp: a true −0.9 pp harm reads as "no significant loss". 80% power on a guardrail also means a 20% miss rate on real harm — the asymmetry is backwards.
- **Historical benchmark.** B's numbers come from a past run (different season, cohort, app version); "held the B level" and "recovered B's retention" are not testable against them.
- **Forced interaction as the harm vector.** No ✕, no skip, disabled UI, dead taps — delivered to users who just declined two paywalls. Plausible mechanism for *worsening* first-session churn, i.e. the guardrail itself; it also contradicts the team's own "keep the flow short / no repeated pressure" finding.
- **Internal sizing inconsistencies.** Retention baseline 42.14% in the design table vs 37.58% control in #7622; ARPU MDE 0.032 against a 20% lift on $0.68 ($0.136); 15,041/arm where #7622 needed ~24,500 to resolve ARPU.

## Non-monetization effects to instrument
- **Negative side:** uninstalls, D1/D3/D7 return, session length, disabled-tap counts and rage-tap bursts, App Store rating volume, support tickets. Stop-rule: halt on D1 ≤ −1.0 pp or demo `fallback='error'` >5%.
- **Positive side:** Tab View 60s and tabs-viewed/user may *rise* (value received inside the tab); feature discovery may lift post-purchase Backing-track/Simplify usage and therefore renewal — instrument feature usage at D7/D30 among buyers.
- **Refunds/trials:** the temporary paid unlock creates expectation mismatch — track refund rate, trial-cancellation rate and 30-day renewal, not just 14d ARPU, with a pre-set halt threshold.
- **Upper funnel:** no acquisition effect is claimed, but watch Explore entry and search→tab flow after paywall dismiss.

## Blocking design fixes
1. Add the Variation B arm, or delete every B-relative goal and restate success purely versus control.
2. Enroll/analyse the primary comparison at the Chords branch (post format-choice, pre-divergence), re-size on the corrected retention baseline, and power the guardrail as a pre-registered non-inferiority test at ≥90%.
3. Freeze one exposure event fired from an identical code path in all arms, with SRM and activation checks.

# APPENDIX

## B. Design & measurement checklist

**Goal metric vs touched surface**
- Goal (ARPU/exposed) and guardrail (Retention 14d) are measured on the full exposed population; the intervention exists only for Chords choosers with feature-bearing songs. Effect-on-exposed ≈ 0.78 × dose-coverage × effect-on-treated; required n scales by ~1/(0.78·c)². Either move enrollment to the format-choice step (legitimate: it precedes any divergence) or inflate n accordingly and pre-register the on-exposed value as the forecasting number.
- `Tab Official Open` fires the three availability flags in **every** variation — good. Use them to build matched strata (same feature-availability profile) for a like-for-like treated-vs-control comparison. Do not condition on post-randomization step completion.
- The "no features available" case reproduces B exactly; report it as a separate stratum and confirm QA coverage.

**Delivery / exposure gates**
- Resolve the `Tour Post Decline Gift Offer Close` vs `App Experiment Start` ambiguity in doc, code and admin config; one event, one code path, all arms, fired before the format branch.
- Verify the activation conditions (never subscribed, trial-eligible, tour not skipped) are evaluable at the same instant in every arm.
- `from_tour` is not implemented on any app event today — treat it as new instrumentation with its own QA gate; without it the demo funnel is not separable from organic feature use.
- `demo_unlock` must be client-side only and must never write to rights; add an explicit test that entitlement state is unchanged after the session.

**SRM / activation**
- Daily SRM on the activation event and on each downstream gate (format choice, tab open, paywall 2 view). A treatment-side gate that fires later or more often than control is the most likely silent bias here.
- Check arm balance on the availability flags — a skew means the song-recommendation surface differs by arm.

**Maturity horizon**
- 39 days enrollment is *enrollment only*. Add 14 days for the retention window and the ARPU-at-14d window: ~53 days calendar minimum, longer if a third arm is added (~31 days enrollment ⇒ ~45+).
- #7622 fact: snapshot +17.25% vs mature +22.8%/+24.2%. Pre-register the mature window as the decision reading and the snapshot as monitoring only. For trial-eligible users, ARPU at 14d may precede the trial→paid billing event; state whether trial starts are counted at expected value or at realised revenue.
- Use the empirical zero-inflated ARPU distribution (bootstrap or CUPED) for sizing and inference; a normal approximation on a $17.76-AOV, ~4%-purchase-rate metric will misstate both MDE and p-values.

**Guardrails and stop-rules worth adding**
- Non-inferiority framing: pre-register margin δ, one-sided CI, decision = reject rollout unless the upper bound of the retention loss is inside δ. Be explicit with the PO that δ = 0.5 pp is not affordable at this traffic (roughly 4× the current n before dilution); choose δ = 1.0 pp honestly or accept that the guardrail is monitoring, not a gate.
- Multiplicity: 4 metrics at α = 0.05 each. One primary, one binding guardrail, everything else descriptive; no peeking without a sequential boundary.
- Add: crash/ANR rate, demo failure rate by component, D1 retention, refund + trial-cancellation rate, App Store rating volume.
- Pre-register the fast-clicker slice definition (dwell_ms threshold) **before** the readout, and treat it as descriptive — it is post-randomization.

## C. Design changes that would most improve expected value

1. **Three arms: control / Variation B / demo.** Without B in-flight, neither "preserved the uplift" nor "recovered the loss" can be measured; the extra ~9 days of enrollment is cheap relative to an uninterpretable result.
2. **Enroll the primary analysis at the format-choice step (Chords), keeping the gift-offer-close event as the secondary full-population readout.** This removes ~22% pure A/A dilution at zero bias cost, and restores most of the power lost to dose coverage.
3. **Ship a skippable variant of the demo as a fourth cell if budget allows — otherwise soften the current one (a ✕ after the first step).** The coercive flow is the single largest threat to the very guardrail this experiment exists to protect; if it fails, you will not be able to tell whether the content or the coercion caused it.
