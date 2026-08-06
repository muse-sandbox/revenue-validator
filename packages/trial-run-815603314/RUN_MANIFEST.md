# TRIAL RUN — Official Tabs micro-demo in first session

Пробный прогон Validator V1.2 на живом незапущенном эксперименте.
Не является зачётным кейсом shadow pilot: pre-AI snapshot не фиксировался,
время ревью человеком не замерялось.

- Источник карточки: Confluence 815603314, версия 51, space CRO
- Валидатор: frozen bundle `../revenue-kb-v1.2/` (не изменялся)
- Дата прогона: 2026-08-06
- Плечи выполнены в изолированных контекстах, без доступа к поиску и внешним источникам

## Результат линтера

| Плечо | Вердикт | Ошибок | Карточек | Уровни |
|---|---|---|---|---|
| A, без базы | PASS | 0 | 0 (корректно) | — |
| B, с базой | PASS | 0 | 3 | заявленные = вычисленным 3/3 |

## Объём ответов

| Плечо | Слов | Кап промпта |
|---|---|---|
| A | 802 | ~700 |
| B | 736 | ~700 |

## SHA-256

| Файл | Хеш |
|---|---|
| `inputs/arm-a.md` | `41a73c5572f8acec2311c5bcfec42232107612aecd32cbfca1152e8b61e141c4` |
| `inputs/arm-b.md` | `ac218903f8b926e2d54f9b3451349726de2966519bb822b03024071c016dee73` |
| `outputs/arm-a.md` | `d10f7940b242191ea31575147fd9915d98531941569fcfdfa7ff9eb28ab54ef2` |
| `outputs/arm-b.md` | `1c2a59a3cbdf47672bd6ba66688032f9d5079944e298758e2539ccec352e45cb` |

## Использованные frozen-файлы (не изменялись)

| Файл | Хеш |
|---|---|
| `revenue-kb-v1.2/validator_prompt_v1_2.md` | `62a39eb89eede880b977310ac943e6fa73788f6da8daf2e7876dfb90ad818b4a` |
| `revenue-kb-v1.2/knowledge_base.md` | `626ec56497da9986db66510dbf09d5ddbe805d63e57fbdd9e266c226dfc0b2c7` |
| `revenue-kb-v1.2/pattern_cards.md` | `b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703` |
