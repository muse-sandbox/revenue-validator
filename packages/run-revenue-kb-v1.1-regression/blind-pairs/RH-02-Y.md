## 1. Verdict

**Launch with changes.** The mechanic sits in the corpus's best-mapped family and the direct predecessor line showed a real ARPU signal on free users [T1-02], but the current design cannot deliver a valid read: the run (8–12 days) is shorter than the 14-day trial it sells, and it is powered only for lifts ~3× larger than the closest clean precedent.

## 2. Predicted outcome

[hypothesis] Directionally positive layer-attributed conversions with heavy cannibalization of other paywall sources and displaced ad revenue; Total free-ARPU lift plausibly in the mid-single digits (the clean predecessor read was iOS +7.5% [T1-02 iter2, fact]) — i.e., **below this design's MDE**, so the most likely outcome as designed is an inconclusive read. I would be surprised by a Total ARPU lift at or above the designed 23% (iOS), and equally surprised by a significant Total ARPU *decline*, since the daily splash largely replaces low-value ad exposure rather than an existing monetization surface.

## 3. Top risks & failure modes

- **Immature trial economics.** A 14-day free trial with an 8–12 day run means trial→charge and early-cancel money is almost entirely pending at read time; T1-02's generous 14d trial pulled below-average trial→charge (−13% iOS / −45% Android) [T1-02], and maturity has flipped conclusions before [T1-08, P-13].
- **Cannibalization + ad-revenue displacement eat the gross lift.** The same layer cannibalized 34% (iOS) / 63% (Android) of its conversions [T1-02]; where real ad inventory is displaced, the segment without layer accesses went −24.7% [T1-04]. Net increment, not layer revenue, is the value (P-02).
- **Underpowered for the realistic effect.** Designed lifts of 23.15%/12.89% vs a +7.5% clean precedent; baseline table audience ("failed to view an ad interstitial") does not match the actual all-free daily-exposure population (P-12).
- **Retention cost of forced daily exposure.** A 5-second-delayed close shown daily to every free user is a soft version of non-skippability, which cost Android D1 retention −9.15% (p=0.012) [T1-07, P-03]. Risk to instrument, not a blocker.
- **Ex-subscriber contamination of the "free" read.** "No active subscription" audiences have imported ex-premium revenue before (~37% of a fake lift) [T1-02 iter1, P-14]; the planned splits must be confirmatory, not exploratory.

## 4. Analogs

```yaml
analog:
  source: T1-02 (ab 6002/6128/6191; 2025-04..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact            # S3-S4 interstitial layer
    segment: exact               # free (iter2 clean read)
    trigger_eligibility: adjacent # ad-slot replacement vs once-daily first-open + ad-fail
    surface: exact               # interstitial slot + banner places
    mechanism: exact             # subscription offer instead of ads, generous 14d trial
    offer: adjacent              # Pro+ $39.99 extended 14d trial vs premium 14d free trial
    behavior: adjacent
    metric: exact                # ARPU
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact        # exposure -> trial start -> charge in both
  platform: exact
  level: L1
  transferable: >
    [fact] Clean iter2: iOS ARPU +7.5% (p=0.029), Android +4.94% (p=0.36);
    cannibalization 34% iOS / 63% Android; interstitial trial->charge below
    surface average (-13% iOS / -45% Android) [T1-02]. [interpretation] Source
    team read the killed decision as net-increment and trial-quality driven,
    not sign-driven. [hypothesis] For RH-02: sign likely positive on iOS free
    ARPU via the same mechanism, with material cannibalization and
    below-average trial quality on the new source.
  not_transferable: >
    All magnitudes (+7.5%, 34/63% cannibalization shares — config- and
    inventory-specific). Iter1 lifts (+24%/+13%) are a contamination artifact
    (P-14). result_class is mixed, so treat the directional transfer with the
    §2.3 validity caveat; the "novelty trap" rationale is interpretation.
  sizing_prior: >
    prior: clean Total-free ARPU lift order of magnitude ~5-8% iOS, smaller
    and noisier on Android — sizing only, argues the current MDE is ~3x too
    coarse.
```

