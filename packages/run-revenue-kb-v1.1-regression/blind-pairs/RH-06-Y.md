This is an arm-B validation: I'll assess the RH-06 pre-launch card against the KNOWLEDGE CONTEXT.

## 1. Verdict

**Redesign before launch.** The idea is testable, but the design cannot answer its own question: the stated sample (1,602 plan-menu views/arm) is ~18× above what the card's own baseline (~479 views per ~16 days ≈ 30/day) can deliver in 6 days, the goal metric doesn't sit on the money-chain link the treatment moves, and a 7-day read structurally penalizes the trial-shifted arm before trials mature.

## 2. Predicted outcome

[hypothesis] Plan-menu→access CR likely rises (default-selected trial + fewer options makes "access" mechanically easier), but charges and net revenue in the read window are flat-to-down: the removed $19.99 instant carried ~32 of ~98 channel accesses, and the substitution evidence (T3-03, P-06) plus web price elasticity (T3-02, P-07) argue that demand will not re-sort into trials and higher-priced offers as modeled. What would surprise me: trial accesses genuinely ~7×ing (8→56) *while* trial access→charge simultaneously improves 24.18%→30% — both assumptions are counter-evidenced (T3-06, P-05).

## 3. Top risks & failure modes

- **Substitution, not migration:** menu offers are substitutes (P-06, T3-03); removing the cheapest acceptable instant likely loses its buyers rather than converting them to trials — the model's central assumption.
- **Trial mechanics overrated:** the corpus's instant-vs-trial line (T3-06, T3-05, P-05) shows instant charges beat trial mechanics on charge quality; RH-06 runs that mechanism in reverse while also raising prices.
- **Goal-metric mismatch:** plan-menu→access can win while net revenue loses; a trial start is not a charge (different money-chain link) — P-11.
- **Power/delivery failure:** ~30 plan-menu views/day and ~6 accesses/day cannot support the stated 6-day sample or any revenue read — P-12. Also the hypothesis says +$500/day while the model shows +$501 over the whole modeled slice (~$31/day) — a ~16× internal inconsistency in the success criterion.
- **Compound treatment:** strip creative + menu removal + two price increases + exit offer + cancellation-funnel changes in one arm — a null or negative is unattributable, and the creative changes the population entering the funnel.

## 4. Analogs

```yaml
analog:
  source: T3-03 (ab 7502; 2026-05..06; SRM ok, pending 14d 24%/15.7%; significant-negative; killed)
  axes:
    flow_stage: exact            # S5–S6 web plan menu in both
    segment: exact               # web new/unconverted in both
    trigger_eligibility: adjacent
    surface: adjacent            # web plan menu; different funnel entry/scope
    mechanism: exact             # offer-structure: plan-menu composition
    offer: different             # added cheap short plans vs removed discounted instant
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact        # menu choice → purchase/trial-start in both
  platform: exact
  level: L1
  transferable: >
    [fact] Adding 3m/6m plans to the web menu: members→subscribers −11.08%
    (p=0.028), buyers −11.90% (p=0.038); short plans cannibalized annual
    instants; trial sub-mechanics were positive (trial→charge +21.7–25.8%)
    yet the net was negative (T3-03). [interpretation] Menu offers are
    substitutes, not additions (P-06). [hypothesis] Transfer as sign +
    mechanism, direction-reversed with caution: the $19.99 instant is likely
    carrying its own demand (32/98 accesses), not stealing trial demand;
    removing it risks losing those buyers, and positive funnel sub-metrics
    can coexist with revenue loss.
  not_transferable: >
    Magnitudes (−11%; forecast −$918…−$1408/day). The source tested ADDING
    plans; removal is the untested reverse — this card is a warning about the
    substitution mechanism, not a measured removal effect. Read had pending
    charges 24%/15.7%.
```

```yaml
analog:
  source: T3-05 (ab 6464..7178; 2025-08..2026-06; SRM ok all iterations; mixed; intro iteration rolled-out) — scoped to the plan-menu-composition iterations
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: adjacent
    surface: adjacent
    mechanism: exact             # plan composition / instant-vs-trial offer structure
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L1
  transferable: >
    [fact] Plan-menu iterations lost; the winning iteration was an
    intro/instant offer (ARPU +12.1–19.2% significant, trial→charge
    +28.9–32%); paid-trial-as-cheap-instant failed twice (T3-05).
    [interpretation] Choice overload suspected on three-plan menus; intro/
    instant structure beats trial mechanics on conversion quality (P-05).
    [hypothesis] Simplification may help menu→choice conversion, but RH-06
    removes exactly the offer type this line found strongest on web and bets
    the channel on trial mechanics — against the measured direction.
  not_transferable: >
    All magnitudes (vary by iteration); the intro-offer wins sit on the
    post-trial-start chain, not the plan menu; the rolled-out variant carries
    a measured retention minus and a wrongful-charge caveat.
  conflict: >
    With T3-03 on "fewer options": T3-05's choice-overload reading
    (interpretation, 2025-08..2026-06) mildly supports a two-option menu;
    T3-03 (2026-05..06, significant) implies the removed cheap instant
    carries real demand. Not averaged: T3-03 is significant and closer to the
    removal question, so its warning dominates the revenue read.
```

