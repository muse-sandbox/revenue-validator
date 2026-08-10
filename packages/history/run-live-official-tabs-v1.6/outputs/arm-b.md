# MAIN

## Verdict

**Redesign before launch** — the idea is worth a slot, but a two-arm design sized on a control contrast cannot answer the question the card actually asks (did in-tab context preserve Variation B's monetization while recovering retention), and the retention guardrail is sized at twice the loss the team says it will accept.

## Findings

- **[stop]** [topic: b-arm-absent-arpu-resolution] We spend the slot and get a number that reads as a win over control whether the demo held B's lift or ate most of it. *If:* the run stays two-armed with the goal sized on a 20.00% difference versus control. *Mechanism:* [computed] B's mature readings were +22.8% and +24.2%, so the gap between "held B" and merely clearing the detectable step is 24.2% − 20.00% = 4.2 pp of relative lift, about a fifth of what this design resolves (4.2 / 20.00 ≈ 0.21). *Consequence:* outcomes that differ by half of B's effect all return the same "significant versus control" verdict. *Price:* decision impossible — the mechanism question stays open. *Fix:* add the Variation B arm and size the goal on the B-versus-demo difference.
- **[stop]** [topic: retention-guardrail-margin-power] We spend 39 days of enrollment and come back with a retention result that cannot clear the launch condition. *If:* the guardrail keeps the working −0.5 pp margin and the sample stays at 38,147. *Mechanism:* [computed] the sizing detects 2.37% of a 42.14% baseline: 42.14% × 2.37% ≈ 1.0 pp, and 1.0 / 0.5 = 2× the margin the card names. *Consequence:* a non-significant guardrail stays compatible with twice the loss the team said it would accept, so "within the approved margin" can be declared on no outcome. *Price:* decision impossible. *Fix:* approve the margin as a number first, then size retention as a non-inferiority test bounded by it.
- **[stop]** [topic: exposure-boundary-cohort-mismatch] The retention cohort we compare turns out to be a different population from the one the sizing describes. *If:* implementation and admin configuration ship with the two exposure events the card still lists as open. *Mechanism:* [computed] the guardrail baseline here is 42.14% while the #7622 control at the same stated boundary read 37.58% — 42.14 − 37.58 = 4.56 pp apart, roughly 2.5× the 1.84 pp loss the experiment exists to recover (4.56 / 1.84 ≈ 2.5). *Consequence:* the ARPU denominator and the retention baseline describe populations that cannot be lined up with the reference experiment. *Price:* experiment slot. *Fix:* freeze one boundary, re-measure the baseline on it, re-run the sizing.
- **[improve]** [topic: chords-branch-dilution-readout] A fifth of the arm carries no demo at all and shrinks whatever the demo does to the goal number. *If:* whole-arm Total ARPU / exposed stays the only pre-registered goal. *Mechanism:* [computed] the demo runs on the Chords branch only — 78% — and 78% × (1 − 27%) ≈ 57% of the arm reaches the Simplify step, while the 22% Tabs branch sees tab → paywall as before. *Consequence:* a flat goal will not separate "the demo is neutral" from "the demo moved Chords and Tabs diluted it", and the format choice exists only where the guided flow runs, so control holds no matching subgroup. *Price:* share of the expected effect — 22% of the arm cannot move it. *Fix:* pre-register the Chords-branch contrast against the B arm as primary, whole-arm ARPU as the net check (P-11).

## What you decide

- **[product owner]** Whether this question is worth a three-arm run booked past 39 + 14 = 53 days to a mature read; the in-run revenue at risk is bounded by 38,147 × ($0.77 − $0.66) ≈ $4.2k.
- **[product owner]** The acceptable Retention 14d loss, as a number, before any re-sizing — that number sets the run length.
- **[analyst]** One canonical exposure event, and the baseline re-derived on it.
- **[analyst]** The primary readout scope and the pre-registered non-inferiority rule for retention.

## Product proposals

- **[mechanic]** [topic: demo-after-paywall-dismissal-nonbuyers] *If:* the demo moves behind the Paywall 2 dismissal, aimed at the 81% who reach the paywall without purchasing and carry the −1.79 pp, where the card's own research says the chooser already improves the 34–40% who never reach Tab View 60s. *Grounds:* [fact] T2-07 (L2 card below) measured a pre-offer demo losing conversion along the whole funnel — access CR −36% iOS / −28.5% Android, banner click→purchase −22%/−26%. *Then:* Retention 14d higher than Variation B with members → subscribers unchanged.
- **[segment]** [topic: level-slice-eligibility-intermediate] *If:* user level becomes a decision segment instead of an analytical slice, with Intermediate — where the card places the iOS harm behind the 1.60 pp full-cohort loss — powered as the primary retention read. *Grounds:* [fact] T2-07 concentrated its loss in beginners (−42.1% against −36% overall), which is what separated a bad mechanic from a badly targeted one. *Then:* Retention 14d on the level that keeps the demo higher than the whole-arm number.

## Non-monetization effects to instrument

- [topic: forced-steps-early-churn-signal] Forced steps (no ✕, feature tap the only exit) may push abandonment inside the demo; equally, the 8-second Play with unlocked features may raise tab engagement. Instrument demo-start → Paywall 2 View, dwell_ms, Disabled Tap, Tab View 60s, Retention 1d/7d. Stop-rule: halt if Retention 1d falls below control by the approved margin.
- [topic: temporary-unlock-expectation-refunds] The client-side unlock may raise refunds, cancels and support contacts once features re-lock, and may equally raise purchase intent among demo_unlock = 1 users. Instrument refunds/cancels 14d split by demo_unlock, support contacts. Stop-rule: refunds 14d above a pre-set bound.
- [topic: first-session-content-engagement] The demo consumes the first-session song moment: return-to-tab and 3+ tabs weekly may rise, song search and choice may fall. Instrument Tab View, Tab View 60s, 3+ tabs/scores weekly, day-2 return to the same content_id.

## Closest analogs

- **T2-07** (partial): a 10-second feature demo between the feature tap and the paywall cut access conversion 36% (iOS) / 28.5% (Android), worst among beginners; it differs here because our flow has no exit bypassing Paywall 2 and the demo follows a format choice rather than a revealed feature intent.
- **T1-07** (weak signal only, used for guardrail and instrument design): a forced non-skippable pre-paywall step on the same new-post-tour audience multiplied funnel engagement and layer revenue but cost 9.15% of Android D1 retention; the mechanism there was a gamified coupon in the interstitial layer, so no product conclusion is carried over.
- These two point opposite ways on interactive pre-offer steps — `evidence is mixed`: the negative side is where the step delays something the user has just asked for (T2-07), the positive side where it adds a novel interaction with nothing pending (T1-07), and the retention cost in T1-07 appeared at D1 on Android, not at iOS Retention 14d. This case sits on the negative side by placement and on the positive side by content, which is exactly why the third arm decides it.

## Predicted outcome

Total ARPU / exposed above control, most likely landing between control and B's mature +22.8%/+24.2%, with wide uncertainty and no way to place it against B. Retention 14d above B's 35.74% and below control — the loss narrows rather than disappears. It would surprise me if Retention 14d matched control while members → subscribers held B's +13.11%, or if a material share of the demo arm never reached Paywall 2.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T2-07 (ab 6806; 2025-12; SRM ok, duration/sample under design, negatives significant anyway; significant-negative; killed)
  axes:
    flow_stage: different        # S1–S3 feature-gate vs S3–S4 first-session post-decline flow
    segment: adjacent            # free never-subscribed App vs free never-subscribed iOS first session
    trigger_eligibility: different  # feature tap (revealed intent) vs gift-offer close
    surface: different           # feature paywall with preview+timer vs in-tab step overlays
    mechanism: exact             # a step showing the paid feature inserted between the user's action and the offer
    offer: adjacent              # standard Pro offer behind both
    behavior: adjacent           # forced wait/interaction before the offer
    metric: adjacent             # feature→access % vs ARPU/exposed + members→subscribers
    money_chain: adjacent        # App free: exposure → paywall → purchase
    guardrails: different        # no retention guardrail there; Retention 14d binding here
  segment_monetization_state: exact
  money_chain_link: different    # there: intent → paywall access; here: exposure → Paywall 2 purchase, arrival structurally guaranteed
  platform: adjacent             # iOS+Android vs iOS, mechanism platform-agnostic
  level: L2
  transferable: >
    [fact] Access CR −36% iOS (p=0.00) / −28.5% Android (p=0.008); losses along the whole
    funnel (conversion to banner −10%/−18%; banner click→purchase −22%/−26%); beginners iOS
    −42.1%; AOV +14.2% / ARPPU +17.9% through mix shift. [interpretation] The source team read
    it as captured intent being deferred by a step. [hypothesis] Here, a multi-step demo between
    the tab the user asked for and Paywall 2 pushes members → subscribers below B's +13.11%
    rather than holding it, and the loss concentrates in a user-level slice rather than spreading
    evenly — direction only, with real uncertainty because the placement differs.
  not_transferable: >
    All magnitudes (−36%, −28.5%, −42.1%, +14.2%) — they are not predictions for this case.
    The access-CR mechanism cannot repeat in the same form: this flow has no exit that bypasses
    Paywall 2, so the equivalent loss can only appear as app abandonment mid-demo. T2-07 followed
    a revealed feature intent; this demo follows a format choice. T2-07 carried no retention
    guardrail and ran under design sample (Android 4 of 10 days), so it says nothing about
    Retention 14d. Free never-subscribed only; no transfer to ex-paid.
  sizing_prior: >
    prior — a step inserted before an App offer moved its own step conversion by tens of percent,
    not single digits; use only to set the floor on the demo-start → Paywall 2 View instrument.
  conflict: >
    Points the opposite way to T1-07 below on interactive pre-offer steps; T2-07 is the closer
    card and wins on placement. See [topic: demo-after-paywall-dismissal-nonbuyers].
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok, pending-trial maturity undocumented; mixed; killed)
  axes:
    flow_stage: adjacent         # S3–S4 interstitial layer vs in-tab step before Paywall 2
    segment: exact               # free new post-tour first-session users
    trigger_eligibility: adjacent
    surface: different           # interstitial slot vs official tab screen overlays
    mechanism: adjacent          # forced non-skippable pre-paywall step, but gamified coupon vs feature demo
    offer: different             # scratch-coupon discount vs unchanged Paywall 2 offer
    behavior: adjacent           # forced interaction to proceed
    metric: adjacent             # ARPU + layer CR vs ARPU/exposed + Retention 14d
    money_chain: adjacent
    guardrails: adjacent         # retention measured there at D1, binding here at 14d
  segment_monetization_state: exact
  money_chain_link: exact        # exposure → paywall access → purchase in the App first session
  platform: adjacent
  level: L3
  transferable: >
    Nothing product-level (L3 — weak signal for guardrails, measurement and sizing only).
    [fact] Non-skippable var3 produced ×8 engagement into the funnel and +150–160% layer revenue
    while Android D1 retention fell 9.15% (p=0.012); iOS var2 ARPU +26.5% (p=0.011) with a small
    absolute increment (forecast +$474/day). [interpretation] The source team read forced exposure
    as buying engagement at a retention price.
  not_transferable: >
    Every product conclusion, including the sign of the ARPU effect and whether removing the skip
    helps or hurts here. All magnitudes. The retention loss was measured at D1, on Android, on a
    gamified coupon — not at iOS Retention 14d on a feature demo. This card may not be used to
    change the launch verdict.
  sizing_prior: >
    prior — where forced exposure charged retention there, it was already visible at D1; a reason
    to carry Retention 1d/7d as an early-warning instrument rather than waiting 14 days.
  conflict: >
    Opposite direction to T2-07 on pre-offer steps; T2-07 is closer and decides. See
    [topic: forced-steps-early-churn-signal].
