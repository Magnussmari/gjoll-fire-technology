#!/usr/bin/env python3
"""Reconcile the registry's annual fire deaths with the official HMS series, 1968-2018.

The official series (data/hms2020_official_fire_deaths_1968_2018.csv) is
digitized from the HMS 2020 report by scripts/digitize_hms2020_chart.py. This
script puts it year by year beside the registry's deaths (structure + other
tables) and writes data/hms_reconciliation_1968_2018.csv. It interprets
nothing: a difference in a year is reported as a difference, not explained.

Usage:
  python3 scripts/reconcile_hms2020.py
"""
from __future__ import annotations

import csv
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "hms_reconciliation_1968_2018.csv"


def rows(name):
    with open(DATA / name, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def reconcile() -> list[dict]:
    structure, other = Counter(), Counter()
    for r in rows("fire_incidents_deaths_structure.csv"):
        structure[int(r["year"])] += int(r["deaths"])
    for r in rows("fire_incidents_deaths_other.csv"):
        other[int(r["year"])] += int(r["deaths"])
    out = []
    for h in rows("hms2020_official_fire_deaths_1968_2018.csv"):
        y = int(h["year"])
        reg = structure[y] + other[y]
        off = int(h["deaths_total"])
        out.append({"year": y, "official_total": off,
                    "official_buildings": int(h["deaths_buildings"]),
                    "registry_total": reg, "registry_structure": structure[y],
                    "difference_registry_minus_official": reg - off})
    return out


def main() -> int:
    out = reconcile()
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    off = sum(r["official_total"] for r in out)
    reg = sum(r["registry_total"] for r in out)
    eq = sum(r["difference_registry_minus_official"] == 0 for r in out)
    print(f"  wrote {OUT.relative_to(ROOT)}: official {off}, registry {reg}, "
          f"{eq}/{len(out)} years equal")
    for r in out:
        d = r["difference_registry_minus_official"]
        if d:
            print(f"    {r['year']}: official {r['official_total']}, registry {r['registry_total']} ({d:+d})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
