"""Read the flat ISO 9660 / Rock Ridge root produced by the tester CD builder."""
from hashlib import sha256


def desktop_program_hashes(image, receipt):
    iso_size = receipt.get("iso_bytes")
    if type(iso_size) is not int or iso_size != len(image):
        raise ValueError("Desktop receipt ISO byte count differs from the image")
    declared = receipt["on_disc"]
    sector = 2048
    volume = image[16 * sector:17 * sector]
    if volume[:7] != b"\x01CD001\x01" or int.from_bytes(volume[128:130], "little") != sector:
        raise ValueError("Expected a tester CD with 2048-byte ISO sectors")

    def extent(record):
        block = int.from_bytes(record[2:6], "little")
        size = int.from_bytes(record[10:14], "little")
        start = block * sector
        if start + size > len(image):
            raise ValueError("ISO extent outside the image")
        return image[start:start + size]

    root = volume[156:190]
    if len(root) != 34 or root[0] != 34 or root[25] != 2 or root[32:] != b"\x01\x00":
        raise ValueError("Invalid tester CD root directory")
    directory = extent(root)
    files = {}
    offset = 0
    while offset < len(directory):
        length = directory[offset]
        if not length:
            offset = (offset // sector + 1) * sector
            continue
        record = directory[offset:offset + length]
        if length < 34 or len(record) != length or offset % sector + length > sector:
            raise ValueError("Invalid ISO directory record")
        offset += length
        name_length = record[32]
        if not name_length or 33 + name_length > length:
            raise ValueError("Invalid ISO filename")
        name = record[33:33 + name_length]
        if name in (b"\x00", b"\x01") and record[25] == 2:
            continue
        if record[25] != 0:
            raise ValueError("Expected only regular files in the tester CD root")
        name = name.split(b";", 1)[0].decode("ascii")
        pos = 33 + name_length + (name_length % 2 == 0)
        while pos + 4 <= length:
            field_size = record[pos + 2]
            if field_size < 4 or pos + field_size > length:
                raise ValueError("Invalid Rock Ridge field")
            field = record[pos:pos + field_size]
            if field[:2] in (b"CE", b"CL", b"SL"):
                raise ValueError("Expected in-place regular files and names on the tester CD")
            if field[:2] == b"NM":
                if len(field) < 6 or field[4] != 0:
                    raise ValueError("Expected a complete Rock Ridge filename")
                name = field[5:].decode("utf-8")
            pos += field_size
        if name in files:
            raise ValueError(f"Duplicate tester CD member: {name}")
        data = extent(record)
        files[name] = (len(data), sha256(data).hexdigest())

    if files.keys() != declared.keys():
        difference = sorted(files.keys() ^ declared.keys())
        raise ValueError(f"Desktop receipt and ISO inventory differ: {difference}")
    for name, (size, digest) in files.items():
        byte_count = declared[name].get("bytes")
        if type(byte_count) is not int or byte_count != size or declared[name].get("sha256") != digest:
            raise ValueError(f"Desktop receipt differs from ISO member: {name}")
    return {name: digest for name, (_, digest) in files.items() if name.endswith(".elf")}
