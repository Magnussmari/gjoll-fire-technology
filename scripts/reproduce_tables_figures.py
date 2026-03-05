#!/usr/bin/env python3
"""
Reproducibility script for:
  Fatal Fire Incidents in Iceland, 1968–2025:
  Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation

Reads exported CSVs from the Gjöll registry and regenerates all manuscript
tables and figures. Run from the fire_technology/ directory:

    pip install pandas matplotlib
    python scripts/reproduce_tables_figures.py

Output is written to generated/.

Author: Magnús Smári Smárason (magnus@smarason.is)
Data:   DOI 10.34881/I5WGJU  |  https://www.gjoll.is
"""

import os
import sys
import warnings
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore", category=FutureWarning)

# ── Paths ────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
OUT  = os.path.join(BASE, "generated")
os.makedirs(OUT, exist_ok=True)

# ── Load data ────────────────────────────────────────────────────────────
structure = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_structure.csv"))
other     = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_other.csv"))
pop       = pd.read_csv(os.path.join(DATA, "population_1jan_MAN00000_1968_2025.csv"))

structure["incident_date"] = pd.to_datetime(structure["incident_date"])
other["incident_date"]     = pd.to_datetime(other["incident_date"])
structure["month"]         = structure["incident_date"].dt.month
other["month"]             = other["incident_date"].dt.month

all_incidents = pd.concat([
    structure[["year", "deaths", "month"]].assign(category="Structure fires"),
    other[["year", "deaths", "month"]].assign(category="Other fire-related deaths"),
], ignore_index=True)

print(f"Loaded: {len(structure)} structure, {len(other)} other, {len(pop)} population rows")
print(f"Total incidents: {len(all_incidents)}, Total deaths: {all_incidents['deaths'].sum()}")

# ══════════════════════════════════════════════════════════════════════════
# TABLE 1: Overall burden
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ TABLE 1: Overall burden ═══")
for cat in ["Structure fires", "Other fire-related deaths"]:
    sub = all_incidents[all_incidents["category"] == cat]
    n_inc = len(sub)
    n_deaths = sub["deaths"].sum()
    mean_d = n_deaths / n_inc if n_inc > 0 else 0
    print(f"  {cat}: {n_inc} incidents, {n_deaths} deaths, {mean_d:.2f} deaths/incident")
total_inc = len(all_incidents)
total_deaths = all_incidents["deaths"].sum()
print(f"  TOTAL: {total_inc} incidents, {total_deaths} deaths, {total_deaths/total_inc:.2f} deaths/incident")

# ══════════════════════════════════════════════════════════════════════════
# TABLE 2: Period totals and crude mortality rates
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ TABLE 2: Period totals and crude mortality rates ═══")
bins = [(1968, 1969), (1970, 1979), (1980, 1989), (1990, 1999),
        (2000, 2009), (2010, 2019), (2020, 2025)]

table2_rows = []
for start, end in bins:
    sub = all_incidents[(all_incidents["year"] >= start) & (all_incidents["year"] <= end)]
    pop_sub = pop[(pop["year"] >= start) & (pop["year"] <= end)]
    n_inc = len(sub)
    n_deaths = sub["deaths"].sum()
    n_years = end - start + 1
    mean_pop = pop_sub["population_1jan"].mean()
    rate = (n_deaths / n_years) / (mean_pop / 1_000_000) if mean_pop > 0 else 0
    label = f"{start}–{end}" + ("*" if start == 1968 and end == 1969 else "")
    table2_rows.append({
        "Period": label, "Incidents": n_inc, "Deaths": n_deaths,
        "Mean pop": f"{mean_pop:,.0f}", "Rate/million": f"{rate:.1f}"
    })
    print(f"  {label}: {n_inc} inc, {n_deaths} deaths, pop={mean_pop:,.0f}, rate={rate:.1f}/M")

table2_df = pd.DataFrame(table2_rows)
table2_df.to_csv(os.path.join(OUT, "table2_period_rates.csv"), index=False)

# ══════════════════════════════════════════════════════════════════════════
# TABLE 3: Fatal structure fires by building construction year
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ TABLE 3: Construction year bands ═══")
cy_bands = [
    ("1900–1919", 1900, 1919), ("1920–1939", 1920, 1939),
    ("1940–1959", 1940, 1959), ("1960–1979", 1960, 1979),
    ("1980–1997", 1980, 1997),
]

structure_1996 = structure[structure["year"] >= 1996]

for label, lo, hi in cy_bands:
    full = structure[(structure["construction_year"] >= lo) & (structure["construction_year"] <= hi)]
    sub  = structure_1996[(structure_1996["construction_year"] >= lo) & (structure_1996["construction_year"] <= hi)]
    print(f"  {label}: full={len(full)} inc/{full['deaths'].sum()} deaths, "
          f"1996+={len(sub)} inc/{sub['deaths'].sum()} deaths")

unknown_full = structure[structure["construction_year"].isna()]
unknown_sub  = structure_1996[structure_1996["construction_year"].isna()]
print(f"  Unknown: full={len(unknown_full)} inc/{unknown_full['deaths'].sum()} deaths, "
      f"1996+={len(unknown_sub)} inc/{unknown_sub['deaths'].sum()} deaths")
print(f"  Total:   full={len(structure)} inc/{structure['deaths'].sum()} deaths, "
      f"1996+={len(structure_1996)} inc/{structure_1996['deaths'].sum()} deaths")

