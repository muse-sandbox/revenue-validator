**Verdict: redesign before launch.** The idea (make one-click payment options visible on the payment page) is cheap and directionally sensible, but the documented design cannot test its own hypothesis: the power calculation is built around a 500% lift while the hypothesis claims 3%, the goal metric starts upstream of the touched surface, and the desktop-only audience excludes the small screens the problem statement is about.

**Predicted outcome.** [hypothesis] Small positive-to-null effect on payment-page→purchase conversion, with a likelier and larger shift in payment-method mix (toward PayPal/Apple Pay/Google Pay) than in total conversion — visibility changes usually reroute buyers before they recruit new ones. Under the documented design (1,996/arm, baseline 0.05%), the realistic outcome is an unreadable null. It would surprise me if a layout compaction produced a significant total-conversion lift at that sample; it would also surprise me if arm B (header removed) hurt conversion, but that direction is live — stripping header/trust elements from a card-details page can reduce trust, and this is ungrounded assumption, not corpus-backed.

**Top risks & failure modes**
- **Power design is internally incoherent (P-12).** Baseline 0.05%, lift 500%, n=1,996/arm detects only absurd effects. Detecting the hypothesized 3% relative lift on a 0.05% baseline needs orders of magnitude more users; as designed, a null is guaranteed and uninterpretable.
- **Goal metric mis-scoped to the touched surface (P-11).** "Users tab view → subscribed" starts far upstream of the payment page; T1-10 shows a diluted goal metric structurally drowning a real surface effect. The 0.05% baseline itself suggests the denominator is all tab viewers, not payment-page reachers — verify the metric definition (P-14).
- **Platform/problem mismatch.** The stated problem is buttons not fitting the viewport "especially on small screens", but the experiment runs desktop-only, where the problem is weakest. A null here says little about the hypothesis.
- **No exposure event (P-12).** The Analytics section is blank, so exposure-scoped SRM and activation checks are impossible; assignment-level SRM on a funnel this deep is a weak substitute.
- **Payment-mix side effects (L3 signal, T3-05).** Earlier UI iterations in the web funnel line were rejected on guardrails (cancels +37.4%, refunds +72.3%, print AOV −32.2%) — [fact] from T3-05. [hypothesis] Arm C's reordering could shift method mix with different refund/renewal-failure profiles per method; guardrails, not the primary metric, are where this experiment can silently lose.

**Analogs**

no direct analogs

The corpus contains no checkout-page UX/layout case; the cards below compute to L3 and are used only for measurement, guardrails and sizing — not as a basis for the verdict.

```yaml
analog:
  source: T3-05 (ab 6464..7178; 2025-08..2026-06; SRM ok; mixed; rolled-out intro iteration)
  axes:
    flow_stage: exact            # S5–S6 web purchase funnel in both
    segment: adjacent
    trigger_eligibility: adjacent
    surface: adjacent            # paywall/offer chain vs payment page — same funnel, different page
    mechanism: different         # offer structure vs pure layout
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: different    # trial→charge chain vs payment-page→purchase
  platform: exact
  level: L3
  transferable: >
    [fact] Earlier UI iterations in this web-funnel series were rejected on
    guardrails: cancels +37.4%, refunds +72.3%, print AOV -32.2% (T3-05).
    [hypothesis] L3 measurement/guardrail lesson only: a web checkout UI
    change needs cancel/refund/AOV guardrails with 14d maturity, because UI
    wins in this funnel have died on guardrails before.
  not_transferable: >
    All magnitudes; every offer-structure product conclusion (different
    mechanism); no product conclusion about layout changes transfers.
```

```yaml
analog:
  source: T3-02 (ab 7268; 2026-04; refund 14d included; significant-positive; rolled-out)
  axes:
    flow_stage: exact
    segment: adjacent
    trigger_eligibility: adjacent
    surface: adjacent            # paywall+checkout prices vs payment-form layout
    mechanism: different         # price change vs layout
    offer: different
    behavior: adjacent
    metric: adjacent
    money_chain: adjacent
    guardrails: adjacent
  segment_monetization_state: different
  money_chain_link: different
  platform: exact
  level: L3
  transferable: >
    [fact] Web funnel read included cancel/refund 14d and a comeback-offer
    guardrail (-20%); post-rollout revenue came in below the experiment read
    (T3-02). [hypothesis] L3 sizing/measurement lesson only: use this case's
    funnel baselines for sample sizing and expect experiment-to-rollout
    shrinkage.
  not_transferable: >
    All magnitudes; the price-decrease product conclusion (different
    mechanism, different money-chain link).
  sizing_prior: >
    prior: web desktop funnel volumes/CRs from T3-02 are the closest
    available baselines for recomputing the sample size on a
    payment-page-scoped metric.
```

**## Non-monetization effects to instrument**
- **Trust/anxiety on the card form (negative and positive):** removing the header and compacting a payment page can reduce trust cues, or reduce abandonment via less scrolling. Instrument: form-start rate, field-abandonment, back-navigation from the payment page. Stop-rule: payment-page abandonment up significantly in B or C.
- **Payment-method mix (both directions):** alt-buttons-first (C) may raise one-click share — faster checkout, possibly better renewal reliability — or cannibalize card payments with worse refund/chargeback profiles. Instrument: method share per arm, refund/chargeback rate by method, renewal-failure rate by method. Stop-rule: refunds or payment failures significantly up.
- **Engagement/upper funnel:** none expected upstream (change is at the funnel's end), but instrument return-visit purchase completion for users who abandoned once — faster checkout could help second attempts.
- **Support contacts:** payment-page confusion shows up in support tickets before metrics; tag and count payment-related contacts per arm.

**Design & measurement checklist**
- Primary metric: payment-page reached → purchase, per arm; secondary: method mix, time-to-complete. Keep "tab view → subscribed" only as a dilution/guardrail read (P-11).
- Recompute power from the real payment-page baseline and the 3% hypothesis; expect a much longer run or acceptance of a larger MDE (P-12).
- Define the exposure event (payment-page render with assigned layout) before launch; SRM on exposed users, not assignments (P-12).
- Include small-viewport traffic (mobile web, or at minimum segment desktop by viewport height) — that's where the hypothesis lives.
- 14d refund/cancel maturity before the final read; trial purchases via this page inherit the trial-window lag (P-13).

**Changes that would most improve expected value**
1. Rescope the primary metric to payment-page→purchase and re-derive sample size from its actual baseline — this alone decides whether the experiment can say anything.
2. Run where the problem is: add mobile-web/small-viewport arms or segments, rather than desktop-only.
3. Split the two changes cleanly: B (compaction) vs C (button reordering) already do this — keep both arms and pre-register method-mix plus refund guardrails so a mix shift isn't mistaken for a win or missed as a loss.
