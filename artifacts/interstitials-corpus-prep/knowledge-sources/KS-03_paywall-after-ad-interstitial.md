# UG iOS: paywall – paywall after ad interstitial

## Identity
- Experiment ID(s): AB 6335
- Aliases: registry name "[UG Monetization] UG iOS: paywall – paywall after ad interstitial" (registry run 2025-07-11..2025-07-17); Confluence page title "[2025-07-07] UG iOS: paywall – paywall after ad interstitial [2025-08-12]"; Jira UMN-8971
- Source: https://alice.mu.se/pages/viewpage.action?pageId=707134897
- Dates: 2025-07-07..2025-08-12
- Related experiments: sibling of the "replace interstitial ads with our banners and videos" project line — the decision explicitly redirects effort there (KS-02/KS-06 offer-instead-of-ads, KS-04 monetization video). KS-05 (winback interstitials) cites this experiment as prior research ("advertising instead of interstitials, which have already proven themselves well").

## Context & Research (pre-launch)
- Goal: "Use ads in the app as a way to attract people to subscribe and increase the conversion to access".
- Foundation: UG did not specifically advertise the subscription as being ad-free — all entry points were about features or premium content. UG reached ~100k unique interstitial viewers a day on iOS, a potentially good spot for selling subscriptions. Interstitial ads existed only in the iOS app.
- Research references: a similar monetization has been implemented at Duolingo (mockups reference "Duo ref" screens). Ads and ad load can also be a good tool to "press" on the cold and ex-premium audience (e.g., YouTube increases the ad load on "cold old" users). Adding a paywall scenario creates a purchase point from ads, enabling future ad-load experiments.
- A/B test model (iOS):

| Metric | A | B | diff |
|---|---|---|---|
| Interstitials (by admob_shown) | 100,643 | 100,643 | — |
| Accesses | 587 | 646 | 59 |
| Charges | 336 | 370 | 34 |
| Interstitial → Access, % | 0.58% | 0.64% | 10% |
| Revenue, $ | $8,625 | $9,488 | $863 |
| ARPPU, $ | $25.65 | $25.65 | — |
| ARPU, $ | $0.086 | $0.094 | $0.008 |

## Hypothesis
"If we show a paywall after the ads, focusing on an ad-free experience, then the conversion to access will increase by 10%. This is because we'll make the paywall more noticeable and communicate with the audience that an ad-free experience is available to them."

## Mechanics
- Placement: a new payment flow shown AFTER every successful display of an advertising interstitial (first version copies the Duolingo scenario).
- Flow for variation B, after the interstitial:
  1. Pre-paywall with a description of the ad-free experience; includes a "no, thanks" button that exits the payment scenario.
  2. Pre-paywall with a benefits compare table containing: 1.4+ million tabs & chords; Ads-free experience; High quality Official tabs; Practice mode; Autoplay & autoscroll; Transpose. Designed as "a similar table but without the option to close the screen", CTA button "Continue".
  3. Standard pro-paywall.
- Trigger: every successful ad interstitial impression. If the user declines/closes the paywall or pre-paywall (or buys something), they are taken to the tab page they were trying to access.
- Timing/Frequency: after every ad; the first pre-paywall is skippable ("no, thanks"), the compare-table screen has no close.
- Audience segment: all free users without Pro rights, INCLUDING ex-premium. Plan content follows standard logic (general check for any paywall on trial/introductory eligibility and transaction type purchase/upgrade).
- Platforms: UGT_IOS only.
- SKUs / offers shown: standard pro-paywall with annual Pro+ $39.99 / year (instant + trial) and $9.99 / month instant.
- Design rationale recorded: "To check the potential, we can go two ways: make pre-paywalls impenetrable or show them after every ad, but with the option to leave after the first pre-paywall (doing both at once seems too harsh…). Therefore, we'll first test the impact of the number of paywall displays with the option to skip them, and then we'll work on the funnel itself."

## Experiment design
- Arms: control (ads only) vs variation 2 (ads + post-ad payment flow).
- Primary metric: Interstitial → Access, %.

| Parameter | value |
|---|---|
| Baseline | 0.58% |
| Lift, % | 10% |
| MDE | 0.0075 |
| Power | 0.8 |
| Alpha | 0.05 |
| Sample size (per variation) | 603,858 |
| Duration (days) | 6 |
| Seasonality | took whole week in calculations |

