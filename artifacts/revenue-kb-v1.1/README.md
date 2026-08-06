# Revenue Knowledge Base / Validator V1.1 (FLOW-586)

Бандл KB + Validator V1.1 для regression-прогона A/B по pre-registered
протоколу `../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md` (frozen, пороги
не менялись). Собран после формального NO blind A/B теста FLOW-579: гейт §6
провалился по единственному условию — один формальный unsupported transfer
типа «инфляция уровня близости» (заявленный в analog-карточке уровень выше
уровня, детерминированно следующего из осей той же карточки). Текст и
конкретика holdout-кейсов builder'у V1.1 не передавались; фикс generic и
применяется ко всем analog-карточкам одинаково.

Дата freeze: **2026-08-05**. Старые бандлы (`../revenue-kb-v1/`,
`../revenue-evidence-policy-v1/`) НЕ редактировались ни байтом — их хеши
сверены с их FREEZE/BUNDLE-манифестами перед сборкой и после неё.

## Отличия V1.1 от V1 (все — generic, ни одно не таргетирует конкретный кейс)

1. **Level больше не назначается моделью.** KB §2.2 — детерминированная
   формализация правил L1/L2/L3 из `evidence_policy_rules.yaml`
   `level_computation` в терминах полей карточки; уровень вычисляется из
   осей и проверяется машинным линтером; расхождение = невалидный ответ.
2. **Строгий машинопарсируемый формат analog-карточки** (KB §2.4): YAML-блок
   в ```-фенсе с обязательными полями `source`, все 10 осей
   (exact/adjacent/different), `segment_monetization_state`,
   `money_chain_link`, `platform`, `level`, `transferable`, непустой
   `not_transferable`; опциональные `sizing_prior` (с меткой prior) и
   `conflict`; маркировка fact/interpretation/hypothesis сохранена.
3. **`linter.py`** — детерминированный машинный линтер (stdlib-only, без
   сети/времени/рандома): пересчёт уровня, hard errors по Evidence Policy V1
   (level mismatch, пустой `not_transferable`, несуществующий source ID,
   непарсируемая карточка, отсутствие `no direct analogs` при пустых L1/L2,
   отсутствие секции side-effects; в `--no-kb-arm` — запрет эмиссии
   карточек).
4. **Промпт V1.1** (`validator_prompt_v1_1.md`): требования строгого формата
   и самостоятельного вычисления уровня по формуле (с предупреждением о
   машинной проверке); L3 — только явно помеченный слабый сигнал
   (guardrails/measurement/sizing), никогда не direct analog и не
   самостоятельное основание менять вердикт; обязательная строка
   `no direct analogs` при пустых L1/L2; явное «нет обязанности находить
   аналог»; обязательная секция `## Non-monetization effects to instrument`
   (retention/refunds/engagement/upper-funnel в обе стороны + что
   инструментировать + stop-rules) в обоих плечах.
5. **Evidence Policy V1 включена в бандл** байт-в-байт
   (`evidence_policy.md`, `evidence_policy_rules.yaml`) как нормативный
   источник формализации.

Корпус (§4), индексы (§3) и `pattern_cards.md` — без изменений
(pattern_cards.md байт-идентичен V1, хеш совпадает).

## Состав

| Файл | Что это |
|---|---|
| `knowledge_base.md` | V1.1: корпус и индексы V1 + переработанный §2 (детерминированная модель близости, строгий формат карточки §2.4) |
| `pattern_cards.md` | Байт-в-байт копия V1 |
| `validator_prompt_v1_1.md` | Frozen combined validator prompt V1.1 — один текст для обоих плеч; плейсхолдеры `{EXPERIMENT_CARD}` / `{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` в синтаксисе V1 |
| `evidence_policy.md`, `evidence_policy_rules.yaml` | Байт-в-байт копии frozen Evidence Policy V1 |
| `linter.py` | Детерминированный машинный линтер ответов |
| `linter_selftest.py`, `selftest_fixtures/` | Selftest (25 тестов) на синтетических фикстурах (источники T9-0x/P-90 выдуманы; ни одна фикстура не из RH-кейсов) |
| `FREEZE_MANIFEST.md` | SHA-256 всех файлов, хеш и размер KNOWLEDGE_CONTEXT, правило заморозки |

**KNOWLEDGE CONTEXT плеча B** = `knowledge_base.md` + `\n\n---\n\n` +
`pattern_cards.md` (байтово; хеш в `FREEZE_MANIFEST.md`). Механика прогона —
как в `../revenue-kb-ab-run/run_manifest.md`: в плече B `{KNOWLEDGE_CONTEXT}`
подставляется, в плече A блок `<knowledge-context>…</knowledge-context>`
удаляется целиком.

## Как запускать линтер

```
python3 linter.py <answer.md> --kb knowledge_base.md \
    --patterns pattern_cards.md            # плечо B (KB)
python3 linter.py <answer.md> --kb knowledge_base.md \
    --patterns pattern_cards.md --no-kb-arm  # плечо A (без KB)
```

Exit 0 = PASS, 1 = FAIL (ответ невалиден), 2 = ошибка ввода. JSON-отчёт в
stdout (карточки, claimed/computed levels, errors, verdict); полный текст
ответа линтер не печатает. Selftest: `python3 linter_selftest.py` (запускался
дважды, вывод байт-идентичен).

## Формализованные правила уровней (кратко; полностью — KB §2.2)

- **L1**: mechanism exact ∧ flow_stage exact ∧ surface ∈ {exact, adjacent} ∧
  segment_monetization_state exact ∧ money_chain_link exact ∧
  platform ≠ different.
- **L2** (не L1, любая ветка): (A) mechanism exact ∧ (surface different ∨
  flow_stage different); (B) surface exact ∧ flow_stage exact ∧ mechanism
  different; (C) mechanism exact ∧ flow_stage exact ∧ surface ∈ {exact,
  adjacent} ∧ money_chain_link exact ∧ (segment_monetization_state different
  ∨ segment different ∨ platform different).
- **L3**: всё остальное. Совпадение метрики уровень никогда не повышает.
- Разрешения неоднозначностей R1–R5 задокументированы в KB §2.2 (все — в
  сторону более низкого уровня).

## Freeze

После freeze файлы бандла не меняются; любое изменение = V1.2 с новым
манифестом и новым прогоном протокола. Хеши — в `FREEZE_MANIFEST.md`.
