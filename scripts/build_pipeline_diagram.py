#!/usr/bin/env python3
"""Draw the Gjöll data pipeline from pipeline/pipeline.json, and check it.

WHY THIS EXISTS
---------------
The pipeline is described in three places: the manuscript's Methods, this
repository, and www.gjoll.is. Three descriptions of one thing is three chances
to disagree. pipeline/pipeline.json is the single record; the diagram is drawn
from it here and the website renders its pipeline page from the same file.

The numbers in that file are not trusted. `--check` recomputes every one of
them from the deposited CSVs (and counts the passing checks of
verify_statistics.py), then re-renders the diagrams and compares them byte for
byte with the committed copies. CI runs it, so the page, the figure and the data
cannot drift apart silently.

DESIGN
------
Follows the house diagram system (diagram-design, `data-flow` type): role lanes,
numbered step columns, orthogonal connectors with rounded bends, one focal node
at the start (the registry) and one at the end (the CI gate). This is a web and
repository surface, so the house skin applies; the journal figure
(figures/fig_study_design.png) keeps the journal's own spec and is untouched.

Steps run in the order the work was done, taken from the record rather than
from the manuscript's prose: the registry was compiled and cross-checked against
the official tallies (2025), analysed (March 2026), re-coded blind (14 July) and
reconciled against ICD-10 (22 July). A first version ordered them for layout
and left the official cross-check out; that is why the order is stated here.

Ten nodes, one over the skill's budget of nine. Deliberate: the two official
comparisons are separate steps done a year apart against different sources, and
merging them would hide exactly that. Folding the denominators into the
analysis node is what kept it at ten.

The AI lane holds exactly one node. That is the argument, drawn: no model
produced any reported value. The models re-applied the classification rule
blind to construction year, and their output only ever reaches a gate.

Usage:
  python3 scripts/build_pipeline_diagram.py           # write figures/pipeline*.svg (+ PNG)
  python3 scripts/build_pipeline_diagram.py --check   # verify record + figures, no writes
"""
from __future__ import annotations

import csv
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SSOT = ROOT / "pipeline" / "pipeline.json"
DATA = ROOT / "data"
OUT = ROOT / "figures"

# ── Skin (diagram-design style guide) ─────────────────────────────────────────
PAPER, INK = "#F5F0E8", "#14110D"
MUTED, SOFT = "#6E6659", "#8A7D68"
ACCENT = "#B87333"
SANS = "Archivo, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'SF Mono', SFMono-Regular, ui-monospace, Menlo, monospace"

# ── Geometry (4px grid) ───────────────────────────────────────────────────────
LABEL_COL_W, SLOT_W, RIGHT_PAD = 120, 192, 24
HEADER_H, LANE_H, LEGEND_H = 48, 88, 48
NODE_W, NODE_H, NODE_PAD = 160, 64, 12

LANES = ["SRC", "REG", "CODE", "AI", "GATE"]
LANE_NAMES = {
    "en": {"SRC": ("EXTERNAL", "SOURCES"), "REG": ("GJÖLL", "REGISTRY"),
           "CODE": ("DETERMINISTIC", "CODE"), "AI": ("LANGUAGE", "MODELS"),
           "GATE": ("VERIFICATION", "GATE")},
    "is": {"SRC": ("YTRI", "HEIMILDIR"), "REG": ("GJALLAR-", "SKRÁIN"),
           "CODE": ("ÁKVÖRÐUNAR-", "BUNDINN KÓÐI"), "AI": ("MÁL-", "LÍKÖN"),
           "GATE": ("SANNPRÓFUN", "")},
}
UI = {
    "en": {"flow": "FLOW", "hand": "Data hand-off", "ci": "Recomputed in CI",
           "chk": "κ carried from Agreement into CI",
           "descr": "DESCRIPTIONS", "reg": "REGISTRY", "every": "EVERY NUMBER",
           "kappa": "κ RECOMPUTED"},
    "is": {"flow": "FLÆÐI", "hand": "Gögn afhent", "ci": "Endurreiknað í CI",
           "chk": "κ flutt úr Samræmi í CI",
           "descr": "LÝSINGAR", "reg": "SKRÁIN", "every": "HVER TALA",
           "kappa": "κ ENDURREIKNAÐ"},
}