- Exposure event: admob_shown (existing event on iOS; noted "add for Android"; sent for both variations).
- New events: Pre-paywall Adfree View, Pre-paywall Adfree Close, Pre-paywall Compare View (all value = Interstitial); existing banner funnel with new value Interstitial: Banner Upgrade View, Banner Purchase Click, Purchase Process Start, Purchase Process Finish, Purchase Process Canceled.
- Calculation config (#6335):
  - Total: {'pro_rights': 'Free'}
  - Splash accesses only: {'pro_rights': 'Free', 'custom_sub_having': "funnel_source like '%Splash%'", 'monetization_only': 1}
  - Interstitial funnel: members > Pre-paywall Adfree View > [Adfree Close, Compare View > Banner Upgrade View > Banner Purchase Click > Purchase Process Finish] (all with value='Interstitial').

## Execution notes
- Ran 7 days (design 6); duration and A/B balance checks complete; no visible bugs throughout the experiment; no external effects.
- Actual activated sample: 35,411 control / 34,913 variation 2 (the design's 603,858/arm counted a different unit — interstitial audience — than activated members).
- No relaunches or config incidents documented.

## Results
Exposure event: admob_shown. Verdict: FAIL.

Headline results:
- "We expected to achieve 10% growth in subscriptions through the new source, but ultimately the difference between variations was around 0."
- "In the new scenario, conversion to subscription was only 0.07% of those who saw the new splash."
- "As a result, the share of subscriptions from the new source accounted for 3% of all subscriptions, but at the same time it cannibalized other sources from the tab page."
- "In the new scenario, 96% of users leave at the very first pre-paywall, indicating there are problems with paywall reach."

Interstitial funnel (variation 2, 34,913 members):

| Step | count | step conversion |
|---|---|---|
| Pre-paywall Adfree View | 33,608 | 96.26% of members |
| Pre-paywall Adfree Close | 32,486 | 96.66% of views (drop-off) |
| Pre-paywall Compare View | 1,005 | 2.99% of views |
| Banner Upgrade View | 876 | 87.16% |
| Banner Purchase Click | 77 | 8.79% |
| Purchase Process Finish | 26 | 33.77% |
| members → Purchase Process Finish | — | 0.07% |

(Control: all funnel steps 0.)

Monetization stats (Total segment):

| Variation | Members | Subscribers | Accesses | Instants | Trials | Ex trials | Charged trials | Buyers | Charges | Revenue | Cancels 14d | Refunds 14d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| control | 35,411 | 755 | 793 | 261 | 503 | 29 | 127 | 408 | 417 | $9,159 | 90 | 20 |
| variation 2 | 34,913 | 745 | 802 | 276 | 495 | 31 | 146 | 446 | 453 | $9,970 | 96 | 24 |
| diff, % | -1.4% | -1.3% | +1.1% | +5.7% | -1.6% | +6.9% | +15% | +9.3% | +8.6% | +8.9% | +6.7% | +20% |

Monetization metrics (Total):

| Metric | control | var 2 | diff, % | p |
|---|---|---|---|---|
| ARPU | $0.259 | $0.286 | +10.4% | 0.19 |
| AOV | $22 | $22 | +0.209% | 0.96 |
| ARPPU | $22.4 | $22.4 | -0.415% | 0.90 |
| Access CR | 2.13% | 2.13% | +0.083% | 0.99 |
| Charge CR | 1.15% | 1.28% | +10.9% | 0.13 |
| Trials share | 63.4% | 61.7% | -2.69% | 0.48 |
| Trial → charge | 25.2% | 29.5% | +16.8% | 0.13 |
| Charge → 14d cancel | 21.6% | 21.2% | -1.81% | 0.89 |
| Charge → 14d refund | 4.8% | 5.3% | +10.5% | 0.74 |

Splash-accesses-only segment: 52 vs 48–49 subscribers/charges per arm; ARPU $0.0265 → $0.0295 (+11.5%, p=0.62); AOV +16.7% (p=0.16); ARPPU $18 → $21.5 (+19.1%, p=0.030); access CR -6.38% (p=0.74); 14d cancel -51.8% (p=0.12).

Retention metrics: 1d 23.5% → 23% (-2.16%, p=0.11); 7d 52.8% → 52.3% (-0.976%, p=0.17); 14d 61.6% → 61.5% (-0.196%, p=0.74).

Tab view metrics: Tab View per user 12.1 → 14.5 (+20.2%, p=0.00); Tab View 60s per user 4.83 → 4.72 (-2.32%, p=0.048); shares 60s–300s down -0.41%…-1.1% (n.s.).

Forecast (per day):

| Variation | admob_shown | Accesses | Charges | Revenue, $ |
|---|---|---|---|---|
| control | 72,907 | 1,632 | 858 | $18,858 |
| variation 2 | 72,907 | 1,674 | 945 | $20,821 |
| diff | 0 | 42 | 87 | $1,963 |

(Forecast not realized as significant; Total ARPU p=0.19.)

## Decision
- Not rolling out: "We're not rolling out, as we were unable to achieve the expected increase in access."
- Root cause: "The main problem is the drop-off from the first pre-paywall in the new scenario, resulting in a very low conversion rate of the source (only 0.07%)."
- Considered and rejected: "We could try to make the entire funnel leak-proof and lead all users to the paywall, but most likely, we won't get any additional access there, as the source cannibalizes other entry points on the tab."
- "We won't continue with this hypothesis. We'll focus on the project that involves replacing interstitial ads with our banners and videos."

## Lessons & Insights
- "Longer funnel with pre paywall screen works worse than just banner" — the team's core conclusion. Each extra step multiplies drop-off; the very first (skippable) pre-paywall lost 96% of viewers.
- Post-ad placement inherits an annoyed context: users who just sat through an ad overwhelmingly dismiss a follow-up sales screen.
- Even when a new source generates subscriptions (3% of total), it can be net-zero because it cannibalizes other tab-page entry points.
- Recorded next-step idea (not pursued in this project): "we can make all pre-paywalls in the new scenario unskippable. This will solve the problem of high churn and low paywall visibility."
- The pivot decision from this experiment shaped the roadmap: effort moved to replacing ad interstitials with own banners/videos rather than appending paywalls after ads.
