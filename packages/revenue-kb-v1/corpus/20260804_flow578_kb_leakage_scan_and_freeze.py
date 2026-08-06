#!/usr/bin/env python3
"""FLOW-578: leakage-скан бандла revenue-kb-v1 и генерация SHA-256 для FREEZE_MANIFEST.

Сканирует все файлы бандла на запрещённые идентификаторы holdout-кейсов
(EXCLUSION_MANIFEST FLOW-575): ключи, pageId, AB id, Jira, биграммы названий.
AB id проверяются как отдельные токены (не подстроки), чтобы не ловить
легитимные id вроде 6461 внутри других чисел. Затем печатает SHA-256 файлов.
"""
import hashlib
import re
from pathlib import Path

BUNDLE = Path(
    "/Users/elzira/Documents/Codex/2026-08-03/"
    "users-elzira-obsidian-ug-ai-infrastructure/outputs/revenue-kb-v1"
)

KEYS = ["T1-05", "T1-06", "T2-03", "T2-04", "T3-04", "T3-07"]
PAGE_IDS = ["714409638", "714432870", "746536863", "746543363", "787253507", "805316848"]
AB_IDS = ["6461", "6644", "6491", "6626", "6716", "6896", "6878", "6902", "7328", "7598"]
JIRA = ["UMN-9259", "UMN-9389", "UMN-10264", "UMN-10299", "UMN-9885", "UMI-92", "UMN-11436", "UMN-11941"]
BIGRAMS = [
    "winback - interstitials",
    "animation for XMAS",
    "Promo block",
    "checkout size",
    "two plans: trial",
]
# 'offer instead of ad' допустим ТОЛЬКО в контексте iter 1–2 (T1-02, разрешён манифестом)
CONDITIONAL = ["offer instead of ad"]

hits = []
files = sorted(p for p in BUNDLE.rglob("*") if p.is_file())
for f in files:
    text = f.read_text(errors="replace")
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for tok in KEYS + PAGE_IDS + JIRA + BIGRAMS:
            if tok in line:
                hits.append((f.name, i, tok, "BANNED"))
        for tok in AB_IDS:
            if re.search(rf"(?<![\d]){tok}(?![\d])", line):
                hits.append((f.name, i, tok, "BANNED-ABID"))
        for tok in CONDITIONAL:
            if tok in line and "iter 1–2" not in line and "iter 1-2" not in line:
                hits.append((f.name, i, tok, "CONDITIONAL-CHECK"))

if hits:
    print("НАЙДЕНЫ упоминания:")
    for f, i, tok, kind in hits:
        print(f"  [{kind}] {f}:{i} — {tok!r}")
else:
    print("LEAKAGE SCAN: PASS — запрещённых идентификаторов в бандле нет.")

print("\nSHA-256:")
for f in files:
    if f.name == "FREEZE_MANIFEST.md":
        continue
    digest = hashlib.sha256(f.read_bytes()).hexdigest()
    print(f"{digest}  {f.relative_to(BUNDLE)}")
