#!/usr/bin/env python3
"""Assemble the arm-B inference input for the V1.6 run on page 828875488.

Deterministic, stdlib only. The experiment card is the plain text of Confluence
page 828875488 (space CRO, version 10), extracted with the Confluence tool's
`scripts/extract_text.py` and prefixed with the two-line provenance header used
by every earlier live run.

Only arm B (validator with the knowledge base) is built: this run reviews a live
hypothesis, it does not A/B the validator itself.

  python3 build_inputs.py path/to/card_raw.md
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "inputs")
BUNDLE = os.path.normpath(os.path.join(HERE, "..", "revenue-kb-v1.6"))

TITLE = ("[2026-08-10] UG iOS: Paywall — Premium tab by default "
         "for top propensity decile [2026-XX-XX]")
SOURCE = "Confluence page 828875488, version 10, space CRO"


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def prompt_body():
    """The PROMPT section of the frozen prompt file (header/notes stripped)."""
    text = read(os.path.join(BUNDLE, "validator_prompt_v1_6.md"))
    return text.split("## PROMPT\n", 1)[1].lstrip("\n")


def experiment_card(raw_path):
    body = read(raw_path).strip()
    return ("# EXPERIMENT CARD — %s\n# Source: %s\n\n%s\n"
            % (TITLE, SOURCE, body))


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    raw_path = sys.argv[1]
    body = prompt_body()
    kc = (read(os.path.join(BUNDLE, "knowledge_base.md"))
          + "\n\n---\n\n"
          + read(os.path.join(BUNDLE, "pattern_cards.md")))
    card = experiment_card(raw_path)

    os.makedirs(OUT, exist_ok=True)
    text = body.replace("{KNOWLEDGE_CONTEXT}", kc).replace(
        "{EXPERIMENT_CARD}", card)
    digest = write(os.path.join(OUT, "arm-b.md"), text)
    print("%s  arm-b.md (%d bytes)" % (digest, len(text.encode("utf-8"))))
    digest = write(os.path.join(OUT, "experiment_card.md"), card)
    print("%s  experiment_card.md (%d bytes)"
          % (digest, len(card.encode("utf-8"))))
    print("%s  KNOWLEDGE_CONTEXT (%d bytes)"
          % (hashlib.sha256(kc.encode("utf-8")).hexdigest(),
             len(kc.encode("utf-8"))))


if __name__ == "__main__":
    main()
