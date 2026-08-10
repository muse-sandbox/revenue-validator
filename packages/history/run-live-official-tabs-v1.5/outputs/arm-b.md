# MAIN

## Verdict
**Redesign before launch** — the mechanic is worth a slot, but the guardrail that decides the launch is sized above the margin it must protect, and the goal ("hold Variation B") has no arm to hold against.

## Findings

- **[stop]** We spend the slot and come back with a Retention 14d number that cannot clear the approved margin either way. *Mechanism:* [computed] the design resolves a drop of `42.14% × 2.37% ≈ 1.0 pp`, while the working margin is `0.5 pp` — `1.0 / 0.5 = 2×` the loss the team says it would accept. *Consequence:* a non-significant guardrail is compatible with twice the accepted retention loss, so the condition the experiment exists to test can never be declared met. *Price:* decision impossible — the retention question stays open whatever the numbers say. *Fix:* approve the margin as a number, then size on it.
- **[stop]** Arms enrolled at one boundary and read at another produce a composition artifact indistinguishable from the retention effect. *Mechanism:* the card leaves the canonical exposure event open between the gift-offer close and App Experiment Start and defers alignment to implementation; P-12 makes delivery/exposure a pre-launch gate for exactly this failure. *Consequence:* an unfavourable retention read will be disputed as an enrollment artifact instead of decided. *Price:* experiment slot — the run is redone, not re-analysed. *Fix:* one activation event from the same code path in every arm, plus a 48-hour SRM and exposure-parity gate.
- **[stop]** The question the card is built on — did the demo keep B's uplift — gets answered against another experiment's numbers rather than a live arm. *Mechanism:* [computed] the ARPU row is powered for a `20.00%` lift versus control, while "holding B" is the gap to B's mature readings: `24.2% − 20.0% = 4.2 pp` of relative lift, which no arm in a two-arm design measures. *Consequence:* any result between "kept B" and "regressed halfway to control" becomes a matter of opinion. *Price:* experiment slot — the mechanism comparison has to be run again. *Fix:* fund the third arm (the card puts binding enrollment at ≈31 days) or pre-register a non-inferiority test against control.
- **[improve]** Both headline metrics land on a population where 22% of the arm never sees a demo, so a flat read leaves the treated branch undecided. *Mechanism:* [computed] the demo runs on the Chords branch only — `78%` — and Simplify is unavailable for `~27%` of songs, so `78% × (1 − 27%) ≈ 57%` of the arm reaches the full step list; landing the overall guardrail at `−0.5 pp` from B's `−1.60 pp` needs `1.60 − 0.50 = 1.10 pp` overall, i.e. `1.10 / 0.78 ≈ 1.41 pp` inside the branch that sees it. *Consequence:* a null on either metric stays compatible with a real branch-level effect. *Price:* share of the expected effect — 22% of the arm is untreated by construction. *Fix:* pre-register the Chords branch as primary analysis population, Tabs as the placebo check.
- **[improve]** The calendar drifts by weeks: the card's reach figure and its sizing yield 10 days and 39 days for the same sample. *Mechanism:* [computed] at `≈7,700` exposed/day over two arms, `38,147 / (7,700 / 2) ≈ 10` days; at the exp #7622 rate of `24,500 / 22 ≈ 1,114` per variation per day, `38,147 / 1,114 ≈ 34` days — the rates differ by `3,850 / 1,114 ≈ 3.5×`. *Consequence:* the "audience is sufficient" answer and the plan rest on different numbers, before the 14-day maturity tail. *Price:* days to decision. *Fix:* state the experiment traffic share and add the maturity tail.

