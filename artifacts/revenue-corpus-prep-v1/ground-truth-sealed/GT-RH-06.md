# GT-RH-06 — UG Web: permanent banner — two plans: trial & monthly

## Identity
- pageId: 805316848 — "[2026-06-11]: UG Web: permanent banner —  two plans: trial & monthly [2026-07-06]" (snapshot v21)
- URL: https://alice.mu.se/pages/viewpage.action?pageId=805316848
- AB experiment id: 7598 (Results block titled "#7598"); run 2026-06-19 .. 2026-06-25 (6 days, per design). Exposure event: App Experiment Start; exposure condition: "Those users who saw the permanent banner".
- Jira: UMN-11941
- Dates: project page dates 2026-06-11 .. 2026-07-06; experiment ran 6 days on UG_WEB only.
- Arms (2): control — current permanent-banner paywall with 3 plans (annual with trial, discounted instant annual $19.99 no trial, monthly no trial); variation 2 — 2 plans only (annual trial selected by default + monthly), the $19.99 Express Plan replaced by a $24.99 seasonal/welcome offer repositioned to exit-intent ("ambulance"), banner creative changed to a discount on the trial offer, timer remains on the banner (disappears when expired), only the "white landing page" kept, cancellation funnel refined.
- Design/config: goal metric Plans View → Access, baseline 20.50%, MDE 20%, power 0.8, alpha 0.05, sample 1,602 plans-views per variation, 6 days (+1 week seasonality; Design summary "Days 7"). Internal corpus key: T3-04 (flow-577 revenue inventory).

## Actual outcome
Sample sizes (Design vs Reality / Stats, UG_WEB): control 547,440 vs variation 2 546,777; duration 6 days = design.

Total segment, Monetization Metrics (control → variation 2):
- ARPU: $0.041 → $0.036 (−10.36%, p=0.11) — not significant
- AOV: $34.19 → $32.95 (−3.64%, p=0.35)
- ARPPU: $39.14 → $37.49 (−4.22%, p=0.25) — not significant
- members → subscribers: −2.16% (p=0.68); members → buyers: 0.10% → 0.097% (−6.41%, p=0.27) — not significant
- trials share: 44.28% → 47.85% (+8.04%, p=0.13) — more trials, as planned, but not significant
- trial → charge: 37.59% → 34.12% (−9.23%, p=0.30) — not significant (trial → any charge identical)
- churn 14d: −12.63% (p=0.37); refund 14d: +29.15% (p=0.46) — both preliminary (see maturity)
- Stats: revenue control $22,191 vs $19,868; buyers 567 vs 530; trials 399 vs 422; charges 649 vs 603.

Retention Metrics — significantly BETTER in the test arm:
- web retention 1d: 9.12% → 9.20% (+0.79%, p=0.19, ns)
- web retention 7d: 24.47% → 24.81% (+1.39%, p=0.000) — significant
- web retention 14d: 29.61% → 30.03% (+1.43%, p=0.000) — significant

