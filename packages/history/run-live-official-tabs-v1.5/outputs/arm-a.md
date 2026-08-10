# MAIN

## Verdict
**Redesign before launch** — the design tests a bundle (B funnel + demo) against the old control while the hypothesis is stated against Variation B, and the binding guardrail is sized at roughly twice the loss it is supposed to approve.

*No KNOWLEDGE CONTEXT was supplied, so this review has no access to past experiments beyond what the card itself reports; all general product reasoning below is explicitly an ungrounded assumption.*

## Findings

- **[stop] Two arms return one bundled verdict on funnel-plus-demo, and the demo's own contribution stays unmeasured.**
  Mechanism: the hypothesis is "hold approximately the Variation B level", but with only control and the demo arm, B exists solely as a historical reading from exp #7622 (different 22-day window, different seasonality); the card lists the third arm as an open decision.
  Consequence: a readout of "+X% ARPU vs control" that cannot say whether the demo added, cost, or did nothing versus B — and the same for the retention recovery, which is the entire point of the iteration.
  Price: `decision impossible`.
  Fix: add the B arm, or restate the goal as "bundle beats control" and drop every B-relative claim.

- **[stop] The guardrail decision lands on a −0.5 pp threshold the design cannot see.**
  Mechanism: `[computed]` the table's detectable retention change is `42.14% × 2.37% ≈ 1.00 pp`, while the working approval margin is 0.5 pp — so a true loss of exactly the margin, or of twice it, both return "not significant"; halving a detectable difference quadruples the sample, i.e. `38,147 × 4 ≈ 152,588` per arm and `39 × 4 ≈ 156` days. The card also states the guardrail three ways (−1.0 pp in the Q&A, −2.37 in the design row, MDE 0.020), which resolve to different decisions.
  Consequence: the guardrail passes by default; "within margin" and "twice the margin" are the same readout.
  Price: `decision impossible`.
  Fix: size it as a non-inferiority test against a margin the team actually approves first, and reconcile the three numbers.

- **[stop] A mismatched activation event costs the whole run its enrollment set.**
  Mechanism: the card alternates between `Tour Post Decline Gift Offer Close` (used for reach and enrollment) and the dedicated `App Experiment Start` (Analytics spec, admin `experiment_event_start`); the eligibility filters differ (never-subscribed, trial-eligible, tour not skipped).
  Consequence: the exposed cohorts in code and in the admin diverge, SRM becomes undiagnosable, and the 14d metrics attach to a population nobody defined.
  Price: `experiment slot`.
  Fix: freeze one canonical event, fire it from one code path in both arms, and QA the counts before ramp.

- **[improve] The retention half of the hypothesis rests on a mechanism iteration 3 already failed to confirm, so a null retention result yields no learning.**
  Mechanism: the card's own research says Variation C added information and choice and did not improve retention relative to B — the awareness gap is unconfirmed. The demo is the same "give more context" theory in an interactive wrapper, while the harm is concentrated in the 81% who saw the paywall and did not buy (−1.79 pp).
  Consequence: whichever way retention moves, the team cannot attribute it to awareness, so the next iteration starts from the same place.
  Price: `experiment slot`.
  Fix: pre-register the competing explanation (paywall pressure / bait from the temporary unlock) and a slice that separates it.

- **[improve] Roughly a fifth of the arm gets the control experience, so the measured effect shrinks before it reaches the readout.**
  Mechanism: `[computed]` the demo runs on the Chords branch only — `22%` of the arm (Tabs choosers) receives exactly the variation-B experience, and with Simplify unavailable for ~27% of songs only `78% × (1 − 27%) ≈ 57%` of the arm sees the full demo; the sizing assumes the 20% ARPU effect on 100% of the arm.
  Consequence: the ITT estimate is a blend of treated and untreated users; a branch effect large enough to matter can still read flat at the arm level.
  Price: `share of the expected effect`.
  Fix: make the Chords branch the primary analysis unit (both arms restricted to Chords choosers), keep ITT as secondary, and re-size on it.

