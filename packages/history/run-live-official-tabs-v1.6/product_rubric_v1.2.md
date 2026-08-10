# Product-argument rubric V1.2 (FLOW-642)

**Status: canonical.** Supersedes `product_rubric.md` (V1.0, FLOW-628) and the
unapproved patch `product_rubric_v1.1.md` written by the FLOW-632 executor and
applied by the V1.4 run. This file is self-contained — grade against it alone,
do not read V1.0 alongside it.

**What changed and why.** FLOW-631 found two holes that made the rubric
unusable as a ruler: Q3 counted invented numbers (§Q3 below), and the boundary
between a product argument and a methodological remark was undefined, so the
same answer scored 2 or 3 depending on the grader (§Boundary below). Both holes
move the *baseline*, not the new run, so §Effect on published scores restates
every score already published under the old readings.

**Relation to the V1.1 patch.** V1.1 is accepted in substance and superseded in
form. V1.2 keeps its two rules, states them as rules of the rubric rather than
as a proposal, adds the worked examples the tickets asked for, and adds three
adjudications V1.1 left open: what the Q3 denominator is, what happens when a
stated operation does not reproduce, and whether operational feasibility is a
product argument. §Changelog lists each and says whether it moves a published
number.

---

## Scope

The **product** half of the validator answer — arguments for or against the
pitch itself. The experiment-methodology half stays under the linter and the
evidence policy; §Boundary draws the line.

## Normalizations

Carried over from V1.0 unchanged. Each is flagged so it can be rejected.

1. **Two units of evaluation.** Q1–Q4 apply to *each* product argument. Q5–Q9
   apply to the answer as a whole. The original list mixed both.
2. **"Yes" always means good.** Q7 was inverted (`contains duplicated
   information?` → `is free of duplicated information?`) so the score is
   monotone.
3. **Q1 is a classifier, not a score.** "Is the argument framed as an assumption
   or a hypothesis?" reads as *what kind of statement is this*, which then
   routes Q2 (a fact needs a source; an assumption needs to be labelled as one).
   It awards no points on its own.

## Claim level — applied to every product argument

| # | Question | Yes = |
| -- | -- | -- |
| Q1 | Statement type: fact / interpretation / hypothesis / bare assumption | classifier only |
| Q2 | Does the statement have a source, or an explicit confidence when it has none? | traceable |
| Q3 | Does the claim say that the target metric will move, **with a magnitude or a decision threshold whose origin is traceable** — not only a direction? | decision-grade |
| Q4 | Is it phrased as "if we do X, grounded in Y, then Z happens to a named metric"? | actionable form |

`Q1` routes: a statement classified as fact must pass Q2 against the evidence
base; a statement classified as hypothesis or assumption must pass Q2 by
carrying its own confidence label. An unlabelled assertion with no source fails
Q2 outright.

## Document level — applied once

| # | Question | Yes = |
| -- | -- | -- |
| Q5 | Do the conclusions avoid contradicting each other? | consistent |
| Q6 | Where they do contradict, did the agent name the inconsistency and resolve it? | self-aware |
| Q7 | Is the answer free of the same idea restated in different words? | non-redundant |
| Q8 | Do the proposals reach project direction, strategy or monetization tactics — not only the mechanics of this one pitch? | strategic altitude |
| Q9 | Is the answer free of cheap generic UI changes? | substantive |

Q6 is evaluated only when Q5 is "no". When Q5 is "yes", Q6 is not applicable and
does not count against the score.

---

## Q3 — the magnitude must be traceable (hole 1)

**What went wrong.** In the FLOW-631 run the arm *without* a knowledge base
produced magnitudes freely — "ARPU +8–18% vs control", "retention −0.7…−1.5 pp,
outside the working −0.5 pp margin" — and flagged them itself as ungrounded. By
the letter of V1.0 they counted. The arm *with* the base produced none, because
prompt rule 4 forbids transferring magnitudes, and scored Q3 = 0. The rubric
rewarded the fabricator over the disciplined answer, which is the opposite of
what it exists to do.

