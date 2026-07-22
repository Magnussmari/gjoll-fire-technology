#!/usr/bin/env python3
"""Completeness reconciliation: Gjöll registry vs Statistics Iceland ICD-10 X00–X09.

Addresses the peer-review request for the "definitive completeness check" described in
Data and Methods. Compares the registry's annual fire-death counts (1996–2024) against
the official cause-of-death series (ICD-10 X00–X09, exposure to smoke, fire and flames)
from Statistics Iceland table MAN05302, pulled live from the PxWeb API.

The two series are NOT expected to coincide, and the direction of each discrepancy is
informative:
  * Registry > official: the registry additionally captures intentional fire deaths
    (arson/homicide, coded outside X00–X09), non-building fire deaths (ships, vehicles),
    and at least one death the official series omits (the documented 2009 zero-deaths error).
  * Official > registry: a small number of single-death years (concentrated early)
    where the official series records a death the registry did not ascertain — the
    residual early-decade under-ascertainment already disclosed as a limitation.

Writes data/icd10_reconciliation_1996_2024.csv (tracked/deposited).
Network required (Statistics Iceland PxWeb).
"""
import json, urllib.request, csv, pathlib
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://px.hagstofa.is/pxen/api/v1/en/Ibuar/Faeddirdanir/danir/danarmein/MAN05302.px"
FIRE_CODES = ["X00", "X04", "X06", "X08", "X09"]  # ICD-10 X00–X09 present in MAN05302
YEARS = list(range(1996, 2025))


def official_counts():
    q = {"query": [
        {"code": "Aldur", "selection": {"filter": "item", "values": ["0"]}},
        {"code": "Kyn", "selection": {"filter": "item", "values": ["0"]}},
        {"code": "Dánarmein", "selection": {"filter": "item", "values": FIRE_CODES}},
        {"code": "Ár", "selection": {"filter": "item", "values": [str(y) for y in YEARS]}}],
        "response": {"format": "json-stat2"}}
    req = urllib.request.Request(BASE, data=json.dumps(q).encode(),
                                 headers={"content-type": "application/json"})
    d = json.load(urllib.request.urlopen(req, timeout=60))
    arr = np.array([v or 0 for v in d["value"]]).reshape(d["size"])
    yr_ax = d["id"].index("Ár")
    labels = list(d["dimension"]["Ár"]["category"]["index"].keys())
    out = {}
    for yi, y in enumerate(labels):
        sl = [slice(None)] * len(d["id"]); sl[yr_ax] = yi
        out[int(y)] = int(arr[tuple(sl)].sum())
    return out


def registry_counts():
    reg = {}
    for fn in ["data/fire_incidents_deaths_structure.csv", "data/fire_incidents_deaths_other.csv"]:
        for r in csv.DictReader(open(ROOT / fn)):
            try:
                y = int(str(r["year"])[:4])
            except (ValueError, KeyError):
                continue
            try:
                n = int(float(r.get("deaths") or 1))
            except ValueError:
                n = 1
            if 1996 <= y <= 2024:
                reg[y] = reg.get(y, 0) + n
    return reg


def main():
    official = official_counts()
    reg = registry_counts()
    out = ROOT / "data" / "icd10_reconciliation_1996_2024.csv"
    matches = 0
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "official_X00_X09", "registry_all_fire", "match"])
        for y in YEARS:
            o, rg = official.get(y, 0), reg.get(y, 0)
            m = int(o == rg); matches += m
            w.writerow([y, o, rg, m])
    to, tr = sum(official.get(y, 0) for y in YEARS), sum(reg.get(y, 0) for y in YEARS)
    print(f"Official X00–X09 total 1996–2024: {to}")
    print(f"Registry (all fire) total 1996–2024: {tr}")
    print(f"Exact-year matches: {matches}/{len(YEARS)}")
    print(f"Registry exceeds official in {sum(reg.get(y,0)>official.get(y,0) for y in YEARS)} years; "
          f"official exceeds registry in {sum(official.get(y,0)>reg.get(y,0) for y in YEARS)} years "
          f"({[y for y in YEARS if official.get(y,0)>reg.get(y,0)]}).")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