- **[improve] The "hold the B level" target reads against three different B numbers, so any outcome finds a supporting one.**
  Mechanism: `[computed]` the card gives B's ARPU lift as +17.25% in snapshot and +22.8% / +24.2% mature — a spread of `22.8 − 17.25 = 5.55` to `24.2 − 17.25 = 6.95` pp of relative lift, against a goal window fixed at 14 days.
  Consequence: "approximately B" is chosen after the data arrives, and the goal becomes unfalsifiable.
  Price: `share of the expected effect`.
  Fix: name one reading and one horizon in the plan.

- **[improve] Enrollment takes about three times longer than the stated reach implies, and the guardrail readout arrives ~53 days out.**
  Mechanism: `[computed]` exp #7622 collected ≈24,500 per variation in 22 days at the same exposure point → `24,500 ÷ 22 ≈ 1,114` per variation per day, versus the stated ≈7,700 exposed/day; at the observed rate `38,147 ÷ 1,114 ≈ 34` days, and adding the 14-day metric maturity gives `39 + 14 = 53` days to a readable guardrail (more with a third arm).
  Consequence: the slot is booked for roughly a month and read almost two months out.
  Price: `days to decision`.

## What you decide
- **[product owner]** Which question this run answers: "does the demo beat B" (the third arm is then mandatory and the slot is longer) or "does the bundle beat control" (then the B-relative goal wording goes).
- **[product owner]** The retention line that actually blocks rollout — accept ~1.0 pp as the decision threshold at this sample, or fund the longer run for 0.5 pp. This is a business call, not an analyst call.
- **[analyst]** The canonical exposure event and the primary analysis unit (Chords branch vs whole arm), both pre-registered before ramp.
- **[analyst]** Whether the guardrail is tested as non-inferiority against an approved margin instead of a two-sided difference test.

## Product proposals
no direct analogs

no grounded product proposal

- **[ungrounded]** The branch key is format (78% Chords), but the card says the iOS harm concentrates in Intermediate users — worth checking whether level, not format, is the right eligibility or branching variable before this ships.
- **[ungrounded]** The temporary unlock of paid features may be an offer mechanic in its own right (a bounded feature trial around Paywall 2) rather than a tour step; nothing here establishes which direction it moves conversion or retention.
- **[ungrounded]** The Tabs branch (22%) gets no treatment while its demand sits in Smartscroll/Autoscroll — a symmetric demo there is untested and should not be assumed to behave like the Chords one.

## Non-monetization effects to instrument
- **Engagement, both directions.** `Tab View 60s` is the largest later loss (34–40% do not reach 60s); the demo may improve it (users arrive at the tab already oriented) or worsen it (8 seconds of Play consumed inside the tour). Instrument the transition split by branch and by `demo_unlock`.
- **Feature discovery, upside.** Backing Track / Strumming / Simplify usage in sessions 2–7 with `from_tour = 0` — the demo's plausible positive side-effect is durable feature adoption even where money does not move.
- **Frustration and the unlock hangover, downside.** Forced steps with no ✕ and a disabled UI plus paid features that vanish after the session: instrument `Tab Official Post Decline Demo Disabled Tap` rate, `fallback = 'error'` rate, session-2 return, uninstall, and store-rating prompts; report the fast-clicker slice from `dwell_ms` separately.
- **Refunds/cancellations.** The B gain was volume-driven (conversion, not AOV), so track trial-start → refund and first-period cancellation as a guardrail; more marginal buyers can mean more refunds.
- **Stop-rules to add.** Crash/ANR on the demo screens; `fallback = 'error'` above a pre-set share; D1 return in the demo arm below control by a pre-set margin; demo completion below a floor (the flow is broken, not tested).

