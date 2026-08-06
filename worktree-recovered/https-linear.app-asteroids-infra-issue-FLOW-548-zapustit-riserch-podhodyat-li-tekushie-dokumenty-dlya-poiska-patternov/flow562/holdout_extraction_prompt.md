# Шаблон промпта извлечения holdout (FLOW-562)

Ты — read-only исследователь документа эксперимента UG в Confluence. НИЧЕГО не изменяй в Confluence. Аутентификация в `.env`.

## Шаг A. Скачай снапшот

```bash
.venv/bin/python .claude/confluence/confluence_page.py fetch <PAGE_ID> --out-dir output/flow562/pages/<PAGE_ID>
```

Прочитай `output/flow562/pages/<PAGE_ID>/confluence_<PAGE_ID>.txt` целиком.

## Шаг B. Файл 1 — BLINDED pre-launch карточка → `output/flow562/prelaunch_pack/<NEUTRAL_ID>.md`

Назначение: карточку будет читать «валидатор», который НЕ должен узнать исход эксперимента. Правила блайндинга (СТРОГО):

- В карточке НЕТ: pageId, URL, названия страницы, Jira-ключей, номеров экспериментов (#NNNN), дат из заголовка.
- В карточке НЕТ ничего из разделов Results / Decision / Conclusion / Forecast (per day) / Significance analysis / Post-rollout / Next steps, никаких фактических метрик, rollout/rollback, статусов (SUCCESS/FAIL), insights после запуска.
- НЕ исправляй и не улучшай прогноз задним числом. Отсутствующее → `missing`. Шаблонные плейсхолдеры (например «N%») передавай как есть с пометкой `placeholder`.
- Если формулировка pre-launch раздела прямо раскрывает исход (редко, например «UPD. Since we rollout…») — замени на `[REDACTED: post-launch вставка]`.

Структура карточки (пиши по-русски, цифры как в документе):

```
# <NEUTRAL_ID> — pre-launch карточка
(без идентификаторов источника)

## Контекст и цель
## Предлагаемое изменение (что именно меняем, для кого, где)
## Аудитория / платформа / сценарий
## Baseline
## Reach
## Денежная модель (цепочка поведение→деньги, все коэффициенты)
## Ожидаемая incremental revenue и горизонт
## Допущения и их коэффициенты (каждое с типом: observed fact / assumption / forecast-model / author opinion)
## Evidence, доступный до запуска (замеры, прошлые эксперименты — описательно, без ссылок-идентификаторов)
## Target metric
## Guardrail metrics (заявленные до запуска; иначе missing)
## Дизайн: MDE / power / alpha / sample size / duration
## Сегменты
## Риски (каннибализация / refunds / reconversion / LTV — если упомянуты; иначе missing)
## План rollout и stop-rules (если зафиксированы; иначе missing)
```

## Шаг C. Файл 2 — ground truth из документа → `output/flow562/ground_truth/<NEUTRAL_ID>_gt.md`

Отдельный файл, сюда — ВСЁ про результат:

```
# <NEUTRAL_ID> — ground truth (doc-side)
Источник: <PAGE_ID> | <название> | URL
Эксперимент(ы): #NNNN если указаны на странице

## Прогноз IR (повтор из pre-launch, для сверки plan/fact)
## Факт: target metric и денежные метрики (значения A/B, uplift, p-value/CI — как в документе)
## Достигнутая выборка и длительность (vs дизайн)
## Денежные guardrails (факт)
## Каннибализация / refunds / reconversion (факт)
## Rollout/rollback по документу (решение, формулировка)
## Post-rollout данные (если есть; иначе missing)
## Data issues / ограничения измерения (недоборы, SRM, сломанный трекинг, модельные «деньги»)
## Черновая классификация по правилам FLOW-562 (positive / negative / no meaningful uplift / inconclusive / not measurable) с обоснованием в 2–3 предложениях. p>0.05 сам по себе НЕ означает «нет эффекта»: при широком CI — inconclusive.
## Тип результата: CM / EE / OE / NM (по каждому денежному числу, не смешивать)
```

## Шаг D. Финальный текст — компактная выжимка (8–12 строк): категория-черновик, ключевые числа plan vs fact, experiment id (#NNNN), заметные проблемы данных. Подтверди, что в blinded-карточку не попали идентификаторы и результаты.
