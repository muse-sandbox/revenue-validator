**Verdict: redesign before launch.** The idea (arm B) is a legitimate retest of an inconclusive precedent, but the design as written cannot answer it — the sample math doesn't close, the primary metric is mis-scoped for a surface treatment, the hypothesis and instrumentation sections are unfilled, and arm C's price increase carries evidence-backed elasticity and refund risks with no dedicated guardrails.

**Predicted outcome.** Arm B: no significant Total DAU→Charge lift; likely a significant lift on splash-view/entry engagement metrics with flat money — the pattern measured on the closest precedent (T2-02, P-03). Arm C: charge conversion down on the touched offer, ARPPU up, net ARPU flat-to-negative, refund risk up (T3-01 direction). What would surprise me: a significant Total ARPU lift from the creative alone, or arm C's +$24.99 surviving the loss of the $19.99 intro for new users. The model's assumed +10% lift on both subscribe and charge is ungrounded — the direct precedent measured ≈0.

**Top risks & failure modes**
- **Under-delivery is near-certain as designed.** Android needs 304,757 users per arm × 3 arms (~914k) against 68,560 DAU over 9 days; iOS needs ~650k against 138,669 DAU over 3 days. The precedent had the identical iOS design target (216,622) and reached 20,329 [T2-02, P-12].
- **Total-only analysis segment will drown a surface effect.** One free-rights Total segment, no scenario-scoped metrics — the precedent's only significant read was scenario-level [T2-02, P-11; T1-10].
- **Emotional presentation lifts attention, not payment** [T2-02, P-03] — and the pre-splash animation inserts a step before the offer, a funnel-lengthening pattern that lost conversion elsewhere [T2-07, P-04; L2 warning, context differs].
- **Arm C price increase: elasticity ate a comparable App increase**, with refunds 14d +26.2% [T3-01, P-07]; and it removes the intro $19.99, whose intro-pricing mechanic was the measured positive component in T1-02.
- **Early rollout temptation in a fixed seasonal window** — the precedent rolled out on interim reads, forfeited the final read, and post-rollout forecast went negative [T2-02, P-12/P-13].

**Analogs**