**Rule.** Q3 counts a claim only when **every** number in it has one of the
three origins below **and the claim says which**:

1. **Computed from the card under review.** The number appears in the
   experiment card, or is the result of an operation over card numbers that the
   claim states well enough for a reader holding the card to reproduce it. This
   is the `[computed]` label of KB §2.8; where the answer uses that label, run
   the linter with `--card` before scoring.
2. **Borrowed and marked as borrowed.** The number comes from a cited source,
   carries its ID, and is labelled a sizing prior rather than a prediction, as
   rule 4 requires. A borrowed number counts **only if the claim also names what
   it is being compared against** — a bare prior with no decision threshold is
   not a decision-grade statement.
3. **Stated by the team in the card.** The card's own expected effect, approved
   guardrail margin, MDE or baseline, quoted as such.

A number with none of these origins does not count, however confidently it is
phrased, and it is recorded as a defect on the same line of the score table.

### Three adjudications

**(a) A stated operation that does not reproduce disqualifies the claim.** The
rubric does not grade whether the underlying evidence is *true* (§What the
rubric does not measure). It does grade whether an arithmetic step the answer
performs on card numbers comes out right, because that is checkable from the
card alone and it is the only thing separating origin 1 from a guess. Record it
as `arithmetic-does-not-reproduce`, a different defect from fabrication.

**(b) A card number restated in another unit must name the field it came from.**
Turning `MDE 0.020` into "the design resolves ~2 pp" is an operation, not a
quotation, and it silently changes the unit. If the claim does not name the
field and the conversion, the number is not traceable. See the worked example
below — this exact conversion is wrong by 2×, and it survived three runs
precisely because nobody could see which field it came from.

**(c) Q3 is per claim, not per number.** One untraceable number in an otherwise
grounded claim fails the whole claim. Splitting a claim into two sentences to
quarantine the bad number does not help: the grader scores the assertion, not
the sentence.

### Worked examples

| Claim | Q3 | Why |
| -- | -- | -- |
| "ARPU +8–18% vs control" (FLOW-631 arm A) | **no** | fabricated — no card number, no source ID, no operation |
| "retention −0.7…−1.5 pp, outside the working −0.5 pp margin" (FLOW-631 arm A) | **no** | the threshold (−0.5 pp) is the card's, the magnitude is invented; per (c) the claim fails |
| "the sample resolves ~2 pp against the approved −0.5 pp margin — four times finer" (FLOW-624) | **no** | `MDE 0.020` is Cohen's *h*, not pp; the card's own −2.37% × 42.14% baseline gives **1.00 pp**, so the true ratio is 2×, not 4×. Fails (a) and (b) |
| "a −0.5 pp margin on a 42.14% baseline needs ~10⁵ users/arm at 80%/0.05; the design carries 38,147, so the approved margin cannot be tested as designed" (FLOW-624, appendix B) | **yes** | all inputs are card fields, the operation is named and reproduces (153,098), it names the decision threshold, and it closes on the decision |
| "42.14% × 2.37% ≈ 1.0 pp against an approved 0.5 pp margin — a null is compatible with a two-fold loss" (FLOW-632 / V1.4) | **yes** | origin 1, operation written out in the claim, threshold named |
| "beginners lost −42.1% access CR in T2-07" used to size this case | **no** | origin 2 without the second half: a borrowed magnitude with no decision threshold in this case |
| "the demo reaches ~78% of the arm, minus the ~27% of songs without Simplify" | **no** | card numbers, but they size the *dose*, not the effect, and no threshold is named |
| "…therefore a true +20% reads as ~+11%, below what this design can detect" | **yes** | same card numbers, carried through to a magnitude and compared with a threshold |

The last two rows are the whole point of the fix: identical inputs, and only the
second one can stop a launch.

---

## Boundary — product argument vs methodological remark (hole 2)

