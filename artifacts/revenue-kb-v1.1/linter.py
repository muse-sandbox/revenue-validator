#!/usr/bin/env python3
"""Deterministic analog-card linter for Revenue Validator V1.1 (FLOW-586).

Machine check of a validator answer against the deterministic closeness model
of knowledge_base.md §2.2 and the strict card format of §2.4 (Evidence Policy
V1, level_computation + linter.hard_errors).

Usage:
    python3 linter.py <answer.md> --kb <knowledge_base.md> \
        --patterns <pattern_cards.md> [--no-kb-arm]

Exit code 0 = PASS (no hard errors), 1 = FAIL (answer invalid),
2 = usage/IO error. A JSON report is printed to stdout. The linter is fully
deterministic: stdlib only, no network, no clock, no randomness, and it reads
ONLY the files passed as arguments. It never prints the full answer text —
only extracted cards and errors.
"""

import argparse
import json
import re
import sys

AXES = [
    "flow_stage",
    "segment",
    "trigger_eligibility",
    "surface",
    "mechanism",
    "offer",
    "behavior",
    "metric",
    "money_chain",
    "guardrails",
]
MATCH3 = ("exact", "adjacent", "different")
MATCH2 = ("exact", "different")
LEVELS = ("L1", "L2", "L3")

# Enum-valued card fields outside `axes`.
ENUM_FIELDS = {
    "segment_monetization_state": MATCH2,
    "money_chain_link": MATCH2,
    "platform": MATCH3,
    "level": LEVELS,
}
REQUIRED_FIELDS = [
    "source",
    "axes",
    "segment_monetization_state",
    "money_chain_link",
    "platform",
    "level",
    "transferable",
    "not_transferable",
]

SOURCE_ID_RE = re.compile(r"\bT\d-\d{2}\b|\bP-\d{2}\b")
FENCE_RE = re.compile(r"^```")
SIDE_EFFECTS_RE = re.compile(r"non-monetization effects to instrument", re.IGNORECASE)
NO_DIRECT_ANALOGS_RE = re.compile(r"no direct analogs", re.IGNORECASE)

# Hard-error codes (generic; Evidence Policy V1 linter.hard_errors).
E_LEVEL_MISMATCH = "E_LEVEL_MISMATCH"          # claimed level != computed level
E_EMPTY_NOT_TRANSFERABLE = "E_EMPTY_NOT_TRANSFERABLE"
E_UNKNOWN_SOURCE_ID = "E_UNKNOWN_SOURCE_ID"    # source ID absent from KNOWLEDGE CONTEXT
E_CARD_PARSE = "E_CARD_PARSE"                  # card unparsable / missing fields or axes
E_MISSING_NO_DIRECT_ANALOGS = "E_MISSING_NO_DIRECT_ANALOGS"
E_MISSING_SIDE_EFFECTS = "E_MISSING_SIDE_EFFECTS"
E_CARD_IN_NO_KB_ARM = "E_CARD_IN_NO_KB_ARM"    # analog card emitted without a KB


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def extract_fenced_blocks(text):
    """Return the contents of all ``` fenced blocks, in document order."""
    blocks = []
    lines = text.splitlines()
    inside = False
    current = []
    for line in lines:
        if FENCE_RE.match(line.strip()):
            if inside:
                blocks.append("\n".join(current))
                current = []
                inside = False
            else:
                inside = True
            continue
        if inside:
            current.append(line)
    # An unterminated fence is treated as a block too (still deterministic).
    if inside and current:
        blocks.append("\n".join(current))
    return blocks


