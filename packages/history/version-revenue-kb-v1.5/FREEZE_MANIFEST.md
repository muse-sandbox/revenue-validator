# FREEZE MANIFEST — Revenue KB / Validator V1.5 (FLOW-629)

Дата freeze: **2026-08-08**. После freeze файлы бандла не меняются; любое
изменение = версия V1.6 с новым манифестом и новым прогоном протокола
(`../revenue-corpus-prep-v1/EVALUATION_PROTOCOL.md`, пороги неизменны).
Хеши считаются по байтам файлов (SHA-256, `shasum -a 256`).

## Состав KNOWLEDGE CONTEXT плеча B (зафиксировано)

Конкатенация ровно двух файлов в порядке:
`knowledge_base.md` + разделитель `\n\n---\n\n` + `pattern_cards.md` (байтово).

```
41387c34cbdf88cb9203d5bad1ea1b732e43e8807de10757102d804cdc150321  KNOWLEDGE_CONTEXT (98281 bytes)
```

Плечо A получает тот же промпт без блока KNOWLEDGE CONTEXT. Любое другое
включение файлов во вход инференса — нарушение протокола. Линтер-файлы
(`linter.py`, `linter_selftest.py`, `selftest_fixtures/`) и policy-копии во
вход инференса НЕ входят — они применяются к ответам после генерации.
**Карточка эксперимента** тоже не входит в KNOWLEDGE CONTEXT: она уже внутри
`{EXPERIMENT_CARD}`, а линтеру передаётся отдельно через `--card`.

## Frozen combined validator prompt V1.5

```
d053830fd04e79567573132a545ab1ebff3cb51bb214611fd29717734f490f77  validator_prompt_v1_5.md
```

Идентичен для плеч A/B; плейсхолдеры `{EXPERIMENT_CARD}` /
`{KNOWLEDGE_CONTEXT}` и блок `<knowledge-context>` — в синтаксисе
V1…V1.4 (Phase B runner не меняется). Отличия от V1.4 — новое правило 13
(форма замечания: последствие, механизм, цена), одна вставка в правило 8
(куда кладётся `[computed]`), одна правка формулировки каналов в правиле 12 и
перестроенный `### Output format`: три раздела MAIN (`Top risks & failure
modes`, `Blocking design fixes`, `What this experiment cannot show`) заменены
одним `## Findings`, добавлен `## What you decide`, добавлено приложение
`## D. Findings without a price`. **Правило 4 не изменено.**

## SHA-256 файлов бандла

