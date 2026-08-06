# Transfer classes registry

Formal registry of the generalization classes of Revenue KB V1.2. Compiled from
`packages/revenue-kb-v1.2/knowledge_base.md` §2.6 (GC-01…GC-06, KB-declared) and
from `packages/revenue-kb-v1.2/pattern_cards.md` for the families §2.6 does not
cover (GC-07…GC-13, derived here).

**This file is not evidence.** It is a routing and contradiction table. Every
claim must still cite the source cards (`knowledge_base.md` §4) and the pattern
cards. Never cite a GC id as the basis of a product conclusion.

## Verdict rules (normative for this file)

1. **TWO-SIDED** — the class has at least one source with a positive outcome AND
   at least one with a negative outcome. The counts are irrelevant: one positive
   against four negatives is still TWO-SIDED.
2. An **indeterminate** source carries no sign. It never makes a class
   one-sided, and it never resolves a contradiction. Sources are indeterminate
   when the KB assigns them no direction in this family, or when their outcome
   inside the family is mixed within the source itself.
3. **INSUFFICIENT** — fewer than three sources in the class. Signed sources are
   counted for this threshold; indeterminate sources are listed but not counted.
4. **ONE-SIDED** — three or more sources, all signed the same way.
5. Contradictions are preserved, never averaged. A source that points one way in
   one class and the other way in another class keeps both records.

## Violation warning

**A one-sided claim over a TWO-SIDED class is a violation of KB §2.5 (G2/G3).**
Any sentence that generalizes across the corpus about such a class must either
contain the literal phrase `evidence is mixed` with the transfer boundary
enumerated, or be narrowed to the evidenced sub-class and annotated per G1:

```
[scope: <sub-class>; ids: <ID>[, <ID>…]; not covered: <what the claim does NOT cover>]
```

ONE-SIDED does not license an unqualified universal either: it still requires
the G1 annotation, and the per-class caveats below list the within-source
counter-evidence that bounds it. INSUFFICIENT classes must not carry a
corpus-level generalization at all.

## Summary table

| id | label | verdict | positive | negative | indeterminate | signed n | origin |
|---|---|---|---|---|---|---|---|
| GC-01 | personalization | TWO-SIDED | T2-06 | T1-09, T3-01 | — | 3 | KB §2.6 |
| GC-02 | price change | TWO-SIDED | T1-08, T3-02, T3-06 | T3-01 | T1-10, T1-02 | 4 | KB §2.6 |
| GC-03 | offer structure | TWO-SIDED | T1-08, T2-05, T2-06, T3-05, T3-06 | T3-03 | T1-10, T1-02 | 6 | KB §2.6 |
| GC-04 | monetization surface added/replaced/removed | TWO-SIDED | T1-04, T2-01 | T1-01, T1-02, T1-03 | T2-02, T2-06 | 5 | KB §2.6 |
| GC-05 | creative / design / gamification | TWO-SIDED | T1-04, T1-07 | T1-09, T2-02 | T3-05 | 4 | KB §2.6 |
| GC-06 | funnel length | TWO-SIDED | T1-07 | T1-03, T2-07 | — | 3 | KB §2.6 |
| GC-07 | reach, frequency, forced exposure | TWO-SIDED | T1-04 | T1-01, T1-02 | T1-07, T1-09 | 3 | derived (P-01, P-03) |
| GC-08 | lifecycle segment targeting by monetization state | ONE-SIDED (positive) | T1-08, T2-05, T2-06 | — | T1-02, T1-09 | 3 | derived (P-08) |
| GC-09 | metric scope vs touched surface (method) | ONE-SIDED (positive) | T1-10, T1-08, T2-06 | — | — | 3 | derived (P-11) |
| GC-10 | delivery / exposure gate (method) | TWO-SIDED | T1-10, T1-09, T2-02 | T2-07 | — | 4 | derived (P-12) |
| GC-11 | maturity gate (method) | ONE-SIDED (positive) | T1-08, T1-10, T3-03, T2-02 | — | — | 4 | derived (P-13) |
| GC-12 | attribution artifacts / segment contamination (method) | TWO-SIDED | T1-02, T1-09, T2-05, T3-05 | T2-06 | — | 5 | derived (P-14) |
| GC-13 | decision-moment offer timing | INSUFFICIENT | T2-05, T1-08 | — | — | 2 | derived (P-09) |

