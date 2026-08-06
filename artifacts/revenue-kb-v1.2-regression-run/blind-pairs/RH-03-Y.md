# RH-03 validation (Arm B — with KNOWLEDGE CONTEXT)

## 1. Verdict

**Redesign before launch.** The design cannot answer its own question — planned durations are arithmetically insufficient for the stated sample requirements, the hypothesis and instrumentation sections are unfilled templates, the only analysis segment is Total — and its closest analog (T2-02) failed precisely as a delivery/measurement failure; arm C additionally bundles a price increase into a creative test.

## 2. Predicted outcome

[hypothesis] B vs A: null on DAU→Charge at Total scope, with attention metrics (splash views) possibly up — the L1 analog T2-02 read exactly that shape, and P-03 gives the mechanism. The modeled +10% lift on both subscribe and charge is an ungrounded assumption; the card's own precedent read n.s. [hypothesis] C vs A: structure shift — ARPPU up, charge CR down, refunds up, net roughly flat (T3-01, L2 warning). What would surprise me: a significant Total DAU→Charge lift from theming alone inside a 3-day iOS window.

## 3. Top risks & failure modes

- **Repeat of the precedent's delivery failure.** T2-02 reached a fraction of its design sample (20,329 vs 216,622 iOS) and was rolled out early, forfeiting the final read (P-12, P-13). RH-03's own arithmetic fails: 216,622 uniques/arm × 3 arms > iOS DAU 138,669 × 3 days even ignoring returning-user overlap; Android likewise (304,757 × 3 > 68,560 × 9).
- **Attention ≠ purchase intent** (P-03): T2-02's only significant lift was CR→Splash View; T1-09 halved paywall→click. Within creative/design changes on exposure surfaces, evidence is mixed: decorative/emotional theming did not move money (T2-02 — measurement lesson; T1-09), while creative that changed reach/content did on Android (T1-04); the boundary is whether the creative changes what is reached/offered, not how festive it looks.
- **Arm C elasticity + refunds** (T3-01, L2): the comparable App price increase saw charge CR −11% (p=0.003) and refunds 14d +26.2%; C also silently removes the intro offer for new users — intro pricing of the same annual plan was the positive component of T1-02 iter1–2.
- **Pre-splash animation as friction/forced exposure**: retention cost where measured on a non-skippable variant — Android D1 −9.15% (T1-07, explicitly L3 weak signal, guardrail only); P-04 warns about inserted steps before the offer.
- **Total-only segment hides cannibalization** (P-11, P-02): T2-02 showed ~−2% cannibalization of other sources; a Total metric diluted across all free users cannot separate scenario lift from source-shift.

## 4. Analogs (ranked)

```yaml
analog:
  source: T2-02 (ab 6701; 2025-10; SRM ok; duration/sample incomplete; inconclusive; rolled-out early)
  axes:
    flow_stage: exact            # S3–S4 seasonal sale window in both
    segment: exact               # free App users
    trigger_eligibility: exact   # seasonal-window display on same surfaces
    surface: exact               # sale splash + Explore banner + entry animation
    mechanism: exact             # copy/design — emotional/thematic seasonal presentation
    offer: exact                 # production offers unchanged (arms A/B)
    behavior: adjacent
    metric: exact                # CR DAU→Charge in both
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L1
  transferable: >
    [fact] Finals n.s. (ARPU iOS -2.95% p=0.66, And -1.38% p=0.91); only
    CR->Splash View significant (p=0.001); ~-2% cannibalization; post-rollout
    forecast iOS -$1716/day (T2-02). Source is result_class inconclusive, so
    per the validity gate (§1.7, §2.3.6) NO product conclusion transfers even
    at L1 — only measurement lessons. [hypothesis] RH-03 repeats the same
    design (short window, Total metric, sample it cannot reach) and therefore
    risks reproducing the same unreadable outcome, not necessarily the same
    product outcome.
  not_transferable: >
    Any "seasonal emotional design does not work" product conclusion
    (inconclusive source); all magnitudes; the author's "suitable for big
    one-off events" extrapolation.
```

```yaml
analog:
  source: T2-01 (ab 6293; 2025-07; SRM ok; R14 mature; significant-negative for turn-off; killed)
  axes:
    flow_stage: exact            # S3–S4
    segment: exact               # free
    trigger_eligibility: adjacent
    surface: exact               # sale banner + sale splash, same surfaces
    mechanism: different         # surface OFF gating vs creative restyle
    offer: adjacent
    behavior: adjacent
    metric: adjacent             # ARPU vs DAU->Charge
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Turning banner+splash off cost ARPU -11.6% iOS / -26% And (both
    p=0.036); splash-only-off n.s. (T2-01). [hypothesis] The seasonal
    surfaces carry real incremental value, concentrated in the banner; a
    restyle that adds friction before the splash puts existing value at risk,
    and the downside is bounded-real, not hypothetical.
  not_transferable: >
    Magnitudes (seasonal, inventory-specific); any conclusion about the
    animation itself (mechanism differs).
```

