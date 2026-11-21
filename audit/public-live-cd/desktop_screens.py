"""Read the desktop, verification page and selected program using the tested kernel's font."""
from collections import Counter
import re
import runpy
import subprocess


def clean_home(rows):
    placed = (".elf", "may use:", "RECENT ACTIVITY", "THIS MACHINE", "SESSION", "SHORTCUT")
    return not any(word in row for row in rows for word in placed)


def selected_program(rows, expected, program_hashes):
    # The marker, name, size and digest share a row. The grant text starts under the name.
    selected = [(i, match) for i, row in enumerate(rows)
                for match in re.finditer(r"> ([\w.-]+\.elf) ", row)]
    if len(selected) != 1:
        return False
    i, match = selected[0]
    if match[1] != expected or i + 1 >= len(rows):
        return False
    identity = re.match(r" +\d+(?:\.\d+)? (?:KiB|MiB) +SHA-256 ([0-9a-f]{16})\.\.\.", rows[i][match.end(1):])
    if not identity or identity[1] != program_hashes.get(expected, "")[:16]:
        return False
    # Both desktop fixtures provide AC'97, loader files and a store. Neither
    # fixture names a restricted grant or an Ethernet/second-serial image.
    # The digest is drawn at the card's right edge on every graphical desktop.
    name_column = match.start(1)
    left = max(0, name_column - 3)
    right = match.end(1) + identity.end() + 1
    if rows[i + 1][left:name_column].strip():
        return False
    grants = rows[i + 1][name_column:right].rstrip()
    if not re.fullmatch(r"may use: display, keyboard, sound, loader files, store"
                        r"(?: +(?:in the dock|on the desktop))?", grants):
        return False
    # Current cards put a pin label on its own row. The plate edge (or blank
    # background on older desktops) must follow the complete disclosure.
    after = i + 2
    pin = " " * (name_column - left) + "pinned to the desktop"
    if after < len(rows) and rows[after][left:right].rstrip() == pin:
        after += 1
    return after < len(rows) and not rows[after][left:right].strip(" ?")


def power_warning_rows(frame, glyphs):
    """Decode the 1x power dialog, including small screens and the literal question mark."""
    try:
        magic, size, depth, pixels = frame.split(b"\n", 3)
        width, height = map(int, size.split())
    except ValueError:
        return []
    if (magic != b"P6" or depth != b"255" or width < 320 or height < 200
            or len(pixels) != width * height * 3):
        return []

    # The dialog has one flat background. Refuse a non-font cell, including
    # damage at the question mark where the general reader substitutes '?'.
    background = pixels[:3]
    blank = background * 200
    stride = width * 3
    rows = []
    for y in range(0, height - 19, 20):
        line = []
        for x in range(0, width - 9, 10):
            start = y * stride + x * 3
            cell = b"".join(pixels[offset:offset + 30]
                            for offset in range(start, start + 20 * stride, stride))
            if cell == blank:
                line.append(" ")
                continue
            mask = tuple(cell[i:i + 3] != background for i in range(0, len(cell), 3))
            letter = glyphs.get(mask)
            if letter is None:
                return []
            line.append(letter)
        rows.append("".join(line).strip())
    return rows


def complete_power_warning(rows):
    if len(rows) < 5:
        return False
    actions = "Enter switch off    Esc go back"
    if rows[:2] == ["POWER OFF", "Switch PCP OS off?"]:
        if rows[-1] == actions:
            warning = rows[2:-1]
        elif rows[-2:] == ["Enter switch off", "Esc go back"]:
            warning = rows[2:-2]
        else:
            return False
    elif (rows[:5] == ["", "POWER OFF", "", "Switch PCP OS off?", ""]
          and rows[-2:] == [actions, ""]):
        warning = rows[5:-2]
    else:
        return False
    return " ".join(line for line in warning if line) == (
        "The register is closed and verified first. "
        "Files of this session that were not saved by a program are lost.")


