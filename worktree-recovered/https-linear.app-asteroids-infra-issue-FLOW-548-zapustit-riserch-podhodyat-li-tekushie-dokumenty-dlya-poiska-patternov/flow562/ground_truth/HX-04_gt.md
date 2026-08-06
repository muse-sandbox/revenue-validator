# HX-04 — ground truth (doc-side)
Источник: 579970694 | [2024-10-15] UG Web: tour update on desktop web [2025-04-10] | https://alice.mu.se/pages/viewpage.action?pageId=579970694
Эксперимент(ы): на странице оба results-блока подписаны «#5463». По warehouse-фактам (`warehouse_facts.md`) итерация 1 = #5463 (2024-11-07→11-08), итерация 2 = #5769 (2025-02-25→02-28) — метка «#5463» во втором блоке выглядит незамененной копией. Jira: UMN-6853.

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
- Итерация 1: +27 accesses, +16 charges, +$685 revenue на модельный период; ARPU $0.041→$0.044 (+6%); target Tab View → access 0.11%→0.12% (+10%). Forecast (per day) в results-блоке: Tab View 270,830/арм; план-факт см. ниже.
- Итерация 2: +23 accesses, +14 charges, +$915 revenue; ARPU $0.044→$0.048 (+10%). Forecast (per day): 204,820/арм.

## Факт: target metric и денежные метрики (значения A/B, uplift, p-value/CI — как в документе)
Итерация 1 (exposure: Tab View; 64,971 vs 64,654 members):
- access cr: 0.052% → 0.045%, diff −14.29%, p=0.54; charge cr: 0.028% → 0.032%, +17.24%, p=0.62.
- ARPU $0.022 → $0.026, +17.08%, p=0.61; AOV $64.42 → $68.80, +6.80%, p=0.52; ARPPU $78.74 → $78.63, −0.14%, p=0.99.
- Revenue: $1,417 (control) vs $1,651 (variation); accesses 45 vs 35; charges 22 vs 24.
- Воронка механики: Tab Practice Mode View 44,574 → Click 307 (0.7%) → Preview View 306 (100%). Менее 1% кликнули по кнопке.
- Forecast vs Fact (per day): Tab View 270,830 (план) vs 270,830; accesses 188 vs 147 (−41); charges 92 vs 101 (+9); revenue $5,907 vs $6,916 (+$1,009). (Так в документе; строки «1/2» — план/факт.)

Итерация 2 (exposure: App Experiment Start; 132,173 vs 132,066 members):
- access cr: 0.05% → 0.06%, +5.64%, p=0.739; charge cr: 0.034% → 0.029%, −15.49%, p=0.444.
- ARPU $0.0290 → $0.0253, −12.82%, p=0.527; AOV +2.95%, p=0.749; ARPPU +3.15%, p=0.815.
- trial → charge: 32.31% → 18.67%, −42.22%, p=0.063; charge → 14d cancel: 17.31% → 6.82%, −60.61%, p=0.105.
- Revenue: $3,839 (control) vs $3,344 (variation); accesses 96 vs 104; charges 52 vs 44; charged trials 21 vs 14.
- Воронка тура: Tour start 130,599 → Chords Hook 83,256 (63.75%) → … → PlayBack Hook 78,018 (Tour Start→PlayBack 59.74%, в тексте «~60% дошли до последнего окна») → Landing Checkout 9,828 (7.53% от старта) → Clicked Purchase 60 (0.61%) → Accesses 5 (Tour Start→Access 0.0038%) → Charges 2. Менее 1% дошедших до чекаута кликнули покупку.
- Forecast vs Fact (per day): Tab View 204,820 vs 204,820 (0); accesses 148 vs 161 (+13); charges 80 vs 68 (−12); revenue $5,906 vs $5,168 (−$738).

## Достигнутая выборка и длительность (vs дизайн)
- Итерация 1: дизайн 13 дней / 1,664,683 на арм; факт 1 день, 64,971/64,654 (~3.9% дизайна). Чек «duration of exp >= design» — incomplete. A/B-баланс сохранён; багов и внешних эффектов не отмечено.
- Итерация 2: дизайн 15 дней / 3,138,690 (на все вариации); факт 4 дня, 132,173/132,066 (~8% дизайна). Чек «duration of exp >= design» — incomplete. A/B-баланс сохранён.

