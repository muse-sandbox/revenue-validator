# GT-RH-05 — UG Web: checkout size optimization

## Identity
- pageId: 787253507 — "[2026-04-20]: UG Web — сheckout size optimization [2026-05-26]" (snapshot v16, 2026-07-27)
- URL: https://alice.mu.se/spaces/CRO/pages/787253507
- AB experiment id: 7328. Data window 2026-05-04 .. 2026-05-11 (8 days). Exposure/start event: App Experiment Start (item_id = 7328), web platform = 1 (Desktop); results SQL excludes email funnel sources.
- Jira: UMN-11436
- Dates: project page dates 2026-04-20 .. 2026-05-26; experiment ran 8 days per Design vs Reality.
- Arms: control (current checkout); variation 2 — compact checkout (header block removed, smaller heading, reduced spacing between blocks, window height ~15% lower); variation 3 — same compact layout plus alternative payment buttons moved above the card-details form. Audience: everyone in the payment funnel, all Pro+ funnel checkouts, desktop web.
- Segment configured for #7328: Total {'pro_rights': 'all', 'platform': 'Desktop'}.

## Actual outcome
Sample sizes (Design vs Reality; design duration/samples recorded as 0 — not calculated): UG_WEB control 3480 / variation 2 3565 / variation 3 3478 (8 days). Monetization Stats table members: 3,480 / 3,566 / 3,479.

