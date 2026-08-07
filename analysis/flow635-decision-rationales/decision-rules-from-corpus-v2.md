# Decision rules of the 18-case revenue corpus — V2 (source-checked)

**Version.** V2 supersedes the V1 draft
(`agent-orchestrator-lab@ilzirasubs/flow-631-…:workspace/drafts/claude/decision-rules-from-corpus.md`),
which is preserved unedited. V1 was **induced from the numbers** of the corpus cards. V2 is
checked against the **Decision / Conclusion / Next steps sections of all 18 source Confluence
pages** (FLOW-635, pulled 2026-08-07). Where the team's wording contradicted an induced rule,
the wording won.

**What changed from V1.** One rule reformulated (R-06), three narrowed (R-03, R-04, R-11),
none dropped, four added that could not be induced from numbers at all (R-12…R-15). Both open
questions of V1 are resolved by quotation. Full diff and per-rule verdicts:
`03_rules_check.md`; verbatim sections: `01_verbatim_decision_sections.md`.

**Corpus scope (unchanged).** 18 cases, 8 rolled out / 9 killed / 1 stopped. The unit is a
whole project page; iterations inside a page are one case. Nothing outside these 18 cases
(holdout, excluded cases) contributes evidence. Every quotation below is verbatim from the
page, with the case id and ab_id it comes from; source typos are preserved.

**How to read a rule.** Each card states: the **claim**, the **evidence** (quotations, not
paraphrases), the **boundaries** — where the corpus does not support it — and a **strength**
label. `strong` = 3+ cases with explicit wording on both sides where the rule is two-sided;
`medium` = 2–3 cases or one-sided; `weak` = 1 case.

---

## R-01 — Significance on the goal metric is neither necessary nor sufficient

**Claim.** A p-value on the headline metric is an input to the decision, never the decision.
Cases were killed with a significant goal-metric lift and rolled out without one.

**Evidence.**
- T1-02 (6002/6128/6191), page-level `Decision`: "Even though ARPU is growing, we won't roll
  out the current solution yet."
- T1-08 (7487), `Decision`: "Can roll out variation 2 … no significant increase on arpu but
  only due to small segments."
- T3-06 (6326), `Conclusion`: "ARPU are not significantly changed in this read" → "Roll out to
  iOS Pro paywalls as tested".
- T3-01 (6026/6260): iteration 1 significant (+11.44%, p=0.01), decision taken on iteration 2 —
  "shouldn't rollout test variation".

**Boundaries.** The corpus never rolled out **against** a significant *harm* on the goal
metric — the asymmetry is only on the positive side. Significance still governs what may be
*claimed* (see R-13).

**Strength.** strong (6 cases, both directions).

---

## R-02 — The net increment decides; gross lift does not. Cannibalization kills.

**Claim.** More paying users is not more money. A decision is taken on the increment left
after the treated surface has taken traffic from other surfaces.

**Evidence.**
- T2-02 (6701), `Decision`: "the final results showed that due to cannibalization of other
  sources by the sale source, we ended up with less revenue despite having more paying users.
  Ultimately, we cannot use this mechanic permanently."
- T3-03 (7502), `Decision`: "The positive trial mechanics signal … does not offset the loss of
  instant annual subscription revenue — the two plans acted as substitutes, not additions."
- T1-04 (6359/6416/6428), `Conclusion`: "On iOS, Variation 2 shows a significant ARPU drop in
  the 'Without interstitial accesses' segment; hold iOS."
- T1-08 (7487), `Decision`: "Android — clear win, roll out. No cannibalization. / iOS — roll
  out, but watch full-price cannibalization."

