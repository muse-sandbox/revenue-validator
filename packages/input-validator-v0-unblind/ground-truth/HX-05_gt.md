# HX-05 — ground truth (doc-side)
Источник: 670205164 | [2025-01-29] UG Web: short PDF download funnel [2025-08-20] | https://alice.mu.se/pages/viewpage.action?pageId=670205164
Эксперимент(ы): #5996 (Iteration 1), #6068 (Iteration 2). Jira: UMN-7626.

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
Ожидание: ARPU $0,096 → $0,115 (B, +20%, +$0,02) / $0,117 (C, +25%, +$0,021); Revenue $2 460 → $2 952 (B, +$492) / $2 980 (C, +$520) на когорту 25 463 tab views; Access 51 → 61/64; Charges 30 → 36/37; ARPPU $82 без изменений. Дизайн: 272 909/вариацию, 21 день, power 0.8, alpha 0.05.

## Факт: target metric и денежные метрики
**Iteration 1 (#5996), 3 вариации (control / var2=B / var3=C):**
- Members: 42 788 / 42 421 / 42 691.
- ARPU: control $0,223; var2 $0,177 (−20,5%, p=0,16); var3 $0,257 (+15,4%, p=0,34).
- Revenue: $9 532 / $7 511 (−21%) / $10 971 (+15%). Charges: 117 / 95 (−19%) / 139 (+19%). Accesses: 217 / 197 (−9,2%) / 203 (−6,5%).
- Access cr: 0,372% / 0,335% (−9,92%, p=0,36) / 0,382% (+2,75%, p=0,81). Charge cr: 0,222% / 0,191% (−14%, p=0,32) / 0,276% (+24,5%, p=0,11).
- AOV: $81,5 / $79,1 (p=0,76) / $78,9 (p=0,69); ARPPU: $100 / $92,7 (p=0,36) / $93 (p=0,33).
- Ни одна метрика не значима (все p > 0,05).

**Iteration 2 (#6068), control / var2 (= бывшая C):**
- Members: 10 974 / 11 085.
- ARPU: control $0,247; var2 $0,0787 (−68,1%, p=0,002).
- Revenue: $2 709 / $872 (−68%). Charges: 31 / 11 (−65%). Accesses: 52 / 20 (−62%).
- Access cr: 0,328% / 0,153% (−53,3%, p=0,008). Charge cr: 0,219% / 0,0902% (−58,8%, p=0,015).
- AOV: $87,4 / $79,3 (p=0,65); ARPPU: $113 / $87,3 (p=0,29).

## Достигнутая выборка и длительность (vs дизайн)
- Iteration 1: 7 дней вместо 21; ~42,4–42,8 тыс./вариацию вместо 272 909 (~16% дизайна). Чек «duration ≥ design» — incomplete; A/B balance — complete; багов и внешних эффектов не отмечено.
- Iteration 2: 3 дня вместо 21; ~11 тыс./вариацию вместо 272 909 (~4% дизайна). Чек «duration ≥ design» — incomplete; A/B balance — complete.

## Денежные guardrails (факт)
Pre-launch guardrails не заявлялись; фактически посчитаны: Iteration 1 — Cancels 14d: 21 / 22 (+4,8%) / 23 (+9,5%); Refunds 14d: 8 / 12 (+50%) / 8 (0%); Charge→14d cancel: 17,9% / 23,2% (p=0,35) / 16,5% (p=0,77); Charge→14d refund: 6,84% / 12,6% (p=0,16) / 5,76% (p=0,72). Retention 1/7/14d — без значимых отличий. Iteration 2 — Cancels/Refunds 14d в var2: 0 против 10/8 в контроле (−100%, p=0,000/0,001 — следствие обвала покупок); Retention без значимых отличий (p≥0,18).

## Каннибализация / refunds / reconversion (факт)
Каннибализация и reconversion отдельно не анализировались (`missing`). Refunds — см. guardrails выше; в Iteration 1 var2 рефанды выросли на 50% (8→12, p=0,16, незначимо).

## Rollout/rollback по документу (решение, формулировка)
Iteration 1: Conclusion — **Fail** («no any changes»; «increased print landings in variation #3 but it didn't affect conversion to access and arpu»; «could be better in variation #3 but due to short period we didn't get enough data»). Next steps: запуск Iteration 2 с теми же изменениями, но без худшей вариации #2.
Iteration 2: Conclusion — **Fail** («Severely underperformed in terms of access and bottom line revenue»; «the result does not coincide with the results of the first iteration, perhaps the experiment was not held enough»). «Decided not to roll out test variation». «Generally at the time of the results we changed their approach to selling from print and pdf sources». «Closing the project as fail».

## Post-rollout данные
`missing` — раскатки не было; раздел Post-rollout analysis пуст (шаблонный плейсхолдер).

## Data issues / ограничения измерения
- Оба запуска сильно недобрали и по длительности (7/21 и 3/21 дней), и по выборке (16% и 4% от дизайна) — эксперимент никогда не был близок к задуманной мощности.
- Противоречие итераций: var3(C) в Iteration 1 показывала +15% ARPU (p=0,34), та же механика в Iteration 2 дала −68% (p=0,002) на выборке втрое меньше — сами авторы пишут «perhaps the experiment was not held enough».
- «Forecast (per day)» посчитан из фактов эксперимента (Iteration 1: var2 −$1 164/день, var3 +$872/день; Iteration 2: var2 −$4 283/день) — экстраполяция с незрелых коротких данных.
- Аномалии воронок Print landing: plans > landing в ряде строк (125%, 126%, 97%), т.е. шаги воронки несопоставимы между вариациями (в C-флоу лендинга как шага нет); Export2pdfCopy var3 — 33 277 members против ~2,3–2,5 тыс. в контроле (в C пейволл вешается на попытку копирования, экспозиция источника несопоставима). Сравнивать по источникам можно только с оговорками.
- Значимые p-values Iteration 2 (−100% cancels/refunds p≈0) — артефакт почти нулевых покупок в var2, не самостоятельный сигнал.

## Черновая классификация по правилам FLOW-562
**negative** (по совокупности с оговоркой). Iteration 2 дала статистически значимое падение денежных метрик (ARPU −68,1%, p=0,002; access cr p=0,008; charge cr p=0,015), решение — не раскатывать, проект закрыт как fail. Однако обе итерации драматически недобрали дизайн (3–7 дней вместо 21, 4–16% выборки), а Iteration 1 для той же механики была незначимо положительной (+15,4% ARPU, p=0,34) — поэтому отдельно взятая Iteration 1 классифицируется как **inconclusive** (широкие интервалы, недобор), и итоговое «negative» опирается в основном на короткую Iteration 2 плюс решение авторов.

## Тип результата: CM / EE / OE / NM (по каждому денежному числу)
(легенда предположена: CM = прямое чистое измерение; EE = экстраполяция/оценка из измерения; OE = мнение/модель автора до запуска; NM = не измерено)
- Iteration 1 Revenue $9 532 / $7 511 / $10 971, ARPU $0,223 / $0,177 / $0,257, ARPPU, AOV — **CM** (калькуляторный замер по когорте эксперимента, но незрелый: 7 дней).
- Iteration 2 Revenue $2 709 / $872, ARPU $0,247 / $0,0787 — **CM** (замер, 3 дня, крайне незрелый).
- Forecast (per day): −$1 164 и +$872 (It1), −$4 283 (It2) — **EE** (экстраполяция факта на день).
- Pre-launch ожидания +$492 / +$520, ~$495 от удаления тура, «+5%» для C — **OE** (авторская модель/допущение до запуска).
- Post-rollout деньги — **NM** (раскатки не было).
