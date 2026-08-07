# MAIN

## Verdict
**Redesign before launch.** The hypothesis is stated relative to Variation B ("hold B's ARPU, recover most of B's Retention 14d loss"), but Iteration #1 has no B arm and the binding guardrail is sized to detect −2.37 pp while the decision threshold is −0.5 pp — as designed the experiment cannot answer its own question; the idea itself is worth testing.

## Predicted outcome
[hypothesis] Total ARPU/exposed lands **between control and B** — a partial regression of B's lift rather than a clean hold — because the demo defers an already-captured intent before Paywall 2; direction from T2-07 (L1), magnitude explicitly not transferred. [hypothesis] Retention 14d reads *closer to control than B* but with a CI several times wider than the ±0.5 pp decision margin, i.e. undecidable. What would surprise me: ARPU at or above B **with** retention within −0.5 pp and a CI tight enough to prove it; or a significant ARPU lift above B (that would contradict the post-intent-friction direction).

## Product proposals
- **[mechanic]** Deliver the in-tab value **after the paywall dismiss** instead of between the tab and Paywall 2 — grounded in T2-07 (L1 card) and P-04, whose transfer ban explicitly leaves content outside the post-intent → pre-offer slot untested. [fact] the retention loss in #7622 is concentrated in the 81% who saw the paywall and did not buy; [hypothesis] moving the demo there leaves members→subscribers at B's level while acting where the loss lives. Direction: Tab View 60s and Retention 14d up in the non-purchaser slice, access CR unchanged.
- **[segment]** Pre-register the **user-level split as a decision rule**, not an analytical slice, and consider making the demo eligibility-gated by level — grounded in T2-07 (L1): [fact] its friction cost concentrated in beginners (−42.1% access CR). [hypothesis] here the split decides whether the mechanic is bad or only badly targeted. Direction: members→subscribers at or above B on the untreated levels.
- **[offer]** Test changing Paywall 2's **structure instead of its preamble** — instant discounted purchase in place of the trial — grounded in P-05 (applicability: iOS paywalls with an existing trial step, free audience). Direction: charge CR up, AOV down, 14d cancels down; net ARPU direction uncertain, no magnitude transferred.

## Top risks & failure modes
- Goal and guardrail are both **B-relative**, but B is only available as a historical arm from #7622 — different weeks, different cohort; any "held B" claim is uncontrolled (P-12).
- The guardrail is **unpowered at its own threshold**: MDE −2.37 pp vs an approved margin of −0.5 pp and a B loss of −1.60 pp — a null here is uninformative, not reassuring (P-11, P-13).
- **Post-intent friction** costs funnel conversion where measured [T2-07, L1; T1-03, L2] — the card's "main risk" is the modal outcome, not the tail.
- **Forced steps** (no ✕, feature-tap the only exit) buy engagement at a measured retention price in an adjacent case [T1-07, L3 weak signal — guardrail lesson only, not a product conclusion].
- **Dose heterogeneity**: only ~78% (Chords) are treated, ~27% of songs lack Simplify, fail-forward skips steps — the goal metric averages over largely untreated users (P-11).

## Closest analogs
**T2-07** (L1): a 10-second feature demo before the paywall cut access CR −36% iOS / −28.5% Android with losses along the whole funnel; it differs in that the demo was passive and triggered by an organic feature tap, while ours is a forced multi-tap tour step with paid features unlocked. **T1-03** (L2): an extra pre-paywall screen after an ad dropped 96% of users at the first screen and read powered-null on the goal; it differs by context (post-ad irritation) and surface. **T1-07** (L3, explicitly a weak signal for guardrails/sizing only — not a direct analog): a gamified pre-paywall step lifted layer ARPU on iOS but cost Android D1 retention −9.15% on the same free new post-tour segment. Conflict, not averaged: T1-07 points the other way from T2-07/T1-03, so `evidence is mixed` — the boundary is *where the step sits*: a teaser in the interstitial slot before the user's own trigger lifted layer conversion [T1-07], a step after captured feature intent and before the offer lost access CR [T1-03, T2-07]. This case sits on the losing side of that boundary; T1-07's positive sign may not be borrowed for it.

