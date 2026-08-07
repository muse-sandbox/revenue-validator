# MAIN

## Verdict
**Redesign before launch** — the idea is worth testing, but with no Variation-B arm and a binding guardrail margin (−0.5 pp) four times finer than what the sample can resolve (~2 pp, diluted further by the 22% Tabs branch that receives no treatment), the design can answer neither "did ARPU hold at B" nor "was the retention loss recovered".

## Predicted outcome
[hypothesis] Total ARPU/exposed lands between control and Variation B — partial regression, not a full hold — because a step inserted between the content moment and the offer lost access conversion where it was measured (T2-07, T1-03; both L2, so this is a warning, not a prediction). Uncertainty is wide, and the ITT read is pulled artificially toward B by the untreated Tabs branch. Retention 14d: at best a small recovery, not separable from B at this power; the no-skip chain could also move it the wrong way (T1-07). It would surprise me to see a clean +20% ARPU hold *and* a visible retention recovery on one read — I would check exposure delivery and the new event paths first (P-12, P-14).

## Product proposals
- **[mechanic]** Deliver the in-tab context *after* the Paywall 2 dismiss instead of before it — grounded in T2-07, T1-03 (L2) and P-04: [fact] both lost funnel conversion when a screen was inserted ahead of the offer. [hypothesis] Paywall pressure stays at B while the 81% non-purchaser cohort, where the retention loss sits, still gets the value. Direction: members→subscribers at B level, Tab View 60s and Retention 14d above B.
- **[mechanic]** Choose the compact composition with an always-available Continue over the multi-step no-skip gauntlet — grounded in T1-07 (L2) and P-03: [fact] there the skippable gamified arm carried the iOS ARPU win and the non-skippable arm carried the measured retention cost. [hypothesis] skippability, not demo content, decides this guardrail. Direction: Retention 14d closer to control, demo completion lower.
- **[segment]** Pre-register user level and the format branch as readout slices, and consider restricting the demo to Intermediate — grounded in T2-07 and T1-07: [fact] the demo's access-CR loss was deepest on beginners; the retention cost was measured on new post-tour users. Direction: members→subscribers at or above B on untouched slices.

## Top risks & failure modes
- **Deferred offer costs conversion** (P-04): each overlay is an exit; access CR fell significantly in T2-07 and the inserted chain in T1-03 read powered-null on goal — the "+20% hold" is the fragile part, not the retention half.
- **Guardrail cannot resolve the decision** (P-11, P-13): a null retention read at ~2 pp resolution is fully consistent with the −1.6 pp loss it is meant to remove; 14d retention plus pending trials also need maturity before any read.
- **Forced exposure trades money for retention** (P-03, T1-07): the no-skip arm there multiplied engagement and layer revenue but showed a significant D1 retention drop — this design uses that exact lever to fix a retention problem.
- **Treatment is variable-length** (P-12): ~27% of songs lack Simplify, backing track/strumming may be absent, fail-forward auto-skips — part of the test arm receives literal Variation B, blending the ITT.
- **New instrumentation** (P-14): a new activation event, `from_tour` (not implemented on any app event today) and `demo_unlock` are exactly the paths that fabricated or dropped conversions in T2-05 iter3 and T1-09.

## Closest analogs
**T1-07** (L2, closest): a gamified pre-paywall step on the same free new post-tour audience lifted iOS layer ARPU in the skippable arm but cost Android D1 retention in the non-skippable arm; it sat in the interstitial slot with a discount offer, not inside the tab with the offer unchanged. **T2-07** (L2): a 10-second demo before the paywall cut access CR significantly on both platforms with losses along the whole funnel, but it fired on a captured feature tap, whereas here intent is not yet expressed. **T1-03** (L2): a pre-paywall plus compare-table chain lost 96% on the first inserted screen and read powered-null, in a post-ad context and on a cohort that included ex-premium users. Conflict, stated rather than averaged: T1-07 points positive on money, T2-07/T1-03 point negative, and the plausible boundary is captured-intent (negative) versus neutral-moment (positive) placement — [interpretation] in this evidence base the direction of a step inserted before the offer is not one-sided, so evidence is mixed [scope: steps inserted between a trigger or content moment and an App paywall; ids: T1-03, T2-07, T1-07; not covered: web funnels, offer-structure or price changes, steps shown before any intent signal].

