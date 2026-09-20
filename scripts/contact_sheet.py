"""Build a labelled contact sheet from a set of stills.

Usage:
    python scripts/contact_sheet.py <out.png> <label> <img1> [<img2> ...]

Lays images out in a grid (2 columns for up to 4 images, 3 columns above that),
downscaled so the sheet stays under ~2500px wide, with the filename stem
stamped in the top-left corner of each tile.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    out = Path(sys.argv[1])
    label = sys.argv[2]
    paths = [Path(p) for p in sys.argv[3:]]
    if not paths:
        sys.exit("no images given")

    cols = 2 if len(paths) <= 4 else 3
    rows = (len(paths) + cols - 1) // cols
    tile_w = 1200
    gutter = 16
    header = 64

    images = [Image.open(p).convert("RGB") for p in paths]
    tile_h = round(tile_w * images[0].height / images[0].width)

    sheet_w = cols * tile_w + (cols + 1) * gutter
    sheet_h = header + rows * tile_h + (rows + 1) * gutter
    sheet = Image.new("RGB", (sheet_w, sheet_h), (24, 24, 24))
    draw = ImageDraw.Draw(sheet)

    try:
        font_big = ImageFont.truetype("arial.ttf", 40)
        font = ImageFont.truetype("arial.ttf", 34)
    except OSError:
        font_big = font = ImageFont.load_default()

    draw.text((gutter, 14), label, fill=(240, 240, 240), font=font_big)

    for i, (img, p) in enumerate(zip(images, paths)):
        r, c = divmod(i, cols)
        x = gutter + c * (tile_w + gutter)
        y = header + gutter + r * (tile_h + gutter)
        tile = img.resize((tile_w, tile_h), Image.LANCZOS)
        sheet.paste(tile, (x, y))
        tag = p.stem
        tw = draw.textlength(tag, font=font)
        draw.rectangle([x, y, x + tw + 24, y + 50], fill=(0, 0, 0))
        draw.text((x + 12, y + 6), tag, fill=(255, 255, 255), font=font)

    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, optimize=True)
    print(out)


if __name__ == "__main__":
    main()
