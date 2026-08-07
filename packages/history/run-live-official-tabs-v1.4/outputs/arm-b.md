# MAIN

## Verdict
**Redesign before launch.** The experiment is powered to detect a retention drop roughly twice as large as the margin it exists to protect, and it has no Variation-B arm, so it cannot answer either half of its own hypothesis ("hold B's ARPU, recover B's retention loss").

## Predicted outcome
[hypothesis] Total ARPU/exposed lands between control and B — positive versus control but short of +20% — because a forced multi-step demo spends the paywall pressure that produced B's volume-driven lift; Retention 14d improves versus B but stays worse than control by more than 0.5 pp. Uncertainty is wide in both directions. What would surprise me: ARPU at or above B's mature +22.8% *with* retention at control level; or Tab View 60s falling, which would mean the demo consumed the engagement it was meant to create.

## What this experiment cannot show
- [computed] The guardrail is sized at −2.37% relative on a 42.14% baseline, i.e. 42.14% × 2.37% ≈ 1.0 pp, while the acceptable margin is 0.5 pp — 1.0 / 0.5 = 2× that margin. A non-significant guardrail is therefore compatible with twice the loss the team said it would accept: this design cannot show the retention condition was met.
- [computed] Only the Chords branch is treated (78% of the arm), so a demo that recovers half of B's 1.60 pp loss on treated users arrives arm-wide as 78% × (1.60 pp / 2) ≈ 0.62 pp — under the ~1.0 pp floor above. A null would not mean the mechanic failed.
- [computed] Reach and duration disagree by ~4×: 2 × 38,147 = 76,294 exposures at ≈7,700/day is ≈10 days, not the 39 stated; at exp #7622's own rate (24,500 per variation ÷ 22 days ≈ 1,114/day) it is 38,147 / 1,114 ≈ 34 days, plus 14 days of maturity ≈ 48 days to a final read.

## Product proposals
- **[mechanic]** Keep Continue always available instead of feature-tap-only exits — grounded in **T1-07** (L2): [fact] the skippable gamified pre-paywall variant carried the iOS ARPU lift, while the non-skippable one bought ×8 engagement and a measured Android D1 retention loss. [hypothesis] Direction here: Retention 14d closer to control on a skippable demo, with conversion largely preserved.
- **[mechanic]** Place the feature demo *after* the Paywall 2 dismissal (the chooser slot the card already says improves the 60s transition) rather than before it — grounded in **P-04** (covers funnel-lengthening on S3–S5) and **T1-03** (L2). Direction: ARPU held at B level with Tab View 60s up.
- **[segment]** Pre-register the readout split by chosen format and by user level, and consider restricting eligibility to Chords — grounded in **T2-07** (L2): [fact] the demo's damage there was concentrated in one proficiency segment (beginners −42.1%). [hypothesis] Direction: treated-branch retention above the arm average; a mixture read decides nothing.