## Non-monetization effects to instrument
- **Upside — feature learning:** Tab View 60s (the card's own worst step, 34–40% loss) and week-1 Simplify/backing-track usage may rise on the Chords branch; instrument by branch and by demo completion, and report D1/D7 alongside D14.
- **Downside — early-session friction:** disabled-UI taps and forced steps can shorten the first session; instrument Demo Disabled Tap rate, post-dismiss session length, D1 retention; stop-rule: interim D1 on the Chords arm below control by a pre-set amount.
- **Refunds/cancels:** temporarily unlocked paid features create post-purchase expectation mismatch; instrument 14d cancels and refunds split by `demo_unlock`; stop-rule on refund rate.
- **Composition A/A:** format-choice split (78/22) and tour completion are pre-treatment — any shift signals leakage upstream of the branch.

## Blocking design fixes
1. Add a Variation-B arm (or make B the control) and pre-register the goal as non-inferiority of ARPU versus B with a stated margin.
2. Restate the guardrail as a testable non-inferiority margin sized at real enrollment, read on the treated Chords branch, with Total kept as a dilution check.
3. Freeze one canonical exposure event fired from the same code path in every arm, with SRM and format-split A/A before any readout.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok, pending-trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent      # first-session pre-paywall zone in both; interstitial slot vs in-tab step before Paywall 2
    segment: adjacent         # free new post-tour in both; new case iOS-only, trial-eligible, tour-completed
    trigger_eligibility: adjacent
    surface: different        # interstitial slot overlay vs official-tab screen with step overlays
    mechanism: exact          # interactive step before the offer, with a forced (no-skip) exit path
    offer: different          # scratch-coupon discount there vs unchanged Paywall 2 offer here
    behavior: adjacent        # forced gimmick interaction vs forced feature taps
    metric: exact             # ARPU + access CR in both
    money_chain: adjacent
    guardrails: adjacent      # D1 retention measured there, Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Gamification lifted layer conversion on both platforms; the skippable arm (var2) showed a
    significant iOS ARPU gain (p=0.011) and the non-skippable arm (var3) multiplied engagement and layer
    revenue while Android D1 retention fell significantly (p=0.012) [T1-07, mixed/killed].
    [interpretation] The source team read this as a monetization/retention trade-off of non-skippability
    (P-03). [hypothesis] For the case under review, skippability — not demo content — is the likely
    driver of the Retention 14d guardrail, and a forced tooltip chain can move the guardrail in the
    direction the experiment exists to repair. Transfer hypothesis only.
  not_transferable: >
    All magnitudes (+26.5% ARPU, +72.7%/+166% segment CR, −9.15% D1, +150–160% layer revenue) — the
    retention cost was measured on Android and on D1, this case is iOS and D14, so neither the platform
    nor the horizon carries over. The var2 internals are flagged unexplained in the source, so its
    positive direction is weaker than its negative counterpart. The discount-coupon offer is absent
    here, so the money mechanism is not the same one that produced the source lift.
  sizing_prior: >
    prior: a retention effect of the order of ~1 pp at D1 was detectable there on a comparable
    first-session audience — useful only as an order-of-magnitude input to guardrail sizing.
  conflict: >
    Points positive on money for a pre-offer step, against T2-07 and T1-03 which point negative;
    the plausible boundary is neutral-moment vs captured-intent placement. Not averaged.
```

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; SRM ok, duration/sample under design; significant-negative; killed)
  axes:
    flow_stage: different     # S1–S3 feature-gate vs first-session S3–S5 onboarding flow
    segment: adjacent         # App free never-subscribed vs iOS first-session free never-subscribed
    trigger_eligibility: different  # feature tap (captured intent) vs onboarding position
    surface: different        # feature paywall with preview+timer vs official tab with step overlays
    mechanism: exact          # demo/preview step inserted before the paywall, deferring the offer
    offer: adjacent           # offer itself unchanged in both
    behavior: adjacent
    metric: adjacent          # feature→access % vs Total ARPU/exposed with access proxies
    money_chain: adjacent
    guardrails: different     # no retention guardrail there; binding Retention 14d here
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Access CR fell significantly on both platforms (p=0.00 iOS, p=0.008 Android) with losses along
    the whole funnel, beginners hit hardest; AOV/ARPPU rose through mix shift [T2-07,
    significant-negative/killed]. [interpretation] The source team read this as captured intent that must
    not be deferred (P-04). [hypothesis] Here the Chords branch may lose Paywall 2 conversion relative to
    Variation B, and the loss may concentrate in the least experienced users — a transfer hypothesis, and
    the weaker case for it is that intent is not yet captured at the moment this demo fires.
  not_transferable: >
    All magnitudes (−36% / −28.5% access CR, −42.1% beginners, +14.2% AOV). The feature-gate context does
    not carry over: the source's users had just tapped a gated feature, this case's users have not asked
    for anything. The source page explicitly does not condemn demo content shown BEFORE intent, which is
    closer to this case. Sample fell below design, so only the significant negatives are load-bearing.
  sizing_prior: >
    prior: funnel-step losses of tens of percent, not single digits, are the order of magnitude to plan
    guardrails and proxy MDEs around.
  conflict: >
    Contradicts T1-07's positive money direction for a pre-offer step; boundary hypothesis is
    captured-intent vs neutral-moment placement. Reported, not averaged.
```

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07; SRM ok 35,411/34,913; powered-null; killed)
  axes:
    flow_stage: adjacent      # S3–S4 post-ad pre-paywall chain vs first-session pre-Paywall-2 step
    segment: adjacent         # iOS free incl. ex-premium vs iOS free never-subscribed
    trigger_eligibility: different  # post-ad-view vs post-gift-offer-close onboarding position
    surface: different        # standalone pre-paywall + compare-table screens vs in-tab overlays
    mechanism: exact          # extra screen(s) inserted between the moment and the paywall
    offer: adjacent           # standard paywall offer in both
    behavior: different       # skippable informational screens vs forced feature interactions
    metric: adjacent          # interstitial→access % vs ARPU/exposed with access proxies
    money_chain: adjacent
    guardrails: different
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] 96% of users dropped on the first inserted skippable screen, new-scenario conversion 0.07%,
    goal metric powered-null, and the new source cannibalized tab sources [T1-03, powered-null/killed].
    [interpretation] The source team read a longer funnel after an ad as multiplicatively worse than a
    plain banner (P-04). [hypothesis] For this case the drop-off is expected to be smaller because the
    demo lives inside content the user asked for, but the direction — fewer users arriving at Paywall 2
    in a usable state — is the risk to instrument step by step. Transfer hypothesis only.
  not_transferable: >
    The 96% drop, the 0.07% conversion and the +10.4% Total ARPU (n.s.) are magnitudes and do not
    transfer. The post-ad irritation context is absent here and the source explicitly does not condemn
    pre-paywalls in a neutral context. The cohort mixed free with ex-premium users, so per P-08 no
    segment-level product conclusion crosses into this strictly never-subscribed audience.
  sizing_prior: >
    prior: expect per-step drop-off to be the dominant term in any multi-step pre-offer flow; size the
    demo funnel on per-step retention, not on end-to-end completion.
  conflict: >
    Same direction as T2-07, opposite to T1-07 (see that card's conflict field).
```

## B. Design & measurement checklist

- **Goal metric vs touched surface (P-11).** The demo touches only the Chords branch (~78%), minus sessions where all three features are unavailable (Simplify alone missing on ~27% of songs). Total ARPU/exposed is therefore a diluted ITT: the observable effect is roughly the treated share times the true effect, inflating the effective MDE by ~1/0.7 or worse. Pre-register a Chords-branch primary read with Total kept as the dilution/cannibalization check.
- **Estimand.** "Hold approximately the Variation B level" is a non-inferiority claim; the current design tests superiority versus control at +20%, which is a question exp #7622 already answered. Without a B arm the ARPU comparison is against a historical benchmark run at a different time — not randomized.
- **Guardrail sizing.** A −0.5 pp margin on a ~42% baseline needs on the order of 10⁵ users per arm at 80%/0.05; the design carries 38,147 and resolves ~2 pp. Either widen the approved margin to what the traffic can test, accept a longer run, or make the decision rule explicitly Bayesian/descriptive rather than a significance test.
- **Delivery/exposure gates (P-12).** One canonical activation event, fired from the same code path in control and test at the gift-offer close; verify arms live, iOS build coverage, planned days and sample reached before any read. Log `fallback` reasons and per-step availability so treatment-received can be reconstructed.
- **SRM and activation.** SRM on the activation event; A/A on the pre-treatment format split (78/22), tour completion and eligibility flags; SRM again on the Chords sub-population, which is a post-exposure slice and needs its own check.
- **Maturity (P-13).** Retention 14d plus 14-day trial/charge maturity means no final read earlier than exposure + 14 days for the last enrolled cohort; report pending-charge share with every interim, and do not roll out on an interim read (T2-02's failure mode).
- **Guardrails and stop-rules worth adding.** D1/D7 retention on the Chords arm; refunds and 14d cancels split by `demo_unlock`; demo error rate (`fallback='error'`, including failed backing-track downloads); disabled-tap rate during Play; fast-clicker slice funnel and retention as pre-registered, not exploratory.
- **Attribution hygiene (P-14).** `from_tour` is new to every app event — validate end-to-end before launch; treat any large lift from a newly instrumented path as suspect until the counter is reconciled against the existing funnel events.

## C. Design changes that would most improve expected value

1. **Three arms: control / Variation B / B+demo**, with B as the comparison of record for both metrics; if a third arm pushes enrollment to ~31+ days, that cost buys the only clean answer available and is worth paying — otherwise drop the ARPU-hold claim from the goal and run this purely as a retention-recovery test against B.
2. **Move the primary analysis to the Chords branch** and pre-register the Tabs branch as an internal negative control (it should show no effect on either metric); this converts the biggest dilution problem into a validity check.
3. **Pre-register a decision table** mapping ARPU-vs-B and Retention-vs-B outcomes into roll-out / iterate / kill, including the "both effects too small to resolve" cell — which, on current sizing, is the single most likely result.
