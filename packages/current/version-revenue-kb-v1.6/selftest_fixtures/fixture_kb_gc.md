# Synthetic fixture knowledge base with generalization classes (linter selftest only)

Entirely invented sources and classes for testing the V1.2 scope checks. Not
real experiments; the topics (widget nudges, glow buttons) do not exist.

### T9-01 — Synthetic: imaginary widget banner test
- coords: S3–S4; imaginary banner; mechanism new-surface; metric ARPU
- validity: SRM ok; result significant-positive; decision rolled-out

### T9-02 — Synthetic: imaginary pricing tweak on a made-up menu
- coords: S5–S6; imaginary plan menu; mechanism price; metric revenue
- validity: SRM ok; result significant-negative; decision killed

### T9-03 — Synthetic: imaginary widget nudge that earned money
- coords: S3–S4; imaginary widget nudge; mechanism invented; metric ARPU
- validity: SRM ok; result significant-positive; decision rolled-out

### T9-04 — Synthetic: imaginary glow-button restyle
- coords: S3–S4; imaginary glow button; mechanism invented; metric ARPU
- validity: SRM ok; result powered-null; decision killed

## Machine-readable generalization classes (synthetic)

```
generalization_class: GC-90
  label: synthetic widget nudges — invented family for the selftest only
  keywords: widget nudge, widget nudges
  outcome_positive: T9-03
  outcome_negative: T9-01, T9-02
```

```
generalization_class: GC-91
  label: synthetic glow-button restyles — invented family for the selftest only
  keywords: glow button, glow buttons
  outcome_positive: T9-01
  outcome_negative: T9-04
```