## Non-monetization effects to instrument
- **Engagement, both directions**: Tab View 60s and D1–D7 use of Simplify/Backing track/Strumming (upside: the demo teaches features and lifts tab dwell); downside: repeated pressure before Paywall 2 depresses the same transition. Instrument per demo step; stop-rule if Tab View 60s falls below control.
- **Early churn**: D1 and D7 retention plus first-session abandonment at each step (dwell_ms, disabled-tap counts). Add an interim stop-rule on D1 retention — D14 arrives too late to protect the cohort.
- **Refunds and cancels**: the demo unlocks paid features that lock again after purchase — instrument 14d refunds/cancels and trial→charge maturity (P-13); stop-rule on refunds. Positive side: T3-06-style structure shifts reduce early cancels, so read cancels as an effect, not only a risk.
- **Untreated Tabs branch (22%)**: instrument as an in-experiment negative control — any movement there signals exposure or randomization contamination (P-14), not a treatment effect.

## Blocking design fixes
1. Add the **Variation B arm** (accepting ≈31-day enrollment) or restate the hypothesis as a control-only claim — otherwise "hold B" is untestable.
2. Re-specify goal and guardrail as **pre-registered non-inferiority tests** with margins the sample supports; primary readout on the treated Chords branch, full-exposed as secondary.
3. Freeze **one canonical activation event** (App Experiment Start) fired from the same code path in every arm, with daily SRM and a delivery gate on demo failure/skip rates.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; App iOS+Android; SRM ok, under-delivered but negatives significant; significant-negative; killed)
  axes:
    flow_stage: exact            # step interposed between the user's feature/content trigger and the paywall
    segment: adjacent            # free never-subscribed vs free never-subscribed new first-session iOS
    trigger_eligibility: different  # organic feature tap vs scripted onboarding tour step
    surface: adjacent            # feature paywall with in-context preview vs in-tab step overlays before Paywall 2
    mechanism: exact             # interpose a timed feature demo before the offer (delayed paywall)
    offer: adjacent              # standard offer unchanged by the treatment in both
    behavior: different          # passive 10s preview + timer vs forced multi-tap interactive demo
    metric: adjacent             # feature->access % vs ARPU/exposed + members->subscribers
    money_chain: adjacent
    guardrails: different        # no binding retention guardrail there; Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: exact        # pre-paywall step -> paywall access -> purchase, same link
  platform: adjacent             # iOS+Android vs iOS-only; the friction mechanism is platform-agnostic
  level: L1
  transferable: >
    [fact] Access CR −36% iOS (p=0.00) / −28.5% Android (p=0.008), with losses along the whole
    funnel (conversion to banner −10%/−18%; banner click->purchase −22%/−26%); beginners iOS
    −42.1%; AOV +14.2% / ARPPU +17.9% through mix shift [T2-07].
    [interpretation] The source team read this as "captured intent must not be deferred" — a step
    between feature desire and the paywall loses conversion; the psychological-friction vs
    broken-navigation split was not isolated.
    [hypothesis] For this case: the Chords demo branch most likely reduces Paywall 2 access and
    members->subscribers relative to Variation B, with the loss concentrated in a level segment;
    sign and mechanism only, and the mix-shift shape (AOV up while volume falls) is worth
    pre-registering as an outcome pattern rather than a prediction.
  not_transferable: >
    All magnitudes (−36% / −28.5% access CR, −42.1% beginners, +14.2% AOV) — sizing only, never
    predictions. The passive-preview form of the demo (ours is forced, multi-step, with paid
    features temporarily unlocked). The feature-gate trigger context. The Android read (this case
    is iOS-only). T2-07's under-delivered sample means its own null-space is not characterized;
    only its significant negatives are usable.
  sizing_prior: >
    prior: a post-intent demo step has cost access CR on the order of tens of percent in this
    source — use for MDE sizing on the access/subscribe proxies, not as an expected value.
  conflict: >
    Contradicts T1-07 (L3 below), where a gamified pre-paywall step lifted iOS layer ARPU. Not
    averaged: T2-07 is the closer card (L1 vs L3) and its step sits after captured intent, which
    is this case's position; T1-07's step sits in the interstitial slot before the user's own
    trigger.