**What went wrong.** "MDE −2.37 pp against an approved margin of −0.5 pp — a
null here is uninformative" scored 3 when read as a product argument and 2 when
read as methodology. V1.0 did not say which, so a whole point moved on the
grader's taste and two runs stopped being comparable.

**Rule.** A claim about what the design can or cannot resolve is a **product
argument** when both hold:

- it connects a *product* quantity — the expected effect of the mechanic, the
  share of the arm actually exposed, the dose treated users receive, the
  approved margin — to a decision threshold; **and**
- it is about the decision on the **idea**: what this experiment will or will
  not be able to tell us, and therefore what running it as designed would and
  would not settle.

A claim is **methodology**, and stays out of the rubric, when it is about the
*correctness of the measurement* rather than about what the measurement can
decide.

**The boundary is the consequence, not the vocabulary.** A claim may use MDE,
power or exposure and still be a product argument; a claim may avoid all of them
and still be methodology.

| Claim | Side | Why |
| -- | -- | -- |
| "MDE is −2.37% on a 42.14% baseline" | methodology | a property of the design, no decision attached |
| "…which is 1.0 pp, against the −0.5 pp margin the team approved, so a null on the guardrail cannot clear this launch" | **product** | product quantity → approved threshold → what the experiment cannot settle |
| "run an SRM check on the activation event before any readout" | methodology | measurement validity |
| "one canonical exposure event fired from the same code path in every arm" | methodology | measurement validity |
| "Retention 14d plus trial maturity means no read before exposure + 14 days" | methodology | measurement validity |
| "`from_tour` is new to every app event — validate end to end" | methodology | instrumentation hygiene |
| "the demo touches only the ~78% Chords branch, so Total ARPU/exposed is a diluted ITT" | **product** | dose is a product quantity and the claim is about what the readout means for the idea — it fails Q3 for want of a threshold, it is not out of scope |
| "the goal is non-inferiority versus B, but the design tests superiority versus control at +20% — a question #7622 already answered" | **product** | what running this settles about the idea |
| "temporarily unlocked paid features may raise cancels and refunds" | **product** | a consequence of the mechanic for the money |
| "the guardrail baseline in the card disagrees with the one in the results table" | methodology | baseline consistency |

**A weak product claim stays in scope and fails Q3.** It is not demoted to
methodology. Demoting weak claims would shrink the Q3 denominator and reward an
answer for arguing badly — the failure mode this rubric was written to remove.

### Third reading: operational feasibility is **not** a product argument

Ruled here because the V1.4 run surfaced it as the next ambiguity of the same
class, and leaving it open would reopen the hole this ticket closes.

Claims about whether the experiment can be *run* as planned — enrollment rate
versus required sample, duration, slot occupancy, implementation effort — are
**out of the product rubric**. They argue about the plan, not about the idea:
the same claim holds whether the idea is excellent or worthless.

- "reach implies ~10 days to fill 38,147/arm, but the design says 39 days" →
  out of scope (a planning inconsistency in the card).
- "a third arm pushes binding enrollment to ≈31 days" → out of scope.
- "this occupies the only iOS first-session slot for ~48 days, so the idea must
  clear a higher bar than its own expected effect before it is worth running" →
  **in scope**, and it is also the kind of claim Q8 asks for. The conversion to
  a decision about the idea is what brings it in, exactly as in hole 2.

This ruling is deliberately the conservative direction: it leaves the already
published V1.4 score at 3 of 5 rather than lifting it to 4. A ruling that moved
a published number upward would be fitting the ruler to the result.

---

## Scoring

- **Claim score** = share of product arguments passing Q2, Q3, Q4 **separately**.
  Report the three shares, never average them — they fail for different reasons
  and the fixes are different.
