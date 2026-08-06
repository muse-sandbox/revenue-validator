# Модель релевантности экспериментов для валидатора (FLOW-574)

Версия V0 для разметки inventory (FLOW-577) и проверки на holdout. Обобщает структуру карточек Interstitials KB (FLOW-567) на весь revenue-корпус; словарь `flow_stage` берётся из Revenue User Flow V0 (FLOW-576), поля выровнены с существующим корпусом `context/hypotheses/` (surface/lever, mechanism, platform, metric, outcome).

---

## 1. Схема данных: координаты эксперимента

Каждый завершённый эксперимент описывается тремя блоками. Блок B — оси релевантности, по ним считается близость; блок A гейтит право эксперимента вообще быть evidence; блок C — то, что переносится.

### Блок A — идентификация и валидность (не оси близости, а фильтр допуска)

| Поле | Значения / формат |
|---|---|
| `exp_id`, `links`, `dates` | id эксперимента, ссылки на Confluence/итоги, период |
| `iteration_of` | id родительской итерации, если это повтор идеи |
| `validity.srm_ok` | да/нет (SRM-проверка активированных рук) |
| `validity.maturity_ok` | да/нет (trial-окно дозрело, pending trials share в норме) |
| `validity.result_class` | significant-positive / significant-negative / powered-null / inconclusive |
| `validity.ci` | доверительный интервал ключевой метрики |
| `plan_fact` | прогноз vs факт (incremental revenue) |
| `decision` | rolled-out / killed / inconclusive-stopped |

Эксперимент с `srm_ok = нет` или `result_class = inconclusive` не может быть основанием продуктового вывода ни на каком уровне близости — только источником measurement-уроков («как не надо мерить»).

### Блок B — десять осей релевантности

| # | Ось | Что фиксирует | Словарь / формат |
|---|---|---|---|
| B1 | `flow_stage` | этап Revenue User Flow, где вмешивается treatment | enum из FLOW-576: action → eligibility → surface → exposure → paywall → trial/purchase → charge → renewal/cancel/refund → net revenue |
| B2 | `segment` | кто под воздействием | монетизационное состояние (free-new / free-existing / ex-paid / winback / trial / paying) + платформа (iOS / Android / Web) + тип трафика (paid / organic / referral) + geo, если гейтится |
| B3 | `trigger_eligibility` | что именно помещает пользователя под воздействие | событие-триггер (Tour End, App Start, N-й tab view, …), timing / frequency caps, админ-гейты (версия, страна, локаль) |
| B4 | `surface` | где показано | interstitial, tour/onboarding, tab-page paywall, banner, search, settings, email, web landing, checkout, … |
| B5 | `mechanism` | тип вмешательства | price, offer-structure (trial length, intro, instant offer, bundle), new-surface, copy/design, frequency/timing, gating/entitlement, checkout-UX, … |
| B6 | `offer` | продукт и условия | Pro / Pro+ / OTP / songbook; SKU, trial length, price point, billing period |
| B7 | `behavior` | какое поведение механизм предполагает изменить | одна фраза «изменение X → поведение Y» (снизить friction на paywall → больше trial starts) |
| B8 | `metric` | primary + proxy | канонические имена из `metrics.yaml` (trial → charge %, trial → any charge %, buyers, ARPU, …) |
| B9 | `money_chain` | через какое звено идёт денежный эффект и на каком горизонте | звено exposure → paywall → trial → charge → renewal; горизонт D0/D7/D30/LTV; всегда net revenue |
| B10 | `guardrails` | что защищали | retention, engagement (tab views), refunds/cancellations, pending trials share, support load |

### Блок C — результат и урок (то, что переносится)

| Поле | Содержание |
|---|---|
| `outcome` | фактический результат с CI и значимостью |
| `lesson` | подтверждённый продуктовый вывод, 1–2 фразы, с источником |
| `transfer_bounds` | где lesson применим и где нет (сегменты, платформы, условия) |
| `fact_vs_interpretation` | явная пометка: что — измеренный факт, что — интерпретация автора |

---

## 2. Совпадение по оси

Для каждой оси B сравнение нового кейса с историческим даёт одно из трёх значений:

- **exact** — то же значение словаря;
- **adjacent** — соседнее значение той же группы (другой interstitial-триггер; free-new vs free-existing; iOS vs Android при одинаковой механике биллинга);
- **different** — другая группа (free vs ex-paid; paywall vs email; price vs copy).

Платформенная оговорка: iOS vs Android — adjacent, но становится different, если механизм завязан на платформенную специфику (instant offer как same-subscription plan switch на iOS, комиссии, review-процесс).

---

## 3. Уровни близости

### L1 — прямой аналог
`mechanism` exact **и** `flow_stage` exact **и** (`surface` exact или adjacent) **и** `segment` совпадает по монетизационному состоянию **и** `money_chain` — то же звено.
→ Переносится **продуктовый вывод directionally** (знак и механизм). Величина эффекта не переносится никогда.