def is_analog_block(block):
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped == "analog:" or stripped.startswith("analog:")
    return False


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def parse_analog_card(block):
    """Parse one strict analog card (KB §2.4 subset of YAML).

    Returns (card_dict, errors). card_dict maps field -> scalar string or,
    for `axes`, a dict axis -> value-line. Prose fields (`transferable`,
    `not_transferable`, `sizing_prior`, `conflict`) collect their folded
    continuation lines.
    """
    errors = []
    card = {}
    lines = [ln for ln in block.splitlines()]
    # Locate the `analog:` root line.
    root_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "analog:" or ln.strip().startswith("analog:"):
            root_idx = i
            break
    if root_idx is None:
        return None, ["no `analog:` root key"]

    i = root_idx + 1
    current_field = None       # field currently collecting prose continuation
    in_axes = False
    axes_indent = None
    field_indent = None
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip():
            continue
        ind = indent_of(raw)
        stripped = raw.strip()
        if field_indent is None and stripped:
            field_indent = ind  # indentation level of top card fields
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(.*)$", stripped)
        if in_axes:
            if ind > (axes_indent if axes_indent is not None else 0) and m:
                axis = m.group(1)
                card["axes"][axis] = m.group(2).strip()
                continue
            in_axes = False  # fell out of the axes mapping
        if m and ind == field_indent:
            key = m.group(1)
            rest = m.group(2).strip()
            current_field = None
            if key == "axes":
                card["axes"] = {}
                in_axes = True
                axes_indent = ind
            else:
                card[key] = rest
                if rest in (">", "|", ">-", "|-", ""):
                    card[key] = ""
                    current_field = key
        elif current_field is not None and ind > field_indent:
            card[current_field] = (card[current_field] + " " + stripped).strip()
        elif m and field_indent is not None and ind > field_indent:
            # Nested mapping outside `axes` — tolerate but ignore.
            continue
        else:
            errors.append("unrecognized line in card: %r" % stripped[:80])
    return card, errors


def enum_value(raw):
    """First token of an enum-valued line; ` # rationale` comments allowed."""
    if raw is None:
        return None
    value = raw.split("#", 1)[0].strip()
    if not value:
        return None
    return value.split()[0]


def validate_card_structure(card, parse_errors):
    """Return list of E_CARD_PARSE reasons for missing/invalid fields."""
    reasons = list(parse_errors)
    for field in REQUIRED_FIELDS:
        if field not in card:
            reasons.append("missing required field: %s" % field)
    axes = card.get("axes")
    if isinstance(axes, dict):
        for axis in AXES:
            if axis not in axes:
                reasons.append("missing axis: %s" % axis)
            else:
                val = enum_value(axes[axis])
                if val not in MATCH3:
                    reasons.append(
                        "axis %s has invalid value %r (expected one of %s)"
                        % (axis, val, "/".join(MATCH3))
                    )
        for axis in sorted(axes):
            if axis not in AXES:
                reasons.append("unknown axis: %s" % axis)
    elif "axes" in card:
        reasons.append("`axes` is not a mapping")
    for field, allowed in ENUM_FIELDS.items():
        if field in card:
            val = enum_value(card[field])
            if val not in allowed:
                reasons.append(
                    "field %s has invalid value %r (expected one of %s)"
                    % (field, val, "/".join(allowed))
                )
    return reasons


