# Closeness model

How the validator decides whether a past experiment may inform a new one.
Normative definition lives in `packages/revenue-kb-v1.2/knowledge_base.md` §2.2;
this file is the human-readable summary.

## Axes

Every analog is described on ten axes: flow stage, segment, trigger and
eligibility, surface, mechanism, offer, target behavior, metric, money chain,
guardrails. Plus three dedicated fields: segment monetization state, money
chain link, platform.

Each axis is `exact`, `adjacent` or `different`.

## Levels

| Level | Meaning | What may be used |
|---|---|---|
| L1 | direct analog | sign and mechanism transfer as a hypothesis |
| L2 | same shape, different context | warning only, not a prediction |
| L3 | weak signal | guardrails, measurement and sizing lessons only |

The level is **computed** from axis values, never chosen by the model. A linter
recomputes it from the answer's own analog card; any mismatch invalidates the
answer.

## Hard rules

- Effect magnitudes never transfer as predictions. They may appear only as
  explicitly labelled sizing priors.
- L3 alone can never justify changing a launch decision.
- When no L1 or L2 analog exists, the answer must say so rather than promote
  the nearest weak source.
- Outcomes from inconclusive or bug-contaminated cases ground measurement
  lessons only.
