## 1. Verdict

**Launch with changes.** The idea is a cheap, well-instrumented format test, but the power design is built around the model's own optimistic target (92%/40% lifts, 2-day Android run), the exposure definition is wrong, and the two demoted funnels (Spotify tile, discount tile) have no guardrails — fix these before launch.

## 2. Predicted outcome

[hypothesis] Showcase view→click on the discount card plausibly rises — the one close precedent for an interactive-format wrapper on this exact segment lifted layer conversion (T1-07, L2 warning/hypothesis only). But the goal metric (access CR) is likely flat-to-modestly positive, well short of the modeled 92% (Android) / 40% (iOS) lifts, because the model's load-bearing assumption — flat click→access and access→charge — is exactly the assumption that failed in wrapper-only changes before (P-03, P-10). The ≈65% ARPU uplift is a target, not a prediction, and I would be surprised by it. I would *not* be surprised by a net-negative read on the Spotify funnel. What would most surprise me: a significant Total revenue lift within one week.

## 3. Top risks & failure modes

- **The stated cause isn't in the test.** The hypothesis credits "additional personalization", but iteration 1 shows the same four static cards to everyone. Wrapper changes without offer changes have not lifted purchases in this corpus (P-10; T1-09 direction lesson).
- **Attention ≠ intent** (P-03): a richer carousel can add curiosity clicks that convert worse downstream, violating the flat-downstream assumption the whole +$500/day model rests on.
- **Demoting the Spotify tile** (8–8.8% CTR, dedicated always-visible placement) into carousel position 2 may cut its effective reach; surface value does not redistribute for free (P-02; T2-01 as L3 guardrail signal). The model's assumption it *improves* to 10% is ungrounded.
- **Within-showcase competition** [hypothesis]: the two non-monetizing cards (tuner, courses) can siphon taps from the two selling cards — cannibalization is the default (P-02).
- **Auto-advance (arm C)** is mild forced exposure; the engagement/retention trade-off has a measured precedent on this exact segment (P-03; T1-07 Android D1 retention −9.15% under non-skippable — transfer warning).

## 4. Analogs

Ranked by closeness. No conflict to declare: T1-07 (interactive format lifted layer CR) and T1-09 (message-only wrapper, flat) differ in lever, and T1-09 is inconclusive/L3, so they are not at comparable evidentiary standing.

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact            # S3–S4 exposure both
    segment: exact               # free new post-tour in both
    trigger_eligibility: different  # scenario-triggered interstitial vs persistent layout
    surface: different           # full-screen interstitial slot vs embedded discovery carousel
    mechanism: exact             # presentation-format redesign of an offer surface, offers unchanged, incl. a forced-exposure arm
    offer: adjacent
    behavior: adjacent           # scratch interaction vs swipe
    metric: exact                # layer CR + ARPU both
    money_chain: exact
    guardrails: different        # T1-07 tracked retention; RH-04 card lists none
  segment_monetization_state: exact
  money_chain_link: exact        # both act on exposure→click/access
  platform: exact
  level: L2
  transferable: >
    [fact] Gamified format lifted interstitial-segment conversion on both
    platforms (T1-07); [fact] non-skippable variant multiplied engagement but
    cost Android D1 retention -9.15% (p=0.012); [fact] significant relative
    lift did not yield a sufficient absolute increment. [hypothesis] For
    RH-04: a richer interactive format can lift showcase CR directionally;
    the auto-advance arm carries a retention-risk warning; even a significant
    CR win may not clear the +$500/day bar.
  not_transferable: >
    All magnitudes (+26.5% ARPU, +72-166% layer CR, -9.15% retention) —
    different surface and interaction. Var2 internals flagged anomalous on
    the source page. L2: warning/hypothesis only, not a launch basis.
