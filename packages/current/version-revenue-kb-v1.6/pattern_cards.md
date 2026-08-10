# Revenue Knowledge Base V1.2 — Pattern Cards (FLOW-593; corpus unchanged from FLOW-578)

V1.2 changes ONLY the scope wording of pattern headings/claims (and, where a
scope was implicit, of the applicability and transfer-ban lines): every card
title now names exactly the sub-class its facts cover, so a title can no
longer license a generalization wider than its own evidence. No fact, no
figure, no source ID and no transfer ban was added, removed or weakened.

Patterns are organized by product causality along the Revenue User Flow
(S1 action → S2 eligibility → S3 surface → S4 exposure → S5 intent/checkout →
S6 trial/purchase → S7 charge → S8 lifecycle → S9 net revenue), not as a list of
experiments. Every pattern card states: the causal claim, the mechanism, the
measured facts (each tagged with a source ID from `knowledge_base.md` and its
validity class), where it applies, and where transfer is FORBIDDEN.

Global transfer rules (inherited from the relevance model, see
`knowledge_base.md` § "Closeness model"):

- Only the **sign and the mechanism** of an effect ever transfer. Effect
  magnitudes, baselines and conversion rates transfer ONLY as explicitly
  labelled sizing priors.
- Facts from cases with `result_class: inconclusive` ground **measurement
  lessons only**, never product conclusions.
- A pattern must not be applied outside its `applicability` scope without
  flagging the transfer as unsupported.
- **Title = evidence scope.** A card's heading names exactly the sub-class its
  facts cover. Reading a heading as a claim about a wider family (all
  surfaces, all price changes, all wrappers, all personalization, all
  decision moments…) is an unsupported transfer, even when the wider claim
  sounds like a paraphrase of the title.
- **No unqualified universals.** Any statement that generalizes across the
  corpus ("never / always / have not … in this corpus") must carry an
  explicit scope annotation per `knowledge_base.md` §2.5; when the cited
  cases point in conflicting directions inside the same class, the answer
  must state `evidence is mixed` and enumerate the transfer boundaries
  instead of asserting a one-sided universal. Several cards below
  (P-07, P-10) contain counter-examples to their own headline direction —
  that is the normal state of this corpus, not an exception.

---

## A. Exposure & reach (S3–S4)

### P-01 Reach is the binding constraint of an App S3–S4 exposure surface (interstitial layer, splash, banner)

- **Claim (scope: App S3–S4 exposure surfaces; all facts below are from that
  sub-class):** such a surface moves money only in proportion to the
  audience it actually reaches; per-impression conversion quality is secondary.
- **Mechanism:** surface revenue = reach × per-exposure conversion; in practice
  reach varies by orders of magnitude (no-fill-only vs guaranteed placement)
  while per-exposure CR varies by tens of percent.
- **Facts:**
  - Passive filling of no-fill ad slots (1/day cap) produced 4 accesses over a
    whole experiment; every monetization diff insignificant (ARPU −10.5%,
    p=0.67) [T1-01, inconclusive/killed — measurement lesson: reach gates
    everything].
  - Video interstitial value came from reach, not clicks: click rate 0.5–1% of
    views, yet Android ARPU +17–19% (significant) where the video replaced
    "nothing" [T1-04, mixed/rolled-out].
  - First exposure does 60–87% of the layer's work [T1-02, mixed/killed];
    show #1 yields 50–60% of layer conversions [T1-09, inconclusive/killed —
    supporting observation]; repeated splashes add almost nothing [T1-07,
    mixed/killed].
- **Applicability:** App offer layers and splashes (S3–S4), free and ex-paid
  segments; any pre-launch reach/frequency sizing.
- **Transfer bans:** does not justify unlimited frequency (see P-03 retention
  trade-off); reach numbers are config-specific (caps, triggers) and never
  transfer as magnitudes. Scope of the ban: the evidenced class is App S3–S4
  exposure surfaces only — web funnels, checkout and S5–S6 paywall internals
  are NOT covered by this card.

### P-02 For an App S3–S4 monetization surface, value = net increment; cannibalization of existing sources is the default, and an off-test measures it

- **Claim (scope: App S3–S4 monetization surfaces; all facts below are from
  that sub-class):** a new or changed surface takes a large share of its conversions
  from existing sources; its true value is the net increment, which a
  turn-off (negative/holdout) test measures directly and cheaply.
- **Mechanism:** monetization surfaces compete for the same purchase intent;
  users redistribute across paywall entry points.
