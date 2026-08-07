#!/usr/bin/env python3
"""FLOW-578: подготовка очищенного входного inventory для KB V1 builder.

По EXCLUSION_MANIFEST.md (FLOW-575) записи T1-05, T1-06, T2-03, T2-04,
T3-04, T3-07 должны быть удалены из inventory FLOW-577 ДО того, как builder
прочитает их содержимое. Скрипт копирует inventory в рабочий каталог,
вырезает эти записи из inventory.yaml, summary_table.md и README.md и
печатает только счётчики/версию — никакого содержимого удаляемых записей.
"""
import re
import sys
from pathlib import Path

HOLDOUT_KEYS = ["T1-05", "T1-06", "T2-03", "T2-04", "T3-04", "T3-07"]

SRC = Path(
    "/Users/elzira/orca/workspaces/claude-ug-manipulator/"
    "flow-577-04-revenue-flow-2/output/flow577_revenue_inventory"
)
DST = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "output/flow578_kb_v1_input/inventory_cleaned"
)
DST.mkdir(parents=True, exist_ok=True)


def strip_yaml(text: str) -> tuple[str, int, int]:
    """Удаляет из experiments записи с holdout-ключом (парсинг yaml, дамп без изменений остальных)."""
    import yaml

    data = yaml.safe_load(text)
    exps = data["experiments"]
    total = len(exps)
    data["experiments"] = [e for e in exps if e.get("key") not in HOLDOUT_KEYS]
    removed = total - len(data["experiments"])
    return (
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100),
        removed,
        total,
    )


def strip_md(text: str) -> tuple[str, int]:
    """Удаляет строки таблиц/списков и секции-заголовки, содержащие holdout-ключ."""
    out, removed = [], 0
    for line in text.splitlines(keepends=True):
        if any(k in line for k in HOLDOUT_KEYS):
            removed += 1
            continue
        out.append(line)
    return "".join(out), removed


yaml_text = (SRC / "inventory.yaml").read_text()
clean_yaml, n_removed, n_total = strip_yaml(yaml_text)
# защита: ни один ключ не должен остаться
leftover = [k for k in HOLDOUT_KEYS if k in clean_yaml]
(DST / "inventory.yaml").write_text(clean_yaml)

report = [f"inventory.yaml: всего записей {n_total}, удалено {n_removed}, осталось {n_total - n_removed}"]
if leftover:
    report.append(f"ВНИМАНИЕ: ключи всё ещё упоминаются в yaml: {leftover} — нужна ручная зачистка")

for name in ("summary_table.md", "README.md"):
    text = (SRC / name).read_text()
    clean, removed = strip_md(text)
    left = [k for k in HOLDOUT_KEYS if k in clean]
    (DST / name).write_text(clean)
    report.append(f"{name}: удалено строк {removed}" + (f"; ОСТАЛИСЬ упоминания {left}" if left else ""))

ver = re.search(r"(?im)^.*(V0\.\d|версия[^\n]*).*$", (SRC / "README.md").read_text())
report.append(f"README версия (строка): {ver.group(0).strip() if ver else 'не найдена'}")
print("\n".join(report))
