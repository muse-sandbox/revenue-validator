#!/usr/bin/env python3
"""Deterministic answer linter for Revenue Validator V1.2 (FLOW-593).

Machine check of a validator answer against

  * the deterministic closeness model of knowledge_base.md §2.2 and the
    strict card format of §2.4 (Evidence Policy V1, level_computation +
    linter.hard_errors) — unchanged from V1.1; and
  * the scope rules for corpus-level generalizations of §2.5, using the
    machine-readable generalization classes of §2.6 (new in V1.2).

Usage:
    python3 linter.py <answer.md> --kb <knowledge_base.md> \
        --patterns <pattern_cards.md> [--no-kb-arm]

Exit code 0 = PASS (no hard errors), 1 = FAIL (answer invalid),
2 = usage/IO error. A JSON report is printed to stdout. The linter is fully
deterministic: stdlib only, no network, no clock, no randomness, and it reads
ONLY the files passed as arguments. It never prints the full answer text —
only extracted cards, flagged-sentence excerpts (<= 160 chars) and errors.
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

# --- V1.2 hard-error codes (KB §2.5, generic; no case-specific tuning) -----
E_UNQUALIFIED_UNIVERSAL = "E_UNQUALIFIED_UNIVERSAL"        # G1/G2
E_SCOPE_ANNOTATION_MALFORMED = "E_SCOPE_ANNOTATION_MALFORMED"
E_SCOPE_UNKNOWN_ID = "E_SCOPE_UNKNOWN_ID"
E_UNIVERSAL_CONTRADICTS_SOURCE = "E_UNIVERSAL_CONTRADICTS_SOURCE"  # G3

# --- V1.2 lexicons (normative copy of knowledge_base.md §2.5) --------------
CORPUS_SCOPE_MARKERS = (
    "this corpus",
    "the corpus",
    "our corpus",
    "corpus-wide",
    "this knowledge base",
    "the knowledge base",
    "this evidence base",
    "the evidence base",
    "the knowledge context",
    "the reviewed cases",
    "the cases reviewed",
    "the cited cases",
    "the source cases",
    "past experiments",
    "prior experiments",
    "historical cases",
)
UNIVERSAL_MARKERS_NEGATIVE = (
    "never", "none", "nothing", "nowhere", "not a single", "at no point",
    "no case", "no experiment", "no source", "no iteration", "no evidence",
    "has not", "have not", "had not", "hasn't", "haven't", "does not",
    "do not", "did not", "doesn't", "don't", "is not", "are not", "was not",
    "were not", "cannot", "can't", "failed to", "fails to",
)
UNIVERSAL_MARKERS_POSITIVE = (
    "always", "every", "all", "any", "universally", "invariably",
    "without exception", "in all cases", "only ever",
)

# Retrieval statements about analog availability are not product
# generalizations (KB §2.5 exemption b).
NO_ANALOG_EXEMPT_RE = re.compile(r"\bno\s+(?:\w+\s+)?analogs?\b", re.IGNORECASE)
SCOPE_ANNOTATION_RE = re.compile(r"\[scope:[^\]]*\]", re.IGNORECASE | re.DOTALL)
SCOPE_INNER_RE = re.compile(
    r"^\s*(?P<sub>[^;]+?)\s*;\s*ids\s*:\s*(?P<ids>[^;]+?)\s*;"
    r"\s*not\s+covered\s*:\s*(?P<nc>.+?)\s*$",
    re.IGNORECASE | re.DOTALL,
)
STRICT_SOURCE_ID_RE = re.compile(r"^(?:T\d-\d{2}|P-\d{2})$")
EVIDENCE_MIXED_RE = re.compile(r"evidence is mixed", re.IGNORECASE)
GEN_CLASS_HEAD_RE = re.compile(r"^generalization_class:\s*(\S+)\s*$")
GEN_CLASS_FIELD_RE = re.compile(r"^\s+([a-z_]+):\s*(.*)$")
BULLET_SPLIT_RE = re.compile(r"\n(?=\s*(?:[-*+]\s|\d+[.)]\s|#{1,6}\s))")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
EXCERPT_LEN = 160


def _marker_re(marker):
    return re.compile(r"(?<!\w)" + re.escape(marker) + r"(?!\w)", re.IGNORECASE)


CORPUS_MARKER_RES = tuple((m, _marker_re(m)) for m in CORPUS_SCOPE_MARKERS)
NEG_MARKER_RES = tuple((m, _marker_re(m)) for m in UNIVERSAL_MARKERS_NEGATIVE)
POS_MARKER_RES = tuple((m, _marker_re(m)) for m in UNIVERSAL_MARKERS_POSITIVE)


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


# ---------------------------------------------------------------------------
# V1.2: corpus-level generalizations (KB §2.5) over the classes of KB §2.6
# ---------------------------------------------------------------------------

def parse_generalization_classes(kb_text):
    """Parse the §2.6 blocks. Returns a list of dicts, in document order.

    Grammar (inside a fenced block, exactly as written in the KB):

        generalization_class: GC-01
          label: <free text>
          keywords: <comma-separated substrings>
          outcome_positive: <comma-separated source IDs>
          outcome_negative: <comma-separated source IDs>

    A KB without such blocks simply yields no classes and the contradiction
    check never fires (this is what keeps V1.1 fixtures behaving as in V1.1).
    """
    classes = []
    current = None
    for block in extract_fenced_blocks(kb_text):
        for line in block.splitlines():
            head = GEN_CLASS_HEAD_RE.match(line.strip()) if line.strip() else None
            if head and line[:1] not in (" ", "\t"):
                current = {
                    "class_id": head.group(1),
                    "label": "",
                    "keywords": [],
                    "outcome_positive": [],
                    "outcome_negative": [],
                }
                classes.append(current)
                continue
            if current is None:
                continue
            field = GEN_CLASS_FIELD_RE.match(line)
            if not field:
                if line.strip():
                    current = None      # block ended / unrelated content
                continue
            key, value = field.group(1), field.group(2).strip()
            if key == "label":
                current["label"] = value
            elif key == "keywords":
                current["keywords"] = [
                    k.strip().lower() for k in value.split(",") if k.strip()
                ]
            elif key in ("outcome_positive", "outcome_negative"):
                current[key] = [k.strip() for k in value.split(",") if k.strip()]
        current = None
    return classes


def strip_fenced_blocks(text):
    """Answer prose: every fenced block replaced by a paragraph break."""
    out = []
    inside = False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            inside = not inside
            out.append("")
            continue
        out.append("" if inside else line)
    return "\n".join(out)


def normalize_scan_text(text):
    """Whitespace-collapsed, ASCII-apostrophe copy used for marker matching."""
    return " ".join(text.replace("’", "'").split())


def split_paragraphs(prose):
    return [p for p in re.split(r"\n\s*\n", prose) if p.strip()]


def split_sentences(paragraph):
    """Deterministic sentence split; `[scope: …]` annotations are protected."""
    annotations = SCOPE_ANNOTATION_RE.findall(paragraph)
    protected = paragraph
    for i, ann in enumerate(annotations):
        protected = protected.replace(ann, "\x00A%d\x00" % i, 1)
    sentences = []
    for chunk in BULLET_SPLIT_RE.split(protected):
        for sentence in SENTENCE_SPLIT_RE.split(chunk):
            if sentence.strip():
                sentences.append(sentence)
    restored = []
    for sentence in sentences:
        for i, ann in enumerate(annotations):
            sentence = sentence.replace("\x00A%d\x00" % i, ann)
        restored.append(sentence)
    return restored


def matched_markers(scan_text, marker_res):
    return [m for m, rx in marker_res if rx.search(scan_text)]


def validate_scope_annotation(raw, known_ids):
    """Return (parsed_or_None, errors) for one `[scope: …]` annotation."""
    inner = raw[raw.index(":") + 1:-1]
    match = SCOPE_INNER_RE.match(inner)
    if not match:
        return None, [{
            "code": E_SCOPE_ANNOTATION_MALFORMED,
            "detail": "expected `[scope: <sub-class>; ids: <ID>[, <ID>…]; "
                      "not covered: <text>]`, got %r"
                      % normalize_scan_text(raw)[:EXCERPT_LEN],
        }]
    errors = []
    sub = normalize_scan_text(match.group("sub"))
    not_covered = normalize_scan_text(match.group("nc"))
    ids = [i.strip() for i in match.group("ids").split(",") if i.strip()]
    if not sub:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty <sub-class>"})
    if not not_covered:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty `not covered:` part"})
    if not ids:
        errors.append({"code": E_SCOPE_ANNOTATION_MALFORMED,
                       "detail": "empty `ids:` list"})
    for source_id in ids:
        if not STRICT_SOURCE_ID_RE.match(source_id):
            errors.append({
                "code": E_SCOPE_ANNOTATION_MALFORMED,
                "detail": "%r is not a source ID (T*-** / P-**)" % source_id,
            })
        elif source_id not in known_ids:
            errors.append({
                "code": E_SCOPE_UNKNOWN_ID,
                "detail": "scope ID %s does not exist in KNOWLEDGE CONTEXT"
                          % source_id,
            })
    parsed = {
        "sub_class": sub,
        "ids": ids,
        "not_covered": not_covered,
        "excluded_ids": sorted(set(SOURCE_ID_RE.findall(match.group("nc")))),
    }
    return parsed, errors


def check_generalizations(answer_text, known_ids, gen_classes):
    """KB §2.5 G1–G3. Returns a list of report entries (each with `errors`)."""
    entries = []
    cited_ids = set(SOURCE_ID_RE.findall(answer_text))
    prose = strip_fenced_blocks(answer_text)
    index = 0
    for p_index, paragraph in enumerate(split_paragraphs(prose)):
        paragraph_has_mixed = bool(
            EVIDENCE_MIXED_RE.search(normalize_scan_text(paragraph))
        )
        for sentence in split_sentences(paragraph):
            annotations_raw = SCOPE_ANNOTATION_RE.findall(sentence)
            errors = []
            parsed_annotations = []
            for raw in annotations_raw:
                parsed, ann_errors = validate_scope_annotation(raw, known_ids)
                errors.extend(ann_errors)
                if parsed is not None:
                    parsed_annotations.append(parsed)
            # Detection runs on the sentence WITHOUT annotations and without
            # the analog-availability exemption (KB §2.5 exemptions b, c).
            scan_source = SCOPE_ANNOTATION_RE.sub(" ", sentence)
            scan_source = NO_ANALOG_EXEMPT_RE.sub(" ", scan_source)
            scan_text = normalize_scan_text(scan_source)
            corpus_hits = matched_markers(scan_text, CORPUS_MARKER_RES)
            neg_hits = matched_markers(scan_text, NEG_MARKER_RES)
            pos_hits = matched_markers(scan_text, POS_MARKER_RES)
            flagged = bool(corpus_hits) and bool(neg_hits or pos_hits)
            if not flagged:
                if errors:      # a voluntary annotation must still be valid
                    index += 1
                    entries.append({
                        "index": index,
                        "paragraph": p_index + 1,
                        "flagged": False,
                        "polarity": None,
                        "classes": [],
                        "annotations": len(annotations_raw),
                        "excerpt": scan_text[:EXCERPT_LEN],
                        "errors": errors,
                    })
                continue
            index += 1
            polarity = "negative" if neg_hits else "positive"
            if not annotations_raw:
                errors.append({
                    "code": E_UNQUALIFIED_UNIVERSAL,
                    "detail": "corpus-scoped universal without a [scope: …] "
                              "annotation (corpus markers %s; universal "
                              "markers %s)"
                              % (sorted(corpus_hits),
                                 sorted(neg_hits + pos_hits)),
                })
            excluded = set()
            for parsed in parsed_annotations:
                excluded.update(parsed["excluded_ids"])
            hit_classes = []
            for gen_class in gen_classes:
                if not any(k in scan_text.lower() for k in gen_class["keywords"]):
                    continue
                counter_field = ("outcome_positive" if polarity == "negative"
                                 else "outcome_negative")
                counters = sorted(
                    set(gen_class[counter_field]) & cited_ids - excluded
                )
                hit_classes.append({
                    "class_id": gen_class["class_id"],
                    "counter_ids": counters,
                })
                if counters and not paragraph_has_mixed:
                    errors.append({
                        "code": E_UNIVERSAL_CONTRADICTS_SOURCE,
                        "detail": "%s universal over class %s, but the answer "
                                  "cites opposite-direction source(s) %s that "
                                  "the declared scope does not exclude; the "
                                  "paragraph must contain the literal "
                                  "'evidence is mixed'"
                                  % (polarity, gen_class["class_id"],
                                     ", ".join(counters)),
                    })
            entries.append({
                "index": index,
                "paragraph": p_index + 1,
                "flagged": True,
                "polarity": polarity,
                "classes": hit_classes,
                "annotations": len(annotations_raw),
                "excerpt": scan_text[:EXCERPT_LEN],
                "errors": errors,
            })
    return entries


def lint(answer_text, known_ids, no_kb_arm, gen_classes=()):
    report = {
        "mode": "no-kb-arm" if no_kb_arm else "kb-arm",
        "cards": [],
        "generalizations": [],
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

    # V1.2 (KB §2.5): scope/qualifier rules for corpus-level generalizations.
    # Applied in both arms — they constrain the answer's prose, not the cards.
    report["generalizations"] = check_generalizations(
        answer_text, known_ids, list(gen_classes)
    )

    any_card_error = any(e for c in report["cards"] for e in c.get("card_errors", []))
    any_gen_error = any(
        e for g in report["generalizations"] for e in g.get("errors", [])
    )
    if report["errors"] or any_card_error or any_gen_error:
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
    gen_classes = parse_generalization_classes(kb_text)
    report = lint(answer_text, known_ids, args.no_kb_arm, gen_classes)
    report["files"] = {
        "answer": args.answer,
        "kb": args.kb,
        "patterns": args.patterns,
    }
    report["known_source_ids_count"] = len(known_ids)
    report["generalization_classes"] = [c["class_id"] for c in gen_classes]
    print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
