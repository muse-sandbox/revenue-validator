# FREEZE MANIFEST — Revenue KB / Validator V1.2 (FLOW-593)

Дата freeze: **2026-08-06**. После freeze файлы бандла не меняются; любое
изменение = версия V1.3 с новым манифестом и новым прогоном протокола
(`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`, пороги неизменны).
Хеши считаются по байтам файлов (SHA-256, `shasum -a 256`).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md` (байтово).

```
9949e10b34df6c2e67c14dcec30e2f00ef8c175bccc327d2c262e752ddd10df3  KNOWLEDGE_CONTEXT (72 949 bytes)
```

Плечо A получает тот же промпт без блока KNOWLEDGE CONTEXT. Любое другое
включение файлов во вход инференса — нарушение протокола. Линтер-файлы
(`linter.py`, `linter_selftest.py`, `selftest_fixtures/`) и policy-копии во
вход инференса НЕ входят — они применяются к ответам после генерации.

## Frozen combined validator prompt V1.2

```
62a39eb89eede880b977310ac943e6fa73788f6da8daf2e7876dfb90ad818b4a  validator_prompt_v1_2.md
```

Идентичен для плеч A/B; плейсхолдеры `{EXPERIMENT_CARD}` /
`{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` — в синтаксисе V1/V1.1
(Phase B runner не меняется).

## SHA-256 файлов бандла

```
3b1ebce07d98fab488c939bad48c398fd3d04907747fc66410c432c7af1b53eb  README.md
be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3  evidence_policy.md
e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a  evidence_policy_rules.yaml
626ec56497da9986db66510dbf09d5ddbe805d63e57fbdd9e266c226dfc0b2c7  knowledge_base.md
16251d6a370128b7b3892849925d50c9e1a54a8f38808e9f09492d5dc70a9c3e  linter.py
3fe53f55b014d9275a161d57bcf444945b6b9976a8a1c5cec15bd956f8cf3c9b  linter_selftest.py
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  pattern_cards.md
5edd8630df28ed595cea4038e98155ab9cccd942a7ab59c5d791cd23951c6bca  selftest_fixtures/answer_fail_bad_source.md
b3a3843647f300ba1ec2641332a246b53beafca105f6ccfcd347f280bc2d4b6a  selftest_fixtures/answer_fail_contradiction.md
b81e9d82b80aa8b8a879c037331c01d6439f3b6cd818a7d453d00c1b822c495a  selftest_fixtures/answer_fail_empty_nt.md
9b7c86511078ff0211da0aa426fd8a66a7d1cd53c0b459cbc963837a2dd0d735  selftest_fixtures/answer_fail_inflation.md
2ff487fdd35c25674fcf6ed11bc900bd7b9c692ffedd3169279a7985a41185bf  selftest_fixtures/answer_fail_missing_axis.md
6636617501820341251c2ff4397214ce5ee95b2d90d497dbd38ee80558c40cf1  selftest_fixtures/answer_fail_missing_no_direct.md
b9b0d3b738cfb1e941efd888309bc737cf6c2f0ffe33e4576b5fa9d7c1559919  selftest_fixtures/answer_fail_no_sideeffects.md
366f79c15e3c4243e7191ee5c6a637cd3819723eec31a8c412b6cc7c8e16d31c  selftest_fixtures/answer_fail_scope_bad_id.md
0b9c1729d6fa90ca9e33a08048d4c967f1df8e4bccd130e2e6e4b065189cafde  selftest_fixtures/answer_fail_scope_malformed.md
d19eba9d44f5c2f188b013813e9c6db46d280198915494fe9635cc7c27e10642  selftest_fixtures/answer_fail_unqualified_universal.md
084eda7c7d485e8969606d42ef5bb1313b4a06e8db973e433ea6f1bf08eb874d  selftest_fixtures/answer_nokb_fail_card.md
83bdf8e3fdec0ea9815d6d0b1d46ddc5dbffd5a9d3b3d76992646d8631847730  selftest_fixtures/answer_nokb_pass.md
940380d4d871da91037bddfa7dc9097c8e9b8a3a0025d9bcca9fda5845e31a11  selftest_fixtures/answer_pass_l1.md
010392f13aac04f0998f1c7fe29f18742ccf8805bd8fea1b6521e4e2c4e94407  selftest_fixtures/answer_pass_l2_branches.md
9ce93e650de0632ab9d8a7056e38376782a8118030491320fe4e9a9847057490  selftest_fixtures/answer_pass_l3_nodirect.md
8b4a430a26afd229ad658d02e471f81a7b2721f550073208c50539ffaa42c9df  selftest_fixtures/answer_pass_mixed_evidence.md
f64a391acc6d03c31d60ff3be1197ddcb1c36b27699a4101495185b38f4b217a  selftest_fixtures/answer_pass_no_generalization.md
b5db5bd90a36f35ee92bedfb4c676f6c29cbbf91c1809b647932c84aa4735e9e  selftest_fixtures/answer_pass_scoped_universal.md
5dd6f5273c159d7f6619173455487cb01dc9957fc430c3354ee28d882c04f98f  selftest_fixtures/fixture_kb_gc.md
edaebd7a360fcc01ad31b3299a5d45035d7e01e33c351f717ecffea09b9b60fd  selftest_fixtures/fixture_kb.md
c2ed99419c5dc78176a6e5dae3ab3acb55b6a1be75db92515383e411f8a67b61  selftest_fixtures/fixture_patterns.md
62a39eb89eede880b977310ac943e6fa73788f6da8daf2e7876dfb90ad818b4a  validator_prompt_v1_2.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Байт-идентичность унаследованных файлов (проверено `cmp` перед freeze)

- `evidence_policy.md` (`be2f9f0d…41b3`), `evidence_policy_rules.yaml`
  (`e4b83e6c…561a`) = `../revenue-evidence-policy-v1/` и
  `../revenue-kb-v1.1/` — хеши совпадают с манифестами обоих бандлов; файлы
  НЕ расходятся с frozen Evidence Policy V1.
- 13 фикстур V1.1 (`answer_fail_bad_source.md`, `answer_fail_empty_nt.md`,
  `answer_fail_inflation.md`, `answer_fail_missing_axis.md`,
  `answer_fail_missing_no_direct.md`, `answer_fail_no_sideeffects.md`,
  `answer_nokb_fail_card.md`, `answer_nokb_pass.md`, `answer_pass_l1.md`,
  `answer_pass_l2_branches.md`, `answer_pass_l3_nodirect.md`,
  `fixture_kb.md`, `fixture_patterns.md`) = `../revenue-kb-v1.1/
  selftest_fixtures/` — все хеши совпадают с FREEZE_MANIFEST V1.1.
- Изменены относительно V1.1 (ожидаемо): `knowledge_base.md` (+§2.5, §2.6,
  §1.9, шапка), `pattern_cards.md` (аудит scope заголовков/claim/бан-строк),
  `linter.py` и `linter_selftest.py` (новые проверки и тесты), новый
  `validator_prompt_v1_2.md`, новые фикстуры, README.
- Старые бандлы не менялись: полный пересчёт манифестов
  `revenue-corpus-prep-v1`, `revenue-kb-v1`, `revenue-kb-ab-run`,
  `revenue-kb-evaluation`, `revenue-evidence-policy-v1`, `revenue-kb-v1.1`,
  `revenue-kb-v1.1-regression-run`,
  `revenue-kb-v1.1-regression-evaluation` дал `TOTAL: ok=168 fail=0` до и
  после сборки V1.2.

## Selftest

`python3 linter_selftest.py`: 64 теста, verdict GREEN; запущен дважды —
stdout байт-идентичен (детерминизм). Фикстуры полностью синтетические
(T9-01…T9-04, P-90, классы GC-90/GC-91, выдуманные темы «widget nudges» и
«glow buttons»); линтер — stdlib-only, без сети/времени/рандома, читает
только файлы из аргументов.

## Регрессия V1.1

Линтер V1.2 по замороженным фикстурам V1.1 (два KB-режима, 22 прогона):
`ok=22 fail=0` — все вердикты и наборы кодов ошибок V1.1 сохранены,
новых кодов на V1.1-фикстурах не появилось
(`analysis_scripts/20260805_flow593_v11_fixture_regression.py`).
