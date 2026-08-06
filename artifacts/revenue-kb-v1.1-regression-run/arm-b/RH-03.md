**1. Verdict — redesign before launch.** The idea is a legitimate re-run of an inconclusive precedent, but the current design repeats the exact delivery failure of that precedent, measures a surface-scoped treatment on a diluted Total metric, and confounds a +25% price increase with the creative change in arm C.

Note: the card's "autumn seasonal test (October 2025), thematic entry animation, no significant differences" matches T2-02 on date, surface, mechanism and metric — [interpretation] I treat T2-02 as that precedent.

**2. Predicted outcome.** [hypothesis] B vs A on DAU→Charge: most likely no detectable effect at this power — the identical mechanic on the identical surfaces produced no significant monetization finals (T2-02, inconclusive → measurement lesson only, so a real effect below/near the 10% MDE is not excluded), and emotional-design lifts of attention without money is the corpus pattern (P-03). [hypothesis] C: structure shift — conversion down, ARPPU up — with elasticity and refunds eating the price gain (P-07 warning). I would be surprised by a significant ≥10% DAU→Charge lift from creative alone, or by arm C being net-revenue-positive without elevated refunds.

**3. Top risks & failure modes**
- **Delivery/power failure:** 3-day iOS run vs 216,622 required per variation ×3 arms; the same design sample on the same surfaces delivered ~9% of plan last time and ended inconclusive with early rollout (T2-02, P-12).
- **Metric dilution:** Total DAU→Charge on all free users for a seasonal-surface treatment; Total metrics drowned a +58% surface effect in T1-10 (P-11).
- **Arm C confound:** price +25% plus intro-offer removal bundled with new creative; only C-vs-B isolates price, and it isn't declared. App price increases showed charge CR −11%, refunds 14d +26.2% (T3-01, P-07).
- **Inserted step before the offer:** the animation delays the splash; extra steps between trigger and offer are multiplicative drop-offs (P-04, T1-03/T2-07) — instrument animation abandonment, don't assume.
- **Maturity:** +7-day trial with a 3-day run means charges are pending at read time (P-13).

**4. Analogs** (ranked; no conflicts between them — T2-01 bounds the upside T2-02 fails to demonstrate)

```yaml
analog:
  source: T2-02 (ab 6701; 2025-10; SRM ok; delivered 4-5 of 7 design days, iOS 20,329 vs 216,622 design; inconclusive; rolled-out early)
  axes:
    flow_stage: exact            # S3-S4 seasonal exposure
    segment: exact               # App free users
    trigger_eligibility: exact   # seasonal window, production display rules
    surface: exact               # sale splash + Explore banner
    mechanism: exact             # copy/design: thematic seasonal creative + entry animation
    offer: exact                 # production offers unchanged (arms A/B)
    behavior: exact
    metric: exact                # CR DAU→Charge in both
    money_chain: exact
    guardrails: adjacent         # R14 not computed in source
  segment_monetization_state: exact
  money_chain_link: exact        # exposure→charge
  platform: exact                # iOS+Android
  level: L1
  transferable: >
    [fact] All monetization finals n.s. (ARPU iOS -2.95% p=0.66, And -1.38%
    p=0.91); only CR→Splash View iOS significant (p=0.001); post-rollout
    forecast iOS -$1716/day, And -$426/day (T2-02). [fact] result_class
    inconclusive: despite computed L1, the validity gate (§1.7, §2.3-6)
    blocks product-conclusion transfer — measurement lessons only.
    [hypothesis] The new case's +10% assumed lift has no evidential support;
    the same design sample failed to deliver on these surfaces before.
  not_transferable: >
    Any product conclusion (source inconclusive). Magnitudes and the
    "suitable for big one-off events" extrapolation. The -$1716/day forecast
    is source-specific, not a prediction here.
```

```yaml
analog:
  source: T3-01 (ab 6026/6260; 2025-05..07; SRM ok; decisive iter2 4.4x design; mixed; killed) — scoped to arm C's price component only
  axes:
    flow_stage: exact            # S6 purchase conditions (arm C price change)
    segment: different           # device-tier free proxy vs all free
    trigger_eligibility: different
    surface: adjacent            # standard App paywalls vs seasonal sale paywall
    mechanism: exact             # price increase
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact   # free in both
  money_chain_link: exact             # price acts on paywall→charge
  platform: adjacent                  # decisive iteration iOS-only; price mechanism platform-agnostic
  level: L1
  transferable: >
    [fact] Decisive iteration: Total ARPU +1.38% (p=0.61); ARPPU +7.34%
    (p=0.001) eaten by charge CR -11% (p=0.003); refunds 14d +26.2%
    (p=0.006); page verdict "price increase too high" (T3-01). [fact]
    result_class mixed, so §2.3-6 blocks full conclusion transfer.
    [hypothesis] As a warning per P-07: arm C's +25% increase plus intro
    removal likely shifts structure without net revenue gain and elevates
    refunds. Not used as a standalone verdict basis.
  not_transferable: >
    Magnitudes (elasticity curve unmeasured; only two points known). Does
    not transfer to price decreases or web (P-07 limits, T3-02).
  sizing_prior: >
    Prior: refunds-14d guardrail sized around the +26.2% source read.
```