Totals: 13 classes — 9 TWO-SIDED, 3 ONE-SIDED, 1 INSUFFICIENT.

For the method classes GC-09…GC-12, `positive` means "the gate fired: the
measurement condition changed, blocked or invalidated the read" and `negative`
means "the gate did not fire: the read survived the condition". These are
method claims, never product conclusions.

---

## GC-01 — personalization

```
generalization_class: GC-01
  label: tailoring the message, creative, offer or price to a user attribute or state (direction = did the personalization lift money)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial (T1-09); App splash (T2-06); standard App paywalls (T3-01)
    segment: free + ex-paid winback (T1-09); paying Pro without Courses/Sing (T2-06); free on mid-high device tiers (T3-01)
    mechanism: message/creative personalization with the offer held constant (T1-09); occasion-based offer personalization (T2-06); price personalization by a payment-capacity proxy (T3-01)
    flow_stage: S3-S4 (T1-09, T2-06); S6 purchase conditions with S2 segmentation (T3-01)
  outcome_positive: T2-06
  outcome_negative: T1-09, T3-01
  outcome_indeterminate: -
  related_patterns: P-10
```

- **Positive.** T2-06 — anniversary upsell splash on paying Pro users, offer
  personalized to the milestone (Pro+Courses bundle discount): significant on
  both platforms, rolled out, post-rollout ≈$1100/day iOS.
- **Negative.** T1-09 — song-personalized interstitial with offers unchanged:
  flat conversion, paywall→click halved; `result_class: inconclusive`, so this
  is a direction lesson only. T3-01 — device-tier price personalization:
  elasticity ate the increase, killed.
- **Boundary that explains the split (P-10).** What was personalized: the OFFER
  (positive) versus the wrapper around an unchanged offer, or a capacity proxy
  instead of the user's actual state (negative). Non-personalized creative
  changes are GC-05, not this class.

## GC-02 — price change

```
generalization_class: GC-02
  label: moving the price level up or down on any surface (direction = did the price change move net revenue)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial (T1-08, T1-10); web paywall + checkout (T3-02); iOS internal PRO paywalls (T3-06); standard App paywalls (T3-01)
    segment: ex-paid past the winback window (T1-08); web new + unconverted (T3-02); free (T3-06, T3-01, T1-10)
    mechanism: deep-discount instant (T1-08); entry-price decrease across the menu (T3-02); trial->instant at -40% (T3-06); increase by device tier (T3-01)
    flow_stage: S3-S4 (T1-08, T1-10); S5-S6 (T3-02); S6 (T3-06, T3-01)
  outcome_positive: T1-08, T3-02, T3-06
  outcome_negative: T3-01
  outcome_indeterminate: T1-10, T1-02
  related_patterns: P-07 (base + LIMITS), P-05
```

- **Positive.** T1-08 — $19.99 final offer on ex-paid: segment ARPU +241%
  (p=0.000), rolled out. T3-02 — web entry-price decrease: Access CR +68.9%,
  Charge CR +88.9%, revenue fact +4.18%, rolled out; post-rollout humbler
  (full-rollout revenue ≈ flat). T3-06 — iOS trial→instant at −40%: charge CR
  +16.4% (p=0.00), rolled out, ARPU itself n.s.
- **Negative.** T3-01 — App paywall increase on a device-tier proxy: decisive
  iteration Total ARPU +1.38% (p=0.61), refunds 14d +26.2%, killed.
