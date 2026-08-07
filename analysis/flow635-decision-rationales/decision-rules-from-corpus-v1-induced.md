> **Status: superseded draft, kept for comparison.**
>
> These eleven rules were induced from the corpus cards by numbers alone —
> matching conditions against outcomes, without reading what the team wrote.
> FLOW-635 checked them against the verbatim decision sections of the same
> eighteen pages: D-06 contradicted the source, D-03 and D-04 narrowed, D-11
> lost a case, and four rules appeared that numbers could not yield.
>
> The corrected set is `decision-rules-from-corpus-v2.md` in this directory.
> This file is not maintained; it exists so the difference stays visible.
>
> Rescued 2026-08-08 from an uncommitted task worktree where it was the only copy.

# Decision rules induced from the 18 corpus cases (draft)

Source: `revenue-kb-v1.3/knowledge_base.md` §4, all 18 evidence source cards.
Method: for every case, read what was decided (`decision`), what the result
class was, and which fields the card names as load-bearing. Then look for
conditions that separate `rolled-out` from `killed`.

Outcome split: 8 rolled out, 9 killed, 1 stopped as "hold and re-run".

**Status of this draft.** These are *induced* rules — what the team demonstrably
did, not what anyone declared. Each rule carries the cases it rests on so it can
be rejected. Rules resting on two cases are marked weak. The corpus records
*conditions* of decisions well and *reasons* for them only in fragments (two
cards quote the page verdict verbatim, the rest do not) — see "What is missing"
at the end.

---

## D-01 — Significance on the goal metric is neither necessary nor sufficient

**Killed despite a significant goal-metric lift:**
- T1-02 — iter2 iOS ARPU +7.5% (p=0.029) → killed
- T1-07 — iOS var2 ARPU +26.5% (p=0.011) → killed
- T3-01 — iter1 iOS ARPU +11.44% (p=0.01) → killed

**Rolled out despite a non-significant goal metric:**
- T3-06 — ARPU +5% (p=0.18) → rolled out
- T3-02 — ARPU +2.93% (p=0.45) → rolled out
- T1-08 — Total ARPU +9.3% (p=0.40) → rolled out

Six of eighteen cases were decided *against* the significance of their own goal
metric. The p-value on the headline metric is an input, not the decision.

**Strong** (6 cases, three on each side).

---

## D-02 — Net increment decides, gross lift does not. Cannibalization kills.

- T1-02 — killed with a significant lift: cannibalization 34% iOS / 63% Android,
  interstitial trial→charge below average
- T3-03 — killed: short plans cannibalized annual instant subscriptions
- T1-04 — iOS not rolled out: the segment without interstitial accesses read
  −24.7%, i.e. the new surface competed with existing ad inventory; Android,
  where the video replaced nothing, was rolled out
- T2-01 — the off-test measured incrementality directly and found conversion does
  **not** fully redistribute when a surface is removed

**Open contradiction.** T1-08 was rolled out while carrying a diffuse dilution of
−$702/day on iOS non-winback against a forecast of +$151/day iOS and +$107/day
Android. On the face of it the dilution exceeds the gain. The card marks the
dilution analysis as *exploratory* and its transfer bound says "iOS dilution
bounds the net increment" — so either the dilution was not trusted, or the
segment win was accepted on other grounds. **This needs the source page to
resolve.**

**Strong** for the killing direction, **unresolved** for the tolerance limit.

---

## D-03 — A retention / cancel / refund guardrail outweighs a money win

- T1-07 — iOS ARPU +26.5% (p=0.011) against Android D1 retention −9.15%
  (p=0.012) → killed
- T3-01 — tour ARPPU +7.34% (p=0.001) against refunds 14d +26.2% (p=0.006) and
  charge CR −11% → killed
- T3-05 — early UI iterations rejected on guardrails alone: print AOV −32.2%,
  cancels +37.4%, refunds +72.3%
- T3-06 — rolled out with a non-significant ARPU, and 14d cancels −42.2%
  (p=0.00) is named among the reasons

**The asymmetry is the finding.** A guardrail breach kills on its own. A
guardrail win never rolled anything out on its own — it only supports a case
that was already structurally positive.

**Strong** (4 cases).

---

## D-04 — The decision is taken in money per day, not in percent

- T1-07 — +26.5% relative translates to a forecast of +$474/day; the card names
  "significant relative lift ≠ sufficient absolute increment" as the lesson
- T2-06 — +3910% against a near-zero control base was rolled out, but only after
  post-rollout confirmed ≈$1100/day iOS and ≈$300/day Android in actual revenue
- T3-03 — killed with forecasts of −$918/day and −$1408/day
- T2-02 — post-rollout Forecast −$1716/day iOS on a case that had been rolled out

**Caveat that weakens this rule.** T1-08 was rolled out on forecasts of +$151/day
iOS and +$107/day Android — smaller in absolute terms than T1-07's +$474/day,
which was judged insufficient. So there is no absolute threshold in the corpus.
More likely T1-07 was killed by D-03 (the retention guardrail) and the small
absolute was the second argument, not the first.

**Weak as a threshold, strong as a unit of account.** The corpus consistently
reasons in $/day; it does not carry a cut-off.

---

## D-05 — Reach is the first gate, decided before any effect

- T1-01 — killed on reach: 4 accesses from the new source over the entire run;
  all monetization diffs n.s.
