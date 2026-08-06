# UG App: paywall – offer instead of ad interstitials (iterations 1–2)

## Identity
- Experiment ID(s): AB 6002 (original launch, registry 2025-04-28..2025-05-05; not covered by a results block on the page), AB 6128 (labeled "Iteration #1" on the page; registry name suffix "(2 iteration)", 2025-06-02..2025-06-06), AB 6191 (relaunch of that iteration; registry "(2 iteration - relaunch)", 2025-06-06..2025-06-19)
- Aliases: AB registry name "[UG Monetization] UG App: changing banners and interstitials" (with the iteration suffixes above); Confluence page title "[2025-04-11] UG App: paywall – offer instead of ad interstitials [2025-07-10]"; Jira UMN-8263
- Source: https://alice.mu.se/pages/viewpage.action?pageId=682704865
- Dates: 2025-04-11..2025-07-10
- Related experiments: successor of KS-01 "Interstitial - Swap into Landing" (cited as the prior launch with "pretty poor results, yet we saw the perspectives of its kind of source"). KS-06 "offer instead of ad interstitials (iterations 3+)" is a later iteration of this same project. KS-04 (monetization video) and KS-05 (winback interstitials) both cite this experiment as research foundation.

## Context & Research (pre-launch)
- Goal: "the main goal is to earn additional revenue with changing the zero states ads for selling subscription on the app".
- Foundation: redesign existing 'zero states' of ad sources to sell UG Subscriptions through the same slots with a new approach.
- Research: the previous launch (KS-01) got pretty poor results but showed the source's potential.
- A/B test model (iOS, based on conversion from the last interstitial experiment):

| Metric | A | B | diff |
|---|---|---|---|
| ad banners placement | 36,047 | 36,047 | — |
| Accesses | 124 | 212 | 88 |
| Charges | 78 | 133 | — |
| ad banners → Access, % | 0.34% | 0.59% | 71% |
| Revenue, $ | $2,066 | $3,532 | — |
| ARPPU, $ | $26.5 | $26.5 | — |
| ARPU, $ | $0.058 | $0.098 | $0.04 |

## Hypothesis
"If we swap zero-states ads with new paywalls, it will help us earn additional 71% revenue, because landing can show all the benefits of subscription."

## Mechanics
- Placement: inner banner selling access to UG Pro+ shown in place of ad interstitials AND ad banners (tab page, versions page, search page) whenever there is no ad to show.
- Trigger: user enters a screen with an ad source and gets no ad to see (adfail event / no response on the ad request → show inner). For banners: no ad OR zero-state (Melodics house ad) → replace with the new subscription banner. On iOS: user enters the tab, last-visit data is checked; either the ad loads (shown, last-show time stored) or ad_load_failed fires and the app tries next time. On Android the server constantly cycles this ("the server tries to show ad, but can not, due to it has no ad to show").
- Timing: on the interstitial, the close button appears after 5 seconds.
- Frequency: existing interstitial logic kept — max 5 shows per day, 180 sec gap between shows, logic renews daily at 23:59.
- Flow: clicking on the banner or interstitial → paywall with 'Go ad-free experience'.
- Audience segment: iteration 1 — only free users without any subscriptions (excluding Edu and Sings singles). Iteration 2 — same, but additionally excluding ex-premium users (those who ever had any pro rights) to avoid the repeat-trials issue.
- Platforms: iOS and Android.
- SKUs / offers shown: Pro+ $39.99 / year with extended 14-day trial. New products for the 14-day trial: iOS com.ultimateguitar.ugt.plus.1year7, Android com.ultimateguitar.tabs.plus.1year5.

