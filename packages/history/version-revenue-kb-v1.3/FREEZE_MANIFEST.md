# FREEZE MANIFEST — Revenue KB / Validator V1.3 (FLOW-624)

Дата freeze: **2026-08-07**. После freeze файлы бандла не меняются; любое
изменение = версия V1.4 с новым манифестом и новым прогоном протокола
(`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`, пороги неизменны).
Хеши считаются по байтам файлов (SHA-256, `shasum -a 256`).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md` (байтово).

```
6ad35b7a39ea051b33056683bcbf42884044c03e7b5c0b6d2cc9afa12a2bd94d  KNOWLEDGE_CONTEXT (79 589 bytes)
```

Плечо A получает тот же промпт без блока KNOWLEDGE CONTEXT. Любое другое
включение файлов во вход инференса — нарушение протокола. Линтер-файлы
(`linter.py`, `linter_selftest.py`, `selftest_fixtures/`) и policy-копии во
вход инференса НЕ входят — они применяются к ответам после генерации.

## Frozen combined validator prompt V1.3

```
94a4f414a06221ceb4e82ca94de71ce499fd38438e6d397d7149396632f894ce  validator_prompt_v1_3.md
```

Идентичен для плеч A/B; плейсхолдеры `{EXPERIMENT_CARD}` /
`{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` — в синтаксисе
V1/V1.1/V1.2 (Phase B runner не меняется). Отличия от V1.2 — правило 12 и
формат вывода MAIN/APPENDIX.

## SHA-256 файлов бандла

```
b087db11aea4497e050e023a8f27400cdafab481b08b88d8b4c7c0a70e66a5d9  README.md
be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3  evidence_policy.md
e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a  evidence_policy_rules.yaml
3ca1ec9d5aba19db84b0ccc89f3b63f43e07711fae8e697a1d55502aaaa670cd  knowledge_base.md
e8d381c32ed98bf3cf46a6181e512575c8566b2d21e430b7ef41120a6d74ce04  linter.py
bb33108f86a872557f91a8dd16e152f101b6877dd88ec453a4c17e03032e004e  linter_selftest.py
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  pattern_cards.md
94a4f414a06221ceb4e82ca94de71ce499fd38438e6d397d7149396632f894ce  validator_prompt_v1_3.md
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
0ae62a580a1edd5a1ad8c88396b75cbae2c0c5b05922aa3348954e11be9dbb08  selftest_fixtures/answer_pp_fail_id_in_ungrounded.md
93883cac7a623b159cf04c100635808f6b269d5836f2dfd6af7b91b78fdbd08f  selftest_fixtures/answer_pp_fail_missing_literal.md
f1054dba358893b086ec900c2a6d0bebaa274c5affb3602eb407c9348b116791  selftest_fixtures/answer_pp_fail_missing_section.md
25d17550cb2ac4e849131c409cf77e389145e15428d5863b906d4aee4614aa73  selftest_fixtures/answer_pp_fail_ungrounded_claim.md
75806b5504a7e4807f5444e9fe837520121457825368ed74826c075b263d2295  selftest_fixtures/answer_pp_fail_unknown_id.md
cd9d25ecb1434daee1d02b064cbd0b8a5648e14e53b7bcac4b2563d88991d408  selftest_fixtures/answer_pp_fail_untyped.md
efd60b26c69590b6c8f8a8630baf69c3faef38a6b7908accf90491e9c1e7ca6e  selftest_fixtures/answer_pp_fail_weak_grounding.md
37a4cb5848887e5070c03b4459b905ec5415cc6df81da7c1b69a49f8eb8f5d21  selftest_fixtures/answer_pp_nokb_fail_proposal.md
86d9933551a3615f7d4b555afaec8064adce1f4aa75ea09841bb66923af65381  selftest_fixtures/answer_pp_nokb_pass.md
c8cc11a4ed0c177a038298709dcfe2a8e9d76b85794fe4e057c0a8be33a0628f  selftest_fixtures/answer_pp_pass_abstention.md
4026e3a352ec88b36b9f7f7666ac081edd9c6c615bc3c6496803aca96f8aeb30  selftest_fixtures/answer_pp_pass_cap_warning.md
833b72973164977adc9f5f4ebe960531c35507a01a307df0af19403f1348d735  selftest_fixtures/answer_pp_pass_duplicate_heading.md
b5c7da01a95210e7ebc290c070801a13b3996d1a0f11142823b3ddd8d4c4c47b  selftest_fixtures/answer_pp_pass_grounded.md
5bda8426a7280ccef6da70c48f57836d3bd907b8b1d418741b430d55be865406  selftest_fixtures/answer_pp_pass_risk_without_proposal.md
edaebd7a360fcc01ad31b3299a5d45035d7e01e33c351f717ecffea09b9b60fd  selftest_fixtures/fixture_kb.md
5dd6f5273c159d7f6619173455487cb01dc9957fc430c3354ee28d882c04f98f  selftest_fixtures/fixture_kb_gc.md
c2ed99419c5dc78176a6e5dae3ab3acb55b6a1be75db92515383e411f8a67b61  selftest_fixtures/fixture_patterns.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Байт-идентичность унаследованных файлов (проверено `cmp` перед freeze)

- `pattern_cards.md` (`b66247b4…b703`) — байт-в-байт равен V1.2 и V1.1:
  корпус паттернов V1.3 не менялся.
- `evidence_policy.md` (`be2f9f0d…41b3`), `evidence_policy_rules.yaml`
  (`e4b83e6c…561a`) = `../revenue-evidence-policy-v1/`,
  `../revenue-kb-v1.1/` и `../revenue-kb-v1.2/` — хеши совпадают со всеми
  тремя манифестами; файлы НЕ расходятся с frozen Evidence Policy V1.
- 21 фикстура V1.1/V1.2 (`answer_fail_*`, `answer_nokb_*`, `answer_pass_*`,
  `fixture_kb.md`, `fixture_kb_gc.md`, `fixture_patterns.md`) = 
  `../revenue-kb-v1.2/selftest_fixtures/` — все хеши совпадают с
  FREEZE_MANIFEST V1.2.
- Изменены относительно V1.2 (ожидаемо): `knowledge_base.md` (+§2.7, §1.10,
  шапка), `linter.py` и `linter_selftest.py` (проверки §2.7 и тесты), новый
  `validator_prompt_v1_3.md`, 14 новых фикстур `answer_pp_*`, README.
- Старые бандлы не менялись: `revenue-corpus-prep-v1`, `revenue-kb-v1`,
  `revenue-kb-v1.1`, `revenue-kb-v1.2`, `revenue-kb-ab-run`,
  `revenue-kb-evaluation`, `revenue-evidence-policy-v1`,
  `revenue-kb-v1.1-regression-run`, `revenue-kb-v1.2-regression-run`,
  `trial-run-815603314` — ни один файл не редактировался.

## Selftest

`python3 linter_selftest.py`: 91 тест, verdict GREEN; запущен дважды —
stdout байт-идентичен (детерминизм). Фикстуры полностью синтетические
(T9-01…T9-04, P-90, классы GC-90/GC-91, выдуманные темы «widget nudges»,
«glow buttons», «invented widget»); линтер — stdlib-only, без
сети/времени/рандома, читает только файлы из аргументов.

## Регрессия V1.1/V1.2

V1.3 делает раздел `## Product proposals` обязательным, поэтому
унаследованные фикстуры как есть больше не проходят. Блок `v13_delta_*`
в `linter_selftest.py` утверждает дельту: exit 1 и набор кодов = ровно
прежний плюс `E_MISSING_PRODUCT_PROPOSALS`, ничего больше; проверено в двух
KB-режимах (без классов §2.6 и с ними), 22 прогона. То же на реальном
ответе: `../trial-run-815603314/outputs/arm-b.md` (живой ответ V1.2) под
линтером V1.3 даёт FAIL с единственным кодом
`E_MISSING_PRODUCT_PROPOSALS`, все три карточки по-прежнему считаются
L2/L2/L3.

## Прогон на живом кейсе

`../trial-run-815603314-v1.3/` — тот же кейс 815603314, оба плеча, линтер
V1.3: A PASS (0 предложений, честный отказ), B PASS (3 заземлённых
предложения, 3 карточки L2). Детали и хеши — в `RUN_MANIFEST.md` того
бандла.