- T1-10 — stopped, not killed: 83–88% of revenue was untouched, making the goal
  metric "structurally blind"
- T1-04, T1-09 — both cards name front-loading of layer conversion (first
  impression does 50–87% of the work) as the binding constraint

No case in the corpus was rolled out on a surface with negligible reach, and no
case was killed on effect size before reach was established.

**Strong** (2 decisive cases, supported by the P-01 pattern across four more).

---

## D-06 — The decisive read is the last iteration, not the best one

- T3-01 — iter1 significant (+11.44%, p=0.01); iter2, run at ≈4.4× the design
  sample, read +1.38% (p=0.61). Decided on iter2 → killed
- T1-02 — iter1's +24%/+13% lift was a segment-contamination artifact (ex-premium
  ≈37% of revenue); iter2 was clean → killed
- T3-05 — six iterations; the intro iteration (6875) was rolled out, the
  paid-trial iterations (7091 stopped at −23.8%, 7178 −6.66% n.s.) were not

**Strong** (3 cases).

---

## D-07 — Under-delivery suspends the decision; it does not produce a negative one

- T1-10 — 9 of 15–20 design days, 2 of 3 arms live, 59–79% of charges still
  pending → "hold and re-run, do not discard". Explicitly not killed.
- T2-07 — sample far below design **but the negatives were significant anyway** →
  killed

The rule that separates them: incomplete delivery suspends a decision **unless
the harm is already significant at the delivered sample**.

**Medium** (2 cases, but they form a clean pair).

---

## D-08 — Platforms are decided separately

- T1-04 — rolled out on Android (ARPU +17–19% significant in both iterations),
  not on iOS (+2.66%, p=0.43)
- T2-05 — iOS win rolled out; Android expensive plans read −55% ARPU, with the
  page instruction "keep cheap control on Android"
- T3-06 / T3-01 — decided on iOS, with Android elasticity explicitly named as a
  different question

No case in the corpus forced a single decision across both platforms.

**Strong** (3 cases).

---

## D-09 — A large number is not accepted until it is proven not to be an artifact

- T2-05 — the control segment "without winback accesses" read n.s. (+6.47%,
  p=0.32), localizing the effect in the target cohort before rollout
- T1-08 — same structure: segment win checked against the untargeted population
- T2-06 — the targeting bug (splash shown to trial users) was **quantified**
  (6 iOS / 26 Android subs) and shown not to drive the result, before the +3910%
  was accepted
- T1-09 — the visible ×4.6 winback lift was found to be an attribution artifact
  → killed
- T2-05 iter3 — a subscription-tracking bug fabricated a −30% conversion read

Every rollout on a large relative number was preceded by an artifact check. Two
cases were killed *because* the number turned out to be an artifact.

**Strong** (5 cases).

---

## D-10 — Rolling out on an interim read is recorded as a mistake, not a practice

- T2-02 — rolled out before the final read; finals came back n.s. (ARPU iOS
  −2.95% p=0.66) and post-rollout Forecast was −$1716/day iOS. The card files
  this under lessons (P-12, P-13), not under decision rules.

This is the one rollout in the corpus that the corpus itself disowns.

**Weak as a rule** (1 case), **strong as a warning** — it is the only case where
the decision procedure, rather than the result, is named as the failure.

---

## D-11 — Post-rollout reality lands at or below the forecast, never above

- T3-02 — post-rollout full revenue ≈ flat (−0.45%) against a significant
  pre-rollout read; the card says "below what the experiment led us to expect"
- T3-06 — forecast +$353/day against a plan of +$500/day
- T2-02 — post-rollout negative on a case rolled out as positive
- T2-06 — post-rollout **confirmed** the revenue (≈$1100/day iOS)

Of the four cases with a post-rollout comparison, three landed below expectation
and one confirmed it. None landed above.

**Medium** (4 cases) — directionally consistent, small n.

---

## What these rules do NOT contain

The corpus supports the rules above and is silent on everything below. Each of
these is a real input to a launch decision that no card records:

1. **No effect threshold.** There is no "we do not run for less than $X/day".
   D-04 shows the corpus reasons in $/day but carries no cut-off, and T1-07 vs
   T1-08 shows a smaller forecast being accepted where a larger one was not.
2. **No cost of an experiment slot.** Nothing about what running this costs, what
   it displaces, or how long a slot is worth holding.
3. **No portfolio.** No card says what else was competing for the same slot, so
   "is this worth running at all" cannot be answered from the corpus.
4. **No declared preference between money and retention.** D-03 shows that in
   practice a retention breach kills a money win — but as an observed regularity
   over four cases, not as a stated policy. If the policy is real, it should be
   written down rather than re-derived.
5. **No decision owner.** Cards record what was decided, never by whom or under
   what mandate.

## What is missing from the corpus and exists on the source pages

Two cards quote the page verdict directly:

- T2-01 — note: *actual verdict on the page: "We're not rolling out the
  experiment"*
- T3-01 — outcome fact: *page verdict "price increase too high"*

The other sixteen carry conditions but not the team's own words. Those pages
almost certainly end with a Decision / Conclusion section explaining why the
result was read as a failure and why it was not rolled out — exactly the
material these rules are induced from indirectly.

**Next step to harden this draft:** pull the Decision/Conclusion sections of all
18 source pages through `scripts/cnfl` and check each rule against what the team
actually wrote. Where the stated reason contradicts the induced rule, the stated
reason wins and the rule is corrected.