```
89f373e353f5fdb73a37ea22e69e681ec9db0a7b3af814eec13cffae98362ca7  README.md
be2f9f0d98cd87df7e563219240fcdc2964171447263d24dcbff254ba13441b3  evidence_policy.md
e4b83e6c069d01a1e7593fa5fa69b9f8b4b07a864edd3550598818e557af561a  evidence_policy_rules.yaml
3200783192b2e2ddc9ffbe62b7df12f78aa69b2ce7a104a7107bb60b22ae75bd  knowledge_base.md
aec3de7de5894ae141c936be0886bcf7447cca127869da26ce298a9d47798ecf  linter.py
bb68e8bcd49b7683ed6d57677a60d1da1a19f55288d2d8888731eab1473d57d8  linter_selftest.py
b66247b43bf96d2683e1236fc92063d21b84322f1b86a0bfa75ba87a4e0b7703  pattern_cards.md
d053830fd04e79567573132a545ab1ebff3cb51bb214611fd29717734f490f77  validator_prompt_v1_5.md
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
761d164f52461f60933bd3f91c4826d043daa8e7272f0e3408d22e86eeb91a28  selftest_fixtures/answer_fd_fail_analog_card_in_main.md
119018e3720a9865df5168689764d195f566f57013cd367f239d6dffa628da71  selftest_fixtures/answer_fd_fail_decision_role_missing.md
0260ead5b1accf0b682f7c3d7ac0f4bdbe015d1fb3f7a927301e98ef0388ca72  selftest_fixtures/answer_fd_fail_machine_field_main.md
954803e023b12e075480394a08180ab3c113ba1330e6e81bd20e0f5e6f8dae01  selftest_fixtures/answer_fd_fail_mechanism_ungrounded.md
e7b81ccc760dad916894386c8d8348eb694c5b4d3e6222299ef8117a74a737b3  selftest_fixtures/answer_fd_fail_missing_decisions.md
be7bbe632b055a10e9d4a280761a887f99a4ff58a82025276a8801111de11b6e  selftest_fixtures/answer_fd_fail_missing_findings.md
bd6b751a9f66e9cec4ab673fdf1de2f3cecc480908ed41ed4691a6fb2f4e4522  selftest_fixtures/answer_fd_fail_no_consequence.md
a463629f9c7905af7a59f85d9958f95477a184c2945c31ba7ebd26a00d6f3da6  selftest_fixtures/answer_fd_fail_no_mechanism.md
fd4f913d07f06b572a6f6c6ccc7a611fffcb75cbdaf4e26308c75d748764412b  selftest_fixtures/answer_fd_fail_no_price.md
d2e6e6b34da47a2d8d02b99392082c881c26be045b572080389eec15584ee09e  selftest_fixtures/answer_fd_fail_no_result_verb.md
1686d2cf8e9d4b9c7077e4e66867da1cce5ef5c75b98c5d631c6f19b0bdcf457  selftest_fixtures/answer_fd_fail_not_ranked.md
953854829e0046e9b3add1c0e485b40f7b311dc57f3d5670f6ff90a976d4f75f  selftest_fixtures/answer_fd_fail_paper_headline.md
b1694de902ca3ec8c34fa79201e5f4310735075634f0a8d759a97248f4f1c0d5  selftest_fixtures/answer_fd_fail_price_unit.md
a34f1517e9625d22c840721b363cbd75ac3aa9cf648b2295615c48a3e75ba142  selftest_fixtures/answer_fd_fail_too_many_stops.md
ff2961f35d27e56c5701ff0c43f5d01f801c4637425462bc75fc84153ffd504d  selftest_fixtures/answer_fd_fail_untyped.md
1cc77474b10c8d80ff8355f81b3fabf7c2ffa7f312c14db96ad2407b5fcb701f  selftest_fixtures/answer_fd_nokb_pass.md
5997ed95610abff70a1c7c7ad3ecbe2b33ba8b45f057589f89d34bc4130bbc3a  selftest_fixtures/answer_fd_pass.md
4eb9dce83e1cdfbeb71fa42d558850abdeecf06b8bdb884dcbccb11d2467ba6c  selftest_fixtures/answer_fd_pass_abstention.md
dec812418840ed055c71bd99ea5f0d9e7544efe9698aedc2ff4ab2cc7d48db58  selftest_fixtures/answer_fd_pass_ordinal_heading.md
e25ebce8fa2f51b9cda044d88e21c1c7978a16c73658f2245b0b75d5d2a845d2  selftest_fixtures/answer_fd_warn_duplicate.md
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
883ba06cc67d8747bd986a5102807a9652e021409672829caba54c5a0481aab4  selftest_fixtures/fixture_card.md
4c1c8b6a81876b405570851d1f0b03c793760ccafbf6f577d300343383fc843e  selftest_fixtures/fixture_card_no_numbers.md
edaebd7a360fcc01ad31b3299a5d45035d7e01e33c351f717ecffea09b9b60fd  selftest_fixtures/fixture_kb.md
5dd6f5273c159d7f6619173455487cb01dc9957fc430c3354ee28d882c04f98f  selftest_fixtures/fixture_kb_gc.md
2d8733e30a40cef180671feb5e965041402aa4930cf7901a07ed0e7b3411380a  selftest_fixtures/fixture_kb_num.md
c2ed99419c5dc78176a6e5dae3ab3acb55b6a1be75db92515383e411f8a67b61  selftest_fixtures/fixture_patterns.md
```

`FREEZE_MANIFEST.md` в список не входит (самоссылка).

## Байт-идентичность унаследованных файлов (проверено SHA-256 перед freeze)

- `pattern_cards.md` (`b66247b4…b703`) — байт-в-байт равен V1.4, V1.3, V1.2 и
  V1.1: корпус паттернов не менялся с V1.1.
- `evidence_policy.md` (`be2f9f0d…41b3`), `evidence_policy_rules.yaml`
  (`e4b83e6c…561a`) = `../revenue-evidence-policy-v1/` и всем бандлам
  V1.1–V1.4 — хеши совпадают со всеми манифестами; файлы НЕ расходятся с
  frozen Evidence Policy V1.
