"""make.fun news-image-20261120 entry: writes the committed entry.png (drawn by render.py) to the output dir.

Offline, standard library only. Run: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).with_name("entry.png"), out / "entry.png")
