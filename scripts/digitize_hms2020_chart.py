#!/usr/bin/env python3
"""Digitize the official 1968-2018 fire-death series from the HMS 2020 report.

SOURCE
------
"Skýrsla starfshóps um brunamál" (Húsnæðis- og mannvirkjastofnun, 2020),
printed page 6 (PDF page 7): a stacked bar chart of fire deaths in Iceland
1968-2018, blue = in buildings ("Fjöldi í húsum"), red = elsewhere
("Annarsstaðar"). The report publishes the series only as this chart; no table
of the values exists in it.

  PDF    sha256 6d2aa5f31587422142b6e3b1369329f7b08ad16aa59fba5f162069d76ec5daa2
  chart  sha256 375a9240f64bfd85db3688a83d3b84a978f2284713e19c56e6103eeaa252c788
         (image 4 on PDF page 7, 1767x1090 JPEG, as extracted by `pdfimages -j`)

METHOD
------
Nothing is read by eye. The gridlines (0, 2, ..., 12) are located from their
pixel rows, which fixes the scale. Each of the 51 year slots is sampled at its
centre column; the topmost blue and red pixels give the heights of the two
segments. The series is integer-valued, so every reading must land on a whole
number: the script fails if any reading is further than 0.1 from one. On the
source chart the largest residual is 0.03 units (about 2 pixels).

Usage:
  python3 scripts/digitize_hms2020_chart.py <Skýrsla_HMS2020.pdf | chart.jpg>
writes data/hms2020_official_fire_deaths_1968_2018.csv
"""
from __future__ import annotations

import csv
import hashlib
import pathlib
import subprocess
import sys
import tempfile

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "hms2020_official_fire_deaths_1968_2018.csv"
CHART_SHA256 = "375a9240f64bfd85db3688a83d3b84a978f2284713e19c56e6103eeaa252c788"
FIRST, LAST = 1968, 2018


def chart_from(src: pathlib.Path) -> pathlib.Path:
    if src.suffix.lower() != ".pdf":
        return src
    tmp = pathlib.Path(tempfile.mkdtemp())
    subprocess.run(["pdfimages", "-f", "7", "-l", "7", "-j", str(src), str(tmp / "p")],
                   check=True)
    return tmp / "p-002.jpg"


def blue(c):
    r, g, b = c
    return b > 150 and r < 120 and g < 160 and b - r > 60


def red(c):
    r, g, b = c
    return r > 150 and g < 110 and b < 110


def gray(c):
    r, g, b = c
    return 200 < r < 235 and abs(r - g) < 8 and abs(g - b) < 8


def main() -> int:
    chart = chart_from(pathlib.Path(sys.argv[1]))
    digest = hashlib.sha256(chart.read_bytes()).hexdigest()
    if digest != CHART_SHA256:
        raise SystemExit(f"chart image hash {digest} is not the documented source")
    im = Image.open(chart).convert("RGB")
    W, H = im.size
    px = im.load()

    rows = [y for y in range(H) if sum(gray(px[x, y]) for x in range(100, 1700, 10)) > 100]
    grid: list[list[int]] = []
    for y in rows:
        if not grid or y - grid[-1][-1] > 2:
            grid.append([y])
        else:
            grid[-1].append(y)
    lines = [sum(g) / len(g) for g in grid]
    if len(lines) != 7:
        raise SystemExit(f"expected 7 gridlines (0..12 by 2), found {len(lines)}")
    y0, y12 = lines[-1], lines[0]
    unit = (y0 - y12) / 12

    yb = int(y0) - 3
    runs, start = [], None
    for x in range(W):
        on = blue(px[x, yb]) or red(px[x, yb])
        if on and start is None:
            start = x
        if not on and start is not None:
            runs.append((start, x - 1))
            start = None
    x_first = sum(runs[0]) / 2
    x_last = sum(runs[-1]) / 2
    pitch = (x_last - x_first) / (LAST - FIRST)

    out, worst = [], 0.0
    for i, year in enumerate(range(FIRST, LAST + 1)):
        xc = int(round(x_first + i * pitch))
        top_b = top_r = None
        for y in range(int(y12) - 40, int(y0) + 1):
            c = px[xc, y]
            if top_r is None and red(c):
                top_r = y
            if top_b is None and blue(c):
                top_b = y
        tops = [t for t in (top_b, top_r) if t is not None]
        total = (y0 - min(tops)) / unit if tops else 0.0
        build = (y0 - top_b) / unit if top_b is not None else 0.0
        for v in (total, build):
            worst = max(worst, abs(v - round(v)))
        b, t = round(build), round(total)
        out.append({"year": year, "deaths_buildings": b, "deaths_elsewhere": t - b,
                    "deaths_total": t})
    if worst > 0.1:
        raise SystemExit(f"a reading is {worst:.2f} from a whole number: scale or colours off")

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    print(f"  wrote {OUT.relative_to(ROOT)}: {len(out)} years, "
          f"{sum(r['deaths_total'] for r in out)} deaths, max residual {worst:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
