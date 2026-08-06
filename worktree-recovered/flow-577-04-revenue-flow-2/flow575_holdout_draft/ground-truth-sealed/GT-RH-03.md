# GT-RH-03 — UG App: sale – animation for XMAS and NY sales

## Identity
- pageId: 746536863 — "[2025-12-09] UG App: sale - animation for XMAS and NY sales [2025-12-30]" (snapshot v16, 2025-12-30). The hypotheses base / FLOW-577 inventory (key T2-03) titles it "UG App – XMAS and New Year sales with animation".
- URL: https://alice.mu.se/pages/viewpage.action?pageId=746536863 (space CRO; webui /spaces/CRO/pages/746536863)
- AB experiment id: 6878 — run 2025-12-13 .. 2025-12-22 (10 days). Exposure event: Explore Open. Iteration of the Halloween seasonal-animation experiment (inventory T2-02, Oct 2025, Red FAIL on overall metrics).
- Jira: UMN-10299
- Dates: project page window 2025-12-09 .. 2025-12-30.
- Arms: control / variation 2 (B: new Explore-banner visual + thematic animation shown before the sale splash; plans, prices, splash and paywall display rules unchanged) / variation 3 (C: same as B, plus Pro+ annual offer at $24.99 for all users instead of $19.99 or introductory $19.99; SKUs WW iOS `com.ultimateguitar.ugt.plus.1year3`, WW Android `com.ultimateguitar.tabs.plus.inst.1year5`).
- Audience: Free users (without Pro/Pro+; free rights — no trial, no subscription; organic + referral), WW Apps, smartphones only (platform = 2), iOS + Android. Page also specs an NY (New Year) second wave with animation/mockups TBD; only the XMAS wave ran as #6878.
- Segments configured for #6878: Total {'pro_rights': 'free', 'platform': 'Mobile'}.

## Actual outcome
Sample sizes (Experiment rows, 10 days; control / variation 2 / variation 3):
- UGT_IOS: 139025 / 138088 / 139952
- UGT_ANDROID: 71693 / 70575 / 70769

UGT_IOS, Total segment (Monetization Metrics):
- ARPU: control $0.254; var2 $0.273 (+7.84%, p=0.06); var3 $0.259 (+2.31%, p=0.57)
- Charge cr: 1.18% → var2 1.25% (+5.69%, p=0.11); var3 1.17% (−1.57%, p=0.65)
- Access cr: 2.16% → var2 2.21% (+2.49%, p=0.33); var3 2.12% (−1.72%, p=0.50)
- AOV/ARPPU: var3 +4.05% (p=0.05) / +3.94% (p=0.06); var2 +2.05% (p=0.31) / +2.03% (p=0.31)
- Charge→14d refund: var2 −26.4% (p=0.05); Charge→14d cancel: var2 −9.48% (p=0.10); var3 both ns (p=0.82/0.83)
- Trial→charge: 17.4% → var2 18.2% (+4.5%, p=0.56); var3 17.1% (−1.82%, p=0.81)
- Stats: revenue $35246 / $37753 (+7.1%) / $36301 (+3%); buyers 1646/1728/1631; charges 1674/1757/1657; refunds 14d 88/68 (−23%)/90.
- Retention flat: var2 ret1d −0.285% p=0.67, ret7d +0.219% p=0.50, ret14d +0.229% p=0.44; var3 p=0.26/0.39/0.30. Tab View metrics all ns (var2 lowest p=0.06–0.09 on mild negatives).

UGT_ANDROID, Total segment:
- ARPU: control $0.194; var2 $0.2 (+3.57%, p=0.61); var3 $0.212 (+9.43%, p=0.19)
- Charge cr: 0.749% → var2 0.793% (+5.94%, p=0.34); var3 0.783% (+4.51%, p=0.46)
- Access cr: 1.65% → var2 1.7% (+3.56%, p=0.39); var3 1.69% (+2.51%, p=0.54)
- Trial→charge: 13.5% → var2 15.6% (+16.1%, p=0.21); var3 15.3% (+14%, p=0.28)
- Charge→14d cancel/refund: all ns (var2 p=0.65/0.53; var3 p=0.26/0.53)
- Stats: revenue $13877 / $14148 (+2%) / $14990 (+8%); buyers 537/560/554; charges 544/573/572.
- Retention flat: var2 p=0.77/0.30/0.86; var3 p=0.68/0.41/0.07 (ret14d −0.767%, ns). Tab View: var3 has small significant negatives — Tab View 180s −1.17% (p=0.019), Tab View 600s −2.8% (p=0.021); everything else ns.