**Boundaries.** Dilution is not an automatic veto: it is a veto when it turns the net negative
(T2-02), and a rollout condition when the net stays positive (T1-08 — net +$296 iOS / +$395
Android over the run). Do not compare a per-run dollar figure with a per-day forecast; they are
different units (this was V1's arithmetic error).

**V1 open question, resolved.** T1-08 was not rolled out *in spite of* the dilution analysis
and not by distrusting it: `Next steps` reads "Roll out variation 2 on iOS, with a post-rollout
watch on non-winback / full-price conversion (Total − Winbacks) to confirm the diffuse dilution
stays bounded and the net stays positive." The dilution was measured, accepted as bounded, and
converted into a rollout condition.

**Strength.** strong (4 cases with explicit wording).

---

## R-03 — Money-quality guardrails kill on their own; retention guardrails constrain the choice of variation

**Claim.** Cancels and refunds are treated as revenue and can kill a case single-handedly.
Retention and engagement are treated as a cost that can be traded: they bound which variation
is chosen, but no case in the corpus was killed by them alone.

**Evidence — money-quality guardrails kill.**
- T3-05 (6743), `Conclusion`: "Even with slightly increase in gross revenue due to higher trials
  share … we lose it because of 70% increase of refunds."
- T3-05 (6482), `Conclusion`: "both 14-day and 1-month post-charge cancellations increased
  significantly … the net ARPU impact is at risk" → "Do not roll out".
- T3-01 (6026), `Conclusion`: "can rollout variation#5 on iOS in two weeks if churn rate will
  be fine" — the guardrail stated as the rollout condition.

**Evidence — retention constrains the variation, not the case.**
- T1-07 (7160/7187), `Decision`: "variation #3 on Android has better monetization … but worsen
  retention" — while the case was decided on other grounds (see R-04).
- T1-04 (6359), `Conclusion`: "Variation 3 should be rejected: it hurts Android retention and
  downstream monetization" — variation rejected, case rolled out on Android with variation 2.

**Counter-example that sets the boundary (new in V2).** T3-05 (6875) was rolled out on the very
variation carrying `retention 1d: -4.8%`, `retention 7d: -2.5%`, `retention 14d: -2.1%` —
"Recommendation: Roll out, but staged. Prefer C (three-level paywall)". Retention loss was
accepted against ARPU +19% and 14d cancels −20%. V1's "a guardrail breach kills on its own" is
false as stated for retention.

**The asymmetry holds.** A guardrail *win* never rolled anything out on its own; it supports an
already positive case — T3-06: "Charge conversion increases strongly and early cancellations
drop by ~42%-46%, while engagement and retention remain unchanged."

**Strength.** strong for money-quality guardrails (3 cases); medium with an explicit
counter-example for retention.

---

## R-04 — The unit of account is money on the surface the treatment reached; there is no absolute threshold

**Claim.** Decisions are reasoned in dollars, not percentages — but in dollars **attributable
to the changed surface**. The corpus carries no cut-off of the form "we do not ship for less
than $X/day".

**Evidence — money is the unit.**
- T1-07 (7160/7187), `Next steps`: "It was decided not to roll it out because the revenue was
  too low." — no number, no comparison threshold.
- T1-01 (4845), `Conclusion`: "average accesses per day are so insignificant, there is no reason
  in rollout this variation."

**Evidence — but not the all-surface forecast.**
- T1-10 (7712), `Decision`: "The headline Forecast understates the change and should not drive
  the call. The projected rollout effect is about −$215/day on iOS and −$110/day on Android, but
  it is built on Total ARPU, which averages the treated interstitials (12% of iOS and 17% of
  Android cohort revenue) together with the untouched surfaces that supply the rest and drifted
  independently."

**V1 open question (no threshold), resolved.** V1 could not reconcile T1-07 (+$474/day judged
insufficient) with T1-08 (+$151/$107 per day accepted), and guessed T1-07 was really killed by a
retention guardrail. The page says otherwise: the only ground given is "the revenue was too
low", and the recommended variation carried an execution defect that made its number
untrustworthy — "i do not recommend full roll out since for some reason variation #2 had 75-77%
lower conversion from interstitial to banner which needs further investigation (or relaunch to
test)". The two cases were decided on different grounds (an untrustworthy number vs a verified
segment win), not on different thresholds. **There is no threshold in the corpus**, and no
cross-case comparison of forecast magnitudes is licensed.

**Boundaries.** Do not read this rule as "always compute $/day". Read it as: name the money,
and name the population it belongs to.

**Strength.** strong as a unit of account; strong as a *negative* claim about thresholds.

---

## R-05 — Reach is the first gate — both for the effect and for the measurement

**Claim.** A surface moves money in proportion to the audience it reaches; and a treatment that
reaches a small share of revenue cannot be judged on an all-revenue metric.

**Evidence — reach gates the effect.**
- T1-01 (4845): "no changes since we affect only a very small portion of users" /
  "average accesses per day are so insignificant, there is no reason in rollout this variation".
- T1-03 (6335): "96% of users leave at the very first pre-paywall, indicating there are problems
  with paywall reach."

