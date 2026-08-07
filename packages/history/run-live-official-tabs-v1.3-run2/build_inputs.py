#!/usr/bin/env python3
"""Assemble the arm-A / arm-B inference inputs for the V1.3 trial re-run.

Deterministic, stdlib only. The experiment card is lifted verbatim from the
V1.2 trial run (`../trial-run-815603314/inputs/arm-a.md`) so that the only
difference between the two runs is the validator bundle.

  python3 build_inputs.py
"""

import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "inputs")
BUNDLE = os.path.normpath(os.path.join(HERE, "..", "revenue-kb-v1.3"))
PREV = os.path.normpath(os.path.join(HERE, "..", "trial-run-815603314"))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def prompt_body():
    """The PROMPT section of the frozen prompt file (header/notes stripped)."""
    text = read(os.path.join(BUNDLE, "validator_prompt_v1_3.md"))
    marker = "## PROMPT\n"
    body = text.split(marker, 1)[1]
    return body.lstrip("\n")


def experiment_card():
    prev = read(os.path.join(PREV, "inputs", "arm-a.md"))
    start = prev.index("<experiment-card>") + len("<experiment-card>\n")
    end = prev.index("</experiment-card>")
    return prev[start:end]


def main():
    body = prompt_body()
    kc = (read(os.path.join(BUNDLE, "knowledge_base.md"))
          + "\n\n---\n\n"
          + read(os.path.join(BUNDLE, "pattern_cards.md")))
    card = experiment_card()

    os.makedirs(OUT, exist_ok=True)
    for arm, knowledge in (("arm-a", ""), ("arm-b", kc)):
        text = body.replace("{KNOWLEDGE_CONTEXT}", knowledge)
        text = text.replace("{EXPERIMENT_CARD}", card)
        path = os.path.join(OUT, arm + ".md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        print("%s  %s (%d bytes)" % (digest, arm + ".md",
                                     len(text.encode("utf-8"))))
    print("%s  KNOWLEDGE_CONTEXT (%d bytes)"
          % (hashlib.sha256(kc.encode("utf-8")).hexdigest(),
             len(kc.encode("utf-8"))))


if __name__ == "__main__":
    main()
