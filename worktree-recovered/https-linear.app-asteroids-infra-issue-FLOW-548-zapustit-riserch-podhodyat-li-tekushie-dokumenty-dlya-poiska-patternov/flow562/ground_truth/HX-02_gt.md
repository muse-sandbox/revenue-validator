# HX-02 — ground truth (doc-side)
Источник: 522531558 | [2024-08-05] UG WEB: revenue retention — non-removable subscription expiration banner [2024-XX-XX] | https://alice.mu.se/pages/viewpage.action?pageId=522531558
Эксперимент(ы): #5202 (Iteration #1). Jira epic: UMN-6211.

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
Гипотеза: «additional $X in revenue» — placeholder, не заполнен. Числовая модель: A 566 юзеров → 5 реактиваций (0.88%), $265, ARPU $0.47; B 566 → 31 реактивация (5%), $1293, ARPU $2.05; diff +$1028 / +$1.58 ARPU. Дизайн: MDE 0.2636, power 0.8, alpha 0.05, sample 566 (все вариации), duration 1 день.

## Факт: target metric и денежные метрики (значения A/B, uplift, p-value/CI — как в документе)
Monetization stats (control / variation 2):
- members: 486 / 499; subscribers 55 / 42; accesses 55 / 42; instants 52 / 39; trials 3 / 3; charged trials 1 / 2; buyers 53 / 42; charges 53 / 42; recurrent charges 16 / 12; revenue $3580 / $2657; 14d cancels 6 / 2; 14d refunds 0 / 1; disputes 0 / 0.
Monetization metrics (control / variation 2 / diff / p-value):
- ARPU $7.37 / $5.32 / −27.73% / p=0.023 (значимо, отрицательно)
- ARPPU $43.40 / $43.73 / +0.75% / p=0.96
- access CR 11.32% / 8.42% / −25.63% / p=0.13
- charge CR 10.91% / 8.42% / −22.82% / p=0.19
- charge → 14d cancel 11.32% / 4.76% / −57.94% / p=0.23
Resubscription funnel: control 486 members, 0 resubscriptions, 16 recurrent charges, members→charges 3.3%, recurrent revenue $1280, recurrent ARPU $2.63; variation #2 499 members, 39 resubscriptions (7.8%), 12 recurrent charges (resubscriptions→charges 31%, members→charges 2.4%), recurrent revenue $856 (−27%… доля в таблице), recurrent ARPU $1.72 (в diff-строке документа: −27% / −35%).
Decision-раздел: «8% conversion to successful resubscribe», но «yet hadn't increase recurrent charges»; лишь 30% ресабскрайберов реально прошли charge в billing date, у большинства остальных транзакции отклонены (PROCESSOR_DECLINED); «earned even less from them».
Product/SEO: retention 1d −9.65% (p=0.30), retention 7d −8.46% (p=0.12), long-tab members −1.50% (p=0.70), pageview/session +10.31% (p=0.010).

## Достигнутая выборка и длительность (vs дизайн)
Дизайн: 1 день, 283+283. Факт: 37 дней, 486/499 members (по значимости) или 891 members в bad-split таблице. Документ: «very few users. got less than 1k for 1+ month. while expected to get this amount in a few days» — набор аудитории радикально медленнее плана.

## Денежные guardrails (факт)
Заранее guardrails не заявлялись (missing в дизайне). Фактически измерены: revenue −$923 abs (3580→2657), ARPU −27.73% p=0.023, recurrent revenue −27% ($1280→$856), recurrent charges 16→12 (−35% по ARPU-строке), 14d refunds 0→1.

## Каннибализация / refunds / reconversion (факт)
Каннибализация отдельно не анализировалась (missing). Refunds 14d: 0 (control) / 1 (variation). Reconversion — суть эксперимента: 39 ресабскрипшенов в вариации, но только ~30% (12) дошли до реального charge; остальные — PROCESSOR_DECLINED. То есть реактивации не сконвертировались в деньги.

## Rollout/rollback по документу (решение, формулировка)
Conclusions: «can't rollout this test variation» — вариация не раскатана. Next steps: разобраться с малым sample size; предлагать пользователям обновить карту после ресабскрайба. Есть раздел Project Termination Stage (удалить код по коммитам, удалить таблицу forum.service_access_short) — проект сворачивается.

## Post-rollout данные
missing — раздел «Post-rollout analysis (optional)» пуст («..»), раскатки не было.

## Data issues / ограничения измерения
- Bad split: из 891 members у 40 (4.49%) — обе вариации одновременно («bad split routine»).
- Критический недобор: <1k users за 1+ месяц против плановых 566 за ~1 день; тест шёл 37 дней вместо 1.
- Дизайновая цель по выборке в Results-таблице (283/283) не совпадает с pre-launch sample 566 total — фактические 486/499 формально больше 283/283, чек «duration >= design» и «A/B balance maintained» помечены complete, но плановая скорость набора не достигнута.
- Биллинговый шум: большинство ресабскрайб-транзакций отклонены процессингом (PROCESSOR_DECLINED) — измеренная revenue занижает «поведенческий» эффект, но это и есть реальные деньги.
- ARPU-эффект (p=0.023) включает всю монетизацию когорты (accesses/instants), не только ресабскрайб-воронку; access CR сам по себе не значим (p=0.13).

## Черновая классификация по правилам FLOW-562
**negative.** Поведенческая цель достигнута (7.8% ресабскрипшенов против 0% в контроле), но денежный итог отрицательный: ARPU −27.73% при p=0.023, recurrent revenue −27%, recurrent charges ниже контроля, и документ фиксирует «earned even less from them» и «can't rollout». Оговорка: bad split 4.49% и сильный недобор аудитории подрывают чистоту измерения, поэтому величина негативного эффекта ненадёжна — но направление решения и значимый минус по ARPU дают «negative», а не «inconclusive».

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
- Revenue $3580 / $2657 (значимость-таблица) — CM (фактические charges когорты)
- Recurrent revenue $1280 / $856, recurrent ARPU $2.63 / $1.72 — CM
- ARPU $7.37 / $5.32, ARPPU $43.40 / $43.73 — CM (производные от фактических денег)
- Forecast (per day): var1 — 283 starts, 32 accesses, 31 charges, 9 recurrent, $2085; var2 — 283, 24, 24, 7, $1507; diff −8 accesses, −7 charges, +2 recurrent (как в документе), −$578 — EE (модельный прогноз per day, не факт)
- Pre-launch модель ($265 / $1293 / +$1028) — EE (forecast-model)
- «additional $X» из гипотезы — NM (placeholder, не заполнен)