## Predicted outcome
ARPU most likely holds near the B level versus control with a wide interval — a regression toward control is entirely possible if the demo dampens paywall pressure, which is the card's own stated main risk. Retention 14d most likely lands between B and control and reads "not significant" at this sample, which is the ambiguous outcome the design is built to produce. I would be surprised by a full retention recovery to control (that would contradict the iteration-3 finding that context alone does not fix it), and equally surprised by an ARPU drop below control (nothing in the flow removes a paywall).

# APPENDIX

## B. Design & measurement checklist
- **Goal metric vs touched surface.** The surface changes for Chords choosers only; the goal metric is measured on all exposed. Either restrict the primary metric to the branch or accept the dilution explicitly in the sizing.
- **Sizing baselines vs observed control.** The design table uses Retention 14d baseline 42.14% and ARPU $0.68, while the iOS control from exp #7622 reads 37.58% and $0.66 — a `42.14 − 37.58 = 4.56` pp gap that changes both variance and the pp↔relative conversion of the guardrail. Re-run the calculator on the observed baseline.
- **Internal consistency of the design table.** `Lift, %` and `MDE` do not reconcile with baseline × lift in any row (e.g. `$0.68 × 20% = $0.136` vs MDE 0.032). State the unit of the MDE column.
- **Duration consistency.** The Q&A says a third arm pushes binding enrollment to ≈31 days; the design summary already gives 39 days for the guardrail on two arms. Reconcile before quoting a slot length.
- **Delivery/exposure gates.** One canonical activation event, fired from the same code path in control and test, for users who never subscribed, are trial-eligible and did not skip the tour; verify it fires exactly once per user.
- **SRM/activation.** Daily SRM on the activation event; also check branch-share balance (Chords/Tabs ≈ 78/22) across arms — a skew there silently changes treated share.
- **Feature-availability stratification.** Log `has_backing_track` / `has_strumming` / `has_simplify` at exposure (row 2 already does) and pre-register the "all three unavailable" stratum as an as-treated control check — those users are variation B by construction.
- **Maturity horizon.** ARPU at 14 days is a snapshot; the card's own mature B readings are higher. Fix the analysis horizon and the last-enrollment cut-off before launch.
- **Guardrail form.** Non-inferiority test with a pre-approved margin, plus a pre-registered rule for what happens when the point estimate is inside the margin but the interval is not.
- **Stop-rules.** Crash/ANR, `fallback='error'` share, disabled-tap rate, D1 return, demo completion floor.
- **Client-side unlock.** QA that `demo_unlock` never writes to user rights and expires at paywall open, including on app kill mid-demo.

## C. Design changes that would most improve expected value
1. **Add the Variation B arm** and re-size; without it the run answers a question the team is not asking. If the slot cannot absorb three arms, change the stated goal instead of pretending B is measured.
2. **Convert the guardrail to a non-inferiority test** against a margin approved before launch, and re-size on the observed control baseline (37.58%) rather than 42.14%.
3. **Pre-register the Chords branch as the primary analysis population** in both arms (format choice exists in both), with whole-arm ITT as a secondary, so the effect is not diluted by the 22% who receive no treatment.

## D. Findings without a price
- The fast-clicker segment is defined only as "e.g. every step below a threshold" — the threshold is not fixed in advance, which makes the slice post-hoc.
- `from_tour` is not implemented on any app event today; it is a new client dependency on the critical measurement path with no stated fallback if it ships broken.
- `Tab Official Post Decline Demo Step View` does not fire for steps skipped due to feature unavailability, so the denominator for step-level funnels has to be reconstructed from row 2's flags — workable, but state the reconstruction rule in the analysis plan.
- The QA note covers the all-features-unavailable case but not the mid-demo interruption cases (backing-track download failure after the tooltip switched, app backgrounding during the 8-second Play).
- The Results/Forecast sections are still the unedited template; harmless pre-launch, but the significance table lists Retention 7d and "Users with 3+ tabs weekly" rather than the metrics this experiment actually declares.
