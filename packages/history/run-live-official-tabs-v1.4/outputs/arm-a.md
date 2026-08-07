# MAIN

## Verdict
Redesign before launch — the card's own goal ("hold the Variation B level while recovering retention") is a non-inferiority claim against an arm that does not exist in this design, and the binding guardrail is powered at twice the decision threshold, so the two-arm Iteration #1 cannot answer its own question no matter how it comes out.

## Predicted outcome
[ungrounded assumption — there is no evidence base in this prompt] Direction: ARPU per exposed most likely stays positive versus control but attenuated relative to B, because the demo inserts delay and a satiation moment before Paywall 2; Retention 14d most likely improves versus B but stays below control. What would surprise me: retention landing at or above control *while* ARPU holds ≈+20% — that combination would mean the paywall-pressure and retention channels are separable, which the card itself says is unconfirmed (Variation C added information and did not improve retention). Also surprising: demo completion above ~90%, given a forced, no-close, four-step gate.
no direct analogs

## What this experiment cannot show
- [computed] Only the Chords branch sees the demo (78% of exposed), and the full flow needs Simplify, unavailable for ~27% of songs, so at most `78% × (1 − 27%) ≈ 57%` of exposed users can see the complete demo. A whole-arm readout therefore cannot separate "the demo does not work" from "the demo was diluted to ~57% coverage"; a Chords-only retention readout needs `38,147 / 0.78 ≈ 48,900` per arm, i.e. `39 / 0.78 ≈ 50` days.
- [computed] The guardrail is sized to detect `42.14% × 2.37% ≈ 1.0 pp`, but the working decision margin is −0.5 pp; halving the detectable difference multiplies sample by `(1.0 / 0.5)² = 4` → `38,147 × 4 ≈ 152,600` per arm, `39 × 4 ≈ 156` days. So a true −0.5 pp loss will be non-significant, and "no significant drop" must not be read as "within margin".
- [computed] The reach numbers contradict each other: `38,147 × 2 / 7,700 ≈ 9.9` days versus the stated 39 days, while #7622 ran at `24,500 × 2 / 22 ≈ 2,230` exposed/day. Until reconciled, the card cannot state whether this is a ~10-day or a 39-day (+14 days maturity ≈ 53 days) commitment.
- [computed] The MDE column does not reconcile with baseline × lift for any metric: `0.68 × 20% = 0.136 ≠ 0.032`; `6.49% × 13% ≈ 0.84 pp ≠ 0.033`; `3.76% × 14% ≈ 0.53 pp ≠ 0.027`. Sample sizes cannot be verified from the card as written.

## Product proposals
no grounded product proposal
- [ungrounded] Research whether the retention loss is caused by paywall friction or by unmet in-tab value: instrument #7622's non-purchaser cohort (81%, −1.79 pp [fact]) for post-paywall behaviour before adding another pre-paywall step.
- [ungrounded] Research a Tabs-branch equivalent (Smartscroll/Autoscroll) — the card reports Tabs demand exists but the design gives that 22% nothing, which both dilutes the arm and leaves a segment untreated.
- [ungrounded] Research a non-gated variant (skippable demo, ✕ close available) so the forced-gate cost can be separated from the demo-content benefit.

## Top risks & failure modes
- Mechanism unconfirmed: Variation C showed more explanation did not recover retention [fact]; this iteration is a heavier member of the same family, so a null result will again be uninterpretable.
- Forced gate: no ✕, disabled UI, feature tap as the only exit, 8-second locked Play — plausibly converts a retention problem into a frustration problem for exactly the non-purchasers already losing retention.
- Temporary unlock then removal: paid features are unlocked for the demo and taken away at Paywall 2 — a loss-aversion path to worse retention and to refunds if users believe they bought what they sampled.
- Exposure-event ambiguity (Gift Offer Close vs App Experiment Start, plus new "trial-eligible / did not skip tour" conditions) breaks both SRM diagnosis and comparability with #7622 — and the whole verdict rests on that comparison.
- Fail-forward silently skips unavailable steps, so "treatment" is a distribution of 1–4-step experiences; without per-user step-coverage flags the arm average is not attributable to any specific demo.

