# MAIN

## Verdict
Redesign before launch: the surface the design enrolls on holds ~$0/day of the leak the hypothesis targets, and a two-arm package cannot attribute any result to the default tab.

## Findings

- **[stop]** [topic: tab-restore-default-confound] The slot buys a verdict on "tabs plus a Premium default" and leaves the card's own question — which product is shown first — open. *If:* the run stays two-arm, as the single 4,805 / 7-day design column implies. *Mechanism:* [computed] the treatment moves two things where production has neither, and the card prices separating them at `13.5 − 6.3 = 7.2` extra enrollment days. *Consequence:* a lift is attributable to the tab layer, the default, or their interaction; a null clears none of them. *Price:* decision impossible. *Fix:* three arms, or set the default without restoring the tab layer.
- **[stop]** [topic: guardrail-refund-cancel-subscribers] The safety half of the read arrives on far fewer subscriptions than it was sized for, and no outcome can fail it. *If:* enrollment stops at 4,805 exposed per arm with thresholds still to be defined. *Mechanism:* [computed] `4,805 × 17.43% ≈ 838` buyers per arm against the `1,185` subscriptions refunds 14d, cancels 14d and the bundle-share proxy require; the refund guardrail then resolves only `4.61% × 58.8% ≈ 2.71 pp`, so refunds at `4.61% + 2.71 = 7.32%` still read n.s. *Consequence:* the safety condition is met on any outcome. *Price:* decision impossible. *Fix:* size on subscriptions — `1,185 ÷ 17.43% ≈ 6,798` exposed per arm, `2 × 6,798 ÷ 1,373 ≈ 9.9` days — and set a numeric failure threshold per guardrail.
- **[stop]** [topic: tour-surface-zero-addressable] A tour-only run spends the slot and returns a defensive read against a target the surface cannot produce. *If:* version 1 enrolls on the tour paywall as scoped. *Mechanism:* [computed] `$9,459/day × 15% ≈ $1,419/day` is required, while the tour's addressable leak is ~`$0/day` — 2,646 of 2,647 tour purchases are already the bundle. *Consequence:* the goal metric must move on a surface where the mechanism has nothing to shift. *Price:* experiment slot. *Fix:* enroll where the leak is, or restate the tour arm as a defensive read.
- **[improve]** [topic: pro-tab-downside-top-segment] The segment gets a cheaper option it cannot choose today, and the bundle mix pays for it. *If:* the tab layer ships on the tour, where this segment sees only pro_edu_sing SKUs. *Mechanism:* [hypothesis] T3-03's menu-composition direction — buyers re-sort to the cheapest acceptable option — carried to a $47.70-ARPPU surface that currently offers one tier. *Consequence:* ARPU can fall through mix while buyer rate looks healthy. *Price:* share of the expected effect. *Fix:* make subscriptions→bundle share (baseline 64.24%) a stop-rule on the tour arm, not a proxy.
- **[improve]** [topic: feature-surface-bundle-price-gap] The surfaces that hold the leak stay outside version 1 while the catalogue gap creating it stays open. *If:* no bundle price exists off-tour and UMN-12572 has not landed. *Mechanism:* [computed] `1,083 ÷ 15 ≈ 72` cheap-path subscriptions/day `× $28.50 ≈ $2,058/day` sit on feature paywalls and ad interstitials, where no bundle SKU is priced. *Consequence:* the more expensive product cannot be presented on the only surfaces where a cheaper one is chosen. *Price:* money — that share of the $2,344/day upper bound is unreachable by any default tab. *Fix:* price the bundle off-tour and gate the feature arm on UMN-12572.

## What you decide
- **[product owner]** Whether version 1 enrolls on the tour at all, given ~$0/day addressable against the ~$1,419/day the +15% target needs.
- **[product owner]** Whether the ~86% of iOS tour traffic that now defaults to Pro ships without its own read; the $6.89 baseline covers only the 14.2% targeted.
- **[analyst]** Two arms or three — whether attribution is worth ~7 extra enrollment days.
- **[analyst]** The numeric failure threshold for refund 14d, cancel 14d, retention 7/14d, tour skip and store rating, and which denominator sizes the run.

