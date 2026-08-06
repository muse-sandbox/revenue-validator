## 1. Verdict

**Redesign before launch.** [hypothesis] The design cannot answer its own question: the goal is defined against Variation B, which is not an arm; the binding retention margin (-0.5 pp) sits ~4x below the table's detectable drop (-2.37 pp); and 22% of enrollees get no treatment.

## 2. Predicted outcome

[hypothesis] Total ARPU/exposed lands between A and B - partial regression of B's lift, not the intended hold; transfer mechanism (sign only, T1-03/T2-07): a step between trigger and offer sheds users before paywall access. [hypothesis] Retention 14d recovers only partly, or not at all: the demo is forced (no close button, UI disabled) and taxes the 81% who never buy. [hypothesis] Surprises: ARPU at or above B with retention at control parity, or any effect in the untreated Tabs branch.

## 3. Top risks & failure modes

- **Added-step conversion loss.** Every overlay is an exit; constrained exits push loss into early paywall opens (`play_interrupt`) [T1-03 L2, T2-07 L2]; [interpretation] P-04 excludes pre-intent demos, so this is a warning.
- **Forced non-skippability trades retention for engagement** - the metric under protection [T1-07, explicitly labelled L3 weak signal: guardrail input only, never a verdict basis].
- **Unmeasurable guardrail.** A -0.5 pp margin against a ~2.0-2.37 pp MDE makes "within margin" indistinguishable from -2 pp harm; the card self-contradicts (-1.0 vs -2.37 pp).
- **Dilution and exposure ambiguity.** 22% Tabs, ~27% of songs without Simplify and fail-forward skips attenuate ITT; the exposure event has two competing definitions (P-12).
- **Expectation mismatch.** Features unlocked, then withdrawn at Paywall 2; attention need not become intent (P-03), and Tab View 60s may fall.

## 4. Analogs

[interpretation] Among the reviewed cases, inserting a step between trigger and offer points in conflicting directions, so evidence is mixed: steps added after a captured feature intent lost conversion [scope: steps inserted between a captured intent trigger and the offer in App funnels; ids: T1-03, T2-07; not covered: gamified pre-steps in a neutral pre-intent context (T1-07), web funnels, offer-structure and price changes], whereas a gamified pre-paywall step in a neutral post-tour context lifted layer conversion at an Android D1 retention cost [T1-07]. The boundary is intent capture: this case is pre-intent but forced, so both directions stay live.

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07, 7-day run; iOS; SRM ok 35,411/34,913; powered-null; killed)
  axes:
    flow_stage: adjacent         # S3–S4 App pre-paywall chain in both; post-ad vs post-gift-decline first session
    segment: adjacent            # iOS free incl. ex-premium vs iOS free never-subscribed new-session
    trigger_eligibility: different  # ad-interstitial close vs gift-offer close + song pick
    surface: different           # pre-paywall + compare table vs in-tab guided overlay
    mechanism: exact             # insert an extra screen between the trigger and the paywall
    offer: exact                 # standard Pro paywall offer unchanged in both
    behavior: adjacent           # skippable informational screens vs forced feature taps
    metric: adjacent             # Interstitial→Access % vs ARPU/exposed + access proxies
    money_chain: exact           # exposure → paywall → trial → charge
    guardrails: different        # no retention guardrail there; Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] In the lengthened post-ad chain the new scenario converted at a
    near-zero rate, most users were lost on the first inserted screen, and the
    goal metric came out a powered null with Total ARPU not significant (p=0.19)
    [T1-03]. [interpretation] The source team read this as multiplicative
    drop-off: an extra step after the trigger works worse than a plain banner.
    [hypothesis] For the new case this is a transfer hypothesis of SIGN and
    MECHANISM only, not a prediction: the in-tab demo should be expected to shed
    users before Paywall 2, so "hold B's ARPU" is the optimistic edge of the
    range, and the step-level funnel (Demo Step View → Success) must be
    instrumented to locate the loss.
  not_transferable: >
    Magnitudes (96%, 0.07%, +10.4%) never transfer as predictions. The post-ad
    irritation rationale is the source team's interpretation and is not isolated
    experimentally. Per T1-03's transfer bounds, it does not condemn pre-paywalls
    in a neutral context, and the new case's forced-exit design has no counterpart
    there.
  sizing_prior: >
    prior: order-of-magnitude only — first-screen drop-off in an inserted App step
    can be tens of percent, so size the demo funnel expecting large per-step loss.
  conflict: >
    Points opposite to T1-07 (L3), where a gamified inserted pre-step lifted layer
    conversion. Not averaged: the closer L2 cases dominate the verdict; T1-07 is
    kept as a guardrail signal only.