### L2 — частичный аналог
Одно из: `mechanism` exact при different `surface`/`flow_stage`; **или** `surface`+`flow_stage` exact при different `mechanism`; **или** выполнены условия L1, но `segment`/платформа different.
→ Переносится как **гипотеза или предупреждение** + prior на порядок эффекта для sizing. Не основание для решения launch/deprioritize сам по себе.

### L3 — слабый evidence
Совпадение только по `metric`, только по `segment` или только по `surface` без `mechanism`.
→ Только для **sizing, measurement и guardrails**: baseline, дисперсия, MDE, длительность, зрелость trial-окна, типовые guardrail-провалы. Продуктовый вывод не переносится.

Совпадение по `metric` (B8) **не повышает уровень**: уровень определяется механизмом и контекстом (B1–B5), метрика лишь подтверждает, что сравнимо измерено.

---

## 4. Обязательный минимум для переноса продуктового вывода

Все условия одновременно:

1. `mechanism` exact;
2. `flow_stage` exact;
3. `surface` **или** `trigger_eligibility` exact/adjacent;
4. сегменты сопоставимы по монетизационному состоянию — вывод с free-аудитории не переносится на ex-paid/winback и наоборот;
5. то же звено `money_chain` (эффект на trial starts ≠ эффект на trial → charge);
6. блок A валиден: `srm_ok`, `maturity_ok`, и `result_class` — significant либо powered-null (для вывода «не работает» нужен именно powered-null, а не inconclusive).

Переносим всегда только **знак и механизм**. Величина эффекта, baseline и конверсия из прошлого эксперимента — только как prior для sizing с явной пометкой.

---

## 5. Когда совпадения по метрике недостаточно

Всегда — для продуктового вывода. Метрика — исход, а не причина: та же trial → charge % двигается ценой, длиной триала, копирайтом paywall и частотой interstitials, и это разные продуктовые уроки на разных этапах flow. Metric-only-совпадение легально используется только для: baseline и дисперсии под MDE, оценки длительности и зрелости, выбора guardrails и известных ловушек измерения (pending trials, instant offer day-0 charge, web intro two-leg merge).

---

## 6. Формат объяснения релевантности (карточка на каждый найденный аналог)

```
analog:
  exp_id + ссылка + даты + validity-флаги
  level: L1 | L2 | L3
  matched: [ось: exact/adjacent — почему]
  mismatched: [ось: different — и чем это грозит переносу]
  transferable: что именно переносим (факт из outcome, directionally, со ссылкой)
  not_transferable: ≥1 пункт обязательно; величина эффекта — всегда здесь;
                    плюс всё, что за пределами transfer_bounds исходного кейса
  conflict: если противоречит другому найденному аналогу — с кем и в чём
```

Карточка без заполненного `not_transferable` считается невалидной: у любого аналога есть границы переноса.

---

## 7. Правила ранжирования evidence

1. **Hard filter:** отбросить всё, что не проходит блок A (кроме использования в measurement-уроках).
2. **Группировка по уровню:** L1 > L2 > L3.
3. **Внутри уровня** сортировать по: (a) числу exact-осей из B1–B7; (b) сегментной близости; (c) свежести (продукт и цены меняются — эксперимент 3-летней давности слабее прошлогоднего при прочих равных); (d) точности результата (узкий CI выше широкого).
4. **Противоречащие аналоги:** выигрывает более близкий по координатам; при сравнимой близости — конфликт репортится явно (оба кейса, обе даты, гипотеза о причине расхождения), а не усредняется и не замалчивается.
5. **Пустой результат:** если L1/L2 не найдено — валидатор обязан сказать «прямых аналогов нет», а не подтягивать L3 до статуса аналога.

---

## 8. Проверка на holdout (как выполняется DoD)

1. Разметить inventory по схеме блоков A–C (FLOW-577).
2. Для каждого holdout-кейса: человек независимо помечает известные ему прямые аналоги; retrieval по модели должен (a) поставить их в топ ранжирования, (b) не породить ни одного ложного L1 (precision L1 = 1.0 — приоритетнее полноты).
3. Перенос: для каждого L1-аналога сравнить перенесённый directional-вывод со знаком фактического исхода holdout-кейса; расхождения разбирать — чаще всего это сигнал, что ось, по которой кейсы различались, должна быть обязательной.
4. Метрики проверки: precision/recall по уровням, доля карточек с непустым и содержательным `not_transferable`, число незадекларированных конфликтов.

---

## Зависимости и стыковки

- **FLOW-576:** словарь `flow_stage` (B1) и звенья `money_chain` (B9) финализируются картой Revenue User Flow V0; до неё использовать черновой enum из этой схемы.
- **FLOW-577:** разметка inventory ведётся ровно по блокам A–C; существующий корпус `context/hypotheses/` уже покрывает часть полей (surface/lever → B4/B5, mechanism → B5/B7, platform → B2, metric → B8, outcome → C), остальное дозаполняется.
- **FLOW-580:** уровни L1–L3 и обязательный минимум (§4) — вход для evidence policy: какие уровни могут менять решение, какие — только предупреждать.