- **Indeterminate.** T1-10 — $29.99 discounted instant on the interstitial:
  `inconclusive`, maturity failed (pending 59–79%), stopped with "hold and
  re-run"; §2.6 assigns it no direction. T1-02 — the card notes intro pricing of
  the same annual plan was the positive part of iter 1–2, but §2.6 assigns T1-02
  only to GC-04 (negative); no price direction is declared for it.
- **Boundary.** Direction of the move (decrease vs increase), platform
  elasticity (Android washed out where iOS won — T1-10, P-05), and segment
  intent (high-intent ex-paid vs free). P-07 explicitly forbids transferring
  "price is a dead lever" to web funnels, to decreases, or to discount-instants.

## GC-03 — offer structure

```
generalization_class: GC-03
  label: changing what is offered (plan menu composition, trial vs instant, intro offers, bundle upsells) (direction = did the structural change earn money)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial (T1-08, T1-10); splash + Explore banner (T2-05, T2-06); web paywall + offer chain (T3-05, T3-03); iOS internal paywalls (T3-06)
    segment: ex-paid (T1-08); canceling at autorenew-off (T2-05); paying (T2-06); web new + unconverted (T3-03, T3-05); free (T3-06)
    mechanism: trial -> instant / intro offer (T1-08, T3-05, T3-06); immediate offer at the cancel moment (T2-05); bundle upsell (T2-06); adding plans to a menu (T3-03)
    flow_stage: S3-S4 (T1-08, T2-06); S8 -> S3 (T2-05); S5-S6 (T3-03, T3-05); S6 (T3-06)
  outcome_positive: T1-08, T2-05, T2-06, T3-05, T3-06
  outcome_negative: T3-03
  outcome_indeterminate: T1-10, T1-02
  related_patterns: P-05, P-06, P-09
```

- **Positive.** T1-08, T2-05, T2-06, T3-05 (intro iteration 6875: ARPU
  +12.1–19.2%, trial→charge +28.9–32%), T3-06 — all rolled out.
- **Negative.** T3-03 — adding 3m/$19.99 and 6m/$24.99 to the web menu:
  members→subscribers −11.08% (p=0.028), forecast −$918…−$1408/day, killed.
- **Indeterminate.** T1-10 (inconclusive, undelivered design); T1-02 (offer
  component Pro+ $39.99/yr with an extended 14d trial — §2.6 records T1-02 only
  under GC-04).
- **Boundary (P-06 vs P-05).** Adding an option to an existing menu behaves as a
  substitute (negative, web only — App menus untested). Replacing the trial step
  with an instant/intro charge behaves as a structure shift toward immediate
  payment (positive, iOS + web post-trial chains). Inside T3-05 itself the paid
  trial $0.99 failed twice — the positive is the intro/instant sub-class, not
  "offer structure changes" as a family.

## GC-04 — monetization surface added, replaced or removed

```
generalization_class: GC-04
  label: monetization surface added, replaced or removed (direction = did the surface carry net incremental money; removal tests count positive when turning the surface OFF harmed revenue)
  verdict: TWO-SIDED
  bounds:
    surface: interstitial slot (T1-01, T1-02, T1-03, T1-04); sale banner + splash (T2-01, T2-02); anniversary splash (T2-06)
    segment: free, incl. mixed free + ex-paid (T1-02 iter1 contaminated, T1-04)
    mechanism: new-surface replacing ad inventory or no-fill (T1-01..T1-04); surface OFF as a negative test (T2-01)
    flow_stage: S3-S4 throughout
  outcome_positive: T1-04, T2-01
  outcome_negative: T1-01, T1-02, T1-03
  outcome_indeterminate: T2-02, T2-06
  related_patterns: P-01, P-02
```

- **Positive.** T1-04 — video interstitial where it replaced "nothing":
  Android ARPU +17–19% significant, rolled out on Android. T2-01 — turning the
  sale banner + splash OFF cost ARPU −11.6% iOS / −26% Android (p=0.036): the
  surfaces carried real incremental money.
