**Evidence status:** no KNOWLEDGE CONTEXT was supplied, so I cite no past experiments and emit no analog cards. All numbers below are facts *as stated in the card* (exp #7622 readings, sizing table); everything I add is ungrounded general reasoning, marked as assumption or hypothesis.

## 1. Verdict

**Redesign before launch.** The design cannot deliver its own decision rule: the binding guardrail is a −0.5 pp Retention 14d margin, but the sizing detects ≈−2.4 pp (Q&A says −1.0 pp), and the primary goal ("hold the Variation B level") has no B arm in the experiment.

## 2. Predicted outcome

Hypothesis (transfer, uncertain): ARPU/exposed lands between control and B — directionally positive vs A, plausibly a partial regression from B's +20%, because the demo delays and softens paywall pressure for the Chords branch. Retention 14d: I expect improvement vs B but not full recovery to A; a forced, non-dismissible 3–4 step tutorial is as likely to add friction as to add perceived value (assumption — the awareness-gap mechanism is explicitly unconfirmed per Variation C in the card). What would surprise me: ARPU *above* B, or retention fully at control level with ARPU held — that combination would mean the demo added value without diluting paywall intent.

## 3. Top risks & failure modes

- **Guardrail is unfalsifiable as written.** Powered for −2.37 pp, decision margin −0.5 pp; a non-significant retention result will be misread as "within margin". Needs a non-inferiority test against a pre-registered margin, not a two-sided null.
- **Dilution by branch.** Only ~78% (Chords) get the demo, and steps skip when features are unavailable (~27% of songs lack Simplify); goal and guardrail are measured on 100% exposed, shrinking the true effect ~1.3× and inflating heterogeneity of dose.
- **No B arm.** "Hold B level" would be judged against historical #7622 numbers across a different time window — a non-randomized comparison confounded by seasonality, app version and pricing.
- **Forced-flow frustration.** No ✕, no Continue before the feature tap, whole UI disabled, "any other tap" during Play ends the demo — mechanically this can produce rage-taps and drop-off among exactly the non-purchaser majority (81% of cohort) where the retention loss was concentrated.
- **Exposure/instrumentation ambiguity.** The card alternates between Gift Offer Close and App Experiment Start as the canonical enrollment event; mismatched admin config vs client code produces SRM and non-comparable denominators. Baselines also disagree (Retention 42.14% in the sizing table vs 37.58% control).

## 4. Analogs

no direct analogs

## Non-monetization effects to instrument

- **Retention, both directions.** Positive: demo users may return for the features they saw (instrument D1/D3/D7 return, Retention 14d split by demo-completed vs demo-skipped vs Tabs branch). Negative: forced-flow abandonment. Stop-rule: halt if Retention 7d in the test arm is worse than B's observed level at ≥95% confidence.
- **Engagement.** Positive: Tab View 60s, Simplify/Transpose/Backing-track usage *outside* the tour (from_tour = 0) in the following 14 days; searches and second-song starts. Negative: session length shrinkage, disabled-element tap attempts. Stop-rule on Tab View 60s falling below B.
- **Refunds / cancellations.** The demo unlocks paid features temporarily; buyers may feel misled once rights revert. Instrument refund rate, trial-cancel rate and day-1 subscription cancellations by `demo_unlock`; stop-rule if refunds exceed control by a pre-set absolute margin.
- **Upper funnel / brand.** App Store rating and review volume, support tickets mentioning "can't close"/"stuck", uninstall rate on iOS. Stop-rule on uninstall-rate regression.
- **Fast-clickers.** Already planned: report the low-`dwell_ms` slice separately for both funnel and retention.

## 6. Design & measurement checklist

- Pre-register the primary analysis population as the **Chords branch** (goal + guardrail), with the all-exposed readout secondary; power on that population.
- Re-size for the decision margin actually used: −0.5 pp non-inferiority on Retention 14d requires far more than 38,147/arm; either accept a larger margin or accept a longer run and state it.
- Fix one canonical exposure event fired from a shared code path in all arms; run SRM checks daily on it, plus activation-rate parity.
- Set a maturity horizon: trial-to-paid conversion must be mature before the ARPU readout (the card itself shows snapshot +17.25% vs mature +22.8/+24.2%); read cohorts at equal age.
- Add strata by feature availability flags (row 2 events) so the "all steps skipped" cell is analysable as a within-test placebo.

## 7. Changes that would most improve expected value

1. Add the third arm (A / B / B+demo). Without it the goal metric has no valid comparator, and the whole "recover retention while holding ARPU" claim is untestable.
2. Give the tooltip a real exit (✕ or Skip) and instrument its use, converting a blocking risk into a measured one — it also removes the dead-end QA class.
3. Replace the two-sided guardrail check with a pre-registered non-inferiority margin plus a sequential stop-rule on Retention 7d as an early proxy.
