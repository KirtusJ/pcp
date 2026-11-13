#!/usr/bin/env python3
"""Local check for one edition of PCP Version 1.0. Standard library only.

  python3 verify_edition.py            full check
  python3 verify_edition.py --quick    skip the packets' own verifiers

Checks the inventory and digests of this folder against MANIFEST.json; that the
two packets are the ones EDITION.json names; that each plugin is whole, states
this edition and carries the method's text, each file the Implementation packet's
own; that the PCP OS programs are the ones named and may be run; that the machine
form describes that packet; that the license, notice, price
schedule and evidence statement carry their controlling statements for this
edition; that the Readers packet belongs to this edition and pins this
Implementation packet; that the edition guide's reading copy was generated from
the guide beside this file; and, unless --quick, runs each packet's own verifier
on a temporary extraction. A pass is a local fact about these files. It
authenticates nobody, validates no meaning, and is not legal advice or a
statement that the product has been tested.
"""
import hashlib, json, subprocess, sys, tempfile, zipfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
EDITIONS = {"PERSONAL": "Personal Edition", "COMMERCIAL": "Commercial Edition", "ENTERPRISE": "Enterprise Edition"}
PRICE_ROWS = ("| Personal | **US$5.00** | One payment for one license held by one natural person. Not a subscription: no renewal and no recurring charge. |",
              "| Commercial | No published price | Licensed only under a written agreement negotiated individually with the rights holder. |",
              "| Enterprise | No published price | Licensed only under a written agreement negotiated individually with the rights holder. |")
EVIDENCE = ("**Not peer reviewed.**", "**Not independently reviewed.**", "**Not empirically evaluated.**", "**No observational evidence of effect.**")


class Fail(Exception):
    pass


def need(cond, msg):
    if not cond:
        raise Fail(msg)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def text(name):
    return (HERE / name).read_text(encoding="utf-8")


def extract(zpath, dest):
    with zipfile.ZipFile(zpath) as z:
        for n in z.namelist():
            need(not n.startswith("/") and ".." not in n.split("/") and "\\" not in n, "unsafe path in %s" % zpath.name)
        z.extractall(dest)
    tops = sorted(p for p in dest.iterdir() if p.is_dir())
    need(len(tops) == 1, "%s must hold exactly one top-level folder" % zpath.name)
    return tops[0]


