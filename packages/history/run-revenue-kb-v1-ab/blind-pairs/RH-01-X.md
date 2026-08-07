**Verdict: launch with changes.** The delivery channel and segment are well-grounded (ex-paid users are the corpus's strongest responders, and active replacement of the ad slot is a proven high-reach surface), but the trial-based offer contradicts the strongest ex-paid evidence in the base, and the 10-day run cannot read the revenue claim behind a 14-day trial.

**Predicted outcome.** The goal metric (eligible user → access %) should move up, driven by splash-source accesses — direction supported by P-08 and the winback line (T1-08, T2-05). The net revenue increment will be smaller than the model's +$0.042 ARPU, because the model assumes zero cannibalization and zero ad-revenue displacement, and because a granted re-trial historically converts to charge below average (T1-02). ARPU/revenue will be unreadable inside the 10-day window (all late-run trials pending). What would surprise me: a null on splash-source conversion itself (would contradict P-08's direction), or trial→charge at or above segment average (would contradict the T1-02 trial-quality warning).

**Top risks & failure modes**
- **Low-quality trials.** A generous granted trial pulls users who don't convert: interstitial trial→charge ran −13% (iOS) / −45% (Android) vs average in T1-02; the card's own prior research found a 6-month trial "not a strong enough incentive." Mechanism: generosity recruits low-intent starters (P-05 warning).
- **Additivity assumption is wrong by default.** The model books +54 accesses as pure increment; measured cannibalization on this exact surface was 34–63% (T1-02, P-02), and the splash also consumes the day's first ad impression — the segment's forgone ad revenue must be netted out.
- **Maturity blindness.** 10-day run, 14-day trial: the money chain (exposure→trial→charge) cannot mature in-window; T1-08's Total lift evaporated after control trials matured; T1-10 had 59–79% pending charges (P-13).
- **Attribution artifacts on new source values.** T1-09's ×4.6 winback lift was an attribution artifact; this design introduces four new source values on a low-volume segment — validate the counter before believing any funnel number (P-14).
- **Repeat-trial incentive and winback interaction** — users may learn that lapsing yields a fresh trial, and the splash may intercept the existing winback sequence (T1-08 won partly *because* it was sequenced after it, P-09). Risk to instrument (winback-offer conversion guardrail), not a blocker.

**Analogs.** No L1 direct analogs: no corpus case combines this mechanism (re-trial offer) with the ex-paid segment. Best evidence is L2.

```
analog:
  source: T1-02 (ab 6002/6128/6191, 2025-04..07; mixed/killed; iter1 bug-contaminated)
  level: L2
  matched: flow_stage S3–S4 exact; surface interstitial slot exact; mechanism
    exact (new-surface + offer-structure with extended 14d trial — nearly the
    same offer); money_chain exact (exposure→paywall→trial→charge)
  mismatched: segment different — free (iter2 clean) vs ex-paid; per §2.3 this
    blocks product-conclusion transfer
  transferable: warning — the extended trial pulled below-average trial→charge
    (−13% iOS / −45% And); cannibalization 34–63% of layer conversions; the
    iter1 bug showed ex-premium responding up to 13× (direction only), which
    is the very observation motivating RH-01
  not_transferable: all magnitudes; free-audience net-value conclusion (killed)
    does not transfer to ex-paid (P-08); 13× figure is bug-derived, not a prior
```

