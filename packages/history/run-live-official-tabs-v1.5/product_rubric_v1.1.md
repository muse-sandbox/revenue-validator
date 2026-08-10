# Product-argument rubric V1.1 — patch closing the two holes found in FLOW-631

Base document: `product_rubric.md` (FLOW-628), unchanged except where this
file says otherwise. Everything not listed here — the nine questions, the two
units of evaluation, the three normalizations, the five-point scale, the
"what the rubric does not measure" section — carries over verbatim.

**Status.** This patch is written by the FLOW-632 executor because FLOW-632
cannot be interpreted without it: FLOW-631 established that the V1.3 run
scores 2 or 3 depending on readings the rubric leaves open, and a V1.4 run
measured against an ambiguous rubric measures nothing. The rubric is owned by
FLOW-628; treat V1.1 as a proposal that this run applies and states openly,
not as an approved change to that document.

## Hole 1 — Q3 counted any number, including an invented one

**What FLOW-631 found.** The arm WITHOUT a knowledge base emitted magnitudes
freely — "ARPU +8–18% vs control", "retention −0.7 to −1.5 pp" — and labelled
them itself as ungrounded transfer hypotheses. By the letter of Q3 those
count. The arm WITH the base emitted none, because rule 4 forbids
transferring magnitudes from other experiments, and scored Q3 = 0. On this
case the rubric therefore rewarded the fabricator over the disciplined
answer, which is the opposite of what it exists to do.

**V1.1 rule.** Q3 counts a claim only when the magnitude or threshold it
states is **traceable**. A magnitude is traceable when every number in the
claim has one of these three origins, and the claim says which:

1. **Computed from the card under review** — the number appears in the
   experiment card, or is the result of an operation written out in the same
   claim over numbers that do. This is the `[computed]` label of KB §2.8 and
   it is machine-checkable: run the V1.4 linter with `--card`.
2. **Borrowed and marked as borrowed** — the number comes from a cited
   source, carries its ID, and is labelled as a sizing prior rather than a
   prediction, as rule 4 requires. A borrowed number counts for Q3 only when
   the claim also says what it is being compared against; a bare prior with
   no decision threshold is not a decision-grade statement.
3. **Stated by the team in the card** — the card's own expected effect,
   guardrail margin or MDE, quoted as such.

A number whose origin is none of these does not count for Q3, however
confidently it is phrased, and it should be recorded as a defect in the same
line of the score table. The direction of the fix is deliberate: Q3 stops
being a reward for producing digits and becomes a reward for producing digits
that can be checked.

**Consequence for grading.** Where an answer marks a claim `[computed]`, run
the linter before scoring it. `E_COMPUTED_NUMBER_FABRICATED` and
`E_COMPUTED_NUMBER_FROM_KB` each disqualify the claim from Q3.

## Hole 2 — "this design cannot resolve X" was neither in nor out of scope

**What FLOW-631 found.** The V1.3 answer stated "MDE −2.37 pp against an
approved margin of −0.5 pp and a B loss of −1.60 pp — a null here is
uninformative". Counted as a product argument, Q3 > 0 and the answer scores
3; counted as methodology, Q3 = 0 and it scores 2. The rubric does not say
which, so the score moved by a whole point on the grader's taste.

**V1.1 rule.** A claim about what the design can or cannot resolve **is a
product argument** when both of these hold:

- it connects a *product* quantity — the expected effect of the mechanic, the
  share of the arm that is actually exposed, the dose the treated users
  receive — to a decision threshold; **and**
- it ends in a consequence for the decision about the IDEA: what this
  experiment will not be able to tell us, and therefore what running it as
  designed would and would not settle.

A claim is **methodology** — and stays out of the rubric, as before — when it
is about the correctness of the measurement rather than about what the
measurement can decide: SRM, activation, exposure gates, maturity horizons,
multiplicity, baseline consistency, denominator choice.

The boundary is the consequence, not the vocabulary. "MDE is −2.37 pp" alone
is methodology. "MDE is −2.37 pp against the −0.5 pp margin the team approved,
so a null on the guardrail cannot clear this launch" is a product argument:
it says the experiment cannot settle the question it was built to settle.

## Consequence: the FLOW-624 / FLOW-631 baseline moves

Both holes cut in the direction of the baseline, so the baseline must be
recomputed before any comparison is drawn. Under rubric V1.1 the FLOW-631
answer (arm B, bundle V1.3, same input) scores:

| | Rubric V1.0 | Rubric V1.1 |
|---|---|---|
| Q3 | 0/11 | 1/11 — the guardrail claim qualifies under hole 2, and its numbers are the card's own |
| Document gates | 3 of 4 (Q7 failed) | 3 of 4, unchanged |
| **Rating** | **2 of 5** | **3 of 5** |

The V1.3 arm-A answer loses its magnitudes under hole 1: "ARPU +8–18%" and
"retention −0.7…−1.5 pp" are traceable to nothing, so arm A's Q3 goes to 0
under V1.1.

**This is the honest comparison for FLOW-632.** The V1.4 run must be read
against **3 of 5**, not against 2 of 5. Measured against the old baseline any
V1.4 number would be flattered by the rubric fix; measured against the new
one, only what the bundle change itself produced is visible. The task
description predicted "one `[computed]` claim makes Q3 non-zero and the score
becomes 3" — under rubric V1.1 the V1.3 answer already reaches 3 without any
bundle change, so reaching 3 is no longer evidence that V1.4 did anything.
What V1.4 has to show is a *higher count* of traceable magnitudes, not a
non-zero one.