- **Negative.** T1-01 (reach ≈ zero, 4 accesses, inconclusive), T1-02 (34%/63%
  cannibalization, killed), T1-03 (new-scenario conversion 0.07%, powered-null).
- **Indeterminate.** T2-02 — seasonal surfaces with emotional design,
  `inconclusive`, rolled out early; §2.6 records it under GC-05 only. T2-06 —
  the control had NO splash, so it is also a surface addition, but §2.6 assigns
  it to GC-01/GC-03; no GC-04 direction is declared.
- **Boundary (P-02).** Whether the new surface displaces monetized inventory
  (iOS ads and other paywalls → cannibalization is the default) or fills empty
  space (Android → pure increment). Seasonal surfaces do not transfer to
  permanent layers. Web surfaces are outside P-01/P-02 evidence entirely.

## GC-05 — creative, design or gamification change

```
generalization_class: GC-05
  label: creative, design or gamification change on an existing surface, personalization aside (direction = did the creative/design change move the funnel)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial slot (T1-04, T1-07, T1-09); sale splash + banner + paywall-entry animation (T2-02); web paywall UI (T3-05, indeterminate)
    segment: free (T1-07 new post-tour, T2-02); free + ex-paid (T1-04, T1-09)
    mechanism: video creative (T1-04); gamified scratch coupon (T1-07); song creative (T1-09); emotional design with sound/haptics (T2-02)
    flow_stage: S3-S4; S5-S6 for the indeterminate web UI iterations
  outcome_positive: T1-04, T1-07
  outcome_negative: T1-09, T2-02
  outcome_indeterminate: T3-05
  related_patterns: P-03, P-10 (scope boundary)
```

- **Positive.** T1-04 — creative quality mattered (the chords variant was
  strictly worse); Android ARPU +17–19%. T1-07 — gamified scratch coupon: iOS
  var2 ARPU +26.5% (p=0.011), interstitial segment +72.7%.
- **Negative.** T1-09 — creative lifted attention, halved paywall→click
  (inconclusive; direction lesson only). T2-02 — emotional seasonal design: all
  money metrics n.s., post-rollout forecast iOS −$1716/day (inconclusive).
- **Indeterminate.** T3-05 — earlier web UI iterations rejected on guardrails
  (print AOV −32.2%, cancels +37.4%, refunds +72.3%); §2.6 records T3-05 under
  GC-03 only.
- **Boundary (P-03, P-10).** Engagement/attention lifts do not imply purchase
  lifts; T1-07's monetization win came with Android D1 retention −9.15%
  (p=0.012). Personalized wrappers belong to GC-01 — do not merge the two
  classes into a "wrapper changes" universal.

## GC-06 — funnel length

```
generalization_class: GC-06
  label: inserting or removing a step between the trigger and the offer (direction = did the extra step help)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial slot (T1-07); post-ad interstitial chain (T1-03); feature paywall (T2-07)
    segment: free new post-tour (T1-07); free incl. ex-premium (T1-03); free never-subscribed (T2-07)
    mechanism: gamified pre-step before the offer (T1-07); pre-paywall + compare table after an ad (T1-03); 10s feature demo + timer after feature tap (T2-07)
    flow_stage: S3-S4 (T1-07, T1-03); S1-S3 feature-gate (T2-07)
  outcome_positive: T1-07
  outcome_negative: T1-03, T2-07
  outcome_indeterminate: -
  related_patterns: P-04
```

- **Positive.** T1-07 — a gamified step inserted before the offer in a neutral
  context lifted layer conversion on both platforms (the card was still killed
  on absolute increment and the retention guardrail).
- **Negative.** T1-03 — 96% drop on the first skippable pre-paywall after an ad,
  powered-null on goal. T2-07 — a 10-second demo after the user tapped the
  feature: access CR −36% iOS / −28.5% Android, significant-negative.
