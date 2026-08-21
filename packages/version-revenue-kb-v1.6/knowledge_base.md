# Revenue Knowledge Base V1.6 — Corpus & Closeness Model (FLOW-641, frozen 2026-08-08)

This file plus `pattern_cards.md` form the KNOWLEDGE CONTEXT for arm B of the
evaluation protocol. Contents:

1. How to use this base (retrieval contract)
2. Closeness model (L1/L2/L3): deterministic level computation, the strict
   machine-parsable analog-card format, the scope rules for corpus-level
   generalizations (§2.5–§2.6), the grounding rules for product
   proposals (§2.7), the provenance rules for computed claims (§2.8), and the
   consequence/mechanism/price form of the findings themselves (§2.9)
3. Indices: by flow stage, segment, mechanism, decision type
4. 18 evidence source cards (T1-01…T3-06)

Scope: completed UG revenue experiments, verified against Confluence source
pages on 2026-08-04 (inventory FLOW-577 V0.1, holdout-excluded input). Money
figures are net revenue unless stated otherwise. The anchor family of the
typology is the UG App monetization interstitial layer (S3–S4).

V1.1 changed only §1 cross-references and §2 (the closeness model became a
deterministic, linter-checked specification per Evidence Policy V1); the
corpus (§4) and the indices (§3) were unchanged from V1.

V1.2 adds §2.5 (scope and qualifiers for corpus-level generalizations; the
ban on unqualified universals; the `evidence is mixed` requirement) and §2.6
(machine-readable generalization classes consumed by the linter), plus the
matching §1.9 contract item. The corpus (§4) and the indices (§3) are again
unchanged; `pattern_cards.md` V1.2 changes only heading/claim SCOPE wording,
no facts. Nothing in §2.1–§2.4 (axes, level computation, card format) was
touched, so every V1.1 hard error keeps its exact V1.1 behaviour.

V1.3 adds §2.7 (product proposals: what makes a proposal grounded, the typed
bullet form, and the honest-abstention literal `no grounded product
proposal`) plus the matching §1.10 contract item. It exists because the
knowledge in this base is largely product knowledge — which segment, offer or
mechanic earns money — and the V1.2 answer format had nowhere to put it: a
product finding could only surface as a WARNING inside the risks section, so
the reader got "what may break" and never "what to do instead". §2.7 opens a
separate channel for the same evidence and, at the same time, forbids
ungrounded invention: a proposal without a qualifying source is not allowed
to exist as a proposal. The corpus (§4), the indices (§3), `pattern_cards.md`
and §2.1–§2.6 are unchanged, so every V1.1/V1.2 hard error keeps its exact
prior behaviour; the only new failure mode an old answer can acquire under
the V1.3 linter is the missing `## Product proposals` section.

V1.4 adds §2.8 (computed claims: the fourth statement label `[computed]`, the
provenance rule for every number inside one, and the honest-abstention
literal `no computable limit`) plus the matching §1.11 contract item. It
exists because §2.7 and rule 4 govern what may be carried IN from other
experiments, and nothing governed what can be derived from the numbers the
card under review states about itself. Two runs of the same live case
(FLOW-624, FLOW-631) produced no statement that reached "the metric will move
by this much", although the card's own numbers implied one; the arithmetic
was attempted ad hoc, in the appendix, and never finished. §2.8 requires that
arithmetic, gives it a fixed slot in the answer, and makes its provenance
machine-checkable. It does NOT relax rule 4: the moment a knowledge-base
number enters the calculation, the statement is a transfer under §1.8/rule 4
and not a computation. The corpus (§4), the indices (§3), `pattern_cards.md`
and §2.1–§2.7 are unchanged, so every V1.1/V1.2/V1.3 hard error keeps its
exact prior behaviour; the only new failure mode an old answer can acquire
under the V1.4 linter is the missing `## What this experiment cannot show`
section.

---

