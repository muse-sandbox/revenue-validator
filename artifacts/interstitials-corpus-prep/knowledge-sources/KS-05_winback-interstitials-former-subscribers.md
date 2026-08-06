# UG App: winback – interstitials for former subscribers

## Identity
- Experiment ID(s): AB 6461 (iteration 1, registry 2025-09-09..2025-09-16), AB 6644 (relaunch — registry "[UG Monetization] UG App: winback interstitials for former subscribers (relaunch)", 2025-10-13..2025-10-17; no separate results block on the page)
- Aliases: registry name "[UG Monetization] UG App: winback interstitials for former subscribers"; Confluence page title "[2025-08-01] UG App: winback – add interstitials for former subscribers [2025-10-17]"; Jira UMN-9259
- Source: https://alice.mu.se/pages/viewpage.action?pageId=714409638
- Dates: 2025-08-01..2025-10-17
- Related experiments: builds on KS-03 (paywall after ad interstitial — "our own advertising instead of interstitials, which have already proven themselves well"), KS-04 (monetization video — "there is potential here as well"), and KS-02 (offer instead of ad interstitials — whose segmentation error accidentally revealed high ex-subscriber conversion). A later follow-up experiment exists (held out).

## Context & Research (pre-launch)
- Goal: "Increase the conversion of former subscribers back to paid plans in the Ultimate Guitar mobile app by offering them a personalized promotional offer, including the possibility of a renewed trial, through targeted interstitials."
- Foundation: "Former subscribers have previously demonstrated a willingness to pay and showed high conversion rates when offered a renewed trial by mistake in an earlier experiment. In this project, we will intentionally target this segment with a clear, attractive offer to encourage their return to a paid subscription."
- Explicit link to KS-02: "Due to a segmentation error, former subscribers were included in the experiment and offered an additional trial. Although these users had already used their trial and were charged immediately, they demonstrated a high conversion rate. With this new project, we are deliberately targeting former subscribers and designing a special promotional offer that allows them to start a new trial and potentially return."

### Prior winback experiments reviewed on the page
1. [2024-11-28] "winback – non-removable subscription expiration trial banner" ("scary" banner on Explore + splash after auto-renewal off):
   - Only ~30–32% of Explore openers actually saw the banner (data to be re-verified).
   - view→click: iOS B 6.1%, iOS C 7.2%; Android B 25.8%, Android C 13.2%.
   - click→purchase: 9–14% (iOS), 37–40% (Android). Total view→charge: ~0.2–1.1% iOS, 0–2.6% Android.
   - iOS ARPU by arm: $0.45 / $0.62 / $0.69; Android $0.40 / $0.56 / $0.30.
   - Conclusion: hypothesis not confirmed — extremely low banner-view→click conversion; small reach and weak CTR despite a small ARPU increase.
2. [2024-02-08] "churn – winback right after cancel" (push + personalized splash, iOS): variation B "Extra trial" (30-day) best on conversions and revenue (ARPU $1.04 vs control $0.81; splash→click 5.4%, click→access 58.46%); but only ~50% of sent pushes were delivered, splash reach <80% of the target group, and up to 20% never saw the splash; goal not met due to poor push delivery and incorrect display accounting.
3. [2025-02-17] repeat "churn – winback right after cancel" (6-month trial, iOS+Android): pushes 1,358 sent / 988 delivered (72%); opened app after cancel 831 (29.5% vs 30.2% control); splash seen 703 (25%); splash→click 3.84% (27 clicks); splash→purchase 1.28% (9 purchases); ARPU $0.31→$0.37 (+22%, p=0.54); ARPPU $25.38→$27.06 (+6.6%, p=0.36); revenue $837.7→$1,055.3 (+26%); re-subscription 1.21%→1.38% (+14%, n.s.). Conclusion: "A six-month trial was not a strong enough incentive" — price alone doesn't tempt; intangible/personalized bonuses suggested.

### Ad-pressure and audience research
- Ad frequency: 7–9 impressions/day ≈ 7–9% of a user's total daily ad noise — noticeable but not dominating; creates discomfort that motivates subscribing (especially with a splash explaining how to remove ads); above the current 5-impression cap but below the scare-away 10–12 zone. Conversion-focused campaigns can run higher frequency than image campaigns (2–3/day), with testing advised to avoid burnout.
- Returning ex-subscribers: on average 140 users return to the app and open ≥1 tab on the day their subscription ends, seeing ~70 ads/day as a group; the number declines only ~10% over two weeks (day-14: 126 returning, 50 seeing ads).
- Ad exposure distribution: 77.7% of these users see 0–1 ads/day (51.4% see none, 26.3% see one); only 24 of 1,215 (~2%) hit the 5/day cap.
- Tab-opening distribution: ~20% open only one tab/day; the 5-impression limit and 180s interval only affect the <10% who open 6+ tabs/day.
- Assessments recorded: raising the cap 5→8 affects only 1–2% of the audience ("for 98% of users, the increase in the limit will have no effect"); shortening the 180s interval helps only the "hardcore" ~5–7% (<100 people); a splash on EVERY tab open would reach ~1,500 users and at an optimistic 1% CR yield ~$600/day ($480/day from the 2nd tab) — "very optimistic… we may scare away loyal users. The potential conversion rate looks low."