## Top risks & failure modes
- Forced progression (no ✕, feature-tap-only exits, disabled taps during Play) is itself a retention lever pointing the wrong way — the arm may re-import the harm it was built to remove (T1-07, P-03).
- Dampened paywall pressure regresses ARPU toward control; with no B arm the "held B's level" claim rests on a cross-experiment comparison to #7622, which is not randomized (P-14).
- Dose varies per user: 22% Tabs untreated, Simplify skipped for ~27% of songs, fail-forward auto-completions — an ITT null is uninterpretable (P-12).
- Exposure-event ambiguity (Gift Offer Close vs App Experiment Start) risks activation mismatch, SRM, and non-comparability with #7622 baselines (P-12).
- The guardrail baseline used for sizing (42.14%) is not the cohort that produced the harm (#7622 iOS control 37.58%), so the sample size answers a different question than the one asked.

## Closest analogs
Ranked by exact-axis count. **T1-07** (gamified pre-paywall step, same free new post-tour segment, App): the skippable variant lifted iOS ARPU while the non-skippable one traded engagement for an Android D1 retention loss — differs in surface (interstitial layer, not in-tab) and in that its step changed the offer framing. **T1-03** (iOS post-ad pre-paywall → compare table): 96% dropped at the first inserted screen and the goal read powered-null — differs in trigger (post-ad irritation) and cohort (included ex-premium). **T2-07** (10-second feature demo before a feature paywall): access CR −36% iOS with losses along the whole funnel and AOV up by mix shift — differs in flow stage (captured feature intent at a gate, not a scripted first session). Conflict, stated rather than averaged: T1-07 points positive on money, T1-03 and T2-07 point negative on conversion — `evidence is mixed` for inserted pre-paywall steps [scope: interactive steps inserted between a first-session or feature trigger and an App paywall; ids: T1-07, T1-03, T2-07; not covered: web funnels, offer/price changes, placements after paywall dismissal]. The boundary the cases draw: steps placed *after captured feature intent* lost conversion (T1-03, T2-07); a step in a neutral scripted moment could still earn money (T1-07) but charged retention when it was forced. This case sits on the T1-07 side of the boundary with T1-07's forcing switched on.

## Non-monetization effects to instrument
- **Upside — feature learning:** the demo may raise Tab View 60s, Simplify/Backing-track/Strumming adoption D1–D14 among non-buyers, and session depth. Instrument these as pre-registered secondary successes, not anecdotes; report for buyers and non-buyers separately.
- **Downside — early annoyance:** measure Retention D1 and D7 alongside D14 (T1-07's forced arm showed its cost at D1) and add an interim stop-rule on D1 versus control, so a repeat of B's harm is caught before day 39.
- **Funnel composition upstream:** the format-choice step already loses ~1%; instrument choice-share (Chords/Tabs) per arm to confirm the pre-demo screens are identical, and the fast-clicker slice already specified.
- **Purchase quality:** track 14d cancels and refunds on Paywall 2 purchases plus AOV/ARPPU — a demo-warmed cohort may buy differently even with AOV flat, and this read must mature (P-13).
- **Technical experience:** demo `fallback='error'` share and disabled-tap counts as a frustration proxy; stop-rule if error fallbacks exceed a pre-set threshold, since a broken demo measures neither arm.

## Blocking design fixes
1. Add the Variation-B arm and re-size as a **non-inferiority** test (retention margin 0.5 pp versus control; ARPU margin versus B), accepting ≈31-day enrollment.
2. Fix one canonical activation event fired from the same code path in every arm, identical to #7622's boundary, with daily SRM on it.
3. Re-derive the guardrail sample on the observed control baseline (37.58%), pre-register the Chords-branch analysis as primary, and hold the read until last-enrollee + 14 days.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok, pending-trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent         # S3–S4 interstitial pre-paywall vs S3→S5 in-tab step before Paywall 2
    segment: exact               # free new post-tour first-session users in both
    trigger_eligibility: adjacent # new case adds trial-eligibility + iOS-only + tour-not-skipped
    surface: different           # interstitial slot vs in-tab tooltip overlay on the tab screen
    mechanism: exact             # interactive pre-paywall step with the skip removed (forced progression)
    offer: different             # scratch-coupon discount reveal vs unchanged standard Paywall 2 offer
    behavior: adjacent           # tap-through forced interaction before the offer
    metric: exact                # ARPU + retention in both
    money_chain: adjacent        # exposure→paywall→purchase in both, different layer revenue definition
    guardrails: exact            # retention guardrail explicit in both
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L2
  transferable: >
    [fact] iOS var2 (skippable gamified pre-paywall) ARPU +26.5% (p=0.011) with interstitial-segment
    conversion up; var3 (non-skippable) produced ×8 engagement into the funnel and +150–160% layer
    revenue but Android retention D1 −9.15% (p=0.012) [T1-07]. [interpretation] The source team read
    this as a monetization/retention trade-off of forced exposure (P-03), and killed the line despite
    the significant relative lift because the absolute increment was small. [hypothesis] For this case,
    the forcing built into the demo (no ✕, feature-tap-only exits, disabled taps during the 8-sec Play)
    is a plausible independent cause of retention harm, working against the very metric the experiment
    exists to recover; direction only, with high uncertainty.
  not_transferable: >
    All magnitudes: +26.5% ARPU, ×8 engagement, +150–160% layer revenue, −9.15% D1. The retention cost
    was measured on Android and on the var3 configuration only — an iOS-only run has no measured price
    here. Var2 internals are flagged unexplained in the source. Source maturity is undocumented and
    result_class is mixed, so under §2.3(6) this does not carry a product conclusion, only a warning.
  sizing_prior: >
    prior: engagement-into-funnel effects of forced steps are order-of-magnitude, retention effects
    order of ~1 pp/day-1 — useful only for choosing tripwire thresholds, not for forecasting.
  conflict: >
    Points positive on money where T1-03 and T2-07 point negative on conversion; the hypothesized
    boundary is whether the inserted step sits after captured feature intent (T1-03, T2-07) or inside
    a neutral scripted moment (T1-07). Not averaged.
```

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07; SRM ok 35,411/34,913; powered-null; killed)
  axes:
    flow_stage: adjacent         # S3–S4 post-ad chain vs S3→S5 first-session chain before Paywall 2
    segment: adjacent            # iOS free including ex-premium vs iOS free never-subscribed new users
    trigger_eligibility: different # ad-view completion vs gift-offer decline in a guided first session
    surface: different           # interstitial + compare table vs in-tab overlay
    mechanism: exact             # extra screens inserted between the user and the paywall
    offer: exact                 # standard Pro paywall unchanged at the end of the chain in both
    behavior: adjacent
    metric: adjacent             # Interstitial→Access % vs Total ARPU/exposed with funnel proxies
    money_chain: adjacent
    guardrails: different        # no retention guardrail there
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] The lengthened chain converted at 0.07% with a 96% drop on the first skippable pre-paywall;
    Total ARPU +10.4% was not significant and the goal read powered-null; 3% of subscriptions came from
    the new source with cannibalization of tab sources [T1-03]. [interpretation] The team read the extra
    step as a multiplicative drop-off (P-04). [hypothesis] Here, each added demo step is an exit
    opportunity even when the exit is only the paywall; expect the treated branch to arrive at Paywall 2
    thinner and later than in Variation B — direction only.
  not_transferable: >
    Magnitudes (96% first-screen drop, 0.07% conversion, +10.4% ARPU) do not transfer: the source ran in
    a post-ad irritation context on a cohort containing ex-premium users, and its screens were skippable
    while this design removes the skip. Says nothing about demo content shown before intent, which the
    source's own transfer bounds mark untested.
  conflict: >
    Contradicted in sign by T1-07 (a pre-paywall step that lifted ARPU). Boundary as stated in the
    T1-07 card; not averaged.
```

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; SRM ok, sample under design; significant-negative; killed)
  axes:
    flow_stage: different        # S1–S3 feature gate vs S3→S5 post-decline first-session flow
    segment: adjacent            # App free never-subscribed vs iOS free never-subscribed new users
    trigger_eligibility: different # user taps a gated feature vs scripted first-session sequence
    surface: different           # feature paywall with preview vs in-tab tooltip overlay
    mechanism: exact             # a timed demo of paid functionality inserted before the offer
    offer: adjacent              # standard subscription offer, unchanged, behind the demo in both
    behavior: adjacent           # forced wait/interaction before the paywall appears
    metric: adjacent             # feature→access % vs ARPU/exposed with access proxies
    money_chain: adjacent
    guardrails: different
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L2
  transferable: >
    [fact] Access CR −36% iOS (p=0.00) / −28.5% Android (p=0.008) with losses along the whole funnel
    (conversion to banner −10%/−18%; banner click→purchase −22%/−26%), beginners worst hit (−42.1%),
    while AOV +14.2% and ARPPU +17.9% through mix shift [T2-07]. [interpretation] The team read this as
    deferred captured intent (P-04). [hypothesis] Here the same demo-before-offer shape can move the
    outcome mix rather than the sum — fewer, higher-intent buyers — so a flat ARPU may hide a structural
    change; and the response is likely to differ sharply by proficiency, which is why the level split
    must be pre-registered rather than explored.
  not_transferable: >
    All magnitudes (−36%/−28.5% access CR, −42.1% beginners, +14.2% AOV). The source's intent context is
    different: its users had just tapped the gated feature, whereas here the user has already declined
    Paywall 1 and the gift offer. Its transfer bounds explicitly exclude demo content shown before
    intent, and it isolates neither friction nor navigation as the cause.
  sizing_prior: >
    prior: proficiency-segment spread in the response to a pre-paywall demo was of the same order as the
    average effect — size the level slice to be readable, do not treat it as a footnote.
  conflict: >
    Same conflict with T1-07 as recorded in that card.
```

## B. Design & measurement checklist

- **Goal metric vs touched surface (P-11):** Total ARPU/exposed is correctly scoped to exposed users, unlike a company-wide Total — but it is still diluted by the untreated 22% Tabs branch. Pre-register both the arm-level ITT read and the Chords-branch read, and name which one decides.
- **Post-randomization conditioning:** the format choice happens before any treatment screen, so conditioning on Chords is legitimate *if* the choice screen is byte-identical across arms; verify choice-share balance per arm as a falsification check before trusting the branch read.
- **Delivery/exposure gate (P-12):** confirm both arms are live on the same code path, one activation event, planned duration and per-variation sample reached; report demo step-view rates against the `has_backing_track / has_strumming / has_simplify` flags so the actual delivered dose is known, not assumed.
- **SRM/activation:** daily SRM at the activation event and again at the Chords branch; the `App Experiment Start` vs `Tour Post Decline Gift Offer Close` ambiguity must be closed in code *and* admin config before the first user is bucketed, or the arms are not comparable to each other or to #7622.
- **Maturity horizon (P-13):** Retention 14d and ARPU@14d both need last-enrollee + 14 days; no interim rollout and no early read — T2-02 lost its final read exactly this way.
- **Guardrails and stop-rules to add:** Retention D1/D7 tripwires; demo `fallback='error'` share; disabled-tap rate during Play; 14d cancels and refunds on Paywall 2 purchases; the fast-clicker slice; a pre-agreed kill threshold on D1 rather than a post-hoc judgement.
- **Non-inferiority statistics:** "hold approximately the B level" is an equivalence claim; a superiority-powered test that fails to reject is not evidence of holding. Specify the margin, the arm, and the decision rule before launch.

## C. Design changes that would most improve expected value

1. **Add the Variation-B arm and re-size as non-inferiority** on both metrics (retention margin = the approved pp value versus control; ARPU margin versus B). This is the only change that makes the stated hypothesis testable; the ≈31-day enrollment cost is the price of an answer.
2. **Re-derive the guardrail sizing on the cohort that produced the harm** (#7622 iOS control 37.58%, not 42.14%) and at the approved margin rather than −1.0 pp; if the required sample is infeasible, change the margin openly instead of leaving a design that cannot see it.
3. **Define and instrument dose, and pre-register a per-protocol analysis** (full-step Chords users) alongside ITT as the headline, so that a null is attributable — mixture, forcing, or content — instead of being an uninterpretable average over 22% untreated users, ~27% Simplify-less songs, and fail-forward skips.
