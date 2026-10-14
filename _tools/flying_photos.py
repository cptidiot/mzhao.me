#!/usr/bin/env python3
"""Prepare photos for /flying.

    python3 _tools/flying_photos.py ~/Downloads/flying-photos

For every image in the source folder this writes three web sizes
(600 / 1200 / 2400 px on the long edge) to flying/photos/ and records it in
flying/photos.json. All EXIF metadata, GPS included, is dropped from the
published files; only the capture date is kept, in the manifest. Photos
without a capture date go to the end of the wall and show no date.

Re-running is incremental: photos already in the manifest (matched by source
file name) are skipped, new ones are appended, and the wall is re-sorted by
capture date. Hand-written "alt" and "caption" fields are preserved.

Needs Pillow (pip install pillow). HEIC files also need pillow-heif.
"""

import argparse
import base64
import io
import json
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "flying"
PHOTOS = OUT / "photos"
MANIFEST = OUT / "photos.json"
EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".tif", ".tiff", ".webp"}
SIZES = (600, 1200, 2400)


def capture_date(img):
    exif = img.getexif()
    raw = exif.get_ifd(0x8769).get(36867) or exif.get(306)  # DateTimeOriginal, DateTime
    try:
        return datetime.strptime(str(raw).strip()[:19], "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%dT%H:%M")
    except ValueError:
        return ""


def save_jpeg(img, dest, icc, quality):
    img.save(dest, "JPEG", quality=quality, optimize=True, progressive=True,
             subsampling="4:2:0", icc_profile=icc)


def process(path, pid):
    with Image.open(path) as src:
        date = capture_date(src)
        icc = src.info.get("icc_profile")
        img = ImageOps.exif_transpose(src).convert("RGB")

    w, h = img.size
    for size in SIZES:
        scale = min(1, size / max(w, h))
        out = img if scale == 1 else img.resize(
            (round(w * scale), round(h * scale)), Image.LANCZOS)
        save_jpeg(out, PHOTOS / f"{pid}-{size}.jpg", icc,
                  quality=86 if size == SIZES[-1] else 80)

    # 24px-wide blur-up placeholder, inlined in the manifest
    tiny = img.resize((24, max(1, round(24 * h / w))), Image.LANCZOS)
    buf = io.BytesIO()
    tiny.save(buf, "JPEG", quality=60)
    lqip = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

    r, g, b = img.resize((1, 1), Image.BOX).getpixel((0, 0))
    return {
        "id": pid,
        "w": w,
        "h": h,
        "date": date,
        "color": f"#{r:02x}{g:02x}{b:02x}",
        "lqip": lqip,
        "alt": "",
        "caption": "",
        "source": path.name,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("src", type=Path, help="folder of original photos")
    args = ap.parse_args()

    files = sorted(p for p in args.src.iterdir()
                   if p.is_file() and p.suffix.lower() in EXTS)
    if not files:
        sys.exit(f"No images found in {args.src}")

    PHOTOS.mkdir(parents=True, exist_ok=True)
    photos = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else []
    known = {p["source"] for p in photos}
    next_id = max((int(p["id"]) for p in photos), default=0) + 1

    added = 0
    for path in files:
        if path.name in known:
            continue
        pid = f"{next_id:02d}"
        print(f"  {path.name} -> {pid}")
        photos.append(process(path, pid))
        next_id += 1
        added += 1

    photos.sort(key=lambda p: (p["date"] or "~", p["source"]))  # undated last
    MANIFEST.write_text(json.dumps(photos, indent=1, ensure_ascii=False) + "\n")
    print(f"Added {added}, {len(photos)} photos total -> {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
