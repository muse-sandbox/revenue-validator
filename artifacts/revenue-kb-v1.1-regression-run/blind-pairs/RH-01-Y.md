**1. Verdict — launch with changes.** The idea is well-motivated by the team's own prior reactivation work, but the design has fixable flaws: a diluted goal metric, a run shorter than the trial's charge horizon, and exposure-accounting gaps that sank the prior attempts. (No KNOWLEDGE CONTEXT was provided, so everything below is general reasoning marked as ungrounded assumption; prior experiments are cited only as described in the card itself.)

**2. Predicted outcome.** Directionally positive on offer-sourced access conversion (the mechanism — high-reach owned slot × lapsed users who already demonstrated willingness to convert — is plausible), but the projected +54/+28 accesses will be hard to detect on the diluted "eligible user → access" metric, and ARPU at +6% is likely to land non-significant in 10 days (transfer hypothesis, high uncertainty; the card's own prior cancel-moment test got +22% ARPU at p=0.54). I would be surprised by a *negative* access conversion; I would not be surprised by a flat or noisy revenue read. A genuine surprise: a retention drop in this segment, since exposure is once/day replacing an ad, not adding pressure.

**3. Top risks & failure modes**
- **Metric dilution:** ~900 of 953 projected accesses are organic; the goal metric mixes them in, so the treatment signal is ~6% of the metric's own baseline. Underpowering by construction.
- **Immature revenue:** a 14-day free trial means charges occur ≥14 days after access; the 9–10-day run ends before any treatment-driven charge can land. Revenue/ARPPU/charges as reported at day 10 will be structurally biased toward control.
- **Exposure accounting failure (repeat offender):** both prior splash attempts missed goal partly due to <80% reach and "incorrect display accounting" (per the card). The fallback path (splash on ad-load error) further muddies who saw what and can exceed once/day.
- **Cannibalization of full-price organic re-subscription:** 3.35% of this segment converts organically; a free-trial offer may divert would-be full-price renewals into a delayed, cancellable trial. The "without offer-sourced accesses" segment partially covers this — watch it for a *drop*.
- **Ad-revenue displacement:** the splash consumes the first (for 77.7% of the segment, often the *only*) daily ad impression. Small absolute dollars, but it must be measured, not assumed.

**4. Analogs.** No KNOWLEDGE CONTEXT present — no analog cards can be emitted (rule 1).
no direct analogs

## Non-monetization effects to instrument
- **Retention (both directions):** negative — full-screen promo to lapsed users could suppress return rate; positive — users who reactivate typically engage more (ungrounded assumption). Instrument 7- and 14-day return rate for the eligible segment by arm; stop-rule: deprioritize-review if 7-day retention drops beyond the guardrail MDE.
- **Engagement:** track the stated 3+ tabs/scores-weekly guardrail plus tabs-per-day distribution (the 20% one-tab-per-day users see *only* the splash on treatment days). Positive side: reactivated subscribers' tab consumption may rise. Stop-rule on significant engagement decline in treatment.
- **Refunds/cancellations:** users granted a second trial on an annual SKU may cancel within 14 days (benign) or be surprised by the annual charge (refunds, support tickets). Instrument trial→paid conversion, cancel-within-trial rate, refund rate at 30/45 days. Stop-rule: refund rate materially above the segment's historical baseline.
- **Upper-funnel:** banner entry points on tab/song-results/search pages may shift navigation and search behavior. Instrument banner CTR by placement and search-session completion; positive shift (more purposeful sessions) is possible too.
- **Ad experience:** treatment users see one fewer ad; log ad impressions per user per arm to quantify displacement and any ad-frequency compensation.

**6. Design & measurement checklist**
- Replace or supplement the goal metric with **offer-sourced access rate among eligible exposed users**; keep total access as a cannibalization check. Recompute power against the undiluted metric (the stated MDE 0.011 vs a 0.2pp absolute projected lift looks inconsistent — verify units).
- Extend the readout horizon to run + ≥14 days (trial maturity) before any revenue verdict; pre-register that day-10 revenue is not decision-grade.
- Delivery gate: verify Splash View fires and reconcile against eligibility counts daily (SRM check on App Experiment Start); the prior tests' reach failures make this the single most likely silent killer.
- Cap the fallback path (ad-error → splash) or log it separately; it breaks the once/day contract and confounds arms.
- Fill in the "XX%" significance placeholder; confirm eligibility logic excludes users with an active subscription (the motivating discovery was itself a segmentation bug).
- Decide Android explicitly — it's sized in the model but not shipping; don't report Android projections as expectations.

**7. Changes that would most improve expected value**
1. Switch the primary metric to offer-sourced conversion among exposed eligibles and re-power the test.
2. Extend measurement to cover trial maturation (charges, cancels, refunds) before the launch/hold decision.
3. Add a per-user exposure reconciliation dashboard (eligible → activated → splash viewed) from day 1, with an SRM/reach stop-rule.
