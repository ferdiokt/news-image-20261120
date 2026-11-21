"""make.fun news-image-20261120 entry: writes the committed entry.png (drawn by render.py) to the output dir.

Offline, standard library only. Run: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import struct
import zlib
from pathlib import Path

data = Path(__file__).with_name("entry.png").read_bytes()

# The gate's rules: a whole PNG, at most 1 MiB and 1024x1024. Fail loudly rather than ship an invalid entry.
assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
assert len(data) <= 1 << 20, f"{len(data)} bytes > 1 MiB"
pos, seen = 8, []
while pos < len(data):
    n, kind = struct.unpack(">I4s", data[pos:pos + 8])
    body = data[pos + 8:pos + 8 + n]
    assert struct.unpack(">I", data[pos + 8 + n:pos + 12 + n])[0] == zlib.crc32(kind + body), f"bad CRC in {kind}"
    seen.append(kind)
    pos += 12 + n
w, h = struct.unpack(">II", data[16:24])
assert seen[0] == b"IHDR" and seen[-1] == b"IEND" and w <= 1024 and h <= 1024, (seen[:1], w, h)

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.png").write_bytes(data)
