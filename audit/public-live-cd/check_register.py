"""Read the visible task records directly from the pinned 10 by 20 kernel font."""
import argparse
import ast
import json
from pathlib import Path
import re


def read_rows(path, glyphs):
    # On these public CDs the kernel draws register rows in TEXT over GROUND.
    with path.open("rb") as ppm:
        if [ppm.readline().strip() for _ in range(3)] != [b"P6", b"1024 768", b"255"]:
            raise ValueError(f"{path}: unexpected framebuffer header")
        pixels = ppm.read()
    stride = 1024 * 3
    if len(pixels) != 768 * stride:
        raise ValueError(f"{path}: incomplete framebuffer")
    rows = []
    for row in range(3, 35):
        cells = []
        for col in range(2, 100):
            start = row * 20 * stride + col * 30
            cell = b"".join(pixels[start + y * stride:start + y * stride + 30] for y in range(20))
            cells.append(glyphs[cell])
        rows.append("".join(cells).rstrip())
    return rows


def check_register(font, directory):
    source = font.read_text()
    coverage = ast.literal_eval("[" + source.split(" = [", 1)[1].split("];", 1)[0] + "]")
    # Match the integer blend used by kernel ui::text.
    palette = [bytes((back * (255 - a) + ink * a + 127) // 255
                     for back, ink in zip((16, 40, 63), (242, 247, 252))) for a in range(256)]
    glyphs = {b"".join(palette[a] for a in data): chr(32 + i) for i, data in enumerate(coverage)}
    latest = read_rows(directory / "register-latest.ppm", glyphs)
    earlier = read_rows(directory / "register-earlier.ppm", glyphs)
    restored = read_rows(directory / "register-restored.ppm", glyphs)
    def sequence(rows):
        return [int(line.split()[0]) for line in rows]
    last = sequence(latest)
    first = sequence(earlier)
    if (latest != restored or first[0] >= last[0] or first[-1] >= last[-1] or
            last != list(range(last[0], last[0] + len(last))) or
            first != list(range(first[0], first[0] + len(first)))):
        raise ValueError("Register scroll sequence differs")
    starts = []
    ends = {}
    for line in latest:
        start = re.search(r"\bTASK_STARTED\s+label surf\.elf; id (T\d+)\b", line)
        if start:
            starts.append((int(line.split()[0]), start[1]))
        end = re.search(r"\bTASK_ENDED\s+id (T\d+); outcome (\w+);", line)
        if end:
            ends.setdefault(end[1], []).append((int(line.split()[0]), end[2]))
    if len(starts) != 2 or starts[0][1] == starts[1][1]:
        raise ValueError("Expected two distinct Surfbird launches on the register screen")
    tasks = []
    for (seq, task), outcome in zip(starts, ["DONE", "STOPPED"]):
        recorded = ends.get(task, [])
        if len(recorded) != 1 or recorded[0][0] <= seq or recorded[0][1] != outcome:
            raise ValueError(f"Unexpected displayed result for {task}: {recorded}")
        tasks.append({"id": task, "start": seq, "end": recorded[0][0], "outcome": outcome})
    if tasks[0]["end"] >= tasks[1]["start"]:
        raise ValueError("Surfbird task records are out of order")
    record = {"tasks": tasks, "earlier_rows": earlier, "latest_rows": latest}
    (directory / "register.json").write_text(json.dumps(record, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("font", type=Path)
    parser.add_argument("directory", type=Path, nargs="+")
    args = parser.parse_args()
    for directory in args.directory:
        check_register(args.font, directory)
