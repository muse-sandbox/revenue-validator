# Revenue Corpus Prep V1 — Stratified Blind Holdout (FLOW-575)

Заморожённый stratified blind holdout из 6 завершённых revenue-экспериментов,
сформированный ДО сборки Knowledge Base V1. Источник кандидатов — корпус FLOW-577
(24 кейса, все сверены с Confluence-страницами 2026-08-04). Split заморожен
2026-08-04 (`split_manifest.md`); после freeze состав не меняется.

Строение повторяет `interstitials-corpus-prep/` (FLOW-568): blind-карточки без
исходов, запечатанный ground truth с mapping, exclusion-манифест для KB-билдера,
leakage-check, pre-registered evaluation protocol, SHA-256 всего бандла.

## Состав holdout (страты)

| ID | Страта | Что тестирует |
|---|---|---|
| RH-01, RH-02 | 1 — та же поверхность и механизм, что якорь (App interstitial-слой) | ближний перенос |
| RH-03, RH-04 | 2 — тот же этап flow (S3–S4 exposure), другая поверхность | средний перенос |
| RH-05, RH-06 | 3 — та же метрика (ARPU/конверсия), другой flow/механизм (web) | дальний перенос: guardrails/measurement, не продуктовые величины |

Раскрытие страты в ID — часть дизайна (ось анализа переносимости); исходы не раскрывает.

## Кому что разрешено читать

| Каталог / файл | KB V1 builder | Inference-агент (плечи A/B) | Судья (оценка) |
|---|---|---|---|
| `README.md`, `BUNDLE_MANIFEST.md` | ✓ | ✓ | ✓ |
| `EVALUATION_PROTOCOL.md` | ✓ | ✓ | ✓ |
| `holdout-blind/` | **✗ запрещено** | ✓ (его вход) | ✓ |
| `ground-truth-sealed/` | **✗ запрещено** | **✗ запрещено** | ✓ (после получения предсказаний) |
| `split_manifest.*`, `EXCLUSION_MANIFEST.md`, `LEAKAGE_CHECK.md` | только `EXCLUSION_MANIFEST.md` (обязан выполнять) | ✗ | ✓ |

Дополнительные запреты builder'а и inference-агента — в `EVALUATION_PROTOCOL.md` §8
и `EXCLUSION_MANIFEST.md` (исходные страницы holdout, зеркало базы гипотез,
`success_variation`, бандлы `interstitials-*`, Linear-комменты задач семейства,
поиск по формулировкам blind-карточек).

## Состав

- `split_manifest.md` + `split_manifest.json` — детерминированное правило отбора,
  проверка сожжённости (T1-07..T1-10 = IH-01..04; HX-пересечений нет), составы, SHA-256.
- `holdout-blind/RH-01…RH-06.md` — очищенные pre-launch карточки (английский,
  формат IH-*), исходы и идентификаторы удалены.
- `ground-truth-sealed/GT-RH-01…06.md` + `MAPPING.md` — фактические исходы с
  p-values, решения, уроки, ссылки; mapping ID → эксперимент.
- `EXCLUSION_MANIFEST.md` — что обязан исключить/не читать KB V1 builder; SHA-256 карточек.
- `EVALUATION_PROTOCOL.md` — pre-registered протокол A/B-оценки KB V1 (6 кейсов,
  пороги YES/YES-NARROW/NO, стратное правило C6).
- `LEAKAGE_CHECK.md` — результаты автоматической+ручной проверки утечек.
- `BUNDLE_MANIFEST.md` — SHA-256 всех файлов пакета.

## Handoff

KB V1 builder получает только: `README.md`, `BUNDLE_MANIFEST.md`,
`EXCLUSION_MANIFEST.md`, `EVALUATION_PROTOCOL.md` — и вход из FLOW-577 inventory
**с уже удалёнными** записями T1-05, T1-06, T2-03, T2-04, T3-04, T3-07.
Inference-агент получает только `holdout-blind/` + frozen KB V1 bundle по протоколу.