def verify(quick):
    man = json.loads(text("MANIFEST.json")); ed = json.loads(text("EDITION.json"))
    need(man.get("format") == "pcp-edition-local-integrity/1.0", "unsupported manifest format")
    edition = ed.get("edition"); need(edition in EDITIONS and man.get("edition") == edition, "edition identity")
    name = EDITIONS[edition]
    files = {e["path"]: e for e in man["files"]}
    actual = sorted(p.relative_to(HERE).as_posix() for p in HERE.rglob("*")
                    if p.is_file() and p.name != "MANIFEST.json" and "__pycache__" not in p.parts)
    need(actual == sorted(files) and man.get("payload_count") == len(files), "inventory differs from manifest: %s" % sorted(set(actual) ^ set(files))[:5])
    for p, e in files.items():
        data = (HERE / p).read_bytes()
        need(len(data) == e["bytes"] and sha(data) == e["sha256"], "content differs from manifest: %s" % p)
    # Identity and fixed points
    need(ed.get("product") == "Parrot Council Protocol" and ed.get("abbreviation") == "PCP" and ed.get("method") == "Adversarial Claim Review"
         and ed.get("version") == "1.0" and ed.get("creator") == "Kirtus Justus", "product identity")
    need(ed.get("licensing") == "PROPRIETARY_ALL_RIGHTS_RESERVED" and ed.get("license_model") == "LICENSED_NOT_SOLD", "licensing status")
    want = ({"amount": "5.00", "currency": "USD", "basis": "SINGLE_PURCHASE", "subscription": False} if edition == "PERSONAL"
            else {"amount": None, "currency": None, "basis": "INDIVIDUALLY_NEGOTIATED_WRITTEN_AGREEMENT", "published_price": False})
    need(ed.get("price") == want, "price record for this edition")
    need(ed.get("evidence") == {"peer_review": "NOT_PERFORMED", "independent_review": "NOT_PERFORMED", "empirical_evaluation": "NOT_PERFORMED",
                                "behavioral_validation": "NOT_PERFORMED", "observational_evidence": "NONE_OF_EFFECT",
                                "plugins_in_live_sessions": "UNCONTROLLED_SESSIONS_ONLY"}, "evidence record")
    # Controlling statements
    pricing = text("PRICING.md")
    need("**This schedule is fixed.**" in pricing and all(r in pricing for r in PRICE_ROWS), "price schedule")
    notice = text("NOTICE.md")
    need("**Proprietary material. All rights reserved.**" in notice and "Copyright (c) 2026 Kirtus Justus. All rights reserved" in notice
         and "PCP is licensed, not sold." in notice and "Holding a copy grants nothing." in notice, "notice")
    ev = text("EVIDENCE_STATUS.md"); need(all(x in ev for x in EVIDENCE), "evidence statement")
    lic = text("LICENSE.md")
    need(lic.startswith("# Parrot Council Protocol (PCP) 1.0 | %s License" % name) and "The Materials are proprietary. They are licensed, not sold" in lic
         and all(o not in lic.splitlines()[0] for k, o in EDITIONS.items() if k != edition), "license belongs to this edition")
    if edition == "PERSONAL":
        need("**License fee:** US$5.00, paid once" in lic and "one natural person" in lic, "Personal license terms")
    else:
        need("**Without a signed Agreement there is no license.**" in lic and "no price is published" in lic, "organization license conditions")
    need(text("EDITION_GUIDE.md").startswith("# PCP 1.0 | %s Guide" % name) and name in text("README.md").splitlines()[0], "guide and readme belong to this edition")
    # Packets
    ip, rp = HERE / ed["packets"]["implementation"]["file"], HERE / ed["packets"]["readers"]["file"]
    need(sha(ip.read_bytes()) == ed["packets"]["implementation"]["sha256"], "Implementation packet differs from EDITION.json")
    need(sha(rp.read_bytes()) == ed["packets"]["readers"]["sha256"], "Readers packet differs from EDITION.json")
    with tempfile.TemporaryDirectory() as td:
        impl = extract(ip, Path(td) / "i"); rd = extract(rp, Path(td) / "r")
        im = (impl / "MANIFEST.json").read_bytes()
        need(sha(im) == ed["packets"]["implementation"]["manifest_sha256"], "Implementation fingerprint differs from EDITION.json")
        rman = json.loads((rd / "MANIFEST.json").read_text(encoding="utf-8"))
        need(rman.get("edition") == edition, "the Readers packet belongs to another edition")
        need(rman["implementation_packet"]["manifest_sha256"] == sha(im), "the Readers packet pins another Implementation packet")
        need(sha((rd / "MANIFEST.json").read_bytes()) == ed["packets"]["readers"]["manifest_sha256"], "Readers fingerprint differs from EDITION.json")
        guide = [e for e in rman["files"] if e.get("source_packet") == "EDITION"]
        need(len(guide) == 1 and guide[0]["generated_from"] == "EDITION_GUIDE.md"
             and guide[0]["source_sha256"] == sha((HERE / "EDITION_GUIDE.md").read_bytes()), "edition guide reading copy does not match EDITION_GUIDE.md")
        for p in impl.rglob("*"):
            if p.is_file() and p.suffix in (".md", ".json", ".csv", ".py"):
                low = p.read_text(encoding="utf-8", errors="replace").lower()
                need(all(n.lower() not in low for n in EDITIONS.values()), "edition marker inside the Implementation packet: %s" % p.name)
        # Plugins: whole, of this edition, and carrying this Implementation packet and no other
        impl_files = {e["path"]: e["sha256"] for e in json.loads(im)["files"]}
        market = json.loads(text("PCP_1.0_Plugins/.claude-plugin/marketplace.json"))
        need(market.get("name") == "pcp-" + edition.lower() and [p["name"] for p in market["plugins"]] == ["pcp", "pcp-os"], "marketplace identity")
        for plugin in ("pcp", "pcp-os"):
            root = HERE / "PCP_1.0_Plugins" / "plugins" / plugin
            pm = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
            for e in pm["files"]:
                need(sha((root / e["path"]).read_bytes()) == e["sha256"], "plugin %s: %s differs from its manifest" % (plugin, e["path"]))
            listed = {e["path"] for e in pm["files"]}
            on_disk = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json" and "__pycache__" not in p.parts}
            need(listed == on_disk, "plugin %s: inventory differs from its manifest" % plugin)
            prof = json.loads((root / "edition" / "EDITION.json").read_text(encoding="utf-8"))
            need(prof.get("edition") == edition and prof.get("method_release", {}).get("manifest_sha256") == sha(im), "plugin %s states another edition or method release" % plugin)
            need(sha((root / "method" / "MANIFEST.json").read_bytes()) == sha(im), "plugin %s carries another method release" % plugin)
            # A plugin carries the method's text: every file of the packet outside its programs and probes, each the packet's own bytes
            held = {p.relative_to(root / "method").as_posix() for p in (root / "method").rglob("*") if p.is_file()} - {"MANIFEST.json"}
            need(held <= set(impl_files) and not any(p.startswith("INTEGRATION/") for p in held), "plugin %s: its method folder holds a file that does not belong there" % plugin)
            need(all(p in held for p in impl_files if not p.startswith(("INTEGRATION/", "TOOLS/"))), "plugin %s: a file of the method's text is missing" % plugin)
            for path in held:
                need(sha((root / "method" / path).read_bytes()) == impl_files[path], "plugin %s: method file %s is not the packet's" % (plugin, path))
            pj = json.loads((root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
            need(pj.get("name") == plugin and pj.get("version") == ed.get("plugin_version") and pj.get("author", {}).get("name") == "Kirtus Justus", "plugin %s identity" % plugin)
        import os
        for g in ed["components"]["plugins"]["pcp-os"]["programs"]:
            need(sha((HERE / "PCP_1.0_Plugins" / g["file"]).read_bytes()) == g["sha256"], "a PCP OS program is not the one EDITION.json names: %s" % g["file"])
        if os.name == "posix":
            for f in ["PCP_1.0_Plugins/plugins/pcp-os/servers/pcpos"] + ["PCP_1.0_Plugins/" + g["file"] for g in ed["components"]["plugins"]["pcp-os"]["programs"]]:
                need(os.access(HERE / f, os.X_OK), "%s is not executable: the archive was extracted without its permissions. Run: chmod +x '%s'" % (f, HERE / f))
        osreq = json.loads(text("PCP_1.0_OS/PCP_OS_Requirements.json"))
        need(osreq["source_sha256"] == sha((HERE / "PCP_1.0_OS" / "PCP_OS_Specification.md").read_bytes()), "the PCP OS requirements were not generated from the Specification beside them")
        need(all((HERE / "PCP_1.0_OS" / f).is_file() for f in ("PCP_OS_Overview.pdf", "PCP_OS_Specification.pdf", "backgrounds/pcp-core.svg")), "PCP OS reading copies or backgrounds are missing")
        machine = json.loads(text("PCP_1.0_Machine/pcp.machine.json"))
        need(machine["method_release"]["manifest_sha256"] == sha(im), "the machine form describes another method release")
        for m in machine["modules"]:
            need(impl_files.get(m["specification"]["path"]) == m["specification"]["sha256"], "machine form: %s is not the packet's Specification" % m["id"])
        if not quick:
            for cmd in ([sys.executable, "-B", str(impl / "TOOLS/verify_release.py")],
                        [sys.executable, "-B", str(rd / "verify_readers.py"), str(impl)]):
                out = subprocess.run(cmd, capture_output=True, text=True)
                need(out.returncode == 0 and out.stdout.startswith("PASS"), "packet verifier failed: %s" % (out.stdout.strip().split("\n")[0][:160] or out.stderr.strip()[-160:]))
    return edition, len(files), sha((HERE / "MANIFEST.json").read_bytes()), ed["packets"]["implementation"]["sha256"]


def main(argv):
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__.strip()); return 0
    try:
        edition, n, fp, impl = verify("--quick" in argv)
    except Fail as e:
        print("FAIL_EDITION_CHECK: %s" % e); return 1
    except (OSError, KeyError, ValueError, TypeError, IndexError, zipfile.BadZipFile) as e:
        print("FAIL_EDITION_CHECK: %s: %s" % (type(e).__name__, e)); return 1
    print("PASS_EDITION_CHECK %s edition, %d files%s (not authenticated, not certified, not peer reviewed, behavior not tested)"
          % (edition, n, "" if "--quick" not in argv else ", packet verifiers skipped"))
    print("edition fingerprint (SHA-256 of MANIFEST.json): %s" % fp)
    print("Implementation packet SHA-256 (the same in every edition): %s" % impl)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
