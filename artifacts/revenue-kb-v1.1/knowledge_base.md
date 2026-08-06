# Revenue Knowledge Base V1.1 — Corpus & Closeness Model (FLOW-586, frozen 2026-08-05)

This file plus `pattern_cards.md` form the KNOWLEDGE CONTEXT for arm B of the
evaluation protocol. Contents:

1. How to use this base (retrieval contract)
2. Closeness model (L1/L2/L3): deterministic level computation and the strict
   machine-parsable analog-card format
3. Indices: by flow stage, segment, mechanism, decision type
4. 18 evidence source cards (T1-01…T3-06)

Scope: completed UG revenue experiments, verified against Confluence source
pages on 2026-08-04 (inventory FLOW-577 V0.1, holdout-excluded input). Money
figures are net revenue unless stated otherwise. The anchor family of the
typology is the UG App monetization interstitial layer (S3–S4).

V1.1 changes only §1 cross-references and §2 (the closeness model is now a
deterministic, linter-checked specification per Evidence Policy V1); the
corpus (§4), the indices (§3) and `pattern_cards.md` are unchanged from V1.

---

## 1. How to use this base (retrieval contract)

When validating a new pre-launch experiment card:

1. Locate the new case on the flow map (stage S1–S9), and read its segment,
   surface, mechanism, offer, metric and money chain.
2. Retrieve candidate analogs via the indices (§3) and source cards (§4).
3. For every analog you use, emit an analog card in the STRICT format of §2.4.
   You do NOT choose the closeness level: apply the deterministic rules of
   §2.2 to the axis values you filled in — the level is a computed property
   of those axes, and a machine linter recomputes it from your card. Any
   mismatch between the stated level and the computed level invalidates the
   whole answer. A card without a non-empty `not_transferable` section is
   invalid.
4. Apply `pattern_cards.md` patterns whose applicability scope covers the new
   case; respect every `transfer_bans` entry.
5. Ranking: L1 > L2 > L3; within a level rank by (a) number of exact axis
   matches, (b) segment closeness, (c) recency, (d) precision of the result
   (narrow CI beats wide). Contradicting analogs: the closer one wins; at
   comparable closeness report the conflict explicitly (both cases, both
   dates, hypothesized reason) — never average, never suppress.
6. If no L1/L2 analog exists, say "no direct analogs" explicitly. Never
   promote L3 evidence to analog status. There is NO duty to find an analog:
   the presence of historical cases creates no obligation to cite one, and in
   empty-corpus zones an honest "no direct analogs" is the correct answer —
   not a promotion of the nearest source.
7. Validity gate: cases with `result_class: inconclusive` (and
   bug-contaminated iterations) ground measurement lessons only — never
   product conclusions. For a "does not work" conclusion you need
   powered-null, not inconclusive.
8. Only the sign and mechanism of an effect transfer. Magnitudes, baselines
   and conversions transfer only as sizing priors with an explicit label.

## 2. Closeness model (deterministic; from the FLOW-574 relevance model as codified by Evidence Policy V1)

### 2.1 Axes, match values, and the three dedicated comparison fields

Ten axes: flow_stage, segment, trigger_eligibility, surface, mechanism,
offer, behavior, metric, money_chain, guardrails. Each comparison of the new
case against a source yields one of three values: `exact` / `adjacent` /
`different`.

In addition to the ten axes, every analog card carries three dedicated
comparison fields that the level computation consumes directly:

- `segment_monetization_state: exact | different` — whether the two segments
  are in the same monetization state (free vs ex-paid/winback vs canceling vs
  paying). This is a coarser judgment than the `segment` axis: two different
  segments (e.g. "free new post-tour" vs "all free") can still share the
  monetization state (`exact`), while free vs ex-paid is always `different`.
- `money_chain_link: exact | different` — whether the specific money-chain
  link the treatment acts on is the same (an effect on trial starts is not an
  effect on trial→charge). This is stricter and more local than the
  `money_chain` axis, which describes the overall chain similarity.
- `platform: exact | adjacent | different` — `exact` = same platform(s);
  `adjacent` = iOS vs Android where the mechanism is platform-agnostic;
  `different` = iOS vs Android where the mechanism is platform-specific
  (instant offer as same-subscription plan switch on iOS; commissions; store
  review flows), and any App vs Web comparison.

### 2.2 Deterministic level computation (normative; linter-enforced)

The closeness level is NEVER assigned by the model. It is computed
deterministically from the card's own `axes`, `segment_monetization_state`,
`money_chain_link` and `platform` fields by the rules below, and a machine
linter recomputes it from every emitted card. `claimed level != computed
level` is a hard error: the answer is invalid. Level is a property of the
(new case, source) pair, not of the source.

