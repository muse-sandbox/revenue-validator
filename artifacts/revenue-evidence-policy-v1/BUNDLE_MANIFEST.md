# BUNDLE MANIFEST — revenue-evidence-policy-v1 (FLOW-580)

Frozen: 2026-08-05. Evidence Policy V1 for Revenue Validator V1 — the decision
rules distilled from the FLOW-579 blind A/B verdict (formal NO, gate §6
condition 5) on top of the FLOW-574 relevance model and Revenue KB V1
(FLOW-578). Input for the Validator V1.1 assembly and regression rerun
(FLOW-581); rerun preconditions are part of the policy.

| File | sha256 | Contents |
|---|---|---|
| `evidence_policy.md` | `be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3` | Short human policy: decision matrix by L1/L2/L3, mandatory validator behaviors, conflicts, blocking requirements, fact vs transfer hypothesis, retention/side-effect zone, rerun gate before FLOW-581 freeze |
| `evidence_policy_rules.yaml` | `e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a` | Machine-readable rules: deterministic L-level computation from axes, card linter hard errors, allowed influence per level, blocking gate, mandatory outputs, conflict resolution, rerun gate |

Working copies live in the task repo at `output/flow-580/` (gitignored);
this bundle is the canonical location, next to `revenue-kb-v1/` and
`revenue-corpus-prep-v1/`.