Decision text confirms: "Across both platforms, no statistically significant differences were observed in overall monetization metrics."

Christmas funnel (Insights; free users → Christmas Splash funnel; NO p-values reported for these uplifts):
- iOS: Splash View 13,860 / 14,034 (+1.26%) / 14,133 (+1.97%); Splash View→Splash Click 2.97% → 4.01% (+35.28% var2) / 3.45% (+16.44% var3); Subscribed 245 → 334 (+36.33%) / 272 (+11.02%); Revenue $3,564 → $4,866 (+36.52%) / $4,897 (+37.40%); ARPU (of Splash View) $0.26 → $0.35 (+34.83%) / $0.35 (+34.75%); ARPPU $14.55 → $14.57 (+0.14%) / $18.00 (+23.76%). Animation View End reached ~94% of splash viewers (94.07% var2, 93.70% var3).
- Android: Splash View 6,320 / 6,376 / 6,258; Splash View→Splash Click 3.99% → 4.83% (+21.15% var2) / 3.87% (−3.02% var3); Subscribed 120 → 172 (+43.33%) / 125 (+4.17%); Revenue $2,136 → $3,000 (+40.47%) / $2,522 (+18.09%); ARPU $0.34 → $0.47 (+39.24%) / $0.40 (+19.26%); ARPPU $17.80 → $17.44 (−2.00%) / $20.18 (+13.37%).
- Banner vs Automatic splash split (iOS): Banner Splash — var2 best (Revenue +32.47%, Subscribed +32.02% vs var3 +31.97%/+6.58%); Automatic Splash — var3 strongest revenue/ARPU (+113.31% revenue, ARPU +112.56%; var2 +93.17%/+94.53%). Android: var2 improves the whole funnel (banner revenue +33.08%, automatic +138.94%); var3 cuts banner Splash View→Splash Click by −16.19% and weakens the top of funnel despite higher revenue.
- Cannibalization check ("Did we cannibalise non-sale sources?"): non-Christmas paywall funnel diffs are small and non-significant on both platforms (e.g. iOS other-charged −1.33% var2 / −3.27% var3; Android −5.60% var2 / +5.60% var3). Page conclusion: "the experiment does not have a measurable impact on core (non-Christmas) purchases and does not introduce any negative side effects outside of the Christmas splash scenarios."

Forecast (per day): iOS var2 +84 accesses / +117 charges / ARPU +7.48% / +$3,185 vs control; iOS var3 −67 accesses / −17 charges / +$838. Android var2 +44 accesses / +39 charges / +$532; var3 +35 / +30 / +$1,594.

## Uncertainty & maturity
- Overall (Total-segment) monetization: nothing significant at 0.05 on either platform. Closest: iOS var2 ARPU p=0.06 and refund-share p=0.05; iOS var3 AOV p=0.05 / ARPPU p=0.06; Android all money metrics p≥0.19.
- The Christmas-funnel uplifts (+30–40% revenue/ARPU) and the banner/automatic split are reported WITHOUT p-values or significance testing (raw funnel counts from ad-hoc SQL over `ug_rt_events_app` + `ug_subscriptions_events`).
- Design vs Reality: all checks complete on both platforms — "duration of exp ≥ design" (10 ≥ 9 UGT_IOS; 10 ≥ 3 UGT_ANDROID), "A/B balance is maintained" (SRM ok; per-arm counts above), "No visible bugs", "No external effects".
- Inconsistency on the page: the pitch Experiment-design table lists sample 216,622 / duration 3 days under IOS and 304,757 / 9 days under ANDROID, while the Design-vs-Reality block pairs them the other way (UGT_IOS Design 9 days / 304757; UGT_ANDROID 3 days / 216622) — the platform assignment is transposed between the two tables (power math — higher iOS baseline 0.73% needs the smaller sample — favors the pitch-table pairing). Either way, actual per-arm samples (~139k iOS, ~71k Android) are below both design sample figures; only the duration check is marked complete.
- Pending-trial maturity is not documented on the page; 14-day cancel/refund and retention 14d are computed (R14 present).
- The formal Hypothesis section was left as an unfilled template (no pre-registered expected effect beyond the Reach & Impact +10% model).

