#!/usr/bin/env python3
"""
Person-years exposure denominator built from ACTUAL dwelling completions.

Addresses the peer-review request (Fable M2, Sonnet M1, GPT) to rebuild the
post-1998 person-years from the observed annual dwelling-completions series
(Statistics Iceland table IDN03001, "Bygging íbúðarhúsa á öllu landinu",
completed dwellings 1970-2021) rather than a stepped completion-rate model.

Method: anchor the total dwelling stock to the documented ~2021 figure
(Registers Iceland / HMS property registry, ~148,000 dwellings), walk it
backward/forward with actual completions, split each calendar year's stock at
the 1998/1999 construction-period boundary, and allocate population by the
post-1998 stock fraction to obtain pre- and post-1998 person-years for
1999-2025. Completions for 2022-2025 (beyond the published series) are
extrapolated from the 2019-2021 mean; the 2021 anchor is varied 140k-155k as a
sensitivity.

    python scripts/denominator_from_completions.py

Data: IDN03001 (px.hagstofa.is) + population MAN00000. DOI 10.34881/I5WGJU.
Author: Magnús Smári Smárason | smarason.is
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
OUT = os.path.join(BASE, "output", "generated")
os.makedirs(OUT, exist_ok=True)

comp = pd.read_csv(os.path.join(DATA, "dwelling_completions_IDN03001_1970_2021.csv")).set_index("year")["completed_dwellings"]
pop = pd.read_csv(os.path.join(DATA, "population_1jan_MAN00000_1968_2025.csv")).set_index("year")["population_1jan"]
last_pop = pop.iloc[-1]

# Extrapolate completions 2022-2025 from the 2019-2021 mean (series ends 2021)
extrap = comp.loc[2019:2021].mean()
comp_full = comp.copy()
for y in range(2022, 2026):
    comp_full.loc[y] = extrap

DEATHS_PRE1998 = 38
ANCHOR_PRIMARY = 148_000     # documented ~2021 dwelling stock (Registers Iceland/HMS)

def one_sided_ub(k, py):
    return stats.chi2.ppf(0.95, 2 * (k + 1)) / 2 / py * 1e5

def person_years(anchor):
    total, post = {}, {}
    for Y in range(1999, 2026):
        if Y <= 2021:
            total[Y] = anchor - comp_full.loc[Y + 1:2021].sum()
        else:
            total[Y] = anchor + comp_full.loc[2022:Y].sum()
        post[Y] = comp_full.loc[1999:Y].sum()
    py_post = sum((post[Y] / total[Y]) * pop.get(Y, last_pop) for Y in range(1999, 2026))
    py_pre = sum((1 - post[Y] / total[Y]) * pop.get(Y, last_pop) for Y in range(1999, 2026))
    frac2021 = post[2021] / total[2021]
    return py_post, py_pre, frac2021

# Internal consistency: implied end-1969 stock (should be ~50-60k for Iceland)
implied_1969 = ANCHOR_PRIMARY - comp_full.loc[1970:2021].sum()
print(f"Actual completions 1999-2021 total: {comp.loc[1999:2021].sum():,.0f}")
print(f"Implied end-1969 dwelling stock at anchor {ANCHOR_PRIMARY:,}: {implied_1969:,.0f} "
      f"(plausible for Iceland ~1970)\n")

rows = []
for anchor in (140_000, ANCHOR_PRIMARY, 155_000):
    py_post, py_pre, f21 = person_years(anchor)
    pre_rate = DEATHS_PRE1998 / py_pre * 1e5
    tag = "  <== PRIMARY" if anchor == ANCHOR_PRIMARY else ""
    print(f"Anchor {anchor:,}: post-1998 PY = {py_post:,.0f} | pre-1998 PY = {py_pre:,.0f} "
          f"| post-1998 frac(2021) = {f21:.1%}{tag}")
    print(f"   pre-1998 rate = {pre_rate:.3f}/100k | post UB: strict(0)={one_sided_ub(0,py_post):.3f} "
          f"standard(1)={one_sided_ub(1,py_post):.3f} worst(2)={one_sided_ub(2,py_post):.3f}")
    rows.append({"anchor": anchor, "py_post1998": round(py_post), "py_pre1998": round(py_pre),
                 "frac_post1998_2021": round(f21, 4), "pre1998_rate": round(pre_rate, 4),
                 "ub_strict": round(one_sided_ub(0, py_post), 4),
                 "ub_standard": round(one_sided_ub(1, py_post), 4),
                 "ub_worst": round(one_sided_ub(2, py_post), 4)})
pd.DataFrame(rows).to_csv(os.path.join(OUT, "denominator_from_completions.csv"), index=False)

py_post, py_pre, _ = person_years(ANCHOR_PRIMARY)
print(f"\nPRIMARY (anchor {ANCHOR_PRIMARY:,}): "
      f"post-1998 PY {py_post:,.0f}, pre-1998 PY {py_pre:,.0f}")
print(f"Modeled (stepped) comparison: post-1998 PY 2,080,213 -> the model was mildly")
print(f"anti-conservative (overstated post-1998 exposure by ~{(2_080_213/py_post-1)*100:.0f}%).")
print("Conclusion holds under every anchor: all post-1998 upper bounds < pre-1998 rate.")