## Experiment design
- Arms: A (control, existing ad/zero-state behavior) vs B (subscription banner/interstitial + paywall).
- Primary metric: Interstitial → Access, %.
- Design parameters (iOS): baseline 0.34%, lift 71%, MDE 0.036, power 0.8, alpha 0.05, sample size per variation 36,047, duration 1 day per unit; design summary: sample 252,329, 7 days; seasonality — whole week taken in calculations.
- Design vs Reality tables list: iOS design 6 days / 301,929 per arm; Android design 10 days / 297,550 per arm.
- Exposure event: App Experiment Start (item_id = %experiment id%), sent for both variations when an ad failed to load on tab, search, or during an interstitial.
- Events: Splash View / Splash Close (value 'AD Interstitial' from interstitial, 'AD Tab' from tab page, 'AD Search' from search page in-between versions); existing banner funnel with the new values: Banner Upgrade View, Banner Purchase Click, Purchase Process Start, Purchase Process Finish, Purchase Process Canceled.

## Execution notes
- AB 6002 was the original registry launch (2025-04-28..2025-05-05); the page's Results section documents 6128 and 6191 only.
- Iteration 1 (#6128): ran 5 days vs design 6 (iOS) / 10 (Android) — "duration ≥ design" incomplete on both platforms; A/B balance maintained; no visible bugs; no external effects. Samples: iOS 85,075 / 85,327; Android 77,246 / 77,062.
- Iteration 1 segmentation bug: ex-premium users were included; on iOS 21% of users who tried to get the 14-day trial were instantly charged instead; ~37% of interstitial revenue came from ex-trial subscribers.
- Iteration 2 (#6191): full relaunch with ex-premium excluded. Ran 14 days; all checks complete. Samples: iOS 260,468 / 259,687; Android 156,391 / 157,021.

## Results
### Iteration 1 (#6128) — FAIL
Headline results (page bullets):
- ARPU increased 24% iOS and 13% Android.
- Ex-trial problem on iOS: 21% of users tried to get 14d trials but got instantly charged instead.
- iOS interstitials have 13% less conversion rate from trials than average; Android -45%.
- Cannibalization: iOS — 34% of earnings cannibalized by reduced accesses from other sources; Android — 63%.

iOS monetization metrics (control / variation 2 / diff / p):

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.11 | $0.14 | +23.62% | 0 |
| AOV | $22.65 | $23.51 | +3.81% | 0.18 |
| ARPPU | $23.19 | $23.93 | +3.20% | 0.20 |
| access CR | 0.80% | 1.06% | +33.28% | 0 |
| charge CR | 0.49% | 0.59% | +19.79% | 0.0062 |
| trial → charge | 28.68% | 26.81% | -6.51% | 0.52 |
| charge → 14d cancel | 17.80% | 19.22% | +7.96% | 0.58 |

- iOS stats: control 85,082 members / 669 subs / $9,859 rev; var 2 85,332 / 901 / $12,326. Interstitials-only (var 2): 274 subscribers, 188 trials, 50 ex trials, 134 charges, $3,557, ARPU $0.042, trial→charge 24.47%. Interstitials-only rights=0: 72,941 members, 184 subs, $1,308.
- iOS Without-interstitials segment: ARPU -11.32% (p=0.12), access CR -5.96%, charge CR -10.22% (p=0.13) — the cannibalization signal.
- iOS retention: ret1d 20.02% → 19.69% (-1.64%, p=0.089); ret7d 24.66% → 24.27% (-1.58%, p=0.062).

Android monetization metrics:

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.10 | $0.11 | +12.51% | 0 |
| AOV | $26.38 | $25.71 | -2.53% | 0.51 |
| ARPPU | $26.74 | $26.09 | -2.42% | 0.54 |
| access CR | 0.72% | 1.33% | +83.11% | 0 |
| charge CR | 0.38% | 0.44% | +15.29% | 0.074 |
| trial → charge | 19.66% | 11.39% | -42.08% | 0.00053 |
| charge → 14d cancel | 13.80% | 13.16% | -4.69% | 0.81 |

- Android stats: control 77,258 members / 560 subs / $8,101; var 2 77,072 / 1,023 / $9,500. Interstitials-only (var 2): 526 subscribers, 487 trials, 0 ex trials, 106 charges, $3,103, ARPU $0.023, trial→charge 11.29%. Rights=0 only: $1,203.
- Android Without-interstitials: ARPU -20.85% (p=0.013), charge CR -15.74% (p=0.044), trial→charge -37.62% (p=0.0060).
- Android retention: ret1d +1.30% (p=0.16), ret7d +0.44% (p=0.55).
- Forecast (per day): iOS control $7,231 → var 2 $8,939 (+$1,708, +175 accesses, +61 charges); Android $4,211 → $4,737 (+$526, +253 accesses, +24 charges).
- Team's read: "can be roll outed, but will have an effect of tour update with most revenue on start"; fixed the ex-subscription problem and relaunched.

### Iteration 2 (#6191, relaunch, ex-premium excluded) — FAIL
Headline results:
- iOS ARPU +7.5% (vs +24% in iteration 1): $0.19 → $0.20 (p=0.029). ~37% of iteration-1 interstitial revenue was from ex-trial subscribers, now fixed.
- Android +5% non-significant (vs +13%): $0.145 → $0.153 (+4.94%, p=0.36), with almost no charges from ex-subscribers.
- Interstitials-only ARPU: iOS $0.021 (vs $0.018 in iteration 1), Android $0.020 (vs $0.018) — "all matches if take into account all users with rights 4 and 5".

iOS (control / var 2 / diff / p): access CR 1.33% → 1.48% (+11.32%, p=0); charge CR 0.83% → 0.88% (+5.77%, p=0.060); trial→charge 28.32% → 28.33% (+0.028%, p=1.0); 14d cancel +5.89% (p=0.37); refund 14d +7.19% (p=0.63). Stats: control 260,468 members / 3,468 subs / $48,568; var 2 259,687 / 3,849 / $52,073. Interstitials-only (var 2): 597 subs, 495 trials, 224 buyers, $5,381, ARPU $0.021, trial→charge 24.39%, 14d cancel 27.11%. Without-interstitials: ARPU -3.57% (p=0.29), access CR -5.95% (p=0.011). Retention: ret1d -0.41% (p=0.40), ret7d -0.65% (p=0.026).

Android: access CR 1.00% → 1.23% (+23.60%, p=0); charge CR +7.28% (p=0.13); trial→charge 21.65% → 18.96% (-12.45%, p=0.11); 14d cancel +20.91% (p=0.10). Stats: control 156,391 / 1,560 subs / $22,755; var 2 157,021 / 1,936 / $23,975. Interstitials-only (var 2): 433 subs, 411 trials, $3,062, ARPU $0.020, trial→charge 17.27%, 14d cancel 20.0%. Without-interstitials: ARPU -8.46% (p=0.11), trial→charge -9.03%, 14d cancel +16.70%. Retention: ret1d -1.21% (p=0.060), ret7d -1.18% (p=0.0021).

- Forecast (per day): iOS control $11,864 → var 2 $12,758 (+$894); Android $6,041 → $6,340 (+$299).
- Key finding: "despite fixing only one part with ex subscribers we got 2-3 times worse results than in the previous iteration"; some users with rights 4 or 5 were still able to get a valid trial without paying instantly, and excluding them removed almost all of the revenue improvement.

### Post-rollout research (deep-dives on the page)
Q: Funnel by pro rights (why conversions differed so much in iteration 2):
- 30% of iOS users in the experiment didn't see the interstitial at all.
- Ex-subscription users have 13x higher conversion rate than free users on Android and 3.6x higher on iOS.
- Most ex-subscribers were still able to get a valid trial; ALL Android ex-trial users could get a trial again; 27% of iOS ex-trial users could get another valid trial.
- Android ex-trial users convert at only 8% from trial — 50% less than free users ("seems like for them it's just another free 14 days").
- Data-quality note: "need to fix problem with Charge only events without Subscription".

| source | rights | members | banner clicks | accesses | banner → access, % | trials → charge | revenue | ARPU |
|---|---|---|---|---|---|---|---|---|
| UGT_ANDROID | free | 68,759 | 991 | 202 | 0.30% | 16% | $1,315 | $0.019 |
| UGT_ANDROID | ex | 8,349 | 487 | 325 | 3.93% | 8% | $1,379 | $0.165 |
| UGT_IOS | free | 73,102 | 472 | 193 | 0.36% | 21% | $1,518 | $0.021 |
| UGT_IOS | ex | 12,452 | 433 | 117 | 1.32% | 46% | $2,712 | $0.218 |

Q: Funnel by region tiers (tier1 US/CA/GB, tier2 EU, tier3 other):
- iOS regional distribution of the new banner matches the ad interstitials it replaces (e.g. US: banner share 44.5% vs ad share 44.8%).
- Android has ad interstitials only in the EU and in almost absent amounts (~3k unique views in 5 days).
- Best ARPU cells: iOS US $0.075, Android US $0.068, Android CA $0.063; worst: Android Other $0.0093.

Q: Effectiveness by number of banner encounters (+ by rights):
- iOS ex: 1.5% conversion to access from the FIRST banner interaction — 87% of all their interstitial accesses; free users 0.3–0.4% on views 1–3, 77% of accesses from the first.
- Android ex: 7.5% conversion on first interaction (66% of accesses), 3.8% on second; free 0.5% on first (60% of accesses).

Q: Retention impact:
- Correlation between banner occurrences and 1/7/14d retention is >0.95 (Android) / >0.85 (iOS), but the same correlation holds with the number of sessions with tabs — "number of banner most probably doesn't affect on future retention, while it depends on how many times user have already entered app".

Q: Session-duration impact:
- iOS: strong negative correlation -0.96 with banner count, but identical for tab sessions → likely no real effect.
- Android: strong positive correlation 0.99 with banner count and no correlation (abs<0.2) with tab sessions → probably a real effect: more banners → ~10% longer average sessions.

Q: Ad shown before our interstitial:
- Conversion from the interstitial banner is ~30% worse if the user saw an ad interstitial before it: members→access 0.47% (didn't see ad first) vs 0.34% (saw ad first), -28%; members→charge 0.14% vs 0.12%, -14%.

Q: CPM comparison (ours vs ads, by tier):
- iOS banner "CPM" ~10x the ad CPM: US/CA/GB $55.51 vs $5.36; EU $19.64 vs $2.19; Other $12.06 vs $1.81.
- Android: ads $0 (no ad interstitials); banner CPM $75.70 (US/CA/GB), $35.17 (EU), $9.33 (Other).

## Decision
FAIL / no rollout: "Even though ARPU is growing, we won't roll out the current solution yet. First, we'll test other alternatives to replace ads and try less generous offers. We want to avoid the novelty effect trap, where the audience quickly drops off. Instead, we'll implement a general solution first and then fine-tune it with offers if needed." → next project (the video format, KS-04, then iterations 3+, KS-06).

## Lessons & Insights
- Most of the apparent iteration-1 win was an artifact: mis-included ex-premium users (repeat trials / instant charges) generated ~37% of interstitial revenue; cleaning the segment shrank the effect 2–3x.
- Heavy cannibalization of other paywall entry points on the tab: 34% (iOS) to 63% (Android) of the new source's earnings offset by reduced accesses elsewhere.
- Ex-subscribers are the strongest responders to interstitial offers (up to 13x CR) — this insight directly seeded the winback-interstitial project (KS-05).
- The generous 14-day trial pulls low-quality trials: interstitial trial→charge conversion is below average (-13% iOS, -45% Android; Android ex-trial users convert at just 8%).
- The first impression does nearly all the work; effectiveness decays sharply with repeat views (60–87% of accesses from the first encounter).
- Banners don't hurt retention once you control for visit frequency; on Android they may even lengthen sessions ~10%.
- Ad-primed users convert ~30% worse on the offer — sequencing matters.
- Monetizing the slot with own offers yields ~10x the "CPM" of the ads it replaces (iOS), which frames the opportunity cost of ad inventory.