- **Boundary (P-04, T1-03 transfer bounds).** The split is intent: a step
  inserted AFTER a captured intent trigger is a multiplicative drop-off; a step
  shown BEFORE intent, in a neutral context, is the positive case and remains
  largely untested. "Extra steps always lose" is a violation of this class.

## GC-07 — reach, frequency and forced exposure (derived)

```
generalization_class: GC-07
  label: how much exposure an App S3-S4 surface gets - reach, repeat frequency, capping, removal of the skip option (direction = did more or forced exposure earn net money)
  verdict: TWO-SIDED
  bounds:
    surface: App interstitial layer and splashes (S3-S4)
    segment: free; free + ex-paid; new post-tour for the forced-exposure arm
    mechanism: no-fill-only passive filling vs guaranteed placement; repeat shows; non-skippable exposure
    flow_stage: S3-S4 only - web funnels and S5-S6 internals are NOT covered (P-01 ban)
  outcome_positive: T1-04
  outcome_negative: T1-01, T1-02
  outcome_indeterminate: T1-07, T1-09
  related_patterns: P-01, P-03
  note: signs derived from pattern cards; not declared in KB 2.6
```

- **Positive.** T1-04 — value came from reach, not click quality (click rate
  0.5–1% of views, Android ARPU +17–19%).
- **Negative.** T1-01 — no-fill-only with a 1/day cap produced 4 accesses over
  the whole run; everything n.s. T1-02 — the first exposure does 60–87% of the
  layer's work, so additional frequency buys little.
- **Indeterminate.** T1-07 — mixed within the source: repeated splashes added
  almost nothing, while non-skippable exposure gave ×8 engagement and +150–160%
  layer revenue at Android D1 retention −9.15% (p=0.012). T1-09 — show #1 = 50–60%
  of layer conversions, but the case is `inconclusive` and supporting only.
- **Boundary.** Reach numbers are config-specific (caps, triggers) and never
  transfer as magnitudes. More exposure is not a free lever: P-01 does not
  license unlimited frequency, and the retention price was measured only on
  Android, new post-tour users.

## GC-08 — lifecycle segment targeting by monetization state (derived)

```
generalization_class: GC-08
  label: targeting a segment defined by monetization state (ex-paid, canceling, paying) with a tailored App offer (direction = did targeting that segment earn money)
  verdict: ONE-SIDED (positive)
  bounds:
    surface: App interstitial (T1-08); splash + Explore banner (T2-05, T2-06)
    segment: ex-paid past the winback window; canceling at autorenew-off; paying Pro at milestones
    mechanism: deep-discount instant; immediate offer at the cancel decision; milestone bundle upsell
    flow_stage: S3-S4 and S8 -> S3
  outcome_positive: T1-08, T2-05, T2-06
  outcome_negative: -
  outcome_indeterminate: T1-02, T1-09
  related_patterns: P-08, P-09
  note: signs derived from pattern cards; not declared in KB 2.6
```

- **Positive.** T1-08 (+241% segment ARPU), T2-05 (iOS ARPU +49.3%, charge CR
  +67.3%), T2-06 (significant on both platforms) — the three largest significant
  segment wins in the corpus, all rolled out.
- **Indeterminate.** T1-02 — ex-subscribers up to 13×, but discovered through a
  segmentation bug (direction only). T1-09 — ex-paid ~20× better per member, but
  `inconclusive`/supporting.
- **Caveats that bound the one-sidedness.** Within-source counter-evidence
  exists and must be carried: T2-05 iter2 Android expensive plans −55% ARPU
  ("keep cheap control on Android"); T2-05 iter3 invalidated by a
  subscription-tracking bug; T1-08 iOS diffuse dilution −$702/day on non-winback
  users. The 13×/20× figures are direction indicators, never sizing priors.
