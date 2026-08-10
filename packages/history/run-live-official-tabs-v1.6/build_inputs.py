#!/usr/bin/env python3
"""Assemble the arm-A / arm-B inference inputs for the V1.6 trial run.

Deterministic, stdlib only. The experiment card is lifted verbatim from the
V1.2 trial run (`../trial-run-815603314/inputs/arm-a.md`) — the same source
the V1.3 runs used — so that the only difference between the V1.5 and V1.6
runs is the validator bundle.

Besides the two arm inputs this writes `inputs/experiment_card.md`: the card
alone, byte-identical to the copy embedded in both arm inputs. The V1.6
linter needs it to check the provenance of the numbers inside `[computed]`
statements (KB §2.8).

  python3 build_inputs.py
"""

import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "inputs")
BUNDLE = os.path.normpath(os.path.join(HERE, "..", "revenue-kb-v1.6"))
PREV = os.path.normpath(os.path.join(HERE, "..", "trial-run-815603314"))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def prompt_body():
    """The PROMPT section of the frozen prompt file (header/notes stripped)."""
    text = read(os.path.join(BUNDLE, "validator_prompt_v1_6.md"))
    marker = "## PROMPT\n"
    body = text.split(marker, 1)[1]
    return body.lstrip("\n")


def experiment_card():
    prev = read(os.path.join(PREV, "inputs", "arm-a.md"))
    start = prev.index("<experiment-card>") + len("<experiment-card>\n")
    end = prev.index("</experiment-card>")
    return prev[start:end]


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
        digest = write(os.path.join(OUT, arm + ".md"), text)
        print("%s  %s (%d bytes)" % (digest, arm + ".md",
                                     len(text.encode("utf-8"))))
    digest = write(os.path.join(OUT, "experiment_card.md"), card)
    print("%s  experiment_card.md (%d bytes)"
          % (digest, len(card.encode("utf-8"))))
    print("%s  KNOWLEDGE_CONTEXT (%d bytes)"
          % (hashlib.sha256(kc.encode("utf-8")).hexdigest(),
             len(kc.encode("utf-8"))))


if __name__ == "__main__":
    main()