Evaluate in order; the first rule that fires decides the level.

**L1 — direct analog.** ALL of:

```
axes.mechanism  == exact
axes.flow_stage == exact
axes.surface    in {exact, adjacent}
segment_monetization_state == exact
money_chain_link == exact
platform in {exact, adjacent}
```

→ The product conclusion transfers **directionally** (sign + mechanism).
Effect size never transfers.

**L2 — partial analog.** Not L1, and ANY of the three branches:

```
(A) axes.mechanism == exact
    AND (axes.surface == different OR axes.flow_stage == different)

(B) axes.surface == exact AND axes.flow_stage == exact
    AND axes.mechanism == different

(C) axes.mechanism == exact AND axes.flow_stage == exact
    AND axes.surface in {exact, adjacent}
    AND money_chain_link == exact
    AND (segment_monetization_state == different
         OR axes.segment == different
         OR platform == different)
```

→ Transfers as a **hypothesis or warning** plus an order-of-magnitude prior
for sizing. Not a launch/deprioritize basis by itself.

**L3 — weak evidence.** Everything else (single-axis similarity: metric-only,
segment-only, or surface-only without mechanism; and any combination that
fires neither L1 nor an L2 branch). → Usable ONLY for sizing, measurement and
guardrails: baselines, variance, MDE, duration, trial-window maturity,
typical guardrail failures. No product conclusion transfers. Every L3 signal
must carry an explicit L3 label; L3 is never a "direct analog" and never a
standalone basis to change a launch/revise/deprioritize verdict.

Invariants:

- A match on `axes.metric` NEVER raises the level (metric appears in no rule
  above).
- `axes.offer`, `axes.behavior`, `axes.trigger_eligibility`,
  `axes.guardrails`, `axes.metric` and `axes.money_chain` do not participate
  in the level formula; they inform ranking within a level (§1.5) and the
  transfer-minimum gate (§2.3).

