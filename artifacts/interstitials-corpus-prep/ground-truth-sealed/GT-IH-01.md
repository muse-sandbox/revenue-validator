# GT-IH-01 — UG App: paywall – pre-paywall with animation for interstitials

## Identity
- pageId: 773658792 — "[2026-03-09] UG App: paywall – pre-paywall with animation for interstitials [2026-07-01]" (snapshot v27, 2026-07-23)
- URL: https://alice.mu.se/spaces/CRO/pages/773658792
- AB experiment ids: 7160 (original run, AB registry 2026-03-16..2026-03-18) and 7187 (relaunch; registry 2026-03-20..2026-03-27). The page's Results block is titled "Iteration #1 - #7187 (relaunch)"; the analytics section references "#7187 config". Exposure/start event: App Experiment Start (item_id = exp id).
- Jira: UMN-10952
- Dates: project page dates 2026-03-09 .. 2026-07-01; experiment ran 8 days per Design-vs-Reality ("Experiment 8" days, iOS and Android).
- Arms: control (variation 1), variation 2 (scratch-coupon interstitial with 5-second timer + skip), variation 3 (same but no timer and no option to skip). Audience: new users who completed tour install during the experiment, free only (never had a subscription), iOS + Android. New interstitial shown once, on first tab entry.
- Segments configured for #7187: Total {'pro_rights': 'Free'}; Interstitials {'pro_rights': 'Free', 'custom_sub_having': "funnel_source like '%Interstitial%' and funnel_source not like '%Winback%'"}.

## Actual outcome
Sample sizes (Design vs Reality; design sample "not calculated" for both platforms):
- UGT_IOS: control 13899 / variation 2 13872 / variation 3 13795 (8 days)
- UGT_ANDROID: control 7854 / variation 2 7891 / variation 3 7746 (8 days)

UGT_IOS, Total segment (Monetization Metrics):
- ARPU: control $0.321; var2 $0.406 (+26.5%, p=0.011); var3 $0.33 (+2.9%, p=0.75)
- Access cr: 4.58% → var2 5.33% (+16.4%, p=0.004); var3 5.05% (+10.4%, p=0.06)
- Charge cr: 2.43% → var2 3.08% (+26.6%, p=0.001); var3 3.05% (+25.5%, p=0.002)
- AOV/ARPPU: var3 −18.1%/−18% (p=0.001/0.001); var2 flat (−0.145%/−0.0345%, p=0.98/1.00)
- Trial→charge: 16.7% → var2 19.8% (+18.6%, p=0.25); var3 12.8% (−23.3%, p=0.14)
- Charge→14d cancel: 36.5% → var2 28.1% (−22.8%, p=0.014); var3 25.2% (−30.8%, p=0.001)
- Stats: revenue control $4455, var2 $5627 (+26%), var3 $4550 (+2.1%); buyers 338/427/421; charges 340/430/424.

UGT_IOS, Interstitials segment:
- ARPU: control $0.0399; var2 $0.0689 (+72.7%, p=0.001); var3 $0.106 (+166%, p=0.00)
- Access cr: 0.59% → var2 1% (+69.8%, p=0.000); var3 1.57% (+165%, p=0.00)
- Stats: interstitial-attributed subscribers 82 → 139 (var2, +70%) → 216/217 (var3, +160%); revenue $554 → $956 (+72%) → $1462 (+160%).

UGT_IOS retention: flat for var2 (ret1d −2.31% p=0.38; ret7d +0.459% p=0.76; ret14d +0.0992% p=0.94); var3 positive-but-ns (ret1d +3.61% p=0.17; ret7d +2.22% p=0.15; ret14d +0.946% p=0.47).

UGT_ANDROID, Total segment:
- ARPU: control $0.145; var2 $0.148 (+2.28%, p=0.91); var3 $0.185 (+27.9%, p=0.20)
- Charge cr: 0.738% → var2 0.811% (+9.83%, p=0.60); var3 0.93% (+25.9%, p=0.19)
- Trial→charge: 5.06% → var3 9.02% (+78.1%, p=0.21) — the decision text notes Android var3 "has better monetization (because trials have near 5% conversion rate) metrics".
- Stats: revenue control $1139, var2 $1170 (+2.8%), var3 $1436 (+26%).