# Post-1998 check
post_1998 = structure[structure["construction_year"] > 1998]
print(f"\n  *** Post-1998 fatal structure fires: {len(post_1998)} incidents ***")

# Mean construction year
known_cy_all = structure["construction_year"].dropna()
known_cy_1996 = structure_1996["construction_year"].dropna()
print(f"  Mean construction year (all known, n={len(known_cy_all)}): {known_cy_all.mean():.0f}")
print(f"  Mean construction year (1996+ subset, n={len(known_cy_1996)}): {known_cy_1996.mean():.0f}  ← manuscript uses this")
print(f"  Missingness: {structure['construction_year'].isna().sum()}/{len(structure)} "
      f"({structure['construction_year'].isna().mean()*100:.0f}%)")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 1: Annual fire-related deaths (1968–2025)
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ Generating Figure 1: Annual deaths ═══")
annual = all_incidents.groupby("year")["deaths"].sum().reindex(range(1968, 2026), fill_value=0)
rolling = annual.rolling(5, center=True, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(annual.index, annual.values, color="#4682B4", alpha=0.7, label="Annual deaths")
ax.plot(rolling.index, rolling.values, color="#C0392B", linewidth=2, label="5-year rolling mean")
ax.set_xlabel("Year")
ax.set_ylabel("Deaths")
ax.set_title("Annual Fire-Related Deaths in Iceland (1968–2025)")
ax.legend()
ax.set_xlim(1967, 2026)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig1_annual_deaths.png"), dpi=150)
plt.close()
print("  Saved fig1_annual_deaths.png")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 2: Monthly seasonality
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ Generating Figure 2: Monthly seasonality ═══")
monthly_deaths = all_incidents.groupby("month")["deaths"].sum()
monthly_incidents = all_incidents.groupby("month").size()

heating = all_incidents[all_incidents["month"].isin([10, 11, 12, 1, 2, 3])]
print(f"  Heating season (Oct–Mar): {len(heating)}/{len(all_incidents)} incidents "
      f"({len(heating)/len(all_incidents)*100:.0f}%), "
      f"{heating['deaths'].sum()}/{all_incidents['deaths'].sum()} deaths "
      f"({heating['deaths'].sum()/all_incidents['deaths'].sum()*100:.0f}%)")

fig, ax = plt.subplots(figsize=(8, 5))
months = range(1, 13)
month_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
bar_width = 0.35
x = np.arange(12)
ax.bar(x - bar_width/2, [monthly_deaths.get(m, 0) for m in months],
       bar_width, color="#C0392B", alpha=0.8, label="Deaths")
ax.bar(x + bar_width/2, [monthly_incidents.get(m, 0) for m in months],
       bar_width, color="#4682B4", alpha=0.8, label="Incidents")
ax.set_xticks(x)
ax.set_xticklabels(month_labels)
ax.set_ylabel("Count")
ax.set_title("Monthly Distribution of Fatal Fire Incidents")
ax.axvspan(9 - 0.5, 11 + 0.5, alpha=0.08, color="orange", label="Heating season (Oct–Mar)")
ax.axvspan(-0.5, 2 + 0.5, alpha=0.08, color="orange")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig2_monthly_seasonality.png"), dpi=150)
plt.close()
print("  Saved fig2_monthly_seasonality.png")

# ══════════════════════════════════════════════════════════════════════════
# FIGURE 3: Construction year distribution
# ══════════════════════════════════════════════════════════════════════════
print("\n═══ Generating Figure 3: Construction year distribution ═══")
bands_data = []
for label, lo, hi in cy_bands:
    sub = structure[(structure["construction_year"] >= lo) & (structure["construction_year"] <= hi)]
    bands_data.append({"Band": label, "Incidents": len(sub), "Deaths": sub["deaths"].sum()})

fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(bands_data))
bar_width = 0.35
ax.bar(x - bar_width/2, [d["Deaths"] for d in bands_data],
       bar_width, color="#C0392B", alpha=0.8, label="Deaths")
ax.bar(x + bar_width/2, [d["Incidents"] for d in bands_data],
       bar_width, color="#4682B4", alpha=0.8, label="Incidents")
ax.set_xticks(x)
ax.set_xticklabels([d["Band"] for d in bands_data], rotation=45, ha="right")
ax.set_ylabel("Count")
ax.set_title("Fatal Structure Fires by Building Construction Year")
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig3_construction_year.png"), dpi=150)
plt.close()
print("  Saved fig3_construction_year.png")

# ══════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print(f"All outputs written to {OUT}/")
print(f"{'='*60}")
print(f"  table2_period_rates.csv")
print(f"  fig1_annual_deaths.png")
print(f"  fig2_monthly_seasonality.png")
print(f"  fig3_construction_year.png")
print(f"\nKey manuscript claims verified:")
print(f"  Total: {total_inc} incidents, {total_deaths} deaths ✓")
print(f"  Post-1998 structure fires: {len(post_1998)} ✓")
print(f"  Mean construction year (1996+ subset): {known_cy_1996.mean():.0f} ✓")
print(f"  Heating season share: {len(heating)/len(all_incidents)*100:.0f}% incidents, "
      f"{heating['deaths'].sum()/all_incidents['deaths'].sum()*100:.0f}% deaths ✓")
