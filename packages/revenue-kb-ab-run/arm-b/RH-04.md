**1. Verdict — launch with changes.** The idea is a reasonable, reversible format test on a real surface, but the current design would produce an unreadable result: the exposure gate, goal-metric scoping, runtime, and power target all need fixing before launch, and the +65% ARPU hypothesis is not supported by the mechanism actually shipped in iteration 1.

**2. Predicted outcome.** Showcase view→click may rise (richer format, four destinations), but I expect conversion-to-access and ARPU to be roughly flat to modestly positive at best. The model assumes view→click improves while click→access and access→charge stay flat — that is exactly the pattern the corpus warns against: attention gains do not propagate to purchases (P-03, T1-09), and iteration 1 contains no actual personalization, only re-packaging of unchanged offers (P-10). Meanwhile the two existing tiles lose guaranteed simultaneous exposure: the discount and Spotify offers become one-of-four rotating cards, and first-position exposure carries most of a layer's value (P-01; T1-02: first exposure does 60–87% of the work). A significant ARPU lift anywhere near 65% inside a one-week immature window would genuinely surprise me; a *negative* read on the Spotify-connection funnel would not.

**3. Top risks & failure modes**
- **Reach dilution of proven placements.** The Spotify tile converts 8–8.8% view→click today; buried behind a swipe it will lose most of its exposure. Per-card reach, not per-impression CR, is the binding constraint (P-01, T1-04).
- **Net-increment loss from removing surfaces.** Turning off a discovery banner+splash cost −11.6%/−26% ARPU and conversion did not redistribute (T2-01). Replacing two always-visible tiles with one rotating slot is a partial off-test embedded in the treatment.
- **Clicks without money.** Two of four cards (tuner, courses) lead to non-monetizing or weakly monetizing destinations and can divert taps from the discount card (P-03).
- **Auto-advance retention price (arm C).** Forced motion on brand-new post-tour users echoes the non-skippable variant that cost Android D1 retention −9.15% (T1-07, P-03). No retention guardrail is currently listed.
- **Structurally unreadable design.** Exposure counted at tour-end banner-dismiss rather than showcase view dilutes every metric (P-11, P-12); a 2-day Android run powered only for a 92% lift cannot resolve realistic effects; purchases via the discount splash are trial-bearing, so a 1-week read is immature (P-13, T1-10).

**4. Analogs.** No L1 direct analogs — nothing in the corpus tests a carousel/showcase format on the discovery screen. Closest evidence:

```
analog:
  source: T2-01 (ab 6293, 2025-07, significant-negative/killed, SRM ok, R14 mature)
  level: L2
  matched: [flow_stage: exact — S3–S4 exposure; surface: adjacent — Explore/discovery
            promo tile family; segment: exact — free]
  mismatched: [mechanism: different — surface OFF vs format replacement; offer: seasonal]
  transferable: warning — discovery-surface promo tiles carry real incremental value
    (ARPU −11.6% iOS / −26% And when removed) and conversion does not redistribute;
    degrading a tile's exposure risks losing, not moving, its revenue
  not_transferable: magnitudes; seasonal-sale context; says nothing about the
    showcase's own upside
```

```
analog:
  source: T1-07 (ab 7160/7187, 2026-03..07, mixed/killed, SRM ok)
  level: L2
  matched: [segment: exact — free new post-tour; flow_stage: exact — S3–S4;
            mechanism: adjacent — design/format + skippability (arm C ≈ forced exposure)]
  mismatched: [surface: different — interstitial slot vs persistent discovery tile;
               trigger: different — event-triggered vs always-on]
  transferable: warning — format/engagement changes can lift layer conversion
    substantially yet still be killed for insufficient absolute increment;
    forced exposure buys engagement at a measured retention cost
  not_transferable: all magnitudes (+26.5% ARPU, −9.15% D1); var2 internals flagged
    anomalous on the source page
```

```
analog:
  source: T1-09 (ab 7454, 2026-05..06, inconclusive/killed — measurement lessons only)
  level: L3
  matched: [segment: adjacent — free; metric: same funnel metrics]
  mismatched: [surface: different; mechanism: adjacent-but-key — wrapper changed,
               offers unchanged, which is exactly RH-04 iteration 1]
  transferable: measurement/direction lesson only — repackaging unchanged offers
    produced ≈0 purchase movement ("personalize the offer, not the message");
    grounds skepticism about the 65% hypothesis, not a product conclusion
  not_transferable: any product conclusion (inconclusive); iOS arm unreadable
  conflict: mild vs T1-07 — format change lifted layer CR there but message-only
    change did nothing here; hypothesized reason: T1-07 altered interaction
    mechanics, T1-09 only creative. Both agree net money impact was small.
```

**5. Design & measurement checklist**
- **Exposure gate:** count exposure at showcase (or discovery-screen) view, not tour-end banner dismiss; keep randomization where it is but define the analysis population on actual exposure, with SRM checked at both points (P-11, P-12).
- **Metric scoping:** make the goal metric surface-scoped — access/charge from the showcase plus the two replaced tiles' funnels — with Total ARPU and Spotify-connection completions as guardrails, not the goal (P-11, T1-10).
- **Power/runtime:** the 92%/40% "target lifts" are model aspirations, not MDEs. Re-derive sample size for a defensible surface-level MDE (~20–30%) and run both platforms the same, longer window; a 2-day Android run also confounds day-of-week.
- **Maturity:** use a fixed per-user post-exposure window (late-cohort users otherwise get days of observation) and gate the revenue read on pending trial charges <5% (P-13).
- **Guardrails/stop-rules:** D1/D7 retention (mandatory for arm C), per-position card view rates and swipe-depth distribution, and a stop-rule on significant Spotify-funnel or Total ARPU degradation.

**6. Changes that would most improve expected value**
1. Reframe iteration 1's success criterion honestly: it tests carousel throughput, not personalization. Success = non-inferior ARPU plus clean per-position funnel data to design the personalized iteration (P-10); drop the 65% claim from the hypothesis.
2. Fix the measurement package above (exposure definition, surface-scoped goal, realistic MDE, maturity window) — without it even a true effect will be unreadable.
3. Test card ordering (e.g., rotate which card is in position 1 across users): position share will likely dominate everything else, and you get the reach curve you need for CRM sequencing for free.