Ambiguity resolutions codified in this formalization (all err toward the
LOWER level, matching the policy's anti-inflation intent):

- **R1 (platform in L1):** the policy's L2 branch "L1 conditions hold except
  segment or platform" implies platform difference precludes L1, so L1
  additionally requires `platform != different`. `platform == adjacent`
  (cross-platform, platform-agnostic mechanism) does not by itself demote
  from L1.
- **R2 (what "except segment" relaxes):** segment enters L1 via
  `segment_monetization_state`; branch (C) therefore triggers on
  `segment_monetization_state == different` as well as on the finer
  `axes.segment == different`. A card whose only segment difference is the
  finer axis (same monetization state) still satisfies L1, and L1 is
  evaluated first — branch (C) only applies to cards that are not L1.
- **R3 (dedicated fields, not axes):** the level formula uses the dedicated
  fields `segment_monetization_state`, `money_chain_link` and `platform`
  where the policy says "segment.monetization_state", "money_chain.link" and
  "platform"; the ten-axis values for `segment` and `money_chain` are broader
  descriptors and participate only where listed above.
- **R4 (money-chain link):** `money_chain_link == different` excludes both L1
  and branch (C). Such a card can still be L2 via branches (A)/(B) — exactly
  as the policy states them — otherwise it is L3.
- **R5 (adjacent is not exact, and adjacent is not different):** `adjacent`
  never substitutes for `exact` where a rule requires `exact`
  (flow_stage/mechanism in L1; surface/flow_stage/mechanism in (B)/(C)), and
  never triggers a branch that requires `different` (the (A) and (C)
  disjuncts). Consequently some adjacent-heavy cards compute to L3; this
  strictness is intentional.

### 2.3 Mandatory minimum for transferring a product conclusion

All simultaneously: (1) mechanism exact; (2) flow_stage exact; (3) surface OR
trigger_eligibility exact/adjacent; (4) segments comparable by monetization
state — free-audience conclusions do not transfer to ex-paid/winback and vice
versa; (5) same money-chain link (an effect on trial starts is not an effect
on trial→charge); (6) source case valid: SRM ok, maturity ok, result_class
significant or powered-null.

### 2.4 STRICT machine-parsable analog-card format (emit one per analog used)

Every analog card MUST be a fenced code block (``` … ```) whose first
non-comment line is `analog:`, containing a YAML mapping with EXACTLY this
structure. The linter parses these blocks; a card that does not parse, or
misses a required field or axis, is a hard error.

````
```yaml
analog:
  source: T1-08 (ab 7487; 2026-05..07; SRM ok, trials matured; significant-positive; rolled-out)
  axes:
    flow_stage: exact            # S3–S4 exposure in both
    segment: different           # free new vs ex-paid winback-exhausted
    trigger_eligibility: adjacent
    surface: exact               # interstitial slot in both
    mechanism: exact             # deep-discount instant instead of trial
    offer: adjacent
    behavior: adjacent
    metric: exact
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: exact
  platform: exact
  level: L2
  transferable: >
    [fact] Source outcome facts with sign, CI/p-values, metric, segment, each
    tied to the source ID. [hypothesis] What that suggests for the new case,
    directionally, explicitly marked as a transfer hypothesis.
  not_transferable: >
    REQUIRED, >=1 item. Effect magnitudes are ALWAYS listed here (or in
    sizing_prior with an explicit "prior" label) — never as predictions.
    Everything outside the source case's transfer_bounds.
  sizing_prior: >
    OPTIONAL. Order-of-magnitude figures for sizing only, each labeled
    "prior".
  conflict: >
    OPTIONAL. If this analog contradicts another retrieved analog — which one
    and how; never average, never suppress.
```
````

Format rules (normative for the linter):

- Required fields: `source`, `axes` (with ALL ten axes), 
  `segment_monetization_state`, `money_chain_link`, `platform`, `level`,
  `transferable`, `not_transferable`. Optional: `sizing_prior`, `conflict`.
- `source` must contain a source ID that exists in the KNOWLEDGE CONTEXT
  (case IDs `T*-**`, pattern IDs `P-**`). Citing a nonexistent ID is a hard
  error.
- Each of the ten axes takes exactly one value from
  `exact | adjacent | different`; `segment_monetization_state` and
  `money_chain_link` take `exact | different`; `platform` takes
  `exact | adjacent | different`; `level` takes `L1 | L2 | L3`. On these
  enum-valued lines the value is the first token after the colon; an optional
  rationale may follow after ` # `.
- `level` must equal the value computed by §2.2 from the card's own fields —
  the linter recomputes it; a mismatch (including any upgrade of a computed
  L3 to a claimed L2/L1) invalidates the answer.
- `not_transferable` must be non-empty.
- Prose fields keep the fact/interpretation/hypothesis marking: source
  measurements are `[fact]`, the source team's readings are
  `[interpretation]`, and every claim about the NEW case is `[hypothesis]`.
  Effect magnitudes appear only inside `not_transferable` or `sizing_prior`
  (labeled "prior") — never as predictions for the new case.

## 3. Indices

### 3.1 By flow stage (where the treatment intervenes)

| Stage | Cases |
|---|---|
| S1–S3 feature-gate (intent → paywall) | T2-07 |
| S3–S4 exposure: App interstitial layer (anchor family) | T1-01 T1-02 T1-03 T1-04 T1-07 T1-08 T1-09 T1-10 |
| S3–S4 exposure: App splash / banner / other surfaces | T2-01 T2-02 T2-06 |
| S5–S6 web paywall / checkout / plan menu | T3-02 T3-03 T3-05 |
| S6 purchase conditions on App paywalls | T3-01 T3-06 |
| S8 lifecycle → S3 (cancel-moment offer) | T2-05 |

### 3.2 By segment monetization state

| Segment | Cases |
|---|---|
| free (incl. new post-tour) | T1-01 T1-02 T1-03 T1-07 T1-10 T2-01 T2-02 T2-07 T3-01 T3-06 |
| free + ex-paid mixed | T1-04 T1-09 |
| ex-paid / winback | T1-08 |
| canceling (at autorenew-off moment) | T2-05 |
| paying (upsell) | T2-06 |
| web new + unconverted | T3-02 T3-03 T3-05 |

### 3.3 By mechanism

| Mechanism | Cases |
|---|---|
| new-surface (replace ads / add offer layer) | T1-01 T1-02 T1-03 T1-04 |
| copy / design / creative / gamification | T1-07 T1-09 T2-02 |
| offer-structure: instant-vs-trial | T3-06 T1-08 T1-10 T3-05 |
| offer-structure: plan menu composition | T3-03 T3-05 |
| offer-structure: bundle upsell | T2-06 |
| price change | T3-01 T3-02 T1-10 |
| timing / frequency / gating | T2-01 T2-05 T2-07 T1-07 |

### 3.4 By decision (what the team did)

| Decision | Cases |
|---|---|
| rolled-out | T1-04 T1-08 T2-02 T2-05 T2-06 T3-02 T3-05 T3-06 |
| killed | T1-01 T1-02 T1-03 T1-07 T1-09 T2-01 T2-07 T3-01 T3-03 |
| inconclusive-stopped ("hold and re-run") | T1-10 |

### 3.5 By result class (validity gate input)

| result_class | Cases |
|---|---|
| significant-positive | T1-08 T2-05 T2-06 T3-02 |
| significant-negative | T2-01 T2-07 T3-03 |
| powered-null | T1-03 |
| mixed (by platform/arm/iteration) | T1-02 T1-04 T1-07 T3-01 T3-05 T3-06 |
| inconclusive (measurement lessons only) | T1-01 T1-09 T1-10 T2-02 |

## 4. Evidence source cards

Closeness-to-anchor legend: each card carries the corpus stratum relative to
the anchor family (type1 = same surface+mechanism family; type2 = same flow
stage, different surface; type3 = same metric, different flow/mechanism).
This is NOT the closeness to YOUR case — recompute L-levels vs the case under
validation using §2.

---

### T1-01 — iOS: Interstitial "Swap into Landing" [type1]
- ab_ids 4845; 2024 (run 07-15..07-20); iOS; free (no sub, no trial)
- coords: S3–S4; interstitial slot (scroll landing instead of house-ad
  no-fill); mechanism new-surface; standard Pro offer; metric
  Interstitial→Access %, ARPU; chain exposure→paywall→trial→charge D0–D14
- validity: SRM ok (3,283/3,250); maturity undocumented; result
  **inconclusive**; decision killed
- outcome fact: reach ≈ zero (no-fill only, 1/day cap): 4 accesses from the
  new source over the whole run; all monetization diffs n.s. (ARPU −10.5%,
  p=0.67)
- lesson: reach is the binding constraint (P-01); passive no-fill filling
  moves nothing
- transfer bounds: only this passive config; says nothing about the layer's
  potential under active replacement
- note: inconclusive ⇒ measurement lesson only

### T1-02 — App: paywall — offer instead of ad interstitials, iter 1–2 [type1]
- ab_ids 6002/6128/6191; 2025-04..07; iOS+Android; free (iter1 contaminated
  by ex-premium; iter2 clean)
- coords: S3–S4; interstitial slot + ad-banner places; mechanism new-surface
  + offer-structure (Pro+ $39.99/yr, extended 14d trial); metric
  Interstitial→Access %, ARPU
- validity: SRM ok; result **mixed**; decision killed
- outcome fact: iter2 iOS ARPU +7.5% (p=0.029), And +4.94% (p=0.36);
  cannibalization 34% iOS / 63% And; interstitial trial→charge below average
  (−13% iOS / −45% And); iter1 lift (+24%/+13%) was a segment-contamination
  artifact (ex-premium ≈37% of revenue)
- lesson: ex-subscribers respond up to 13× (direction only — found via the
  bug) (P-08); first exposure does 60–87% of the work (P-01); a generous
  trial pulls low-quality trials; surface value = net increment (P-02)
- transfer bounds: free App audience; magnitudes non-transferable; "novelty
  trap" rationale is interpretation
- note: intro pricing of the same annual plan was the positive part of
  iter 1–2 (see P-06 bans)

### T1-03 — iOS: paywall after ad interstitial [type1]
- ab_ids 6335; 2025-07 (7-day run); iOS; free incl. ex-premium
- coords: S3–S4 post-ad; chain pre-paywall → compare table → standard
  paywall; mechanism new-surface + funnel structure; metric
  Interstitial→Access %
- validity: SRM ok (35,411/34,913); result **powered-null**; decision killed
- outcome fact: new-scenario conversion 0.07%; 96% drop on the first
  skippable pre-paywall; Total ARPU +10.4% (p=0.19); 3% of subs from the new
  source with cannibalization of tab sources
- lesson: longer funnel after an ad works worse than a plain banner; extra
  step = multiplicative drop-off (P-04)
- transfer bounds: iOS post-ad context; does not condemn pre-paywalls in a
  neutral context (cf. T1-07 where a gamified pre-step lifted conversion)

### T1-04 — App: monetization video instead of ad interstitials [type1]
- ab_ids 6359/6416/6428; 2025-07..08; iOS+Android; free + ex-paid (all
  without Pro rights)
- coords: S3–S4; interstitial slot (video creative, "Try for Free" button);
  mechanism new-surface + creative; metric ARPU (goal)
- validity: SRM ok; result **mixed**; decision rolled-out (Android)
- outcome fact: And ARPU +17–19% significant in both iterations; iOS iter2
  +2.66% (p=0.43); iOS iter1 segment without interstitial accesses −24.7%
  (cannibalization of ad revenue and other paywalls)
- lesson: value comes from reach, not per-impression conversion (clicks
  0.5–1% of views) (P-01); pure increment where the video replaces "nothing"
  (And) vs competition where ad inventory exists (iOS) (P-02); creative
  quality matters (chords variant strictly worse); retention price appears
  when replacing a guaranteed daily show, not when filling fails
- transfer bounds: Android conclusion does not transfer to iOS; magnitudes
  depend on ad-inventory presence

### T1-07 — App: pre-paywall with animation (scratch coupon) [type1, ex-holdout IH-01]
- ab_ids 7160/7187; 2026-03..07 (8-day run); iOS+Android; free new
  (post-tour)
- coords: S3–S4; interstitial slot, gamified scratch coupon; var3
  non-skippable; mechanism copy/design (gamification) + frequency/timing
  (skip vs no-skip); metric ARPU, interstitial→access CR
- validity: SRM ok; pending-trial maturity undocumented; result **mixed**;
  decision killed
- outcome fact: iOS var2 ARPU +26.5% (p=0.011); interstitial segment +72.7%
  (var2) / +166% (var3); non-skippable: ×8 engagement, +150–160% layer
  revenue, but And var3 retention D1 −9.15% (p=0.012); absolute increment
  small (forecast iOS var2 +$474/day)
- lesson: gamification lifts layer conversion on both platforms;
  monetization/retention trade-off of non-skippability (P-03); repeated
  splashes add almost nothing (P-01); significant relative lift ≠ sufficient
  absolute increment (P-11 flavor)
- transfer bounds: new post-tour users only; var2 anomaly (−75–77%
  interstitial→banner) unexplained — treat var2 internals with caution

### T1-08 — App: winback — final interstitial offer $19.99 [type1, ex-holdout IH-02]
- ab_ids 7487; 2026-05..07 (~21-day run); iOS+Android v7.3.9+; ex-paid who
  exhausted the winback window
- coords: S3–S4 after winback-window exhaustion; interstitial slot ("last
  chance" offer); mechanism offer-structure + price (deep-discount instant
  $19.99 instead of trial); metric members→buyers %, segment ARPU; chain
  exposure→instant charge (no trial link), D0
- validity: SRM ok (9,933/9,753 iOS; 3,566/3,602 And); trials matured
  (pending=0), churn/refund 14d preliminary; result
  **significant-positive**; decision rolled-out
- outcome fact: iOS winback ARPU +241% (p=0.000), buyers +365.6%; Total ARPU
  +9.3% (p=0.40) — lift lost significance after control trials matured;
  final offer converts to 100% instant purchases; forecast +$151/day iOS,
  +$107/day And; iOS diffuse dilution −$702/day on non-winback
- lesson: deep-discount instant revives a dead segment: trades trials for
  immediate payment, EV-positive on high-intent ex-paid (P-05, P-08);
  sequencing protects the standard winback structurally (P-09); maturity
  changes conclusions (P-13); segment win real while Total lift evaporates
  (P-11)
- transfer bounds: ex-paid high-intent ONLY; transfer to free is forbidden;
  iOS dilution bounds the net increment
- note: page marks confirmatory vs exploratory explicitly; "where iOS
  non-winback purchases went" is exploratory

### T1-09 — App: personalized interstitial [type1, ex-holdout IH-03]
- ab_ids 7454; 2026-05..06 (10-day run); iOS+Android (iOS unreadable — real
  volume only 3 days); free + ex-paid (winback branch)
- coords: S3–S4; interstitial slot, song creative "Play %SONG% like
  %AUTHOR%"; mechanism copy/design — message personalization only, offers
  unchanged (free: 80% off Pro+; ex-paid: +14d Pro+)
- validity: SRM ok; result **inconclusive**; decision killed
- outcome fact: ≈0: pauses→paywall slightly up, paywall→click ×0.5
  (7.25%→3.90%); visible winback lift ×4.6 was an attribution artifact; all
  monetization p ≥ 0.32; ~70–165 interstitial conversions per arm
- lesson: "Personalize the offer, not only the message around the offer"
  (P-10); attention ≠ intent (P-03); layer conversion front-loaded: show #1
  = 50–60% (P-01); ex-paid convert ~20× better per member (P-08, supporting)
- transfer bounds: message-only personalization; does NOT disprove offer
  personalization; iOS read impossible
- note: inconclusive ⇒ measurement/direction lessons only

### T1-10 — App: interstitial — discounted prices ($29.99 instant) [type1, ex-holdout IH-04]
- ab_ids 7712; 2026-07 (delivered 9 of 15/20 design days, 2 of 3 arms);
  iOS+Android; free new (post-tour)
- coords: S3–S4; both layer scenarios replaced by a discount interstitial;
  mechanism price + offer-structure (instant $29.99, no trial/intro); metric
  Total ARPU (goal — chosen wrongly), surface ARPU/net revenue (actually
  informative); chain exposure→instant charge D0
- validity: SRM ok (<1%); maturity NO (pending 14d charges 59–79%);
  result **inconclusive**; decision inconclusive-stopped ("hold and re-run,
  do not discard")
- outcome fact: touched surface iOS +58.14% net revenue (final trial-free
  read; surface ARPU p=0.22) with flat volume; And −5.06% (elasticity ate
  it); Total flat-negative (−5.4% iOS, p=0.61) — structurally blind: 83–88%
  of revenue untouched
- lesson: measure surface-scoped treatments on the touched surface — the
  page's main lesson (P-11); platforms differ in elasticity, not execution
  (P-07); design under-delivery leaves large effects unresolved (P-12)
- transfer bounds: measurement lessons only (inconclusive); And read is
  about the $29.99 step, not instant mechanics in general; winback surface
  undecided

### T2-01 — App: sale — turning off banner and splash [type2]
- ab_ids 6293; 2025-07; iOS+Android; free
- coords: S3–S4; sale banner (Explore) + sale splash (NOT interstitial);
  mechanism gating/frequency — surface OFF (negative test of value); metric
  ARPU
- validity: SRM ok; R14 mature; result **significant-negative** (turn-off
  harmed); decision killed (surfaces kept)
- outcome fact: both-off arm: ARPU −11.6% iOS (p=0.036) / −26% And
  (p=0.036), charge CR −38.1% And (p=0.000); splash-only-off arm n.s.
  (iOS −1.2% p=0.83)
- lesson: an off-test is a cheap direct measure of a surface's
  incrementality; conversion does NOT fully redistribute when a surface
  disappears; splash weaker than banner (P-02)
- transfer bounds: seasonal sale surfaces; does not transfer to non-seasonal
  layers without a test
- note: actual verdict on page: "We're not rolling out the experiment";
  the "keep banner, manage splash frequency" quote is a mirror artifact —
  absent from the page

### T2-02 — App: Halloween sale with emotional design [type2]
- ab_ids 6701; 2025-10 (iOS 4 days / And 5 days vs 7-day design; iOS 20,329
  vs 216,622 design sample); App; free
- coords: S3–S4 seasonal window; sale splash + Explore banner + paywall-entry
  animation; mechanism copy/design (emotion, sound, haptics); metric CR
  DAU→Charge
- validity: SRM ok; duration/sample INCOMPLETE; R14 not computed; early
  rollout before final read; result **inconclusive**; decision rolled-out
- outcome fact: finals n.s. (ARPU iOS −2.95% p=0.66, And −1.38% p=0.91;
  "slightly lower by ~−2% by cannibalization"); significant only
  CR→Splash View iOS (p=0.001), scenario ARPU p=0.060; post-rollout
  Forecast iOS −$1716/day, And −$426/day
- lesson: emotional design alone does not move money (P-03); early rollout
  on interim reads forfeits the final read (P-12, P-13)
- transfer bounds: seasonal events; "suitable for big one-off events" is the
  author's extrapolation, not a measurement
- note: inconclusive ⇒ measurement lessons only

### T2-05 — App: winback right after cancel [type2]
- ab_ids 6404/6614/6863; 2025-08..12 (3 iterations); iOS+Android; canceling
  users (at autorenew-off moment)
- coords: S8→S3; splash + Explore banner (NOT interstitial); mechanism
  offer-structure + timing (immediate offer at the cancel decision); metric
  trial→charge %, access CR, charge CR, ARPU
- validity: SRM ok in all 3 iterations; cancels/refunds 14d computed;
  post-rollout analysis present; result **significant-positive**; decision
  rolled-out
- outcome fact: iter1 iOS var2: ARPU +49.3%, access CR +50.9%, charge CR
  +67.3% (all p=0.00), trial share −30.1% (shift to direct purchase), AOV
  −11.4%, R7/R14 +2.0/+1.4%; control segment "without winback accesses"
  n.s. (+6.47%, p=0.32) — effect localized in the target cohort; iter2 iOS
  winback ARPU +370%; And expensive plans −55% ARPU ("keep cheap control on
  Android"); iter3 FAIL — subscription-tracking bug (−30% conversions)
- lesson: an offer at the cancel decision moment converts (P-09); discount
  shifts structure from trial to direct payment (P-05 flavor); segment
  localization check supports causality (P-11); tracking bugs fabricate
  reads (P-14)
- transfer bounds: cancel moment; magnitudes iOS-specific; Android negative
  on expensive plans

### T2-06 — App: Anniversary upgrade splash for Pro subscribers [type2]
- ab_ids 6515; 2025-09 (run 09-11..09-15); iOS+Android; paying (Pro without
  Courses/Sing), milestones 30/90/180/365 days
- coords: S3–S4 upsell; personalized anniversary splash (NOT interstitial);
  mechanism offer-structure + personalization (Pro+Courses bundle discount
  tied to the milestone); metric anniversary members → upsell %
- validity: SRM ok; cancels/refunds 14d present; post-rollout confirms
  revenue (iOS ≈$1100/day, And ≈$300/day); result **significant-positive**;
  decision rolled-out
- outcome fact: iOS ARPU +3910% (p=0.00), And +1280% (p=0.00) — against a
  near-zero control base (control had NO splash); targeting bug (splash to
  trial users) provably did not drive monetization (6 iOS / 26 And subs)
- lesson: occasion-based offer personalization on paying users converts
  (P-10); giant percentages = near-zero base, not bug inflation — quantify
  bugs before blaming them (P-14, P-11)
- transfer bounds: paying segment only; percentages non-transferable
  (near-zero base); no transfer to free/ex-paid

### T2-07 — App: Feature preview paywall (10-second demo) [type2]
- ab_ids 6806; 2025-12 (And 4 of 10 design days; samples far below design);
  App; free (never-subscribed)
- coords: S1–S3 feature-gate; feature paywall with 10s preview + timer;
  mechanism timing/friction (delayed paywall after feature try); metric
  feature → access %
- validity: SRM ok; duration/sample under design, negatives significant
  anyway; result **significant-negative**; decision killed
- outcome fact: access CR −36% iOS (p=0.00) / −28.5% And (p=0.008); losses
  along the whole funnel (conversion to banner −10%/−18%; banner
  click→purchase −22%/−26%); beginners iOS −42.1%; AOV +14.2% / ARPPU
  +17.9% (mix shift)
- lesson: captured intent must not be deferred — a step between feature
  desire and the paywall loses conversion (P-04); consistent with T1-03
- transfer bounds: feature-gate context; does not condemn demo content
  BEFORE intent (untested); "psychological friction" vs "broken navigation"
  contributions not isolated

### T3-01 — App: increasing prices for "whales" (device-tier pricing) [type3]
- ab_ids 6026/6260; 2025-05..07; iter1 iOS+And, iter2 (decisive) iOS only;
  free with mid-high devices (storage proxy)
- coords: S6 purchase conditions (segmentation at S2); standard App
  paywalls; mechanism price (personalized increase by device tier); metric
  ARPU, trial→charge
- validity: SRM ok; iter2 duration/sample ≈4.4× design (mature); result
  **mixed**; decision killed
- outcome fact: iter1 iOS var5 ARPU +11.44% (p=0.01), 2024-flagship segment
  +48.68%; decisive iter2: Total ARPU +1.38% (p=0.61); tour ARPPU +7.34%
  (p=0.001) eaten by charge CR −11% (p=0.003); refunds 14d +26.2% (p=0.006);
  page verdict "price increase too high"
- lesson: price moves structure, not sum — elasticity eats the increase
  (P-07 base); a payment-capacity proxy (device) is insufficient for price
  discrimination (P-10)
- transfer bounds: App paywall price INCREASES; does not transfer to
  decreases (T3-02 is the counter-direction) or to web; elasticity curve
  shape unmeasured

### T3-02 — Web: paywall — price decrease for Pro+ [type3]
- ab_ids 7268; 2026-04 (run 04-09..04-29); Web/Desktop; new + unconverted
- coords: S5–S6 web paywall + checkout; mechanism price (entry prices down:
  monthly $24.99→$9.99, trial $99.99→$39.99, instant $64.99→$24.99,
  ambulance $49.99→$19.99); metric revenue, accesses
- validity: no explicit SRM check on page (members diff 0.95%);
  cancel/refund 14d included; post-rollout analysis present; result
  **significant-positive**; decision rolled-out
- outcome fact: Access CR +68.87%, Charge CR +88.91%, trial→charge +18.25%
  (p=0.00); AOV −44.58% / ARPPU −45.51%; ARPU +2.93% (p=0.45); revenue fact
  +4.18%; retention 1/7/14d +3.6/+1.8/+1.3% significant; comeback-offer CR
  −20% (guardrail); post-rollout: full revenue ≈ flat (−0.45%), 2-year
  cohort uplift +1.5% — "below what the experiment led us to expect"
- lesson: web entry-price decrease works through volume + the upsell chain —
  the counter-example bounding "price doesn't move revenue" (P-07 limits);
  model-based long-horizon forecasts overstate (post-rollout humbler)
- transfer bounds: web funnel; 3-year figure is a model, not a fact; no
  direct transfer to App prices (different elasticity)

### T3-03 — Web: Three-month / Six-month plans [type3]
- ab_ids 7502; 2026-05..06 (12 of 15 design days; var C stopped early);
  Web/Desktop; web subscription funnel
- coords: S5–S6 plan menu; mechanism offer-structure (add $19.99/3m,
  $24.99/6m with intro pricing); metric conversion to payment, ARPU
- validity: SRM ok; pending 14d charges 24.0%/15.7% ("re-check churn in ~2
  weeks"); result **significant-negative**; decision killed
- outcome fact: var C: members→subscribers −11.08% (p=0.028), →buyers
  −11.90% (p=0.038); trials share +22.7%/+12.2%; trial→charge +21.7%/+25.8%
  (positive trial mechanics); ARPU B −7.07% (p=0.23); forecast −$918 (B) /
  −$1408 (C) per day; short plans cannibalized annual instants
- lesson: a new menu offer is a substitute, not an addition (P-06); positive
  sub-mechanics do not compensate the annual-revenue loss
- transfer bounds: web plan menus; not App paywalls; does not contradict
  intro pricing of the same annual plan (different mechanism)

### T3-05 — WEB: "Flo"-like paywall, 6 iterations incl. intro offers [type3]
- ab_ids 6464/6482/6743/6860/6875/7091/7178; 2025-08..2026-06; Web; Pro web
  funnels
- coords: S5–S6 web paywall + post-trial-start offer chain; mechanism
  offer-structure (intro instant offer; paid trial; plan composition);
  metric trial→charge %, ARPU
- validity: SRM ok in all 7 iterations; 7091 stopped day 3 of 7; wrongful
  charges (2% intro charged as weekly) controlled post-rollout; result
  **mixed**; decision rolled-out (intro iteration)
- outcome fact: best iteration 6875 (intro on all funnels): ARPU +12.1%
  (var2, p=0.020) / +19.2% (var3, p=0.000), trial→charge +28.9–32%, 14d
  cancel −19–20%, BUT var3 retention significantly worse; paid-trial
  iterations failed (7091 ARPU −23.8%, stopped; 7178 −6.66% n.s.); earlier
  UI iterations rejected on guardrails (print AOV −32.2%; cancels +37.4%;
  refunds +72.3%)
- lesson: intro/instant offer structure beats trial mechanics on conversion
  quality — cross-flow confirmation with T3-06 (P-05); choice overload
  suspected on plan menus (P-06); guardrails kill UI wins (P-14 flavor)
- transfer bounds: web funnels; magnitudes vary by iteration; intro quality
  depends on wrongful-charge control; rolled-out var carries a measured
  retention minus

### T3-06 — iOS: trial to Instant on internal paywalls [type3]
- ab_ids 6326; 2025-06..09 (23-day run ≥ 19 design); iOS; free on internal
  PRO paywalls (not courses/songbooks)
- coords: S6 offer structure at purchase; internal App paywalls; mechanism
  offer-structure (trial→instant: −40% price, $24.99 annual, immediate
  charge); metric ARPU, charge CR; chain paywall→instant charge D0
- validity: SRM ok (members diff 0.96%); duration complete; renewal/LTV
  under post-rollout monitoring; result **mixed**; decision rolled-out
- outcome fact: charge CR +16.4% (p=0.00), access CR +4.04% (p=0.05), ARPU
  +5% (p=0.18, n.s.), AOV/ARPPU −9.8…−13.2% (p=0.00), trial→charge −39.5%
  (p=0.00), 14d cancels −42.2% (p=0.00); subscriber→buyer +11.9–15.7%;
  forecast +$353/day vs plan +$500
- lesson: "drop the trial, promote direct purchase" works on iOS internal
  paywalls: structure shift to immediate payment, fewer early cancels
  (P-05); mirror-derived "significant-positive" overstated it — ARPU itself
  n.s. (P-14 flavor)
- transfer bounds: iOS internal paywalls; Android elasticity differs;
  discount size is a parameter, not a constant; long-term EV conditional on
  renewal (monitored)
