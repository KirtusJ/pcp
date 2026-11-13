#!/usr/bin/env python3
"""ACR local reference tool: fetch exact text instead of holding all of it in context.

Read-only and standard library only. It looks up clauses, searches the sources,
looks up defined terms, parses the optional command profile and checks the shape
of a fidelity record. It authenticates nothing, decides nothing and grants no
permission. Run `python3 acr.py --help`.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMPONENT_RE = re.compile(r"^\*\*Component:\*\* `(acr\.[a-z_]+)`, Version (\S+)", re.M)
VERSION_OK = re.compile(r"[0-9][0-9A-Za-z.+-]{0,63}")


def header(text):
    """(identifier, version) from the component line in a Specification's first 60 lines, or None.
    The version is the whole field as written, so that 1.0.1 and 2.4.1-rc.2 are not read as shorter ones."""
    m = COMPONENT_RE.search("\n".join(text.splitlines()[:60]))
    if not m:
        return None
    version = m.group(2).rstrip(".,;")
    return (m.group(1), version) if VERSION_OK.fullmatch(version) else None


def discover(root=ROOT, ambiguous=None):
    """The modules of a packet, read from the header of each Specification under MODULES, in folder order.
    Adding a module is adding a folder: nothing here lists them. An identifier that two folders declare is
    served from neither, because which text applies must never depend on the order of folder names; the
    folders are put in `ambiguous` under the module's key."""
    out, twice = {}, {}
    for spec in sorted((Path(root) / "MODULES").glob("*/SOURCE/Specification.md")):
        h = header(spec.read_text(encoding="utf-8"))
        if not h:
            continue
        key, rel = h[0][4:], spec.relative_to(root).as_posix()
        if key in twice:
            twice[key].append(rel)
        elif key in out:
            twice[key] = [out.pop(key)[1], rel]
        else:
            out[key] = (h[0], rel)
    if ambiguous is not None:
        ambiguous.update(twice)
    return out


AMBIGUOUS = {}
COMPONENTS = discover(ambiguous=AMBIGUOUS)
CONDITIONAL = {
    "command_interface": "SUPPLEMENTS/Core_Conditional/Command_Interface.md",
    "methods": "SUPPLEMENTS/Core_Conditional/Methods_Catalog.md",
    "records": "SUPPLEMENTS/Core_Conditional/Record_Contracts.md",
}
ALIASES = {"qa": "quality_assurance", "math": "mathematics", "maths": "mathematics", "stats": "statistics",
           "crypto": "cryptography", "eng": "engineering", "sci": "science"}
H2 = re.compile(r"^## (?:(\d+)\. (.+)|Appendix ([A-Z])\. (.+)|(.+))$")
H3 = re.compile(r"^### (\d+\.\d+) (.+)$")
NUMBERED = re.compile(r"^(\d+\.\d+)\. (.+)$")
FIDELITY = {
    "delivery": ("ABSORBED_TEXT", "RETRIEVAL", "TOOL_ASSISTED", "HOST_ENFORCED", "UNKNOWN"),
    "grounding": ("EXTERNAL_INSPECTED", "SUPPLIED_ONLY", "RECALL_ONLY", "NONE", "UNKNOWN"),
    "execution": ("EXECUTED", "REASONED", "UNKNOWN"),
    "observability": ("INSPECTABLE", "BLACK_BOX", "UNKNOWN"),
}
REASONING_TRACE = ("FULL", "SUMMARY", "NONE", "UNKNOWN")   # optional: what the host exposes of the participant's reasoning
DISPOSITIONS = ("SUPPORTED_IN_SCOPE", "CONDITIONAL", "REFUTED_IN_SCOPE", "NOT_IDENTIFIED_IN_SCOPE",
                "DISPUTED", "UNRESOLVED", "INCOMPARABLE")


class AcrError(ValueError):
    pass


def component_key(name):
    key = name.strip().lower().replace("-", "_").replace(" ", "_")
    key = key[4:] if key.startswith("acr.") else key
    key = ALIASES.get(key, key)
    if key in AMBIGUOUS:
        raise AcrError("%r is declared by more than one folder (%s); the identifier is ambiguous and none of them is used"
                       % (name, ", ".join(AMBIGUOUS[key])))
    if key not in COMPONENTS and key not in CONDITIONAL:
        raise AcrError("unknown component %r; use one of: %s" % (name, ", ".join(list(COMPONENTS) + list(CONDITIONAL))))
    return key