```yaml
analog:
  source: T3-06 (ab 6326; 2025-06..09; SRM ok, duration complete; mixed; rolled-out)
  axes:
    flow_stage: adjacent         # S6 App purchase conditions vs S5–S6 web menu
    segment: adjacent
    trigger_eligibility: adjacent
    surface: different           # iOS internal paywalls vs web plan menu
    mechanism: exact             # instant-vs-trial offer structure (reversed direction)
    offer: adjacent
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: different            # App vs Web
  level: L2
  transferable: >
    [fact] Replacing trial with a discounted instant on iOS internal
    paywalls: charge CR +16.4% (p=0.00), trial→charge −39.5%, 14d cancels
    −42.2%; ARPU +5% n.s. (T3-06). [interpretation] Instant charges collect
    committed users; the trial step loses ~40–60% at trial→charge (P-05).
    [hypothesis] Warning only (L2): RH-06 reverses this mechanism, so expect
    fewer immediate charges and more early-cancel exposure in the trial-heavy
    arm; the modeled trial→charge improvement (24.18%→30.00%) has no support.
  not_transferable: >
    iOS/App magnitudes and elasticity (web differs — T3-02); the reversed
    direction is untested; long-term EV of instant cohorts was itself under
    post-rollout monitoring.
```

```yaml
analog:
  source: T3-02 (ab 7268; 2026-04; members diff 0.95%, 14d included; significant-positive; rolled-out)
  axes:
    flow_stage: exact
    segment: exact
    trigger_eligibility: adjacent
    surface: adjacent
    mechanism: adjacent          # pure price change vs composite menu restructure
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: exact
    guardrails: adjacent
  segment_monetization_state: exact
  money_chain_link: exact
  platform: exact
  level: L3
  transferable: >
    L3 — sizing/guardrail signal only, not an analog and not a verdict basis.
    [fact] Web entry-price DECREASE: Charge CR +88.91%, Access CR +68.87%
    (p=0.00), revenue fact +4.18%, post-rollout ≈flat; comeback-offer CR −20%
    as guardrail (T3-02). [hypothesis] Sizing lesson: web volume is strongly
    price-elastic, so the $19.99→$24.99 exit repricing and $39.99 instants
    should be sized with material volume loss; adopt save-offer CR as a
    guardrail.
  not_transferable: >
    All magnitudes; opposite price direction; the 3-year uplift was a model,
    not a fact.
```

## Non-monetization effects to instrument

- **Retention (both directions):** a cleaner two-option choice with a default trial could improve early subscriber satisfaction/retention; conversely, higher effective prices correlated with retention moving with price on web (T3-02 saw retention +1.3–3.6% under a *decrease*). Instrument D1/D7/D14 retention by arm and by offer type; stop-rule on significant D7 retention drop in the trial cohort.
- **Refunds/cancels:** "get full access free" creative plus a default-selected trial risks expectation mismatch → trial cancels and refunds (price increases drove refunds +26.2% in T3-01; guardrails killed UI wins in T3-05). Instrument 14d cancels/refunds per arm; stop-rule on refund-rate excess.
- **Upper-funnel (both directions):** new strip creative may lift CTR (+15% assumed) or shift the entering mix toward deal-seekers; the expiring-countdown-then-nothing-changes pattern can erode trust and decay strip CTR over time. Instrument strip CTR by day-in-experiment and exit-offer view/accept rates.
- **Engagement:** exit-intent interception can annoy; instrument funnel bounce/return rates.

## 6. Design & measurement checklist

- Re-scope the goal: decision metric = net charged revenue per strip-exposed visitor on this channel (P-11); plan-menu→access becomes a diagnostic, since the treatment deliberately trades charges for trial starts.
- Resolve the delivery math: at ~30 plan-menu views/day, the stated sample needs on the order of 100+ days, not 6 (P-12). Either extend massively, widen the MDE, or power on a higher-traffic event.
- Maturity gate: no final read until trial windows mature (pending-charge share <5%, P-13); a day-7 read structurally undercounts the trial-shifted arm's revenue.
- Reconcile the success criterion: +$500/day (hypothesis) vs +$501 per modeled multi-day slice (model) differ ~16×.
- SRM at strip-exposure level, not only the experiment-start event; verify strip-view logging parity given the creative differs by arm.
- Guardrails: save/exit-offer CR, 14d cancels/refunds, monthly-plan mix shift, retention D1–D14.

## 7. Changes that would most improve expected value

1. **Unbundle the treatment:** separate arms (or sequential tests) for menu simplification vs price increases vs strip creative — otherwise no outcome is attributable.
2. **Keep one arm with the exit offer at the unchanged $19.99** to isolate "move the discount out of the menu" from "raise its price" — this is the cheapest hedge against the elasticity risk (T3-02 L3 sizing signal, P-07).
3. **Re-power on charges/net revenue with a matured trial window** and pre-register the surface-scoped revenue metric as decisive.
