# FREEZE MANIFEST — Revenue KB / Validator V1.4 (FLOW-632)

Дата freeze: **2026-08-07**. После freeze файлы бандла не меняются; любое
изменение = версия V1.5 с новым манифестом и новым прогоном протокола
(`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`, пороги неизменны).
Хеши считаются по байтам файлов (SHA-256, `shasum -a 256`).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md` (байтово).

```
89c78770592888ab907bc368377db88da7a0ba5386350f286824f292a195d4a8  KNOWLEDGE_CONTEXT (86 851 bytes)
```

Плечо A получает тот же промпт без блока KNOWLEDGE CONTEXT. Любое другое
включение файлов во вход инференса — нарушение протокола. Линтер-файлы
(`linter.py`, `linter_selftest.py`, `selftest_fixtures/`) и policy-копии во
вход инференса НЕ входят — они применяются к ответам после генерации.
**Карточка эксперимента** тоже не входит в KNOWLEDGE CONTEXT: она уже внутри
`{EXPERIMENT_CARD}`, а линтеру передаётся отдельно через `--card`.

## Frozen combined validator prompt V1.4

```
1bc3ab1eafd2d689e48ed7f2bd445a4d282d38844f1a0f4fe6c4e7734fab6919  validator_prompt_v1_4.md
```

Идентичен для плеч A/B; плейсхолдеры `{EXPERIMENT_CARD}` /
`{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` — в синтаксисе
V1/V1.1/V1.2/V1.3 (Phase B runner не меняется). Отличия от V1.3 — метка
`[computed]` в правиле 8 и обязательный раздел MAIN
`## What this experiment cannot show`. **Правило 4 не изменено.**

## SHA-256 файлов бандла

```
410ae3128c84fbd36baf631f4175358ceee388e96bdb0152591865ba780b742e  README.md
be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3  evidence_policy.md
e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a  evidence_policy_rules.yaml
dc3b5e6c3ea179bba3b9a4e8f61ad19338fa07f09e62bb8129ff8ab3c2d9cb6f  knowledge_base.md
581298a52793bf2128fca4b19ba53881346364639eda7cb6d2b6099235c67156  linter.py
a2735671cc801acfdf988a22face1c0efaaab00667abf9f0245b0014ab596065  linter_selftest.py
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  pattern_cards.md
1bc3ab1eafd2d689e48ed7f2bd445a4d282d38844f1a0f4fe6c4e7734fab6919  validator_prompt_v1_4.md
2acf7e68717bfd87df4105e2c3421effdcd2cff7b2747bab487af7063fce186e  selftest_fixtures/answer_cc_fail_arithmetic_mismatch.md
bfbbe185721516a72e1ce8b6de6cf6b0b0287ca93f789f1d1f220728dafaf643  selftest_fixtures/answer_cc_fail_fabricated.md
13edac748739b83f31bda00b18a57024b0247e34f5350581397300f1c06c52ce  selftest_fixtures/answer_cc_fail_kb_transfer.md
8a85ff412d7217a58b0c88eb525046544acb54b716dfc258e641e9f50ffa1635  selftest_fixtures/answer_cc_fail_missing_literal.md
b9b8654244e94546043d7e8fad95063878bfba44dfce214ca0afbe0f2e5d7bd9  selftest_fixtures/answer_cc_fail_missing_slot.md
4a3f4c7be0042b3b428a0e0ad843fd4a24dfeeeddf0fd361c55d81ea39c86084  selftest_fixtures/answer_cc_fail_no_operation.md
09dcb98c770f80acc0e6e6f55567fb623ba0f496dbc4bd680d2d38fa9f43998c  selftest_fixtures/answer_cc_fail_source_id.md
ef9a26cd570e79007d175bda24d042c4068408b65e9d4bbd412fd131d2660705  selftest_fixtures/answer_cc_nokb_fail_invented.md
1187ad31c43af311669ad20d03fbe4dd05829f823120652d22809aeb1c6daa6c  selftest_fixtures/answer_cc_nokb_pass.md
9951a0d40e59e3d5618313c59de6e6cac3f201ec6d6cba465f01063e88ef22c8  selftest_fixtures/answer_cc_pass_abstention.md
3505bb686f7d36ee10ba3260843a1c34c655460e719f3aba0ca43f18077fcdb2  selftest_fixtures/answer_cc_pass_computed.md
8a8e7685bc94c3e5367d8a51d8a13865c3141244f513919667c192bcb09b9ee0  selftest_fixtures/answer_cc_pass_ordinal_heading.md
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
4c1c8b6a81876b405570851d1f0b03c793760ccafbf6f577d300343383fc843e  selftest_fixtures/fixture_card_no_numbers.md
883ba06cc67d8747bd986a5102807a9652e021409672829caba54c5a0481aab4  selftest_fixtures/fixture_card.md
5dd6f5273c159d7f6619173455487cb01dc9957fc430c3354ee28d882c04f98f  selftest_fixtures/fixture_kb_gc.md
2d8733e30a40cef180671feb5e965041402aa4930cf7901a07ed0e7b3411380a  selftest_fixtures/fixture_kb_num.md
edaebd7a360fcc01ad31b3299a5d45035d7e01e33c351f717ecffea09b9b60fd  selftest_fixtures/fixture_kb.md
c2ed99419c5dc78176a6e5dae3ab3acb55b6a1be75db92515383e411f8a67b61  selftest_fixtures/fixture_patterns.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Байт-идентичность унаследованных файлов (проверено `cmp` перед freeze)

- `pattern_cards.md` (`b66247b4…b703`) — байт-в-байт равен V1.3, V1.2 и V1.1:
  корпус паттернов не менялся с V1.1.
- `evidence_policy.md` (`be2f9f0d…41b3`), `evidence_policy_rules.yaml`
  (`e4b83e6c…561a`) = `../revenue-evidence-policy-v1/` и всем бандлам
  V1.1–V1.3 — хеши совпадают со всеми манифестами; файлы НЕ расходятся с
  frozen Evidence Policy V1.
- 35 унаследованных фикстур V1.1/V1.2/V1.3 (`answer_fail_*`, `answer_nokb_*`,
  `answer_pass_*`, `answer_pp_*`, `fixture_kb.md`, `fixture_kb_gc.md`,
  `fixture_patterns.md`) = `../revenue-kb-v1.3/selftest_fixtures/` — все 35
  хешей совпадают с FREEZE_MANIFEST V1.3, ни одна не редактировалась.
- Изменены относительно V1.3 (ожидаемо): `knowledge_base.md` (+§2.8, §1.11,
  шапка), `linter.py` и `linter_selftest.py` (проверки §2.8 и тесты), новый
  `validator_prompt_v1_4.md` вместо `validator_prompt_v1_3.md`, 12 новых
  фикстур `answer_cc_*`, 3 новые фикстуры входных данных (`fixture_card.md`,
  `fixture_card_no_numbers.md`, `fixture_kb_num.md`), README.
- Старые бандлы не менялись: `revenue-corpus-prep-v1`, `revenue-kb-v1`,
  `revenue-kb-v1.1`, `revenue-kb-v1.2`, **`revenue-kb-v1.3`**,
  `revenue-kb-ab-run`, `revenue-kb-evaluation`, `revenue-evidence-policy-v1`,
  `revenue-kb-v1.1-regression-run`, `revenue-kb-v1.2-regression-run`,
  `trial-run-815603314`, `trial-run-815603314-v1.3`,
  `trial-run-815603314-v1.3-run2` — ни один файл не редактировался, хеши
  V1.3 сходятся с его собственным манифестом.

## Selftest

`python3 linter_selftest.py`: 124 теста, verdict GREEN; запущен дважды —
stdout байт-идентичен (детерминизм). Фикстуры полностью синтетические
(T9-01…T9-04, P-90, классы GC-90/GC-91, выдуманная карточка эксперимента с
выдуманными 64% / 25% / 30% / 3 pp / −1,5 pp / −4,2 pp, выдуманные темы
«widget nudges», «glow buttons», «invented widget»); линтер — stdlib-only,
без сети/времени/рандома, читает только файлы из аргументов.

## Регрессия V1.1/V1.2/V1.3

V1.4 делает раздел `## What this experiment cannot show` обязательным,
поэтому унаследованные фикстуры как есть больше не проходят. Блоки
`v14_delta_*` в `linter_selftest.py` утверждают дельту: exit 1 и набор кодов
= ровно прежний плюс `E_MISSING_COMPUTED_SLOT` (для фикстур V1.1/V1.2 — плюс
унаследованный `E_MISSING_PRODUCT_PROPOSALS`), ничего больше, и warnings без
изменений; проверено в двух KB-режимах (без классов §2.6 и с ними).

То же на **реальных ответах**: живой ответ плеча B V1.3 из FLOW-624
(`../trial-run-815603314-v1.3/outputs/arm-b.md`) и из FLOW-631
(`../trial-run-815603314-v1.3-run2/outputs/arm-b.md`) под линтером V1.4 дают
FAIL с единственным кодом `E_MISSING_COMPUTED_SLOT`; уровни карточек
по-прежнему L2/L2/L2 и L1/L2/L3 соответственно, warning FLOW-631
`W_RISK_SOURCE_WITHOUT_PROPOSAL` на месте.

## Прогон на живом кейсе

`../trial-run-815603314-v1.4/` — тот же кейс 815603314 (версия 51), оба
плеча, линтер V1.4 с `--card`. Детали, хеши и оценка по рубрике — в
`RUN_MANIFEST.md` и `rubric_run.md` того каталога.

## Порядок сборки (для воспроизводимости)

`knowledge_base.md` и `validator_prompt_v1_4.md` были заморожены ДО сборки
входов инференса; хеш KNOWLEDGE_CONTEXT в `RUN_MANIFEST.md` прогона совпадает
с указанным выше. `linter.py` и `linter_selftest.py` дорабатывались ПОСЛЕ
генерации ответов — по пяти ложным срабатываниям детектора нотации, которые
этот прогон и выявил (см. README, раздел Selftest). Это законно: линтер не
входит во вход инференса и применяется к ответам после генерации. Вердикты в
`RUN_MANIFEST.md` посчитаны финальной версией линтера, хеш которой указан
здесь.
