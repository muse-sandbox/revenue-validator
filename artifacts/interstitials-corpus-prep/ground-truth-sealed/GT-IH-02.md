# GT-IH-02 — UG App: winback - final interstitial offer

## Identity
- pageId: 788612067 — "[2026-05-04] UG App: winback - final interstitial offer [2026-07-30]" (snapshot v29, 2026-06-30)
- URL: https://alice.mu.se/spaces/CRO/pages/788612067
- AB experiment id: 7487 (single iteration; no relaunch). Run period per page Insights: 2026-05-22 → 2026-06-12 (~21 days); AB registry matches (2026-05-22..2026-06-12). Clients: UGT_IOS, UGT_ANDROID (v7.3.9). Exposure event: App Experiment Start.
- Jira: UMN-11515
- Dates: project page dates 2026-05-04 .. 2026-07-30.
- Arms: Variation 1 = control (users who exhausted the winback window fall back to regular ad monetization); Variation 2 = test (one-time final interstitial with a promo-code paywall at $19.99). Target: former subscribers who previously had Pro, no active subscription; final interstitial shown once, only after the winback interstitial was viewed and no sooner than the following day.
- Segments: Total, and Winbacks (funnel_source in ('AD Winback Interstitial','AD Final Interstitial')); both share the same members, so Total − Winbacks is a clean "everything except the winback interstitial" split.

## Actual outcome
Sample sizes: iOS 9,933 control / 9,753 variation 2; Android 3,566 / 3,602; 21 days both platforms.

UGT_IOS Total: ARPU $0.41 → $0.45 (+9.30%, p=0.40); AOV $21.41 → $18.33 (−14.41%, p=0.001); ARPPU $21.53 → $18.40 (−14.51%, p=0.000); members→buyers 1.89% → 2.42% (+27.85%, p=0.011); charges per user +27.71% (p=0.011); trials share 34.10% → 16.67% (−51.12%, p=0.000); trial→charge 19.10% → 15.22% (−20.33%, p=0.56); churn 14d 21.69% → 22.78% (p=0.79); refund 14d 5.82% → 4.22% (p=0.46). Stats: revenue $4,047 → $4,343; buyers 188 → 236; instant accesses 108 → 161; trials 89 → 46.

UGT_IOS Winbacks: ARPU $0.043 → $0.15 (+241.15%, p=0.000); members→buyers 0.21% → 0.98% (+365.58%, p=0.000); members→subscribers 0.81% → 1.26% (+56.59%, p=0.002); AOV/ARPPU $20.21 → $14.81 (−26.73%, p=0.013); trials share 90.00% → 26.61% (−70.43%, p=0.000); trial→charge 18.06% → 15.15% (−16.08%, p=0.71). Stats: buyers 21 → 96; instant accesses 8 → 91; trials 72 → 33; revenue $424 → $1,422.

UGT_ANDROID Total: ARPU $0.40 → $0.50 (+26.54%, p=0.22); members→subscribers 2.16% → 3.05% (+41.43%, p=0.017); members→buyers 1.49% → 2.19% (+47.57%, p=0.026); AOV −14.25% (p=0.08); trials share 45.45% → 30.63% (−32.61%, p=0.039); trial→charge 31.43% → 5.88% (−81.28%, p=0.004); churn 14d 5.66% → 11.39% (+101.27%, p=0.23). Stats: revenue $1,419 → $1,814; buyers 53 → 79.

UGT_ANDROID Winbacks: ARPU $0.14 → $0.19 (+34.00%, p=0.33); members→buyers 0.48% → 0.97% (+103.82%, p=0.013); members→subscribers +55.93% (p=0.025); AOV/ARPPU $29.10 → $19.13 (−34.26%, p=0.000); trials share 80.00% → 47.62% (−40.48%, p=0.000); trial→charge 28.12% → 6.67% (−76.30%, p=0.019); churn 14d 0.00% → 14.29% (p=0.016 — flagged as preliminary, see below). Stats: buyers 17 → 35; instant accesses 5 → 32; revenue $495 → $669.

Retention (guardrail, both flat): iOS app retention 1d/7d/14d 28.08/69.32/81.41% → 27.39/68.95/81.29% (p=0.28/0.57/0.83); Android 29.28/72.55/84.30% → 28.73/72.40/83.43% (p=0.61/0.89/0.32).

First-show conversion (Insights, confirmatory): member→buyer on the entry interstitial — AD Final (test) vs AD Winback (control): iOS 0.14% → 0.93% (+562%, p<0.001), Android 0.37% → 0.78% (+113%, p=0.02). member→subscription not significant (iOS p=0.26, Android p=0.20); composition opposite — winback interstitial opens almost only trials (iOS 76/78, Android 37/38), final interstitial is 100% immediate payment.

Cannibalization (Total − Winbacks split): iOS winback buyers 21 → 96 (+75) but non-winback buyers 167 → 140 (−27), non-winback revenue $3,623 → $2,921 (−$702), net total +$296 — "mild diffuse dilution" spread across many organic/feature sources (transpose, Smartscroll, autoscroll, Official Tabs Search, …), not concentrated cannibalization of one offer. Android: winback buyers 17 → 35 (+18), non-winback buyers 36 → 44 (+8), non-winback revenue +$221, net +$395 — consistent with no cannibalization but underpowered.

