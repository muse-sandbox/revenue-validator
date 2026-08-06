# HX-07 — ground truth (doc-side)
Источник: 699821637 | [2025-07-01] UG Web: Complete registration offer [2025-09-09] | https://alice.mu.se/pages/viewpage.action?pageId=699821637
Эксперимент(ы): #6344 (Jira: UMN-8927)

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
- Модель A/B на 1533 splash view/вариацию: accesses 56→67 (splash→access 3.65%→4.27%, +20%), charges 31→37, revenue $2121→$2545 (+$424), ARPPU $68 (без изменений), ARPU $1.38→$1.66 (+$0.28).
- Forecast (per day) из раздела результатов: при 1683 Banner Purchase View/день — control 49 accesses / 29 charges / $1859; variation 2 — 67 / 41 / $2688; diff +18 accesses, +12 charges, **+$829/день**.
- Post-rollout комментарий автора: по экспу ожидали «about extra $450 per day» (~+70% ARPU от RegistrationSplash).

## Факт: target metric и денежные метрики
Сегмент Total (UG_WEB), control vs variation 2, 12 дней, members 9108 / 9009 (-1.1%):

- ARPU: $1.1 → $1.6, **+44.6%, p=0.000** (в Decision указано +42%; в Conclusion «~45%»).
- Access CR: 2.18% → 3.03%, **+38.7%, p=0.000** (Decision: +38.69%).
- Charge CR: 1.48% → 2.2%, **+48.3%, p=0.000** (Decision: +48.28%).
- Revenue: $10061 → $14388 (+43%); Charges 157 → 220 (+40%); Buyers 135 → 198 (+47%); Accesses 269 → 360 (+34%); Instants 117 → 180 (+54%).
- AOV +2.05% (p=0.65), ARPPU -2.5% (p=0.56) — не значимо.
- Trials share 56.5% → 50% (-11.5%, p=0.10); Trial→charge 27.6% → 24.4% (-11.5%, p=0.51) — не значимо.

Сегмент Without registration splash: ARPPU $66 → $75.5, **+14.3%, p=0.039** (в Decision: +14.32%); ARPU +26.3% (p=0.08), Access CR +19% (p=0.10) — не значимо.

Воронка Registration splash funnel: members→PURCHASE_SUCCESS 0.61% → 0.84%; Landing Plans View показывается ~100% в тесте (по дизайну — событие шлётся вместе с Banner Purchase View на том же экране, поэтому шаги воронки в тесте не сопоставимы с контролем напрямую).

## Достигнутая выборка и длительность (vs дизайн)
- Дизайн: 20 дней, sample 15330/15330 (в pre-launch таблице дизайна было «Sample size (per variation) 30660» — внутреннее расхождение документа).
- Факт: **12 дней**, 9108 / 9009. Чек «duration of exp ≥ design» помечен **incomplete** (недобор длительности и выборки, ~59% от 15330). A/B баланс соблюдён; видимых багов и внешних эффектов не отмечено.

## Денежные guardrails (факт)
До запуска guardrails не заявлялись. Фактически посчитаны:
- Cancels 14d: 23 → 30 (+30%); Charge→14d cancel: 14.6% → 13.6% (-6.92%, p=0.78).
- Refunds 14d: 6 → 16 (**+170%** по счёту); Charge→14d refund: 3.82% → 7.27% (**+90.3%, p=0.14** — не значимо, но мало наблюдений; в сегменте Without registration splash +141%, p=0.06).
- Retention 1d/7d/14d: без значимых изменений (p=0.23/0.62/0.66).
- Tab View метрики: без значимых изменений.
Вывод документа: «cancellation/refund metrics did not significantly worsen».

## Каннибализация / refunds / reconversion (факт)
- Каннибализация соседних источников напрямую не анализировалась; сегмент «Without registration splash» (покупки не из splash-воронки) тоже вырос (ARPPU +14.3% значимо) — признаков каннибализации в документе нет.
- Refunds — см. выше: номинально сильный рост (6→16), статистически не подтверждён.
- Reconversion — не рассматривалась, missing.

## Rollout/rollback по документу
Conclusion: **Success** (зелёный статус). «Roll outed variation 2». Next steps: смотреть, не затухает ли эффект; QA соц-авторизации (Google/Facebook) в укороченном флоу; follow-up A/B (reviews vs benefits, «ambulance» при закрытии, 24h баннер).

## Post-rollout данные
Таблица «Post-rollout analysis»: daily ARPU от RegistrationSplash — before exp $0.435 (DAU 1544, $674/день); during exp control $0.436, test $0.730 (+67% test vs control; +68% vs before). After rollout: $0.576 (DAU 1579, $908/день) — **+32% vs exp control, ~+$234/день**. Комментарий автора: по экспу ожидали ~70% прироста ARPU и ~+$450/день, фактически после раскатки только ~30% и ~+$230/день (реализовалось примерно вдвое меньше экспериментального эффекта).

## Data issues / ограничения измерения
- Эксперимент остановлен на 12-м дне из 20 по дизайну; выборка ~9.1k/вар против 15.3k по дизайну (чек длительности incomplete) — результат посчитан на недоборе, хотя ключевые p-value 0.000.
- Расхождение внутри документа: sample size в дизайне 30660 «per variation» vs 15330/15330 в Design-vs-Reality.
- Refunds: большой относительный рост при малых счётчиках (6→16), p=0.14 — не разрешено.
- Воронка splash в тесте технически несравнима с контролем (Landing Plans View шлётся вместе с exposure-событием на одном экране).
- Post-rollout сравнение — наблюдательное (before/after + rollout vs exp-control), без CI/p-value; в нём эффект вдвое ниже экспериментального.

## Черновая классификация по правилам FLOW-562
**positive.** Target-метрика splash→access выросла значимо (+38.7%, p=0.000), денежный результат подтверждён: ARPU +44.6% при p=0.000 в основном сегменте, revenue +43%; вариация 2 раскатана со статусом Success. Недобор длительности/выборки и наблюдательный post-rollout (эффект ~+32% ARPU вместо ~+70%) уменьшают величину, но не знак эффекта; guardrails значимо не ухудшились (рост refunds не значим, p=0.14).

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
- ARPU +44.6% (p=0.000), Access CR +38.7%, Charge CR +48.3%, revenue $10061→$14388 (Total, эксперимент) — **CM** (каузально измерено в A/B).
- ARPPU +14.32% (Without registration splash, p=0.039) — **CM**.
- Forecast +$829/день (и pre-launch модель +$424/1533 views) — **EE** (экстраполяция из эксперимента/модели).
- Ожидание «~$450/день» после раскатки — **EE**.
- Post-rollout +32% ARPU / ~+$234/день ($908 vs $674) — **OE** (наблюдательное before/after без стат. теста).
- Рост refunds 14d (+170% по счёту, p=0.14) — измерено в A/B, но не значимо: денежный эффект рефандов на итоговую выручку отдельно не оценён — **NM** как денежная величина.
