# MAPPING — Revenue Holdout V1 (FLOW-575)

SEALED ground-truth mapping. Читает только судья оценки (после получения предсказаний).

| RH-ID | Страта | FLOW-577 key | Original experiment (page title) | pageId | URL | AB ids | Jira | Run dates |
|---|---|---|---|---|---|---|---|---|
| RH-01 | 1 | T1-05 | [2025-08-01] UG App: winback - interstitials for former subscribers [2025-10-17] | 714409638 | https://alice.mu.se/pages/viewpage.action?pageId=714409638 | 6461 (registry 2025-09-09..09-16), 6644 (relaunch 2025-10-13..10-17; блока результатов на странице нет) | UMN-9259 | page 2025-08-01..2025-10-17 |
| RH-02 | 1 | T1-06 | [2025-08-20] UG App: paywall – offer instead of ad interstitials, iter 3+ [2026-03-13] | 714432870 | https://alice.mu.se/pages/viewpage.action?pageId=714432870 | 6491, 6626, 6716, 6896 | UMN-9389, UMN-10264 | page 2025-08-20..2026-03-13 |
| RH-03 | 2 | T2-03 | [2025-12-09] UG App: sale - animation for XMAS and NY sales [2025-12-30] | 746536863 | https://alice.mu.se/pages/viewpage.action?pageId=746536863 | 6878 (run 2025-12-13..12-22) | UMN-10299 | page 2025-12-09..2025-12-30 |
| RH-04 | 2 | T2-04 | [2025-12-16] UG App: explore, sale – Promo block instead of sale banner | 746543363 | https://alice.mu.se/pages/viewpage.action?pageId=746543363 | 6902 (run 2026-01-27..2026-02-02) | UMN-9885 (idea UMI-92) | run 2026-01-27..2026-02-02 |
| RH-05 | 3 | T3-07 | [2026-04-20]: UG Web — сheckout size optimization [2026-05-26] (в заголовке кириллическая «с») | 787253507 | https://alice.mu.se/pages/viewpage.action?pageId=787253507 | 7328 (данные 2026-05-04..05-11) | UMN-11436 | page 2026-04-20..2026-05-26 |
| RH-06 | 3 | T3-04 | [2026-06-11] UG Web: permanent banner — two plans: trial & monthly | 805316848 | https://alice.mu.se/pages/viewpage.action?pageId=805316848 | 7598 (run 2026-06-19..06-25) | UMN-11941 | run 2026-06-19..2026-06-25 |

Примечания:
- Снапшоты страниц, по которым построены GT-карточки: `output/confluence/flow577_verify/<pageId>/` в worktree `flow-577-04-revenue-flow-2` (скачаны 2026-08-04).
- Активационные события: RH-03/RH-05 — `App Experiment Start` (item_id = exp id); RH-04 — `Banner Tour Close`; RH-01/RH-02 — интерстишльные exposure-события (детали в GT-карточках); RH-06 — web-эксперимент.
- Результатные классы (по inventory V0.1): RH-01 significant-positive / rolled-out; RH-02 mixed / rolled-out; RH-03 inconclusive / rolled-out; RH-04 significant-negative / killed; RH-05 mixed / rolled-out; RH-06 inconclusive / killed.