def source_path(key, root=ROOT):
    return root / (COMPONENTS[key][1] if key in COMPONENTS else CONDITIONAL[key])


def read_source(key, root=ROOT):
    return source_path(key, root).read_text(encoding="utf-8")


def version_of(text):
    """Component version stated in the document's front matter, or None."""
    h = header(text)
    return h[1] if h else None


def identity(key, root=ROOT):
    """Exact identity of a component's Specification: id, version and SHA-256 of its bytes."""
    data = source_path(key, root).read_bytes()
    return COMPONENTS[key][0], version_of(data.decode("utf-8")), hashlib.sha256(data).hexdigest()


def index_source(text):
    """Return [(provision, title_or_excerpt, level, start_line, end_line)] in source order.

    HEADING rows are level-2 and level-3 headings; NUMBERED_REQUIREMENT rows are
    paragraphs that begin 'N.M. '. End lines are exclusive.
    """
    lines = text.splitlines()
    marks = []
    for i, line in enumerate(lines):
        m = H2.match(line)
        if m:
            if m.group(1):
                marks.append((m.group(1), m.group(2).strip(), "HEADING", i, 2))
            elif m.group(3):
                marks.append(("Appendix " + m.group(3), m.group(4).strip(), "HEADING", i, 2))
            else:
                marks.append(("SECTION", m.group(5).strip(), "HEADING", i, 2))
            continue
        m = H3.match(line)
        if m:
            marks.append((m.group(1), m.group(2).strip(), "HEADING", i, 3))
            continue
        m = NUMBERED.match(line)
        if m:
            marks.append((m.group(1), m.group(2).strip()[:190], "NUMBERED_REQUIREMENT", i, 4))
    rows = []
    for n, (prov, title, level, start, depth) in enumerate(marks):
        end = len(lines)
        for later in marks[n + 1:]:
            if later[4] <= depth:
                end = later[3]
                break
        rows.append((prov, title, level, start, end))
    return rows


def build_index(root=ROOT):
    out = []
    for key, (cid, rel) in COMPONENTS.items():
        data = (root / rel).read_bytes()
        text = data.decode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        version = version_of(text)
        for prov, title, level, _s, _e in index_source(text):
            out.append((cid, version, prov, title, level, "INDEXED_NOT_SEMANTICALLY_VERIFIED", digest))
    return out


def index_csv(root=ROOT):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(["component_id", "component_version", "provision", "title_or_excerpt", "index_level", "audit_status", "source_sha256"])
    for row in build_index(root):
        w.writerow(row)
    return buf.getvalue()


def clause(component, ref, root=ROOT):
    key = component_key(component)
    text = read_source(key, root)
    lines = text.splitlines()
    want = ref.strip()
    want = re.sub(r"^(section|sec\.?|§+)\s*", "", want, flags=re.I).rstrip(".")
    if re.fullmatch(r"(appendix\s+)?[A-Za-z]", want, flags=re.I):
        want = "Appendix " + want[-1].upper()
    rows = index_source(text)
    hits = [r for r in rows if r[0] == want]
    if not hits and key in CONDITIONAL:
        hits = [r for r in rows if r[1].lower().startswith(want.lower()) or want.lower() in r[1].lower()]
    if not hits:
        raise AcrError("no provision %r in %s; this tool does not guess. Try: acr.py toc %s" % (ref, key, key))
    prov, title, level, start, end = hits[0]
    body = "\n".join(lines[start:end]).strip("\n")
    head = "[%s %s | version %s | %s]" % (key, prov, version_of(text) or "not stated", source_path(key, root).relative_to(root).as_posix())
    return head + "\n\n" + body + "\n"


def toc(component, root=ROOT):
    key = component_key(component)
    return "\n".join("%-12s %s" % (p, t[:90]) for p, t, lvl, _s, _e in index_source(read_source(key, root)) if lvl == "HEADING") + "\n"


