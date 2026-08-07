# GT-RH-01 — UG App: winback – interstitials for former subscribers

## Identity
- pageId: 714409638 — "[2025-08-01] UG App: winback – add interstitials for former subscribers [2025-10-17]"
- URL: https://alice.mu.se/pages/viewpage.action?pageId=714409638
- AB experiment ids: 6461 (iteration 1; AB registry run 2025-09-09..2025-09-16; the page's Results block is titled "Iteration #1 - #6461") and 6644 (relaunch — registry "[UG Monetization] UG App: winback interstitials for former subscribers (relaunch)", 2025-10-13..2025-10-17; the page contains NO separate results block for it). Exposure/start event: App Experiment Start (item_id = experiment id).
- Jira: UMN-9259
- Dates: project page dates 2025-08-01 .. 2025-10-17; iteration #1 ran 8 days (UGT_IOS only).
- Arms: control (normal ads) vs variation 2 (winback splash: 14-day re-trial offer `com.ultimateguitar.tabs.plus.inst.1year2` + `14DAYSFREE`, shown instead of the ad on first tab open per day + on ad-load failure). Audience: users with previously active but currently inactive subscriptions. iOS only (Android was sized in the design but not run).
- Segments configured for #6461: Total {'pro_rights': 'all'}; Without interstitial accesses {'pro_rights': 'all', 'funnel_source_exclude': ['AD Winback Interstitial']}; Interstitial accesses only (funnel_source_include, "for conversion research purposes"); Interstitials Funnel: members > Splash View > [Splash Close; Banner Purchase Click > Purchase Process Finish], all with value 'AD Winback Interstitial'.

## Actual outcome
Iteration #1 (#6461), UGT_IOS. Sample: control 21,932 / variation 2 22,121 (8 days; the Design-vs-Reality table's design column lists 134,015 per arm, while the design section computed 268,030 per variation / 10 days).

UGT_IOS, Total segment — Monetization Stats:

| Arm | Members | Subscribers | Accesses | Instants | Trials | Ex trials | Charged trials | Buyers | Charges | Revenue | Cancels 14d | Refunds 14d |
|---|---|---|---|---|---|---|---|---|---|---|---|
| control | 21,932 | 494 | 515 | 273 | 90 | 152 | 16 | 369 | 373 | $8,241 | 26 | 14 |
| variation 2 | 22,121 | 1,350 | 1,379 | 278 | 949 | 152 | 159 | 513 | 521 | $11,873 | 79 | 27 |
| diff, % | +0.86% | +170% | +170% | +1.8% | +950% | 0% | +890% | +39% | +40% | +44% | +200% | +93% |

UGT_IOS, Total segment — Monetization Metrics (with p-values):
- ARPU: $0.376 → $0.537 (+42.8%, p=0.00)
- AOV: $22.1 → $22.8 (+3.14%, p=0.36); ARPPU: $22.3 → $23.1 (+3.63%, p=0.29)
- Access cr: 2.25% → 6.1% (+171%, p=0.00; the Decision text cites +170.9%)
- Charge cr: 1.68% → 2.32% (+37.8%, p=0.00)
- Trials share: 17.5% → 68.8% (+294%, p=0.00; Decision cites +293.8%)
- Trial → charge: 17.8% → 16.8% (−5.76%, p=0.81)
- Charge → 14d cancel: 6.97% → 15.2% (+118%, p=0.00; Decision cites +117.5%); the Decision bullet also cites charge → 1m cancel +69.0%
- Charge → 14d refund: 3.75% → 5.18% (+38.1%, p=0.30)

"Without interstitial accesses" segment (variation 2 vs control): subscribers 472 vs 484 control-row (−2.5%), accesses 500 vs 504 (−0.79%), revenue $7,754 (−5.9%); metrics ARPU $0.351 vs $0.376 (−6.71%, p=0.40); access cr 2.13% vs 2.21% (−3.31%, p=0.60); charge cr 1.6% vs 1.68% (−5.15%, p=0.47); charge→14d cancel 6.93% vs 6.97% (−0.65%, p=0.98) — "those without interstitial access do not move". (Note: in this segment the control row differs slightly from Total — 484 subscribers / 504 accesses / 79 trials.)

"Interstitial accesses only" research segment: control had 11 subscribers/accesses (all trials, 0 charges, access cr 0.0502%); variation 2: 878 subscribers, 879 accesses, 860 trials, 141 charged trials, 160 buyers/charges, $4,118 revenue, 54 cancels 14d, 11 refunds 14d; metrics: ARPU $0.186; AOV/ARPPU $25.7; access cr 3.97%; charge cr 0.723%; trials share 97.8%; trial→charge 16.4%; charge→14d cancel 33.8%; charge→14d refund 6.88%.

Ad Stats: impressions 333,397 → 310,625 (−22,772, −6.8%); Total CPM+CPC revenue $1,918 → $1,771 (−$147, −7.7%).

Retention Metrics: ret1d 24.4% → 24.9% (+1.93%, p=0.25); ret7d 63.1% → 63.2% (+0.158%, p=0.83); ret14d 75.4% → 74.7% (−0.875%, p=0.11) — unchanged. (Retention Stats row lists variation-2 members as 22,119 vs 22,121 elsewhere — minor page inconsistency.)

Tab View Metrics: tab views per user 9.14 → 10.8 (+18.5%, p=0.00); 60s/120s/180s per user +2.94%/+3.42%/+3.39% (p=0.027/0.010/0.014); 300s/600s per user +2.66%/+2.19% (p=0.07/0.32); tab view 60s share 90.8% → 90.2% (−0.67%, p=0.030).

Interstitials Funnel (variation 2): members → Splash View 22,063 of 22,121 = 99.74%; Splash View → Splash Close 18,552 = 84.09%; Splash View → Banner Purchase Click 1,216 = 5.51%; click → Purchase Process Finish 915 = 75.25%; members → Purchase Finish 4.14%. Control: all zeros.

Forecast (per day):

| Variation | App Experiment Start | Accesses | Charges | Revenue, $ | Ad revenue (CPM+CPC), $ | Winback access CR | Winback charge CR |
|---|---|---|---|---|---|---|---|
| control | 6,295 | 147 | 107 | $2,365 | $551 | — | — |
| variation 2 | 6,295 | 392 | 148 | $3,379 | $504 | 3.9% | 0.7% |
| diff | 0 | +245 | +41 | +$1,014 | −$47 | — | — |

Plan vs fact: the design modeled iOS ARPU +$0.042 (~+6%) and goal-metric lift +6.0%; actual iOS ARPU came in at +42.8% (p=0.00) and access CR +171% — an order of magnitude above plan, at the cost of +69–118% early cancellations.

## Uncertainty & maturity
- SRM: no mismatch — 21,932 / 22,121 (+0.86%), "A/B balance is maintained" checked complete.
- Design vs Reality: "duration of exp ≥ design" is marked INCOMPLETE — ran 8 days vs 10 designed; the check table's design sample column (134,015 per arm) contradicts the design section's 268,030 per variation. "No visible bugs" and "No external effects" complete.
- Platform coverage: iOS only; the Android design column (baseline 2.02%, +13.9% modeled) was never tested.
- Data-quality flag: Next steps say "preferably wait to fix unified_id bug" — a known user-identity issue at the time; AB 6644 is the registry relaunch (2025-10-13..2025-10-17) and the page has no results block for it, so the published numbers are iteration #1 (#6461) only.
- Pending-trial maturity: not documented on the page; 14d cancel/refund are readable, but long-horizon revenue quality (given +69–118% early cancels and 68.8% trial share) is explicitly an open question.
- Effect concentration is verified in-page: the "without interstitial accesses" slice is flat (all p ≥ 0.40), so the Total lift is attributable to interstitial viewers.

## Final decision
Decision status: Green SUCCESS. Exact wording:
- "Can roll out test variation"
- "On iOS, the promo splash with a 14-day re-trial for previously active but currently inactive subscribers meaningfully increases monetization and engagement: ARPU is up ~43%, access and charge conversion rates are higher, and users consume more tabs."
- "The effect is concentrated among users who actually see the interstitial; those without interstitial access do not move."
- "However, early cancellations jump sharply (+69% to +118%). This pattern is consistent with the offer attracting many low-intent re-trialists who cancel quickly. Retention is unchanged."
- Next steps: "preferably wait to fix unified_id bug"
The registry additionally records the #6644 relaunch closing 2025-10-17. The Post-rollout analysis section of the page is an empty template.

## Confirmed product lessons
- Deliberately productizing an accidental discovery worked: the ex-subscriber re-trial appetite first surfaced through a segmentation bug in "[2025-04-11] UG App: paywall – offer instead of ad interstitials" converted into a large significant ARPU win (+42.8%, p=0.00) when targeted on purpose.
- The effect is cleanly incremental: entirely concentrated in users who saw the interstitial (non-viewers flat, p≥0.40), with modest ad-revenue cannibalization (−7.7% ad revenue / −$47 per day vs +$1,014 per day product revenue in the forecast).
- Re-trials attract low-intent users: trial share ballooned to 68.8% of subscriptions; 14d cancels more than doubled (+118%, p=0.00); interstitial-sourced charges cancel at 33.8% within 14 days — long-horizon revenue quality needs monitoring.
- In-app interstitial delivery solves the reach problem that killed the push-based winback attempts (50–72% push delivery, <80% splash reach in the 2024–2025 churn-winback tests): here 99.74% of the target segment saw the splash.
- Offer strength vs delivery context: a 6-month trial via push after cancel was not enough (ARPU +22%, p=0.54, n.s.), while a 14-day re-trial delivered in-app at a natural ad-slot moment produced +42.8% ARPU (p=0.00) — context and reach beat raw generosity.
- Engagement moved up alongside monetization (tab views per user +18.5%, p=0.00); retention was unchanged.

## Sources
- Page: https://alice.mu.se/pages/viewpage.action?pageId=714409638 ("[2025-08-01] UG App: winback – add interstitials for former subscribers [2025-10-17]"), snapshot output/confluence/flow577_verify/714409638/confluence_714409638.txt (+ .storage.xhtml for table structure).
- Sections used: "Research and Context" (prior winback experiments, ad-pressure research, A/B test model), "Hypothesis", "Experiment design template" (#6461), "Description of the Solution & Mockups → Solution", "Analytics" (#6461 config), "Results → Iteration #1 - #6461" (Design vs Reality check, Decision, Forecast (per day), Significance analysis: Monetization/AD/Retention/Long Tab View Stats, Monetization/Retention/Tab View Metrics, Interstitials Funnel).
- AB registry run dates for 6461 (2025-09-09..2025-09-16) and 6644 relaunch (2025-10-13..2025-10-17): from the verified results card KS-05 (`KS-05_winback-interstitials-former-subscribers.md`), which cites the AB registry; these dates are not on the Confluence page itself.
- Cross-checked against inventory record T1-05 (output/flow577_revenue_inventory/inventory.yaml): decision rolled-out, SRM ok, result class significant-positive.
