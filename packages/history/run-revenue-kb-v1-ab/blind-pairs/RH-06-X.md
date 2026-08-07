**1. Verdict — redesign before launch.** The core idea (remove a cannibalizing cheap instant plan from a web menu) has directional support in the corpus, but the design as written cannot be delivered: the traffic math is off by an order of magnitude, and the goal metric is both selection-biased and mechanically rigged to favor the test arm.

**2. Predicted outcome.** Plan-menu→access CR likely rises: fewer options, a default-selected trial, and — critically — the modeled mix shift toward trials inflates "accesses" regardless of whether money moves. Net revenue per visitor within a 6–7 day window is likely flat-to-negative: removed instant charges are lost immediately (the $19.99 instant is ~32 of ~98 channel accesses), while replacement trial revenue arrives only after the trial window, at an *assumed* trial→charge improvement (24.18%→30%) with no evidential basis. What would surprise me: charged revenue rising inside the run window.

**3. Top risks & failure modes**

- **Design is undeliverable.** Baseline shows ~479 plan-menu views over the 16-day model period (~30/day). The design needs 1,602/arm = 3,204 in 6 days (~460/day) — a ~15–18× shortfall. Nulls will be uninterpretable [P-12].
- **Full-redistribution assumption is the default failure.** The model assumes removed instant volume shifts into trials (8→56) and the exit offer. The corpus's direct measurement of option removal shows conversion does NOT fully redistribute [T2-01, P-02]. Expect a leak.
- **Goal metric mismatch on two counts** [P-11]: (a) conditioning on plan-menu views after changing the strip creative (+15% clicks assumed) means the arms' denominators are different populations — selection bias, and menu-level SRM will "fail" by design; (b) "access" counts trial starts, so the metric rewards the exact mix shift being engineered, while the money chain (trial→charge) is unread in 7 days [P-13].
- **Removing the best-converting offer type.** Instant/intro offers beat trial mechanics on conversion quality across iOS and web [T3-06, T3-05, P-05]. RH-06 bets the reverse. Possible, but it's swimming against the corpus's strongest offer-structure pattern.
- **Simultaneous price increases** (exit $19.99→$24.99, instants toward $39.99) ride on unmeasured web elasticity; the App increase was eaten by conversion loss and refunds +26% [T3-01, L3 warning; P-07]. Also: the hypothesis says "+$500 daily" but the model projects +$501 *over the whole ~16-day slice* (~$31/day) — a ~16× internal inconsistency that must be resolved before sizing success.

**4. Analogs** (ranked)

```
analog:
  source: T3-03 (ab 7502, 2026-05..06, significant-negative, SRM ok, killed)
  level: L1
  matched: [mechanism: exact — plan-menu composition; flow_stage: exact — S5–S6 web
    plan menu; surface: exact — web subscription paywall; segment: exact — web
    free/unconverted; money_chain: exact — menu view → purchase]
  mismatched: [operation direction: T3-03 ADDED cheap plans, RH-06 REMOVES one]
  transferable: sign+mechanism — cheap short/instant plans in a web menu are
    substitutes that cannibalize annual purchases (buyers −11.9% when added).
    Directly supports RH-06's premise that the $19.99 instant cannibalizes the
    trial offer.
  not_transferable: effect sizes; the inference "removal recovers the value"
    is a reverse reading of an addition test — hypothesis-grade, not measured;
    trial-mechanics upside inside plans did not compensate revenue loss there.
  conflict: with T3-06/T3-05 below — see those cards.
```