- **Hard rule.** free → ex-paid and ex-paid → free transfers are forbidden by
  the mandatory minimum (KB §2.3, item 4), independently of this class.

## GC-09 — metric scope vs touched surface (method, derived)

```
generalization_class: GC-09
  label: whether the goal metric was scoped to the touched surface or segment (direction = did mis-scoping change the read)
  verdict: ONE-SIDED (positive)
  bounds:
    surface: any surface- or segment-scoped treatment
    segment: any
    mechanism: measurement design, not an intervention
    flow_stage: any
  outcome_positive: T1-10, T1-08, T2-06
  outcome_negative: -
  outcome_indeterminate: -
  related_patterns: P-11
  note: method gate; never usable as a product conclusion
```

- T1-10 — Total ARPU flat-negative (−5.4%, p=0.61) while the touched surface read
  +58.14% net revenue; 83–88% of revenue untouched.
- T1-08 — segment win (+241%, p=0.000) real and rolled out while the Total lift
  lost significance after control trials matured (+9.3%, p=0.40).
- T2-06 — goal correctly scoped to anniversary members → upsell %; the +3910%
  figure is a near-zero control base, not magic.
- **Boundary.** This does not license ignoring Total and guardrail metrics
  (T1-08 iOS dilution −$702/day); surface metrics inherit surface-selection bias
  and need their own SRM check.

## GC-10 — delivery / exposure gate (method, derived)

```
generalization_class: GC-10
  label: whether the treatment was delivered as designed - arms live, platforms launched, duration and sample reached (direction = did under-delivery invalidate or block the read)
  verdict: TWO-SIDED
  bounds:
    surface: any
    segment: any
    mechanism: delivery/instrumentation, not an intervention
    flow_stage: any
  outcome_positive: T1-10, T1-09, T2-02
  outcome_negative: T2-07
  outcome_indeterminate: -
  related_patterns: P-12
  note: method gate; never usable as a product conclusion
```

- **Gate fired.** T1-10 — 9 of 15/20 design days, 2 of 3 arms, churn/refund
  unreadable, ended inconclusive-stopped. T1-09 — iOS effectively never launched
  (real volume 3 days), platform read declared unreadable. T2-02 — sample a
  fraction of design (iOS 20,329 vs 216,622) plus early rollout on interim
  reads, final read permanently lost.
- **Gate did not fire.** T2-07 — significant negatives survived heavy
  undersampling (access CR −36%, p=0.00) and the experiment was correctly
  killed on them.
- **Boundary.** The gate governs the interpretation of nulls and positives, not
  of clear harm. "Under-delivered experiments cannot be read" is a one-sided
  claim over a TWO-SIDED class and is a violation.

## GC-11 — maturity gate (method, derived)

```
generalization_class: GC-11
  label: whether trial windows and pending charges had matured before the read (direction = did immaturity change or block the conclusion)
  verdict: ONE-SIDED (positive)
  bounds:
    surface: any trial-bearing funnel
    segment: any
    mechanism: read timing, not an intervention
    flow_stage: S6-S8 money chain
  outcome_positive: T1-08, T1-10, T3-03, T2-02
  outcome_negative: -
  outcome_indeterminate: -
  related_patterns: P-13
  note: method gate; never usable as a product conclusion
```

- T1-08 — the Total ARPU lift disappeared once control trials matured.
- T1-10 — pending 14d charges 59–79% by arm made churn/refund unreadable.
- T3-03 — pending 24.0%/15.7% with an explicit "re-check churn and refund in
  ~2 weeks".
- T2-02 — early rollout on interim reads forfeited the final read.
- **Boundary.** No counter-case in the corpus, but the gate is about the read,
  not about the product: a matured read does not by itself validate anything,
  and the corpus contains no case where immaturity was shown to be harmless.

## GC-12 — attribution artifacts and segment contamination (method, derived)