## Product proposals
- **[offer]** [topic: bundle-price-feature-catalogue] *If:* a bundle SKU is priced on the feature paywalls before any tab work, covering the 1,083 of 1,235 cheap-path subscriptions sitting there at $22.09 against $50.59. *Grounds:* [hypothesis] transferring T3-03's direction (L2, appendix A): on that web menu the composition of the menu, not its presentation order, decided which plan buyers took; here the expensive tier is absent from the off-tour catalogue, so no default can act. *Then:* subscriptions→bundle share on feature paywalls up.
- **[ungrounded]** [topic: tier-tab-precedent-ios-paywall] Whether a Pro/Premium tab split behaves like a menu addition on an iOS paywall is not covered here — iteration 3 split tabs by duration and died after one day — and needs its own read.

## Non-monetization effects to instrument
- [topic: tour-skip-upper-funnel-top-segment] Bundle-first may cut tour skip (baseline 4.37%) for a segment that already buys the bundle, or raise it if the higher bar reads as a wall. Instrument tour skip and store-rating events daily per arm; stop-rule at the 28.4% relative move this design can detect.
- [topic: retention-d7-d14-tier-default] D7 7.88% / D14 5.73% can rise (more product owned) or fall (remorse at a higher payment bar). Instrument split by buyer/non-buyer and by tier purchased, with refund-reason codes.
- [topic: non-top-pro-default-engagement] The non-targeted majority moving to a Pro default: instrument exposed→buyers and D7 for them as a holdback rather than assuming neutrality.

## Closest analogs
- T3-03 (web three/six-month plans, killed): adding cheaper plans to a menu moved buyers down-market and cut subscribers instead of recruiting new ones; it differs here in platform and surface (web menu vs iOS paywall) and in that this change reorders two tiers rather than adding a plan — a partial analog, so a warning, not a prediction.
- T3-06 (iOS trial→instant on internal paywalls): explicitly weak signal only — an iOS offer-structure change that traded average check for buyers; usable here for sizing the mix-shift guardrails, not as an analog for a tier default.
- No conflict between the two: they point at different links of the chain.

## Predicted outcome
[hypothesis] On a tour-only two-arm run, ARPU/exposed most likely lands statistically flat with a downside tail from mix rather than at +15%, because the card's own measurement leaves nothing on that surface to shift upward. A significant lift on the tour arm would surprise me — it would mean the tab layer, not the default, moved buyer rate, and this design cannot tell those apart.

# APPENDIX

## A. Analog cards

```yaml
analog:
  source: T3-03 (ab 7502; 2026-05..06; SRM ok; pending 14d charges 24.0%/15.7%; significant-negative; killed)
  axes:
    flow_stage: exact            # plan/offer composition at the purchase step in both
    segment: different           # web new+unconverted vs iOS score-capped top propensity
    trigger_eligibility: different
    surface: different           # web plan menu vs iOS tour/feature paywalls
    mechanism: exact             # offer-structure: menu composition of what is offered
    offer: adjacent
    behavior: adjacent
    metric: exact                # conversion to payment + ARPU in both
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: different
  level: L2
  transferable: >
    [fact] Adding $19.99/3m and $24.99/6m to the web menu cut members→subscribers
    −11.08% (p=0.028) and →buyers −11.90% (p=0.038); short plans cannibalized
    annual instants [T3-03]. [interpretation] The source team read this as
    substitution: buyers re-sort to the cheapest acceptable option rather than
    new payers appearing. [hypothesis] For this case, the composition of what
    the segment can choose is the lever, and putting a Pro tab in front of a
    tour audience that today can only buy the bundle risks the same downward
    re-sort; conversely, the absence of a bundle SKU off-tour bounds any
    default-tab effect there.
  not_transferable: >
    All magnitudes (−11.08%, −11.90%, −$918…−$1408/day) — web funnel, different
    elasticity, different platform; P-06 explicitly bans transfer of the web
    plan-menu conclusion to App paywalls, so this card is a warning and a
    hypothesis, never a forecast. Trial-mechanics results inside the new plans
    do not transfer at all. It says nothing about tier-vs-tier tabs, which are
    untested here.
  sizing_prior: >
    prior: order of magnitude for menu-substitution effects on subscriber counts
    is low tens of percent, for sizing conversations only — not a prediction.
  conflict: >
    None with T3-06 below: that card is about payment timing on iOS, this one
    about menu composition on web; they act on different links.
```

