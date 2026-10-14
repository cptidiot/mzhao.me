#!/usr/bin/env python3
"""Prepare photos for /flying.

    python3 _tools/flying_photos.py ~/Downloads/flying-photos

For every image in the source folder this writes three web sizes
(600 / 1200 / 2400 px on the long edge) to flying/photos/ and records it in
flying/photos.json. All EXIF metadata, GPS included, is dropped from the
published files; only the capture date is kept, in the manifest.

It also redraws assets/flying.png, the photo-stack icon on the home page,
from three photos (the first three on the wall, or --icon 05,12,30).

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

from PIL import Image, ImageDraw, ImageFilter, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "flying"
PHOTOS = OUT / "photos"
MANIFEST = OUT / "photos.json"
ICON = ROOT / "assets" / "flying.png"
EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".tif", ".tiff", ".webp"}
SIZES = (600, 1200, 2400)


def capture_date(img, path):
    exif = img.getexif()
    raw = exif.get_ifd(0x8769).get(36867) or exif.get(306)  # DateTimeOriginal, DateTime
    if raw:
        try:
            return datetime.strptime(str(raw).strip()[:19], "%Y:%m:%d %H:%M:%S")
        except ValueError:
            pass
    return datetime.fromtimestamp(path.stat().st_mtime)


def save_jpeg(img, dest, icc, quality):
    img.save(dest, "JPEG", quality=quality, optimize=True, progressive=True,
             subsampling="4:2:0", icc_profile=icc)


def process(path, pid):
    with Image.open(path) as src:
        date = capture_date(src, path)
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
        "date": date.strftime("%Y-%m-%dT%H:%M"),
        "color": f"#{r:02x}{g:02x}{b:02x}",
        "lqip": lqip,
        "alt": "",
        "caption": "",
        "source": path.name,
    }


def make_icon(ids):
    """Three photos fanned like loose prints, on a transparent canvas."""
    S = 4                                   # supersample, then downscale
    size = 360 * S
    pw, ph = 104 * S, 130 * S
    border = 5 * S
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    for pid, angle, dx, dy in zip(ids, (-11, 9, -1), (-27, 27, 0), (6, 3, 0)):
        with Image.open(PHOTOS / f"{pid}-600.jpg") as im:
            photo = ImageOps.fit(im.convert("RGB"), (pw, ph), Image.LANCZOS)
        card = Image.new("RGBA", (pw + border * 2, ph + border * 2), (255, 255, 255, 255))
        card.paste(photo, (border, border))
        mask = Image.new("L", card.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, card.width - 1, card.height - 1], radius=4 * S, fill=255)
        card.putalpha(mask)
        card = card.rotate(angle, resample=Image.BICUBIC, expand=True)

        shadow = Image.new("RGBA", card.size, (20, 24, 30, 0))
        shadow.putalpha(card.getchannel("A").point(lambda a: int(a * 0.22)))
        shadow = shadow.filter(ImageFilter.GaussianBlur(5 * S))
        x = (size - card.width) // 2 + dx * S
        y = (size - card.height) // 2 + dy * S
        canvas.alpha_composite(shadow, (x, y + 4 * S))
        canvas.alpha_composite(card, (x, y))

    # Crop to the cards plus a little room for the shadow.
    l, t, r, b = canvas.getchannel("A").point(lambda a: 255 if a > 200 else 0).getbbox()
    m = 8 * S
    canvas = canvas.crop((l - m, t - m, r + m, b + m))
    canvas = canvas.resize((canvas.width // S, canvas.height // S), Image.LANCZOS)
    ICON.parent.mkdir(exist_ok=True)
    canvas.save(ICON, optimize=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("src", type=Path, help="folder of original photos")
    ap.add_argument("--icon", help="comma-separated photo ids for the home-page icon")
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

    photos.sort(key=lambda p: (p["date"], p["source"]))
    MANIFEST.write_text(json.dumps(photos, indent=1, ensure_ascii=False) + "\n")
    print(f"Added {added}, {len(photos)} photos total -> {MANIFEST.relative_to(ROOT)}")

    ids = args.icon.split(",") if args.icon else [p["id"] for p in photos[:3]]
    if len(ids) == 3:
        make_icon(ids)
        print(f"Icon from {', '.join(ids)} -> {ICON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
