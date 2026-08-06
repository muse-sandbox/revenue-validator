**Verdict: redesign before launch.** The card's own cited precedent (the October 2025 autumn version of this same mechanic) was null on general metrics, the hypothesis is an unfilled template, Arm C confounds creative with a 25% price increase, and the planned 3-day iOS run cannot observe the trial-gated primary metric it is powered on.

**Predicted outcome.** For B vs A, I expect DAU→Charge to be flat to weakly positive — the closest evidence available (the card's own prior autumn test of the same entry-animation mechanic) was concluded negative at the general-metrics level, and a bigger sale window changes the audience mood, not the mechanism. A detectable +10% lift from cosmetic theming alone would surprise me. For C vs A, expect DAU→Subscribe and DAU→Charge down (higher price, and the intro offer is removed for new users), with revenue/ARPU ambiguous — the sign depends on price elasticity that nothing in the card estimates. All of this is ungrounded assumption beyond the single precedent stated in the card itself; no KNOWLEDGE CONTEXT is present, so no direct analogs can be cited.

**Top risks & failure modes**
- **Repeating a known null with a bigger bet.** The same pre-splash animation mechanic already tested null in October 2025 (per the card's own research section). The impact model nonetheless assumes +10% on two conversion metrics with no justification; the realistic prior is ~0%, which means the test is underpowered for any effect it's actually likely to have.
- **Arm C is confounded.** It changes creative *and* raises the premium-plus annual from $19.99 to $24.99 while killing the new-user intro offer. If C moves, you cannot attribute it; if C loses, you don't know whether theming or price killed it. Ungrounded but structural.
- **Maturity mismatch.** The card notes a +7-day trial in the calculation, yet plans 3 days on iOS. DAU→Charge for trial-takers cannot mature inside a 3-day window; the primary metric will be systematically censored on the larger platform.
- **Exposure/effect mismatch.** Exposure fires on Explore open, but the treatment lives on the banner and pre-splash animation — and in Arm C the price change applies at the paywall to *all* users regardless of whether they saw any themed creative. Dilution in B, contamination of the exposure definition in C.
- **Animation as a friction risk.** An intro animation inserted before the splash can add latency and abandonment before the offer is even seen. Nothing in the card instruments animation completion, skip, or time-to-splash.

**Analogs.** No KNOWLEDGE CONTEXT provided — no direct analogs available; nothing beyond the card's own generically described autumn precedent can be cited.

**Design & measurement checklist**
- **Split Arm C's question out.** Run creative (B vs A) and price ($24.99 vs $19.99, same creative) as separable comparisons, or accept that C answers neither question.
- **Fix the primary metric per arm.** DAU→Charge suits B; for a price arm the decision metric is revenue/ARPU with conversion as a guardrail — a price rise is *expected* to lower CR.
- **Align duration with maturity.** Minimum window = sale window + 7-day trial maturity on both platforms; 3 days (iOS) / 9 days (Android) with different durations per platform also makes pooled readouts incoherent. Run both platforms the full window, analyze per platform.
- **Fill the instrumentation table before launch.** Add: banner impression, animation start/complete/skip, splash view, paywall view, per-arm SKU shown. Add SRM checks at exposure and at splash view.
- **Gate the analysis on real exposure** (banner or splash seen), not Explore open; for C, additionally verify the correct SKU rendered (a mis-served price is a silent bug that a "Total segment" analysis won't catch).
- **Segment new vs existing users** — Arm C changes the new-user intro economics specifically; a single Total segment will average two different treatments.
- **Add stop-rules:** abort C if revenue drops beyond a pre-set bound; abort B if splash-view rate drops materially (animation abandonment).

**Changes that would most improve expected value**
1. Write the hypothesis and per-arm success criteria before launch — as specced, Arm C has no modeled outcome at all and the formal hypothesis is a blank template.
2. Decouple price from creative (2×2 or sequential tests) so the December window yields at least one clean answer.
3. Re-power against a realistic effect (the prior test was null): either accept a longer run for a smaller MDE, or state explicitly that the test can only detect ≥+10% and treat "flat" as the expected, decision-relevant result.
