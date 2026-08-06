# GT-RH-02 — UG App: paywall – offer instead of ad interstitials (iterations 3+)

## Identity
- pageId: 714432870 — "[2025-08-20] UG App: paywall – offer instead of ad interstitials [2026-03-13]" (snapshot output/confluence/flow577_verify/714432870/)
- URL: https://alice.mu.se/pages/viewpage.action?pageId=714432870
- AB experiment ids (registry dates per KS-06/inventory; the page itself carries only the #6626/#6896 labels):
  - **6491** — first launch of iteration 1, registry 2025-09-30..2025-10-03; NO results block on the page.
  - **6626** — iteration 1 relaunch, registry 2025-10-06..2025-10-16; carries the iteration-1 results ("Iteration #1 - #6626 (relaunch)").
  - **6716** — "1 iteration (relaunch with new close button)" — timer + report close button, registry 2025-11-07..2025-11-17; NO results block on the page.
  - **6896** — "Iteration#2 - #6896 - intro offers", registry 2025-12-22..2025-12-29; results on page.
- Jira: UMN-9389 (iteration-2 backend analytics "same as" UMN-10264 — intro offer event in subscriptions_events).
- Dates: project page dates 2025-08-20 .. 2026-03-13. Exposure/start event: App Experiment Start (item_id = %experiment id%), sent for both variations.
- Arms: 2 (control vs variation 2) in every iteration. Audience: free users (no subscription), UGT_IOS + UGT_ANDROID. Mechanic: own interstitial paywall once/day on first eligible tab open (same trigger as the monetization-video experiment) + on ad-fail; banners in zero-ad states and replacing ad banners; interstitial → pre-paywall → paywall; banner click → paywall directly; close button after 5s. Iteration 1 offer: 14-day trial ('AD 14Free …' values). Iteration 2 offer: "We will replace the 14-day trial with an introductory plan. It's will be Pro+ ($39.99 per year) with discount for first year 50%".
- Calc segment configs: #6626 old config — Total {'pro_rights': 'Free'}, Without interstitial accesses (funnel_source_exclude: AD Interstitial, AD 14Free Interstitial, AD Tab, AD Song, AD Search, AD 14Free Song, AD 14Free Tab, AD 14Free Search), Long trials {'custom_sub_having': "trial = 14"}, Interstitials Funnel (Splash View → Banner Upgrade View → Banner Purchase Click → Purchase Process Finish, value like 'AD%'). #6626 final config — Total {'pro_rights': 'empty'}, Without interstitial accesses, Total exes {'pro_rights': 'expired any'}, Without interstitial accesses exes, Interstitials Funnel. #6896 config — same as #6626 final config with 'AD Winback Interstitial' added to both exclusion lists.

## Actual outcome

### Iteration 1 — #6491 (first launch): no results documented
The page contains no results block for #6491; #6626 is its relaunch and carries the iteration-1 results.

### Iteration 1 — #6626 (relaunch, 14-day trial offer) — Red fail
Design vs Reality: design sample 54,778/arm iOS and 146,630/arm Android; experiment ran 11 days. iOS samples 120,258 / 120,563 — "duration of exp ≥ design" (12) marked **incomplete**; Android samples 32,148 / 31,934 — duration check (8) complete (note the Android sample is far below the 146,630/arm design). "A/B balance is maintained", "No visible bugs", "No external effects" — complete on both platforms.

UGT_IOS, Total (control / variation 2 / diff / p):
- ARPU $0.181 → $0.198, +9.71%, p=0.06 (not significant)
- Access cr 1.54% → 2%, +29.9%, p=0.00
- Charge cr 0.888% → 0.977%, +10%, p=0.023
- Trials share 51.4% → 60.8%, +18.2%, p=0.00
- Trial → charge 19.9% → 20.1%, +1.17%, p=0.89
- Charge → 14d cancel 25.2% → 27.2%, +8.19%, p=0.26; 14d refund 4.93% → 6.14%, +24.6%, p=0.21
- Retention 7d 58.5% → 58.1%, −0.838%, p=0.015; Retention 14d 70.4% → 69.9%, −0.623%, p=0.019 (both significant declines); Retention 1d −0.77%, p=0.31
- Tab View per user 12.5 → 14.1, +13.6%, p=0.00; Tab View 60s–600s shares −1.12%…−1.67%, p ≤ 0.020
- Stats: subscribers 1,853 → 2,413 (+30%); trials 1,031 → 1,556 (+51%); charged trials 205 → 313 (+53%); buyers 1,068 → 1,178 (+10%); revenue $21,755 → $23,927 (+10%); cancels 14d 271 → 324 (+20%).

UGT_IOS segments:
- Without interstitial accesses: ARPU −6.81% (p=0.16); access cr −6.88% (p=0.032); subscribers −6.6% — cannibalization of other sources.
- Long trials: ARPU $0.00411 → $0.0277, +574%, p=0.00; access cr +445%, p=0.00; charge cr +573%, p=0.00 (base: trials 126 → 688; charges 20 → 135; revenue $494 → $3,341).
- NO RIGHTS (never-subscribed free users): ARPU +3.69%, p=0.56 — minimal; revenue $13,270 → $13,812 (+4.1%).
- EX SUBSCRIBERS Total exes: ARPU $0.453 → $0.537, +18.8%, p=0.025; access cr +85.3%, p=0.00; charge cr +22%, p=0.003; trials share 29.7% → 61%, +105%, p=0.00; trials 193 → 724 (+280%); revenue $8,484 → $10,032 (+18%).
- Without interstitial accesses exes: ARPU −19%, p=0.012; access cr −11.4%, p=0.035 — cannibalization inside the ex segment.

UGT_ANDROID, Total:
- ARPU $0.117 → $0.138, +18.5%, p=0.19 (not significant)
- Access cr 0.939% → 1.21%, +29%, p=0.001
- Trial → charge 26.9% → 15.3%, **−43.3%, p=0.002**
- Charge cr +7.77%, p=0.50; trials share +0.546%, p=0.92
- Retention 1d +3.61%, p=0.008; Retention 7d +1.74%, p=0.005; Retention 14d +0.83%, p=0.09
- Tab view per user 15.6 → 16.3, +4.18%, p=0.001; 60s–300s per user +3.06%…+3.65% (p ≤ 0.047); Tab View 60s share −0.884%, p=0.012
- Stats: subscribers 302 → 387 (+28%); trials 208 → 275 (+32%); charged trials 56 → 42 (−25%); revenue $3,749 → $4,413 (+18%).

UGT_ANDROID segments: Long trials — access cr +86.3% (p=0.00), AOV/ARPPU +23.4% (p=0.029), trial→charge −53.5% (p=0.038); NO RIGHTS — access cr +30.5% (p=0.006), trial→charge −38% (p=0.045); Total exes — ARPU +23.3% (p=0.29, n.s.), trial→charge −49.6% (p=0.017); Without interstitial accesses exes — trial→charge −49.8% (p=0.019).

Interstitials funnel (variation 2): iOS members → Splash View 98.61% (118,889); Splash → Banner Upgrade View 12.09%; → Banner Purchase Click 13.89%; → Purchase Finish 42.79%; members → purchase 0.71%. Android: 93.78% / 15.15% / 12.71% / 23.74%; members → purchase 0.43%.

Conversion decay by occurrence with the interstitial banner (variation 2): iOS no-rights splash→access 1.58% (1st, 55,922 views) → 0.87% (2nd) → 0.52% (3rd) → 0.41% (4+); splash→charge 0.83% → 0.22%. iOS ex-subs 2.59%/2.10% (1st, 9,831) → 0.95%/0.78% (4+). Android no-rights 1.36%/0.43% (1st, 11,740) → 0.27%/0.15% (4+); Android ex-subs 4.02%/3.13% (1st, 448 views).

Forecast (per day): Android Total +253 accesses / +38 charges / **+$1,759** revenue, ad revenue −$5; iOS Total +763 / +153 / **+$2,937**, ad revenue −$388. NO RIGHTS: iOS +$685 and −$329 ad revenue; Android +$772. EX SUBSCRIBERS: iOS +$2,162; Android +$918.

### Iteration 1 close-button relaunch — #6716: no results documented
Documented only as a solution variant: "Completely analogous to iteration 1. The only difference is that we will add a new button to close the ad. Now it contains a timer and a report with the option to skip the ad." No results block on the page.

### Iteration 2 — #6896 (intro offers: Pro+ $39.99/yr, first year −50%, replacing the 14-day trial)
Design vs Reality: experiment ran 8 days. iOS samples 102,128 / 102,273 — "duration of exp ≥ design" (12) **incomplete**; Android samples 117,062 / 116,618 — duration check (8) complete (design sample was 146,630/arm). Balance, no-bugs, no-external-effects — complete on both.

UGT_IOS, Total (control / variation 2 / diff / p):
- ARPU $0.222 → $0.248, **+11.5%, p=0.016** (the Decision bullet rounds this as "+10.9%")
- AOV $20.1 → $18.2, −9.31%, p=0.00; ARPPU $20.6 → $18.5, −10.2%, p=0.00
- Access cr 1.89% → 2.21%, +16.8%, p=0.00; Charge cr 1.08% → 1.34%, +24.1%, p=0.00
- Trials share 59% → 53.4%, −9.48%, p=0.000; Trial → charge −4.41%, p=0.56
- Charge → 14d cancel 25.7% → 26%, +1.09%, p=0.87; 14d refund −8.2%, p=0.67
- Retention flat: 1d −0.53% p=0.49; 7d −0.153% p=0.69; 14d −0.496% p=0.11
- Tab views per user 12.4 → 13.8, +11.5%, p=0.00; Tab View 60s/120s/180s shares −0.641%/−0.866%/−0.802%, p=0.000/0.001/0.009
- Stats: subscribers 1,934 → 2,262 (+17%); instants 831 → 1,096 (+32%); buyers 1,102 → 1,370 (+24%); revenue $22,678 → $25,325 (+12%); cancels 14d 290 → 361 (+24%).

UGT_IOS segments:
- Without interstitial accesses: ARPU $0.222 → $0.204, −8.18%, p=0.08; revenue $22,664 → $20,840 (−8.1%) — the conclusion quantifies this as "on iOS we lose about 30% of received gain in revenue".
- Total exes: ARPPU +8.32%, p=0.026; trial→charge 17.8% → 24.8%, +39.4%, p=0.027 (Decision bullet: "+38.6%"); ARPU +7.75%, p=0.31.
- Without interstitial accesses exes: ARPPU +8.79%, p=0.027; ARPU +10.2%, p=0.21.
- Ad revenue: $2,453 → $1,732 (−$721, −29%).

UGT_ANDROID, Total:
- ARPU $0.113 → $0.141, **+25%, p=0.000** (Decision bullet: "+24.6%"; conclusion: "+25.0%")
- AOV $24.8 → $21.6, −12.9%, p=0.00; ARPPU $25.6 → $22, −14%, p=0.00
- Access cr 0.999% → 1.12%, +12.1%, p=0.004; Charge cr 0.439% → 0.638%, **+45.3%, p=0.00**
- Trials share 68.9% → 53.7%, −22%, p=0.00; Trial → charge +9.02%, p=0.44
- Charge → 14d cancel 19.2% → 14.1%, **−26.6%, p=0.016**; Charge → 14d refund 2.82% → 1.45%, −48.7%, p=0.10
- Retention flat: 1d −0.69% p=0.37; 7d −0.0111% p=0.98; 14d −0.00479% p=0.99
- Tab View 60s share −0.535%, p=0.026; other tab metrics neutral (per-user +1.15%, p=0.07)
- Stats: subscribers 1,169 → 1,306 (+12%); instants 389 → 630 (+62%); buyers 514 → 744 (+45%); revenue $13,172 → $16,397 (+24%); refunds 14d 15 → 11 (−27%); cancels 14d 102 → 107 (+4.9%).

UGT_ANDROID segments: Without interstitial accesses — ARPU +3.39%, p=0.65 (neutral; near-zero cannibalization). Total exes — ARPU −2.2%, p=0.77. Without interstitial accesses exes — trials share 6.98% → 18.1%, +160%, p=0.00; trial→charge −54.3%, p=0.16 (Decision bullets add: "subscriber -> buyer, % & subscription -> charge, %: -10.5% and -11.4%, conversion drop in this subset"). Ad revenue: $293 → $270 (−$23, −8%).

Interstitials funnel (variation 2): iOS members → Splash View 97.31% (99,517); Splash → Banner Upgrade 31.20%; → Purchase Click 3.80%; → Finish 28.41%; members → purchase 0.33%. Android: 96.91% / 28.14% / 5.64% / 13.61%; members → purchase 0.21%.

Forecast (per day): Android control $3,499 → variation 2 $4,372 (**+$873**; 66 intro subscriptions/day; ad revenue −$6); iOS control $7,000 → variation 2 $7,806 (**+$806**; 101 intro subscriptions/day; ad revenue −$223).

## Uncertainty & maturity
- Per-metric p-values are documented for both result-bearing iterations (see above). Iteration 1: iOS ARPU lift NOT significant (p=0.06), Android ARPU NOT significant (p=0.19), while the trial→charge collapse (Android p=0.002; segment values p=0.017–0.045) and iOS retention 7d/14d declines (p=0.015/0.019) ARE significant. Iteration 2: ARPU significant on both platforms (iOS p=0.016; Android p=0.000); Android 14d-cancel drop significant (p=0.016); refund drop not (p=0.10); iOS without-interstitial ARPU drop borderline (p=0.08).
- Duration/sample: #6626 ran 11 days (iOS design 12 — incomplete) with Android samples (32k/arm) far below the 146,630/arm design; #6896 ran 8 days (iOS design 12 — incomplete; Android complete). Note the design table's "Sample size (per variation) 109,556 / 293,260" corresponds to 54,778 / 146,630 per arm in the Design-vs-Reality blocks.
- Iteration-1 next steps open with "Waiting for the unified_id fix" — a known identity-data issue at the time.
- Pending-trial maturity is not documented on the page; iteration 2 replaced trials with instant intro charges, and the explicitly open maturity question is "next year recurrent rate for intro plans" (post-rollout watch item).
- Page-internal inconsistencies (both values on the page): iOS iter-2 ARPU +10.9% (Decision bullet) vs +11.5% (metrics table & conclusion); iOS exes trial→charge +38.6% (bullet) vs +39.4% (table); Android ARPU +24.6% (bullet) vs +25.0% (conclusion/table). Tables are the primary source.
- #6491 and #6716 have no outcome data anywhere on the page — their outcomes are undocumented, not merely unfinished.

## Final decision
- **Iteration 1 (#6626): Red — fail.** Exact wording: "Do not roll out as-is." "As a result, our trial sign-up rate increased (30-86% in different segments), but our conversion rate to paid subscriptions decreased (36-54%). The quality of trials is declining significantly." "Free users are in the black by $685. And we are losing another $320 on advertising, so in fact we are in the black by $365 per day, giving everyone free access for two weeks." "The 5s close delay likely adds friction, reducing perceived UX quality and diluting trial quality." "Notably, Long-trials cohorts show strong ARPU/charge CR lifts on iOS (and better access CR and AOV/ARPPU on Android), suggesting potential when user intent is high, but current broad targeting degrades overall monetization quality." "on iOS most of revenue increase came from ex subscribers, while free users have minimal impact." Next steps: waiting for the unified_id fix; "Re-tune interstitial: shorten/instant close, reduce default emphasis on free trial (promote direct purchase or clearer terms), and/or cap frequency (e.g., ad-fail only or high-intent users)", "especially on Android with current ~10% trial → charge conversion"; "Re-test with KPIs: ARPU, trial→charge, 7d retention."
- **Iteration 2 (#6896): roll out.** Exact wording: "Overall recommendation: can roll out on both platforms with post roll out control of churn and next year recurrent rate for intro plans". What is rolled out: the daily/ad-fail interstitial paywall + subscription banners with the Pro+ $39.99/year intro plan at −50% for the first year (replacing the 14-day trial), on both iOS and Android. The iteration-2 "Next steps" field is left empty on the page; the "Post-rollout analysis (optional)" section is an unfilled template.

## Confirmed product lessons
- Offer type is the decisive lever on an identical placement/trigger: the 14-day free trial inflated trial sign-ups (+30–86% by segment) while collapsing trial→paid conversion (−36–54%) — "The quality of trials is declining significantly" — netting only ~$365/day for free users after ad-revenue loss; the 50%-off first-year intro plan flipped the pattern: trials share down (−9.5% iOS / −22% Android), instants +32% iOS / +62% Android, ARPU +11.5% iOS / +25% Android, Android 14d cancels −26.6% (p=0.016).
- Intro pricing trades AOV/ARPPU (−9.31% to −14%) for volume and conversion quality ("AOV/ARPPU fell on both platforms, because of the first year intro prices"); the residual risk is next-year recurrence for the discounted cohort — the explicit post-rollout control.
- Cannibalization is platform-asymmetric: on iOS ~30% of the gross revenue gain is lost via other sources and ad revenue (without-interstitial ARPU −8.18%; in-cohort ad revenue −29%/−$721; forecast −$223/day), while Android is nearly clean (without-interstitial ARPU +3.39% n.s.; ad revenue −$6/day forecast).
- Interstitial conversion decays steeply with repeat daily exposures (iOS no-rights splash→access 1.58% on the 1st occurrence → 0.41% by the 4th) — the first daily impression carries most of the value.
- Segment-offer fit: the trial offer activated ex-subscribers strongly (iter-1 iOS exes ARPU +18.8% p=0.025, access cr +85.3%, "on iOS most of revenue increase came from ex subscribers"), but the intro-price iteration "Works only on free users. doesn't affect ex subscribers".
- The 5-second close delay is repeatedly implicated in engagement-share declines (60–600s tab-view shares down in both iterations) and iter-1 trial-quality dilution; a timer+report close button was designed as the fix (#6716, outcome undocumented). Iter-2 engagement cost stayed small: long-view shares −0.5…−0.9% while iOS tab views per user grew +11.5%.
- High-intent subgroups (Long trials) showed outsized lifts off tiny bases (iter-1 iOS ARPU +574%, p=0.00), pointing at intent-targeting rather than broad exposure.

## Sources
- Page: https://alice.mu.se/pages/viewpage.action?pageId=714432870 ("[2025-08-20] UG App: paywall – offer instead of ad interstitials [2026-03-13]"); snapshot output/confluence/flow577_verify/714432870/confluence_714432870.txt (+ .storage.xhtml for table structure).
- Sections used: "Research and Context", "Hypothesis", design table ("#6626 Audience users who failed to view ad interstitial"), "Description of the Solution & Mockups" (1 iteration / 1 iteration relaunch with new close button / 2 iteration), "Analytics", segment configs (#6626 old / #6626 / #6896), "Results" → "Iteration#2 - #6896 - intro offers" and "Iteration #1 - #6626 (relaunch)" (Design vs Reality, Decision, Forecast (per day), Significance analysis incl. Monetization/Retention/Tab View Metrics & Stats, Interstitials Funnel, Conversion by occurrences, Ad revenue).
- AB ids and registry run dates: KS-06 card (KS-06_offer-instead-of-ad-interstitials-iter3plus.md) / flow577 inventory entry T1-06 (output/flow577_revenue_inventory/inventory.yaml); Jira UMN-9389, iteration-2 analytics UMN-10264 (Jira macros on the page).
- Predecessor pages cited by the page: "[2024-04-24] UG iOS: Interstitial - Swap into Landing [2024-08-10]", "[2025-04-11] UG App: paywall – offer instead of ad interstitials [2025-07-10]" (iterations 1–2 line), "[2025-07-09] UG App: paywall – monetization video instead of ad interstitials".
