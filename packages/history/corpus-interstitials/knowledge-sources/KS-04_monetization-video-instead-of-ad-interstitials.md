# UG App: paywall – monetization video instead of ad interstitials

## Identity
- Experiment ID(s): AB 6359 (iteration 1, registry 2025-07-18..2025-07-29), AB 6416 (relaunch of iteration 1 — registry "[…] (relaunch)", 2025-07-29, Jira UMN-8999; no separate results block on the page), AB 6428 (iteration 2, registry "(2 iteration)", 2025-08-04..2025-08-11)
- Aliases: registry name "[UG Monetization] UG App: paywall – monetization video instead of ad interstitials"; Confluence page title "[2025-07-09] UG App: paywall – monetization video instead of ad interstitials [2025-XX-XX]" (end date left open on the page); Jira UMN-8994
- Source: https://alice.mu.se/pages/viewpage.action?pageId=707139549
- Dates: 2025-07-09..2025-08-11
- Related experiments: builds directly on KS-02 ("static banner with an offer (14-day trial) in place of the ad interstitials … significant ARPU increase of 7.5% in iOS and a non-significant 5% in Android"). Its once-per-day ad-replacement mechanic was then reused by KS-05 (winback) and KS-06 (offer instead of ads, iterations 3+), both of which cite this page as research foundation.

## Context & Research (pre-launch)
- Goal: "the main goal is to earn additional revenue with changing the zero states ads for selling subscription on the app"; this project tests another format — video ads for the subscription.
- Foundation: "Currently, if there are no ads for a user, then the interstitial is skipped. We want to use this opportunity to show a monetization scenario."
- Reach research (unique users): iOS — expect at least 35k users/day to see the monetization interstitial at least once; Android — at least 85k users/day (Android has no ad interstitials). In iOS, 80% of users with admob_fail have ≤5 display attempts; on Android ~90%. A show limit is needed because 20% of users make between 5 and 200 show attempts. Open question flagged: "Why does the sum of fails and shown not equal the number of requests?" — trigger definition needed discussion.
- Model, iteration 1 (avg per day; only users without pro rights → toUInt8(rights%10) in (0,4,5)):

| Metric | iOS A | iOS B | Android A | Android B |
|---|---|---|---|---|
| Tab Open (not Official/Pro/Vocal) | 161,074 | 161,074 | 90,426 | 90,426 |
| admob_fail | 36,733 | 36,733 | 90,426 | 90,426 |
| tab open → admob_fail | 22.81% | 22.81% | 100% | 100% |
| monetization interstitial view | — | 36,733 | — | 90,426 |
| interstitial CTR (assumed) | — | 10% | — | 10% |
| paywall cannibalization rate | 20% | 20% | 20% | 20% |
| paywall view | 12,406 | 15,344 | 55,983 | 63,216 |
| accesses | 308 | 380 | 354 | 399 |
| charges | 203 | 250 | 194 | 219 |
| ARPPU | $22.98 | $22.98 | $26.00 | $26.00 |
| Revenue | $4,664.94 | $5,745.00 | $5,044.00 | $5,694.00 |
| ARPU (admob_fail) | $0.127 | $0.156 (+23.15%) | $0.056 | $0.063 (+12.89%) |

- Model, iteration 2 (iOS, admob_request 155,890/day, CTR 10%, cannibalization 60–70%): paywall views 77,037 → 83,272; accesses 1,038 → 1,122; charges 685 → 740; revenue $15,741 → $17,005 (+$1,264); ARPU (admob_request) $0.101 → $0.109 (+8.03%).

## Hypothesis
"If we implement the display of video interstitials with a subscription promotion, when the user does not see an advertising interstitial, we expect ARPU to increase by 23% without a drop in 7-day Retention because in the past experiment we saw a similar growth in metrics with another version of the interstitial."