```

```yaml
analog:
  source: T1-09 (ab 7454; 2026-05..06; SRM ok; inconclusive; killed)
  axes:
    flow_stage: exact
    segment: different           # free + ex-paid mixed vs free new
    trigger_eligibility: different
    surface: different           # interstitial vs embedded showcase
    mechanism: adjacent          # message-personalization wrapper vs structural format redesign; both leave offers unchanged
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: exact
    guardrails: different
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    [fact] Wrapper-only change with unchanged offers moved nothing
    (all monetization p>=0.32); paywall→click halved. Inconclusive source:
    measurement/direction lesson only (rule 6). [hypothesis] L3 signal:
    instrument click *quality* (click→access per card), not just click
    volume, since wrapper-driven clicks converted worse.
  not_transferable: >
    All magnitudes; any product conclusion (inconclusive source); does not
    disprove offer-level personalization (the iteration-2 direction P-10
    recommends).
```

```yaml
analog:
  source: T2-01 (ab 6293; 2025-07; SRM ok; significant-negative; killed)
  axes:
    flow_stage: exact
    segment: different           # all free vs free new post-tour
    trigger_eligibility: different
    surface: adjacent            # Explore sale banner/splash vs discovery-top showcase
    mechanism: different         # surface OFF vs surface replacement
    offer: exact                 # seasonal discount offer both
    behavior: different
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    [fact] Removing the sale banner+splash cut ARPU -11.6% iOS / -26%
    Android; conversion did not redistribute. L3 guardrail/sizing signal
    only: [hypothesis] degrading an existing promo surface's effective reach
    (Spotify tile → carousel slot 2) can be net-negative even if the new
    format is "better"; guard the demoted funnels.
  not_transferable: >
    Magnitudes (seasonal-sale surfaces, config-specific); no product
    conclusion — L3 is never a verdict basis.
```

## Non-monetization effects to instrument

- **Positive side:** the tuner and course cards give new users free-feature discovery — instrument tuner opens, course-section entries, and D1/D7 retention per arm; a retention *gain* here would justify the format even with flat money.
- **Negative side:** carousel motion (arm C especially) may annoy or push content below the fold — instrument D1/D7 retention and discovery-screen engagement/scroll depth below the showcase.
- **Upper funnel:** Spotify connection starts and completions per arm, both directions (the model predicts a gain; the demotion risk predicts a loss).
- **Refunds/cancels:** no price change, so low prior, but track 14d cancels/refunds in case purchase mix shifts.
- **Stop-rules:** halt arm C on a significant D1 retention drop (precedent T1-07); flag/stop if Spotify funnel entries fall materially vs control.

## 6. Design & measurement checklist

- **Exposure gate (P-12, P-14):** exposure is counted at the tour-end banner-dismiss, not at showcase view. Anchor analysis (and SRM) at the new showcase-view event; keep SRM at randomization too.
- **Power:** MDE is set equal to the modeled target (92%/40%) — anything smaller reads as null by construction. Re-power on the smallest lift worth shipping; a 2-day Android run covers no weekly cycle — run ≥1 full week per platform.
- **Maturity (P-13):** one week cannot mature trial→charge; pre-commit that access CR decides and all ARPU/revenue reads are exploratory until charges mature.
- **Scope (P-11):** goal correctly scoped to modeled sources — keep it there; read Total only for dilution/cannibalization.
- **Per-card impressions:** log actual per-card views (including via cycling/auto-advance), not just showcase view, so position throughput is real.
- **Buyer switch-back to control layout:** define how post-purchase exposure ends in analysis so it doesn't bias arm comparisons.

## 7. Changes that would most improve expected value

1. Re-power to the smallest meaningful lift, run ≥1 week per platform, decide on access CR (defer ARPU to matured post-read).
2. Move the analysis anchor to the showcase-view event and add guardrails with stop-rules on the two demoted funnels (Spotify entries, discount-splash views).
3. Drop the +65%-ARPU/personalization framing for iteration 1 (nothing personalized is being tested); plan iteration 2 around actual offer/content personalization per P-10.