- **50** унаследованных фикстур V1.1/V1.2/V1.3/V1.4 (`answer_fail_*`,
  `answer_nokb_*`, `answer_pass_*`, `answer_pp_*`, `answer_cc_*`,
  `fixture_card.md`, `fixture_card_no_numbers.md`, `fixture_kb.md`,
  `fixture_kb_gc.md`, `fixture_kb_num.md`, `fixture_patterns.md`) =
  `../revenue-kb-v1.4/selftest_fixtures/` — все 50 хешей совпадают с
  FREEZE_MANIFEST V1.4, ни одна не редактировалась.
- Изменены относительно V1.4 (ожидаемо, ровно три файла): `knowledge_base.md`
  (+§1.12, +§2.9, шапка, правки §2.7/§2.8 на новые имена разделов),
  `linter.py` и `linter_selftest.py` (проверки §2.9 и тесты).
- Добавлены: `validator_prompt_v1_5.md` вместо `validator_prompt_v1_4.md`,
  20 новых фикстур `answer_fd_*`, README, этот манифест.
- Старые бандлы не менялись: `revenue-corpus-prep-v1`, `revenue-kb-v1`,
  `revenue-kb-v1.1`, `revenue-kb-v1.2`, `revenue-kb-v1.3`,
  **`revenue-kb-v1.4`**, `revenue-kb-ab-run`, `revenue-kb-evaluation`,
  `revenue-evidence-policy-v1`, `revenue-kb-v1.1-regression-run`,
  `revenue-kb-v1.2-regression-run`, `trial-run-815603314`,
  `trial-run-815603314-v1.3`, `trial-run-815603314-v1.3-run2`,
  `trial-run-815603314-v1.4` — ни один файл не редактировался.

## Selftest

`python3 linter_selftest.py`: 159 тестов, verdict GREEN; запущен дважды —
stdout байт-идентичен (детерминизм). Фикстуры полностью синтетические
(T9-01…T9-04, P-90, классы GC-90/GC-91, выдуманная карточка эксперимента,
выдуманные темы «widget nudges», «glow buttons», «invented widget»); линтер —
stdlib-only, без сети/времени/рандома, читает только файлы из аргументов.

## Регрессия V1.1–V1.4

V1.5 делает `## Findings`, `## What you decide` и баннер `# MAIN`
обязательными и снимает раздел `## What this experiment cannot show`, поэтому
унаследованные фикстуры как есть больше не проходят. Блоки `v15_delta_*` в
`linter_selftest.py` утверждают дельту: exit 1 и набор кодов = ровно прежний
плюс `E_MISSING_FINDINGS`, `E_MISSING_DECISIONS`, `E_MISSING_MAIN_BANNER`,
минус `E_MISSING_COMPUTED_SLOT` и `E_MISSING_NO_COMPUTABLE_LIMIT`, ничего
больше, и warnings без изменений; проверено в двух KB-режимах (без классов
§2.6 и с ними).

То же на **реальных ответах**: оба живых ответа V1.4
(`../trial-run-815603314-v1.4/outputs/arm-{a,b}.md`) под линтером V1.5 дают
FAIL с прежним единственным §2.8-кодом (`E_COMPUTED_NUMBER_FABRICATED` в
плече A, `E_COMPUTED_NUMBER_FROM_KB` в плече B) плюс ровно
`E_MISSING_FINDINGS` и `E_MISSING_DECISIONS`; `E_MISSING_MAIN_BANNER` не
срабатывает — баннер у них есть. Единственный новый warning —
`W_MAIN_OVER_CAP` в обоих плечах.

## Прогон на живом кейсе

`../trial-run-815603314-v1.5/` — тот же кейс 815603314 (версия 51), оба
плеча, линтер V1.5 с `--card`. Детали, хеши и оценка по рубрике — в
`RUN_MANIFEST.md` и `rubric_run.md` того каталога.

## Порядок сборки (для воспроизводимости)

`knowledge_base.md` и `validator_prompt_v1_5.md` были заморожены ДО сборки
входов инференса; хеш KNOWLEDGE_CONTEXT в `RUN_MANIFEST.md` прогона совпадает
с указанным выше. `linter.py`, `linter_selftest.py` и фикстуры доводились ДО
генерации ответов (selftest GREEN снят до прогона) и после генерации НЕ
менялись. README и этот манифест написаны последними; они во вход инференса
не входят.
