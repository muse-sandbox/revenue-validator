# GT-RH-04 — UG App: explore, sale – Promo block instead of sale banner

## Identity
- pageId: 746543363 — "UG App: explore, sale – Promo block instead of sale banner" (snapshot output/confluence/flow577_verify/746543363/, fetched 2026-08-04)
- URL: https://alice.mu.se/pages/viewpage.action?pageId=746543363
- AB experiment id: 6902; run 2026-01-27 .. 2026-02-02 (7 days), iOS + Android. Exposure/start event: Banner Tour Close.
- Jira: UMN-9885 (project); idea ticket UMI-92.
- Project page dates: 2025-12-16 .. (inventory T2-04).
- Arms: control (variation 1 — static sale banner + separate Spotify banner on Explore), variation 2 (4-card promo-block carousel — Sale / Spotify / Course / Tuner — no autoscroll), variation 3 (same carousel + 8-second autoscroll). Audience: new users only (Tour Install), finishing Tour Install without Pro rights; users buying Pro during the experiment revert to the variation-A Explore view. The Spotify banner exists only inside the new block in B/C.
- Segment config (#6902): Total {'pro_rights': 'free', 'platform': 'mobile', 'exposure_event': 'Banner Tour Close'}.

## Actual outcome
Sample sizes (Design vs Reality; experiment 7 days vs design 4 iOS / 2 Android; design sample 19114/arm iOS, 7453/arm Android):
- UGT_IOS: control 17609 / variation 2 17697 / variation 3 17622
- UGT_ANDROID: control 15727 / variation 2 16080 / variation 3 15869

Primary metric — CR to Access (decision block):
- Android: control 3.48%; var2 3.21% (−7.9%, p=0.17); var3 3.03% (−13%, p=0.023 — statistically significant decline)
- iOS: control 6.87%; var2 6.71% (−2.23%, p=0.57); var3 6.69% (−2.55%, p=0.51) — both not significant

ARPU (all arms not significant):
- iOS: control $0.901; var2 $0.809 (−10.2%, p=0.08); var3 $0.824 (−8.57%, p=0.14)
- Android: control $0.363; var2 $0.351 (−3.23%, p=0.76); var3 $0.338 (−6.86%, p=0.51)

Other monetization metrics (Significance analysis):
- iOS charge cr: 4.34% → var2 4.03% (−7.14%, p=0.15); var3 4.01% (−7.66%, p=0.12). Android charge cr: 1.53% → var2 −0.572% (p=0.95); var3 1.35% (−12%, p=0.17).
- iOS revenue $15867 → $14324 (var2, −9.7%) → $14517 (var3, −8.5%); Android $5710 → $5649 (−1.1%) → $5366 (−6%).
- iOS trial→charge: 19.5% → 16.1% (var2, −17.1%, p=0.12); charge→14d refund elevated in both arms (+59% p=0.11 var2; +66.8% p=0.08 var3) — ns.
- Retention: iOS var2 ret7d 37.2% → 36% (−3.07%, p=0.026 — significant); ret14d −2.45% (p=0.06); var3 flat. Android retention flat-positive, all ns.
- Tab-view engagement: Android 180s share down in both arms (var2 −3.09% p=0.038; var3 −3.66% p=0.014); Android var3 tab views 60s/120s per user −6.24%/−6.1% (p=0.016/0.023). iOS flat.

Promo Block CTR vs monetization (Insights): 4–6% of users click the promo block after exposure. Overall CTR (promo block view → click) higher in var3 vs var2: iOS +35% (5.93% vs 4.38%), Android +47% (5.54% vs 3.77%) — but not for the Sale card: sale view → sale click var3 vs var2 iOS −27% (1.16% vs 1.59%), Android −40% (0.72% vs 1.21%). Page verdict: "the CTR uplift represents attention inflation rather than intent uplift. Increased motion drives more clicks, but these interactions are lower quality and do not convert into additional accesses."

Purchases by source (control / var2 / var3):
- Spotify: iOS 40 / 26 / 32; Android 18 / 6 / 8 — declines on both platforms and both variants. Members → paywall view spotify fell −43..−51% (iOS −42.7%/−37.7%; Android −50.5%/−43.4%).
- Sale (New Year 25): iOS 64 / 71 / 59 (var2 +10.9%, var3 −7.8%); Android 34 / 26 / 15 (−23.5% / −55.9%).
- Courses accesses: iOS 41 / 40 / 40; Android 35 / 32 / 26 — declines despite the extra entry point.
- Other sources: stable in var2, decline in var3 (Android).

Card reach (var2 vs var3): Course card seen by ~5.5–6.5% (var2) vs ~8–9% (var3) of viewers; Tuner ~2–3% vs ~7–8% — users barely scroll manually, autoscroll drives reach of lower positions.

Forecast (per day) — all negative: Android var2 −27 accesses / −3 charges / −$101; var3 −44 / −15 / −$214. iOS var2 −21 / −32 / −$856; var3 −28 / −35 / −$721.

## Uncertainty & maturity
- SRM: "A/B balance is maintained" complete on both platforms (iOS 17609/17697/17622; Android 15727/16080/15869).
- Duration: "duration of exp ≥ design" complete on both platforms (7 days vs design 4 iOS / 2 Android). "No visible bugs" and "No external effects" complete.
- Pending-trial maturity: not documented on the page.
- Significance summary: the only significant monetization result is the Android var3 CR-to-Access decline (p=0.023); ARPU deltas ns everywhere; iOS var2 ret7d decline is significant (p=0.026); Android var3 tab-view-180s decline significant (p=0.014).

## Final decision
Decision status: killed — no rollout. Exact wording: "Do not roll out either Variant 2 or Variant 3, as the expected uplift in monetization metrics was not observed. Moreover, on Android, a statistically significant decline in CR to Access was identified for Variant 3."
Next steps / post-rollout sections were left as unfilled templates.

## Confirmed product lessons
- Plan vs fact: planned ARPU +65% from personalization/offer variability; observed no uplift anywhere — every ARPU and revenue delta is negative (ns), and the primary CR to Access declined, significantly so for Android var3.
- CTR is a false proxy for intent on this surface: motion/variability (autoscroll) raised overall promo-block CTR (+35% iOS / +47% Android vs var2) with no corresponding access or purchase uplift — "attention inflation, not intent" (page author's framing).
- Diluting a concentrated offer hurts it: replacing the dedicated sale banner and dedicated Spotify banner with a shared carousel dropped Sale purchases (Android −24%/−56%) and Spotify purchases on both platforms (iOS 40→26/32; Android 18→6/8); Spotify paywall reach roughly halved.
- Autoscroll specifically cannibalizes the Sale card (view→click −27% iOS / −40% Android vs manual scrolling) while boosting reach/clicks of low-position cards (Course, Tuner).
- Users barely scroll a carousel manually: without autoscroll only ~2–6.5% ever saw positions 3–4.
- Transfer bounds: this tests showcase-content variability on the App Explore surface; it does not refute offer-terms personalization (offer conditions were unchanged).

## Sources
- Page: https://alice.mu.se/pages/viewpage.action?pageId=746543363 ("UG App: explore, sale – Promo block instead of sale banner"), snapshot output/confluence/flow577_verify/746543363/confluence_746543363.txt (+ .storage.xhtml), fetched 2026-08-04.
- Sections used: "Pitch → Reach & Impact / Hypothesis / Experiment design", "Description of the Solution & Mockups → Solution", "Analytics" (#6902 config), "Results → Decision", "Design vs Reality check", "Forecast (per day)", "Significance analysis" (UGT_IOS / UGT_ANDROID Monetization / Retention / Tab View Metrics + Stats), "Insights" (promo-block funnel, Sale/Spotify purchase sources, by-source tables).
- Inventory: output/flow577_revenue_inventory/inventory.yaml, key T2-04 (verified against the page 2026-08-04).
