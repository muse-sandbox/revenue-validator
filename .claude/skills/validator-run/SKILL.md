---
name: validator-run
description: Run the revenue validator on an experiment card. Use when asked to validate, review or assess a pre-launch experiment document, or to reproduce an A/B comparison between arms with and without the knowledge base.
---

# Running the validator

## Assemble the input

The prompt is a template with two placeholders:

```
packages/version-revenue-kb-v1.6/validator_prompt_v1_6.md
  {KNOWLEDGE_CONTEXT}  ->  knowledge_base.md + pattern_cards.md, concatenated
  {EXPERIMENT_CARD}    ->  the experiment document under review
```

Strip everything above the `## PROMPT` heading — it is bundle metadata, not
part of the instruction.

Typical sizes: ~28 KB without the knowledge context, ~100 KB with it.

## Run it

In a fresh context with no conversation history about this experiment. The run
must not have:

- search tools, web access, or Confluence access;
- any file other than the assembled prompt;
- any knowledge of the outcome of the experiment under review.

For an A/B comparison both arms use a byte-identical prompt. The only
difference is whether the knowledge context block is filled.

## Lint the answer

```bash
python3 packages/version-revenue-kb-v1.6/linter.py ANSWER.md \
  --kb packages/version-revenue-kb-v1.6/knowledge_base.md \
  --patterns packages/version-revenue-kb-v1.6/pattern_cards.md
```

Add `--no-kb-arm` for the arm without a knowledge context — there the linter
expects no analog cards at all.

The linter recomputes closeness levels from the answer's own analog cards and
flags corpus-wide generalizations without a scope annotation. It checks form,
not substance: a PASS does not mean the advice is good.

## Record the run

Save inputs, outputs and a manifest with SHA-256 for each file, plus the
checksums of the frozen files used. Прогоны записываются в рабочей папке (`VALIDATOR_WORK_DIR`, по умолчанию `revenue-validator-work` рядом с репозиторием), не в репозиторий.

## Before calling a run a pilot case

Record the human's decision **before** showing them the answer: what they were
going to do, expected effect, main risks, confidence. Without that, a changed
decision cannot be distinguished from a decision they already held.