**Evidence — reach gates the measurement (new in V2).**
- T1-10 (7712), `Insights`: "The goal metric could not have detected this. The two interstitials
  produce only 12.20% of iOS and 17.40% of Android revenue in the control branch."
- T1-09 (7454), `Decision`: "underpowered on the goal metric despite ~80k members/arm —
  interstitial-attributed conversions are only ~70–165 per arm."

**Boundaries.** Front-loading (impression #1 carrying ~50–60% of conversions, T1-09) is a
property of the App interstitial layer; do not transfer it to web landing funnels.

**Strength.** strong (4 cases).

---

## R-06 — Each iteration is judged on its own design; the case verdict belongs to the iteration that was shipped

**Claim (reformulated in V2).** A positive early read does not transfer to a changed design, and
a later negative iteration does not retract a rollout already made on an earlier one. "The last
iteration decides" (V1) is false as stated.

**Evidence — an early positive does not carry over.**
- T3-01 (6026 → 6260): iteration 1 "can rollout variation#5 on iOS in two weeks if churn rate
  will be fine"; iteration 2 "has no significant changes in arpu … shouldn't rollout test
  variation … probably price increase is too high to make the difference". Decided on iteration 2.
- T1-02 (6128 → 6191): "despite fixing only one part with ex subscribers we got 2-3 times worse
  results than in the previous iteration" → "We're not rolling out the solution yet".

**Counter-evidence to V1's wording.**
- T3-05: the rolled-out iteration is **#6875** ("Roll out, but staged. Prefer C"), while the two
  chronologically later iterations #7091 and #7178 both read "Do not roll out". They tested a
  different product (paid trial for the bundle), not a rollback of the intro offer.

**Boundaries.** This rule says nothing about which iteration is *right* — only about how the
corpus assigns verdicts. When citing a T3-05-style multi-iteration case, always name the ab_id
of the iteration the claim comes from.

**Strength.** strong (3 cases, including the one that breaks V1's formulation).

---

## R-07 — Under-delivery suspends the decision unless the harm is already significant

**Claim.** An experiment that did not reach its designed sample/duration produces "re-run", not
"no" — unless the negative is already significant at the delivered sample.

**Evidence.**
- T1-10 (7712), `Decision`: "iOS — hold and re-run, do not discard. … It is still not
  significant (p=0.22 on surface ARPU) because the run delivered 9 of the 15 designed days";
  `Next steps`: "Run the re-test to the designed exposure."
- T2-07 (6806): delivered 4 of 10 designed days on Android ("duration of exp >= design:
  incomplete"), yet "Do not roll out. The 10-second post-action paywall for free users …
  significantly suppresses access conversion on both iOS (-36%) and Android (-28%)."

**Boundaries.** Applies to delivery shortfalls (days, sample, arms), not to maturity shortfalls —
those are R-13.

**Strength.** strong (a clean pair, both sides quoted verbatim; upgraded from V1's "medium").

---

## R-08 — Platforms are decided separately, because they differ in elasticity

**Claim.** No case in the corpus forced one decision across platforms; platform splits are
treated as different markets, not as noise.

**Evidence.**
- T1-04 (6359): "Do not roll out globally. Variation 2 is a clear win on Android … On iOS …
  hold iOS."
- T2-05 (6614): "should roll out expensive test variation in iOS and keep cheap control on
  Android".
- T1-08 (7487): "Android — clear win, roll out. No cannibalization. / iOS — roll out, but watch
  full-price cannibalization."
- T1-10 (7712) names the mechanism: "Android — no case for the $29.99 step. … This is price
  elasticity, not execution: same offer, same creative, same triggers as iOS."

**Boundaries.** The corpus separates iOS/Android on App surfaces and treats UG_WEB as its own
world (T3-02, T3-03, T3-05). It says nothing about geo or locale splits.

**Strength.** strong (4 cases).

---

## R-09 — A large number is not accepted until it is shown not to be an artifact

**Claim.** Every rollout on a large relative number was preceded by an artifact check, and two
cases were killed *because* the number turned out to be an artifact.

**Evidence.**
- T2-05 (6614): "iOS wiback subscriptions were tracked as upgrades thus real profit from the
  current restart splashes is ~10 times lower than expected."
- T1-09 (7454): "The one apparent win (winback paywall +4.6×) was an attribution artifact, not
  real engagement."
- T2-06 (6515): the targeting bug was quantified before acceptance — "but overall it had no
  affect on monetization / only 6 subscriptions from iOS and 26 on Android" → "roll out with
  fix: remove users with trials from anniversary funnel".
- T2-05 (6863): "had problem with tracking subscription events in test variation" → do not roll
  out, fix the events first.
- T1-08 (7487): the segment win checked by the Total − Winbacks subtraction against the
  untargeted population.

**Boundaries.** None found — this is the best-supported rule in the corpus and has no
counter-example.

**Strength.** strong (5 cases).

---

## R-10 — Rolling out on an interim read is recorded as a mistake, not a practice

**Claim.** The one case rolled out before the final read is the one case the corpus disowns.

**Evidence.**
- T2-02 (6701), `Decision`, carrying a Red FAIL status on a rolled-out case: "Based on early
  results and increasing conversion in the sales funnel, we rolled out the experimental group to
  everyone … However, the final results showed that due to cannibalization … Ultimately, we
  cannot use this mechanic permanently."

**Boundaries.** One case. It is a warning, not a base rate. Note also that this is the only
place in the corpus where a **decision procedure**, not a result, is named as the failure.

**Strength.** weak as a rule, strong as a warning (unchanged from V1, now quoted directly).

---

## R-11 — Post-rollout reality lands at or below the forecast, never above

**Claim.** In every case with an actual post-rollout comparison, the shipped result met or
undershot what the experiment implied.

**Evidence.**
- T3-02 (7268), `Post-Rollout Analysis`: "This comes in below what the experiment led us to
  expect: the two-year per-cohort uplift is only +1.5%…" and "Charges grew by +77.5%, notably
  below the growth observed in the experiment (+88.9%). This gap is the main reason full-rollout
  revenue came in essentially flat (-0.45%)."
- T2-02 (6701): post-rollout revenue negative on a case rolled out as positive.
- T2-06 (6515), `Post-rollout analysis`: confirms the expectation — "current revenue per day
  iOS: $1100, Android: $300".

**Boundaries (narrowed in V2).** V1 counted four cases and included T3-06 ("forecast +$353/day
against a plan of +$500/day"). That is a *hypothesis vs forecast* comparison inside the design,
not a post-rollout observation — T3-06 has no post-rollout section at all. The rule rests on
**3 cases**: 2 below expectation, 1 confirming, none above.

**Strength.** medium (n=3, directionally consistent).

---

## R-12 — Judge the decision on the surface the treatment actually changed (new in V2)

**Claim.** Where a treatment touches one surface inside a wider funnel, the corpus judges it on
that surface's metric and explicitly disqualifies the all-surface metric.

**Evidence.**
- T1-10 (7712), `Next steps`: "Do not reuse Total ARPU as the goal metric for surface-scoped
  paywall tests. Size and judge them on the segment that the treatment actually reaches."
- T1-08 (7487): the whole decision is built on the Total − Winbacks split — "Members are
  identical across the Total and Winbacks segments, so the subtraction is a clean 'winback vs
  everything else' attribution."
- T1-04 (6359): the iOS hold rests on the "Without interstitial accesses" segment, not on Total.
- T2-05 (6404): "The 'Without winback accesses' segment shows no significant changes, supporting
  causality from the treatment."

**Boundaries.** This is a rule about the *decision* metric, not about what may be shipped: the
net across surfaces still governs (R-02). The two work together — measure on the treated
surface, decide on the net.

**Strength.** strong (4 cases; stated as an explicit instruction on one of them).

---

## R-13 — Data maturity bounds what may be decided, separately from sample size (new in V2)

**Claim.** Charge/cancel/refund conclusions are held back until the 14-day charge window closes;
the corpus uses a 5% pending-charge gate and states explicitly what is not interpretable yet.

**Evidence.**
- T1-10 (7712): "Pending 14d charges sit far above the 5% gate in every branch, so churn and
  refund movements — including the large nominal Android churn number — are not interpretable at
  this snapshot."
- T1-08 (7487), `Next steps`: "Recheck churn 14d / refund 14d once the control 14d charge windows
  close (currently preliminary — pending-charge share > 5% on control branches)."
- T3-03 (7502), `Next steps`: "Re-check churn and refund metrics in ~2 weeks once the 14d charge
  window matures (currently Pending 14d Charges: Var B 24.0%, Var C 15.7% — preliminary)."
- T3-01 (6026), `Next steps`: "calculate full 14d churn to get accurate churn level for new
  prices."

**Boundaries.** Maturity gates the *guardrail* conclusions. Money conclusions on already-charged
subscriptions can be final while churn is still pending (T1-10 iOS: "trial-free and fully charged
on both sides, so it is a final read").

**Strength.** strong (4 cases, all with the same 14d framing).

---

## R-14 — Rollout is conditional by default: ramp, fix, monitor, or a preferred variation (new in V2)

**Claim.** "Rolled out" in this corpus almost never means "shipped as tested at 100%". Seven of
the eight rollouts carry an explicit condition in the same sentence as the decision; the eighth
is T2-02, which was rolled out on an interim read and is the corpus's own recorded mistake (R-10).

**Evidence.**
- T3-06 (6326): "Roll out to iOS Pro paywalls as tested but stage the rollout and closely monitor
  net revenue and renewal behavior."
- T3-05 (6875): "Recommendation: Roll out, but staged. Prefer C (three-level paywall)."
- T1-04 (6359): "Ship Variation 2 to Android only behind a ramp (10%→50%→100%) with guardrails:
  ARPU ≥ +10%, charge CR ≥ +5%, 1/7/14d retention not worse than -0.5%. Monitor cancels/refunds
  for 14 days." — the one place in the corpus where numeric rollout guardrails are written down.
- T2-06 (6515): "roll out with fix: remove users with trials from anniversary funnel".
- T3-02 (7268): "Rolling out lower prices, but we are also implementing a monitoring system to
  track whether the price reduction is being offset by the anticipated growth."
- T2-05 (6404): "roll out the iOS winback to the eligible canceled-subscriber cohort, while
  monitoring cancellations/refunds".
- T1-08 (7487): "Roll out variation 2 on iOS, with a post-rollout watch on non-winback /
  full-price conversion".

**Boundaries.** The conditions are stated but, except T1-04, not given numeric trip-wires, and no
page records whether a monitoring condition was later checked. Treat "rolled out" in the corpus
as "rolled out under a condition of unknown enforcement".

**Strength.** strong (7 of 8 rollouts).

---

## R-15 — A killed case is an iteration, not a closed direction (new in V2)

**Claim.** The corpus almost never terminates a direction: 16 of 18 pages name a concrete next
test, and several killed cases name the redesign that follows. (T2-01 has no next-step text at
all; T2-07's `Next steps` heading is empty. T1-03 and T3-06 carry the follow-up inside
`Conclusion` rather than under a heading.)

**Evidence.**
- T1-09 (7454): "The main direction is to personalize the offer, not only the message around the
  offer."
- T3-03 (7502): "Investigate the anchor effect: test whether keeping the instant annual plan
  alongside the 3-month trial plan avoids the substitution effect."
- T1-02 (6191): "We're not rolling out the solution yet; first, we're launching the next project."
- T2-02 (6701): "Potentially, this mechanic could work to boost major one-time sales events with
  organic traffic growth (Black Friday, New Year, Christmas)."
- The exception: T1-01 (4845) — "we are not planning future iterations with interstitial, so we
  close experiment as fail. But also we can re-use this landing in future experiments with
  paywalls."

**Boundaries.** This describes how conclusions are written, not whether the follow-up was run.
Do not read "next steps" as evidence that the next iteration happened.

**Strength.** strong as a description of the corpus (16 of 18 pages).

---

## What the source pages still do not contain

Checked against the pages themselves, not inferred from the cards. All four gaps of V1 survive
the source check — none of them is recoverable from these 18 pages:

1. **No decision threshold.** No page states a cut-off. T1-07's "the revenue was too low" is the
   closest, and it names no number (R-04).
2. **No cost of an experiment slot.** No page mentions what the run cost or displaced.
3. **No portfolio.** No page names what competed for the same slot, so "was this worth running"
   is unanswerable from the corpus.
4. **No decision owner.** No page names who decided or under what mandate. The closest is
   T1-10's "Final call is the DRI's" — a role, not a person or a rule.

One V1 gap is **now partly closed**: the declared preference between money and retention. It is
still not stated as policy anywhere, but the practice is legible enough to be written as R-03
with its counter-example.

**Structural caveats for anyone using these pages as evidence** (details in
`02_rationale_quality.md`): the colour status macro is not a reliable carrier of the decision —
T3-05 #6860 is Green SUCCESS over the text "do not roll out the current design globally", and
T2-02 is Red FAIL on a case that was rolled out. Read the text, not the badge.