class DesktopScreens:
    def __init__(self, source, program_hashes):
        self.program_hashes = program_hashes
        reader = "examples/tester-cd/check.py"
        font = "PCP_OS_Rust/crates/pcpos-kernel/src/font.rs"
        for name in (reader, font):
            committed = subprocess.check_output(["git", "-C", source, "show", "HEAD:" + name], encoding="utf-8")
            if (source / name).read_text(encoding="utf-8") != committed:
                raise ValueError(f"Source checkout differs from HEAD: {name}")
        renderer = subprocess.check_output(["git", "-C", source, "show",
                                            "HEAD:PCP_OS_Rust/crates/pcpos-kernel/src/session.rs"], text=True)
        self.has_verification_page = "fn verification_view(" in renderer
        self.confirm_power = "fn power_prompt(" in renderer
        self.verification_key = "f5" if self.confirm_power else "v"
        self.keys_hint = "F1 keys" if self.confirm_power else "K keys"
        self.home_form = "dock" if self.has_verification_page else "two-bar"
        if "fn whole_bar(" in renderer:
            self.home_form = "bar"
        checks = runpy.run_path(str(source / reader))
        self.read_screen = checks["read_screen"]
        self.glyphs = checks["kernel_glyphs"]()

    def only_programs_dock(self, frame, rows):
        _, size, _, pixels = frame.split(b"\n", 3)
        width, height = map(int, size.split())
        dock_left = (width - 160) // 20 * 10
        column = (dock_left + 40) // 10
        if rows[-3][column:column + 8] == "Programs":
            return True
        # The first dock revision centered the same label half a cell to the left.
        left = dock_left + 35
        top = height // 20 * 20 - 60
        for column, letter in enumerate("Programs"):
            x = left + column * 10
            cell = [pixels[pos:pos + 3] for y in range(top, top + 20) for dx in range(10)
                    for pos in (3 * (y * width + x + dx),)]
            ground = Counter(cell).most_common(1)[0][0]
            if self.glyphs.get(tuple(pixel != ground for pixel in cell)) != letter:
                return False
        return True

    def matches(self, frame, surface, startup_checks=71):
        """Recognize the untouched Home, the full verification page or one selected program."""
        if surface == "power":
            return self.confirm_power and complete_power_warning(power_warning_rows(frame, self.glyphs))
        rows = self.read_screen(frame, self.glyphs)
        if not rows:
            return False
        status = f"Verified at start: all {startup_checks} self-tests passed."
        footer = rows[-2]
        if self.has_verification_page:
            if rows[1].strip() == "VERIFICATION":
                return (surface == "verification" and rows[3].strip() == status
                        and re.fullmatch(r"Register: [1-9][0-9]* events, head [0-9a-f]{16}\.\.\.", rows[6].strip()) is not None
                        and rows[7].strip() == "The register's chain is intact."
                        and footer.strip() == "Any key goes back")
            # Both graphical surfaces put their status at the same position in the right corner.
            width = int(frame.split(b"\n", 2)[1].split()[0])
            corner = (width - 120) // 10 + 1
            if footer[corner:corner + 8] != "verified":
                return False
            if surface == "home" and self.home_form == "bar":
                return (footer[6:14] == "Programs" and footer[corner - 5 - len(self.keys_hint):corner - 5] == self.keys_hint
                        and clean_home(rows))
            if surface in ("home", "home-dock"):
                return footer.startswith(self.keys_hint, 3) and clean_home(rows) and self.only_programs_dock(frame, rows)
            return footer[3:14] == "Esc desktop" and self.keys_hint in footer[14:] and selected_program(rows, surface, self.program_hashes)

        # The earlier two-bar desktop displayed the complete verdict on its top bar.
        if not any(status in row for row in rows):
            return False
        home_keys = all(word in footer for word in ("programs", "widgets", "files", "power off"))
        launcher_keys = all(word in footer for word in ("choose", "start", "desktop", "power off"))
        if surface == "home":
            return home_keys and not launcher_keys and clean_home(rows)
        return launcher_keys and not home_keys and selected_program(rows, surface, self.program_hashes)

    async def cancel_power(self, key, capture, name, expected, before_hash):
        """Read the confirmation, cancel, then compare the full restored surface and selection."""
        await key("f10")
        await capture(name + "-power", "power")
        await key("esc")
        after_hash = await capture(name + "-after-cancel", expected)
        if before_hash != after_hash:
            raise ValueError("Power cancellation changed " + name)