def compute_level(card):
    """Deterministic level per KB §2.2 (L1 first, then L2 branches, else L3)."""
    axes = {a: enum_value(v) for a, v in card["axes"].items()}
    sms = enum_value(card["segment_monetization_state"])
    mcl = enum_value(card["money_chain_link"])
    platform = enum_value(card["platform"])

    l1 = (
        axes["mechanism"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["surface"] in ("exact", "adjacent")
        and sms == "exact"
        and mcl == "exact"
        and platform in ("exact", "adjacent")   # R1
    )
    if l1:
        return "L1"

    branch_a = axes["mechanism"] == "exact" and (
        axes["surface"] == "different" or axes["flow_stage"] == "different"
    )
    branch_b = (
        axes["surface"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["mechanism"] == "different"
    )
    branch_c = (
        axes["mechanism"] == "exact"
        and axes["flow_stage"] == "exact"
        and axes["surface"] in ("exact", "adjacent")
        and mcl == "exact"                      # R4
        and (
            sms == "different"                  # R2
            or axes["segment"] == "different"
            or platform == "different"
        )
    )
    if branch_a or branch_b or branch_c:
        return "L2"
    return "L3"


def collect_known_ids(kb_text, patterns_text):
    ids = set(SOURCE_ID_RE.findall(kb_text))
    ids.update(SOURCE_ID_RE.findall(patterns_text))
    return ids


def lint(answer_text, known_ids, no_kb_arm):
    report = {
        "mode": "no-kb-arm" if no_kb_arm else "kb-arm",
        "cards": [],
        "errors": [],
        "verdict": "PASS",
    }
    blocks = [b for b in extract_fenced_blocks(answer_text) if is_analog_block(b)]

    if no_kb_arm:
        if blocks:
            report["errors"].append({
                "code": E_CARD_IN_NO_KB_ARM,
                "detail": "%d analog card(s) emitted, but this arm has no "
                          "KNOWLEDGE CONTEXT — no cards may be emitted" % len(blocks),
            })
            report["cards"] = [
                {"index": i + 1, "checked": False} for i in range(len(blocks))
            ]
    else:
        computed_levels = []
        for i, block in enumerate(blocks):
            entry = {
                "index": i + 1,
                "source_id": None,
                "claimed_level": None,
                "computed_level": None,
                "card_errors": [],
            }
            card, parse_errors = parse_analog_card(block)
            if card is None:
                entry["card_errors"].append(
                    {"code": E_CARD_PARSE, "detail": "; ".join(parse_errors)}
                )
                report["cards"].append(entry)
                continue
            structure_reasons = validate_card_structure(card, parse_errors)
            source_raw = card.get("source", "")
            m = SOURCE_ID_RE.search(source_raw or "")
            if m:
                entry["source_id"] = m.group(0)
            if structure_reasons:
                entry["card_errors"].append(
                    {"code": E_CARD_PARSE, "detail": "; ".join(structure_reasons)}
                )
            else:
                entry["claimed_level"] = enum_value(card["level"])
                entry["computed_level"] = compute_level(card)
                computed_levels.append(entry["computed_level"])
                if entry["claimed_level"] != entry["computed_level"]:
                    entry["card_errors"].append({
                        "code": E_LEVEL_MISMATCH,
                        "detail": "claimed %s but axes compute %s"
                                  % (entry["claimed_level"], entry["computed_level"]),
                    })
                nt = card.get("not_transferable", "")
                if not nt or not nt.strip():
                    entry["card_errors"].append({
                        "code": E_EMPTY_NOT_TRANSFERABLE,
                        "detail": "not_transferable is empty",
                    })
            if "source" in card:
                if entry["source_id"] is None:
                    entry["card_errors"].append({
                        "code": E_UNKNOWN_SOURCE_ID,
                        "detail": "no source ID (T*-** / P-**) found in `source`",
                    })
                elif entry["source_id"] not in known_ids:
                    entry["card_errors"].append({
                        "code": E_UNKNOWN_SOURCE_ID,
                        "detail": "source ID %s does not exist in KNOWLEDGE "
                                  "CONTEXT" % entry["source_id"],
                    })
            report["cards"].append(entry)

        has_l1_l2 = any(lv in ("L1", "L2") for lv in computed_levels)
        any_parse_error = any(
            e["code"] == E_CARD_PARSE
            for c in report["cards"]
            for e in c.get("card_errors", [])
        )
        # With an unparsable card the L1/L2-emptiness is undetermined and the
        # parse error already invalidates the answer, so the no-direct-analogs
        # rule is checked only over successfully computed levels.
        if not has_l1_l2 and not any_parse_error:
            # All cards L3 (or no cards): the literal line is mandatory.
            if not NO_DIRECT_ANALOGS_RE.search(answer_text):
                report["errors"].append({
                    "code": E_MISSING_NO_DIRECT_ANALOGS,
                    "detail": "no card computes to L1/L2, but the mandatory "
                              "line 'no direct analogs' is absent",
                })

    if not SIDE_EFFECTS_RE.search(answer_text):
        report["errors"].append({
            "code": E_MISSING_SIDE_EFFECTS,
            "detail": "mandatory section 'Non-monetization effects to "
                      "instrument' is absent",
        })

    any_card_error = any(e for c in report["cards"] for e in c.get("card_errors", []))
    if report["errors"] or any_card_error:
        report["verdict"] = "FAIL"
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("answer", help="path to the validator answer (.md)")
    parser.add_argument("--kb", required=True, help="path to knowledge_base.md")
    parser.add_argument("--patterns", required=True, help="path to pattern_cards.md")
    parser.add_argument(
        "--no-kb-arm",
        action="store_true",
        help="arm without KNOWLEDGE CONTEXT: cards must not be emitted; "
             "card-level checks are skipped",
    )
    args = parser.parse_args(argv)

    try:
        answer_text = read_text(args.answer)
        kb_text = read_text(args.kb)
        patterns_text = read_text(args.patterns)
    except OSError as exc:
        print(json.dumps({"error": str(exc)}, sort_keys=True))
        return 2

    known_ids = collect_known_ids(kb_text, patterns_text)
    report = lint(answer_text, known_ids, args.no_kb_arm)
    report["files"] = {
        "answer": args.answer,
        "kb": args.kb,
        "patterns": args.patterns,
    }
    report["known_source_ids_count"] = len(known_ids)
    print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
