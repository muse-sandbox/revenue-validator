**Verdict: launch with changes** — the mechanism has a direct positive analog (T1-04, Android rolled out) and the design reuses proven reach mechanics, but the 14-day trial offer cannot mature inside the 8–12-day run, the goal metric is mis-scoped, and the offer choice repeats the weakest part of the direct predecessor (T1-02).

**Predicted outcome.** Layer conversion and trial starts up on both platforms (sign transfer from T1-04, T1-02). Net ARPU: plausibly positive on Android, where the splash displaces little real ad inventory; likely non-significant or negative on iOS, where it competes with real ad revenue and other paywalls (T1-04 iOS iter1 non-interstitial segment −24.7%; T1-02 cannibalization 34% iOS / 63% Android). A significant iOS Total-ARPU lift *within the run* would surprise me — 14-day trial charges will still be pending at read time, so any in-run ARPU "win" is suspect (P-13). A clean, matured Android surface-level win would not surprise me.

**Top risks & failure modes**
- **Immature trial economics:** 14-day trial + 8/12-day run means trial→charge is unreadable at the planned read; T1-08 and T1-10 both show conclusions flipping after maturity (P-13). Also, T1-02's extended 14-day trial pulled below-average-quality trials (trial→charge −13% iOS / −45% Android).
- **Cannibalization eats the increment on iOS:** replacing real ads (not just zero states) trades guaranteed ad revenue for uncertain subscription revenue (P-02; T1-04, T1-02). The cannibalization segment must be read as net of forgone ad revenue.
- **Ex-subscriber contamination:** "users without any subscription" includes ex-paid, who convert order-of-magnitude better (P-08); T1-02 iter1's headline lift was exactly this artifact (P-14). Ex-sub splits are planned — they must gate the headline, not decorate it.
- **Pre-paywall step loss:** splash → pre-paywall → paywall inserts an extra screen; T1-03's post-ad pre-paywall chain lost 96% on the first skippable screen (P-04). Banners already deep-link past it — the splash doesn't.
- **Forced 5-second exposure retention cost:** non-skippable exposure buys engagement at retention price (P-03; T1-07 Android D1 retention −9.15%, p=0.012). Risk to instrument with a stop-rule, not a blocker.