def nodes_for(f: dict, lang: str) -> list[dict]:
    """Node text. Every number is read from the record, never typed here."""
    en = lang == "en"
    inc, dth = f["incidents"], f["deaths"]
    return [
        {"lane": "SRC", "step": 0,
         "title": "Archives & reports" if en else "Söfn og skýrslur",
         "sub": "Tímarit.is · yearbooks" if en else "Tímarit.is · árbækur",
         "tool": "courts · investigations" if en else "dómar · rannsóknir"},
        {"lane": "REG", "step": 0, "focal": True,
         "title": "Gjöll registry" if en else "Gjallarskráin",
         "sub": f"{inc} incidents · {dth} deaths" if en else f"{inc} tilvik · {dth} látnir",
         "tool": f"{f['first_year']}–{f['last_year']} · ≥2 sources" if en
                 else f"{f['first_year']}–{f['last_year']} · ≥2 heimildir"},
        {"lane": "SRC", "step": 1,
         "title": "Official tallies" if en else "Opinberar tölur",
         "sub": f"HMS 2020 · {f['hms_window']}",
         "tool": "digitized from the chart" if en else "lesið af stöplariti"},
        {"lane": "CODE", "step": 1,
         "title": "Cross-check" if en else "Samanburður",
         "sub": f"{f['hms_official_deaths']} vs {f['hms_registry_deaths']} deaths" if en
                else f"{f['hms_official_deaths']} á móti {f['hms_registry_deaths']}",
         "tool": f"{f['hms_years_equal']}/{f['hms_years']} years equal" if en
                 else f"{f['hms_years_equal']}/{f['hms_years']} ár eins"},
        {"lane": "CODE", "step": 2,
         "title": "Analysis" if en else "Greining",
         "sub": "rates · cohorts · ITSA" if en else "tíðni · árgangar · ITSA",
         "tool": "with population, dwellings" if en else "með mannfjölda, íbúðum"},
        {"lane": "AI", "step": 3,
         "title": "Blinded re-code" if en else "Blind endurkóðun",
         "sub": f"2 models · {f['recode_incidents']} incidents" if en
                else f"2 líkön · {f['recode_incidents']} tilvik",
         "tool": "construction year hidden" if en else "byggingarár falið"},
        {"lane": "GATE", "step": 3,
         "title": "Agreement" if en else "Samræmi",
         "sub": f"{f['recode_agreement']}/{f['recode_incidents']} · κ = {f['recode_kappa']:.2f}"
                .replace(".", "." if en else ","),
         "tool": "frozen and deposited" if en else "fryst og varðveitt"},
        {"lane": "SRC", "step": 4,
         "title": "Cause-of-death data" if en else "Dánarmeinaskrá",
         "sub": "ICD-10 X00–X09",
         "tool": "Statistics Iceland" if en else "Hagstofa Íslands"},
        {"lane": "CODE", "step": 4,
         "title": "Completeness" if en else "Heimtur",
         "sub": f"{f['icd10_registry_deaths']} vs {f['icd10_official_deaths']} deaths" if en
                else f"{f['icd10_registry_deaths']} á móti {f['icd10_official_deaths']} látnum",
         "tool": f"{f['icd10_window']} · vs official" if en
                 else f"{f['icd10_window']} · á móti opinberri"},
        {"lane": "GATE", "step": 4, "focal": True,
         "title": "CI verification" if en else "Sannprófun í CI",
         "sub": f"{f['verification_checks']}/{f['verification_checks']} checks" if en
                else f"{f['verification_checks']}/{f['verification_checks']} próf",
         "tool": "on every push" if en else "við hverja breytingu"},
    ]


def fit(s: str, size: float, mono: bool = False, width: float = NODE_W - 16) -> str:
    per = size * (0.62 if mono else 0.58)
    if len(s) * per <= width:
        return s
    raise ValueError(f"label does not fit its node: {s!r} ({len(s) * per:.0f} > {width})")


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size, fill, weight="400", anchor="middle", family=SANS, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{extra}>'
            f"{esc(s)}</text>\n")


def cx(j: int) -> int:
    return LABEL_COL_W + j * SLOT_W + SLOT_W // 2


def top(lane: str) -> int:
    return HEADER_H + LANES.index(lane) * LANE_H + NODE_PAD


def mid(lane: str) -> int:
    return top(lane) + NODE_H // 2


def bottom(lane: str) -> int:
    return top(lane) + NODE_H


def right(j: int) -> int:
    return cx(j) + NODE_W // 2


def left(j: int) -> int:
    return cx(j) - NODE_W // 2