```

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; App iOS+Android; SRM ok, sample under design; significant-negative; killed)
  axes:
    flow_stage: different        # S1–S3 feature-gate after captured intent vs first-session post-decline tour
    segment: adjacent            # App free never-subscribed in both; new-first-session subset here
    trigger_eligibility: different  # feature tap vs gift-offer close
    surface: different           # feature paywall with timer vs in-tab guided overlay before Paywall 2
    mechanism: exact             # interpose a feature demo/preview before the paywall
    offer: exact                 # offer terms unchanged in both
    behavior: adjacent           # passive 10s preview vs forced multi-step feature taps
    metric: adjacent             # feature→access % vs ARPU/exposed + members→subscribers/buyers
    money_chain: adjacent        # trigger → paywall access → purchase; 14d ARPU horizon here
    guardrails: different        # AOV/ARPPU there; Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L2
  transferable: >
    [fact] A 10-second demo before the paywall reduced access CR significantly on
    both platforms (p=0.00 iOS, p=0.008 Android), with losses along the whole
    funnel, beginners hit hardest, and AOV/ARPPU up through mix shift [T2-07].
    [interpretation] The source team read this as deferred intent: a step between
    feature desire and the paywall destroys conversion. [hypothesis] For the new
    case this transfers as SIGN and MECHANISM only — a warning about the same
    demo-before-paywall step, weakened because intent is not yet captured at the
    gift-offer close; the mix-shift signature (fewer but better buyers) is worth
    pre-registering as an alternative outcome shape to a flat ARPU.
  not_transferable: >
    Magnitudes (−36%, −28.5%, −42.1%, +14.2% AOV) are not predictions. Its
    feature-gate context does not cover demo content shown before intent, which is
    untested; the split between psychological friction and broken navigation was
    never isolated. The Android half does not apply to this iOS-only launch.
  sizing_prior: >
    prior: for sizing only, treat a double-digit relative access-CR loss as a
    plausible downside scenario when powering the goal metric.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07, 8-day run; iOS+Android; SRM ok, trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent         # S3–S4 App exposure before the paywall; interstitial layer vs in-tab tour
    segment: exact               # free new post-tour first-session users in both
    trigger_eligibility: adjacent
    surface: different           # interstitial slot vs in-tab overlay on the official tab
    mechanism: adjacent          # forced interactive pre-paywall step, but coupon gamification vs feature education
    offer: different             # scratch discount coupon vs unchanged standard offer
    behavior: adjacent           # skip removed; forced interaction to proceed
    metric: adjacent             # ARPU + layer CR; retention read out in both
    money_chain: adjacent
    guardrails: adjacent         # retention read as a trade-off in both
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L3
  transferable: >
    L3 — explicitly labelled WEAK signal. No product conclusion transfers; usable
    only for guardrails, measurement and sizing. [fact] The non-skippable arm
    produced ×8 engagement into the funnel and +150–160% layer revenue, while
    Android D1 retention fell 9.15% (p=0.012); iOS var2 ARPU +26.5% (p=0.011) came
    with a small absolute increment [T1-07]. [interpretation] The source team read
    this as a monetization/retention trade-off of removing the skip. [hypothesis]
    For the new case this justifies instrumenting D1 retention as an early-warning
    guardrail and pre-registering a stop-rule on it — it is not a basis to launch,
    revise or deprioritize.
  not_transferable: >
    All magnitudes; the retention price was measured on Android and on new
    post-tour users, so it cannot be assumed identical on this iOS cohort. The
    var2 internal anomaly (−75–77% interstitial→banner) is unexplained, so var2
    internals are unreliable. Coupon/offer gamification is a different content
    class from feature education; no directional product transfer is claimed.
  conflict: >
    Points opposite to T1-03 and T2-07 on whether an inserted pre-step helps. As
    an L3 signal it does not overturn them; both directions are reported.
```

## Non-monetization effects to instrument

- **Retention, both ways.** Downside: forced taps raise annoyance churn. Upside: users who learn Simplify or Backing track may return more. Track D1/D3/D7 beside D14 by demo completion and fast-clicker slice; stop if Chords-branch D1 drops significantly below control.
- **Engagement and discovery.** Upside: Tab View 60s, tabs per user, Simplify/Transpose/Autoscroll use on days 1-7 - adoption is the intended mechanism and deserves a success threshold, not only a guard. Downside: the demo may replace self-driven exploration.
- **Upper funnel.** Session length, second-song search, abandonment before Paywall 2, uninstall proxies; stop on a significant abandonment rise.
- **Refunds and support.** The temporary unlock can mis-sell: track 14d cancels, refunds and contacts about locked features; stop on a refund rise.
- **Failure telemetry.** `fallback='error'`, disabled taps, `play_interrupt` share: high error rates mean undelivered treatment (P-12).

## 6. Design & measurement checklist

- **Metric vs touched surface.** ARPU/exposed is correctly scoped (P-11); pre-register the Chords branch as primary population and Tabs as a negative control that must read about zero, with its own SRM check.
- **Baselines.** The table uses $0.68 and 42.14%; #7622 observed $0.66 and 37.58%. Re-size on observed values.
- **Guardrail statistics.** One-sided non-inferiority at an approved margin, powered there; 0.5 pp costs an order of magnitude more sample than 1.6 pp (sizing prior) - widen it or extend the run.
- **Exposure.** Fire App Experiment Start once per eligible user from one shared code path in all arms, before the format branch; align admin `experiment_event_start`.
- **Maturity.** Read ARPU only below 5% pending 14d charges, with full 14-day windows after last enrollment (P-13); no rollout on interim reads.
- **Stop-rules to add.** D1 retention, 14d refunds/cancels, Tab View 60s, demo error rate, paywall-access CR.

## 7. Changes that would most improve expected value

1. **Run B vs C.** Both questions are B-relative; A-vs-C answers neither, and three arms at a 0.5 pp margin are unaffordable.
2. **Give the demo a visible exit** (persistent Continue): it removes the largest retention-risk mechanism; if forced exposure matters, test skippable versus forced.
3. **Fix guardrail and population before sizing** - approved non-inferiority margin, Chords-branch primary, one activation event - then recompute duration.
