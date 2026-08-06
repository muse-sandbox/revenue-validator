# UG iOS: Interstitial - Swap into Landing

## Identity
- Experiment ID(s): AB 4845
- Aliases: registry name "[UG Монетизация] UG iOS: Interstitial - Swap into Landing"; Confluence page title "[2024-04-24] UG iOS: Interstitial - Swap into Landing [2024-08-10]"; Jira UMN-5306
- Source: https://alice.mu.se/pages/viewpage.action?pageId=459868984
- Dates: 2024-04-24..2024-08-10 (AB registry run window for 4845: 2024-07-15..2024-07-20)
- Related experiments: This is the first experiment of the "replace ad interstitials with our own monetization surface" line. The team explicitly planned to work with the first step of the interstitial funnel in later projects (see KS-02 "offer instead of ad interstitials", which cites this experiment's poor results as its research foundation).

## Context & Research (pre-launch)
- Project goal: "we want to convert user into trials and subscriptions with new mechanics".
- Foundation: house ("HL") ads were the "default" fallback state at the time, so the team considered swapping them into additional monetization sources.
- Daily revenue of interstitials was approximately $1,400; there were no interstitials on Android at all.
- Pre-launch A/B model (from the page):

| Metric | iOS A | iOS B | diff | Android A (approx) | Android B (approx) | diff |
|---|---|---|---|---|---|---|
| Interstitial Show (event = admob_shown) | 105,451 | 105,451 | 0 | 65,831 | 65,831 | 0 |
| Accesses | 437 | 481 | 44 | 200 | 230 | 30 |
| Interstitial → Access, % | 0.0041 | 0.0046 | 10% | 0.0030 | 0.0035 | 15% |
| Charges | 290 | 319 | 29 | 110 | 127 | 17 |
| Revenue, $ | $6,663 | $7,329 | $666 | $2,852 | $3,280 | $428 |
| ARPPU, $ | $22.98 | $22.98 | $0.00 | $26 | $26 | $0.00 |
| ARPU, $ | $0.0632 | $0.0695 | 10% | $0.0433 | $0.0498 | 15% |

## Hypothesis
"If we swap HL ads with new landing, it will help us earn additional 10% money, because landing can show all the benefits of subscription."

## Mechanics
- Placement: interstitial slot on tab entry — when the ad auction ends in a "no-fill" state (ex-HL-ad slot), the app instantly shows a scrollable subscription landing instead.
- Trigger logic (as documented):
  1. User goes to a tab; there is a trigger for showing an interstitial.
  2. If the "no-fill" state wins: show the Landing (close button is instant), then note that it was shown today.
  3. If any kind of ad won: show the winner's ad.
  4. If "no-fill" wins again the same day: do NOT show the landing again that day — just let the user pass to the tab.
- Net effect: landing shown once per day, only for the first "winning of no-fill state", muted for the rest of the day, shown again the next day with the same logic.
- Timing: the close button appears immediately (instant) for this launch.
- Frequency (interstitial slot itself): max 5 times per day, with a 180 sec gap between shows; the logic renews every day at 23:59.
- Audience segment: only users without any current subscription or active trial.
- Platforms: iOS only ("Applies only for iOS").
- SKUs / offers shown: no special SKU documented. The landing is scrollable, has a button that scrolls the landing to the paywall at the bottom of the screen; content sections per the scroll-tracking spec: "Official Tabs" (first screen), "Practice Mode" (second), "Smart Scroll" (third), "Choose your plan" (fourth), "Start now" (end of banner).

## Experiment design
- Arms: A (control — existing no-fill/HL behavior) vs B (landing instead of no-fill).
- Primary metric: Interstitial → Access, %.
- A/B test plan table:

| Parameter | iOS | Android |
|---|---|---|
| Base value of the metric | 0.0041 | 0.0030 |
| Lift, % | 10% | 15% |
| Minimal detectable effect | 0.0063 | 0.0080 |
| Power | 0.8 | 0.8 |
| p-value | 0.05 | 0.05 |
| Sample size (for all the variations) | 843,608 | 526,648 |
| Planned duration, days | 8 | 8 |

- (Android was modeled but the experiment shipped iOS-only.)
- Analytics spec:
  - Start event: "Interstitial Banner View" — user sees the interstitial "no-fill" banner; must work for both test and control.
  - Splash View / Splash Close with value 'AD Interstitial'.
  - Banner Upgrade View — value 'AD Interstitial', type 'button' (user clicks "Start now") or 'scroll' (user scrolls to the banner themselves).
  - Banner Upgrade Close — all params from Banner Upgrade View; sent when the user closes the paywall banner; provided for all banners in the app regardless of experiment membership.
  - Interstitial Banner Scroll — value = percent of scroll (0,10,…,100), type = the section header visible (Official Tabs / Practice Mode / Smart Scroll / Choose your plan / Start now); sent every 10% or on reaching the next header, along with Banner Upgrade View (type = scroll).
  - Purchase funnel with new source value 'AD Interstitial': Banner Purchase Click, Purchase Process Start, Purchase Process Click, Purchase Process Canceled, Purchase Process Finish, Banner Free Trial Toggle.

## Execution notes
- Applied only to iOS; the close button was instant for this launch.
- Landing shown only on the first no-fill win of the day (one impression per day cap on the new surface).
- No config problems, relaunches, or iterations documented on the page.

## Results
Exposure event: Interstitial Banner View. Verdict on the page: FAIL (#4845).

- Headline: "The obvious thing about its results is simple: nothing changes at all. We didn't get any results with this experiment, there is simply nothing at all."
- "no changes since we affect only a very small portion of users"
- Only 6% of users with access after the interstitial came from its source.

Forecast (per day):

| Variation | Interstitial Banner View | Accesses | Charges | Revenue |
|---|---|---|---|---|
| control | 800 | 15 | 9 | $183 |
| variation 2 | 800 | 15 | 9 | $164 |
| diff | 0 | 0 | 0 | -$19 |

Monetization stats (cumulative):

| Variation | members | subscribers | accesses | instants | trials | charged trials | buyers | charges | revenue |
|---|---|---|---|---|---|---|---|---|---|
| control | 3,283 | 63 | 63 | 32 | 31 | 6 | 38 | 38 | $753 |
| variation 2 | 3,250 | 59 | 61 | 31 | 28 | 5 | 36 | 37 | $667 |

Monetization metrics:

| Metric | control | variation 2 | diff, % | p-value |
|---|---|---|---|---|
| ARPU | $0.23 | $0.21 | -10.48% | 0.67 |
| AOV | $19.82 | $18.04 | -8.99% | 0.48 |
| ARPPU | $19.82 | $18.54 | -6.46% | 0.61 |
| access CR, % | 1.92% | 1.82% | -5.40% | 0.76 |
| charge CR, % | 1.16% | 1.11% | -4.30% | 0.85 |
| trial → charge, % | 19.35% | 17.86% | -7.74% | 0.88 |
| accesses per subscriber | 1.00 | 1.03 | +3.39% | 0.33 |
| charge → 14d cancel, % | 10.53% | 0.00% | -100% | 0.03 |

Product stats and metrics:

| Metric | control | variation 2 | diff, % | p-value |
|---|---|---|---|---|
| members | 3,283 | 3,250 | — | — |
| retention 1d (count) | 824 | 756 | — | — |
| retention 7d (count) | 1,105 | 1,032 | — | — |
| retention 1d, % | 25.10% | 23.26% | -7.32% | 0.083 |
| retention 7d, % | 33.66% | 31.75% | -5.66% | 0.101 |

Accesses distribution by product source:

| Source | variation 1 | variation 2 | diff |
|---|---|---|---|
| Other | 62 | 54 | -8 |
| AD Interstitial | — | 4 (6%) | +4 |
| Totals | 62 | 58 | -4 |

- Significance/maturity caveats: virtually nothing is significant except the 14d-cancel artifact (p=0.03) on tiny charge counts (37–38 charges per arm); the affected population was very small, so all monetization diffs are noise-level.

## Decision
- No rollout: "average accesses per day are so insignificant, there is no reason in rollout this variation".
- The experiment was closed as fail: "Also we are not planning future iterations with interstitial, so we close experiment as fail."
- The landing asset was earmarked for reuse: "we can re-use this landing in future experiments with paywalls."

## Lessons & Insights
- Reach is the binding constraint: replacing only the no-fill state, once per day, touches so few users that no downstream metric can move (4 accesses from the new source over the whole experiment; 6% of interstitial-touched accesses).
- Recorded next-step idea: "we can work with first step of the interstitial funnel — for example show it for same users we show ad, but only once a week as an extra interstitial" — i.e., move from filling no-fill leftovers to actively substituting/adding impressions. This idea became the backbone of the later interstitial projects (KS-02 and onwards).
- The scrollable landing format itself was judged reusable for future paywall experiments even though this test failed.