## Денежные guardrails (факт)
Guardrails до запуска не заявлены. Фактические продуктовые/SEO-метрики (ит.1): retention 1d +0.76% p=0.33; retention 7d +0.50% p=0.28; members with Long Tab −0.17% p=0.47; pageview per session +0.51% p=0.55 — всё ns. Ит.2: retention 1d 36.85%→36.56%, retention 7d 64.14%→63.86%, long tab 89.15%→87.93%, pageview/session 3.864→3.828 (p-values для ит.2 в документе не приведены).

## Каннибализация / refunds / reconversion (факт)
Ит.2: trial → charge упал на 42% (32.31%→18.67%, p=0.063), автор сам отмечает нерепрезентативность (21 vs 14 charged trials) и что механика не могла на это повлиять. charge → 14d cancel −60.61% p=0.105 (ns). Отдельного анализа каннибализации веб-продаж/refunds/reconversion — missing.

## Rollout/rollback по документу (решение, формулировка)
Обе итерации закрыты как fail, без раскатки. Ит.1: «no changes… less than 1% of users clicked on practice mode button… Closing the iteration as a fail». Ит.2: «No significant changes… Didn't get the expected increase in subscription sales… Closing the iteration as a fail. In this iteration I will close the series of experiments with the tour update on the web». Warehouse подтверждает: sv=0 у обоих экспериментов, раскатки не было.

## Post-rollout данные
missing — раскатки не было; раздел Post-rollout analysis пуст (шаблонный текст).

## Data issues / ограничения измерения
- Радикальный недобор: ит.1 остановлена через 1 день (~4% плановой выборки), ит.2 через 4 дня (~8%) — ни один денежный p-value не близок к значимости, CI широкие (в документе CI не приведены вовсе, только p-values).
- Ит.1: расхождение exposure — модель строилась на Tab View (~270k/день), фактических members 64,971/арм за день; воронка Practice Mode View 44,574 против 64,971 members — доля увидевших кнопку меньше выборки.
- Ит.1 Forecast vs Fact: контрольные факт-значения (accesses 147/день, charges 101/день) сильно расходятся с плановой базой (188 и 92) — сама базовая модель была неточна.
- Метка эксперимента «#5463» продублирована в блоке итерации 2 (фактический id ит.2 — #5769 по warehouse).
- Опечатки в модельных таблицах (baseline «011%»).
- Sloperator-CI недоступны (эксперименты отсутствуют в `sandbox.ug_monetization_sloperator_ug_exp_results`).

## Черновая классификация по правилам FLOW-562
**no meaningful uplift** (обе итерации; денежная сторона — с элементом inconclusive из-за недобора). Механическая причина нулевого эффекта измерена причинно и надёжно: в ит.1 только 0.7% увидевших кнопку кликнули её (307 из 44,574), в ит.2 до покупки дошли 5 accesses / 2 charges со 130,599 стартов тура (0.0038%) — treatment физически не мог сдвинуть деньги, прогноз +10% accesses не реализован на порядки. При этом сами денежные метрики (ARPU ±13–17%, p≈0.5–0.6) из-за ~4–8% плановой выборки формально inconclusive: широкие интервалы не исключают ни вреда, ни пользы; p>0.05 здесь не доказательство отсутствия эффекта, но воронка доказывает отсутствие заявленного механизма. trial→charge −42% (p=0.063) — не считаем negative: автор корректно указывает на малое N и отсутствие причинной связи с механикой.

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
- Прогнозы +$685/период (ит.1) и +$915/период (ит.2) — EE (модельная экстраполяция, не измерены).
- Факт revenue $1,417 vs $1,651 (ит.1) и $3,839 vs $3,344 (ит.2), ARPU/AOV/ARPPU diffs с p-values — CM, но глубоко недомощнённые (все ns; для вывода о величине эффекта фактически NM-качество).
- Forecast vs Fact таблицы ($1,009/день ит.1; −$738/день ит.2) — OE-подобное сравнение план/факт суточных агрегатов без причинной интерпретации (смешивает обе вариации и базовую неточность модели).
- Post-rollout IR — NM (раскатки не было).