```yaml
analog:
  source: T2-01 (ab 6293; 2025-07; SRM ok; R14 mature; significant-negative; killed)
  axes:
    flow_stage: exact            # S3-S4
    segment: exact               # free
    trigger_eligibility: adjacent
    surface: exact               # sale banner + sale splash
    mechanism: different         # surfaces OFF (gating) vs creative restyle
    offer: exact
    behavior: adjacent
    metric: adjacent
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Turning banner+splash off: ARPU -11.6% iOS / -26% And (both
    p=0.036); splash-only-off n.s. (iOS -1.2%, p=0.83) (T2-01).
    [hypothesis] Warning: the banner carries most of the incremental value;
    restyling the splash entry may address the weaker surface, capping
    upside from arm B.
  not_transferable: >
    Magnitudes (seasonal, inventory-specific). An off-test result says
    nothing about whether restyling lifts an already-on surface.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed) — explicit L3 weak signal, guardrails/sizing only
  axes:
    flow_stage: exact
    segment: adjacent            # free new post-tour vs all free
    trigger_eligibility: different
    surface: adjacent            # interstitial slot vs sale splash
    mechanism: adjacent          # gamified interactive animation vs passive thematic animation
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    [L3 — guardrail/measurement lesson only, no product conclusion, not a
    basis for the verdict] [fact] Forced pre-offer animation carried a
    retention price: And var3 D1 -9.15% (p=0.012); significant relative
    lifts translated to small absolute increments (T1-07). [hypothesis]
    Instrument retention and skip behavior for the entry animation.
  not_transferable: >
    All magnitudes; the gamification conversion lift (different mechanism);
    segment-specific retention price.
```

**5.** ## Non-monetization effects to instrument
- **Retention (both directions):** negative — forced entry animation cost D1 retention elsewhere (T1-07, L3 signal); positive — a well-received festive presentation could mildly improve session enjoyment/return. Instrument D1/D7 retention per arm/platform; **stop-rule:** significant D1 drop on any platform stops that arm.
- **Engagement / upper-funnel (both directions):** positive — thematic creative lifted splash-view CR significantly in T2-02; instrument banner CTR, splash views, animation completion vs abandon, time-to-splash. Negative — added latency on Explore entry; instrument Explore-open→content abandonment.
- **Refunds/cancels (both directions):** negative — arm C price rise risks refunds (T3-01 prior); positive — replacing intro $19.99→$39.99 with flat $24.99 removes the year-2 renewal price jump, plausibly lowering later cancels. Instrument 14d refunds/cancels now and renewal cohort later; **stop-rule:** significant refund elevation in C.
- **Source mix / cannibalization:** instrument per-source conversion (sale surfaces vs tab paywalls) — cannibalization is the default (P-02).

**6. Design & measurement checklist**
- Re-scope the primary metric to the exposed/seasonal-surface funnel (banner/splash exposure → charge), with Total ARPU and source-mix as guardrails (P-11); add an exposed-vs-unexposed localization read (T2-05 practice).
- Resolve the duration contradiction: 3 days iOS vs "one week + 7-day trial" — the read needs run + trial maturity before finals (P-13); no rollout on interim reads (T2-02).
- Delivery gate: exposure event defined and QA'd (the instrumentation table is an unfilled template), all 3 arms and both platforms confirmed live, daily sample-vs-design tracking, SRM check (P-12).
- Pre-register C-vs-B as the price contrast; fill the hypothesis template and per-arm success criteria before launch.
- The impact model's +10% on both subscribe and charge is an ungrounded assumption; the only close evidence (T2-02) found nothing significant.

**7. Changes that would most improve expected value**
1. Unbundle price from creative: make the $24.99 test its own experiment or add a price-only arm; as designed, arm C is unreadable.
2. Re-power on the exposed-segment metric with an honest duration for the December window, committing to a matured final read.
3. Complete hypothesis, instrumentation, and stop-rules (retention D1, refunds 14d, charge CR) before launch — this card currently fails the pre-launch gate on paperwork alone.