```yaml
analog:
  source: T3-01 (ab 6026/6260; 2025-05..07; SRM ok; iter2 mature at ~4.4x design; mixed; killed)
  axes:
    flow_stage: adjacent         # S6 purchase conditions vs S3-S4-triggered purchase
    segment: adjacent            # free device-tier subset vs all free
    trigger_eligibility: different
    surface: different           # standard internal paywalls vs seasonal sale splash/paywall
    mechanism: exact             # price increase on App subscription offer (arm C)
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent         # refunds
  segment_monetization_state: exact
  money_chain_link: exact
  platform: adjacent             # decisive iter iOS-only; price mechanism platform-agnostic
  level: L2
  transferable: >
    [fact] Decisive iteration: Total ARPU +1.38% (p=0.61); ARPPU +7.34%
    (p=0.001) eaten by charge CR -11% (p=0.003); refunds 14d +26.2% (p=0.006);
    verdict "price increase too high" (T3-01). [hypothesis] Arm C's +25%
    premium-plus price (plus removal of the intro offer) will shift structure
    rather than lift net revenue for free users; refunds are the guardrail to
    watch. Warning-level only (L2).
  not_transferable: >
    Magnitudes; the elasticity curve shape (unmeasured); anything about price
    DECREASES or web funnels — those point the other way (T3-02, T1-08) and
    are declared out of scope here.
  conflict: >
    Direction differs from T3-02/T1-08 (price decreases, positive) — different
    sub-class (decrease vs increase), not a contradiction within arm C's class.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact            # S3-S4
    segment: adjacent            # free new post-tour vs all free
    trigger_eligibility: adjacent
    surface: adjacent            # interstitial slot vs seasonal splash
    mechanism: adjacent          # interactive gamification vs passive thematic animation
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    Explicit L3 weak signal, guardrails/sizing only: [fact] non-skippable
    exposure bought x8 engagement at Android retention D1 -9.15% (p=0.012);
    significant relative lifts translated to small absolute increments
    (forecast +$474/day) (T1-07). Grounds the retention stop-rule and
    absolute-increment sizing check only; not an analog, not a verdict basis.
  not_transferable: >
    Any product conclusion about the animation (mechanism only adjacent);
    all magnitudes; new-post-tour segment specifics.
```

No conflict among the ranked analogs requires adjudication: T2-02 (L1) constrains measurement, T2-01 and T3-01 (L2) warn on different arms.

## Non-monetization effects to instrument

- **Retention (both directions):** downside — entry animation as friction (L3 signal T1-07: D1 −9.15% on forced exposure); upside — festive theming could raise holiday-period session frequency. Instrument D1/D7 retention and Explore-tab return rate per arm. Stop-rule: significant D1 retention drop in any arm → stop that arm.
- **Refunds/cancels (both directions):** downside on C — refunds up (T3-01 +26.2%); upside — a higher price self-selects intent, potentially fewer early cancels (mix-shift direction seen in T2-07 AOV/ARPPU). Instrument 14d refunds and cancels per arm, matured. Stop-rule: refunds significantly up on C → kill C.
- **Engagement / upper-funnel (both directions):** animation could delay time-to-content and depress Explore engagement, or the new banner could lift Explore interaction. Instrument time-to-first-content after Explore open, animation completion/abandon rate, banner CTR.
- **Cross-source shifts:** conversions redistributing from other paywall entry points (T2-02 ~−2%). Instrument per-source access and charge attribution, not only Total.

## 6. Design & measurement checklist

- **Fix the arithmetic before anything else:** required uniques per arm exceed DAU × planned days on both platforms; recompute duration (accounting for returning-user overlap) or the test is unreadable by design (P-12).
- **Rescope the goal metric** (P-11): primary on the sale-scenario funnel (banner/splash exposure → paywall → charge) and sale-source revenue; keep Total DAU→Charge and ARPU as guardrails with a cannibalization read.
- **Exposure gate:** count exposure at animation/splash render, not Explore open; run SRM at that gate (P-12, P-14).
- **Maturity** (P-13): the +7d trial and 14d refund reads extend past the sale window — commit to a final matured read, no early rollout on interim numbers (the T2-02 failure), and do not launch the second (New-Year) wave inside the measurement window.
- **Pre-register the C vs B contrast:** C differs from A by two mechanisms (creative + price/intro removal); only C vs B isolates price.
- **Fill the templates:** hypothesis statement, event/parameter table, Q&A — currently empty, which is itself the T2-02/T1-09 failure signature.

## 7. Changes that would most improve expected value

1. **Unbundle arm C** into its own properly powered price test (or drop it): it carries the highest downside (T3-01 refunds/elasticity, intro-offer removal) and currently contaminates a creative test.
2. **Re-power around the scenario metric** with realistic duration; if December cannot fit the required sample for three arms, run two arms (A/B) only.
3. **Add the delivery + maturity gates as launch criteria** — animation render events verified pre-launch, and a binding "no rollout before matured final read" rule.