## Non-monetization effects to instrument
- Positive: feature adoption after the first session (Simplify / backing track / strumming usage on days 1–14, `from_tour = 0`), Tab View 60s (the card names Paywall 2 → Tab View 60s as the largest later loss, 34–40%), and session depth on day 1. Instrument as directional wins, not just guardrails.
- Positive: reduced upstream tour abandonment if the demo makes the free tier feel usable — track Tour How To Play Success → Tab Official Open completion.
- Negative: refunds/cancellations within 14 days (segment by `demo_unlock = 1`), app-store rating and uninstall rate on day 0–1, crash/ANR during backing-track download.
- Stop-rules to add: halt on refund rate above control by a pre-registered margin; halt on demo `fallback = 'error'` above a pre-set share of steps; halt on D1 retention drop (faster signal than 14d); daily SRM check.

## Blocking design fixes
1. Add the third arm (Variation B) — without it "hold the B level" is untestable, and pre-register it as a non-inferiority test with an explicit margin.
2. Approve the retention margin first, then power for it (or accept an explicitly wider margin) — currently the decision threshold is half the detectable difference.
3. Fix one canonical exposure event across implementation, admin config and analytics spec, and reconcile the 7,700/day reach figure with the 39-day plan before sizing anything.

# APPENDIX

## B. Design & measurement checklist
- **Goal/surface match.** Goal is Total ARPU/exposed at 14 days on the whole arm, but the intervention touches only the Chords branch (78%) and only steps whose features exist. Pre-register both ITT (all exposed) and the Chords-branch analysis, with the branch analysis powered separately.
- **Baseline consistency.** Retention sizing uses 42.14% while the #7622 iOS control is 37.58% (a 4.56 pp gap) and ARPU sizing uses $0.68 while #7622 control is $0.66. Re-derive all four sample sizes from one agreed baseline source and publish the variance assumption.
- **Exposure gate.** `App Experiment Start` must fire from one code path in every arm, including control, and its conditions (never subscribed, trial-eligible, did not skip tour) must be identical to what #7622 used, or the historical comparison is invalid. Verify no demo-side logic can gate the activation event.
- **SRM / activation.** Daily SRM on the activation event and on `Tab Official Open`; check that `Tab Official Open` feature flags (`has_backing_track`, `has_strumming`, `has_simplify`) fire identically in control (they must, for a like-for-like coverage comparison).
- **Coverage instrumentation.** Per user, record how many demo steps were *eligible* and how many were *shown*; report the arm effect stratified by eligible-step count. Without this, fail-forward and song-level feature availability confound the readout.
- **Maturity horizon.** Retention 14d requires 14 days after the last enrollment; with 39 days of enrollment the readout is ~53 days out (~45 with a 31-day three-arm enrollment). ARPU at 14 days needs the same treatment — do not read either metric on the mixed-maturity cohort, and pre-register the mature-cohort definition (#7622's snapshot vs mature readings differed: −1.84 pp vs −1.60 pp).
- **Multiplicity.** One goal, one binding guardrail, three proxies, plus a fast-clicker slice and a level slice — pre-register which comparisons are confirmatory (goal + guardrail only) and treat the rest as exploratory.
- **Guardrails worth adding.** Refund/cancellation rate; D1 and D7 retention as early indicators; demo error rate; disabled-tap rate during Play (already tracked — set a threshold that means "users feel trapped"); paywall view rate per exposed (to detect users lost inside the demo).
- **QA.** The all-features-unavailable case must be byte-identical to Variation B's experience, and must still fire the activation event; verify `demo_unlock` never writes to user rights.

## C. Design changes that would most improve expected value
1. **Three arms with a pre-registered non-inferiority margin on ARPU versus B**, plus a superiority test on Retention 14d versus B. This is the only structure in which "preserve monetization, recover retention" is a decidable claim; accept the ≈31-day enrollment the card already anticipates.
2. **Make the demo skippable (✕ close / Continue always available) and log the skip.** This converts the forced-gate risk into a measured variable: completers vs skippers become an instrumented contrast rather than an unmeasured confound, and it removes the largest plausible retention-harm channel from the treatment itself.
3. **Stratify randomization (or at minimum the readout) by format choice and by song feature availability**, so the Chords branch has its own powered arm and the 22% Tabs users do not silently dilute every headline number.
