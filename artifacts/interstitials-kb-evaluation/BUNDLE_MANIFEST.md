# BUNDLE MANIFEST — interstitials-kb-evaluation (FLOW-571)

Freeze: 2026-08-04. SHA-256 всех файлов бандла (кроме самого манифеста).

Хронология фаз: preflight (проверка 48/48 хэшей входных бандлов) → blind pairwise review (только blind-pairs + holdout-blind) → freeze `blind_pairwise_scorecards.md` 08:43:16Z → вскрытие `arm_mapping_sealed.md` + `ground-truth-sealed/` → unblind-оценка C1–C7 → вердикт `PENDING_HUMAN_REVIEW` (предварительно YES).

```
0142d53f442e7a7a78669a996beb8f41e51b40c82a703cd17fd256d6f8c35bbf  blind_pairwise_scorecards.md
220f275026836dbcb9e9d38cfb5245c6ad55dc86af975c780c49bba5cb2c06ae  case_scorecards.md
746844d3fd4bedcf724486d9409f85663f4e63a496599b61256bcc8481f789f1  metrics.md
c5049448b10ab892b58898329c9a1d8d2fea977408e166135fceeb78e5f1ede9  grounding_audit.md
346f4e955bc101a69a4c943f1d5382f18f49110b908565e5d63ac44b556b7e80  errors_and_limitations.md
219be5c94487173abd4dbd135a8b1f224c2d8175159e44dbb46e6710df2096d6  product_owner_review.md
e45ce5bfceda28e120e213cacbe446ad6b49f424d9c01c3ab23b0f3f856348fa  analyst_fact_check.md
02bde108ff7d6180fb375386bef20119fefe85df5969f54847eca6cf21cbc7e0  final_verdict.md
8a3f088e22bb6007ccf905a9da24d6936036e2867aec2ba65974c885561ff6bd  recommendations_for_validator_v1.md
```

`blind_pairwise_scorecards.md` заморожен ДО вскрытия arm mapping / ground truth; его sha256 (`0142d53f…`) зафиксирован в тексте `case_scorecards.md`, `metrics.md` и `final_verdict.md` — любое изменение файла после freeze обнаружимо.

## Preflight re-check (для аналитика)

Входные бандлы на момент оценки:
- `interstitials-kb-v0/FREEZE_MANIFEST.md` — 7/7 файлов совпали;
- `interstitials-kb-ab-run/BUNDLE_MANIFEST.md` — 19/19 совпали;
- `interstitials-corpus-prep/BUNDLE_MANIFEST.md` — 22/22 совпали.

Перепроверка: из каждой директории выполнить сверку sha256 по строкам соответствующего манифеста (скрипт-однострочник — в `analyst_fact_check.md` п.1; та же логика, что применялась здесь).
