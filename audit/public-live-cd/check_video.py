"""Identify four captured playback frames from the picture stream on the optical disc."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from check import ISO_SHA, VIDEO_MARKERS
from check_audio import load_verifier, sha256

VIDEO_SHA = "f6a1d9a0702f472f5b02cf0a528586e6d4447acbad2bd92eb0fc6d70eea4df4d"


def check_video(iso, output, verifier, *, expected_iso=ISO_SHA):
    if sha256(iso) != expected_iso:
        raise ValueError("Unexpected optical image")
    media = load_verifier(verifier)
    with tempfile.TemporaryDirectory() as temp:
        clip = Path(temp) / "clip.ppm"
        subprocess.run(["xorriso", "-osirrox", "on", "-indev", str(iso),
                        "-extract", "/clip.ppm", str(clip)], check=True)
        if sha256(clip) != VIDEO_SHA:
            raise ValueError("Unexpected clip.ppm on the CD")
        video = clip.read_bytes()

    frame_size = len(media.HEADER) + 48 * 24 * 3
    if len(video) != media.IMAGES * frame_size:
        raise ValueError("Unexpected size for the CD picture stream")
    frames = []
    for start in range(0, len(video), frame_size):
        if not video.startswith(media.HEADER, start):
            raise ValueError("Invalid header in the CD picture stream")
        frames.append(video[start + len(media.HEADER):start + frame_size])
    if len(set(frames)) != len(frames):
        raise ValueError("The CD picture stream cannot uniquely identify all displayed frames")

    samples = []
    for marker in VIDEO_MARKERS:
        screen = output / f"video-{marker}.ppm"
        actual = media.screenshot_frame(screen, frames)
        if actual // 8 != marker // 8:
            raise ValueError(f"After marker {marker}, the screen shows frame {actual} from another scene")
        samples.append({"serial_marker": marker, "displayed_frame": actual, "screen_sha256": sha256(screen)})
    receipt = {"iso_sha256": expected_iso, "clip_sha256": VIDEO_SHA, "samples": samples}
    (output / "video.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iso", type=Path)
    parser.add_argument("output", type=Path, help="directory containing four playback framebuffers")
    parser.add_argument("verifier", type=Path, help="PCP OS Surfbird replay_local_media.py")
    args = parser.parse_args()
    check_video(args.iso, args.output, args.verifier)
