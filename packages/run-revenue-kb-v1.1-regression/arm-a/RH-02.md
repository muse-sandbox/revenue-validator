**1. Verdict — launch with changes.** The idea is coherent and builds on the team's own stated prior learnings, but the design has a goal-metric/exposure mismatch and a power table that appears inherited rather than recomputed for this variant; both should be fixed before launch. (I have no KNOWLEDGE CONTEXT, so all reasoning below is ungrounded assumption from general experimentation practice, not from specific past experiments.)

**2. Predicted outcome.** Direction on ARPU is genuinely uncertain: the splash should add subscription revenue, but it simultaneously removes third-party ad impressions, so net ARPU is the difference of two opposing flows. With a 14-day free trial as the offer, most subscription revenue lands *after* the trial window — likely beyond the planned 8–12 day durations — so the in-experiment readout will show ad-revenue loss immediately and subscription revenue late. I would expect a flat-to-slightly-negative ARPU during the run and a positive tail only if trial-to-paid holds up. What would surprise me: a large positive ARPU inside 12 days (would suggest measurement leakage or trial revenue being booked at access rather than charge), or a retention *gain* from a forced 5-second-uncloseable full-screen.

**3. Top risks & failure modes** (all ungrounded assumptions):
- **Trial-maturity mismatch:** a 14-day trial cannot convert to a charge within an 8–12 day experiment; ARPU measured at charge will structurally undercount the treatment arm.
- **Ad-revenue displacement exceeding subscription gain:** every daily splash replaces a monetized interstitial for *all* free users, including the large majority who will never subscribe; the cost side scales with reach, the benefit side only with converters.
- **Forced-exposure UX damage:** the 5-second-delayed close on a daily, unavoidable full-screen may depress session starts and next-day retention, which erodes both ad and subscription revenue outside the measurement window.
- **Cross-arm ARPU variance:** ARPU on free users is heavy-tailed (a few converters dominate); the inherited sample sizes from a video-replacement test may be underpowered for this metric — the stated iOS "Lift 23.15%" is an implausibly large MDE for an ARPU experiment.
- **Attribution leakage in the cannibalization segment:** excluding only subscriptions with this surface's source values misses users who saw the splash, dismissed it, and converted later through another entry point; the cannibalization check as designed can only understate cannibalization of other paywalls (and overstate incrementality).

**4. Analogs.** No KNOWLEDGE CONTEXT was provided, so per rule 1 I cite no past experiments and emit no analog cards.

no direct analogs

The card's own references to three predecessor projects are the team's descriptions, not evidence I can verify or ground; I treat them as unverified context only.

## Non-monetization effects to instrument

- **Retention (both directions):** negative — daily forced full-screen may reduce D1/D7 return rate; positive — trial takers may engage more with premium features and retain better. Instrument: D1/D7/D14 retention split by splash-seen vs. ad-seen, and separately for trial starters. Stop-rule: halt if D7 retention drops beyond a pre-set threshold (e.g., >1–2% relative) in the treatment arm.
- **Refunds/cancellations:** a low-friction daily prompt can harvest low-intent trials that cancel or refund post-charge. Instrument: trial cancellation rate during trial, refund rate in the 30 days post-charge. Stop-rule (post-experiment gate): do not roll out if refund/cancel rates materially exceed the organic-paywall baseline.
- **Engagement / upper funnel:** negative — tab opens per day and session length may fall if users learn the first open triggers a splash; positive — banner replacements of dead zero-states may *improve* perceived app quality vs. broken ad slots. Instrument: tab views per user, session starts per day, app-store rating/review volume during the run.
- **Ex-subscriber behavior:** the splash may either win back expired subscribers (positive) or irritate users who deliberately churned (negative). The planned ex-subscriber segments are good; add a splash-close-latency metric (immediate close at 5s vs. engaged views) as a proxy for annoyance.

**6. Design & measurement checklist**
- Recompute power on ARPU with actual free-user ARPU variance for *this* audience (all free users, not "users who failed to view an ad"); the audience definition in the power table doesn't match the exposure rule (all free users daily), which also risks SRM if eligibility differs by arm.
- Extend duration to cover trial maturity: minimum 14 days of trial + charge window, or pre-commit to a two-stage readout (access-based interim, charge-based final).
- Measure ad revenue displacement directly per user (impressions × eCPM by slot), not just net ARPU, so the two flows are separable.
- Gate analysis on the exposure event (splash or banner actually rendered) with an SRM check on that event, since ad-fail triggers may fire at different rates across arms.
- Add stop-rules for retention and session-start declines, not only revenue.

**7. Changes that would most improve expected value**
1. Lengthen the run (or add a holdout followed to charge) so 14-day-trial revenue is observable before the rollout decision.
2. Cap the forced-view: allow immediate close or reduce the 5-second lock, and instrument close latency to answer the open UX question inside this same test.
3. Split the treatment (or plan a fast follow-up) separating "zero-state/ad-fail replacement only" from "daily replacement for everyone" — the first is nearly pure upside, the second carries all the displacement and UX risk, and a single combined arm cannot tell you which component drove the result.