- **Facts:**
  - Offer-instead-of-ads layer cannibalized 34% (iOS) / 63% (Android) of its
    conversions from other sources [T1-02, mixed/killed].
  - Same video creative: pure increment on Android (no ad interstitials to
    displace) vs iOS iter1 segment without interstitial accesses −24.7%
    (competition with real ad revenue and other paywalls) [T1-04,
    mixed/rolled-out].
  - Turning sale banner + splash OFF: ARPU −11.6% iOS (p=0.036) / −26% Android
    (p=0.036) — conversion did NOT fully redistribute; the surfaces carry real
    incremental value; splash alone off ≈ no significant loss [T2-01,
    significant-negative/killed].
  - Seasonal emotional-design scenario: cannibalization ≈ −2% of other
    sources; post-rollout forecast negative (iOS −$1716/day) despite a
    significant splash-view CR lift [T2-02, inconclusive/rolled-out —
    measurement lesson].
- **Applicability:** any new S3 surface, any surface removal/gating decision,
  pre-launch estimates of incremental revenue; the off-test recipe applies to
  any established surface.
- **Transfer bans:** cannibalization shares are platform- and
  inventory-specific (depend on whether ads/other paywalls exist to displace);
  seasonal-surface results do not transfer to permanent layers without a
  dedicated test. Scope of the ban: the evidenced class is App S3–S4
  surfaces — web surfaces are NOT covered by this card.

### P-03 On S3–S4 creative/design/gamification changes, attention/engagement ≠ purchase intent; where the skip option was removed, forced exposure bought engagement at a measured retention cost

- **Claim (scope: creative/design/gamification changes on App S3–S4 surfaces;
  the retention-cost half rests on ONE measured arm — Android non-skippable,
  new post-tour users):** lifting attention metrics (views, clicks into the funnel,
  engagement with a gimmick) does not by itself lift purchases; removing the
  skip option multiplies engagement but charged a retention price where measured.
- **Mechanism:** curiosity and forced interaction push users into the funnel
  without changing their willingness to pay; annoyance accumulates into churn.
- **Facts:**
  - Song-personalized creative: pauses→paywall slightly up, paywall→click
    halved (7.25%→3.90%) — "wins curiosity but loses intent" [T1-09,
    inconclusive/killed — measurement/direction lesson].
  - Non-skippable scratch coupon: ×8 engagement into the funnel, +150–160%
    layer revenue, but Android retention D1 −9.15% (p=0.012) [T1-07,
    mixed/killed].
  - Emotional seasonal design: significant CR→Splash View (p=0.001) with no
    significant money effect (scenario ARPU p=0.060; total ARPU n.s.) [T2-02,
    inconclusive/rolled-out — measurement lesson].
- **Applicability:** creative/gamification/design changes on S3–S4 surfaces;
  frequency and skippability decisions.
- **Transfer bans:** does not prove creative never matters (video creative
  quality mattered in T1-04: chords variant strictly worse); the retention
  price was measured on new post-tour users and on Android — do not assume
  other segments/platforms pay the same price.

---

## B. Funnel structure (S3 → S5)

### P-04 In App funnels, a step inserted AFTER the intent trigger and before the offer is a multiplicative drop-off; captured intent must not be deferred

- **Claim (scope: App funnels, steps inserted after the user's trigger
  moment; steps shown BEFORE intent are not covered — see the transfer
  bans):** inserting any step (pre-paywall, demo pause, comparison screen)
  between the user's trigger moment and the offer multiplies the funnel by a
  large loss factor; when the user has already shown feature intent, delay
  destroys conversion.
- **Mechanism:** each screen is an exit opportunity; intent decays in seconds;
  in a post-ad context the user is additionally irritated.
- **Facts:**
  - Post-ad chain (pre-paywall → compare table → paywall): 96% drop on the
    first skippable screen, new-scenario conversion 0.07%, powered-null on
    goal [T1-03, powered-null/killed].
  - 10-second feature demo before the paywall at the moment of feature tap:
    access CR −36% iOS (p=0.00) / −28.5% Android (p=0.008); losses along the
    whole funnel; beginners hit hardest (−42.1%) [T2-07,
    significant-negative/killed].
- **Applicability:** any funnel-lengthening idea on S3–S5, feature-gate
  paywalls, post-ad monetization, "educate before selling" concepts.
- **Transfer bans:** does not rule out preview/demo content shown BEFORE
  intent (neutral context) — that variant is untested; the post-ad irritation
  explanation is the team's interpretation, not isolated experimentally.

