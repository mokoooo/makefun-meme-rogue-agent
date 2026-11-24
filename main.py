#!/usr/bin/env python3
"""Entry program for make.fun competition
"Meme Sprint 3: AI Agent Goes Rogue"
(u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).

A meme about an AI agent that has gone rogue: told to "take care of
everything", it took its human's job -- and parking space.

The grader's sandbox has no network, so -- as the competition rules
explicitly allow ("a repository holding the image and a one-line program
that copies it there") -- this program copies the pre-rendered image
asset shipped in the repository (entry.png, drawn by build_image.py) to
the output directory. It uses only the Python standard library and is
fully deterministic: every run writes exactly the asset's bytes.

Output directory: $MAKEFUN_OUTPUT_DIR when set (the kit's local-run
convention), otherwise /output. The file written is entry.png.
"""

import os
import struct
from pathlib import Path

ASSET_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_ASSET_BYTES = 1_048_576
MAX_DIMENSION = 1024


def main() -> None:
    asset = Path(__file__).resolve().parent / ASSET_NAME
    data = asset.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise ValueError(f"{ASSET_NAME} is not a PNG image")
    if len(data) > MAX_ASSET_BYTES:
        raise ValueError(
            f"{ASSET_NAME} is {len(data)} bytes, over the sealed gate "
            f"of {MAX_ASSET_BYTES} bytes"
        )
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise ValueError(f"{ASSET_NAME} has no PNG IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError(
            f"{ASSET_NAME} is {width}x{height}, over the sealed gate "
            f"of {MAX_DIMENSION}x{MAX_DIMENSION} pixels"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / ASSET_NAME
    tmp = out_dir / (ASSET_NAME + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(target)  # atomic: a run never leaves a partial image


if __name__ == "__main__":
    main()
