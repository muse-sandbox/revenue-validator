**1. Verdict — launch with changes.** The pairing (ex-paid segment × interstitial slot × special reactivation offer) is well supported directionally by T1-08, but the design as written cannot answer the money question: the 10-day horizon cannot read a 14-day-trial chain, the power model is built on tab views while randomization is by user, and a pre-splash screen adds a known drop-off step.

**2. Predicted outcome.** [hypothesis] Segment-scoped access conversion likely moves up — the sign comes from ex-paid responsiveness observed in T1-02 (direction only; found via the contamination bug this card cites as its origin) and supported in T1-09 (~20× per-member, inconclusive source, direction only). [hypothesis] Revenue direction is genuinely unresolved: a free re-trial maximizes accesses (the goal metric) while pushing conversion onto the trial→charge link, where T1-02's generous-trial arm underperformed on a different segment. What would surprise me: no access lift at all despite confirmed exposure (that would point to a reach failure, T1-01 flavor), or a segment ARPU decline at the matured read.

**3. Top risks & failure modes**
- **Reach shortfall.** The card's own data: 51.4% of the audience sees zero ads/day, and the splash is tied to the ad slot (first-ad replacement + error fallback). If no ad request fires, the splash may never render for half the segment. Reach gates everything on this surface family (T1-01, P-01).
- **Pre-splash step drop-off.** An inserted screen before the offer on auto-display is the pattern that produced a 96% first-screen drop in the post-ad interstitial context (T1-03, P-04).
- **Goal metric rewards trial starts, not money.** "Eligible→access" is mechanically inflated by a free trial; trial→charge quality and 14d cancels are the real question and mature after the run ends (T1-02 warning; P-13).
- **Tiny absolute numbers invite artifacts.** The model expects +54 accesses (iOS) over the whole run; lifts at that volume are where attribution artifacts live (T1-09's ×4.6 phantom, P-14).
- **Ad-revenue displacement uninstrumented.** The splash consumes the day's first ad impression; displacement is acknowledged but absent from the metric plan (P-02, P-11 — read dilution on Total too).

**4. Analogs** (ranked; all three compute to L2 — none satisfies the L1 conditions)

```yaml
analog:
  source: T1-02 (ab 6002/6128/6191; 2025-04..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact            # S3–S4 interstitial exposure
    segment: different           # all free vs expired-subscription
    trigger_eligibility: adjacent
    surface: exact               # ad slot replaced by own promo offer
    mechanism: exact             # replace ad with offer incl. extended free trial
    offer: adjacent              # extended 14d trial in both
    behavior: adjacent
    metric: adjacent
    money_chain: exact           # exposure→paywall→trial→charge
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: exact        # both act on the trial-start link
  platform: exact
  level: L2
  transferable: >
    [fact] Iter2 iOS ARPU +7.5% (p=0.029); cannibalization 34% iOS / 63% And;
    interstitial-sourced trial→charge below average (-13% iOS / -45% And);
    iter1 lift was ex-premium segment contamination — those users converted
    strongly despite immediate charge [T1-02]. [hypothesis] For RH-01: the
    slot can source subscriptions, but a generous trial pulls lower-quality
    trials, and part of the access lift will be cannibalized from existing
    paywall entries. The contamination episode is the direct directional
    support for targeting ex-paid here.
  not_transferable: >
    All magnitudes; free-audience product conclusions do not cross to ex-paid
    (policy minimum, P-08) — this card is a hypothesis/warning only; the 13×
    ex-paid conversion figure is bug-derived, direction only, never a prior.
  conflict: >
    Warns against the trial route, while T1-08 shows the instant (no-trial)
    route winning on ex-paid. Not averaged: the boundary is the money-chain
    link (trial-start vs instant charge) and the segment state.
```

```yaml
analog:
  source: T1-08 (ab 7487; 2026-05..07; SRM ok, trials matured; significant-positive; rolled-out)
  axes:
    flow_stage: exact            # S3–S4 interstitial exposure
    segment: adjacent            # winback-exhausted ex-paid vs all expired
    trigger_eligibility: adjacent
    surface: exact               # interstitial slot
    mechanism: different         # deep-discount instant vs renewed free trial
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: different    # instant charge D0 vs trial→charge
  platform: exact
  level: L2
  transferable: >
    [fact] iOS winback ARPU +241% (p=0.000), buyers +365.6%; converts to 100%
    instant purchases; Total ARPU lift evaporated after control trials
    matured; iOS diffuse dilution -$702/day on non-winback [T1-08].
    [hypothesis] For RH-01: an interstitial offer to lapsed payers can revive
    the segment — but the proven mechanic on this segment/surface skipped the
    trial entirely; the re-trial variant is the untested branch.
  not_transferable: >
    All magnitudes; the instant-charge mechanism conclusion does not cover a
    re-trial offer (different money-chain link); winback-exhausted sequencing
    protections (P-09) are absent in RH-01's design.
  conflict: >
    See T1-02 card: instant-vs-trial direction conflict; closer segment here,
    closer mechanism there — reported, not averaged.
```

```yaml
analog:
  source: T1-09 (ab 7454; 2026-05..06; SRM ok; inconclusive; killed)
  axes:
    flow_stage: exact
    segment: adjacent            # free+ex-paid mix (winback branch = ex-paid)
    trigger_eligibility: adjacent
    surface: exact               # interstitial slot
    mechanism: different         # message personalization, offers unchanged
    offer: adjacent              # its ex-paid branch offered +14d trial
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: different
  platform: adjacent             # iOS arm unreadable; Android carried the read
  level: L2
  transferable: >
    Inconclusive source — measurement lessons only (rule 6). [fact] ~70–165
    interstitial conversions per arm; a visible ×4.6 winback lift was an
    attribution artifact; show #1 delivers 50–60% of layer conversions
    [T1-09]. [hypothesis] For RH-01: at +54 expected accesses, artifact
    control and source-attribution checks are load-bearing; once-daily
    frequency is consistent with front-loading.
  not_transferable: >
    No product conclusion of any kind (inconclusive); the ~20× ex-paid
    observation is direction-only support, never a sizing prior.
```

## Non-monetization effects to instrument
- **Retention (both directions).** Positive: one fewer ad plus a relevant offer for returning ex-subscribers could raise D1/D7. Negative: interruptive splash annoyance — T1-07 measured D1 −9.15% on a non-skippable variant. Instrument D1/D7 split by splash-exposed vs not; stop-rule on a significant D1 drop.
- **Engagement (3+ tabs/scores weekly).** Already a guardrail — add it per exposure cohort; a drop concentrated in splash viewers is a stop signal.
- **Ad revenue / experience.** Instrument ad revenue per eligible user and ad-load error rates (the fallback path changes ad accounting); positive side: fewer ads may reduce uninstalls — track uninstall/return rate.
- **Refunds/cancels.** Trial route lowers refund risk vs instant, but expect trial-end churn: instrument trial→charge, 14d cancels, and repeat-trial abuse (offer is once-per-user — verify enforcement).

**6. Design & measurement checklist.** Goal metric is correctly segment-scoped and the touched-surface funnel segments are already configured (P-11 satisfied). Add: delivery gate = Splash Views / eligible first-tab-opens daily, with SRM on App Experiment Start (P-12); maturity gate = final read only after run + 14-day trial window with pending share <5% (P-13, T1-08's evaporating Total lift); re-do power at user level (tab-view denominator with user randomization overstates power); replace the "XX%" significance placeholder before launch; keep iOS-only conclusions iOS-only — Android was sized but not shipped.

**7. Changes that would most improve expected value**
1. Extend the decision horizon past trial maturity and make trial→charge plus matured segment ARPU the decision metrics; access alone will read "win" for any trial giveaway.
2. Add a deep-discount instant arm (no trial) alongside the re-trial arm — T1-08's significant-positive mechanic on this segment and surface — turning the run into a direct instant-vs-retrial answer.
3. Remove (or arm-test) the pre-splash screen and decouple splash delivery from ad-fill so the ~51% zero-ad users are reachable; add the ad-revenue displacement guardrail with a stop-rule.