UG_WEB, Total segment (Monetization Metrics, primary results block):
- ARPU: control $10.14; var2 $10.80 (+6.47%, p=0.323); var3 $11.69 (+15.26%, p=0.024 — significant)
- Trial → charge: 27% → var2 31.57% (+15.05%, p=0.152); var3 35.24% (+28.42%, p=0.008 — significant, named the main revenue driver)
- Charge cr: 15.78% → var2 16.24% (+2.92%, p=0.598); var3 16.87% (+6.95%, p=0.216 — NOT significant)
- Access cr: 21.44% → var3 22.25% (+3.78%, p=0.413); AOV var3 +6.66% (p=0.066); ARPPU var3 +7.76% (p=0.052)
- Charge → 14d cancel: 13% → var3 16.84% (+31.73%, p=0.043 — significantly WORSE); var2 14.06% (+9.99%, p=0.507). (Narrative text says "from 10% to 16.8%"; the table's control value is 13%.)
- Charge → 14d refund: var3 −9.94% (p=0.645); var2 −10.81% (p=0.617)
- Variation 2 overall: no significant monetization differences (all p ≥ 0.152).
- Stats: revenue control $35,299 / var2 $38,511 (+9.10%) / var3 $40,673 (+15%); buyers 549/579/587; charges 610/647/659; charged trials 135/161/179; 14d cancels 78/91/111.

Retention (members 3355/3413/3357) — var3 significantly WORSE: ret1d 15.7% → 13.9% (−11.1%, p=0.045); ret7d 37.4% → 34.7% (−7.23%, p=0.021); ret14d 42.4% → 39.7% (−6.45%, p=0.023). Var2 retention flat (−6.56%/−3.42%/−2.32%, p=0.24/0.27/0.41). Tab View metrics: var3 per-user views −5.9..−9.7% but not significant (p=0.07–0.46); var2 flat.

Forecast (per day): control 1448 App Experiment Start / 402 accesses / 254 charges / $14,688; variation 2 +4 accesses / +9 charges / +$950; variation 3 +11 accesses / +20 charges / +$2,241.

Insights — payment-method mix (var3 vs control, accesses distribution): CreditCard 68.25% → 55.73%; PayPal 12.00% → 18.71%; Google Pay 10.86% → 14.49%; Apple Pay 8.89% → 11.07%. The cancellation-rate increase in group 3 appears across nearly all payment methods except Apple Pay (CreditCard charges→cancels 13.68% → 18.21%, +33.08%); "an increase in charge... particularly noticeable in the case of credit cards".

Revenue Estimation for next year (Results block; year plans ×0.55 next-year cr, month ×3 reconversion periods, excl. cancels): fact + estimation control $52,984; var2 $56,976 (+7.54%); var3 $59,148 (+11.63%); next-year-only estimation var3 +4.47%.

Post-Rollout Analysis (updated slice of the same cohort): ARPU var3 +12.91% (p=0.053 — significance weakened above 0.05); trial→charge +26.60% (p=0.0105); charge→14d cancel +31.22% (p=0.0399, still significant); 14d refund +8.22% (p=0.7); revenue var3 $39,790 (+12.87%); updated Revenue Estimation: fact + estimation var3 +10.07% (var2 +8.26%). Var2 remained non-significant (ARPU p=0.33).

## Uncertainty & maturity
- SRM / balance: "A/B balance is maintained" — complete; members 3480/3565/3478.
- Duration: "duration of exp ≥ design" — complete (8 days run vs design summary 7 days for seasonality; the raw power calc said 2 days, 1,996 per variation). Design-vs-Reality design sample cells recorded as 0.
- "No visible bugs" and "No external effects" — complete.
- Charge cr uplift for var3 is NOT significant (p=0.216) even though the decision narrative lists charge conversion among the uplifted metrics; the significant drivers are ARPU (p=0.024) and trial→charge (p=0.008).
- Narrative/table discrepancy: decision text states 14d cancel rose "from 10% to 16.8%"; the metrics table shows control at 13% (same +31.7% relative diff).
- Post-rollout recalculation weakened ARPU significance to p=0.053; the cancel penalty stayed significant (p=0.0399).
- Pending-trial maturity: not documented on this page beyond the 14d cancel/refund windows.

## Final decision
Decision status: Green — SUCCESS. Exact wording: "Rollout group 3 but monitor Charge → Cancel conversion".
Supporting decision text: "The compact checkout with alternative payment methods placed above the credit card form delivered the strongest monetization results across the experiment"; "ARPU increased by +15.3% in variation 3"; "The main driver of revenue growth was a +28.4% uplift in Trial → Charge conversion, resulting in an estimated +$2.2K revenue uplift per day versus control". Follow-up idea recorded: "encourage even more users to switch to payment buttons by hiding the credit card form behind the button".

## Confirmed product lessons
- Money moved with no offer change at all — a pure checkout-UX intervention (compact layout + alt-payment buttons above the card form) delivered +15.26% ARPU (p=0.024), ~5x the pre-launch +3% conversion plan.
- The mechanism indicator is the payment-mix shift, not compactness alone: variation 3 moved purchases from CreditCard (68.25% → 55.73% of accesses) to PayPal (12% → 18.71%), Google Pay, and Apple Pay; variation 2 (compact only) showed no significant lift anywhere (all p ≥ 0.15).
- The effect is not "clean": the new checkout converts payers more effectively (+28.42% trial→charge, p=0.008), but those subscribers cancel more after the first charge (14d cancel +31.73%, p=0.043) and retain worse on the platform (7d −7.23% p=0.021, 14d −6.45% p=0.023) — a monetization/quality trade-off, hence "monitor Charge → Cancel conversion".
- The cancellation increase spans nearly all payment methods except Apple Pay — it is not an artifact of a single method.
- Accounting for cancels, next-year revenue estimation keeps variation 3 positive but below the fact lift: +11.63% fact+estimation vs +15.22% fact (post-rollout recalc: +10.07% vs +12.87%).

## Sources
- Page: https://alice.mu.se/spaces/CRO/pages/787253507 ("[2026-04-20]: UG Web — сheckout size optimization [2026-05-26]"), snapshot output/confluence/flow577_verify/787253507/confluence_787253507.txt (v16, 2026-07-27; storage: confluence_787253507.storage.xhtml).
- Sections used: "Pitch" (Initial/Final Context, Hypothesis, Experiment design), "Description of the Solution & Mockups → Solution", "Analytics" (#7328 config), "Results → Decision", "Design vs Reality check", "Forecast (per day)", "Significance analysis" (UG_WEB Monetization/Retention/Tab View + Stats), "Insights" (Monetization Metrics by Payment Method, Revenue Estimation for next year), "Post-Rollout Analysis".
- Inventory cross-check: output/flow577_revenue_inventory/inventory.yaml, key T3-07 (verified against the page 2026-08-04).