def find(terms, component=None, limit=12, root=ROOT):
    words = [t.lower() for t in terms if t.strip()]
    if not words:
        raise AcrError("give at least one search term")
    keys = [component_key(component)] if component else list(COMPONENTS) + list(CONDITIONAL)
    out = []
    for key in keys:
        text = read_source(key, root)
        lines = text.splitlines()
        rows = index_source(text)
        for i, line in enumerate(lines):
            low = line.lower()
            if all(w in low for w in words):
                prov = "-"
                for p, _t, _l, s, e in rows:
                    if s <= i < e:
                        prov = p
                snippet = line.strip()
                pos = low.find(words[0])
                a = max(0, pos - 80)
                out.append({"component": key, "provision": prov, "line": i + 1,
                            "snippet": ("..." if a else "") + snippet[a:a + 240]})
                if len(out) >= limit:
                    return out
    return out


def terms(root=ROOT):
    with open(root / "REFERENCE/Defined_Terms.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def term_lookup(term, root=ROOT):
    t = term.strip().lower()
    for row in terms(root):
        if row["defined_term"].lower() == t:
            return row
    raise AcrError("%r is not a defined ACR term in REFERENCE/Defined_Terms.csv. An undefined term has no ACR meaning "
                   "(Core 15.6); this tool will not supply one." % term)


def check_fidelity(record):
    """Check the shape and internal consistency of a Core 15.8 fidelity record.

    The values are the caller's assertions. Nothing is authenticated and no
    permission, conformance or enforcement is established by this check.
    """
    issues = []
    if not isinstance(record, dict):
        raise AcrError("fidelity record must be a JSON object")
    for field, allowed in FIDELITY.items():
        v = record.get(field)
        if v is None:
            issues.append("%s: missing; state a value or UNKNOWN" % field)
        elif v not in allowed:
            issues.append("%s: %r is not one of %s" % (field, v, ", ".join(allowed)))
    ext = record.get("extent")
    if not (isinstance(ext, list) and ext and all(isinstance(x, str) and x.strip() for x in ext)):
        issues.append("extent: list the components actually available, by identifier, version and digest")
    rt = record.get("reasoning_trace")
    if rt is not None and rt not in REASONING_TRACE:
        issues.append("reasoning_trace: %r is not one of %s" % (rt, ", ".join(REASONING_TRACE)))
    claims = record.get("claims", [])
    if not isinstance(claims, list):
        issues.append("claims: must be a list when present")
        claims = []
    for n, c in enumerate(claims):
        tag = "claims[%d]" % n
        if not isinstance(c, dict):
            issues.append(tag + ": must be an object")
            continue
        kind = c.get("kind")
        g = c.get("grounding", record.get("grounding"))
        ex = c.get("execution", record.get("execution"))
        disp = c.get("disposition")
        if disp is not None and disp not in DISPOSITIONS:
            issues.append("%s: %r is not a Core 5.2 disposition" % (tag, disp))
        if kind == "EXTERNAL_FACT" and disp == "SUPPORTED_IN_SCOPE" and g in ("RECALL_ONLY", "NONE", "UNKNOWN", None):
            issues.append("%s: an external fact cannot be SUPPORTED_IN_SCOPE on %s grounding; use CONDITIONAL or UNRESOLVED (Core 15.8)" % (tag, g))
        if kind == "MECHANICAL_CHECK" and c.get("satisfied") is True and ex != "EXECUTED":
            issues.append("%s: a mechanically checkable obligation is not satisfied by a %s check (Core 5.1, 15.8)" % (tag, ex))
        if kind == "ENFORCEMENT" and c.get("asserted") is True and record.get("delivery") in ("ABSORBED_TEXT", "RETRIEVAL", "UNKNOWN", None):
            issues.append("%s: enforcement cannot be asserted under %s delivery; record it as an intention (Core 15.1, 15.8)" % (tag, record.get("delivery")))
        if kind == "INTERNAL_PROCESS" and c.get("basis") == "REASONING_TRACE" and c.get("asserted") is True:
            issues.append("%s: a reasoning trace is an output of the participant; it does not establish its internal processing or compliance (Core 15.8)" % tag)
        if kind == "INTERNAL_PROCESS" and c.get("basis") == "SELF_REPORT" and record.get("observability") == "BLACK_BOX" and c.get("asserted") is True:
            issues.append("%s: a black-box participant's own account does not establish its internal processing (Core 15.8)" % tag)
    return {"result": "CONSISTENT_AS_DECLARED" if not issues else "INCONSISTENT",
            "issues": issues,
            "note": "Values are the caller's assertions. Nothing was authenticated; no permission, conformance or enforcement follows."}


def kernel(card=False, root=ROOT):
    return (root / ("KERNEL_CARD.md" if card else "KERNEL.md")).read_text(encoding="utf-8")


def sizes(root=ROOT):
    def stat(paths):
        b = w = 0
        for p in paths:
            data = (root / p).read_bytes()
            b += len(data)
            w += len(data.decode("utf-8").split())
        return b, w
    core = COMPONENTS["core"][1]
    specs = [v[1] for v in COMPONENTS.values()]
    overs = [s.replace("Specification.md", "Overview.md") for s in specs]
    tiers = [
        ("T0", "Kernel card", ["KERNEL_CARD.md"]),
        ("T1", "Kernel", ["KERNEL.md"]),
        ("T2", "Core Specification", [core]),
        ("T3", "Core Specification and three conditional contracts", [core] + list(CONDITIONAL.values())),
        ("T4", "All Specifications", specs),
        ("T5", "All Specifications, Overviews and conditional contracts", specs + overs + list(CONDITIONAL.values())),
    ]
    return [(t, label, len(paths)) + stat(paths) for t, label, paths in tiers]


def sizes_csv(root=ROOT):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["tier", "contents", "files", "utf8_bytes", "whitespace_words", "note"])
    for t, label, n, b, words in sizes(root):
        w.writerow([t, label, n, b, words, "Measured bytes and words. Token counts depend on the tokenizer and are not stated."])
    return buf.getvalue()