Permanent banner funnel (Insights, funnel_source = PermanentBanner, experiment window, web commission ×1.0):
- Top of funnel better for the test: banner view → click 0.72% → 0.86% (+19% relative); click → paywall view 13.07% → 14.68% (+12% relative)
- paywall → checkout: 25.34% → 24.46%
- paywall → subscribed: 17.35% → 10.42% (−40% relative; 89/513 vs 72/691) — no p-value documented for this funnel step
- Channel net revenue: $2,152.25 → $1,478.68 (−31%). PermanentBanner is only ~10% / ~7% of total revenue for A/B respectively, but the direction matches the Total-segment metrics — the page calls it "a consistent signal, not an isolated fluke" (author's assessment, not a statistical test).

Forecast (per day), UG_WEB: control 369,296 starts / 608 subscriptions / 438 charges / $14,970 revenue; variation 2 596 / 407 / $13,419; diff −12 subscriptions / −31 charges / **−$1,551 per day** (vs the pre-launch plan of +$500/day).

## Uncertainty & maturity
- No Total-segment money metric is statistically significant (ARPU p=0.11, ARPPU p=0.25, members→buyers p=0.27, trial→charge p=0.30); the decision was made on the consistent negative direction across metrics plus the −40% funnel drop (which carries no p-value). Only the retention 7d/14d improvement is significant (p=0.000), and it favors the test arm.
- SRM/design checks: "A/B balance is maintained" — complete; "duration of exp ≥ design" — complete; "No visible bugs" and "No external effects" — complete. Decision text: "Groups are balanced, and the design (6 days, sample size) was met as planned" (547,440 vs 546,777).
- Maturity: "Churn 14d / refund 14d are preliminary — ~65% of charges are younger than the 14-day observation window (experiment ended 2026-06-25, window closes ~2026-07-09)". The funnel's charged/refund figures fall under the same 14-day caveat.
- ARPU p-value cumulative trace dipped to 0.057 on 2026-06-23 and finished at 0.11 — directionally negative throughout but never crossing 0.05.

## Final decision
Decision status: Red — fail. Exact wording:
- "Do not roll out"
- "The \"fewer plans → less doubt → higher conversion\" hypothesis is not supported by this test"
- Takeaway: "more traffic reaches the paywall, but choosing between 2 plans converts worse than choosing between 3. The removed instant offer likely worked as an anchor/alternative for part of the audience, and without it some users simply do not subscribe rather than moving to trial."
- Next steps: "Keep the permanent banner concept — it drives meaningfully more clicks and paywall views (CTR +19% relative) — but revert the paywall back to 3 plans instead of 2"

Result class per inventory: inconclusive/directionally-negative kill — no significant money metric, decision made on consistent direction; killed, no rollout.

## Confirmed product lessons
- Collapsing the web permanent-banner paywall from 3 plans to 2 (trial + monthly) directionally hurt every money metric (ARPU −10.4%, ARPPU −4.2%, trial→charge −9.2%, buyers −6.4%; none significant) while lifting trials +8% — the trial-mix shift the plan counted on did not pay back in charges.
- The new banner creative genuinely improved top of funnel: banner CTR +19% relative and click→paywall +12% relative — the concept worth keeping per next steps.
- Paywall→subscribed collapsed −40% relative (17.35% → 10.42%): the removed discounted instant plan likely acted as an anchor/alternative — without it, part of the audience does not subscribe at all rather than switching to the trial (author's interpretation, plausible but not isolated by the test).
- Retention 7d/14d was significantly better (+1.39%/+1.43%, p=0.000) in the 2-plan arm — the only significant effect, and it points opposite to the revenue signal.
- Plan vs fact: planned +$500/day net revenue; Forecast landed at −$1,551/day. Mirror lesson to the sibling menu-expansion test (T3-03): changing paywall menu composition is dangerous in both directions; a discounted plan in the menu is not only a sales channel but an anchor for the other plans.
- Transfer bounds: web permanent-banner surface; does not transfer to other paywalls without accounting for the anchor role of the removed plan.

## Sources
- Page: https://alice.mu.se/pages/viewpage.action?pageId=805316848 ("[2026-06-11]: UG Web: permanent banner —  two plans: trial & monthly [2026-07-06]"), snapshot output/confluence/flow577_verify/805316848/confluence_805316848.txt (v21) + .storage.xhtml.
- Sections used: "Pitch → Initial Context & Idea", "Reach & Impact" (channel model, May 21 – Jun 6 2026), "Hypothesis", "Experiment design", "Description of the Solution & Mockups → Solution", "Analytics" (exposure), "Results → #7598" → "Decision", "Next steps", "Forecast (per day)", "Design vs Reality check", "Significance analysis" (UG_WEB Monetization/Retention Metrics + Stats), "Insights → Permanent banner funnel".
- Inventory record: output/flow577_revenue_inventory/inventory.yaml, key T3-04 (verified against the page 2026-08-04).
