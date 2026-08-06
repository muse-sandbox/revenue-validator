#!/usr/bin/env python3
"""FLOW-578: зачистка перекрёстных ссылок на holdout-кейсы в очищенном inventory.

EXCLUSION_MANIFEST запрещает не только сами записи, но и алиасы/пересказы
результатов holdout-кейсов. Скрипт правит оставшиеся упоминания и затем
сканирует файл на все запрещённые идентификаторы (ключи, pageId, AB id, Jira).
"""
from pathlib import Path

F = Path("output/flow578_kb_v1_input/inventory_cleaned/inventory.yaml")
text = F.read_text()

REPL = [
    # T2-02: lineage на T1-05 — нейтрализуем, происхождение без ссылки на кейс
    (
        "iteration_of: T1-05 (развитие winback-линии)",
        "iteration_of: '[предшественник исключён из входа KB V1 по EXCLUSION_MANIFEST FLOW-575]'",
    ),
    # T2-0x winback: lineage на T1-06/T1-05; T1-08 разрешён (сожжённый IH-кейс)
    (
        "iteration_of: next steps T1-06 (UMN-9389) и T1-05/T1-08 линии («drop the trial, promote direct purchase»)",
        "iteration_of: 'next steps [кейсы исключены по EXCLUSION_MANIFEST FLOW-575] и линии T1-08 («drop the trial, promote direct purchase»)'",
    ),
    # lesson: пересказ урока T3-04 — вырезаем парентезу, свой вывод кейса остаётся
    (
        " (ср. T3-04: и удаление, и добавление планов\n      ломает баланс меню)",
        "",
    ),
    # transfer_bounds: «T1-06 iter2» фактически = T1-02 (iter 1–2, разрешён манифестом)
    (
        "(T1-06\n      iter2 — там позитив)",
        "(T1-02, iter 1–2 — там позитив)",
    ),
    (
        "Cross-flow подтверждение вывода T1-06 iter2 и T3-06:",
        "Cross-flow подтверждение вывода T1-02 (iter 1–2) и T3-06:",
    ),
    # пересказ урока T3-04 — вырезаем ссылку, собственное наблюдение кейса остаётся
    (
        "; choice overload повторяет урок T3-04.",
        "; choice overload подтверждается и здесь.",
    ),
]

for old, new in REPL:
    if old not in text:
        print(f"НЕ НАЙДЕНО (проверь вручную): {old[:60]!r}")
    text = text.replace(old, new)

F.write_text(text)

BANNED = [
    "T1-05", "T1-06", "T2-03", "T2-04", "T3-04", "T3-07",
    "714409638", "714432870", "746536863", "746543363", "787253507", "805316848",
    "6461", "6644", "6491", "6626", "6716", "6896", "6878", "6902", "7328", "7598",
    "UMN-9259", "UMN-9389", "UMN-10264", "UMN-10299", "UMN-9885", "UMI-92",
    "UMN-11436", "UMN-11941",
    # названия/биграммы holdout-кейсов
    "winback - interstitials", "offer instead of ad", "animation for XMAS",
    "Promo block", "checkout size", "two plans: trial",
]
hits = []
for token in BANNED:
    for i, line in enumerate(text.splitlines(), 1):
        if token in line:
            hits.append(f"  строка {i}: токен {token!r}")
if hits:
    print("ОСТАЛИСЬ запрещённые идентификаторы:")
    print("\n".join(hits))
else:
    print("Чисто: запрещённых идентификаторов в inventory.yaml не осталось.")

for name in ("summary_table.md", "README.md"):
    t = (F.parent / name).read_text()
    bad = [tok for tok in BANNED if tok in t]
    print(f"{name}: {'ОСТАЛИСЬ ' + str(bad) if bad else 'чисто'}")