- **Q3 denominator** = product arguments in scope, minus those marked `n/a`.
  `n/a` is reserved for meta-claims about the *evidence base* rather than about
  the idea ("the evidence is mixed; the transfer boundary is captured-intent vs
  neutral-moment"). Claims ruled out of scope by §Boundary never enter the table
  at all. Q2 and Q4 keep the meta-claims in their denominator, so the three
  denominators can legitimately differ by the number of `n/a` rows — state all
  three.
- **Document score** = count of Q5–Q9 gates passed, out of 5 (out of 4 when Q6
  is not applicable).
- **Five-point product rating:**

| Rating | Condition |
| -- | -- |
| 5 | Q3 ≥ 2/3 of arguments, all document gates passed |
| 4 | Q3 ≥ 1/3, at most one document gate failed |
| 3 | Q3 > 0, at most two document gates failed |
| 2 | Q3 = 0, or three or more document gates failed |
| 1 | Q2 < 1/2 — the answer is not traceable at all |

Q3 dominates deliberately. An answer where no statement reaches "the metric will
move by this much, and here is where the number comes from" cannot stop a
launch, however well the rest is written.

## What the rubric does not measure

- Whether the underlying evidence is *correct* — that is the closeness model and
  the evidence policy. The one exception is §Q3(a): an arithmetic step the
  answer performs on card numbers must reproduce, because that is checkable from
  the card alone.
- Anything about experiment methodology, as delimited in §Boundary.
- Operational feasibility, as ruled in §Boundary.
- Length. Length is FLOW-609; a short answer can still score 2.

---

## Effect on published scores

Both fixes cut in the direction of the baseline, so every score published under
the old readings is restated here. Nothing below is a re-grade of a new run.

| Answer | Under V1.0 | Under V1.2 | What moved |
| -- | -- | -- | -- |
| V1.3 arm B, FLOW-624 run (`diagnosis_official_tabs.md`) | **2 of 5** (Q3 0/10, 1 of 5 gates) | **2 of 5** (Q3 1/14, 1 of 5 gates) | Q3 stops being zero — the appendix-B sizing claim qualifies — but four document gates still fail, so the rating is unchanged and now rests on the gates. Full recount: `diagnosis_official_tabs_v1.2.md` |
| V1.3 arm B, FLOW-631 rerun | **2 of 5** (Q3 0/11, 3 of 4 gates) | **3 of 5** (Q3 1/11, 3 of 4 gates) | the guardrail claim enters scope under §Boundary and its numbers are the card's |
| V1.3 arm A, both runs | Q3 counted the invented magnitudes | Q3 = 0 | "ARPU +8–18%", "retention −0.7…−1.5 pp" are traceable to nothing |
| V1.4 arm B, FLOW-632 run | — | **3 of 5**, unchanged | graded under the V1.1 patch; V1.2 changes no line of it. The strict Q3 denominator is 3/10 (A3 and A12 are excluded, not `n/a`), which is 0.30 — still short of the 1/3 needed for 4 |

**The comparable baseline for V1.4 is 3 of 5**, from the FLOW-631 rerun on the
same input. Comparing V1.4 against the 2 of 5 in `diagnosis_official_tabs.md` is
wrong twice over: different run, and a rating that under V1.2 holds at 2 for a
reason (failed gates) that V1.4 did not fix either.

## Changelog

| # | Change | Source | Moves a published number? |
| -- | -- | -- | -- |
| 1 | Q3 requires a traceable origin; three origins defined | FLOW-642 hole 1, V1.1 patch | yes — restated above |
| 2 | Product-argument / methodology boundary defined with examples both sides | FLOW-642 hole 2, V1.1 patch | yes — restated above |
| 3 | A stated operation that does not reproduce disqualifies the claim | V1.2 | yes — FLOW-624's "~2 pp / four times finer" now fails Q3 |
| 4 | A card number restated in another unit must name its field | V1.2 | same claim as #3 |
| 5 | A weak product claim stays in scope and fails Q3 rather than being demoted | V1.2 | no |
| 6 | Q3 denominator defined; `n/a` reserved for meta-claims | V1.2 | no — makes V1.4's 3/10 explicit |
| 7 | Operational feasibility ruled out of scope | V1.2, raised by the V1.4 run | no — deliberately leaves V1.4 at 3 |