### A/B test model

| Metric | iOS A | iOS B | diff | Android A | Android B | diff |
|---|---|---|---|---|---|---|
| ex subscribers Tab View | 26,803 | 26,803 | — | 10,005 | 10,005 | — |
| Interstitial accesses | 0 | 54 | 54 | 0 | 28 | 28 |
| Total accesses | 899 | 953 | 54 | 202 | 230 | 28 |
| Tab → access, % | 3.35% | 3.55% | 6.0% | 2.02% | 2.30% | 13.9% |
| Charges | 467 | 495 | — | 148 | 169 | 21 |
| Revenue, $ | $18,667 | $19,788 | $1,121 | $4,355 | $4,959 | $604 |
| ARPPU, $ | $40 | $40 | $0 | $29 | $29 | $0 |
| ARPU, $ | $0.696 | $0.738 | $0.042 | $0.44 | $0.50 | $0.06 |

## Hypothesis
"If we present a unique promotional offer, including a renewed trial, specifically to former subscribers via interstitials, we expect to increase ARPU and repurchase rate among this audience—without negatively impacting 7-day retention or engagement (users with 3+ tabs/scores weekly)."

## Mechanics
- Placement/Trigger: the splash with the unique offer appears INSTEAD of an ad the first time the user opens a tab each day. On subsequent tab openings within the same day, regular ads are shown as usual. The next day, the offer is again shown once on the first tab opening. Additionally, if a regular ad fails to load or an error occurs, the promotional splash is shown instead.
- Flow: if the interstitial is displayed automatically on tab entry, a pre-splash is displayed first; if the user clicks on a banner, only the splash is displayed.
- Frequency cap on the offer: the user cannot take advantage of the offer more than once — after purchasing this subscription, the interstitial no longer appears.
- Audience segment: only users with previously active but currently inactive subscriptions (former subscribers).
- Platforms: shipped on iOS ("The experiment will be available on iOS platform"); UGT_ANDROID was sized in the design.
- SKUs / offers shown: subscription com.ultimateguitar.tabs.plus.inst.1year2 with a 14DAYSFREE promotion offer — 2 weeks of additional trial, even if the user previously had a trial.

## Experiment design
- Arms: control (normal ads) vs variation 2 (winback splash per above).
- Goal metric: ex subscriber → access, %.

| Parameter | UGT_IOS | UGT_ANDROID |
|---|---|---|
| Baseline | 3.35% | 2.02% |
| Lift, % | 6.0% | 13.9% |
| MDE | 0.011 | 0.019 |
| Power | 0.8 | 0.8 |
| Alpha | 0.05 | 0.05 |
| Sample (per variation) | 268,030 | 90,045 |
| Duration (days) | 10 | 9 |