```yaml
analog:
  source: T3-06 (ab 6326; 2025-06..09; SRM ok; 23-day run ≥ 19 design; mixed; rolled-out)
  axes:
    flow_stage: exact            # offer structure at the purchase step
    segment: adjacent            # free iOS on internal paywalls vs free iOS top-propensity
    trigger_eligibility: different
    surface: adjacent            # internal App paywalls vs tour + feature paywalls
    mechanism: different         # trial→instant payment timing vs which product tier is default
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: different
  platform: exact
  level: L3
  transferable: >
    [fact] Charge CR +16.4% (p=0.00), access CR +4.04% (p=0.05), ARPU +5%
    (p=0.18, n.s.), AOV/ARPPU −9.8…−13.2% (p=0.00), 14d cancels −42.2%
    (p=0.00) [T3-06]. Explicitly labelled L3: weak signal, no product
    conclusion transfers. Usable here only as a measurement and guardrail
    lesson — an offer-structure change on iOS paywalls moved the mix and the
    cancel rate while the headline ARPU stayed n.s., which is why the mix and
    cancel metrics here need their own sized denominator and thresholds.
  not_transferable: >
    Every magnitude; the sign of any effect on this case; the product
    conclusion "drop the trial" — this experiment changes tier, not payment
    timing, and the money-chain link differs. It may not ground any product
    proposal or move the verdict.
```

## B. Design & measurement checklist
- Goal metric vs touched surface (P-11): ARPU/exposed is scoped to the segment, which is right, but pooling tour and feature paywalls averages a surface with ~$0/day addressable against one holding the leak. Pre-register the readout split by surface; see [topic: tour-surface-zero-addressable].
- Delivery gate (P-12): the feature arm depends on UMN-12572 and on a bundle price existing off-tour; without both, "top" off-tour is 89% legacy base and the arm is undelivered by construction.
- Maturity (P-13): the 21-day metric window plus 14d refund/cancel windows means the final read is not available at day 7 of enrollment; state the pending-charge share gate before reading.
- SRM/activation: check balance on exposed users, and separately on the score>=−1 qualification event, since the score is device-persisted and frozen on May 2026 cutpoints.
- Attribution (P-14): the bundle-share proxy depends on SKU-level attribution across tour, feature paywalls and ad interstitials; verify funnel_source tagging before launch, given that 2,646 of 2,647 tour purchases already resolve to one SKU family.
- Guardrails worth adding: a numeric floor on subscriptions→bundle share for the tour arm, and a per-arm daily revenue-per-buyer monitor (baselines $22.09 Plus / $50.59 bundle).

## C. Design changes that would most improve expected value
1. Three arms (no tabs / tabs with Pro default / tabs with Premium default), accepting ~13.5 days of enrollment, or drop the tab layer and change only the default.
2. Size the run on the subscription-denominator metrics (~6,798 exposed per arm, ~9.9 days) rather than on the ARPU denominator, and attach a numeric failure threshold to each of the five named guardrails.
3. Re-scope version 1 to the feature paywalls once a bundle SKU is priced, keeping the tour as a bundle-only control arm read defensively.

## D. Findings without a price
- Whether the Pro and Premium tabs retain the monthly/yearly split inside them is open; if retained, the tabs nest and the mockup set doubles, but the cost cannot be named in one of the five units from this card.
- Scorecard cutpoints are frozen on May 2026 data while `score >= -1` is an absolute threshold, so segment composition drifts if the scorecard is reweighted mid-run.
- The Solution/Mockups, analytics events and execution-results sections are unfilled template rows; no exposure or event contract is documented.
- The post-decline instant offer (152 subscriptions / 15 days on ugt.plus.instant.1year3) is listed both as part of the measured leak and as out of scope.

## E. Generic suggestions
- Pre-register the analysis plan, including which comparisons carry α, before enrollment starts.
- Freeze the segment definition and the SKU→tier mapping at launch and log both with the exposure event.
- Run a daily SRM and delivery check for the first three days rather than only at readout.
