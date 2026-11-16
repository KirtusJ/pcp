"""From a POSIX checkout, run: python3 audit/enterprise-checkout/check.py [REV].

Checks the committed Enterprise release in three real Git working trees.
Repository-only files at the root (such as the ISO and audit tools) are
outside the standalone edition. Each release directory is copied in full.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


REPO = Path(__file__).resolve().parents[2]
PLUGINS = ("pcp", "pcp-os")


def run(*args, cwd=None, check=True):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=check)


def check_checkout(revision, mode, target):
    checkout = target / "repo"
    run("git", "clone", "--no-local", "--no-checkout", "--quiet", str(REPO), str(checkout))
    run("git", "-c", "core.autocrlf=" + mode, "checkout", "--quiet", "--detach", revision, cwd=checkout)

    # The standalone verifier requires the exact edition inventory. Keep
    # every file under its declared directories, including any unexpected one.
    edition = target / "edition"
    edition.mkdir()
    manifest = json.loads((checkout / "MANIFEST.json").read_bytes())
    roots = {Path(entry["path"]).parts[0] for entry in manifest["files"]}
    for name in sorted(roots | {"MANIFEST.json"}):
        source = checkout / name
        if source.is_dir():
            shutil.copytree(source, edition / name, symlinks=True)
        else:
            shutil.copy2(source, edition / name, follow_symlinks=False)
    run(sys.executable, "-B", str(edition / "verify_edition.py"))

    plugin_root = checkout / "PCP_1.0_Plugins" / "plugins"
    launcher = plugin_root / "pcp-os" / "servers" / "pcpos"
    for plugin in PLUGINS:
        method = plugin_root / plugin / "method"
        run(launcher, "method", method)
        index = method / "REFERENCE" / "Clause_Index.csv"
        original = index.read_bytes()
        altered = original.replace(b"\r\n", b"\n")
        if altered == original:
            raise ValueError(f"{plugin}: released index has no CRLF to exercise")
        index.write_bytes(altered)
        rejected = run(launcher, "method", method, check=False)
        if rejected.returncode != 6 or "1 differing [REFERENCE/Clause_Index.csv]" not in rejected.stdout:
            raise ValueError(f"{plugin}: altered index returned {rejected.returncode}: {rejected.stdout}")
    print(f"PASS core.autocrlf={mode}: full edition, two plugin reads, two altered-index refusals", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("revision", nargs="?", default="HEAD")
    args = parser.parse_args()
    revision = run("git", "rev-parse", "--verify", "--end-of-options", args.revision + "^{commit}", cwd=REPO).stdout.strip()
    print(f"Testing {revision}", flush=True)
    for mode in ("false", "input", "true"):
        with tempfile.TemporaryDirectory() as directory:
            check_checkout(revision, mode, Path(directory))


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        sys.exit(f"{error.cmd} exited {error.returncode}\n{error.stdout}{error.stderr}")