## Mechanics
### Iteration 1 (#6359, ABC test)
- Trigger: show a promo clip when an "admob_fail" event is received (ad interstitial failed to load) on tab entry. Not displayed in offline mode.
- Frequency: no more than once every 30 seconds and no more than 5 times a day (covers 80% of the audience; "the first 3 showings are the most effective for conversion" per the previous project).
- Creatives: most-converting creatives from the paid UA team (Milanote list); two formats — playing songs by tabs (variation B) and by chords (variation C); in variation C the in-video button changed from "install" to "try for free".
- Presentation: sound kept but muted by default; close "x" appears after 5 seconds (circle-filling animation, tap area matching current ad interstitials); "Try for Free" button on the video, active and visible throughout; if the video ends it stops on the last frame — exit only via "x".
- Click action: opens the standard pro-paywall; trial availability follows the standard current procedure (may vary with the user's past subscriptions).
- Audience: all users without Pro rights (both new users and former subscribers).
- Platforms: UGT_IOS and UGT_ANDROID.

### Iteration 2 (#6428)
- Platform note: the Solution block says "iOS only", but results were computed and reported for both UGT_IOS and UGT_ANDROID.
- Trigger: first tab opening of the current day — the monetization video interstitial REPLACES the standard ad interstitial. For all ad views after the first one, normal ads are shown (in both arms). Additionally, when the user should see ads but no ad inventory is available, the custom interstitial is displayed.
- Delivery: video starts loading at app launch and is saved on the user's device for reuse. Close button ("×") appears after a 5-second mandatory viewing period. Iteration-1 logic otherwise maintained.

## Experiment design
- Goal metric: ARPU.

| Parameter | UGT_IOS | UGT_ANDROID |
|---|---|---|
| Baseline | $0.127 | $0.056 |
| Lift, % | 23.15% | 12.89% |
| MDE | 0.017 | 0.10 |
| Power | 0.8 | 0.8 |
| Alpha | 0.05 | 0.05 |
| Sample (per variation) | 109,556 | 293,260 |
| Duration (days) | 12 | 8 |

- Iteration 1 arms: A control (interstitial skipped on no-ad), B video "songs by tabs", C video "songs by chords". Iteration 2 arms: A control (standard ad interstitials), B video replaces first daily ad interstitial.
- Exposure events: iteration 1 — admob_fail; iteration 2 — admob_try_show (spec) / admob_request (results header).
- Events: Interstitial Video Try Show (video starts loading), Interstitial Video Fail (value='timeout', loader >3s), Interstitial Video Shown (first frame visible, close-timer starts), Interstitial Video View (≥1s watched), Interstitial Video Close / Mute / Unmute; banner funnel with value 'AD Interstitial' (Banner Upgrade View, Banner Purchase Click, Purchase Process Start/Finish/Canceled).
- Calc segments: Total {'pro_rights': 'Free'}; Without interstitial accesses {'pro_rights': 'Free', 'funnel_source_exclude': ['AD Interstitial']}; Interstitials Funnel.

## Execution notes
- Iteration 1 (#6359): ran 12 days on both platforms (Android design was 8); all checks complete; no visible bugs; no external effects. Samples: iOS 19,922 / 19,570 / 18,679 (control/v2/v3); Android 93,901 / 94,481 / 86,952. Variation 3 has notably fewer members than control (-6.2% iOS, -7.4% Android) even though the balance check is marked complete.
- AB 6416 is a same-day relaunch of iteration 1 per the registry (2025-07-29); the page carries two near-identical #6359 result blocks (a recalculation) and no separate #6416 block.
- Iteration 2 (#6428): ran 8 days; all checks complete. Samples: iOS 194,594 / 195,124; Android 116,915 / 115,783.
- Video delivery was lossy in iteration 1: Interstitial Video Fail = 28.05% of Try Shows (iOS v2) and 48.23% (Android v2) — a large share of intended impressions never rendered. Iteration 2 addressed this by preloading/caching the video.

## Results
### Iteration 1 (#6359)
iOS monetization metrics (Total):

| Metric | control | var 2 | diff, % | p | var 3 | diff, % | p |
|---|---|---|---|---|---|---|---|
| ARPU / LT ARPU | $0.202 | $0.17 | -15.8% | 0.20 | $0.221 | +9.12% | 0.49 |
| AOV | $24.3 | $22.2 | -8.47% | 0.20 | $23.2 | -4.59% | 0.47 |
| ARPPU | $25 | $22.2 | -11.2% | 0.08 | $24.1 | -3.67% | 0.55 |
| Access CR | 1.29% | 1.25% | -2.95% | 0.74 | 1.34% | +3.75% | 0.68 |
| Charge CR | 0.808% | 0.766% | -5.16% | 0.64 | 0.915% | +13.3% | 0.25 |
| Trial → charge | 30.3% | 23.8% | -21.4% | 0.20 | 28.9% | -4.78% | 0.78 |

iOS "Without interstitial accesses" (cannibalization check): var 2 ARPU $0.152 vs $0.202 → **-24.7% (p=0.039, significant)**; access CR -13.6% (p=0.11); charge CR -14.6% (p=0.17); trial→charge -29% (p=0.09); revenue $2,983 vs $4,031 (-26%). Var 3: ARPU +5.14% (p=0.69), n.s.
iOS engagement: tab view per user +11.5% v2 / +8.52% v3 (both p=0.00); retention ~flat (v2 1d -0.843% p=0.58, 7d +0.243% p=0.74).
iOS stats: control 257 subs / $4,031; v2 245 / $3,334 (revenue -17%); v3 250 / $4,125 (+2.3%); v2 refunds 14d -50%.

Android monetization metrics (Total):

| Metric | control | var 2 | diff, % | p | var 3 | diff, % | p |
|---|---|---|---|---|---|---|---|
| ARPU / LT ARPU | $0.163 | $0.191 | +16.9% | 0.014 | $0.155 | -4.94% | 0.45 |
| AOV | $26.2 | $27.7 | +5.41% | 0.07 | $27.6 | +5.09% | 0.11 |
| Access CR | 1.07% | 1.22% | +14% | 0.002 | 1.09% | +2.4% | 0.60 |
| Charge CR | 0.608% | 0.682% | +12.1% | 0.046 | 0.555% | -8.65% | 0.14 |
| Trials share | 57.4% | 59.3% | +3.35% | 0.36 | 64.7% | +12.8% | 0.001 |
| Trial → charge | 23.3% | 22.1% | -5.04% | 0.61 | 21.5% | -7.48% | 0.46 |

Android stats: control 1,004 subs / $15,349; v2 1,152 / $18,060 (+18%); v3 952 / $13,511 (-12%).
Android "Without interstitial accesses": v2 ARPU +9.54% (p=0.16, no significant cannibalization); v3 access CR -8.68% (p=0.050), charge CR -13.9% (p=0.016), trial share +8.3% (p=0.033), ARPU -10.8% (p=0.10).
Android retention: v2 neutral (1d -0.566% p=0.52); v3 significantly down — 1d -2.6% (p=0.003), 7d -1.38% (p=0.001), 14d -1.22% (p=0.000).
Android engagement: v2 tab view per user +21.5% (p=0.00), 300s/600s per user +2.55%/+2.82% (p=0.006/0.020); v3 per-user rates -7.4%…-11.1% and view shares -0.6%…-4.1% (significant) — "quality of viewing down".

Interstitials funnel (iteration 1):

| Platform / arm | members → Try Show | Fail rate | Shown | View | Purchase Click of Upgrade View | members → Purchase Finish |
|---|---|---|---|---|---|---|
| iOS v2 | 81.19% | 28.05% | 85.47% | 95.45% | 0.80% | 0.12% |
| iOS v3 | 80.66% | 21.57% | 88.91% | 94.56% | 0.49% | 0.07% |
| Android v2 | 75.73% | 48.23% | 73.70% | 94.35% | 1.03% | 0.10% |
| Android v3 | 74.80% | 49.67% | 72.33% | 97.06% | 0.72% | 0.08% |

Forecast (per day): Android control $7,328 → v2 $8,570 (+$1,242) / v3 $6,966 (-$362); iOS control $2,746 → v2 $2,312 (-$434) / v3 $2,997 (+$251).

Iteration-1 decision text: "Do not roll out globally. Variation 2 is a clear win on Android (ARPU +17%, access/charge CR up, engagement up) with neutral retention—recommend a staged Android-only rollout. On iOS, Variation 2 shows a significant ARPU drop in the 'Without interstitial accesses' segment; hold iOS. Variation 3 should be rejected: it hurts Android retention and downstream monetization despite higher trial share and mixed engagement signals."
Planned next steps: P0 — ship Variation 2 to Android behind a ramp (10%→50%→100%) with guardrails ARPU ≥ +10%, charge CR ≥ +5%, 1/7/14d retention not worse than -0.5%; monitor cancels/refunds 14 days. P1 — deep-dive iOS (segment by exposure saw-clip-vs-not, country, cohort new vs lapsed, trial availability, creative; validate no tracking/eligibility bias due to admob_fail/offline; iterate creatives or disable the "Try for Free" overlay and re-test a small iOS slice). P2 — pause Variation 3; if revisiting, reduce frequency / shorten close delay / alternative creatives; add latency/exposure diagnostics.

### Iteration 2 (#6428)
iOS (Total): ARPU $0.237 → $0.243 (+2.66%, p=0.43, n.s.); access CR +2.52% (p=0.31); charge CR +2.01% (p=0.51); retention flat (1d -0.72% p=0.22); tab view per user 10.9 → 12.4 (+14.2%, p=0.00); tab view 60s/120s/180s shares +0.534%/+0.461%/+0.482% (p=0.001/0.019/0.040). Without-interstitial ARPU -2.93% (p=0.38). Stats: 3,210 → 3,300 subscribers; revenue $46,145 → $47,503 (+2.9%).

Android (Total):

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.135 | $0.16 | +19% | 0.004 |
| Access CR | 0.953% | 1.07% | +12% | 0.006 |
| Charge CR | 0.511% | 0.598% | +16.9% | 0.005 |
| Trial → charge | 19.2% | 24.1% | +25.5% | 0.023 |
| Retention 1d | 22.5% | 21.7% | -3.29% | 0.00 |
| Retention 7d | 56.5% | 55.7% | -1.46% | 0.00 |
| Retention 14d | 67.6% | 67% | -0.918% | 0.001 |
| Tab view per user | 11 | 13.4 | +21.9% | 0.00 |
| Tab view 60s share | 76.9% | 76.4% | -0.648% | 0.005 |

Android stats: 1,114 → 1,236 subscribers; charged trials 133 → 184 (+38%); revenue $15,733 → $18,548 (+18%). Without-interstitial segment: trial→charge +26.4% (p=0.024), ARPU +9.2% (p=0.16), subscriber→buyer +8.9%, subscription→charge +9.8%.
Funnels (v2): iOS members→Try Show 86.98%, →View 87.51%, members→Purchase Finish (AD Interstitial) 0.11%; Android 83.38% / 84.06% / 0.10%. Tour funnel unchanged between arms (activation-neutrality check).
Forecast (per day): Android control $7,240 → v2 $8,620 (+$1,380); iOS control $22,861 → v2 $23,470 (+$609).

## Decision
- Iteration 2 conclusion: "roll outed Android test variation" — the Android test variation was rolled out.
- iOS: not rolled out. Next steps: extend the iOS test duration and compute total revenue impact — verify ad/video interstitial revenue is fully captured in ARPU, compare eCPM and fill vs the standard interstitial, re-check ARPU/cancels/refunds with higher power; cohort follow-up on purchasers (track 14d/1m cancellations and refunds by cohort post-exposure) before full rollout.

## Lessons & Insights
- The video works where it replaces "nothing": Android has no ad interstitials, so the surface is purely incremental — consistent significant ARPU +17–19% across both iterations, with funnel conversions up.
- On iOS the same surface competes with real ad revenue and other paywall entry points: iteration 1 showed a significant -24.7% ARPU in the without-interstitial-accesses segment (cannibalization), and iteration 2 totals stayed non-significant (+2.66%, p=0.43).
- Retention cost appears when the video replaces a guaranteed daily ad impression (iteration 2 Android: -0.9%…-3.3%, all significant) rather than only filling ad fails (iteration 1 Android v2 retention neutral).
- Creative matters: "songs by chords" (variation 3) was strictly worse — more trials (+12.8% share) but worse trial-to-paid (subscriber→buyer -10.8%, subscription→charge -12.0%), significant Android retention decline, and lower viewing quality.
- Technical fill is a real bottleneck: 28–50% of video try-shows timed out (3s loader); pre-loading at app launch + on-device caching was the iteration-2 fix.
- Video click-through to the paywall is tiny (Banner Purchase Click 0.49–1.03% of Banner Upgrade View; members→purchase 0.07–0.12%) — the ARPU effect comes from massive reach, not per-impression conversion.