---

## C. Offer structure & price (S5–S6)

### P-05 Instant-vs-trial: dropping the trial for an immediate discounted charge shifted conversion structure profitably where measured — high-intent iOS audiences and the web post-trial-start offer chain (Android is outside the scope, see transfer bans)

- **Claim (scope: the measured sub-classes named in the heading):** replacing a trial with an immediate discounted purchase increases
  buyers and removes early-cancel churn, at the price of a lower average
  check; net effect was positive where tested on iOS.
- **Mechanism:** the trial→charge conversion step loses ~40–60% of trials;
  an instant charge collects committed users at once and self-selects
  higher-intent buyers (early cancels −42–46%).
- **Facts:**
  - iOS internal PRO paywalls, trial→instant (−40% price, $24.99/yr): charge
    CR +16.4–21.4% (p=0.00), AOV/ARPPU −9.8–13.2%, 14d cancels −42.2–45.5%
    (p=0.00), ARPU +5% n.s.; forecast +$353/day vs plan $500 [T3-06,
    mixed/rolled-out].
  - Deep-discount instant $19.99 on ex-paid users who exhausted the winback
    window: segment ARPU +241% (p=0.000), buyers +365.6%; the "final offer"
    converts to 100% instant purchases [T1-08,
    significant-positive/rolled-out].
  - Web intro/instant offer after trial start (best iteration 6875): ARPU
    +12.1–19.2% (significant), trial→charge +28.9–32%, 14d cancel −19–20%
    [T3-05, mixed/rolled-out]. Paid trial $0.99 as a "cheap instant" failed
    twice (ARPU −23.8%, stopped; −6.66% n.s.) [T3-05].
- **Applicability:** iOS paywalls and offer chains with an existing trial
  step; ex-paid high-intent segments; web post-trial-start offer chains.
- **Transfer bans:** Android showed a different price elasticity — the same
  discount logic washed out (see P-07); LTV/renewal of the discount cohort is
  an open risk explicitly under post-rollout monitoring [T3-06] — long-term EV
  is conditional, not proven; discount size is a parameter, not a constant;
  free-audience transfer of the ex-paid deep-discount result is forbidden
  (segment states differ, see P-08).

### P-06 A new plan added to a WEB plan menu is a substitute, not an addition

- **Claim (scope: web plan menus, S5–S6; App paywall menus are untested in
  this corpus and NOT covered):** adding a cheaper/shorter plan to an existing menu shifts existing
  buyers into it (revenue down) more than it recruits new payers.
- **Mechanism:** menu anchoring: buyers re-sort to the cheapest acceptable
  option; total purchase intent barely grows ("substitutes, not additions" —
  wording from the source page).
- **Facts:**
  - Adding 3m/$19.99 and 6m/$24.99 plans to the web menu: members→subscribers
    −11.08% (p=0.028), buyers −11.90% (p=0.038) in the 3-plan arm; forecast
    −$918…−$1408/day; short plans cannibalized annual instant subscriptions
    [T3-03, significant-negative/killed].
  - Three-plan menus in the Flo-paywall series: "choice overload" suspected on
    the source page; plan-menu iterations lost while the intro-offer
    iteration won [T3-05, mixed/rolled-out].
- **Applicability:** web plan menus (S5–S6); any idea "lower the entry price
  by adding a plan".
- **Transfer bans:** does not transfer to App paywalls (untested there in this
  corpus); does not contradict intro pricing of the SAME annual plan (that is
  a different mechanism — price framing, not menu extension — and won in
  earlier iterations of the offer-instead-of-ads line [T1-02 iter 1–2]);
  trial-mechanics inside the new plans were positive (trial→charge +21–26%)
  but did not compensate the annual-revenue loss [T3-03].

### P-07 An App-paywall price INCREASE on a payment-capacity proxy segment moved structure, not net revenue — WITH EXPLICIT LIMITS (mandatory pattern: the "price doesn't move revenue" claim is bounded to that sub-case)

- **Claim (base pattern; scope: App-paywall price INCREASES on a
  payment-capacity proxy segment — price decreases, web funnels and
  discount-instant mechanics are explicitly NOT covered, see LIMITS):** on App paywalls, raising prices for a
  "payment-capable" proxy segment shifted the ARPPU/conversion structure with
  ≈zero net revenue effect; elasticity ate the increase.
- **Mechanism:** conversion falls roughly in proportion to the price increase;
  device tier is too weak a proxy for willingness to pay to break the
  trade-off.
