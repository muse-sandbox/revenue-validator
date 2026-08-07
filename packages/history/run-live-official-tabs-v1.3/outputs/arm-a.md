# MAIN

## Verdict
**Redesign before launch** — the two claims that define success ("hold approximately the Variation B ARPU level", "improve Retention 14d versus Variation B") are both contrasts against an arm that is not in the experiment, and the binding guardrail threshold (−0.5 pp) is half the retention MDE the design actually buys (−1.0 pp).

no direct analogs

*(No KNOWLEDGE CONTEXT was supplied, so everything below is ungrounded general reasoning plus the card's own numbers — not evidence from past experiments. Facts = card measurements; interpretations = source-team readings; everything about this experiment = hypothesis.)*

## Predicted outcome
Total ARPU/exposed: likely above control and directionally similar to B, but with wide uncertainty about whether the *full* B level survives — the demo adds a mandatory pre-paywall surface where low-intent users can abandon, so partial regression toward control is at least as likely as a clean hold (hypothesis). Retention 14d: I expect it to stay below control, with most of the B-sized gap intact; recovering ≥half of the 1.60 pp would surprise me. What would surprise me most: retention at or above control, or ARPU below control.

## Product proposals
no grounded product proposal

- **[ungrounded]** Research whether the unlocked-feature experience belongs *after* Paywall 2 dismissal rather than before it — the card's own research says the post-dismiss chooser already improves the Paywall 2 → Tab View 60s transition, which is where the retention loss lives.
- **[ungrounded]** Research whether "Intermediate iOS, paywall-non-purchaser" can become an eligibility rule rather than a readout slice, since the harm is concentrated there.
- **[ungrounded]** Research a time-boxed unlock (keep Simplify/backing track for the rest of session 1) versus a demo that shows then removes them; direction on ARPU is unknown.

## Top risks & failure modes
- **The remedy targets an unconfirmed mechanism.** Variation C added information and choice and did not improve retention over B (fact, card); the team reads the awareness gap as unconfirmed (interpretation). This demo is more explanation with *less* agency (hypothesis).
- **Teaser-and-takeaway.** The loss in B is concentrated in the 81% who saw the paywall and did not buy (fact). Unlocking Simplify/backing track and relocking them at Paywall 2 may sharpen deprivation for exactly that majority (hypothesis).
- **Cannibalized recovery.** Spending the first-tab novelty inside a forced demo may reduce the post-dismiss tab session — the transition the card names as the largest later loss (34–40%).
- **Dilution.** Enrollment at gift-offer close; treatment reaches only Chords (~78%), further reduced by feature availability (Simplify absent on ~27% of songs) and fail-forward skips. A null on the exposed cohort will be uninterpretable.
- **Trapped users.** No ✕, no skip, disabled UI, forced feature tap: abandonment moves *upstream* of Paywall 2, moving ARPU/exposed through lost exposure rather than persuasion.

## Non-monetization effects to instrument
Upside to measure, not just downside: feature discovery may lift day-2–14 Simplify/backing-track/Autoscroll usage and tab depth — instrument feature-use rate and Tab View 60s per user by day, plus songs opened in sessions 2–3. Downside: first-session abandonment and D1 uninstall/session length — instrument step-level drop, dwell_ms, disabled-tap rate. Expectation effects run both ways: refunds and trial-cancel rate may rise (demo oversells) or fall (demo sets expectations) — instrument refunds, trial→paid, day-7 cancel, store-rating prompt acceptance and support-ticket volume. Stop-rules to add: demo error/fallback rate, tab-screen crash/ANR, disabled-tap rage rate, D1 retention, each with a pre-set auto-pause threshold.

## Blocking design fixes
1. Add a concurrent Variation B arm; make new-vs-B the primary contrast (non-inferiority on ARPU, superiority on Retention 14d), keeping control as anchor.
2. Set a retention non-inferiority margin the study is powered for (MDE is 1.0 pp, not 0.5 pp) and reconcile the 42.14% design baseline with the 37.58% observed control.
3. Freeze one canonical activation event (App Experiment Start, same code path in all arms) and pre-register the Chords-branch primary analysis with its own sizing.

# APPENDIX

## B. Design & measurement checklist

**Goal metric vs touched surface/segment**
- Goal is ARPU/exposed on the full exposed cohort, but the intervention touches only the Chords branch (~78%), and within it only songs that have at least one demo feature. Pre-register: (a) primary = Chords-branch ITT, (b) secondary = full exposed cohort. Size on (a).
- Format choice and song choice occur before the demo and are identical across arms, so stratifying by `Tour How To Play View value` and by the new `Tab Official Open` availability flags is legitimate — but verify empirically that the format split (78/22) and flag distributions are balanced across arms; if they are not, treatment is leaking upstream and the stratified read is invalid.
- ARPU "hold B level" is a non-inferiority claim. Powering for +20% vs control means a regression from +20% to +10% would still read "significant vs control" while being a failed hypothesis. Define the ARPU non-inferiority margin against B explicitly (e.g. no worse than −5 pp of relative lift) and size for it.
- Retention 14d design baseline (42.14%) differs from the exp #7622 control (37.58%) by ~4.5 pp. Sizing is sensitive to this; document which population/window each comes from before re-running the calculator.
- ARPU baseline is $0.68 in the design table and $0.66 in the pitch. Trivial, but reconcile so the sizing is reproducible.

**Delivery / exposure gates**
- Resolve the exposure-event ambiguity the card itself flags (Tour Post Decline Gift Offer Close vs App Experiment Start). Both the admin `experiment_event_start` and the client must point at one event.
- Fire the activation event from the same code path in every arm including control, strictly before any branch-specific code runs, and log arm assignment on it.
- Confirm eligibility conditions ("never subscribed, trial-eligible, did not skip the tour") are evaluated identically in all arms and are not affected by anything downstream of assignment.
- Verify no exit bypasses the paywall (the QA case where all three features are unavailable must reproduce tab → Paywall 2 exactly), otherwise control and variation differ in paywall-view rate for a reason unrelated to the hypothesis.
- Confirm the demo unlock is client-side only and writes nothing to user rights; add a check that no purchase/entitlement event fires with `demo_unlock = 1` in a way that would misattribute revenue.

**SRM / activation**
- Daily SRM check on the activation event, plus SRM on the Chords/Tabs split within each arm.
- Activation-rate parity: share of gift-offer closers who fire App Experiment Start must match across arms; a gap means differential instrumentation, not a real effect.
- Check for duplicate firing (event is specified as once per user) and for reinstall/device-reset re-enrollment, since reinstalls stay eligible.

**Maturity horizon**
- Retention 14d needs enrollment + 14 days before the last-enrolled user matures; the 39-day figure appears to be enrollment days only. Budget enrollment + 14 days + reporting.
- ARPU at 14 days is trial-heavy: exp #7622 read +17.25% in snapshot and +22.8%/+24.2% mature (fact). Fix the ARPU readout horizon in advance and pre-commit to reading the mature window, not the snapshot, for the go/no-go.
- If a third arm is added, enrollment rises to ≈31 days per the card; recompute after the arm and margin decisions, not before.

**Multiplicity and decision rules**
- One goal, one binding guardrail, two proxies, plus format branch, level slice and fast-clicker slice. Pre-register which are confirmatory (goal + guardrail) and which are exploratory (everything else); no alpha spending on exploratory slices, and no stopping on them.
- Guardrail test should be one-sided non-inferiority at the declared margin, not a two-sided significance test — "not significantly worse" at 1.0 pp MDE is not the same as "within 0.5 pp".
- The Intermediate-user slice (where iOS harm concentrates) will be badly underpowered as a slice; declare it exploratory up front so a null there is not read as safety.

**Guardrails and stop-rules worth adding**
- Paywall 2 view rate per exposed user (detects abandonment moving upstream).
- Demo completion rate, per-step drop, and `fallback = 'error'` rate — auto-pause above a pre-set error threshold.
- Disabled-tap rate during the 8-second Play (rage proxy) and `exit_reason = 'play_interrupt'` share.
- Tab View 60s split into pre-paywall and post-dismiss, so cannibalization is visible.
- Crash/ANR on the tab screen; refunds and trial-cancel rate; store-rating prompt outcomes.
- D1 retention as an early-warning guardrail, since D14 arrives too late to stop harm.

## C. Design changes that would most improve expected value

1. **Three arms (A / B / new), with new-vs-B as the primary contrast.** Without it the experiment answers "is this better than control" — a question already answered — instead of "does this keep B's money while returning retention". Historical comparison to #7622 is time-shifted across app version, seasonality and cohort mix, and cannot carry a ±0.5 pp retention judgement.
2. **Replace the two-sided, control-anchored sizing with an explicit non-inferiority design on both primary claims**, sized on the Chords branch: ARPU non-inferior to B at a declared margin, Retention 14d superior to B and non-inferior to control at a margin the sample can actually resolve. If the required sample is unaffordable, say so and pick the larger margin deliberately rather than inheriting a 0.5 pp threshold the design cannot test.
3. **Add a low-cost skip variant of the demo as a fourth arm, or at minimum instrument forced-flow cost directly.** The whole retention thesis rests on value delivered before the paywall; the coercive delivery (no ✕, disabled UI, mandatory taps) is the part most likely to backfire, and as designed the experiment cannot separate "the content didn't help" from "the forcing hurt".
