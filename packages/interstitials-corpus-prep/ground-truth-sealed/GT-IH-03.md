# GT-IH-03 — UG App: personalized interstitial

## Identity
- pageId: 788613565 — "[2026-05-05] UG App: personalized interstitial [2026-06-18]" (snapshot v41, 2026-06-18)
- URL: https://alice.mu.se/spaces/CRO/pages/788613565
- AB experiment id: 7454 (Iteration #1; no relaunch). AB registry run 2026-05-18..2026-05-27; Design-vs-Reality duration 10 days. Exposure event: App Experiment Start (fires when the user becomes eligible for the new interstitial splash).
- Jira: UMN-11540
- Dates: project page dates 2026-05-05 .. 2026-06-18.
- Arms: control = variation 1 (generic interstitial); variation 2 = test (personalized "song" interstitial anchored on the currently opened song: "Play %SONG_NAME% like %SONG_AUTHOR%"; free users get "80% off Pro+" badge / AD Song Interstitial, ex-paid get "Welcome-back gift: +14 days Pro+" / AD Winback Song Interstitial). Same commercial offers as today; personalized interstitial takes precedence, appears only once.
- Segments configured: Total {'pro_rights': 'All'}; Interstitials {'pro_rights': 'All', 'custom_sub_having': "funnel_source like '%Interstitial%'"}; Free {'pro_rights': 'Free'}.

## Actual outcome
Sample sizes: UGT_IOS 14,674 control / 14,293 variation 2; UGT_ANDROID 81,189 / 80,724; 10 days.
Important delivery caveat (Insights): "iOS effectively never ran: real volume exists only for 2026-05-18…05-20 (~14.3k of 14.7k members), then 1–3 users/day. No iOS reading is possible." The Insights deep-dive is Android only. Also, because App Experiment Start fires only for interstitial-eligible (free/ex-paid) users, Total ≡ Interstitials ≡ Free as member sets (Android v1: 81,189 / 81,189 / 81,187), and Total = Free to the cent in every metric.

UGT_ANDROID Total (= Free): ARPU $0.114 → $0.117 (+2.32%, p=0.77); access cr 0.987% → 0.985% (−0.177%, p=0.97); charge cr 0.525% → 0.53% (+1.05%, p=0.88); trial→charge 14% → 15.6% (+11.2%, p=0.50); churn/refund flat. Stats: revenue $9,274 → $9,434 (+1.7%); buyers 426 → 428; charges 437 → 438.
UGT_ANDROID Interstitials segment: ARPU $0.0278 → $0.0284 (+1.92%, p=0.89); access cr 0.259% → 0.248% (−4.21%, p=0.66); interstitial subscribers 210 → 200 (−4.8%); revenue $2,260 → $2,290 (+1.3%). Nothing significant.
UGT_ANDROID retention: ret1d 22.6% → 22.9% (+1.69%, p=0.07); ret7d 57.3% → 57.5% (+0.362%, p=0.40); ret14d 68.6% → 69% (+0.665%, p=0.048).

UGT_IOS (recorded but not readable per Insights): Total ARPU $0.409 → $0.355 (−13.4%, p=0.11); Interstitials ARPU $0.0713 → $0.0432 (−39.4%, p=0.023), access cr 0.75% → 0.455% (−39.3%, p=0.001), charge cr −45.8% (p=0.002), refund 14d 6.94% → 0% (−100%, p=0.020); retention flat.

Behavioral results (Android, event-based Purchase Process Finish — "a behavioral signal, not net revenue"):
- Net conversion is flat: combined per family ≈ control (free 0.155% vs 0.153%; winback 1.59% vs 1.66%).
- Conversion is heavily front-loaded: impression #1 holds ~50% (free) / ~60% (winback) of all conversions; the personalized splash sits in exactly that slot. Free at #1: 0.077% → 0.072% (−6%, flat); Winback at #1: 0.996% → 0.749% (~−25%), with Test recovering on later impressions (#5+ 0.069% → 0.167%).
- Funnel shape (free flow): Splash→Paywall 30.9% → 32.4% (slightly more paywall views) but Paywall→Click roughly halves: 7.25% → 3.90% — "it wins curiosity but loses intent".
- Apparent winback "paywall lift" (6.4% → 29.8%, 4.6×) is an attribution artifact: the legacy generic winback interstitial does not stamp its own name onto the downstream paywall event, the new song-winback flow does; by any Banner Upgrade View all four groups sit at ~66–76%.
- Intent-to-treat, member level: ex-paid converts ~20× better per member than free (interstitial finish/member 1.95% vs 0.095%) despite being ~10% of the audience (~8.3k/arm vs ~72.5k/arm); genuine paywall-reach lift is modest (+3pp free, +7pp ex-paid); conversion flat-to-noisy (free +14% on a tiny base, ex-paid −7%).
- Treatment dose: the personalized interstitial shows once, then reverts to default AD 14Free; impression #1 is ~74% personalized (AD Song 55.2k + AD Winback Song 4.7k of 80.7k), #2+ almost entirely default (52.2k default vs 5.8k song).

Forecast (per day): iOS control 63,109 App Experiment Start / 2,383 accesses / 464 interstitial accesses / 1,428 charges / $25,839 vs var2 2,172 / 283 / 1,276 / $22,386 → diff −211 accesses / −181 interstitial accesses / −152 charges / −$3,453. Android: control 32,415 / 334 / 84 / 174 / $3,703 vs var2 337 / 80 / 176 / $3,788 → diff +3 / −4 / +2 / +$85.

## Uncertainty & maturity
- Decision text: "No metric is statistically significant (all p ≥ 0.32); underpowered on the goal metric despite ~80k members/arm — interstitial-attributed conversions are only ~70–165 per arm." (Note: the iOS Interstitials table shows some p<0.05, but the page's Insights declare iOS unreadable due to the delivery failure; the Android tables — the readable platform — have all monetization p ≥ 0.32.)
- iOS delivery failure: real exposure only 2026-05-18..05-20, then 1–3 users/day — "No iOS reading is possible."
- Attribution data-quality problem: the winback paywall funnel lift (4.6×) is a measurement artifact of value-tagging asymmetry between the legacy and new flows.
- Segment overlap: Total ≡ Interstitials ≡ Free (same members) — the three configured segments are essentially one set.
- Design vs Reality: design "was not calculated" for both platforms; "duration of exp ≥ design" incomplete on both; A/B balance maintained (Δ 0.57% Android, clean).
- Pending-trial maturity: not documented on this page.
- Android ret14d +0.665% has p=0.048 but is not called out as a finding by the team.

## Final decision
Decision status: Red — Fail. Exact wording:
- "do not roll out iteration #1 as-is. The result is neutral / inconclusive (no significant lift), so iterate before any further investment."
- Supporting bullets: "Net conversion is flat: combined per family ≈ control (free 0.155% vs 0.153%; winback 1.59% vs 1.66%)." / "At impression #1 (~50–60% of all interstitial conversions) the personalized splash converts same-or-worse (free −6%, winback −25%): it wins curiosity but loses intent — paywall→click roughly halves (7.25% → 3.90%)." / "The one apparent win (winback paywall +4.6×) was an attribution artifact, not real engagement." / "No guardrail benefit either; ARPU / churn / refund moves are all within noise."
Next steps (iterate directions): align the paywall to the personalized hook (change the paywall/offer, not just interstitial copy — biggest leak is paywall→click, likely expectation mismatch); extend personalization beyond the first impression; next iteration should test offer-level personalization; possible directions — an additional interstitial with a stronger deal for users free >1 week, or targeting previously-paid users with a discount instead of another free trial; "The main direction is to personalize the offer, not only the message around the offer."

## Confirmed product lessons
- Personalizing only the message/wrapper (song-anchored copy) does not increase purchase intent: it brings slightly more users to the paywall but paywall→click drops ~2× (7.25% → 3.90%) — "the personalized screen created curiosity, but the generic paywall after it did not continue the personalized promise"; "the personalization stopped before the actual purchase decision."
- "Personalization is more likely to work when it changes the offer itself, not only the wrapper around the offer" — winback interstitials and discount offers for young users are cited as better examples of meaningful personalization because the offer matches the segment.
- Interstitial conversion is heavily front-loaded (impression #1 = ~50% free / ~60% winback of conversions), confirming prior internal analysis that 60–90% of conversions happen within the first impressions.
- Ex-paid users convert ~20× better per member than pure free users (1.95% vs 0.095%) — the most valuable cohort despite ~10% of the audience.
- Measurement lessons: legacy vs new flows can tag downstream paywall events asymmetrically (attribution artifact); App Experiment Start eligibility can make configured segments collapse into one; single-source funnels understate a two-source test arm (personalized first + default afterwards must be summed).

## Sources
- Page: https://alice.mu.se/spaces/CRO/pages/788613565 ("[2026-05-05] UG App: personalized interstitial [2026-06-18]"), snapshot output/confluence/flow568-interstitials/788613565/confluence_788613565.txt (v41).
- Sections used: "Pitch / Context & Idea", "Confidence research", "Solution" (#7454), "Analytics" (#7454 config), "Results → Iteration #1 - #7454" → "Decision", "Next steps", "Forecast (per day)", "Design vs Reality check", "Significance analysis" (UGT_IOS / UGT_ANDROID Monetization/Retention/Tab View Metrics + Stats), "Insights" ("Audience & exposure reality", "How the treatment was actually delivered", "Conversion by impression number", "Funnel shape (free flow)", "Winback 'paywall lift' is an attribution artifact", "Free vs ex-paid (winback) behavior").
- AB id/run dates: snapshot `_registry.json` row 7454 (UMN-11540).