- Analytics: App Experiment Start (item_id = %experiment id%; sent for both variations when an ex-subscriber enters a tab for the first time that day); Splash View / Splash Close and the banner purchase funnel (Banner Upgrade View, Banner Purchase Click, Purchase Process Start/Finish/Canceled) with values 'AD Winback Interstitial' / 'AD Winback Tab' / 'AD Winback Song' / 'AD Winback Search'.
- Calc config (#6461): Total {'pro_rights': 'all'}; Without interstitial accesses {'pro_rights': 'all', 'funnel_source_exclude': ['AD Winback Interstitial']}; Interstitial accesses only (funnel_source_include — for conversion research purposes); Interstitials Funnel: members > Splash View > [Splash Close; Banner Purchase Click > Purchase Process Finish], all with value 'AD Winback Interstitial'.

## Execution notes
- Iteration 1 (#6461) ran 8 days vs the 10-day design — "duration ≥ design" check incomplete; A/B balance maintained; no visible bugs; no external effects. Actual sample 21,932 / 22,121 (the check table's design column lists 134,015 per arm).
- A unified_id bug is flagged in next steps ("preferably wait to fix unified_id bug") — a known data-identity issue at the time.
- AB 6644 is the registry relaunch (2025-10-13..2025-10-17); the page contains no separate results block for it.

## Results
Iteration #1 (#6461), UGT_IOS, exposure App Experiment Start. Verdict: Green SUCCESS.

Monetization stats:

| Segment / arm | Members | Subscribers | Accesses | Instants | Trials | Ex trials | Charged trials | Buyers | Charges | Revenue | Cancels 14d | Refunds 14d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total control | 21,932 | 494 | 515 | 273 | 90 | 152 | 16 | 369 | 373 | $8,241 | 26 | 14 |
| Total var 2 | 22,121 | 1,350 | 1,379 | 278 | 949 | 152 | 159 | 513 | 521 | $11,873 | 79 | 27 |
| diff, % | +0.86% | +170% | +170% | +1.8% | +950% | 0% | +890% | +39% | +40% | +44% | +200% | +93% |
| Without interstitial var 2 | 22,121 | 472 | 500 | 259 | 89 | 152 | 18 | 353 | 361 | $7,754 | 25 | 16 |
| (vs control) diff, % | — | -2.5% | -0.79% | -5.1% | +13% | 0% | +12% | -4.3% | -3.2% | -5.9% | -3.8% | +14% |
| Interstitial-only var 2 | 22,121 | 878 | 879 | 19 | 860 | 0 | 141 | 160 | 160 | $4,118 | 54 | 11 |

Monetization metrics (Total):

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.376 | $0.537 | +42.8% | 0.00 |
| AOV | $22.1 | $22.8 | +3.14% | 0.36 |
| ARPPU | $22.3 | $23.1 | +3.63% | 0.29 |
| Access CR | 2.25% | 6.1% | +171% | 0.00 |
| Charge CR | 1.68% | 2.32% | +37.8% | 0.00 |
| Trials share | 17.5% | 68.8% | +294% | 0.00 |
| Trial → charge | 17.8% | 16.8% | -5.76% | 0.81 |
| Charge → 14d cancel | 6.97% | 15.2% | +118% | 0.00 |
| Charge → 14d refund | 3.75% | 5.18% | +38.1% | 0.30 |

- Results bullet also cites charge → 1m cancel +69.0% — "higher post-charge cancellations".
- Without interstitial accesses: ARPU -6.71% (p=0.40); access CR -3.31% (p=0.60); charge CR -5.15% (p=0.47) — "those without interstitial access do not move".
- Interstitial accesses only (research segment): ARPU $0.186; ARPPU $25.7; access CR 3.97%; trial share 97.8%; trial→charge 16.4%; charge→14d cancel 33.8%; refund 6.88%.
- Ad stats: impressions 333,397 → 310,625 (-22,772, -6.8%); Total CPM+CPC revenue $1,918 → $1,771 (-$147, -7.7%).
- Retention: 1d 24.4% → 24.9% (+1.93%, p=0.25); 7d +0.158% (p=0.83); 14d -0.875% (p=0.11) — unchanged.
- Engagement: tab views per user 9.14 → 10.8 (+18.5%, p=0.00); 60s/120s/180s per user +2.94%/+3.42%/+3.39% (p=0.027/0.010/0.014); tab view 60s share -0.67% (p=0.030).
- Interstitials funnel (var 2): members → Splash View 99.74% (22,063 of 22,121); Splash View → Splash Close 84.09% (18,552); Splash View → Banner Purchase Click 5.51% (1,216); click → Purchase Process Finish 75.25% (915); members → Purchase Finish 4.14%.

Forecast (per day):

| Variation | App Experiment Start | Accesses | Charges | Revenue, $ | Ad revenue (CPM+CPC), $ | Winback access CR | Winback charge CR |
|---|---|---|---|---|---|---|---|
| control | 6,295 | 147 | 107 | $2,365 | $551 | — | — |
| variation 2 | 6,295 | 392 | 148 | $3,379 | $504 | 3.9% | 0.7% |
| diff | 0 | +245 | +41 | +$1,014 | -$47 | — | — |

## Decision
- Green SUCCESS: "Can roll out test variation."
- Summary in the decision: "On iOS, the promo splash with a 14-day re-trial for previously active but currently inactive subscribers meaningfully increases monetization and engagement: ARPU is up ~43%, access and charge conversion rates are higher, and users consume more tabs. The effect is concentrated among users who actually see the interstitial; those without interstitial access do not move."
- Caveat: "However, early cancellations jump sharply (+69% to +118%). This pattern is consistent with the offer attracting many low-intent re-trialists who cancel quickly. Retention is unchanged."
- Next step: "preferably wait to fix unified_id bug". The registry additionally shows a relaunch (#6644) closing 2025-10-17.

## Lessons & Insights
- Deliberately productizing an accidental discovery worked: the ex-subscriber re-trial appetite first seen through KS-02's segmentation bug converted into a large, significant ARPU win (+42.8%) when targeted on purpose.
- The effect is entirely concentrated in users who actually see/interact with the interstitial; the rest of the cohort is flat — clean incrementality with minimal cannibalization (ad revenue -7.7% / -$47 per day vs +$1,014 per day product revenue).
- Re-trials attract low-intent users: trial share ballooned to 68.8% of subscriptions and 14d cancels more than doubled (+118%); interstitial-sourced charges cancel at 33.8% within 14 days — long-horizon revenue quality needs monitoring.
- In-app interstitial targeting solves the reach problem that killed the push-based winback attempts (50–72% push delivery, <80% splash reach): here 99.74% of the target segment saw the splash.
- The once-per-first-tab-open-per-day + ad-fail fallback delivery mechanic (from KS-04) is a reliable, high-reach channel for segment-targeted offers.
- Offer strength research from priors: a 6-month trial alone was NOT enough for cold winback via push, but a 14-day re-trial delivered in-app at a natural moment (ad slot) converts — context and reach beat raw generosity.
