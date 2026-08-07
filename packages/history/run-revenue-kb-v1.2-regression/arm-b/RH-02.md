## 1. Verdict

**Launch with changes.** The mechanism is well-precedented on this exact layer (three L1 analogs below), and the design already includes the right cannibalization and ex-subscriber splits — but the 8/12-day duration cannot mature a 14-day trial, the power table is internally inconsistent, and the decision metric must be net of displaced ad revenue before this read can support a rollout.

## 2. Predicted outcome

[hypothesis] Directionally, a positive layer-level effect on Android is more likely than on iOS — the closest analog (T1-04) went positive where the unit replaced thin ad inventory and washed out on iOS where it competed with real ads and other paywalls. [hypothesis] The in-window ARPU read will be dominated by immature trials: with a 14-day free trial and an 8–12-day run, trial→charge revenue lands almost entirely after the experiment ends, so the primary metric will understate (or misstate) the true effect. What would surprise me: a large iOS ARPU lift that survives the cannibalization-check segment, or a significant retention gain from replacing third-party ads.

## 3. Top risks & failure modes

- **Cannibalization is the default, not the exception** [P-02]: the direct predecessor pulled a large share of its conversions from existing sources and was killed for it [T1-02]; the video variant's iOS no-access segment went significantly negative [T1-04]. [hypothesis] Gross ARPU lift can mask net-negative revenue once forgone ad revenue and displaced paywall sources are counted.
- **Funnel length behind the splash** [P-04]: the splash→pre-paywall→main-paywall chain repeats the structure that produced a powered-null with a massive first-screen drop in the post-ad context [T1-03]. The banner deep-link that skips the pre-paywall may outperform the splash's own chain.
- **Trial maturity and trial quality** [P-13]: a generous 14-day trial pulled below-average trial→charge quality in the predecessor [T1-02]; pending charges will be near-100% at readout given the duration.
- **Forced daily exposure retention cost** [P-03]: the 5-second-delayed close is partial non-skippability; the measured Android arm of a non-skippable variant paid a significant D1 retention price [T1-07], and the retention cost of replacing a *guaranteed* daily ad show (vs. filling failures) is flagged in T1-04's lessons. Instrument, don't assume.
- **Ex-subscriber contamination of the read** [P-08, P-14]: the audience ("no current subscription") includes expired subscribers, who respond an order of magnitude more strongly; an apparent lift driven by them fabricated the predecessor's iter-1 result [T1-02]. The planned ex-sub splits are the right defense — make them confirmatory, with SRM per split.

## 4. Analogs

Within the ad-replacement offer-layer family, **evidence is mixed**, and the boundary is enumerable: Android with thin ad inventory went positive (T1-04, rolled out there); iOS trial-offer variants were killed on cannibalization and trial quality (T1-02) or powered-null behind a pre-paywall chain (T1-03); passive ad-fail filling alone moved nothing (T1-01, measurement lesson). The transfer boundaries are ad-inventory presence, funnel length after the splash, and trial-based vs. direct-purchase offers. Ranked cards:

```yaml
analog:
  source: T1-04 (ab 6359/6416/6428; 2025-07..08; SRM ok; mixed; rolled-out on Android)
  axes:
    flow_stage: exact            # S3–S4 interstitial layer in both
    segment: exact               # non-paying without Pro rights; RH-02's "no current sub" also includes expired subs
    trigger_eligibility: exact   # the once-per-day replacement trigger RH-02 explicitly inherits
    surface: exact               # own full-screen unit in the interstitial slot instead of the ad
    mechanism: exact             # new-surface: own monetization unit replacing ads, leading to a trial offer
    offer: adjacent              # video "Try for Free" CTA vs 14d-trial splash + pre-paywall chain
    behavior: adjacent
    metric: exact                # ARPU goal in both
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact        # exposure→trial start in both
  platform: exact
  level: L1
  transferable: >
    [fact] Android ARPU was significantly positive in both iterations; iOS was
    not significant in iter2, and the iter1 iOS segment without interstitial
    accesses was significantly negative (displacement of ad revenue and other
    paywalls) [T1-04]. [interpretation] Value came from reach, not
    per-impression conversion; the unit is pure increment where it replaces
    "nothing" and competition where ad inventory exists. [hypothesis] For
    RH-02, Android is the likelier winner; every iOS read must be judged net
    of ad and paywall displacement.
  not_transferable: >
    Magnitudes (And +17–19%; iOS iter1 no-access segment −24.7%) — sizing
    priors only. The Android conclusion does not transfer to iOS. Source
    creative was a video with a direct CTA; RH-02's splash→pre-paywall chain
    is untested in this source. The retention cost appeared when replacing a
    guaranteed daily show — exactly RH-02's config — and must be re-measured.
  conflict: >
    Contradicts T1-02 (killed) and T1-03 (powered-null) at comparable
    closeness. Not averaged; hypothesized boundary: ad-inventory presence
    (platform), funnel length after the splash, and trial generosity/quality.
```