```
analog:
  source: T1-08 (ab 7487, 2026-05..07; significant-positive/rolled-out; SRM ok, trials matured)
  level: L2
  matched: flow_stage exact; surface interstitial slot exact; segment exact by
    monetization state (ex-paid)
  mismatched: mechanism different (deep-discount instant vs renewed trial);
    money_chain different (instant charge D0 vs trial→charge D14+) — blocks L1
  transferable: hypothesis — ex-paid respond strongly to an interstitial-slot
    offer (buyers +365.6%, segment ARPU +241%, direction only); warnings —
    Total lift lost significance after control trials matured; iOS dilution
    on the non-target segment bounded the net gain
  not_transferable: magnitudes; the winning offer STRUCTURE — T1-08 converted
    100% instant, no trial; its segment was winback-exhausted, higher-intent
    than "all expired"
  conflict: T1-08 (instant wins on ex-paid) vs RH-01's re-trial design; T1-02
    warns the trial arm of that tension is the weak one. Closer on segment,
    T1-08's structural lesson should weigh more.
```

```
analog:
  source: T2-05 (ab 6404/6614/6863, 2025-08..12; significant-positive/rolled-out)
  level: L2
  matched: mechanism family (offer-structure + lifecycle timing at a
    monetization-state transition); segment adjacent (canceling vs expired —
    same lapsing trajectory)
  mismatched: surface different (splash + Explore banner, not interstitial);
    flow_stage S8→S3 vs S3–S4; timing different (at cancel vs after expiry)
  transferable: hypothesis — offers at lapse-adjacent moments convert; the
    "without offer-sourced accesses" localization check (control segment n.s.)
    is the right causality read and RH-01 already includes it — keep it
  not_transferable: magnitudes (iOS-specific); Android expensive-plan negative;
    cancel-moment intent is hotter than post-expiry — direction may attenuate
```

```
analog:
  source: T1-09 (ab 7454, 2026-05..06; inconclusive/killed; iOS unreadable)
  level: L2 by axes (surface+flow exact, ex-paid branch offered +14d trial),
    but result_class inconclusive → measurement lessons only (rule 5)
  matched: surface/flow exact; ex-paid branch with a +14d trial offer
  mismatched: mechanism was message-only personalization, offers unchanged
  transferable: measurement only — the visible ×4.6 winback lift was an
    attribution artifact; winback-branch volumes were tiny (~70–165
    conversions/arm) — expect low counts and validate new source values
  not_transferable: any product conclusion (inconclusive)
```

**Design & measurement checklist**
- **Goal scope (P-11):** the goal is correctly segment-scoped, but "eligible → access" on *total* accesses dilutes +54 splash accesses into a base of 899. Make splash-source conversion the primary confirmatory read, with the total-segment metric and the already-configured "without offer-sourced accesses" segment as the cannibalization check.
- **Power table is internally inconsistent:** expected lift is 6% relative (~0.2pp absolute) but MDE is stated as 0.011 (1.1pp?) — as written the test can't detect its own projection. Reconcile before launch; also replace the "XX%" significance placeholder.
- **Delivery gate (P-12):** iOS-only ship — strike the Android columns from the success criteria or ship Android; do not report an Android "read."
- **Exposure verification:** 51.4% of the segment sees zero ads. Confirm the splash fires on first tab open *regardless of ad fill*, not only as ad-slot fallback — otherwise this repeats T1-01's no-fill trap (4 accesses total). Instrument delivered-reach vs eligible.
- **Maturity (P-13):** extend the read to run + 14 days; gate the revenue verdict on pending-trial share <5%. Add SRM on the exposure event and on splash-source funnel events; add 14d cancels/refunds and forgone segment ad revenue as guardrails, alongside the stated D7 retention/engagement.

**Changes that would most improve expected value**
1. **Add a discounted-instant arm (no trial)** — the corpus's winning ex-paid mechanism (T1-08, P-05), and the accidental discovery motivating this project was *instant charges* converting well, not trials. Testing only the re-trial leaves the stronger candidate unmeasured.
2. **Redefine success as matured net increment:** splash-source revenue minus cannibalized non-splash accesses minus displaced ad revenue, read after trial maturity — not the additive in-window ARPU model.
3. **Fix the power/goal inconsistency and pre-register the decision rule** (which metric, which scope, which horizon) before launch, so an in-window flat Total can't be misread as failure (T1-10's lesson).