```

## B. Design & measurement checklist

1. **Goal metric vs touched surface (P-11).** The demo touches the Chords branch only; register a branch-scoped goal alongside whole-arm ARPU, and note that a branch contrast is identifiable only if an arm containing the format-choice step exists in the comparison (see [topic: chords-branch-dilution-readout]).
2. **Arms.** Resolve open decision 2 before sizing. The card states a third arm pushes binding enrollment to ≈31 days while the two-arm binding design is 39 days — that is internally inconsistent and must be recomputed.
3. **Exposure / activation (P-12).** One event, one code path, fired for control and test alike; verify the admin `experiment_event_start` matches the implementation; verify fire-once semantics; log exposed-but-not-enrolled.
4. **SRM and activation balance** on the enrollment event; also check balance of the Chords/Tabs split across arms (a differential split is itself a bug signal).
5. **Delivery gates.** Share of test-arm users who see ≥1 demo step; full-skip rate (all features unavailable); `fallback = 'error'` rate; per-step skip rate. A high full-skip rate silently converts the test arm into variation B.
6. **Maturity (P-13).** Both goal and guardrail are 14-day metrics; no rollout decision on an interim read; report pending trial share; ARPU@14d and Retention 14d must use the same enrollment cohort.
7. **Guardrails and stop-rules to add.** Retention 1d/7d as early warning; demo-start → Paywall 2 View floor; refunds/cancels 14d; Disabled Tap volume; fast-clicker slice with the dwell threshold fixed in advance, not chosen after the read.
8. **Artifacts (P-14).** `from_tour` is new on all app events — validate before the run; `demo_unlock` must not write to rights; confirm the `'arrows'` tooltip is not counted as a separate step in step-completion rates.

## C. Design changes that would most improve expected value

1. Add the Variation B arm and size the goal on the B-versus-demo difference rather than the control difference; recompute duration for three arms.
2. Convert the retention guardrail into a pre-registered non-inferiority test at the approved margin, with the baseline re-measured on the frozen exposure event.
3. Pre-register the branch-scoped readout and the delivery gates of B5 as decision inputs, so a full-skip-heavy run is identified as under-delivery rather than read as a null.

## D. Findings without a price

- The fast-clicker threshold on `dwell_ms` is defined only as "e.g. every step below a threshold"; without a fixed value the slice is post-hoc.
- The demo unlocks paid features for the session; whether the unlock persists across an app restart mid-flow is unspecified in the card.
- Feature availability is quantified only for Simplify (~27% of songs); backing-track and strumming availability are not stated, so the distribution of demo lengths cannot be anticipated.
- The QA scenario for "no features available" is named but no acceptance threshold is set for how often it may occur.

## E. Generic suggestions

- Pre-register the analysis plan (primary metric, slices, stopping rules) before enrollment opens.
- Run an A/A or a seven-day sanity window on the new events before the treatment goes live.
- Keep one owner for the decision rule so the read is not renegotiated after the numbers land.