```

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07, 7-day run; iOS; SRM ok 35,411/34,913; powered-null; killed)
  axes:
    flow_stage: adjacent         # S3-S4 post-ad exposure chain vs in-tab pre-Paywall-2 step
    segment: adjacent            # iOS free incl. ex-premium vs iOS free never-subscribed new
    trigger_eligibility: different  # ad completion vs onboarding song pick
    surface: different           # post-ad pre-paywall + compare table vs in-tab overlays
    mechanism: exact             # insert an extra screen between the trigger and the paywall
    offer: adjacent              # standard Pro paywall behind the extra step in both
    behavior: adjacent           # skippable screen vs forced tap-through, both pre-offer screens
    metric: adjacent             # interstitial->access % vs ARPU/exposed with access proxies
    money_chain: adjacent
    guardrails: different
  segment_monetization_state: exact
  money_chain_link: exact        # extra screen -> paywall access -> purchase
  platform: exact                # iOS in both
  level: L2
  transferable: >
    [fact] New-scenario conversion 0.07% with a 96% drop on the first skippable pre-paywall
    screen; Total ARPU +10.4% (p=0.19) i.e. powered-null on the goal; 3% of subscriptions from
    the new source with cannibalization of tab sources [T1-03].
    [interpretation] The source team read a longer funnel after an ad as worse than a plain
    banner — each screen is an exit opportunity (P-04).
    [hypothesis] Warning-level for this case: each additional demo step multiplies drop-off before
    Paywall 2, and the fact that our steps are non-skippable converts drop-off into forced
    exposure rather than removing it — an untested substitution, not a fix.
  not_transferable: >
    The 96% and 0.07% figures (post-ad irritation context, different surface) — sizing only.
    The powered-null verdict on ARPU does not transfer as "no effect" here: different surface,
    different exposure volume. Nothing about non-skippable steps was measured in T1-03.
  sizing_prior: >
    prior: per-screen drop-off in an inserted pre-paywall chain has been large enough to dominate
    the funnel — size the step-completion funnel (Demo Step View -> Success) accordingly.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07, 8-day run; iOS+Android; SRM ok, pending-trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent         # S3-S4 interstitial slot vs in-tab step before Paywall 2
    segment: exact               # free new post-tour first-session users in both
    trigger_eligibility: adjacent
    surface: different           # interstitial slot vs in-tab overlay on the official tab
    mechanism: adjacent          # gamified coupon pre-step + non-skippability vs forced feature demo
    offer: different             # scratch-coupon discount vs unchanged standard Paywall 2 offer
    behavior: adjacent           # forced interaction to proceed in both
    metric: adjacent             # ARPU + interstitial->access CR + D1 retention vs ARPU + Retention 14d
    money_chain: adjacent
    guardrails: adjacent         # retention guardrail present in both
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L3
  transferable: >
    L3 — WEAK SIGNAL ONLY, for guardrails, measurement and sizing. No product conclusion transfers
    and this card may not move the verdict.
    [fact] iOS var2 ARPU +26.5% (p=0.011); interstitial segment +72.7% (var2) / +166% (var3);
    non-skippable var3: x8 engagement, +150-160% layer revenue, Android D1 retention −9.15%
    (p=0.012); absolute increment small (forecast iOS var2 +$474/day) [T1-07].
    [interpretation] The source team read a monetization/retention trade-off of non-skippability
    and warned that a significant relative lift is not a sufficient absolute increment.
    [hypothesis] For this case, only the measurement lesson is usable: a forced-exposure design on
    this exact segment needs an early retention read (D1/D7) as a stop-rule, because the guardrail
    that actually moved there was visible long before D14.
  not_transferable: >
    Every product conclusion: the +26.5% ARPU sign must NOT be read as support for this demo
    (different mechanism — an offer/coupon teaser before the user's own trigger, not a feature
    demo after it). All magnitudes. The Android-only retention measurement (do not assume iOS pays
    the same price, per P-03's own transfer ban). The var2 internals are flagged unexplained by the
    source page.
  sizing_prior: >
    prior: retention damage from forced exposure appeared at D1 in that case — use for choosing the
    proxy horizon and the interim stop-rule, not for predicting D14 magnitude here.
  conflict: >
    Points opposite to T2-07 and T1-03. Resolution by closeness, not averaging: T2-07 is L1 and
    T1-03 is L2, both on the post-intent side of the boundary this case sits on; T1-07 is L3 and
    its step sits before the user's own trigger.
```