```yaml
analog:
  source: T1-02 (ab 6002/6128/6191; 2025-04..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact
    segment: adjacent            # iter2 clean free vs RH-02 free incl. expired subs
    trigger_eligibility: adjacent # interstitial + banner-place fill vs guaranteed daily + ad-fail + banners
    surface: exact               # interstitial slot + banner places in both
    mechanism: exact             # subscription offer layer with a 14d extended trial instead of ads
    offer: adjacent              # Pro+ plan/price differ; 14d trial framing shared
    behavior: adjacent
    metric: exact                # ARPU
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact        # exposure→trial start
  platform: exact
  level: L1
  transferable: >
    [fact] The clean iteration showed a significant iOS ARPU lift but heavy
    cannibalization from existing sources on both platforms and below-average
    interstitial trial→charge quality; the iter1 lift was a
    segment-contamination artifact (ex-premium inside "free") [T1-02].
    [interpretation] A generous trial pulls low-quality trials; first exposure
    does most of the layer's work. [hypothesis] RH-02's 14-day-free splash
    will start trials, but net value hinges on trial quality and
    cannibalization, and expired-sub users inside the audience can dominate
    the read.
  not_transferable: >
    Magnitudes (iter2 iOS +7.5% p=0.029, And +4.94% n.s.; cannibalization
    34%/63%; trial→charge −13%/−45%; iter1 +24%/+13% artifact) — priors only.
    result_class is mixed, so the §2.3 gate for a full product-conclusion
    transfer is not met: treat as a sign-and-mechanism warning.
```

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07; SRM ok; powered-null; killed)
  axes:
    flow_stage: exact
    segment: exact               # free incl. ex-premium vs free incl. expired
    trigger_eligibility: adjacent # fired after the ad vs instead of the ad
    surface: adjacent            # post-ad chain vs replacing the ad in the slot
    mechanism: exact             # new-surface with a pre-paywall funnel chain into the standard paywall
    offer: adjacent
    behavior: adjacent
    metric: different            # Interstitial→Access % vs ARPU (does not affect level)
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent             # iOS-only source; mechanism platform-agnostic
  level: L1
  transferable: >
    [fact] Powered-null on the goal, with the overwhelming majority of users
    exiting on the first skippable pre-paywall screen and some cannibalization
    of tab sources [T1-03]. [interpretation] Each inserted screen is a
    multiplicative exit; a longer funnel after an ad works worse than a plain
    banner. [hypothesis] RH-02's splash→pre-paywall→paywall chain risks the
    same multiplicative drop; the banner deep-link that skips the pre-paywall
    may be the stronger path.
  not_transferable: >
    Magnitudes (96% first-screen drop; 0.07% scenario conversion) — priors
    only. Source context was post-ad irritation; its own bounds say it does
    not condemn pre-paywalls in a neutral context, and RH-02 replaces the ad
    rather than following it.
