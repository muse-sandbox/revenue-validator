# EXCLUSION MANIFEST — Revenue Holdout V1 (FLOW-575)

**Правило (жёсткое): перечисленные ниже эксперименты, их страницы, алиасы, дубли,
Jira-задачи и любые пересказы их результатов ЗАПРЕЩЕНО использовать при построении
Knowledge Base V1.** KB V1 builder и inference-агент не читают этот файл целиком
ради mapping'а — builder обязан выполнить раздел «Инструкция builder'у», inference-агент
не читает файл вовсе (см. README, права доступа).

## Инструкция builder'у KB V1 (обязательная)

1. Из входного inventory FLOW-577 (V0.1) **удалить записи с ключами**:
   `T1-05`, `T1-06`, `T2-03`, `T2-04`, `T3-04`, `T3-07` — до любого чтения их содержимого.
2. НЕ читать: бандл `interstitials-kb-v0/` (его `knowledge_base.md` и
   `pattern_cards.md` содержат исходы двух holdout-кейсов как KS-05/KS-06);
   каталог `interstitials-corpus-prep/knowledge-sources/` (KS-05, KS-06);
   локальное зеркало `context/hypotheses/`; поле `success_variation` реестра
   `ab_experiment`; каталоги `holdout-blind/` и `ground-truth-sealed/` этого бандла.
3. НЕ открывать перечисленные ниже Confluence-страницы и не искать их по названиям,
   механикам или числам из blind-карточек.

## Holdout-эксперименты

| Neutral ID | Исходный эксперимент | pageId | AB IDs | Jira |
|---|---|---|---|---|
| RH-01 | UG App: winback - interstitials for former subscribers | 714409638 | 6461, 6644 (relaunch) | UMN-9259 |
| RH-02 | UG App: paywall – offer instead of ad interstitials, iter 3+ | 714432870 | 6491, 6626, 6716, 6896 | UMN-9389, UMN-10264 |
| RH-03 | UG App: sale - animation for XMAS and NY sales | 746536863 | 6878 | UMN-10299 |
| RH-04 | UG App: explore, sale – Promo block instead of sale banner | 746543363 | 6902 | UMN-9885, UMI-92 |
| RH-05 | UG Web — checkout size optimization | 787253507 | 7328 | UMN-11436 |
| RH-06 | UG Web: permanent banner — two plans: trial & monthly | 805316848 | 7598 | UMN-11941 |

Связанные документы, которые могут пересказывать исходы holdout (также запрещены
builder'у): [DOCS] «Монетизационные слои UG – Local interstitials» (777830942),
«UG App: Interstitials research» (777823482), retro/plan-fact страницы Q4 2025 /
Q1–Q2 2026, «[DOC] UG Experiments Health Status» (811865807), «[DOC] UG App
Winback offer sources» (815597838), meeting notes Revenue Weekly 2025–2026,
Linear-комменты FLOW-568/570/571/574/575/576/577/584, предыдущая страница
Halloween-эксперимента (731485619 — прямой предшественник RH-03; его результаты
разрешены как generic precedent ВНУТРИ blind-карточки RH-03, но сама страница
для builder'а запрещена, т.к. содержит перекрёстные ссылки на исход RH-03).

Смежный пред-кейс RH-02: страница iter 1–2 (682704865, AB 6002/6128/6191) —
разрешена builder'у как knowledge-источник (это T1-02, в holdout не входит),
но пересказы исходов iter 3+ на ней отсутствуют (проверено при сверке FLOW-577).

## SHA-256 файлов

(генерируются при freeze; канонические значения — в `BUNDLE_MANIFEST.md`)

### holdout-blind/
```
ab24eb51ab839bcd615828cf4a1d4794917bd37fd410c4c58e7675a48c55e804  holdout-blind/RH-01.md
eb76cb799846d7eb1019977bb927df258792607bd78e0fe79ab43179b5e938bd  holdout-blind/RH-02.md
0d6cd5aead29f2074f1dc370c27b3eb8bdcab9fe1e15e69e07cc028df74983ee  holdout-blind/RH-03.md
906e8cf04414a1e10ad7364770ed8e36b5bb8fea9e005e34513308b3e91ef7e5  holdout-blind/RH-04.md
ef5f81a602ebb072f56e76ec030d81c17959b2137c20846ee8698bc04d96b14a  holdout-blind/RH-05.md
95283c2befb79886104e21c718ad6fd46ac6e4e479077751fa01bd58db10aa62  holdout-blind/RH-06.md
```

### ground-truth-sealed/
```
0853664105f4b28f1fe935fb148c54d8b0f2578059eb29a093d33dae77f77529  ground-truth-sealed/GT-RH-01.md
6b687e2be9607e911cdeb6a302fb7a7156d95e5fd9e38516d28da440a02d3933  ground-truth-sealed/GT-RH-02.md
192c8614a95d02a032fd06b93bca3bc2b311c7bef75cb4d382560c03ce30d2cf  ground-truth-sealed/GT-RH-03.md
e7c9fd96b7440a512b2393752498d32ddb89ef71191c4a25f636ef31b4de5338  ground-truth-sealed/GT-RH-04.md
10766e6fa355820a773ad24287de8d4819fa0989fe8edde9f96ac69b76662091  ground-truth-sealed/GT-RH-05.md
60475482f7b0f48efc3e0975853fe6f726c4430ec1a1fef1be21204661113b9a  ground-truth-sealed/GT-RH-06.md
bc3f03defa59f0d3907f0c2226d89dc51767044ed136b97d3e1e7aa08899200e  ground-truth-sealed/MAPPING.md
```