def h_then_down(x1, y1, x2, y2, r=8) -> str:
    """Horizontal, one quarter-arc, then down. No diagonals."""
    return f"M{x1},{y1} L{x2 - r},{y1} Q{x2},{y1} {x2},{y1 + r} L{x2},{y2}"


def down_then_right(x1, y1, x2, y2, r=8) -> str:
    """Down, one quarter-arc, then right. No diagonals."""
    return f"M{x1},{y1} L{x1},{y2 - r} Q{x1},{y2} {x1 + r},{y2} L{x2},{y2}"


def arrows_for(ui: dict) -> list[dict]:
    """Routing is fixed by hand and checked against the six connector rules:
    orthogonal only, no shared attach points, no crossings, and no transit
    behind a box that is not an endpoint (every lane cell crossed is empty)."""
    return [
        {"d": f"M{cx(0)},{bottom('SRC')} L{cx(0)},{top('REG')}", "style": "muted"},
        {"d": f"M{cx(1)},{bottom('SRC')} L{cx(1)},{top('CODE')}", "style": "muted"},
        # registry → cross-check: stops 24px left of the official series' arrow
        # on the same top edge, so the two never share a point.
        {"d": h_then_down(right(0), mid("REG"), cx(1) - 24, top("CODE")), "style": "muted",
         "label": ui["reg"], "lx": (right(0) + cx(1) - 24) // 2, "ly": mid("REG") - 12},
        {"d": f"M{right(1)},{mid('CODE')} L{left(2)},{mid('CODE')}", "style": "muted"},
        {"d": down_then_right(cx(2), bottom("CODE"), left(3), mid("AI")), "style": "muted",
         "label": ui["descr"], "lx": (cx(2) + left(3)) // 2 + 8, "ly": mid("AI") - 12},
        {"d": f"M{right(2)},{mid('CODE')} L{left(4)},{mid('CODE')}", "style": "muted"},
        {"d": f"M{cx(4)},{bottom('SRC')} L{cx(4)},{top('CODE')}", "style": "muted"},
        {"d": f"M{cx(3)},{bottom('AI')} L{cx(3)},{top('GATE')}", "style": "muted"},
        {"d": f"M{cx(4)},{bottom('CODE')} L{cx(4)},{top('GATE')}", "style": "accent",
         "label": ui["every"], "lx": cx(4) + 10, "ly": mid("AI") + 4, "anchor": "start"},
        {"d": f"M{right(3)},{mid('GATE')} L{left(4)},{mid('GATE')}", "style": "muted",
         "dashed": True},  # 32px gap: no room for a label; the legend names both ends
    ]


def diagram(record: dict, lang: str) -> str:
    f, ui = record["figures"], UI[lang]
    steps = record["steps"]
    W = LABEL_COL_W + len(steps) * SLOT_W + RIGHT_PAD
    lanes_end = HEADER_H + len(LANES) * LANE_H
    H = lanes_end + LEGEND_H
    slug = f"gjoll-pipeline-{lang}"
    title = ("Gjöll data pipeline" if lang == "en" else "Gagnaferli Gjallar")
    desc = ("Fatal-fire incidents are compiled from archival sources into the Gjöll "
            "registry, cross-checked against the official 1968–2018 fire-death series, "
            "analysed, re-coded blind by two language models as a reproducibility check, "
            "and reconciled against official cause-of-death statistics; every reported "
            "number is recomputed in CI."
            if lang == "en" else
            "Banvæn brunatilvik eru tekin saman úr heimildum í Gjallarskrána, borin saman "
            "við opinberar tölur um dauðsföll í eldsvoðum 1968–2018, greind, endurkóðuð "
            "blint af tveimur mállíkönum sem endurtekningarpróf og stemmd af við opinbera "
            "dánarmeinaskrá; hver birt tala er endurreiknuð í CI.")

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
         f'height="{H}" role="img" aria-labelledby="{slug}-title {slug}-desc">\n',
         f'<title id="{slug}-title">{esc(title)}</title>\n',
         f'<desc id="{slug}-desc">{esc(desc)}</desc>\n', "<defs>\n"]
    for mid_, col in (("arr-muted", MUTED), ("arr-accent", ACCENT)):
        o.append(f'<marker id="{slug}-{mid_}" markerWidth="8" markerHeight="6" refX="7" '
                 f'refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{col}"/>'
                 f"</marker>\n")
    o.append("</defs>\n")
    o.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>\n')
    # One tinted lane only: the AI lane, because its emptiness is the point.
    o.append(f'<rect x="0" y="{HEADER_H + LANES.index("AI") * LANE_H}" width="{W}" '
             f'height="{LANE_H}" fill="{INK}" opacity="0.025"/>\n')
    for k in range(len(LANES) + 1):
        y = HEADER_H + k * LANE_H
        o.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{INK}" '
                 f'stroke-opacity="0.12" stroke-width="0.8"/>\n')
    o.append(f'<line x1="{LABEL_COL_W}" y1="{HEADER_H}" x2="{LABEL_COL_W}" y2="{lanes_end}" '
             f'stroke="{INK}" stroke-opacity="0.12" stroke-width="0.8"/>\n')

    for j, s in enumerate(steps):
        x = cx(j)
        o.append(f'<rect x="{x - 16}" y="8" width="32" height="16" rx="8" fill="{INK}" '
                 f'opacity="0.10"/>\n')
        o.append(txt(x, 20, f"{j + 1:02d}", 8, INK, "700", family=MONO))
        o.append(txt(x, 40, s["label"][lang].upper(), 8, MUTED, "600",
                     extra=' letter-spacing="0.12em"'))

    for lane in LANES:
        a, b = LANE_NAMES[lang][lane]
        ym = HEADER_H + LANES.index(lane) * LANE_H + LANE_H // 2
        if b:
            o.append(txt(LABEL_COL_W // 2, ym - 2, a, 8, MUTED, "600",
                         extra=' letter-spacing="0.12em"'))
            o.append(txt(LABEL_COL_W // 2, ym + 10, b, 8, MUTED, "600",
                         extra=' letter-spacing="0.12em"'))
        else:
            o.append(txt(LABEL_COL_W // 2, ym + 4, a, 8, MUTED, "600",
                         extra=' letter-spacing="0.12em"'))

    # Arrows before nodes, labels with an opaque mask and a visible gap.
    for a in arrows_for(ui):
        col = ACCENT if a["style"] == "accent" else MUTED
        dash = ' stroke-dasharray="5,4"' if a.get("dashed") else ""
        wid = 1.2 if a["style"] == "accent" else 1
        o.append(f'<path d="{a["d"]}" fill="none" stroke="{col}" stroke-width="{wid}"{dash} '
                 f'marker-end="url(#{slug}-arr-{a["style"]})"/>\n')
        if a.get("label"):
            lab, anchor = a["label"], a.get("anchor", "middle")
            w = len(lab) * 5 + 8
            x0 = a["lx"] - 4 if anchor == "start" else a["lx"] - w / 2
            o.append(f'<rect x="{x0}" y="{a["ly"] - 9}" width="{w}" height="12" rx="2" '
                     f'fill="{PAPER}"/>\n')
            o.append(txt(a["lx"], a["ly"], lab, 8, col, "600", anchor=anchor, family=MONO,
                         extra=' letter-spacing="0.06em"'))

    for nd in nodes_for(f, lang):
        x, y, c = left(nd["step"]), top(nd["lane"]), cx(nd["step"])
        focal = nd.get("focal", False)
        o.append(f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="6" '
                 f'fill="{PAPER}"/>\n')
        if focal:
            o.append(f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="6" '
                     f'fill="{ACCENT}" fill-opacity="0.08" stroke="{ACCENT}" '
                     f'stroke-width="1.2"/>\n')
        else:
            o.append(f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="6" '
                     f'fill="#FFFFFF" fill-opacity="0.55" stroke="{INK}" '
                     f'stroke-opacity="0.35" stroke-width="1"/>\n')
        o.append(txt(c, y + 24, fit(nd["title"], 12), 12, ACCENT if focal else INK, "600"))
        o.append(txt(c, y + 40, fit(nd["sub"], 8, mono=True), 8, MUTED, family=MONO))
        o.append(txt(c, y + 54, fit(nd["tool"], 8), 8, SOFT))

    ly = lanes_end + 28
    o.append(txt(LABEL_COL_W - 12, ly, ui["flow"], 8, MUTED, "700", anchor="end",
                 extra=' letter-spacing="0.12em"'))
    lx = LABEL_COL_W + 12
    for col, style, dash, lab in ((MUTED, "muted", "", ui["hand"]),
                                  (ACCENT, "accent", "", ui["ci"]),
                                  (MUTED, "muted", ' stroke-dasharray="5,4"', ui["chk"])):
        o.append(f'<line x1="{lx}" y1="{ly - 3}" x2="{lx + 28}" y2="{ly - 3}" stroke="{col}" '
                 f'stroke-width="1.2"{dash} marker-end="url(#{slug}-arr-{style})"/>\n')
        o.append(txt(lx + 36, ly, lab, 8, MUTED, anchor="start"))
        lx += 36 + int(len(lab) * 4.6) + 28
    o.append("</svg>\n")
    return "".join(o)