**Design & measurement checklist**
- **Goal scope (P-11):** Total free ARPU will be diluted by untouched revenue (T1-10: 83–88% untouched drowned a +58% surface effect). Add a surface-scoped co-primary (splash/banner-source net revenue) with its own SRM check; keep Total as guardrail.
- **Maturity gate (P-13):** commit pre-launch to a final read at run-end + 14 days; treat any read with pending-charge share >5% as interim.
- **Delivery gate (P-12):** verify both platforms actually launch and run full design days before interpreting (T1-09's iOS arm was unreadable).
- **Sizing audience mismatch:** the power table's audience is "users who failed to view an ad interstitial," but exposure is *all* free users daily — baselines ($0.127/$0.056) may not describe the exposed population. Also the MDE column is internally inconsistent (iOS lift 23.15% / MDE 0.017 vs Android 12.89% / 0.10). Recompute before launch.
- **Guardrails:** D1/D7 retention (stop-rule tied to the 5s close), tab engagement, per-user ad revenue displacement, SRM on exposure event.

**Changes that would most improve expected value**
1. **Fix the read before the run:** surface-scoped co-primary metric + matured final read; without this the experiment structurally cannot answer its own hypothesis.
2. **Add an intro-price arm instead of relying solely on the 14-day trial:** the positive component of the direct predecessor line was intro pricing of the same annual plan, while the generous trial was the weak component (T1-02; P-05/P-06 note).
3. **A/B the pre-paywall away:** deep-link the splash straight to the paywall (as banners do) in one arm, and make the close immediate in one arm to price the retention trade-off directly (T1-03, T1-07).

---

**Analogs** (ranked by closeness; conflict declared below)

```
analog:
  source: T1-02 (ab 6002/6128/6191, 2025-04..07; iter1 segment-contaminated; result mixed; killed)
  level: L1
  matched: [mechanism: exact — new-surface offer replacing ad interstitials + banner places;
            flow_stage: exact — S3–S4; surface: exact — same interstitial slot + banner slots;
            segment: exact — free App users (iter2 clean); offer: near-exact — extended 14d trial;
            money_chain: exact — exposure→paywall→trial→charge]
  mismatched: [trigger: adjacent — RH-02 adds guaranteed once-daily firing vs predecessor's config]
  transferable: sign + mechanism — the layer can lift ARPU (iter2 iOS +7.5%, p=0.029) but the
    increment is heavily cannibalized (34% iOS / 63% And) and the 14d trial recruits
    low-quality trials (trial→charge −13% iOS / −45% And). Ex-premium contamination
    fabricates headline lifts (iter1).
  not_transferable: all magnitudes (ARPU %, cannibalization shares — inventory-specific);
    iter1 numbers entirely (contaminated); the team's "novelty trap" interpretation.
  conflict: with T1-04 on decision (killed vs rolled-out) — see T1-04 card.
```

```
analog:
  source: T1-04 (ab 6359/6416/6428, 2025-07..08; result mixed; rolled out on Android)
  level: L1
  matched: [mechanism: exact — own full-screen unit replacing ad interstitials once/day (RH-02
            explicitly inherits this trigger and design parameters); flow_stage: exact — S3–S4;
            surface: exact — same slot; segment: exact — free (no Pro rights); metric: exact — ARPU goal]
  mismatched: [creative/offer: adjacent — video "Try for Free" vs paywall splash + pre-paywall chain;
            weakens transfer of the conversion path, not of reach mechanics]
  transferable: sign + mechanism — value comes from reach, not per-impression clicks (0.5–1%);
    positive where the unit replaces "nothing"/weak inventory (Android +17–19% sig., both
    iterations), washes out or turns negative where real ad revenue is displaced (iOS n.s.;
    non-exposed segment −24.7% in iter1).
  not_transferable: magnitudes (inventory-dependent); the Android conclusion does not
    license an iOS conclusion; creative-quality specifics.
  conflict: T1-04 rolled out where T1-02 was killed on the same slot/segment. Both L1.
    Hypothesized reason: offer/creative and net-increment quality differed (video→standard
    funnel vs generous-trial offer layer), and platform inventory determined the net.
    Per ranking rules I report both, do not average: expect the T1-04 pattern (Android net
    positive, iOS washed by displacement) and the T1-02 warning (trial quality, contamination)
    to both apply to RH-02.
```

```
analog:
  source: T1-03 (ab 6335, 2025-07; powered-null; killed)
  level: L2
  matched: [flow_stage: exact — S3–S4 post-ad-slot; surface: exact — interstitial context;
            segment: exact — free incl. ex-premium]
  mismatched: [mechanism: different — funnel-structure chain (pre-paywall → compare → paywall)
            rather than slot replacement; transfers as a warning about RH-02's
            splash → pre-paywall → paywall chain, not as a product conclusion]
  transferable: warning — each inserted screen is a multiplicative drop-off (96% loss on the
    first skippable screen; end-to-end conversion 0.07%) (P-04).
  not_transferable: the null itself (different mechanism); magnitudes; it does not condemn
    pre-steps in all contexts (T1-07's gamified pre-step lifted layer conversion).
```

```
analog:
  source: T1-07 (ab 7160/7187, 2026-03..07; result mixed; killed)
  level: L2
  matched: [flow_stage: exact — S3–S4; surface: exact — interstitial slot;
            mechanism: partial — skippability/frequency axis matches RH-02's 5s-delayed close]
  mismatched: [segment: different — free NEW post-tour vs all free; creative: different — gamified coupon]
  transferable: warning — restricting skip multiplies engagement and layer revenue but charged
    a measured retention price (Android D1 −9.15%, p=0.012); repeated daily shows add little
    beyond show #1 (P-01, P-03).
  not_transferable: all magnitudes; retention price measured on post-tour newcomers/Android —
    do not assume other segments pay the same; var2 internals (unexplained anomaly).
```

```
analog:
  source: T1-01 (ab 4845, 2024; inconclusive; killed)
  level: L1 by axes (mechanism/flow_stage/surface/segment exact), but result_class
    inconclusive ⇒ measurement lessons only, no product conclusion
  matched: [mechanism: exact — own screen into ad slot; flow_stage/surface/segment: exact]
  mismatched: [trigger_eligibility: different — passive no-fill-only with 1/day cap vs RH-02's
            guaranteed daily replacement; this is exactly the config RH-02 was designed to fix]
  transferable: measurement lesson — passive no-fill filling produced 4 accesses total; verify
    actual exposure volume early in the run before trusting any monetization read (P-01, P-12).
  not_transferable: everything product-level (inconclusive); says nothing about active
    replacement's potential.
```