UGT_ANDROID, Interstitials segment: ARPU control $0.0281 → var2 $0.0387 (+37.6%, p=0.38) → var3 $0.0734 (+161%, p=0.003); access cr 0.178% → 0.266% (p=0.24) → 0.452% (+153%, p=0.002); interstitial subscribers 14 → 21 (+50%) → 35 (+150%); revenue $220 → $305 → $568.

UGT_ANDROID retention — var3 significantly WORSE: ret1d 15.5% → 14.1% (−9.15%, p=0.012); ret7d 33.9% → 32.1% (−5.26%, p=0.018); ret14d 39.9% → 38.1% (−4.47%, p=0.023). Var2 retention flat (p=0.83/0.45/0.44).

Funnel (Insights): conversion interstitial→access increased overall — Android +64% (var2) and +164% (var3); iOS +35% (var2) and +171% (var3) (elsewhere in the funnel table iOS var3 shows +164.41% and Android var3 +170.59% — both figures appear on the page). Variation 2 had a lower conversion to interaction with the coupon "due to ability to close the banner. as a result 75-77% lower conversion from interstitial to banner on average" (iOS interstitial→banner 11.71% var2 vs 91.24% var3; Android 11.07% vs 86.35%). Second splashes: "not really" changed — fewer clicks but about the same accesses; most accesses still on the first splash.

## Uncertainty & maturity
- Significance analysis with p-values per metric is documented (see values above). iOS var2 ARPU lift is significant (p=0.011); Android ARPU lifts are NOT significant (var2 p=0.91, var3 p=0.20); var3's Android retention drop IS significant (p=0.012/0.018/0.023).
- Design vs Reality: design sample/duration "not calculated" for both platforms; the check "duration of exp ≥ design" is marked incomplete on both platforms (experiment ran 8 days); "A/B balance is maintained" complete; "No visible bugs" and "No external effects" complete.
- Pending-trial maturity: not documented on this page.
- Data-quality note in the decision: the 75-77% lower interstitial→banner conversion in variation 2 "needs further investigation (or relaunch to test)".

## Final decision
Decision status: Red — fail. Exact wording:
- "variation #2 is best for roll out"
- "variation #3 on Android has better monetization (because trials have near 5% conversion rate) metrics but worsen retention"
- "but i do not recommend full roll out since for some reason variation #2 had 75-77% lower conversion from interstitial to banner which needs further investigation (or relaunch to test)"
- Next steps: "It was decided not to roll it out because the revenue was too low."
No rollout; no staged rollout details documented.

## Confirmed product lessons
- The scratch-coupon (gamified) interstitial did increase conversion from interstitial to access on both platforms (Insights Q: "did we increase conversion from interstitials? yes" — Android +64%/+164%, iOS +35%/+171% for var2/var3).
- Making the interstitial non-skippable (variation 3) massively increases funnel engagement (interstitial→banner ~86-91% vs ~11-12% when skippable) and interstitial-attributed revenue (+150-160%), but on Android it significantly worsens retention (ret1d/7d/14d all p<0.025) — a monetization/retention trade-off.
- Variation 2's skippability caused a 75-77% drop in interstitial→banner conversion vs variation 3; this remained an open question ("needs further investigation (or relaunch to test)").
- Repeat (second) splashes add little: conversion on 2+ splashes did not really change — most accesses come from the first splash.
- Despite significant iOS ARPU lift for var2 (+26.5%, p=0.011), absolute incremental revenue was judged too low to roll out ("revenue was too low").
- Forecast (per day), for reference: iOS var2 +44 accesses / +37 charges / +$474 vs control; iOS var3 +26/+35/+$52; Android var2 −12/+3/+$18; Android var3 −18/+10/+$226.

## Sources
- Page: https://alice.mu.se/spaces/CRO/pages/773658792 ("[2026-03-09] UG App: paywall – pre-paywall with animation for interstitials [2026-07-01]"), snapshot output/confluence/flow568-interstitials/773658792/confluence_773658792.txt (v27).
- Sections used: "Description of the Solution & Mockups → Solution", "Analytics" (#7187 config), "Results → Iteration #1 - #7187 (relaunch)" → "Decision", "Forecast (per day)", "Design vs Reality check", "Significance analysis" (UGT_IOS / UGT_ANDROID Monetization/Retention/Tab View Metrics + Stats), "Insights" (Interstitials funnel, Second splashes).
- AB ids/run dates: snapshot `_registry.json` rows 7160 and 7187 (both UMN-10952, activation App Experiment Start).