Forecast (per day): iOS control 3,989 Experiment Start / 105 subs / 76 charges / $1,625 vs var2 113 / 97 / $1,777 → diff +8 subs / +21 charges / +$151. Android control 1,017 / 22 / 15 / $405 vs var2 31 / 22 / $512 → diff +9 / +7 / +$107.

## Uncertainty & maturity
- Maturity (updated read): all trials have matured — pending trials = 0 in every branch — so trial→charge is final; ARPU / Revenue / Buyers / member→subscriber/buyer conversions are mature. churn 14d / refund 14d remain preliminary: 14d pending-charge share still above 5% on control branches (iOS Winbacks ctrl 52%, Android Total ctrl 19%, Android Winbacks ctrl 47%, iOS Total ctrl 6.9%; all test branches ≤ 6%). E.g. "Android Winbacks churn 0% → 14.3% (p=0.016) must not be read as final."
- Change since the pre-maturity read: as control trials matured into charges, control buyers/revenue rose and the test's relative lift shrank — "the total-account ARPU/Revenue lift is no longer statistically significant on either platform" (iOS Total ARPU +9.3% p=0.40; Android +26.5% p=0.22). The conversion win on the targeted winback segment holds.
- Resolved artifact: the earlier "iOS Winbacks trial→charge −100%" was a maturity artifact; it now reads 18.1% → 15.2% (p=0.71), "no real degradation".
- No SRM: iOS 9,933 / 9,753, Android 3,566 / 3,602 — balance is fine. Design vs Reality: design values are 0 (no formal design); all checks (bugs, external effects, duration ≥ design, A/B balance) marked complete.
- Exploratory caveat: the iOS non-winback funnel_source join "over-counts absolutes vs the package totals, so only the relative pattern is used, not absolute numbers."

## Final decision
Decision status: Green — success. Exact wording:
- "Can roll out variation 2 (the one-time $19.99 final interstitial) on both UGT_ANDROID and UGT_IOS, with active monitoring on iOS."
- "no significant increase on arpu but only due to small segments"
- "Android — clear win, roll out. No cannibalization."
- "iOS — roll out, but watch full-price cannibalization."
- "Trade-off is by design. The offer converts trials into immediate payment, lowering AOV/ARPPU (iOS AOV −14.4%, p=0.001) — expected, since $19.99 < the ~$40/yr plan. It does not affect the standard winback CR (shown only after the winback window is exhausted)."
Next steps: roll out variation 2 on Android at 100% ("clean incremental win"); roll out on iOS with a post-rollout watch on non-winback / full-price conversion (Total − Winbacks) to confirm the diffuse dilution stays bounded and the net stays positive; iterate iOS targeting to cut the dilution (tighten eligibility — exclude users who recently viewed a full-price paywall or are mid-trial); recheck churn 14d / refund 14d once control 14d charge windows close.

## Confirmed product lessons
- "The $19.99 offer revives a previously dead segment": the exhausted-winback segment (zero-converting after 2–5 winback impressions) significantly converts under a one-time deep-discount instant offer on both platforms (iOS member→buyers +365.6% p=0.000; Android +103.8% p=0.013).
- The win is on payment, not on subscription starts: the winback interstitial mostly opens trials that rarely charge; the final interstitial is 100% immediate payment (first-show member→buyer +562% iOS / +113% Android).
- "The offer trades trials for immediate payment" (confirmed, now mature): trial share collapses (iOS Winbacks 90% → 27%, Android 80% → 48%); AOV/ARPPU fall by design; residual trial-takers convert worse (Android trial→charge Total 31.4% → 5.9% p=0.004) because the offer captures high-intent users up front. On this high-intent segment the immediate-$19.99 trade is still EV-positive.
- Cannibalization hypothesis ("any conversion is net-new") "holds on Android but not on iOS": iOS shows mild diffuse dilution (−27 non-winback buyers, −$702), largely offsetting the +$998 winback revenue gain; Android is incremental (+8 non-winback buyers) but underpowered.
- "Standard winback CR is structurally protected" — the final offer appears only after the winback window is exhausted and no sooner than the next day, so it cannot affect the winback interstitial's own conversion (offer-sequencing principle from the Pitch confirmed by design).
- Maturity discipline lesson: apparent significance can disappear as control trials mature into charges — total-account lifts must be re-read after trial maturation.
- (Confirmatory vs exploratory is labeled per finding on the page: mechanism #1, cannibalization split #2, first-show conversion #5 = confirmatory; "where did iOS non-winback purchases go" #3 = exploratory.)

## Sources
- Page: https://alice.mu.se/spaces/CRO/pages/788612067 ("[2026-05-04] UG App: winback - final interstitial offer [2026-07-30]"), snapshot output/confluence/flow568-interstitials/788612067/confluence_788612067.txt (v29).
- Sections used: "Context & Idea", "Confidence research" (1–4), "Solution", "Results → Decision" + "Next steps", "Forecast (per day)", "Design vs Reality check", "Significance analysis" (UGT_IOS / UGT_ANDROID; Total "Monetization Metrics", "Winbacks", "Retention Metrics", "Monetization Stats", "Retention Stats"), "Insights" ("Summary", "Detailed findings" #1–#6).
- AB id/run dates: page Insights Summary + snapshot `_registry.json` row 7487 (UMN-11515).
