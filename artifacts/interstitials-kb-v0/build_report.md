# Build Report — Interstitials KB V0 (FLOW-569)

Дата сборки: 2026-08-04. Задача: FLOW-569 «[CLEAN BUILDER] Собрать и заморозить Interstitials Knowledge Base V0». Это development/build stage: holdout не читался, A/B не запускался, ground truth не открывался.

## Использованные входы (полный список)

1. Корпус `…/outputs/interstitials-corpus-prep/`: прочитаны ТОЛЬКО `README.md`, `BUNDLE_MANIFEST.md` и шесть карточек `knowledge-sources/KS-01…KS-06`. SHA-256 карточек сверены с `BUNDLE_MANIFEST.md` корпуса (перечислены в `source_traceability.md`).
2. Frozen numeric Validator V0 `…/outputs/flow546-clean-input/validator-v0/`: `validator_v0_prompt.md`, `validator_v0_spec.md`, `validator_v0_criteria.md`, `validator_v0_freeze.md` (V0 frozen 2026-08-03).

## Clean-room декларация

- `holdout-blind/` и `ground-truth-sealed/` НЕ открывались (видны только имена файлов в листинге директории и хэши в BUNDLE_MANIFEST — содержимое не читалось).
- `safe_inventory.md`, `corpus_eligibility.md`, `split_manifest.md/.json`, `EXCLUSION_MANIFEST.md`, `LEAKAGE_CHECK.md` НЕ открывались.
- Confluence, Linear (кроме текста самой задачи FLOW-569), Jira, Slack, интернет и локальное зеркало гипотез (`context/hypotheses/`) / реестр `ab_experiment` для Interstitials-контента НЕ использовались.
- Никакие Interstitials-источники вне шести карточек KS-01…KS-06 не использовались.
- Запрещённый материал в контексте сессии не открывался; сессия начата с чистого контекста задачи.

## Что построено

| Артефакт | Содержание |
|---|---|
| `knowledge_base.md` | Правила использования, реестр 6 кейсов, индекс 15 lessons, противоречия, ограничения |
| `pattern_cards.md` | 12 паттернов IKB-P01…P12 + 3 одиночных наблюдения IKB-S01…S03, каждый с полями pattern_id / механика / сегмент / trigger-placement-timing-frequency / механизм / наблюдения / outcome / решение / применимость / границы переноса / источники / confidence |
| `source_traceability.md` | Маппинг карточка→эксперименты, паттерн→источники→факты, проверка правил построения |
| `product_review_prompt.md` | Проход 3 (product review) — единый для A и B |
| `combined_validator_prompt.md` | Сборка входа + ДОСЛОВНЫЙ frozen Validator V0 prompt (sha256 сверен: `61b2ee46…`) + дословный проход 3; программно проверено побайтовое совпадение обеих встроенных частей с источниками |
| `EVALUATION_PROTOCOL.md` | Pre-registered протокол: B vs A, 4 кейса IH-01…IH-04, blind pairwise, критерии C1–C7, правила false blocker, условия YES, лимит ≤10 мин/кейс |
| `FREEZE_MANIFEST.md` | SHA-256 всех файлов бандла |

## Ключевые решения сборки

1. **12 паттернов, а не больше:** требование «короткой» базы; близкие наблюдения слиты (например, каннибализация ad-выручки и соседних paywall-входов — один паттерн IKB-P02), одиночные наблюдения вынесены в отдельный блок с запретом полного переноса.
2. **Мульти-source правило:** каждый IKB-P-паттерн опирается минимум на 2 карточки KS; единственные одно-карточные выводы помечены `single-case evidence` (IKB-P05, IKB-S01…S03, intro-сторона IKB-P08, величины IKB-P10).
3. **Противоречия сохранены:** retention при daily replacement (KS-04-iter2 минус vs KS-06-iter1 плюс vs KS-06-iter2 ноль) оформлено паттерном IKB-P12 с явным запретом выбирать удобную сторону; также сохранены противоречия «значимый ARPU-лифт ≠ rollout» и «engagement вверх / длинные просмотры вниз».
4. **Разметка статусов:** [факт] / [интерпретация] / [гипотеза переноса] проставлены внутри карточек; причинность не заявляется сверх A/B-контрастов с приведённой значимостью.
5. **A/B-инвариант промпта:** product-review-проход добавлен как проход 3 после двух проходов frozen Validator V0; текст промпта один для обоих плеч, разница только во входе (наличие KNOWLEDGE CONTEXT); при отсутствии контекста прописан обязательный отказ от исторических аналогов (анти-галлюцинационное правило).
6. **Validator V0 не изменён:** его прохождения 1–2 включены дословно (побайтовая проверка), проход 3 не переопределяет их правила.

## Ограничения

- База покрывает одну продуктовую линию (mobile interstitials monetization, UG App, 2024–2026); переносимость на другие поверхности — только на уровне механизмов, числа не переносимы.
- Intro-price-результат (KS-06 iter2) и Android-rollout (KS-04 iter2) не имеют долгосрочного follow-up внутри корпуса; next-year recurrence intro-когорты неизвестен.
- Известные дата-проблемы корпуса зафиксированы в базе (unified_id bug, Charge-without-Subscription, расхождение exposure-единиц).
- KS-02 и KS-06 — одна проектная линия на разных страницах: паттерны, опирающиеся только на эту пару, отмечены в traceability.
- Протокол оценивает пользу KB на 4 кейсах одного семейства — вывод YES/NO будет валиден для interstitials-подобных гипотез, не для базы знаний «вообще».