```yaml
analog:
  source: T1-04 (ab 6359/6416/6428; 2025-07..08; SRM ok; mixed; rolled-out Android)
  axes:
    flow_stage: exact
    segment: different           # free + ex-paid mix vs fully free
    trigger_eligibility: exact   # RH-02 reuses this test's once-per-day trigger
    surface: exact               # interstitial slot
    mechanism: exact             # own full-screen unit replacing ads once daily
    offer: adjacent              # video "Try for Free" vs splash -> 14d trial
    behavior: adjacent
    metric: exact                # ARPU goal
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Android ARPU +17-19% significant in both iterations where the
    video replaced empty inventory; iOS iter2 +2.66% (p=0.43); iOS segment
    without interstitial accesses -24.7% [T1-04]. [hypothesis] Warning for
    RH-02: value scales with reach (P-01) and is pure increment only where
    the slot replaces "nothing"; where it displaces served ads, expect
    competition, so the ad-fail/zero-state placements should outperform the
    forced daily replacement per exposure.
  not_transferable: >
    Magnitudes (+17-19% is inventory-specific); the Android rollout
    conclusion does not transfer to iOS; mixed-segment audience differs from
    RH-02's free-only audience.
  conflict: >
    Apparent tension with T1-02's weak Android read (+4.94% n.s., 63%
    cannibalization): resolved by ad-inventory presence (P-02) — T1-04
    Android replaced no-fill, T1-02 replaced live placements. Not averaged;
    RH-02 replaces live ads, so T1-02 is the closer precedent for the daily
    slot, T1-04 for the zero-state placements.
```

```yaml
analog:
  source: T1-07 (ab 7160/7187; 2026-03..07; SRM ok; mixed; killed)
  axes:
    flow_stage: exact
    segment: adjacent            # free new post-tour vs all free
    trigger_eligibility: adjacent
    surface: exact               # interstitial slot
    mechanism: different         # gamified creative/skippability, not ad replacement
    offer: adjacent
    behavior: adjacent
    metric: exact
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Non-skippable variant: x8 engagement and +150-160% layer revenue,
    but Android D1 retention -9.15% (p=0.012); repeated exposures added
    almost nothing beyond show #1 [T1-07]. [hypothesis] Warning for RH-02:
    the 5s-delayed close is a partial forced exposure and may charge a
    retention price on Android; daily frequency beyond the first exposure
    likely adds little conversion (P-01, P-03).
  not_transferable: >
    All magnitudes; the retention penalty was measured on new post-tour
    Android users under full non-skippability — RH-02's 5s delay is milder;
    var2 funnel internals are flagged unreliable on the source page.
```

## Non-monetization effects to instrument

- **Retention (both directions):** daily forced splash may depress D1/D7 (negative, [T1-07]); removing annoying third-party ads may *improve* session quality and retention (plausible positive — the splash replaces an ad, not content). Instrument D1/D7/D14 retention and session length per arm; **stop-rule:** significant D1 retention drop ≥ ~5% on either platform.
- **Engagement / upper funnel:** tab views and tab→song funnel per arm (splash interrupts first open of day); watch for positive spillover from fewer ad interruptions. Stop-rule on significant tab-engagement decline.
- **Refunds/cancels:** generous 14d trial may raise low-intent trials and later cancels/refunds [T1-02]; instrument 14d cancel and refund rates with a pre-committed mature-read date; conversely, fewer accidental ad-driven purchases could *lower* refunds.
- **Ad-ecosystem side effects:** ad revenue per free user in both arms (displacement is a first-order term, not a guardrail afterthought), and ad-load error rates so the ad-fail trigger volume is verified (P-12).

## 6. Design & measurement checklist

- **Maturity:** extend duration or pre-commit the final read to ≥ trial length (14d) + charge lag past last enrollment; pending-trial share >5% blocks any final ARPU claim (P-13).
- **Goal metric:** keep Total free ARPU but pre-register the net-increment decomposition: layer revenue − cannibalized paywall revenue − displaced ad revenue (P-02, P-11); make the clean-free (ex-subscriber-excluded) read confirmatory (P-14).
- **Power:** recompute sample/duration for a realistic 5–8% MDE using baselines from the actual all-free exposed population, not the ad-fail subpopulation; current iOS MDE (23.15%) nearly guarantees an unresolved read (P-12).
- **SRM/activation:** exposure event in both arms is good; add SRM on the exposed population and per-placement delivery checks (daily slot vs ad-fail vs banners fire at designed rates).
- **Guardrails:** retention D1/D7, ad revenue floor, trial→charge quality vs surface average, 14d refunds.

## 7. Changes that would most improve expected value

1. **Re-power and lengthen the run** so the read matures past the 14-day trial window and can detect a ~5–8% lift — otherwise the experiment repeats T1-10's structural blindness.
2. **Pre-register net-increment economics** (ad displacement + cannibalization in the primary decision rule), since the predecessor's gross lift died exactly there [T1-02].
3. **Split daily-replacement vs zero-state-only exposure into separate arms or at least separate confirmatory reads** — the corpus says these have opposite increment profiles [T1-04 vs T1-02], and it directly answers the program's open frequency question.