V1.5 adds §2.9 (findings: the consequence/mechanism/price form, the ranking
by price, the split into blocking and improving, and the ban on headlines
that describe the document instead of the decision) plus the matching §1.12
contract item. It exists because two runs of the same live case produced
objections that were correct and unusable: they named properties of the paper
("the guardrail is unfalsifiable", "the effect is diluted", "there is no B
arm") rather than what the reader gets if nothing changes. A product owner
hears the first form as pedantry, so a correct objection changed no decision.
§2.9 requires each finding to carry what it costs and in which unit, orders
the list by that cost, and caps the blocking findings at three. It also folds
the V1.4 section `## What this experiment cannot show` into the mechanism
slot of the findings and replaces `## Top risks & failure modes` and
`## Blocking design fixes`, because those three sections were three places to
say the same objection. The corpus (§4), the indices (§3), `pattern_cards.md`
and §2.1–§2.8 are unchanged, so every V1.1/V1.2/V1.3 hard error and every
§2.8 provenance check keeps its exact prior behaviour; what changes for an
old answer is which sections the format requires.

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
9. Never promote the evidence you actually have to a claim about a whole
   class of interventions. A pattern-card heading names the sub-class its
   facts cover (`pattern_cards.md`, global rule "Title = evidence scope"); a
   source card covers one experiment. Any sentence that generalizes across
   the corpus must carry the explicit scope annotation of §2.5, and when the
   cases you cite point in conflicting directions inside the class you are
   talking about, you must write `evidence is mixed` instead of a one-sided
   universal. §2.6 lists, machine-readably, which sources point which way for
   the recurring generalization classes of this corpus.
10. This base is mostly PRODUCT knowledge — which segment, which offer and
    which mechanic earned money, and where the boundary of that finding lies.
    Deliver it as a proposal, not only as a warning: the same source that
    tells you a step before the paywall sheds users also tells you what was
    tried instead and how it went. §2.7 defines what makes a product proposal
    grounded, the form it must take, and the literal to write when the corpus
    genuinely has nothing to propose. A proposal that no source supports is
    not a cautious proposal — it is an invented mechanic, and §2.7 forbids it.
11. The card under review states numbers about itself — reach, coverage,
    expected effect, guardrail margin, detectable difference. Those numbers
    are yours to use, and combining them is the one way an answer can reach a
    statement of the form "this design cannot show the thing it was built to
    show". §2.8 requires that computation, defines the `[computed]` label it
    must carry, and fixes where it goes. It changes nothing about §1.8: a
    number that came from this base is a transfer, however it is phrased.

12. An objection only counts if the reader can see what it costs. State
    every finding as what happens if nothing changes, tie it to a number of
    the document or a cited source, and name the price in one of the five
    units of §2.9 — slot, days, share of the expected effect, money, or
    "decision impossible". Rank them by that price and mark at most three as
    blocking. A finding you cannot price is a checklist item; §2.9 sends it
    to the appendix rather than deleting it.

### 1.13 Three things the reader must be able to see in one pass

The FLOW-628 rubric asks nine questions of an answer. Three of them are not
about evidence at all — they are about the sentence the evidence ends up in,
and they are the ones this base closes in §2.10-§2.12.

| Rubric question | Section | The test |
|---|---|---|
| Q4 · reads as "if X, grounded in Y, then Z" | §2.10 | can the reader see what the conclusion stands on without leaving the sentence? |
| Q7 · no idea restated in different words | §2.11 | does each mechanism-on-a-segment appear exactly once? |
| Q9 · no cheap generic UI changes | §2.12 | could this line have been written without reading the document? |

The three are deliberately checked on the FORM of the statement rather than on
its content. A reader who has to assemble a chain from three paragraphs loses
the fact that the chain rests on an assumption; a reader who meets the same
thought twice concludes the answer is padding; and a reader who meets advice
that fits any product stops trusting the advice that does not.

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

### 2.5 Corpus-level generalizations: scope, qualifiers, and the ban on unqualified universals (normative; linter-enforced)

A **corpus-level generalization** is a sentence that claims what this corpus
as a whole does or does not show for a CLASS of interventions ("wrapper
changes have never lifted purchases in this corpus", "every price change in
the knowledge base moved structure only"). Such a sentence is not an analog
card, so §2.2–§2.4 do not constrain it — and that is exactly where the
observed failure mode lives: the asserted class is wider than the cases
behind it, and it can contradict a positive case the same answer cites and
quarantines elsewhere. The three rules below close that hole structurally.

**G1 — A corpus-level generalization MUST carry an explicit machine-readable
scope annotation.** The annotation states what sub-class the claim covers,
which source IDs it rests on, and what it does NOT cover. Exact syntax (one
line or wrapped; it must sit inside the same sentence, normally just before
the final period):

```
[scope: <sub-class>; ids: <ID>[, <ID>…]; not covered: <what the claim does NOT cover>]
```

- `<sub-class>` — free text, non-empty, no `;` inside.
- `ids:` — one or more source IDs (`T*-**` / `P-**`), comma-separated; each
  MUST exist in the KNOWLEDGE CONTEXT (a nonexistent ID is a hard error, as
  everywhere else).
- `not covered:` — free text, non-empty; name the neighbouring sub-classes
  the claim does NOT reach. Listing a source ID here declares that case
  explicitly out of scope (this is what suppresses the contradiction check of
  G3 for that ID).

Example of a compliant sentence:

> [interpretation] Message-only personalization with the offer held constant
> did not lift purchases in this corpus
> [scope: personalization of the message/creative with the offer unchanged;
> ids: T1-09, P-10; not covered: offer personalization (T2-06),
> non-personalized creative/format/gamification changes, retention or
> engagement goals].

**G2 — Unqualified universals are forbidden.** A sentence of the form
"X never / always / has not / have not / does not / no … in this corpus" is
invalid whenever the cited evidence does not cover the whole asserted class.
Practically: either narrow the sentence to the evidenced sub-class and
annotate it per G1, or do not write it. The machine detector (below) flags
any corpus-scoped universal that carries no annotation — including one whose
underlying claim happens to be true.

**G3 — Mixed evidence must be declared with the literal phrase.** If, inside
the class you are generalizing over, the sources you cite point in
conflicting directions (see the machine-readable direction table in §2.6),
you MUST write the exact literal phrase `evidence is mixed` in the same
paragraph and enumerate the transfer boundaries (which sub-class goes which
way, and where the boundary is), instead of asserting a one-sided universal.
Declaring the opposite-direction case out of scope in the `not covered:` part
of the annotation is the other legal option — that is a narrower claim, not a
suppressed one.

**Machine detector (exact, deterministic — this is what the linter runs).**
A prose sentence is a *corpus-scoped universal* when, after the exemptions
below, it contains at least one CORPUS-SCOPE MARKER **and** at least one
UNIVERSAL MARKER.

- CORPUS-SCOPE MARKERS (case-insensitive substrings): `this corpus`,
  `the corpus`, `our corpus`, `corpus-wide`, `this knowledge base`,
  `the knowledge base`, `this evidence base`, `the evidence base`,
  `the knowledge context`, `the reviewed cases`, `the cases reviewed`,
  `the cited cases`, `the source cases`, `past experiments`,
  `prior experiments`, `historical cases`.
- UNIVERSAL MARKERS, absence/negative subset (case-insensitive, whole words):
  `never`, `none`, `nothing`, `nowhere`, `not a single`, `at no point`,
  `no case`, `no experiment`, `no source`, `no iteration`, `no evidence`,
  `has not`, `have not`, `had not`, `hasn't`, `haven't`, `does not`,
  `do not`, `did not`, `doesn't`, `don't`, `is not`, `are not`, `was not`,
  `were not`, `cannot`, `can't`, `failed to`, `fails to`.
- UNIVERSAL MARKERS, absolute/positive subset: `always`, `every`, `all`,
  `any`, `universally`, `invariably`, `without exception`, `in all cases`,
  `only ever`.
- Polarity: a flagged sentence is NEGATIVE if it contains any marker of the
  absence subset, otherwise POSITIVE. G3 then compares against the opposite
  direction in §2.6 (NEGATIVE sentence ↔ `outcome_positive` sources, POSITIVE
  sentence ↔ `outcome_negative` sources).
- Exemptions (nothing else is exempt): (a) text inside analog cards and any
  other fenced block is not prose and is never scanned; (b) the mandatory
  literal `no direct analogs` and any retrieval statement matching
  `no <word>? analog(s)` are removed before scanning — saying that the corpus
  holds no direct analog for your case is a retrieval statement, not a
  product generalization; (c) the text inside a `[scope: …]` annotation is
  not scanned for markers (it is validated as an annotation instead).

**The escape hatch is asymmetric on purpose.** An answer that simply does not
generalize across the corpus triggers nothing and needs no new syntax: every
V1.1-compliant answer that talks about individual sources, about the new
case, or about a named sub-class without a corpus-scope marker stays valid
unchanged. The annotation is required only from an answer that chooses to
make a corpus-wide claim.

### 2.6 Machine-readable generalization classes (linter input; not evidence)

The blocks below are the direction table the G3 contradiction check consumes.
Each class is a recurring generalization FAMILY of this corpus — the kind of
class an over-broad sentence asserts. `outcome_positive` / `outcome_negative`
record, for that family only, which way each source's recorded outcome
points; this is a KB-declared property, not something inferred from the
answer's prose at lint time, and it is not itself evidence (always cite the
source cards in §4 and the pattern cards, never this table). `keywords` are
the case-insensitive substrings that attach a flagged sentence to the class.

```
generalization_class: GC-01
  label: personalization — tailoring the message, creative, offer or price to a user attribute or state (direction = did the personalization lift money)
  keywords: personaliz, personalis, wrapper, message around the offer, tailored to the user
  outcome_positive: T2-06
  outcome_negative: T1-09, T3-01
```

```
generalization_class: GC-02
  label: price change — moving the price level up or down on any surface (direction = did the price change move net revenue)
  keywords: price, pricing, discount, elasticity
  outcome_positive: T1-08, T3-02, T3-06
  outcome_negative: T3-01
```

```
generalization_class: GC-03
  label: offer structure — changing what is offered (plan menu composition, trial vs instant, intro offers, bundle upsells) (direction = did the structural change earn money)
  keywords: offer structure, plan menu, new plan, instant offer, instant purchase, trial to instant, intro offer, bundle, upsell
  outcome_positive: T1-08, T2-05, T2-06, T3-05, T3-06
  outcome_negative: T3-03
```

```
generalization_class: GC-04
  label: monetization surface added, replaced or removed (direction = did the surface carry net incremental money; removal tests count positive when turning the surface OFF harmed revenue)
  keywords: new surface, surface, interstitial, splash, banner, offer layer
  outcome_positive: T1-04, T2-01
  outcome_negative: T1-01, T1-02, T1-03
```

```
generalization_class: GC-05
  label: creative, design or gamification change on an existing surface, personalization aside (direction = did the creative/design change move the funnel)
  keywords: creative, design, gamif, animation, emotional, wrapper
  outcome_positive: T1-04, T1-07
  outcome_negative: T1-09, T2-02
```

```
generalization_class: GC-06
  label: funnel length — inserting or removing a step between the trigger and the offer (direction = did the extra step help)
  keywords: extra step, additional step, pre-paywall, demo, preview, compare table, funnel length, longer funnel
  outcome_positive: T1-07
  outcome_negative: T1-03, T2-07
```

Reading rule: a class listing IDs on both sides means the corpus itself is
mixed for that family. A one-sided universal over such a family is therefore
almost always wrong — say `evidence is mixed` (G3) or narrow the claim to the
sub-class you can actually support (G1).

### 2.7 Product proposals: grounding, form, and the ban on invented mechanics (normative; linter-enforced)

A **product proposal** is a suggestion about the IDEA — which *mechanic*,
which *segment* or which *offer* would plausibly earn more than the one
proposed — as distinct from a change to how the experiment is designed or
measured. The three channels of an answer are disjoint by construction and
each carries the same evidence differently:

| Channel | Question it answers | Section |
|---|---|---|
| finding | what we get instead of an answer, and what it costs | `Findings` (§2.9) |
| non-monetization effect | what else changes besides money, both directions | `Non-monetization effects to instrument` |
| product proposal | what to do differently with the idea itself | `Product proposals` |

One source can feed all three. `T2-07` warning "a demo before the paywall
cost access CR" is a risk; the same card's observation that the losers were
beginners and that AOV rose through mix shift is a proposal input (who to
target, what outcome shape to pre-register). Writing only the risk is the
failure mode this section exists to prevent: the knowledge is in the base,
and it stops at the reader as a caution instead of an option.

**PP1 — The section is mandatory.** Every answer contains the heading
`## Product proposals` (an ordinal prefix such as `## 3. Product proposals`
is allowed). Without a KNOWLEDGE CONTEXT there is no evidence base to ground
anything on: the section must then contain the exact literal
`no grounded product proposal` and one sentence saying why.

**PP2 — One typed bullet per proposal, at most three.** Every bullet in the
section opens with exactly one type literal, written verbatim:

- `[mechanic]` — do the intervention differently (a different step, a
  different placement, forced vs skippable, a different moment).
- `[segment]` — run it on a different audience, or split the readout by one.
- `[offer]` — change what is offered (plan, trial vs instant, price
  structure, bundle) rather than how it is presented.
- `[ungrounded]` — the honest-abstention form (PP4).

**PP3 — Grounding (hard).** A `[mechanic]` / `[segment]` / `[offer]` bullet
MUST cite at least one **grounding source ID** in the same bullet, and every
source ID it cites must qualify as one. A grounding source ID is:

- a pattern ID `P-**` that exists in the KNOWLEDGE CONTEXT and whose
  applicability scope covers the case under review; **or**
- a case ID `T*-**` that exists in the KNOWLEDGE CONTEXT **and** is the
  `source` of an analog card emitted in this same answer whose COMPUTED level
  (§2.2) is `L1` or `L2`.

An `L3` case grounds nothing product-level (§2.2, §1.8): it is a sizing,
measurement and guardrail signal, so it may not appear in a proposal bullet.
A case with `result_class: inconclusive` grounds measurement lessons only
(§1.7) and likewise may not be a proposal's only support. Magnitudes never
transfer (§1.8): a proposal states the expected DIRECTION on a named metric
and, if a number is useful at all, an order of magnitude labelled `prior`.

**PP4 — Honest abstention (hard).** When the corpus has nothing that
qualifies, the correct answer is to say so, not to invent a plausible
mechanic. Then either the section carries only `[ungrounded]` bullets, or it
carries none — and in both cases it MUST contain the exact literal
`no grounded product proposal`. An `[ungrounded]` bullet names the question
that would have to be researched and carries NO source ID; citing an ID
inside one is a hard error, because that is exactly how an unsupported
mechanic acquires the look of evidence.

**PP5 — Do not restate a finding as a proposal.** The finding names what we
get instead of an answer and what it costs; the proposal names the
alternative. Where one source feeds both, the two bullets must say different
things. A grounding source cited in the findings section (§2.9) and nowhere in
the proposals is not an error, but it is usually a missed proposal — the
linter reports it as a warning, not a failure.

**PP6 — Proposals do not overturn the verdict on their own.** The verdict
comes from the design and the evidence as before. A proposal is what the
reader should consider doing with the idea; a `[mechanic]` proposal is never
a substitute for the design fixes, which live in their own section.

Compliant examples (form only; the IDs are illustrative):

> - **[segment]** Read the demo out on beginners separately and consider
>   restricting it to them — grounded in T2-07 (L2 card below): [fact]
>   beginners took the largest access-CR loss there; [hypothesis] here the
>   same split decides whether the mechanic is bad or only badly targeted.
>   Expected direction: access CR on the non-beginner arm at or above control.
> - **[ungrounded]** Whether an in-tab demo AFTER the paywall would keep the
>   monetization and drop the retention cost is not covered by any source
>   here; it needs its own test rather than a recommendation.

### 2.8 Computed claims: the `[computed]` label and the provenance of numbers (normative; linter-enforced)

A **computed claim** is a statement obtained by arithmetic over numbers that
the card under review states about ITSELF — its reach, its coverage, its
expected effect, its guardrail margin, its detectable difference. It is the
fourth statement label alongside `[fact]`, `[interpretation]` and
`[hypothesis]` of rule 8, and it is the only channel in this format through
which an answer can say how much a metric moves. Everything carried in from
this base is governed by §1.8 and rule 4 and stays a direction; everything
derived from the card's own numbers is governed by this section.

The distinction is not a matter of phrasing. It is a matter of where the
digits physically came from, which is why it can be checked by machine.

| Label | What it is | Where the numbers come from |
|---|---|---|
| `[fact]` | a measurement in a source | the KNOWLEDGE CONTEXT, cited by ID |
| `[interpretation]` | the source team's reading | the KNOWLEDGE CONTEXT, cited by ID |
| `[hypothesis]` | a transfer to the case under review | a source's sign/mechanism, no magnitude |
| `[computed]` | arithmetic over the card's own numbers | the card under review, no ID at all |

**CC1 — What `[computed]` may contain (hard).** Every number inside a
`[computed]` statement must be either

- present in the text of the experiment card under review; **or**
- the result of an operation shown inside the same statement over numbers
  that are themselves admissible under this rule.

A number that satisfies neither is one of exactly two failures, and the two
are different diagnoses with different fixes:

| Where the number is | Code | What happened |
|---|---|---|
| nowhere in the card, nowhere derivable | `E_COMPUTED_NUMBER_FABRICATED` | invented magnitude |
| nowhere in the card, but present in this base | `E_COMPUTED_NUMBER_FROM_KB` | a transfer wearing the costume of a calculation |

A number matches a card number when the two values are equal, or when the
card's value rounded to the precision actually written in the answer equals
the written value — `~27%` is an admissible way to write a card's `26.8%`,
`27.4%` is not. A share and a percentage are the same number written two
ways: computing with `0.78` where the card says `78%` is arithmetic, not
invention. Neither is the sign: prose drops the minus of a margin routinely,
and provenance is about the digits. The structural constants `0`, `1` and
`100` are arithmetic scaffolding rather than data — they form complements
and percentages — and need no provenance.

**CC2 — Show the operation (hard).** The arithmetic is written out in the
sentence so the reader can redo it in their head. Not "roughly 57% of the
arm", but `78% × (1 − 27%) ≈ 57%`. A `[computed]` statement in which no
operation is shown is not a computation; it is an assertion with a number
attached, and the linter rejects it (`E_COMPUTED_NO_OPERATION`).

**CC3 — No source ID (hard).** A `[computed]` statement carries no case ID
and no pattern ID (`E_COMPUTED_SOURCE_ID`). The moment a number from this
base enters the calculation, the statement is a magnitude transfer under
§1.8 and rule 4 with all of their restrictions — it must then be relabelled,
carry its ID, and live in `not_transferable` or `sizing_prior` like any
other borrowed magnitude. A borrowed number is allowed to exist; it is not
allowed to be presented as measured, and it is not allowed to be laundered
into a computation.

**CC4 — Say what it costs the decision (normative).** The result is stated
as a consequence for the launch decision — what this experiment will not be
able to show — not as a forecast of the product's success. `[computed]` is
not a licence to predict revenue: the card's numbers describe the design,
so what they legitimately yield is the design's own limit.

> Wrong: `[computed]` the demo will lift ARPU by 11%.
> Right: `[computed]` 78% × (1 − 27%) ≈ 57% of the test arm can actually
> reach the demo, so a true +20% on the exposed users arrives in the overall
> metric as roughly +11%, below the ~2 pp this design can resolve — a null
> result would not mean the mechanic failed.

**CC5 — The MAIN slot is mandatory (amended by §2.9 in V1.5).** Every answer
carries at least one `[computed]` statement in the MAIN part. V1.4 gave that
statement a section of its own, `## What this experiment cannot show`; V1.5
removes that section and puts the same arithmetic in the `Mechanism:` slot of
the findings of §2.9, because a separate section made the answer say the same
objection twice — once as a computation and once as a risk. The requirement
itself is unchanged and so is its motivation: in the two runs that produced
this rule, the calculation was attempted inside the methodology appendix,
where nobody reads it as an argument about the idea.

**CC6 — Honest abstention (hard).** When the card genuinely does not state
enough numbers to compute a limit, the findings section must contain the
exact literal `no computable limit` and one sentence naming the number that
is missing. Inventing a plausible figure to fill the slot is the failure this
section exists to prevent, and CC1 catches it.

**CC7 — The label is not restricted to the slot.** A `[computed]` statement
may appear anywhere in the answer; CC1–CC4 apply to all of them wherever
they are. Both arms are subject to this section in full: it needs no
KNOWLEDGE CONTEXT, because the card carries the numbers. Without a
KNOWLEDGE CONTEXT `E_COMPUTED_NUMBER_FROM_KB` cannot arise — a number absent
from the card is simply fabricated.

### 2.9 Findings: consequence, mechanism, price (normative; linter-enforced)

A **finding** is a statement in the answer that argues the experiment should
not be launched as designed. §2.7 governs what to do differently with the
IDEA and §2.8 governs the arithmetic; this section governs the objections
themselves — how they are written, what each one must carry, and in which
order they appear.

The failure this section exists to prevent is not weak reasoning. It is a
finding that describes a **property of the document** instead of a
**consequence for the decision**. The reader of this answer allocates
experiment slots; a sentence about the paper reads to them as pedantry, and a
correct objection phrased that way changes nothing.

| A finding that describes the paper | The same finding as a consequence |
|---|---|
| the guardrail is unfalsifiable | we spend the slot and get a result no one can decide on |
| the effect is diluted | the +20% you expect arrives in the metric as +11%, below your MDE |
| there is no B arm | the main goal has nothing to test against: the comparison runs on numbers from another quarter |

The test applied to every line of the MAIN part: **is it clear from the
sentence what happens if nothing changes?** A sentence that does not answer
that is not a finding for the MAIN part — it is a checklist item, and it
belongs in the appendix.

**FD1 — The section is mandatory and it is the only home of the findings.**
Every answer carries the heading `## Findings` in the MAIN part (an ordinal
prefix such as `## 2. Findings` is allowed) and at least one finding bullet.
The section replaces the V1.1–V1.4 sections `## Top risks & failure modes`
and `## Blocking design fixes`: the same material, ranked and priced, said
once. A finding that cannot be priced is not deleted — it moves to the
appendix section `## D. Findings without a price`, where it is a checklist
item rather than an argument.

**FD2 — Severity literal, then a headline.** Every bullet opens with exactly
one severity literal, written verbatim:

- `[stop]` — if this is not fixed, the experiment should not start.
- `[improve]` — worth fixing, but the experiment can answer its question
  without it.

At most **three** `[stop]` findings. A list where everything stops is not a
ranking, and the reader treats it as noise. Immediately after the literal
comes the **headline**: one sentence naming what the reader gets instead of
an answer. The headline runs from the literal to the first sentence
terminator or the first slot marker, whichever comes first; markdown emphasis
around it is ignored.

**FD3 — What a headline may not start with (hard).** A headline may not open
with a word that describes the absence of something in the document. The
closed lexicon the linter applies to the first word of the headline is:

`no`, `not`, `none`, `nothing`, `never`, `missing`, `absent`, `lack`,
`lacks`, `lacking`, `unspecified`, `undefined`, `unstated`, `uncalculated`,
`unaddressed`, `unclear`, `undocumented`, `insufficient`, `without`,
`there`.

`there` is on the list because every headline that starts with it in practice
continues `is no` / `are no`. The rule is about the opening word only: a
headline may say what will not happen (`we cannot …`, `the read will not …`)
as long as it does not open by naming a hole in the paper.

**FD4 — The headline states a result (hard).** The headline contains at least
one verb from the closed result lexicon:

`get`, `gets`, `become`, `becomes`, `turn`, `turns`, `end`, `ends`, `lose`,
`loses`, `spend`, `spends`, `cost`, `costs`, `cannot`, `can't`, `won't`,
`will not`, `fail`, `fails`, `arrive`, `arrives`, `read`, `reads`, `leave`,
`leaves`, `return`, `returns`, `yield`, `yields`, `shrink`, `shrinks`,
`drop`, `drops`, `land`, `lands`, `buy`, `buys`, `pay`, `pays`, `produce`,
`produces`, `take`, `takes`, `walk`, `walks`, `stay`, `stays`, `run`, `runs`.

These are the verbs of an outcome, not of a document review. `is`, `are`,
`has`, `have`, `remains` and `appears` are deliberately absent: they carry
descriptions, and a description is what this section forbids.

**FD5 — Three slots, all mandatory except the fix (hard).** After the
headline the bullet carries, in this order, three labelled slots. The label
is the word followed by a colon; surrounding markdown emphasis is ignored, so
`*Mechanism:*`, `**Mechanism:**` and `Mechanism:` are the same marker.

| Slot | What goes in it |
|---|---|
| `Mechanism:` | why, tied to a number of the document under review or to a cited source |
| `Consequence:` | what the reader gets instead of an answer |
| `Price:` | in what unit the loss is measured (FD6) |
| `Fix:` | optional — the one change that removes this finding |

The mechanism must be **grounded**: it carries either a `[computed]`
statement (§2.8, arithmetic over the card's own numbers), or a source ID that
exists in the KNOWLEDGE CONTEXT, or at minimum a number that the card itself
states. A mechanism with none of the three is an opinion with a label on it.
The single exception is the honest-abstention bullet: a finding that carries
the literal `no computable limit` is saying that the card states no numbers,
so there is nothing to ground on — and §2.8 CC6 still makes it name the number
that is missing.

At least one finding in the section must carry a `[computed]` mechanism. This
is where the §2.8 arithmetic now lives: V1.4 gave it a section of its own and
the result was the same argument said twice — once as a computation and once
as a risk. If the card genuinely does not state enough numbers to compute
anything, the section must contain the exact literal `no computable limit`
and name the number that is missing (§2.8 CC6, unchanged).

**FD6 — The price is one of five units (hard).** The `Price:` slot opens with
exactly one of these literals, and the explanation follows it:

| Price unit | What it means | Rank |
|---|---|---|
| `decision impossible` | the result is unusable in principle; the question stays open whatever the numbers say | 5 |
| `experiment slot` | the slot is spent and has to be spent again | 4 |
| `share of the expected effect` | part of the effect the team expects will not reach the measurement | 3 |
| `money` | a money loss computed from the numbers of this document | 2 |
| `days to decision` | only the calendar suffers; the answer still arrives | 1 |

`decision impossible` is the strongest unit and is meant to be rare: it says
the experiment cannot settle its own question. An answer in which most
findings claim it has stopped ranking anything.

**FD7 — Ranked by price (hard).** The bullets appear in non-increasing order
of (severity, price rank): all `[stop]` findings first, and inside each
severity group the price ranks descend. A flat list of seven items in which
the blocking objection sits fifth is the defect this rule removes.

**FD8 — Machine fields stay in the appendix (hard).** Domain vocabulary is
allowed in the MAIN part — MDE, guardrail, retention, ARPU read normally to
this reader. The model's own bookkeeping does not: the axis names and card
fields of §2.4 (`flow_stage`, `trigger_eligibility`, `money_chain`,
`money_chain_link`, `segment_monetization_state`, `transferable`,
`not_transferable`, `sizing_prior`) and the fenced `analog:` blocks belong to
appendix A, where the linter reads them. In the MAIN part the same analog is
one sentence of plain language. The literals the rules require (`[stop]`,
`[computed]`, `no direct analogs`, `evidence is mixed`, `[scope: …]`, the
proposal types) are not bookkeeping and stay. This rule is about a split,
so the split has to be visible: an answer that carries no `# MAIN` banner
cannot be checked against it, and the missing banner is itself the error.

**FD9 — Say who decides what.** The MAIN part carries the heading
`## What you decide`, holding at most four bullets, each opening with exactly
one role literal: `[product owner]` or `[analyst]`, and both roles must
appear. A product owner's decision is about the idea, the slot and the
appetite for the price; an analyst's decision is about design and
measurement. An answer that leaves this implicit produces a document that
everyone reads and no one acts on.

**FD10 — Say it once.** The findings section, the proposals section and the
non-monetization section answer three different questions (§2.7's channel
table, unchanged) and now also differ in what they cost: a finding carries a
price, a proposal carries a direction, a non-monetization effect carries an
instrument. The same sentence in two of them is a duplicate, and the linter
reports the overlap as a warning.

Compliant example (form only; the numbers are illustrative):

> - **[stop]** We spend the slot and come back with a retention number that
>   cannot clear this launch. *Mechanism:* [computed] the guardrail resolves
>   `40% × 2.4% ≈ 1.0 pp` while the margin the team approved is `0.5 pp`, so
>   `1.0 / 0.5 = 2×` the margin. *Consequence:* a non-significant guardrail is
>   compatible with twice the loss the team said it would accept, so the
>   retention condition cannot be declared met on any outcome.
>   *Price:* decision impossible — the question the experiment was built to
>   settle stays open. *Fix:* re-size on the approved margin before launch.

### 2.10 Conditional form: if X, grounded in Y, then Z (normative; linter-enforced)

§2.9 governs what a finding must carry. This section governs the **grammar** of
every statement the answer makes about the case under review, in whichever
channel it sits.

The defect it removes: the premise sits in one sentence, the conclusion in
another, and the link between them in the paragraph after that. Every part is
present and the reader still has to assemble the chain — and what gets lost in
the assembly is the one thing that decides how much weight the conclusion
carries: **whether it stands on a measurement or on an assumption**.

| Assembled by the reader | In conditional form |
|---|---|
| The demo touches only the Chords branch. Total ARPU is measured over the whole arm. The read will therefore be diluted. | *If:* the goal metric stays Total ARPU per exposed user. *Mechanism:* `[computed]` only `78% × (1 − 27%) ≈ 57%` of the arm can see the demo. *Consequence:* a true +20% arrives in the measured metric as ≈ +11%. |
| Winback offers worked in T2-05. This case is also a winback. It should work. | *If:* the offer is placed at the same moment as in the source. *Grounds:* `[interpretation]` T2-05 read its lift as timing-driven, not discount-driven. *Then:* trial start rate moves up, direction only. |

**CF1 — What a conditional claim is.** A statement about the case under review
made of three visible parts, in this order:

| Part | What it holds |
|---|---|
| **X — the condition** | what has to be true or has to be done for the statement to bite. For a finding it is most often that nothing changes; for a proposal it is the change itself |
| **Y — the grounds** | what the statement rests on, carrying its rule-8 label so the reader sees the kind of thing it is |
| **Z — the consequence** | what then happens, on a named quantity |

**CF2 — A finding carries `If:` as its first slot (hard).** The slot order of
§2.9 FD5 becomes `If:` → `Mechanism:` → `Consequence:` → `Price:` → `Fix:`. The
`If:` slot holds X in a few words: `nothing changes`, `the guardrail keeps the
approved margin`, `the goal metric stays ARPU per exposed user`. `Mechanism:`
is Y and `Consequence:` is Z, so a finding that carries the new slot is already
in conditional form. The headline is unchanged: it runs from the severity
literal to the first slot marker, and `If:` is now that marker.

**CF3 — The grounds carry a statement label (hard).** The `Mechanism:` slot of
a finding, and the `Grounds:` slot of a proposal, **open** with exactly one of
the four rule-8 labels:

`[fact]` — a measurement in a source card · `[interpretation]` — a source
team's reading of its own result · `[hypothesis]` — a transfer to this case, or
an assumption of the reviewer · `[computed]` — arithmetic over the numbers of
the card under review (§2.8).

This is the whole point of the section. §2.9 FD5 already forced the mechanism
to be **grounded**; it did not force the answer to say **what kind of ground it
is**, and a reader cannot tell a measured 42.14% from an assumed one by looking
at it. Exactly one label: a mechanism that is partly measured and partly assumed
is two mechanisms, and it is split.

**CF4 — A proposal is written in conditional form (hard).** Every bullet of
`## Product proposals` whose type is `[mechanic]`, `[segment]` or `[offer]`
carries three labelled slots, in this order:

| Slot | What goes in it |
|---|---|
| `If:` | the change proposed — X |
| `Grounds:` | Y, opening with one rule-8 label, and carrying the grounding source ID §2.7 PP3 already requires |
| `Then:` | Z — the expected direction on a named metric |

`[ungrounded]` bullets are exempt: they assert nothing about this case, they
name what would have to be researched, and §2.7 PP4 already governs them.

**CF5 — The consequent names a direction (hard).** The `Then:` slot contains at
least one word from the closed direction lexicon:

`up`, `down`, `higher`, `lower`, `rise`, `rises`, `fall`, `falls`, `grow`,
`grows`, `shrink`, `shrinks`, `increase`, `increases`, `decrease`, `decreases`,
`improve`, `improves`, `worsen`, `worsens`, `more`, `less`, `fewer`,
`unchanged`, `flat`, `no change`.

A direction is not a magnitude and rule 4 is untouched: `Then:` states which way
the metric moves, never by how much.

**CF6 — What is measured.** The linter counts the MAIN argument units — the
findings plus the typed proposals — and how many of them carry the complete
conditional form, and reports the pair as `conditional_form`. That count is the
machine-readable answer to rubric Q4; it is not a verdict on its own.

Compliant example (form only; the numbers are illustrative):

> - **[stop]** [topic: guardrail-margin-retention] We spend the slot and come
>   back with a retention number that cannot clear this launch. *If:* the
>   guardrail keeps the approved margin and the sample is not re-sized.
>   *Mechanism:* [computed] the guardrail resolves `40% × 2.4% ≈ 1.0 pp` while
>   the approved margin is `0.5 pp`, so `1.0 / 0.5 = 2×` the margin.
>   *Consequence:* a non-significant guardrail stays compatible with twice the
>   loss the team said it would accept. *Price:* decision impossible — the
>   question the experiment was built to settle stays open. *Fix:* re-size on
>   the approved margin before launch.

### 2.11 One idea, one place (normative; linter-enforced)

The rubric asks whether the answer is free of the same idea restated in
different words. The known failure is not copy-paste — the linter's 8-gram
check of §2.9 FD10 already catches that. It is the same mechanism appearing as
a risk in one section and as an effect to instrument in another, in different
words, so that a reader who has read both believes they have read two problems.

The rule is stated on the pair the answer is actually about: **a mechanism and
the segment it acts on**. Two statements about the same mechanism on the same
segment are one statement, and they are merged — with the price of the merged
one being the stronger of the two.

**UQ1 — Every MAIN bullet declares its topic (hard).** Each bullet of
`## Findings`, `## Product proposals` and
`## Non-monetization effects to instrument` carries exactly one topic tag,
written verbatim in this syntax and placed after the type or severity literal:

`[topic: <slug>]`

`<slug>` is lower-case kebab-case of two to six words, `[a-z0-9]+(-[a-z0-9]+)+`,
and it names the **mechanism and the segment**, not the section it sits in.
`guardrail-margin-retention` and `demo-dilution-chords-branch` are topics;
`risk-1`, `finding-a` and `retention` are not — the first two name a position
and the third names a metric.

**UQ2 — A topic appears once in MAIN (hard).** Two MAIN bullets carrying the
same slug are the same statement said twice: merge them into one bullet in the
section whose question they actually answer (§2.7's channel table), and keep the
stronger price. The linter reports the slug and both sections.

The check is on the collision, not on the honesty of the slug — a model can
always rename the second bullet. That is not a hole: renaming forces the answer
to write down, in the tag, that the two bullets are about different mechanisms,
and a reader who then finds them identical has a named claim to point at
instead of an impression.

**UQ3 — The appendix refers, it does not restate.** An appendix section may
mention a MAIN topic, but only as a pointer: the slug preceded by `see`. An
appendix that repeats the finding in full is the same defect one level down, and
the linter reports it as a warning. `## D. Findings without a price` holds
findings that never appeared in MAIN, so its topics are new and this does not
touch them.

**UQ4 — The lexical backstop stays.** §2.9 FD10's shared-8-gram warning is
unchanged. UQ2 catches the paraphrase it cannot; it catches the copy-paste that
survives a renamed topic.

**UQ5 — What is measured.** The linter reports every slug it read, the section
it read it in, and every collision, as `topics`. A duplicate-free answer is the
machine-readable answer to rubric Q7.

### 2.12 Nothing you could have written without reading the card (normative; linter-enforced)

The rubric states this one from the wrong end — *the answer contains no cheap
generic UI changes* — because the defect is an absence of specificity, and an
absence is hard to point at. Stated positively: **a line that could have been
written without reading this document does not belong in the main answer.**

§2.7 does not close this. It requires a product proposal to be grounded in an
analog, and "make the button more visible" is perfectly groundable: some source
in any corpus raised some conversion by making something more visible. What the
proposal never does is touch anything that is only true of *this* card.

**GN1 — A proposal is anchored in the card (hard).** Every bullet of
`## Product proposals` typed `[mechanic]`, `[segment]` or `[offer]` carries at
least one number that the experiment card under review states — a reach, a
coverage, a baseline, a margin, an expected effect — or a `[computed]`
statement over such numbers. A source ID is not an anchor for this rule: it
proves the answer read the evidence base, which is what §2.7 already asks, not
that it read the card. Checking this needs `--card`; without it the check is
skipped and the existing `W_CARD_NOT_SUPPLIED` warning covers the gap.

`[ungrounded]` bullets are exempt, for the same reason as in CF4.

**GN2 — The generic-advice lexicon (hard).** A closed list of formulations that
name a cosmetic change with no mechanism through the money chain. Matched
against the finding headlines, the proposal bullets and the `Fix:` slots of the
MAIN part:

`make … (more) visible / prominent / noticeable / obvious / salient / clearer /
discoverable`, `bigger / larger / brighter / bolder / higher-contrast button /
CTA / banner / text`, `improve the copy / wording / UX / UI / design /
onboarding / experience / messaging`, `add a CTA / call-to-action / button /
banner / tooltip / badge / popup`, `A/B test the colour / copy / button /
placement / wording`, `optimise the funnel / flow / onboarding / paywall / UI /
UX`, `increase visibility / awareness / engagement`, `better UX / UI / copy /
design / placement / messaging / wording`, `simplify the flow / UI / interface /
form`, `reduce friction`, `more prominent placement`, `clearer copy / wording /
messaging / value proposition`.

The lexicon is deliberately about the *shape of the phrase*, not about the
subject: a proposal may be about a button and pass, as long as it says through
which link of the money chain the button earns and which of the card's numbers
it acts on. It is the phrase that carries no mechanism that is banned, not the
surface.

**GN3 — Generic advice is not deleted, it moves.** The appendix gains
`## E. Generic suggestions`, for advice that is true of this experiment and of
any other. It is exempt from GN1 and GN2 — that is what the section is for —
and it keeps the answer honest instead of making it silent, exactly as
`## D. Findings without a price` does for §2.9.

**GN4 — What is measured.** The linter reports how many proposals and fixes it
screened, how many carried a card anchor, and every phrase it matched against
the lexicon, as `generic_screen`. A screen with no flagged line is the
machine-readable answer to rubric Q9.

Compliant and non-compliant, same subject:

| Line | Verdict |
|---|---|
| `[mechanic]` *If:* the demo is moved behind the first save. *Grounds:* [interpretation] T2-07 read its lift as intent-driven. *Then:* trial start rate moves up. | fails GN1 — nothing in it comes from this card |
| `[mechanic]` *If:* the demo is moved behind the first save, keeping the 78% Chords reach. *Grounds:* [interpretation] T2-07 read its lift as intent-driven. *Then:* trial start rate moves up. | passes |
| *Fix:* make the demo entry point more visible. | fails GN2 |
| *Fix:* cut the goal metric to the 78% of the arm that can reach the demo. | passes |

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
