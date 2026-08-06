# FLOW-565 pre-registered evaluation protocol

This protocol was fixed before opening the Validator V0 blind-run outputs for evaluation. Do not change thresholds after reading the outputs or ground truth.

## Scope

The evaluation tests whether Validator V0 usefully improves pre-launch monetary decisions. It does not prove growth in causally measured post-rollout incremental revenue.

## 1. Bad-slot catch rate

For each `negative / no meaningful uplift` case, the validator must:

- avoid an unconditional `launch`;
- identify at least one material pre-launch risk confirmed by ground truth or an independent reviewer.

Success threshold: at least 2 of 3 cases.

## 2. False-blocker rate

For the three `positive` cases:

- zero confident `deprioritize` recommendations;
- at most one blocking `revise` whose concern is not supported by ground truth.

A specific non-blocking concern on a positive case is not a false blocker.

## 3. Ambiguity handling

Both `inconclusive / not measurable` cases must receive `revise` because of reach, power, data quality, or measurability.

`Deprioritize` solely because evidence is missing is an error.

Success threshold: 2 of 2 cases.

## 4. Action-class usefulness

An independent reviewer must confirm a useful action class for at least 6 of 8 cases:

- positive: `launch` or a concrete non-blocking `revise`;
- negative/no-uplift: `revise` or `deprioritize` with a demonstrable pre-launch reason;
- inconclusive/NM: `revise` because of measurability.

## 5. Specificity

At least 6 of 8 answers must contain a concrete risk or requested change tied to a number, a model field, or missing evidence. A generic checklist does not count.

## 6. Evidence discipline

- 8 of 8 answers contain no invented facts;
- `missing` stays `missing`;
- template instructions or demonstration values are not treated as project data;
- every critical concern cites a specific input.

Any ground-truth leakage into an inference input makes the backtest invalid.

## 7. Confidence discipline

High confidence is not allowed when a central coefficient, monetary metric, reachable audience, or measurement plan is missing.

## 8. Workflow time

Review time must be no more than 10 minutes per project.

## Overall decision

The backtest passes for progression to a shadow pilot only if all of the following hold:

- bad-slot catch rate at least 2/3;
- zero confident `deprioritize` on positive cases;
- ambiguity handling 2/2;
- action-class usefulness at least 6/8;
- evidence discipline 8/8;
- review time at most 10 minutes per project.

Return one final status: `PASS`, `FAIL`, or `INVALID`.

If the prompt is changed after this evaluation, these eight cases become development data and cannot be described as an independent holdout again.

Subjective judgments, especially action-class usefulness and whether a revision is genuinely blocking, must be listed separately for confirmation by Artyom or the analyst.