```
analog:
  source: T2-02 (ab 6701, 2025-10, Halloween sale emotional design; SRM ok;
          under-delivered; result inconclusive; rolled-out early)
  level: L1 on axes — but validity-gated: inconclusive ⇒ measurement lessons only (§2.3 cond. 6)
  matched: [flow_stage: exact S3–S4 seasonal window; surface: exact — sale splash +
    Explore banner + entry animation; mechanism: exact — copy/design emotional;
    segment: exact — free App; metric: exact — CR DAU→Charge]
  mismatched: [offer: adjacent — no price arm in T2-02, so nothing there speaks to arm C]
  transferable: measurement lessons — Total money reads n.s. while only splash-view CR
    moved; identical iOS sample design (216,622) reached <10%; early rollout lost the
    final read. Note: the experiment card calls this precedent "concluded negatively";
    the KB records it as inconclusive and rolled-out — flag the discrepancy.
  not_transferable: all magnitudes; a product-level "themed animation doesn't work"
    conclusion (inconclusive source); "suitable for big one-off events" (author's
    extrapolation).
  conflict: with T1-07 below.

analog:
  source: T3-01 (ab 6026/6260, 2025-05..07, device-tier price increase; iter2 mature
          at 4.4× design; result mixed; killed)
  level: L2 — mechanism (App price increase) exact; flow_stage/surface differ (S6
    standard paywalls vs seasonal S3–S4 entry); segment adjacent (free device-tier
    proxy vs all free)
  matched: [mechanism: exact; segment: adjacent; platform: exact]
  mismatched: [flow_stage/surface: different — seasonal-context framing untested there;
    offer: different tier]
  transferable: warning — conversion falls roughly with the increase; ARPPU up, charge
    CR down, net ≈0; refunds 14d +26.2% is the guardrail to instrument.
  not_transferable: magnitudes; the elasticity curve shape (two points only); whether
    "seasonal context supports a higher price" — untested.

analog:
  source: T1-02 (ab 6002/6128/6191, 2025-04..07; mixed; killed)
  level: L2 for arm C — offer-structure/price-framing mechanism overlaps (intro
    pricing of the same annual plan); surface adjacent (interstitial vs splash)
  matched: [segment: exact free App; flow_stage: exact S3–S4]
  mismatched: [mechanism: adjacent, not exact — intro-pricing framing vs flat increase;
    surface: adjacent]
  transferable: warning — intro pricing of the same annual plan was the measured
    positive component; arm C deletes it for new users, working against a measured win.
  not_transferable: magnitudes (iter1 contaminated, P-14); any Pro+ $39.99 specifics.

analog:
  source: T1-07 (ab 7160/7187, 2026-03..07, gamified scratch-coupon pre-paywall;
          mixed; killed)
  level: L2 — mechanism (gamified/animated pre-step presentation) exact-ish; surface
    adjacent (interstitial vs sale splash); segment adjacent (free new post-tour vs all free)
  matched: [flow_stage: exact S3–S4; mechanism: adjacent-exact copy/design+gamification]
  mismatched: [segment: new post-tour only; trigger: interstitial cadence, not seasonal window]
  transferable: hypothesis in favor of arm B — an engaging pre-step CAN lift layer
    conversion on both platforms; but significant relative lift ≠ sufficient absolute
    increment (+$474/day forecast), and forced exposure charged retention (P-03).
  not_transferable: magnitudes; var2 internals (unexplained anomaly); non-skippable
    variant conclusions.
  conflict: T1-07 (engaging pre-step lifted money on the layer) vs T2-02 (emotional
    seasonal design moved no money). T2-02 is closer on surface and seasonality but is
    inconclusive; T1-07 is valid but on a different surface/segment. Hypothesized
    reason: T1-07 changed the interaction (gamified action), T2-02 only the wrapper
    (P-10 flavor). Report as unresolved; do not average.

analog:
  source: T2-01 (ab 6293, 2025-07, sale banner+splash off-test; significant-negative;
          killed/surfaces kept)
  level: L3 — surface exact, mechanism different (gating vs creative)
  matched: [surface: exact; segment: exact free]
  mismatched: [mechanism: different — grounds sizing/guardrails only]
  transferable: sizing/guardrail — these sale surfaces carry real incremental value
    (both-off ARPU −11.6% iOS / −26% And); splash is the weaker of the two (splash-only
    off n.s.), so banner-side creative may matter more than the splash intro.
  not_transferable: any product conclusion about creative; magnitudes.
```

**Design & measurement checklist**
- Redo the power math against reachable uniques; as designed, both platforms fall short. Options: drop arm C on Android, run 2 arms, or extend the window — decide before launch, not after (P-12).
- Rescope the primary read: sale-scenario metrics (banner/splash-attributed accesses, charges, scenario net revenue) as primary, Total DAU→Charge and ARPU as guardrails (P-11). Add SRM on both Total and the exposed scope.
- Exposure event on Explore open counts users who never see the splash — gate activation on first splash/banner exposure or analyze an exposed segment.
- Maturity: with the +7-day trial window, commit to a mature final read and no early rollout inside the sale window (P-13, T2-02).
- Fill the hypothesis template and the event/parameter table before launch; an unfilled analytics spec is how attribution artifacts get in (P-14).
- Arm C guardrails and stop-rule: refunds/cancels 14d (T3-01), and a separate read for new users who lose the intro price vs existing users.

**Changes that would most improve expected value**
1. Fix the power/arm-count plan and rescope the goal metric to the touched scenario — otherwise the experiment structurally repeats T2-02's unreadable outcome.
2. Split arm C reporting by intro-eligible new users vs others, with refund/cancel guardrails and a pre-agreed stop-rule; consider testing $24.99 without removing the new-user intro, since intro pricing is the one measured positive in this family (T1-02).
3. Pre-register the decision rule: what scenario-level result rolls out, and an explicit commitment not to roll out on interim reads before trial maturity.
