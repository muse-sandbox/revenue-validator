# Synthetic experiment card (linter selftest only)

Entirely invented. Not a real experiment, not derived from any holdout case.

## Mechanics

The invented widget is shown once in the synthetic surface. 64% of the test
arm reaches the branch where it can appear, and 25% of sessions in that
branch have no eligible content, so the widget stays hidden for them.

## Hypothesis

Showing the widget lifts the invented metric by 30% on the users who see it.

## Design and power

- Primary metric: invented metric per exposed user.
- This design resolves a difference of about 3 pp on the overall arm.
- Guardrail: synthetic retention, working margin -1.5 pp.
- Minimum detectable effect on the guardrail: -4.2 pp.