## What you decide
- **[product owner]** The retention margin, as a number, before re-sizing: [computed] halving the detectable drop multiplies the sample by `(1.0 / 0.5)² = 4` → `38,147 × 4 ≈ 152,588` per variation and `39 × 4 ≈ 156` days. Accept the calendar, or accept a wider margin.
- **[product owner]** Whether the third arm is funded — without it the goal is "beat control", not "hold B".
- **[analyst]** The exposure event, the guardrail baseline (design uses 42.14% where exp #7622 control read 37.58%), and the primary analysis population.
- **[analyst]** The early stop-rule, since Retention 14d arrives after the run ends.

## Product proposals
- **[offer]** Test the Paywall 2 offer structure — instant discounted purchase instead of the trial — rather than lengthening the funnel: grounded in P-05 (iOS paywalls with an existing trial step). Expected direction: charge CR up and 14d cancels down, with AOV down; it adds no step, so it does not spend retention to buy conversion.
- **[mechanic]** Keep an exit on the demo steps instead of making the feature tap the only way out: grounded in P-03 (skippability decisions). Expected direction: Paywall 2 access CR closer to control, demo engagement lower — which is the trade this guardrail is about.
- **[segment]** Pre-register the level split as a decision rule, not an analytical slice: grounded in T2-07, where the pre-paywall demo's access-CR loss concentrated in beginners. Expected direction: Paywall 2 access CR lowest among the least experienced users; if so, restrict eligibility rather than kill the mechanic.

## Non-monetization effects to instrument
- **Retention mechanism (both directions):** split D1/D7/D14 by demo completion, fail-forward skip, feature availability and the fast-clicker slice. Stop-rule: D1 in the treated branch below control by the approved margin in the first 72 hours.
- **Engagement upside:** Tab View 60s, tabs opened in week 1, and repeat use of Simplify/Backing track in sessions 2+ — a learned-feature gain the money metric will not show. Read Chords against Tabs.
- **Refunds and cancels:** purchases made while `demo_unlock = 1` may rest on temporarily unlocked features; instrument 14d refunds/cancels by that flag, with a stop-rule on refunds.
- **Frustration and upper funnel:** disabled-tap attempts, play-interrupt rate, tab abandonment before Paywall View, D0 uninstalls, store-rating watch.

## Closest analogs
- **T2-07** (closest): a 10-second feature demo placed before an App paywall for free never-subscribed users cut access CR on both platforms, worst among beginners, with AOV rising through mix shift; it differs here because intent was captured at a feature tap, while this flow leads the user into the tab, and it carried no retention guardrail.
- **T1-03**: a pre-paywall plus compare-table chain on iOS free users lost 96% on the first extra screen and read powered-null on its goal; it differs in being skippable, informational, and placed right after an ad.
- **T1-07** (weak L3 signal, not a direct analog): the same free new post-tour audience with a forced non-skippable pre-paywall step showed engagement up and Android D1 retention down — usable here only for sizing the retention guardrail and its stop-rule, not as a reason to launch or kill.
- Conflict, stated rather than averaged: `evidence is mixed` for steps inserted between an App trigger moment and the paywall — the step cost conversion where the user had already reached for the feature (T1-03, T2-07) and lifted layer conversion where it was a gamified coupon in a neutral post-tour moment (T1-07) [scope: steps inserted between an App trigger moment and the paywall; ids: T1-03, T2-07, T1-07; not covered: web funnels, offer-structure or price changes, steps shown after the paywall]. This case sits on the boundary: neutral onboarding context like T1-07, but a paywall the flow is already carrying the user toward, like T2-07.

## Predicted outcome
Total ARPU/exposed most likely lands above control and below B's mature readings, with wide uncertainty; Retention 14d most likely lands between B and control and reads non-significant at the current sizing — the modal outcome is an undecidable guardrail rather than a clear answer. It would surprise me if retention returned to control level (the awareness-gap mechanism is unconfirmed by the card's own research), if ARPU exceeded B (the demo would then add intent rather than dampen pressure), or if the Tabs branch moved at all — that would signal instrumentation, not product.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; App, free never-subscribed; SRM ok, samples below design, negatives significant; significant-negative; killed)
  axes:
    flow_stage: adjacent      # S1–S3 feature-gate there vs a step inside the first-session flow before Paywall 2 here
    segment: adjacent         # App free never-subscribed vs iOS new first-session free never-subscribed
    trigger_eligibility: adjacent
    surface: different        # feature paywall with preview+timer vs in-tab overlay tooltips on the tab screen
    mechanism: exact          # a demo step inserted between the user's contact with the feature and the offer
    offer: adjacent           # unchanged standard offer behind the delay in both
    behavior: adjacent        # 10s auto preview vs forced multi-step interaction
    metric: adjacent
    money_chain: adjacent
    guardrails: different     # no retention guardrail there; Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L2
  transferable: >
    [fact] Access CR −36% iOS (p=0.00) / −28.5% Android (p=0.008), losses along the whole
    funnel (conversion to banner −10%/−18%; banner click→purchase −22%/−26%), beginners iOS
    −42.1%, AOV +14.2% / ARPPU +17.9% through mix shift [T2-07]. [interpretation] The source
    team read this as captured intent that must not be deferred. [hypothesis] Here the risk
    sits on the goal, not only the guardrail: the Chords branch may lose Paywall 2 access
    relative to the preserved B funnel, so "hold B" is the claim most exposed — direction
    only, with real uncertainty because the intent state differs.
  not_transferable: >
    Every magnitude above (−36%, −28.5%, −42.1%, +14.2%) — none is a prediction for this
    case. T2-07 deferred a paywall at the moment of a feature tap, where intent was already
    captured; here the flow leads the user into the tab, so the drop-off factor does not
    carry. T2-07 measured no retention outcome, so its silence about Retention 14d says
    nothing here. The "psychological friction vs broken navigation" split was never isolated.
  sizing_prior: >
    prior — pre-paywall friction on a feature-intent App audience produced double-digit
    relative access-CR losses [T2-07]; use for guardrail sizing and stop-rule design only,
    never as an expected effect.