```

```yaml
analog:
  source: T1-01 (ab 4845; 2024; SRM ok; inconclusive; killed)
  axes:
    flow_stage: exact
    segment: exact               # free
    trigger_eligibility: adjacent # no-fill-only with 1/day cap vs guaranteed daily + ad-fail
    surface: exact               # interstitial slot
    mechanism: exact             # new-surface fill of the slot
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent             # iOS-only; mechanism platform-agnostic
  level: L1
  transferable: >
    [fact] Passive filling of no-fill slots produced near-zero reach and no
    significant monetization differences; source is inconclusive, so per rule
    6 this grounds a measurement lesson only [T1-01]. [hypothesis] RH-02's
    ad-fail placement (b) will contribute roughly nothing by itself — the
    once-daily active replacement carries the reach — so instrument reach per
    placement (a)/(b)/(c) separately.
  not_transferable: >
    Any product conclusion (inconclusive source). Reach figures are
    config-specific (caps, triggers) and never transfer as magnitudes.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact
    segment: adjacent            # free new post-tour vs all free incl. expired
    trigger_eligibility: adjacent
    surface: exact               # interstitial slot
    mechanism: different         # gamified creative + skippability change vs new-surface ad replacement
    offer: adjacent
    behavior: adjacent
    metric: exact                # ARPU
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Reduced skippability multiplied funnel engagement and layer
    revenue but produced a significant Android D1 retention drop in the
    measured non-skippable arm; repeated exposures added almost nothing
    beyond the first [T1-07]. [hypothesis] RH-02's 5-second-delayed close is
    partial forced exposure — expect an engagement/retention trade-off and
    front-loaded value on show #1; this is a warning to instrument, not a
    launch basis (L2).
  not_transferable: >
    Magnitudes (×8 engagement; +150–160% layer revenue; And D1 −9.15%
    p=0.012) — priors only. Source audience was free new post-tour;
    gamification mechanism differs; var2 internals carry an unexplained
    anomaly per the source's own bounds.
```

## Non-monetization effects to instrument

- **Retention, both directions:** negative — daily forced 5s exposure replacing a guaranteed ad show may cost D1/D7 retention (mechanism per P-03/T1-07, T1-04 lesson); positive — replacing third-party ads with a cleaner own unit could *improve* perceived UX and retention. Instrument D1/D7/D14 per platform and per exposure count; **stop-rule:** significant D1 retention drop on either platform.
- **Engagement / upper funnel:** tab views, session length, and interstitial→banner interplay in both directions — the banners in zero states may lift paywall entries broadly, or the splash may suppress downstream banner engagement. Instrument the planned splash→banner→click→finish funnel per source value.
- **Ad ecosystem:** ad impressions and ad revenue on treated users, both the loss from replaced slots and the gain from newly monetized zero states; **stop-rule:** combined subscription-plus-ad revenue significantly negative.
- **Refunds / early cancels:** trial mix shift raises within-window cancels; track trial cancels and 14-day refunds even though they mature post-window.

## 6. Design & measurement checklist

- **Duration vs. trial window (blocking):** 8 (And) / 12 (iOS) days cannot mature a 14-day trial [P-13]. Extend to ≥ trial length + 7 days, or pre-commit a matured re-read with a pending-charge gate before any rollout decision.
- **Power table (blocking):** internally inconsistent — iOS lift 23.15% vs MDE 0.017 on a $0.127 baseline don't reconcile, and And MDE 0.10 exceeds the $0.056 baseline; parameters were inherited from a design whose audience was "failed to view an ad interstitial," not all free users. Recompute on the actual audience [P-12].
- **Goal metric:** free-user ARPU is acceptably scoped (the treatment touches all free users daily), but the decision metric must be net revenue including displaced ad revenue, with the cannibalization-exclusion segment confirmatory [P-11, P-02].
- **Delivery gates:** exposure event in both arms (present — good); verify arms/platforms live for the full window, SRM overall and within the ex-sub splits, and reach per placement (a)/(b)/(c) separately [T1-01, P-12, P-14].
- **Seasonality:** "1 week in calculations" doesn't divide the 8/12-day durations into whole weekly cycles; align duration to full weeks.

## 7. Changes that would most improve expected value

1. Extend the run past trial maturity and recompute the power table on the real all-free audience (both currently invalidate the planned read).
2. Add or plan a splash→paywall-direct arm (skipping the pre-paywall), given the multiplicative-drop warning from T1-03/P-04, and instrument the pre-paywall step's drop-off explicitly in this run.
3. Make the decision rule explicit pre-launch: net revenue (subscriptions minus displaced ad revenue) on the confirmatory segment, plus the D1-retention stop-rule — and pre-register the ex-subscriber split as confirmatory so a contamination-driven lift cannot drive rollout [P-08, P-14].