```
analog:
  source: T3-05 (ab 6464…7178, 2025-08..2026-06, mixed, rolled-out intro arm)
  level: L2
  matched: [surface+flow_stage: exact — web paywall/offer chain; segment:
    exact — web funnels; mechanism: adjacent — offer-structure, but intro/paid-
    trial variants, not plan removal]
  mismatched: [mechanism detail: different — its winning lever was the
    intro/instant offer, which RH-06 removes from the menu]
  transferable: warning — instant/intro structure was the conversion-quality
    winner (trial→charge +29–32%, cancels −19–20%); "choice overload" on
    3-plan menus is a corpus-suspected mechanism supporting the 2-option menu.
  not_transferable: magnitudes; guardrail failures (cancels +37%, refunds +72%
    killed UI arms) — instrument, don't assume.
  conflict: supports fewer options but contradicts removing the instant SKU;
    report both, don't average.
```

```
analog:
  source: T3-06 (ab 6326, 2025-06..09, mixed, rolled-out)
  level: L2
  matched: [mechanism: exact — instant-vs-trial trade; money_chain: exact —
    offer structure at purchase]
  mismatched: [platform/surface: different — iOS internal App paywalls, not
    web; direction: it dropped the TRIAL for instant, RH-06 drops the instant]
  transferable: warning-grade — instant replaced trial and grew buyers
    (charge CR +16.4%) with fewer early cancels; RH-06's opposite bet needs
    the unproven trial→charge lift to be true.
  not_transferable: all magnitudes; iOS elasticity ≠ web; no product
    conclusion transfers cross-platform at L2.
  conflict: with T3-03's pro-removal reading, as above.
```

```
analog:
  source: T3-02 (ab 7268, 2026-04, significant-positive, rolled-out)
  level: L2
  matched: [surface+flow_stage+segment: exact — web paywall, new/unconverted;
    mechanism: adjacent — price, but a DECREASE]
  mismatched: [price direction: different — RH-06 raises exit/instant prices]
  transferable: warning — web revenue responded through volume at lower entry
    prices; raising price points risks the opposite side of the same
    elasticity; also a sizing lesson: post-rollout reality was humbler than
    the experiment read.
  not_transferable: magnitudes; decrease results never license increase
    conclusions [P-07].
```

```
analog:
  source: T2-01 (ab 6293, 2025-07, significant-negative, killed)
  level: L3 (App surface off-test, different surface and mechanism)
  transferable: sizing/measurement lesson only — when an option/surface is
    removed, conversion does not fully redistribute (ARPU −11.6%/−26% on
    turn-off); budget a redistribution leak into the model instead of the
    assumed near-full shift.
  not_transferable: any product conclusion; App seasonal surfaces ≠ web menu.
  matched: [mechanism-family: removal/gating]
  mismatched: [surface, platform, flow detail: different]
```

**5. Design & measurement checklist**

- Re-anchor the goal on the exposed population (strip viewers, intent-to-treat): net revenue per strip viewer, with menu→access as diagnostic only. Do SRM at the strip-view exposure event, not at menu views.
- Separate trial *starts* from *charges* everywhere; run ≥ trial length + charge window before the final read; pre-register the pending-charge gate [P-13].
- Redo power on realistic traffic: at ~30 menu views/day, either extend to months, power on a higher-traffic upstream metric, or widen eligibility. Resolve the $31/day-vs-$500/day inconsistency first.
- Guardrails: refunds/cancels 14d (price increases: T3-01's refunds +26%), exit-offer take-rate at $24.99 vs the current $19.99 save-offer baseline (~23 accesses), monthly-plan mix shift.
- The bundled treatment (creative + menu + prices + exit offer + cancellation-funnel change) cannot attribute a win; at minimum ship the cancellation-funnel change to both arms.

**6. Changes that would most improve expected value**

1. Split into two arms or two sequential tests: (a) menu reduction alone at unchanged prices, (b) exit-offer repricing — otherwise a null is unreadable and a win unattributable.
2. Move the goal to net revenue per strip viewer with a run long enough to mature trials; treat menu→access as a diagnostic, since the mix shift inflates it by construction.
3. Replace the full-redistribution assumption with a leak-adjusted model (T2-01-style: assume 30–50% of removed-instant volume does not return) and re-check whether the hypothesis survives; if it only works at 100% redistribution, the bar for launch should rise.
