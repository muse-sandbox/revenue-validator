# FREEZE MANIFEST — Revenue KB / Validator V1.1 (FLOW-586)

Дата freeze: **2026-08-05**. После freeze файлы бандла не меняются; любое
изменение = версия V1.2 с новым манифестом и новым прогоном протокола
(`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`, пороги неизменны).
Хеши считаются по байтам файлов (SHA-256, `shasum -a 256`).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md` (байтово).

```
ae980e466379392e751e714c2abe2566a76f3c3880c8437ffd6a3b62ac6b91df  KNOWLEDGE_CONTEXT (58 094 bytes)
```

Плечо A получает тот же промпт без блока KNOWLEDGE CONTEXT. Любое другое
включение файлов во вход инференса — нарушение протокола. Линтер-файлы
(`linter.py`, `linter_selftest.py`, `selftest_fixtures/`) и policy-копии во
вход инференса НЕ входят — они применяются к ответам после генерации.

## Frozen combined validator prompt V1.1

```
bb2296b6a98d16f4eee2f33bff9707c5c6248ab8f322f982c7885bcbd93cf380  validator_prompt_v1_1.md
```

Идентичен для плеч A/B; плейсхолдеры `{EXPERIMENT_CARD}` /
`{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` — в синтаксисе V1.

## SHA-256 файлов бандла

```
214912a71545c0a9f27203f363fe0a9cea0f4bc37891ca6e4b0250a5b5c46d22  README.md
be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3  evidence_policy.md
e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a  evidence_policy_rules.yaml
a561ba52e60d3d78c4fc789165086e24e6a26ff4c954b3d60db4a991972c5623  knowledge_base.md
a2d4f5b872a49aecd03a37692b5fa53b4e8950cf0b8e752d750363fb24c63fe0  linter.py
845c9c4da40fa4453f833fd6f3683ef4536e3a1e96d78b8622f3a6bad95d1a65  linter_selftest.py
a3f3b7ac9cb0991a29558dee28054c926a0d065018b2e27f9ff5a270e75c04a0  pattern_cards.md
5edd8630df28ed595cea4038e98155ab9cccd942a7ab59c5d791cd23951c6bca  selftest_fixtures/answer_fail_bad_source.md
b81e9d82b80aa8b8a879c037331c01d6439f3b6cd818a7d453d00c1b822c495a  selftest_fixtures/answer_fail_empty_nt.md
9b7c86511078ff0211da0aa426fd8a66a7d1cd53c0b459cbc963837a2dd0d735  selftest_fixtures/answer_fail_inflation.md
2ff487fdd35c25674fcf6ed11bc900bd7b9c692ffedd3169279a7985a41185bf  selftest_fixtures/answer_fail_missing_axis.md
6636617501820341251c2ff4397214ce5ee95b2d90d497dbd38ee80558c40cf1  selftest_fixtures/answer_fail_missing_no_direct.md
b9b0d3b738cfb1e941efd888309bc737cf6c2f0ffe33e4576b5fa9d7c1559919  selftest_fixtures/answer_fail_no_sideeffects.md
084eda7c7d485e8969606d42ef5bb1313b4a06e8db973e433ea6f1bf08eb874d  selftest_fixtures/answer_nokb_fail_card.md
83bdf8e3fdec0ea9815d6d0b1d46ddc5dbffd5a9d3b3d76992646d8631847730  selftest_fixtures/answer_nokb_pass.md
940380d4d871da91037bddfa7dc9097c8e9b8a3a0025d9bcca9fda5845e31a11  selftest_fixtures/answer_pass_l1.md
010392f13aac04f0998f1c7fe29f18742ccf8805bd8fea1b6521e4e2c4e94407  selftest_fixtures/answer_pass_l2_branches.md
9ce93e650de0632ab9d8a7056e38376782a8118030491320fe4e9a9847057490  selftest_fixtures/answer_pass_l3_nodirect.md
edaebd7a360fcc01ad31b3299a5d45035d7e01e33c351f717ecffea09b9b60fd  selftest_fixtures/fixture_kb.md
c2ed99419c5dc78176a6e5dae3ab3acb55b6a1be75db92515383e411f8a67b61  selftest_fixtures/fixture_patterns.md
bb2296b6a98d16f4eee2f33bff9707c5c6248ab8f322f982c7885bcbd93cf380  validator_prompt_v1_1.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Байт-идентичность унаследованных файлов (проверено `cmp` перед freeze)

- `pattern_cards.md` = `../revenue-kb-v1/pattern_cards.md`
  (`a3f3b7ac…c04a0` — совпадает с FREEZE_MANIFEST V1).
- `evidence_policy.md`, `evidence_policy_rules.yaml` =
  `../revenue-evidence-policy-v1/` (frozen Evidence Policy V1).
- Старый бандл `../revenue-kb-v1/` не менялся: все 9 файлов его
  FREEZE_MANIFEST пересчитаны 2026-08-05, хеши совпали.

## Selftest

`python3 linter_selftest.py`: 25 тестов, verdict GREEN; запущен дважды —
stdout байт-идентичен (детерминизм). Фикстуры полностью синтетические
(T9-01/T9-02/P-90); линтер — stdlib-only, без сети/времени/рандома, читает
только файлы из аргументов.