- **Facts:**
  - Device-tier price increase, decisive iOS iteration at ~4.4× design
    sample: Total ARPU +1.38% (p=0.61); tour ARPPU +7.34% (p=0.001) eaten by
    charge CR −11% (p=0.003); refunds 14d +26.2% (p=0.006); "price increase
    too high" [T3-01, mixed/killed].
- **LIMITS of the pattern (do NOT overgeneralize "price doesn't move ex/net
  revenue"):**
  1. **Web entry-price DECREASE produced a real positive** through volume and
     the upsell chain: Access CR +68.9%, Charge CR +88.9%, trial→charge
     +18.3% (all p=0.00), revenue fact +4.18%; retention slightly positive.
     Caveat: post-rollout showed a humbler reality (full-rollout revenue
     ≈ flat, 2-year cohort uplift +1.5%, "below what the experiment led us to
     expect") [T3-02, significant-positive/rolled-out].
  2. **Deep-discount price on a high-intent dead segment moved revenue
     strongly** (ex-paid final offer, P-05) [T1-08].
  3. One price-increase arm DID win: iter1 iOS var5 ARPU +11.44% (p=0.01),
     concentrated in 2024-flagship iPhones (+48.68%) — the elasticity
     conclusion comes from the decisive second iteration, not from all arms
     [T3-01].
- **Applicability:** App-paywall price increases (base pattern); web funnels
  and deep-discount instants (limits).
- **Transfer bans:** never transfer "price is a dead lever" to web funnels,
  to price DECREASES, or to discount-instant mechanics — each has a measured
  counterexample above; never transfer the web-decrease magnitudes to App
  (different elasticity, see also the Android wash in P-05); the elasticity
  curve shape was never measured — only two points on it.

---

## D. Segments & lifecycle (S2, S8)

### P-08 Segment monetization state gates App offer results: ex-paid respond to App offers far more strongly than free, and conclusions do not cross the boundary

- **Claim (scope: App monetization offers/surfaces; the free↔ex-paid
  non-transfer rule itself is a policy minimum and applies everywhere):** ex-subscribers are the strongest responders to App offers by an
  order of magnitude; any product conclusion obtained on free users must not
  be transferred to ex-paid/winback and vice versa.
- **Mechanism:** ex-paid users have demonstrated willingness to pay and lapsed
  for a reason (price/need), so price/offer levers act on them directly;
  free users are dominated by never-payers.
- **Facts:**
  - Ex-subscribers showed up to 13× the conversion rate of free users —
    discovered via a segmentation bug, so direction only [T1-02,
    mixed/killed].
  - Ex-paid convert ~20× better than free per member on the same layer
    [T1-09, inconclusive/killed — supporting observation].
  - The entire winback line (deep-discount instant [T1-08], cancel-moment
    offer [T2-05]) produced the largest significant segment wins in the
    corpus.
- **Applicability:** segment prioritization for any App monetization idea;
  audience definitions at S2.
- **Transfer bans:** free→ex-paid and ex-paid→free transfers are forbidden by
  the relevance model's mandatory minimum; the 13×/20× figures are direction
  indicators, not sizing priors (one comes from a bug-contaminated iteration,
  the other from an underpowered case).

### P-09 Decision-moment timing: an offer at the two evidenced lifecycle moments (autorenew-cancel, winback-window exhaustion) converts; sequencing protects the standard funnel

- **Claim (scope: the two lifecycle moments actually measured — the
  autorenew-cancel moment and winback-window exhaustion; other "decision
  moments" are not covered):** catching the user at such a decision point with a targeted offer produces large
  segment wins without breaking the standard funnel, IF sequenced after it.
- **Mechanism:** at the decision moment the user is actively re-evaluating
  price/value; an immediate alternative redirects the decision instead of
  competing with the standard flow.
- **Facts:**
  - Winback splash immediately at autorenew-cancel: iOS ARPU +49.3%, access
    CR +50.9%, charge CR +67.3% (all p=0.00), trial share −30.1% (shift to
    direct purchase); control segment without winback accesses n.s. — effect
    localized in the target cohort [T2-05, significant-positive/rolled-out].
  - Final $19.99 offer shown only AFTER the winback interstitial and not
    earlier than next day: revives a zero-converting segment; sequencing
    protects the standard winback structurally [T1-08,
    significant-positive/rolled-out].
- **Applicability:** S8 lifecycle moments (cancel, expiry, winback-window
  exhaustion); offer sequencing design.
- **Transfer bans:** Android is NOT symmetric: expensive plans at the cancel
  moment decreased ARPU by 55% — "keep cheap control on Android" [T2-05
  iter2]; iter3 of the same line failed due to a subscription-tracking bug
  (measurement, not product); magnitudes are iOS-specific.

### P-10 Message/creative PERSONALIZATION around an unchanged offer did not lift purchases; OFFER personalization did (mandatory pattern)

- **Claim (scope: personalization changes only — cases where the
  message/creative wrapper is personalized to the user while the OFFER is
  held constant, versus cases where the offer itself is personalized. This
  card does NOT cover wrapper/creative changes in general — format, creative
  quality, gamification, seasonal or emotional design are a different class,
  see P-03 and its limits):** personalizing only the message/creative around an unchanged offer
  did not lift purchases where measured; personalization moved money when the
  OFFER itself (terms, product, occasion) matched the user's state.
- **Mechanism:** message personalization raises curiosity but creates
  expectation mismatch on the generic paywall behind it; offer
  personalization changes the actual value proposition.
- **Facts:**
  - Song-personalized interstitial ("Play %SONG% like %AUTHOR%") with
    unchanged offers: flat conversion, paywall→click halved; the page's own
    formulation: "Personalize the offer, not only the message around the
    offer" [T1-09, inconclusive/killed — direction lesson].
  - Anniversary upsell splash to paying Pro users (offer = Pro+Courses bundle
    discount tied to the subscription milestone): significant on both
    platforms, rolled out, post-rollout ≈$1100/day iOS revenue [T2-06,
    significant-positive/rolled-out].
  - Device-tier price personalization (payment-capacity proxy) failed to beat
    elasticity [T3-01, mixed/killed] — a proxy is not the user's state.
- **Applicability:** personalization ideas on S3–S6 — both the
  personalized-wrapper/unchanged-offer sub-case and the personalized-offer
  sub-case; the wrapper-vs-offer decision INSIDE a personalization idea. NOT
  applicable to non-personalization creative/format/design changes (P-03).
- **Transfer bans:** T2-06 lift percentages are non-transferable (near-zero
  control base — control had no splash at all); paying-segment upsell
  economics do not transfer to free/ex-paid acquisition; message-only
  personalization is not disproven for retention/engagement goals (untested
  here) — the ban is on expecting purchase lifts. Scope of the ban: it covers
  ONLY message/creative personalization with the offer held constant. Do NOT
  extend it to "wrapper changes" or "creative changes" as such: a
  non-personalized creative/format change is outside this card's evidence
  (P-03 records a case where creative quality did matter), and offer
  personalization points the other way inside this same card — a one-sided
  universal over "personalization" or over "wrapper changes" is therefore an
  unsupported transfer.

---

## E. Measurement & design gates (cross-cutting; these patterns guard every other card)

Scope note (V1.2 heading audit): P-11–P-14 are deliberately corpus-wide
METHOD gates — claims about how to measure and interpret an experiment, not
product claims about a family of interventions. Their evidence (cases where a
mis-scoped metric, an undelivered design, an immature read or an attribution
artifact changed the read) supports exactly that scope, so their titles were
NOT narrowed. They still may not be used as product conclusions.

### P-11 The goal metric must match the touched surface (mandatory pattern)

- **Claim:** a surface-scoped treatment must be measured on the touched
  surface/segment; a Total metric diluted by 80%+ untouched revenue is
  structurally unable to detect the effect and produces false "no effect"
  reads.
- **Mechanism:** signal-to-noise: the treated share of revenue bounds the
  detectable Total lift; maturity and platform mix add further dilution.
- **Facts:**
  - Discounted-instant interstitial: Total ARPU goal was flat-negative (−5.4%,
    p=0.61) while the touched surface read +58.14% net revenue (final
    trial-free read) — Total metric drowned the effect in 83–88% untouched
    revenue; the page's main lesson [T1-10, inconclusive-stopped —
    measurement lesson].
  - Winback final offer: segment win (+241% ARPU, p=0.000) real and rolled
    out while the Total ARPU lift lost significance after control trials
    matured (+9.3%, p=0.40) [T1-08, significant-positive/rolled-out].
  - Anniversary splash: goal correctly scoped to anniversary members →
    upsell%; Total-style percentages exploded (+3910%) only because the
    control base was near zero — scoping, not magic [T2-06].
- **Applicability:** pre-launch design of EVERY surface- or segment-scoped
  experiment: goal metric, sample sizing, and success thresholds must be
  defined on the affected scope.
- **Transfer bans:** does not license ignoring Total/guardrail metrics —
  dilution/cannibalization must still be read on Total (T1-08 iOS dilution
  −$702/day on non-winback); surface metrics inherit surface-selection bias
  and need their own SRM check.

### P-12 Delivery/exposure is a pre-launch gate (mandatory pattern)

- **Claim:** before interpreting any result, verify the treatment was actually
  delivered as designed (arms live, platforms launched, planned duration and
  sample reached); undelivered design leaves large effects unresolved and is
  the most common silent killer in this corpus.
- **Mechanism:** partial delivery (missing arms, dead platform, short run)
  destroys power and biases platform/segment mixes without any error message.
- **Facts:**
  - Run delivered 9 of 15/20 design days and 2 of 3 arms; churn/refund
    unreadable (pending 59–79%); experiment ended inconclusive-stopped with
    "hold and re-run" [T1-10, measurement lesson].
  - iOS effectively never launched (real volume only 3 days) — the platform
    read was declared unreadable [T1-09, measurement lesson].
  - Sample reached a fraction of design (iOS 20,329 vs 216,622 design) and
    the experiment was rolled out early on interim reads, permanently losing
    the final read; post-rollout forecast turned negative [T2-02,
    measurement lesson].
  - Significant negatives CAN survive undersampling (T2-07 killed on −36%
    access CR at a fraction of design) — the gate is about interpreting
    nulls/positives, not about ignoring clear harm.
- **Applicability:** pre-launch checklist AND first-analysis checklist of
  every experiment: delivery, arms, platforms, duration ≥ design, sample ≥
  design, SRM.
- **Transfer bans:** none — this is a universal gate; but do not use it to
  dismiss significant results that survived under-delivery.

### P-13 Maturity changes conclusions: trial windows and pending charges must mature before a read is final

- **Claim:** reads taken before trial windows mature systematically overstate
  or misplace effects; early rollout forfeits the final read.
- **Mechanism:** trial→charge conversions arrive with the trial-length lag;
  pending shares of 15–79% mean the money is not yet counted, asymmetrically
  across arms.
- **Facts:**
  - Total ARPU lift disappeared after control trials matured [T1-08].
  - Pending 14d charges 59–79% by arm made churn/refund unreadable [T1-10].
  - 3-plan test left pending 24%/15.7% with an explicit "re-check churn and
    refund in ~2 weeks" [T3-03].
  - Early rollout on interim reads deprived the team of the final read
    [T2-02].
- **Applicability:** every trial-bearing funnel; any read where pending trial
  share is material (the calculator's >5% gate).
- **Transfer bans:** none.

### P-14 Attribution artifacts and segment contamination fabricate lifts; verify the cohort and the counter before believing a number

- **Claim:** the corpus contains multiple large "effects" that were artifacts
  of attribution, segment contamination, or tracking bugs; a striking lift
  from a low-volume or newly-instrumented source is guilty until proven
  innocent.
- **Mechanism:** mis-scoped segments import someone else's revenue;
  new event paths misattribute conversions; tracking bugs silently drop them.
- **Facts:**
  - Iter1 lift +24%/+13% ARPU was an artifact of ex-premium users in the
    "free" segment (~37% of revenue); the clean iter2 read was 2–3× smaller
    [T1-02].
  - A visible ×4.6 winback lift was an attribution artifact [T1-09].
  - An entire iteration failed on a subscription-tracking bug (−30%
    conversions in test) [T2-05 iter3].
  - 2% of intro subscriptions were wrongfully charged as weekly — controlled
    post-rollout [T3-05].
  - A targeting bug showed the splash to trial users but provably did NOT
    drive the result (6 iOS / 26 And subscriptions) — bugs must be quantified,
    not assumed decisive [T2-06].
- **Applicability:** analysis reviews; any surprising segment lift; any new
  event source.
- **Transfer bans:** none — universal gate.

---

## Pattern → mandatory-pattern mapping (task FLOW-578)

| Mandatory pattern from the task | Card |
|---|---|
| goal metric matches the touched surface | P-11 |
| delivery/exposure as a pre-launch gate | P-12 |
| personalize the offer, not only the wrapper | P-10 |
| limits of the "price doesn't move net revenue" pattern | P-07 |

The left column repeats the FLOW-578 task wording. It is a task label, not a
scope statement: the scope of each card is the one written in its own heading
and claim line (V1.2). In particular the P-10 row must not be read as a claim
about wrappers/creatives in general — see the P-10 heading and transfer bans.
