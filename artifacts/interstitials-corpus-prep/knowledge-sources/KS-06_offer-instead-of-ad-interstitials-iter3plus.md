# UG App: paywall – offer instead of ad interstitials (iterations 3+)

## Identity
- Experiment ID(s): AB 6491 (first launch of this page's iteration 1, registry 2025-09-30..2025-10-03; no results block on the page), AB 6626 (relaunch of iteration 1 — registry "(relaunch)", 2025-10-06..2025-10-16; results on page), AB 6716 (close-button relaunch — registry "(close button relaunch)", 2025-11-07..2025-11-17; solution documented as "1 iteration (relaunch with new close button)", no results block on the page), AB 6896 (iteration 2 with intro offers — registry "(2 iteration)", 2025-12-22..2025-12-29; results on page)
- Aliases: registry name "[UG Monetization] UG App: paywall – offer instead of ad interstitials" (+ the suffixes above); Confluence page title "[2025-08-20] UG App: paywall – offer instead of ad interstitials [2026-03-13]"; Jira UMN-9389 (iteration 2 analytics reference UMN-10264). Note: the direct predecessor project (KS-02) carried the registry name "UG App: changing banners and interstitials" — this page continues that same project line under the "offer instead of ad interstitials" name.
- Source: https://alice.mu.se/pages/viewpage.action?pageId=714432870
- Dates: 2025-08-20..2026-03-13
- Related experiments: iteration 3+ of the same project as KS-02 (cited: "We have already launched a very similar experiment, which resulted in an increase in ARPU, but we decided not to roll it out and to experiment more with the format"). Also builds on KS-01 ("got pretty poor results, yet we saw the perspectives of its kind of source") and KS-04 ("we tried for the first time to apply a mechanism that displays our interstitial instead of advertising once a day. This significantly increased the reach of the experiment"). "Now we want to repeat and combine the experience from previous experiments."

## Context & Research (pre-launch)
- Goal: "the main goal is to earn additional revenue with changing the zero states ads for selling subscription on the app".
- Foundation: "We want to redesign existing 'zero states' of ad-sources in order to increase sales of UG Subscriptions."
- Research chain: KS-01 poor but promising → KS-02 ARPU up but deliberately not rolled out → KS-04 proved the once-per-day ad-replacement mechanic massively increases reach → this project combines the banner/paywall offer with the daily replacement trigger.

## Hypothesis
"If we show our subscription paywall to all free users once per day instead of usual interstitial, we will increase conversion to paid subscriptions and overall revenue by at least XX%."

## Mechanics
### Iteration 1 (#6491, relaunched as #6626)
- Placement/Trigger: show UG's own interstitial paywall ONCE PER DAY to all free users, replacing the regular ad interstitial on their first eligible tab open of the day (same trigger as the monetization-video experiment, KS-04). Additionally show the interstitial paywall whenever an ad fails to load, as in previous experiments. Also add banners with subscription offers in all zero-ad states and as replacements for ad banners.
- Flow: interstitial trigger (daily or ad-fail) → pre-paywall screen → main paywall. Clicking a subscription banner sends the user directly to the paywall, skipping the pre-paywall.
- Timing: the close button on the interstitial appears after 5 seconds.
- Audience segment: only users without any subscription (free users).
- Platforms: UGT_IOS and UGT_ANDROID.
- Offer: 14-day trial (analytics values 'AD 14Free …'; calc segment "Long trials" defined by trial = 14).

### Close-button relaunch (#6716)
- "Completely analogous to iteration 1. The only difference is that we will add a new button to close the ad. Now it contains a timer and a report with the option to skip the ad."

### Iteration 2 (#6896, intro offers)
- Same mechanic as iteration 1, with the offer changed: "We will replace the 14-day trial with an introductory plan. It's will be Pro+ ($39.99 per year) with discount for first year 50%." Copyrights (copy) updated to the new offer.
- Backend: intro-offer event in subscriptions_events (analytics reference UMN-10264).

## Experiment design
- Goal metric: ARPU. Design template (#6626), parameters inherited from the KS-04 design:

| Parameter | UGT_IOS | UGT_ANDROID |
|---|---|---|
| Baseline | $0.127 | $0.056 |
| Lift, % | 23.15% | 12.89% |
| MDE | 0.017 | 0.10 |
| Power | 0.8 | 0.8 |
| Alpha | 0.05 | 0.05 |
| Sample (per variation) | 109,556 | 293,260 |
| Duration (days) | 12 | 8 |

- Exposure event: App Experiment Start (item_id = %experiment id%), sent for both variations.
- Events: Splash View / Splash Close + banner purchase funnel (Banner Upgrade View, Banner Purchase Click, Purchase Process Start/Finish/Canceled) with values 'AD 14Free Interstitial' / 'AD 14Free Search' / 'AD 14Free Song' / 'AD 14Free Tab'.
- Calc configs:
  - #6626 old config: Total {'pro_rights': 'Free'}; Without interstitial accesses (funnel_source_exclude: AD Interstitial, AD 14Free Interstitial, AD Tab, AD Song, AD Search, AD 14Free Song, AD 14Free Tab, AD 14Free Search); Long trials {'custom_sub_having': "trial = 14"}; Interstitials Funnel (Splash View → Banner Upgrade View → Banner Purchase Click → Purchase Process Finish, value like 'AD%').
  - #6626 final config: Total {'pro_rights': 'empty'}; Without interstitial accesses; Total exes {'pro_rights': 'expired any'}; Without interstitial accesses exes; Interstitials Funnel.
  - #6896 config: same as #6626 final config, plus 'AD Winback Interstitial' added to both exclusion lists.

## Execution notes
- #6491 (first launch) has no results block on the page; #6626 is its relaunch and carries the iteration-1 results.
- #6626: ran 11 days on both platforms; iOS "duration ≥ design" (12) marked incomplete, Android complete; A/B balance maintained; no visible bugs; no external effects. Samples: iOS 120,258 / 120,563; Android 32,148 / 31,934.
- #6716 (timer + report close button) documented as a solution variant; no results block on the page.
- #6896: ran 8 days; iOS "duration ≥ design" (12) incomplete, Android (8) complete; balance maintained. Samples: iOS 102,128 / 102,273; Android 117,062 / 116,618.
- Recurrent data issue: iteration-1 next steps say "Waiting for the unified_id fix" (same identity bug noted in KS-05).

## Results
### Iteration 1 (#6626 relaunch, 14-day trial offer) — Red FAIL

iOS Total (control / var 2 / diff / p):

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.181 | $0.198 | +9.71% | 0.06 |
| Access CR | 1.54% | 2% | +29.9% | 0.00 |
| Charge CR | 0.888% | 0.977% | +10% | 0.023 |
| Trials share | 51.4% | 60.8% | +18.2% | 0.00 |
| Trial → charge | 19.9% | 20.1% | +1.17% | 0.89 |
| Charge → 14d cancel | 25.2% | 27.2% | +8.19% | 0.26 |
| Retention 7d | 58.5% | 58.1% | -0.838% | 0.015 |
| Retention 14d | 70.4% | 69.9% | -0.623% | 0.019 |
| Tab view per user | 12.5 | 14.1 | +13.6% | 0.00 |
| Tab View 60s–600s shares | — | — | -1.12%…-1.67% | ≤0.020 |

- iOS stats (Total): 1,853 → 2,413 subscribers (+30%); trials 1,031 → 1,556 (+51%); charged trials 205 → 313 (+53%); revenue $21,755 → $23,927 (+10%).
- iOS Without interstitial accesses: access CR -6.88% (p=0.032); ARPU -6.81% (p=0.16); subscribers -6.6%.
- iOS Long trials: ARPU $0.00411 → $0.0277 (+574%, p=0.00); access CR +445%; charge CR +573% (base: 126 → 688 trials, 20 → 135 charges).
- iOS NO RIGHTS (free users): ARPU +3.69% (p=0.56) — minimal; revenue +4.1%.
- iOS EX SUBSCRIBERS Total exes: ARPU $0.453 → $0.537 (+18.8%, p=0.025); access CR +85.3% (p=0.00); charge CR +22% (p=0.003); trial share +105% (p=0.00); trials 193 → 724 (+280%). Without-interstitial exes: ARPU -19% (p=0.012); access CR -11.4% (p=0.035) — cannibalization inside the ex segment.
- Android Total: ARPU $0.117 → $0.138 (+18.5%, p=0.19, n.s.); access CR +29% (p=0.001); trial → charge 26.9% → 15.3% (-43.3%, p=0.002); retention 1d +3.61% (p=0.008), 7d +1.74% (p=0.005); tab view per user +4.18% (p=0.001), 60s–300s per user +3.1–3.7% (significant); 60s share -0.884% (p=0.012).
- Android segments: Long trials access CR +86.3% (p=0.00), AOV/ARPPU +23.4% (p=0.029), trial→charge -53.5% (p=0.038); NO RIGHTS access CR +30.5% (p=0.006), trial→charge -38% (p=0.045); Total exes ARPU +23.3% (p=0.29), trial→charge -49.6% (p=0.017); Without-interstitial exes trial→charge -49.8% (p=0.019).
- Frequency decay (conversion by occurrences with the interstitial banner, variation 2):

| Segment | occurrence | splash views | splash → access | splash → charge |
|---|---|---|---|---|
| iOS no rights | 1 | 55,922 | 1.58% | 0.83% |
| iOS no rights | 2 | 20,366 | 0.87% | 0.43% |
| iOS no rights | 3 | 10,025 | 0.52% | 0.29% |
| iOS no rights | 4+ | 13,438 | 0.41% | 0.22% |
| iOS ex subs | 1 | 9,831 | 2.59% | 2.10% |
| iOS ex subs | 4+ | 1,786 | 0.95% | 0.78% |
| Android no rights | 1 | 11,740 | 1.36% | 0.43% |
| Android no rights | 4+ | 8,027 | 0.27% | 0.15% |
| Android ex subs | 1 | 448 | 4.02% | 3.13% |

- Funnel (iOS var 2): members → Splash View 98.61% (118,889); Splash → Banner Upgrade View 12.09%; → Banner Purchase Click 13.89%; → Purchase Finish 42.79%; members → purchase 0.71%. Android var 2: 93.78% / 15.15% / 12.71% / 23.74%; members → purchase 0.43%.
- Forecast (per day): Android +$1,759 revenue (ad revenue -$5); iOS +$2,937 (ad revenue -$388). NO RIGHTS: iOS +$685 and -$329 ad revenue; Android +$772. EX SUBSCRIBERS: iOS +$2,162; Android +$918.
- Conclusion (verbatim highlights): "Do not roll out as-is." "As a result, our trial sign-up rate increased (30-86% in different segments), but our conversion rate to paid subscriptions decreased (36-54%). The quality of trials is declining significantly." "Free users are in the black by $685. And we are losing another $320 on advertising, so in fact we are in the black by $365 per day, giving everyone free access for two weeks." "The 5s close delay likely adds friction, reducing perceived UX quality and diluting trial quality." "Notably, Long-trials cohorts show strong ARPU/charge CR lifts on iOS…, suggesting potential when user intent is high, but current broad targeting degrades overall monetization quality." "on iOS most of revenue increase came from ex subscribers, while free users have minimal impact."
- Next steps: wait for the unified_id fix; re-tune the interstitial (shorten/instant close, reduce default emphasis on the free trial — promote direct purchase or clearer terms — and/or cap frequency, e.g. ad-fail only or high-intent users), especially on Android with its ~10% trial→charge; re-test with KPIs ARPU, trial→charge, 7d retention.

### Iteration 2 (#6896, 50%-off first-year Pro+ intro plan instead of trial)

iOS Total:

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.222 | $0.248 | +11.5% | 0.016 |
| AOV | $20.1 | $18.2 | -9.31% | 0.00 |
| ARPPU | $20.6 | $18.5 | -10.2% | 0.00 |
| Access CR | 1.89% | 2.21% | +16.8% | 0.00 |
| Charge CR | 1.08% | 1.34% | +24.1% | 0.00 |
| Trials share | 59% | 53.4% | -9.48% | 0.000 |
| Charge → 14d cancel | 25.7% | 26% | +1.09% | 0.87 |

- iOS stats: subscribers 1,934 → 2,262 (+17%); instants 831 → 1,096 (+32%); buyers 1,102 → 1,370 (+24%); revenue $22,678 → $25,325 (+12%); cancels 14d 290 → 361 (+24%).
- iOS Total exes: ARPPU +8.32% (p=0.026); trial→charge 17.8% → 24.8% (+39.4%, p=0.027); ARPU +7.75% (p=0.31). Without-interstitial exes: ARPPU +8.79% (p=0.027); ARPU +10.2% (p=0.21).
- iOS Without interstitial accesses: ARPU $0.222 → $0.204 (-8.18%, p=0.08); revenue -8.1% — the conclusion quantifies this as "on iOS we lose about 30% of received gain in revenue" (cannibalization).
- iOS engagement/retention: tab views per user +11.5% (p=0.00); 60s/120s/180s shares -0.641%/-0.866%/-0.802% (p≤0.009); retention flat (14d -0.496%, p=0.11).
- iOS ad revenue: $2,453 → $1,732 (-$721, -29%).

Android Total:

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.113 | $0.141 | +25% | 0.000 |
| AOV | $24.8 | $21.6 | -12.9% | 0.00 |
| ARPPU | $25.6 | $22 | -14% | 0.00 |
| Access CR | 0.999% | 1.12% | +12.1% | 0.004 |
| Charge CR | 0.439% | 0.638% | +45.3% | 0.00 |
| Trials share | 68.9% | 53.7% | -22% | 0.00 |
| Trial → charge | 16% | 17.4% | +9.02% | 0.44 |
| Charge → 14d cancel | 19.2% | 14.1% | -26.6% | 0.016 |
| Charge → 14d refund | 2.82% | 1.45% | -48.7% | 0.10 |

- Android stats: subscribers 1,169 → 1,306 (+12%); instants 389 → 630 (+62%); buyers 514 → 744 (+45%); revenue $13,172 → $16,397 (+24%); refunds 14d 15 → 11 (-27%).
- Android Without interstitial accesses: ARPU +3.39% (p=0.65) — neutral. Total exes: ARPU -2.2% (p=0.77). Without-interstitial exes: trial share 6.98% → 18.1% (+160%, p=0.00); trial→charge -54.3% (p=0.16).
- Android retention flat (1d -0.69% p=0.37; 7d -0.0111% p=0.98); tab view 60s share -0.535% (p=0.026), rest neutral.
- Android ad revenue: $293 → $270 (-$23, -8%).
- Funnels (var 2): iOS members → Splash View 97.31% (99,517), Splash → Banner Upgrade 31.20%, → Purchase Click 3.80%, → Finish 28.41%, members → purchase 0.33%; Android 96.91% / 28.14% / 5.64% / 13.61%, members → purchase 0.21%.
- Forecast (per day): Android control $3,499 → var 2 $4,372 (+$873; 66 intro subscriptions/day; ad revenue -$6); iOS control $7,000 → var 2 $7,806 (+$806; 101 intro subscriptions/day; ad revenue -$223).
- Conclusion (verbatim highlights): "The paywall interstitial and banners drove clear monetization gains with minimal user-cost signals." "ARPU increased on both iOS (+11.5%) and Android (+25.0%), supported by higher access and charge conversion and stronger downstream conversion (subscriber -> buyer and subscription -> charge)." "AOV/ARPPU fell on both platforms, because of the first year intro prices." "Android also saw a significant drop in 14-day cancellations. Retention did not change." "Engagement signals show a small decline in long-view shares (60/120/180s) on both platforms, likely from the 5s-close interstitial friction, but iOS total tab views per user actually grew (+11.5%)." "Works only on free users. doesn't affect ex subscribers." "on iOS we lose about 30% of received gain in revenue."

## Decision
- Iteration 1 (#6626): Red FAIL — "Do not roll out as-is" (trial-quality collapse -36…-54% trial→paid, iOS 7d/14d retention decline, gains concentrated in ex-subscribers, thin net economics ~$365/day for free users after ad-revenue loss).
- Iteration 2 (#6896): "Overall recommendation: can roll out on both platforms with post roll out control of churn and next year recurrent rate for intro plans." (The Next-steps field of iteration 2 is left empty on the page.)

## Lessons & Insights
- Offer type is the decisive lever on the same placement: a 14-day free trial inflates trial starts (+30–86% by segment) but collapses trial→paid (-36–54%) and nets only ~$365/day; a 50%-off first-year intro plan flips the pattern — fewer trials (share -9.5% iOS / -22% Android), +32–62% instant purchases, ARPU +11.5% iOS / +25% Android, and Android 14d cancels DOWN -26.6%.
- Intro pricing trades AOV/ARPPU (-9% to -14%) for volume and conversion quality; the open risk moves to next-year recurrence for the discounted cohort — the explicit post-rollout watch item.
- Cannibalization persists on iOS: ~30% of the gross gain is lost via other sources and ad revenue (in-cohort iOS ad revenue -29%; forecast -$223/day), while Android is nearly free of it (-$6/day).
- Interstitial conversion decays steeply with repeat daily exposures (free users splash→access 1.58% → 0.41% by the 4th encounter) — the first daily impression carries most value, echoing KS-02's finding.
- Segment-offer fit: trial-style offers activate ex-subscribers strongly (iteration 1 exes ARPU +18.8%, access CR +85%) but the intro-price iteration "works only on free users, doesn't affect ex subscribers" — the winback line (KS-05) covers exes with a dedicated re-trial offer instead.
- The 5-second close delay is repeatedly implicated in engagement-share declines and trial-quality dilution; a timer+report close button was designed as the friction fix (#6716).
- High-intent subgroups (Long-trials cohorts) show outsized lifts (iOS ARPU +574% off a tiny base), suggesting targeting intent rather than broad exposure as a future direction.