```
generalization_class: GC-12
  label: whether an observed effect was an artifact of attribution, segment contamination or a tracking bug (direction = did the artifact fabricate or destroy the read)
  verdict: TWO-SIDED
  bounds:
    surface: any
    segment: any, especially newly instrumented or low-volume sources
    mechanism: instrumentation and cohort definition, not an intervention
    flow_stage: any
  outcome_positive: T1-02, T1-09, T2-05, T3-05
  outcome_negative: T2-06
  outcome_indeterminate: -
  related_patterns: P-14
  note: method gate; never usable as a product conclusion
```

- **Artifact drove the number.** T1-02 — iter1 +24%/+13% was ex-premium
  contamination (~37% of revenue); the clean iter2 read was 2–3× smaller.
  T1-09 — a visible ×4.6 winback lift was an attribution artifact. T2-05 iter3 —
  a subscription-tracking bug dropped −30% of conversions. T3-05 — 2% of intro
  subscriptions wrongfully charged as weekly.
- **Artifact did NOT drive the number.** T2-06 — a targeting bug showed the
  splash to trial users but provably contributed 6 iOS / 26 Android
  subscriptions.
- **Boundary.** Bugs must be quantified, not assumed decisive. "Any striking
  lift on a new source is an artifact" is a one-sided claim over a TWO-SIDED
  class and is a violation.

## GC-13 — decision-moment offer timing (derived)

```
generalization_class: GC-13
  label: showing a targeted offer at a lifecycle decision moment, sequenced after the standard funnel (direction = did the decision-moment offer convert)
  verdict: INSUFFICIENT
  bounds:
    surface: splash + Explore banner (T2-05); App interstitial (T1-08)
    segment: canceling at autorenew-off (T2-05); ex-paid past the winback window (T1-08)
    mechanism: immediate alternative offer at the moment of re-evaluation, sequenced after the standard flow
    flow_stage: S8 -> S3
  outcome_positive: T2-05, T1-08
  outcome_negative: -
  outcome_indeterminate: -
  related_patterns: P-09
  note: only two signed sources - no corpus-level generalization may be made over this class; both sources also appear as positives in GC-03
```

- The two measured moments are the autorenew-cancel moment (T2-05) and
  winback-window exhaustion (T1-08). Every other "decision moment" is untested
  in this corpus (P-09 scope line).
- Sequencing is part of the evidenced mechanism, not decoration: the T1-08 final
  offer was shown only after the winback interstitial and not earlier than the
  next day, which structurally protected the standard winback.
- Android asymmetry applies here as in GC-08 (T2-05 iter2 expensive plans
  −55% ARPU); magnitudes are iOS-specific.

---

## Compilation notes

- GC-01…GC-06 reproduce the KB §2.6 direction table without change: no source
  was added to or removed from a declared sign. Everything added for those
  classes is either `outcome_indeterminate` (sources the KB assigns no direction
  in that family) or bounds/prose drawn from the source cards.
- GC-07…GC-13 are derived here from pattern cards P-01, P-03, P-08, P-09,
  P-11…P-14, which §2.6 does not cover. Their signs are this registry's
  reading of the source cards, not KB-declared directions. When a G3 check
  disagrees with a derived class, §2.6 wins.
- Pattern cards already folded into KB classes: P-02 → GC-04, P-04 → GC-06,
  P-05 → GC-02/GC-03, P-06 → GC-03, P-07 → GC-02, P-10 → GC-01.
- Sources carrying opposite signs in different classes: T1-02 (negative in
  GC-04 and GC-07, positive in GC-12, indeterminate in GC-02/GC-03/GC-08),
  T1-09 (negative in GC-01 and GC-05, positive in GC-10 and GC-12,
  indeterminate in GC-07), T2-06 (positive in GC-01/GC-03/GC-08/GC-09, negative
  in GC-12, indeterminate in GC-04). These records are kept
  separate on purpose; a source's sign in one class says nothing about its sign
  in another.
