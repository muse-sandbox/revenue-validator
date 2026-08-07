# FREEZE MANIFEST — Interstitials KB V0 (FLOW-569)

- **Версия:** V0
- **Дата заморозки:** 2026-08-04
- **Статус:** заморожен до завершения A/B-теста FLOW-570. Файлы бандла не изменяются; любое изменение после теста — только как новая версия (V1) с фиксацией причин.
- **Единый A/B prompt:** `combined_validator_prompt.md` — одинаков для плеч A и B; единственная разница плеч — наличие KNOWLEDGE CONTEXT (`knowledge_base.md` + `pattern_cards.md`) во входе плеча B.
- **Протокол оценки:** `EVALUATION_PROTOCOL.md` — pre-registered до открытия holdout; пороги после открытия не меняются.

## SHA-256 файлов бандла (кроме самого манифеста)

```
dc04a072dd84a4ee29dc88059518c0b2d011033c5f841d133ed583d7f0b616c3  knowledge_base.md
0bd1f2e06b53a53db43c4b821922fa7f183645b7cb0afd18ca6ad3836685e365  pattern_cards.md
eb815861b78e0707db9270c202568c39d7deeffd2d441c75233e0cac4dfe2ff5  source_traceability.md
b6e4c6151ae04e9fbc7d98969ce3121cd927d520cb31f6ed4708eee5318f3ee1  product_review_prompt.md
43ff7f52b3dc51aefcfe2a1dc596ea54241ff3afe3fa17e838116222df65d612  combined_validator_prompt.md
9f0ca39f3a76df8c470c6b7e26a9e602344a0e02fd876753ca055cd8f7c120a7  EVALUATION_PROTOCOL.md
9f09ea44a758748fb857741bb119be86678d729a6a2bdde1544a6b4ea1c88893  build_report.md
```

## Внешние frozen-зависимости (не входят в бандл, зафиксированы хэшами)

- Validator V0 prompt: `flow546-clean-input/validator-v0/validator_v0_prompt.md`, sha256 `61b2ee469049b1239705e3b4f4e5e30fb8043da10d126952fc90a0584e64b330` (встроен в `combined_validator_prompt.md` дословно, совпадение проверено программно).
- Source cards KS-01…KS-06: sha256 — см. `source_traceability.md` (из `BUNDLE_MANIFEST.md` корпуса interstitials-corpus-prep, freeze 2026-08-04).
