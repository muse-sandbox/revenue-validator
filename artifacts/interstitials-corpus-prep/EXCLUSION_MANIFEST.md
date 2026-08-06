# EXCLUSION MANIFEST — Interstitials Holdout (FLOW-568)

**Правило (жёсткое): перечисленные ниже эксперименты, их страницы, алиасы, дубли, Jira-задачи и любые пересказы их результатов ЗАПРЕЩЕНО использовать при построении knowledge base (FLOW-567).** Knowledge builder и inference-агент не читают этот файл, исходные документы holdout, `holdout-blind/` (builder), `ground-truth-sealed/` (оба), локальное зеркало `context/hypotheses/` и поле `success_variation` реестра `ab_experiment`.

## Holdout-эксперименты

| Neutral ID | Исходный эксперимент | Confluence pageId / документ | AB experiment IDs (вкл. relaunch-дубли) | Jira | Алиасы |
|---|---|---|---|---|---|
| IH-01 | UG App: paywall – pre-paywall with animation for interstitials | 773658792 — «[2026-03-09] UG App: paywall – pre-paywall with animation for interstitials [2026-07-01]» — https://alice.mu.se/pages/viewpage.action?pageId=773658792 | 7160, 7187 (relaunch) | UMN-10952 | реестр: «[UG Monetization] Pre-paywall with animation for interstitials (relaunch)»; механика: scratch-to-reveal coupon |
| IH-02 | UG App: winback – final interstitial offer | 788612067 — «[2026-05-04] UG App: winback - final interstitial offer [2026-07-30]» — https://alice.mu.se/pages/viewpage.action?pageId=788612067 | 7487 | UMN-11515 | реестр: «[UG Monetization] UG App: winback - final interstitial offer» |
| IH-03 | UG App: personalized interstitial | 788613565 — «[2026-05-05] UG App: personalized interstitial [2026-06-18]» — https://alice.mu.se/pages/viewpage.action?pageId=788613565 | 7454 | UMN-11540 | реестр: «[UG Monetization] UG App: personalized interstitial» |
| IH-04 | UG App: interstitial – discounted prices | 811868738 — «[2026-07-03] UG App: interstitial - discounted prices [2026-XX-XX]» — https://alice.mu.se/pages/viewpage.action?pageId=811868738 | 7712 | UMN-12220 | реестр: «[UG Monetization] UG App: interstitials - discounted prices» |

Связанные дубли/копии одного запуска: relaunch-записи реестра учтены в колонке AB IDs (7160→7187). Отдельных страниц-дублей этих запусков не обнаружено (проверено CQL-поиском и дедупликацией inventory).

Связанные документы, которые могут пересказывать исходы holdout (также запрещены builder'у): [DOCS] «Монетизационные слои UG – Local interstitials» (777830942), «UG App: Interstitials research» (777823482), retro/plan-fact страницы Q2 2026 (813827665, 813827670, 800228682), «[DOC] UG Experiments Health Status» (811865807), «[DOC] UG App Winback offer sources» (815597838), meeting notes Revenue Weekly 2026 годов.

## SHA-256 файлов

### holdout-blind/
```
38c58a2a761823105f21493e6518f98e89cfa1d8e2a48585beab43d19f3b6169  holdout-blind/IH-01.md
179cd5ad284ae6c59a4beeb04837c972f86a9bddeceaea359b0a7e9fae573664  holdout-blind/IH-02.md
9381137e3faee6547f15ead3dd609b9749bcb9800e2556c632d2fad2fbfefd6c  holdout-blind/IH-03.md
c7d5494b93cf703a482ab99780b176b1ee93c44efee988b3da2953441f6bc996  holdout-blind/IH-04.md
```

### ground-truth-sealed/
```
a4a4f4f260c577ac67fec3139d41593cba99a1e8f41ebbed496015bd4c4e4758  ground-truth-sealed/GT-IH-01.md
12b7c06e77b42d9977d607780384708d654a8d408a40fb2e10de05c536dd2985  ground-truth-sealed/GT-IH-02.md
021e83db63b2f2f9d5662961dcfced33abe4e17de4b15292eaf5e994348643e8  ground-truth-sealed/GT-IH-03.md
36e41bb17b950fd9260ade4928c461ddd7f7d870b560685edd74cb1490b90735  ground-truth-sealed/GT-IH-04.md
d7c322237db14229611e5c982c9acb72b44482c3d9a6770c23e3e775972002ec  ground-truth-sealed/MAPPING.md
```
