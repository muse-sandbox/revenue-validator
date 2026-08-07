# GT-IH-04 — UG App: interstitial - discounted prices

## Identity
- pageId: 811868738 — "[2026-07-03] UG App: interstitial - discounted prices [2026-XX-XX]" (snapshot v17, 2026-07-31; page end date not filled in — still "2026-XX-XX")
- URL: https://alice.mu.se/spaces/CRO/pages/811868738
- AB experiment id: 7712 ("[UG Monetization] UG App: interstitials - discounted prices"). AB registry run dates 2026-07-13 .. 2026-07-21 (9 delivered days, matching the page's "9 of 15 designed days"). Exposure event: App Experiment Start.
- Jira: UMN-12220
- Dates: project page start 2026-07-03; registry run 2026-07-13..2026-07-21; page end date not documented.
- Arms delivered: control (variation 1) and variation 2. The design specified three variations (A/B/C) with Bonferroni α/2=0.025, but "the admin ran two."
- Treatment: replace both the ad-free (14Free) and winback interstitials with a "discounted interstitial" offering instant Pro+ plans at $29.99 (no trial, no intro ramp). Audience: only users who passed tour install during the experiment. Follow-up to UMN-9389 (free-paywall) and UMN-9259 (winback), whose next steps called for "drop the trial, promote direct purchase".
- Design (binding stats, power 0.8, α/2=0.025, 3 arms): iOS — goal Total ARPU baseline $0.11, lift 60.67%, sample 8,511/variation, 4 days; proxies 14Free ARPU ($0.087, 4 days) and Winback members→buyer (1.41%, +88.30%, 15 days). Android — Total ARPU $0.071 (+67.03%, 13,234, 7 days), 14Free ARPU $0.051 (14,644, 8 days), Winback members→buyer 1.68% (+88.30%, 1,988, 20 days). Binding duration ≈ 15 days iOS / 20 days Android.

## Actual outcome
Delivered sample: iOS 7,075 control / 7,043 variation 2 (design 8,511), 9 of 15 designed days; Android 6,586 / 6,622 (design 14,644 — under half), 9 of 20 designed days.

Treated surface (14Free interstitial; per-surface figures from Insights, net revenue):
- iOS: net revenue $353.87 → $559.62 (+58.14%) at flat subscription volume (28 → 29, +3.57%); surface ARPU $0.050 → $0.080; effective net revenue per subscription $12.64 → $19.30 (+52.69%). "This surface carries no trial in either variation and every subscription has already charged, so the number is final, not preliminary."
- Android: net revenue $262.28 → $249.00 (−5.06%); surface ARPU $0.040 → $0.038; effective first payment $14.57 → $24.90 (+70.89%) but subscription volume 18 → 10 (−44.44%) — "the platforms differ in elasticity, not in the offer."

Package "Interstitials" segment (both interstitials combined):
- iOS: ARPU $0.059 → $0.083 (+41.65%, p=0.22); AOV/ARPPU $13.03 → $20.28 (+55.60%, p=0.000); members→subscribers 0.86% → 0.44% (−48.95%, p=0.002); trials share 54.10% → 6.45% (−88.07%, p=0.000); cheapskaters 15.15% → 0.00% (p=0.015); revenue $417 → $588; subscriptions 61 → 31; instant accesses 28 → 29.
- Android: ARPU $0.040 → $0.053 (+34.17%, p=0.45); AOV/ARPPU $13.81 → $25.28 (+83.08%, p=0.000); members→subscribers 0.61% → 0.26% (−57.73%, p=0.002); trials share 52.50% → 17.65% (−66.39%, p=0.004); revenue $262 → $354; subscriptions 40 → 17.

Total segment (goal metric — flat-to-negative):
- iOS Total: ARPU $0.53 → $0.50 (−5.37%, p=0.61); members→subscribers 4.98% → 4.12% (−17.24%, p=0.014); trials share 46.83% → 39.00% (−16.72%, p=0.042); revenue $3,764 → $3,546; churn 14d 23.87% → 27.78% (p=0.36).
- Android Total: ARPU $0.22 → $0.20 (−7.08%, p=0.73); revenue $1,448 → $1,353; churn 14d 9.09% → 20.31% (+123.44%, p=0.07 — not interpretable, see maturity).
- The two interstitials produce only 12.20% of iOS and 17.40% of Android control-branch cohort revenue; untouched surfaces (87.80% / 82.60% of revenue) drifted −6.56% (iOS) and −21.51% (Android) for reasons unrelated to the treatment, dominating the Total figure.

Cannibalization/recovery: "No measurable recovery" — untouched-surface subscriptions 291 → 266 (iOS) and 157 → 154 (Android), flat to slightly down, not up (exploratory). Engagement guardrails flat (app retention 7d −0.88% iOS / −0.59% Android; tab-view events per user −0.79% iOS). Retention: iOS ret1d/7d/14d 16.88/37.33/42.08% → 16.57/37.00/42.18% (p=0.63/0.69/0.90); Android 13.18/31.61/35.92% → 14.13/31.43/36.09% (p=0.11/0.82/0.84).

Winback interstitial surface: not readable — iOS control 32 of 32 subscriptions are trials, only 4 charged, 18 still inside the charge window; Android 0 of 24 charged. Control revenue on that surface will keep rising, so the comparison understates control.

Forecast (per day; the page itself warns it "understates the change and should not drive the call"): iOS control 7,543 Experiment Start / 387 subs / 237 charges / $4,013 vs var2 321 / 212 / $3,797 → diff −66 subs / −25 charges / −$215. Android control 7,089 / 211 / 71 / $1,558 vs var2 187 / 69 / $1,448 → diff −24 / −3 / −$110.

## Uncertainty & maturity
- iOS surface win not significant: "+58% … still not significant (p=0.22 on surface ARPU) because the run delivered 9 of the 15 designed days." Directionally large surface effects land at p 0.2–0.5 because of the truncated run.
- Charge-quality/churn: no conclusion available — "pending 14d charges share is far above the 5% gate in all branches: iOS 61.26% control / 59.60% test, Android 78.79% / 71.88%." Churn 14d and refund 14d "are therefore not interpretable — the nominal Android churn move 123.44% (p=0.07) sits on a base that is mostly still pending."
- Winback surface: "undecided, not a negative result" — control branch entirely trial-based, most trials haven't reached their charge date; revisit after 2026-08-04 when the control trials' charge window closes.
- Delivery vs design: "No — it ran to roughly half the planned exposure and one variation short." 9 days vs 15 (iOS) / 20 (Android) designed; Android under half its planned sample; 2 of 3 planned variations shipped. A/B balance fine (under 1% on both platforms); "duration of exp ≥ design" check incomplete on both.
- Goal-metric mismatch: "The design baseline for the goal metric ($0.11 iOS / $0.071 Android) is close to the measured interstitial-surface ARPU, not to the measured Total-segment ARPU ($0.53 iOS / $0.22 Android). The experiment was sized for the surface metric but judged on the all-surface metric" — a base roughly 8× wider than the change, "which cannot resolve it at any realistic sample." "The goal metric could not have detected this."
- Findings are labeled on-page: surface-revenue, mechanism, Total-ARPU-dilution, maturity, and delivery answers = confirmatory; other-paywall recovery = exploratory.

## Final decision
Exact wording: "Do not roll out this iteration on either platform. Keep the concept alive for iOS. Final call is the DRI's."
- "iOS — hold and re-run, do not discard. On the 14Free interstitial the instant offer lifted net revenue by roughly +58% at flat subscription volume, and that comparison is trial-free and fully charged on both sides, so it is a final read rather than a preliminary one. It is still not significant (p=0.22 on surface ARPU) because the run delivered 9 of the 15 designed days."
- "Android — no case for the $29.99 step. The higher effective first payment was almost exactly cancelled by a conversion loss, leaving surface revenue slightly negative. This is price elasticity, not execution: same offer, same creative, same triggers as iOS."
- "Winback interstitial — undecided, not a negative result." (control trial revenue still incomplete)
- "The headline Forecast understates the change and should not drive the call." (projected −$215/day iOS, −$110/day Android built on the diluted Total ARPU)
- "Nothing can be concluded about subscriber quality yet."
Next steps: re-run on iOS with the interstitial surface as the primary metric; run the re-test to the designed exposure; revisit the Winback surface after 2026-08-04 and re-read charge quality then; on Android test a smaller price step before repeating $29.99 ("the conversion loss, not the ticket size, is the binding constraint"); "Do not reuse Total ARPU as the goal metric for surface-scoped paywall tests. Size and judge them on the segment that the treatment actually reaches."
No rollout; a hold/re-run stance for iOS. Decision-status macro color: not documented on the page (unlike IH-01 Red / IH-02 Green).

## Confirmed product lessons
- "The offer worked on the surface it changed, on iOS": instant $29.99 (no trial) lifted 14Free-interstitial net revenue +58.14% at flat volume — direct, trial-free, fully-charged evidence (confirmatory).
- "On Android the same offer is a wash, because conversion is price-elastic": +70.89% effective payment × −44.44% volume ≈ −5.06% revenue. Same offer/creative/triggers as iOS ⇒ platform price-elasticity difference, not execution (confirmatory).
- Mechanism = price, not trial removal per se: trials share collapsed as intended on both platforms (iOS 54.10% → 6.45% p=0.000; Android 52.50% → 17.65% p=0.004); the outcome is driven by how each platform absorbs a higher effective first payment. Quality proxies moved the right way where readable (iOS cheapskaters 15.15% → 0.00%, p=0.015; AOV +55.60% iOS / +83.08% Android).
- Metric-design lesson (the page's most emphasized takeaway): a surface-scoped treatment must be judged on the treated surface. Total ARPU averaged a 12–17%-of-revenue surface with 83–88% untouched, independently drifting revenue, making the goal metric structurally unable to detect the effect.
- Losing interstitial subscriptions did not push users to other paywalls (no measurable recovery; exploratory).
- Delivery discipline: stopping at ~half the designed exposure and dropping a planned arm leaves directionally large effects unresolved (p 0.2–0.5).

## Sources
- Page: https://alice.mu.se/spaces/CRO/pages/811868738 ("[2026-07-03] UG App: interstitial - discounted prices [2026-XX-XX]"), snapshot output/confluence/flow568-interstitials/811868738/confluence_811868738.txt (v17).
- Sections used: "Pitch / Context & Idea", "Confidence research", "Reach & Impact" (+ "Impact — forecast"), "Experiment design — binding stats" + "Recommendation", "Solution", "Results → Decision" + "Next steps", "Forecast (per day)", "Design vs Reality check", "Significance analysis" (UGT_IOS / UGT_ANDROID; Total "Monetization Metrics", "Interstitials", "Retention Metrics", "Monetization Stats", "Retention Stats"), "Insights" ("Insight summary" and the six "Supporting questions" subsections).
- AB id/run dates: snapshot `_registry.json` row 7712 (UMN-12220).