## Final decision
Decision status: Green SUCCESS. Exact wording:
- "Roll out Variant 2 for both platforms because it shows better results in revenue and subscriber numbers"
- "Across both platforms, no statistically significant differences were observed in overall monetization metrics. However, when analyzing the experimental funnel separately (Christmas splashes), the following conclusions can be drawn:"
- "iOS platform : The Christmas splash delivered a strong uplift. For Banner Splash, Variant 2 performed best, while for Automatic Splash, Variant 3 showed the strongest results."
- "Android platform : Variant 2 consistently improves the entire funnel and monetization. Variant 3 reduces Splash Click conversion and weakens the top of the funnel, despite higher revenue."
- Cannibalization: "no statistically significant differences were observed between the control group and the variant groups on either the iOS or Android platforms".
Inventory decision field: rolled-out (var2 — animation only — rolled out to both platforms).

## Confirmed product lessons
- Page Insight (verbatim): "Emotional design and thematic animation have a positive impact on sales funnel metrics. This effect persists even when the offer price is increased. As a result, we have seen a 30-40% growth in ARPU for the scenario."
- Seasonal thematic animation does NOT move overall monetization metrics significantly (same as the Halloween predecessor, which was ruled Red FAIL), but inside the seasonal-splash scenario the funnel shows +30–40% revenue/ARPU — this time judged Green SUCCESS with a rollout of the animation-only arm.
- No cannibalization: the Christmas splash does not measurably dent core (non-Christmas) purchases — the seasonal uplift is incremental, not substitution.
- Price increase to $24.99 (var3) raises ARPPU (+23.76% iOS / +13.37% Android in the scenario) and works best on iOS Automatic Splash, but on Android it depresses Splash Click conversion (−3.02% overall, −16.19% on banner) and weakens the top of the funnel — so the unpriced animation arm (var2) was chosen for rollout.
- Next steps (verbatim): "We'll continue to prepare special visuals and animations for big sales (like New Year, Black Friday, etc) and make it different compared to 'permanent' seasonal sales"; "We can separate big thematic sales and permanent offers not only visually, but also by using less cheap offers for permanent sales and making them more dynamic/personal (and manage this through CRM). First of all, don't sell it at the minimum price permanently."
- Caveat carried in the inventory: the var3 conclusion mixes two mechanisms in one arm (design + price), and the scenario-level +30–40% figures have no significance testing.

## Sources
- Page: https://alice.mu.se/pages/viewpage.action?pageId=746536863 ("[2025-12-09] UG App: sale - animation for XMAS and NY sales [2025-12-30]"), snapshot output/confluence/flow577_verify/746536863/confluence_746536863.txt (+ .storage.xhtml for tables; v16, 2025-12-30).
- Sections used: "Pitch → Context & Idea / Reach & Impact / Experiment design", "Description of the Solution & Mockups → XMAS / NY", "Analytics" (# 6878 config), "Results → Decision", "Design vs Reality check", "Forecast (per day)", "Significance analysis" (#6878, UGT_IOS / UGT_ANDROID Monetization / Retention / Tab View), "Insights" (Christmas funnel, Banner vs Automatic splash, cannibalization), "Next steps".
- Inventory: output/flow577_revenue_inventory/inventory.yaml, key T2-03 (verified against the page 2026-08-04; AB id 6878, run 2025-12-13..2025-12-22, Jira UMN-10299, iteration of T2-02 Halloween).