## B. Design & measurement checklist

**Goal metric vs touched surface (P-11).** The treatment reaches only the Chords branch (~78% of exposed) and, inside it, a variable number of steps (Simplify unavailable for ~27% of songs; fail-forward skips). Total ARPU/exposed averages treated and untreated users. Primary readout should be the Chords branch; report full-exposed as the rollout-level secondary; report the Tabs branch as an in-experiment negative control.

**Arm structure.** Two arms cannot test a B-relative hypothesis. If the third arm is dropped, the goal and guardrail must be restated against control only, and "recovering B's retention loss" becomes uncheckable.

**Baseline consistency.** The design calculator uses Retention 42.14% and ARPU $0.68; the #7622 control read 37.58% and $0.66. A 4.5 pp baseline gap changes both the required sample and the interpretation of the −0.5 pp margin. Reconcile before sizing.

**Guardrail power.** MDE −2.37 pp against a −0.5 pp decision margin and a −1.60 pp reference loss. Detecting −0.5 pp at this baseline is roughly two orders of magnitude more sample than planned — so either (a) declare the guardrail a *large-harm screen only* and pre-register that a null does not license rollout, or (b) move the decision to a powered proximal proxy (D1/D7 retention, Tab View 60s) with D14 confirmatory.

**Delivery/exposure gate (P-12).** Demo composition is still an open decision (compact Simplify+Transpose vs the multi-step flow) and Transpose does not appear in the mockup flow — the treatment is not frozen. Also: one activation event from one code path in all arms (the doc alternates between Gift Offer Close and App Experiment Start); admin `experiment_event_start` aligned; daily SRM; monitor `fallback='error'` and step-skip rates as a delivery metric, with a pre-set threshold that invalidates the read.

**Maturity (P-13).** Retention 14d needs 14 days after the last enrollment; ARPU at 14 days will carry pending trial charges — #7622's own snapshot (+17.25%) vs mature (+22.8%/+24.2%) reads show the direction of that bias. Pre-register the mature read date and forbid early rollout on interim reads (T2-02).

**Attribution and slicing (P-14).** The fast-clicker slice and any "demo completers" slice are post-randomization selections — report descriptively, never as decision rules. `demo_unlock=1` must be client-side only and must not write rights; verify in QA that no unlocked-feature state leaks into entitlement or into the purchase funnel attribution. `from_tour` is a new param on existing events — validate before trusting any from_tour split.

**Multiplicity.** One goal, one binding guardrail, and four proxies; pre-register which comparisons can change the decision and at what alpha.

**Guardrails worth adding.** D1 retention (interim stop-rule), Tab View 60s, 14d refunds/cancels, session-2 return rate, demo failure rate, and the untreated Tabs branch as a contamination detector.

## C. Design changes that would most improve expected value

1. **Run A / Variation-B / demo three arms** and specify the two decisions as non-inferiority tests with explicit margins: ARPU non-inferior to B within a stated margin, Retention 14d superior to B. Accept the ≈31-day enrollment; a cheaper two-arm run buys a result nobody can act on.
2. **Move the decision metric for retention to a powered horizon**: D1/D7 retention plus Tab View 60s as the pre-registered decision proxies with an interim stop-rule, and Retention 14d as a confirmatory read — the current design detects only harm about five times larger than the one it is trying to avoid.
3. **Pre-register the analysis structure**: primary on the Chords-treated branch, Tabs branch as negative control, level (Beginner/Intermediate) split as a stated decision rule rather than an exploratory slice, and a fixed mature-read date with no early rollout.