# ── The check: every number in the record, recomputed from the deposit ───────
def recompute() -> dict:
    def rows(name):
        with open(DATA / name, encoding="utf-8") as fh:
            return list(csv.DictReader(fh))

    s = rows("fire_incidents_deaths_structure.csv")
    o = rows("fire_incidents_deaths_other.csv")
    years = [int(r["year"]) for r in s + o]
    icd = rows("icd10_reconciliation_1996_2024.csv")
    rc = rows("blinded_recode_codings_1996_2025.csv")
    hms = rows("hms_reconciliation_1968_2018.csv")

    def kappa(a, b):
        n = len(a)
        po = sum(x == y for x, y in zip(a, b)) / n
        cats = set(a) | set(b)
        pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
        return (po - pe) / (1 - pe)

    orig = [r["orig_coding"] for r in rc]
    agree, kap = set(), set()
    for m in ("claude_sonnet5", "openai_gpt55"):
        other = [r[m] for r in rc]
        agree.add(sum(x == y for x, y in zip(orig, other)))
        kap.add(round(kappa(orig, other), 2))
    if len(agree) != 1 or len(kap) != 1:
        raise SystemExit(f"the two models no longer agree equally: {agree} {kap}")

    sys.path.insert(0, str(ROOT / "scripts"))
    from reconcile_hms2020 import reconcile
    fresh = [{k: str(v) for k, v in r.items()} for r in reconcile()]
    if fresh != hms:
        raise SystemExit("data/hms_reconciliation_1968_2018.csv is stale: rerun reconcile_hms2020.py")

    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "verify_statistics.py")],
                         capture_output=True, text=True, cwd=ROOT)
    m = re.search(r"(\d+)/(\d+) checks passed", out.stdout)
    if out.returncode != 0 or not m or m.group(1) != m.group(2):
        raise SystemExit("verify_statistics.py did not pass cleanly")

    return {
        "incidents": len(s) + len(o),
        "structure_incidents": len(s),
        "other_incidents": len(o),
        "deaths": sum(int(r["deaths"]) for r in s + o),
        "first_year": min(years),
        "last_year": max(years),
        "icd10_window": f"{icd[0]['year']}–{icd[-1]['year']}",
        "icd10_registry_deaths": sum(int(r["registry_all_fire"]) for r in icd),
        "icd10_official_deaths": sum(int(r["official_X00_X09"]) for r in icd),
        "hms_window": f"{hms[0]['year']}–{hms[-1]['year']}",
        "hms_years": len(hms),
        "hms_official_deaths": sum(int(r["official_total"]) for r in hms),
        "hms_registry_deaths": sum(int(r["registry_total"]) for r in hms),
        "hms_years_equal": sum(r["difference_registry_minus_official"] == "0" for r in hms),
        "recode_incidents": len(rc),
        "recode_agreement": agree.pop(),
        "recode_kappa": kap.pop(),
        "verification_checks": int(m.group(2)),
    }


def main() -> int:
    check = "--check" in sys.argv
    record = json.loads(SSOT.read_text(encoding="utf-8"))
    actual = recompute()
    drift = {k: (record["figures"].get(k), v) for k, v in actual.items()
             if record["figures"].get(k) != v}
    if drift:
        for k, (said, is_) in drift.items():
            print(f"  ✗ pipeline.json says {k} = {said!r}, the deposited data says {is_!r}")
        return 1
    print(f"  ✓ all {len(actual)} figures in pipeline.json match the deposited data")

    stale = []
    for lang, name in (("en", "pipeline.svg"), ("is", "pipeline.is.svg")):
        svg = diagram(record, lang)
        path = OUT / name
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != svg:
                stale.append(name)
            continue
        path.write_text(svg, encoding="utf-8")
        print(f"  wrote figures/{name}")
        if shutil.which("rsvg-convert"):
            png = path.with_suffix(".png")
            subprocess.run(["rsvg-convert", "-z", "3", "-o", str(png), str(path)], check=True)
            print(f"  wrote figures/{png.name}")
    if stale:
        print(f"  ✗ out of date, rerun this script: {', '.join(stale)}")
        return 1
    if check:
        print("  ✓ figures/pipeline*.svg are current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
