# Runbook

## Validate one experiment

1. Take the experiment document.
2. Assemble the prompt: `packages/revenue-kb-v1.2/validator_prompt_v1_2.md`,
   substituting the knowledge context and the card.
3. Run in a clean context, no search tools, no access to the outcome.
4. Lint the answer.
5. Save inputs, outputs and a manifest with checksums.

Details: `.claude/skills/validator-run/`.

## Compare with and without the knowledge base

Same as above, twice, with a byte-identical prompt. The only difference is
whether the knowledge context block is filled. Randomize which arm is shown
first to whoever judges them, and strip markers that reveal the arm.

## Evaluate on held-out cases

Read `.claude/skills/holdout-discipline/` first. The order — reserve, build,
blind, infer, then open outcomes — is what makes the result meaningful, and it
cannot be repaired afterwards.

## Add a new version

Never edit a frozen package. Create a new directory, copy forward what does not
change, record what does, and write a fresh manifest with SHA-256 per file.
Verify the previous packages still match their own manifests before and after.

## Verify integrity

Each package has a `BUNDLE_MANIFEST.md` or `FREEZE_MANIFEST.md`. Recompute
SHA-256 for every listed file and compare. A mismatch means a frozen package
was modified, which invalidates any evaluation that relied on it.
