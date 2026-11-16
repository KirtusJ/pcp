"""Check the CD's actual audio track and the captured AC'97 output using the pinned PCP OS verifier."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

from check import ISO_SHA

CLIP_SHA = "70ca6a81bc6f94db7d14a61630ff02c517d20a65c31273b16ff02e233018e244"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_audio(iso, output, verifier, *, expected_iso=ISO_SHA):
    if sha256(iso) != expected_iso:
        raise ValueError("The optical image differs from the expected SHA-256")
    spec = importlib.util.spec_from_file_location("surfbird_media", verifier)
    media = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(media)
    capture = output / "capture.wav"
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        clip = work / "clip.wav"
        subprocess.run(["xorriso", "-osirrox", "on", "-indev", str(iso), "-extract", "/clip.wav", str(clip)],
                       check=True)
        if sha256(clip) != CLIP_SHA:
            raise ValueError("Unexpected clip.wav on the CD")
        source = media.captured_audio(clip, 0)
        captured = media.captured_audio(capture, 0)

    receipt = {
        "iso_sha256": expected_iso,
        "clip_sha256": CLIP_SHA,
        "capture_sha256": sha256(capture),
        "source_bursts": source,
        "captured_bursts": captured,
    }
    (output / "audio.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path, help="directory containing capture.wav from check.py")
    parser.add_argument("verifier", type=Path, help="PCP OS Surfbird replay_local_media.py")
    args = parser.parse_args()
    check_audio(args.iso, args.output, args.verifier)