def main(argv=None):
    ap = argparse.ArgumentParser(prog="acr.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    k = sub.add_parser("kernel", help="print the kernel (verbatim Core extracts)"); k.add_argument("--card", action="store_true")
    c = sub.add_parser("clause", help="print one exact provision"); c.add_argument("component"); c.add_argument("ref")
    t = sub.add_parser("toc", help="list the headings of a component"); t.add_argument("component")
    f = sub.add_parser("find", help="search the sources for lines containing all terms"); f.add_argument("terms", nargs="+"); f.add_argument("--in", dest="component"); f.add_argument("--limit", type=int, default=12)
    p = sub.add_parser("term", help="look up a defined ACR term, or list them all"); p.add_argument("term", nargs="?")
    sub.add_parser("parse", help="parse one message from stdin with the command profile (parsing only)")
    fi = sub.add_parser("fidelity", help="check a Core 15.8 fidelity record (JSON file or - for stdin)"); fi.add_argument("record")
    sub.add_parser("sizes", help="measured size of each load tier")
    sub.add_parser("index", help="print the clause index derived from the sources")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "kernel":
            sys.stdout.write(kernel(a.card))
        elif a.cmd == "clause":
            sys.stdout.write(clause(a.component, a.ref))
        elif a.cmd == "toc":
            sys.stdout.write(toc(a.component))
        elif a.cmd == "find":
            print(json.dumps(find(a.terms, a.component, a.limit), indent=2, ensure_ascii=False))
        elif a.cmd == "term":
            if a.term:
                print(json.dumps(term_lookup(a.term), indent=2, ensure_ascii=False))
            else:
                print(json.dumps(terms(), indent=2, ensure_ascii=False))
        elif a.cmd == "parse":
            try:
                import command_interface
            except ImportError:
                raise AcrError("TOOLS/command_interface.py is not beside this tool; nothing was parsed")
            data = sys.stdin.buffer.read()
            print(json.dumps(command_interface.parse(data[:-1] if data.endswith(b"\n") else data), indent=2, ensure_ascii=False))
        elif a.cmd == "fidelity":
            raw = sys.stdin.read() if a.record == "-" else Path(a.record).read_text(encoding="utf-8")
            res = check_fidelity(json.loads(raw))
            print(json.dumps(res, indent=2))
            return 0 if res["result"] == "CONSISTENT_AS_DECLARED" else 1
        elif a.cmd == "sizes":
            sys.stdout.write(sizes_csv())
        elif a.cmd == "index":
            sys.stdout.write(index_csv())
    except (AcrError, OSError, json.JSONDecodeError) as e:
        print("acr: " + str(e), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.exit(main())