```

```yaml
analog:
  source: T1-03 (ab 6335; 2025-07, 7-day run; iOS; free incl. ex-premium; SRM ok 35,411/34,913; powered-null; killed)
  axes:
    flow_stage: adjacent      # S3–S4 post-ad pre-paywall chain vs in-flow step before Paywall 2
    segment: adjacent
    trigger_eligibility: different   # ad-interstitial close vs guided first-song flow
    surface: different        # full-screen pre-paywall + compare table vs in-tab overlay
    mechanism: exact          # extra step inserted between the trigger and the offer
    offer: adjacent
    behavior: different       # skippable informational screens vs forced interactive demo
    metric: adjacent
    money_chain: adjacent
    guardrails: different
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] 96% dropped on the first skippable pre-paywall; new-scenario conversion 0.07%;
    Total ARPU +10.4% (p=0.19) with 3% of subscriptions from the new source and
    cannibalization of tab sources; powered-null on the goal [T1-03].
    [interpretation] The source team read each extra screen as a multiplicative drop-off.
    [hypothesis] Each demo step here is an exit opportunity even with the ✕ removed, and the
    multi-step Chords flow is the arm most exposed to it — direction only.
  not_transferable: >
    The 96% and 0.07% figures are not predictions here. T1-03's screens were skippable,
    informational and followed an ad, so the irritation context is absent in this case;
    its segment mixed ex-premium users, whose response is gated differently (P-08).
    T1-03 measured nothing about retention.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07, 8-day run; iOS+Android; free new post-tour; SRM ok, pending-trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent
    segment: exact            # free new post-tour users in both
    trigger_eligibility: adjacent
    surface: different        # interstitial slot vs in-tab overlay
    mechanism: adjacent       # gamified coupon creative + skippability vs an in-tab feature demo; only forced exposure is shared
    offer: different          # the step carried a discount coupon there; no offer inside the demo here
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent
  level: L3
  transferable: >
    L3 weak signal only — no product conclusion transfers. [fact] Non-skippable var3 produced
    ×8 engagement into the funnel and +150–160% layer revenue, with Android retention D1
    −9.15% (p=0.012); iOS var2 ARPU +26.5% (p=0.011) on a small absolute increment
    (forecast +$474/day) [T1-07, mixed/killed]. [interpretation] The source team read a
    monetization/retention trade-off of non-skippability. Use here strictly for sizing the
    retention guardrail, for choosing an early (D1) stop-rule, and for expecting engagement
    and intent to diverge in the readout.
  not_transferable: >
    Anything product-level: whether removing the skip helps or harms money in this case does
    not follow from this card, and it may not move the launch verdict. All magnitudes. The
    retention cost was measured on Android D1 in a gamified coupon arm, not iOS D14 in a
    feature demo. The source page flags var2 internals as anomalous (−75–77%
    interstitial→banner, unexplained) and pending-trial maturity as undocumented.
  sizing_prior: >
    prior — one forced-exposure arm showed a single-digit relative D1 retention loss [T1-07];
    order of magnitude for guardrail sizing and stop-rule design only.
```

## B. Design & measurement checklist
- **Goal metric vs touched surface (P-11):** Total ARPU/exposed spans both branches while the treatment touches only Chords; add Chords-branch ARPU/exposed as the touched-scope metric, and keep Total as the dilution/cannibalization read.
- **Guardrail baseline:** the design row uses Retention 14d 42.14% while the exp #7622 control read 37.58% — reconcile the cohort definition before sizing; the sample depends on it.
- **MDE column units:** the retention row states MDE 0.020 alongside a −2.37% detectable lift on a 42.14% baseline (≈1.0 pp). Publish which one the calculator used.
- **Delivery/exposure gate (P-12):** verify every demo step fires; measure fail-forward and skip rates (Simplify unavailable for ~27% of songs); `from_tour` is not implemented on any app event today — implement and verify before launch.
- **SRM/activation:** App Experiment Start must fire once per eligible user in every arm from the same code path, including control; check SRM at the activation event and exposure parity daily, not once.
- **Maturity (P-13):** the goal is ARPU at 14 days on a trial-bearing Paywall 2 — apply the pending-trial gate (>5%) before any read; Retention 14d matures 14 days after the last enrolment, so the decision date is enrolment days + 14.
- **Attribution (P-14):** flag purchases with `demo_unlock = 1`; the temporary unlock must not write to user rights; quantify any targeting or tracking defect before attributing a lift to it.
- **Guardrails and stop-rules worth adding:** Paywall 2 access CR, Tab View 60s, 14d refunds/cancels, D1 retention as the early proxy, and an explicit rule that iOS results do not license an Android rollout (Android was excluded for measured retention loss).

## C. Design changes that would most improve expected value
1. Re-size Retention 14d on the approved margin, or convert it into a pre-registered non-inferiority test at a margin the product owner signs — whichever is chosen, the number must exist before enrolment starts.
2. Pre-register the Chords branch as the primary analysis population, with the Tabs branch (identical to B by design) as the within-experiment composition/placebo check.
3. Pin one activation event, fired from the same code path in all arms, and gate the read on a 48-hour SRM/exposure-parity check.

## D. Findings without a price
- The fast-clicker slice is defined only as "e.g. every step below a threshold" — the threshold and the readout rule are not fixed, so the slice can be drawn after seeing the data.
- The QA case where no tutorial feature is available for the song reproduces variation B inside the test arm; how those users are treated in the primary analysis is not stated.
- `from_tour` is a new parameter on existing events across the app; its rollout risk to other reports is unassessed.
- The card's "control" is not pinned to a flow (pre-#7622 experience or the rolled-out Variation B); the baselines quoted come from two different tables.
