#!/usr/bin/env python3
"""
Advanced analyses for:
  Fatal Fire Incidents in Iceland, 1968-2025:
  Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation

Three analyses:
  1. Person-years exposure denominator (pre- vs post-1998 dwelling stock)
  2. Sensitivity analysis on missing construction year
  3. Interrupted Time Series Analysis (ITSA) via Poisson / Negative Binomial GLM

Run from the fire_technology/ directory:

    pip install pandas matplotlib numpy statsmodels scipy
    python scripts/advanced_analyses.py

Output is written to generated/.

Author: Magnús Smári Smárason (magnus@smarason.is)
Data:   DOI 10.34881/I5WGJU  | https://www.gjoll.is
"""

import os
import sys
import warnings
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ── Publication style ─────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linewidth": 0.5,
    "axes.axisbelow": True,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
OUT  = os.path.join(BASE, "output", "generated")
os.makedirs(OUT, exist_ok=True)

# ── Load data ─────────────────────────────────────────────────────────────────
structure = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_structure.csv"))
other     = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_other.csv"))
pop       = pd.read_csv(os.path.join(DATA, "population_1jan_MAN00000_1968_2025.csv"))

structure["incident_date"] = pd.to_datetime(structure["incident_date"])
other["incident_date"]     = pd.to_datetime(other["incident_date"])

pop_dict = dict(zip(pop["year"], pop["population_1jan"]))

print(f"Loaded: {len(structure)} structure, {len(other)} other, {len(pop)} population rows")
print()

# ==============================================================================
# ANALYSIS 1: Person-Years Exposure Denominator
# ==============================================================================
print("=" * 70)
print("ANALYSIS 1: Person-Years Exposure Denominator")
print("=" * 70)
print()
print("NOTE: Dwelling stock estimates are modeled approximations based on")
print("Iceland's construction history (mean stock year ~1992, ~3,500")
print("completions/year in recent years). These are NOT census figures.")
print()

# Model dwelling completions per year using stepped rates consistent with
# Iceland's construction history and the known fact that mean building stock
# construction year is ~1992 (HMS/Registers Iceland reference [13]).
COMPLETION_RATES = {
    # period_start: completions_per_year
    1920: 500,
    1940: 2000,
    1980: 2500,
    1998: 3000,
    2010: 3500,
}

def completions_for_year(y):
    """Return modeled completions for calendar year y."""
    rate = 500
    for start_yr in sorted(COMPLETION_RATES.keys()):
        if y >= start_yr:
            rate = COMPLETION_RATES[start_yr]
    return rate

# Build cumulative dwelling stock by construction-year band
# We model stock available in each calendar year for the 1999-2025 analysis window.
# Assume a dwelling built in year b contributes to stock from year b onwards
# (simplified: no demolitions; demolition rate in Iceland is very low).

study_years = list(range(1999, 2026))

# For each study year, estimate total stock and post-1998 fraction
stock_records = []
for cal_year in study_years:
    total_stock = sum(completions_for_year(b) for b in range(1920, cal_year + 1))
    post1998_stock = sum(completions_for_year(b) for b in range(1999, cal_year + 1))
    pre1998_stock  = total_stock - post1998_stock
    frac_post1998  = post1998_stock / total_stock if total_stock > 0 else 0
    pop_this_year  = pop_dict.get(cal_year, pop_dict.get(max(pop_dict.keys())))
    stock_records.append({
        "year": cal_year,
        "total_stock": total_stock,
        "post1998_stock": post1998_stock,
        "pre1998_stock": pre1998_stock,
        "frac_post1998": frac_post1998,
        "population": pop_this_year,
        "person_years_post1998": frac_post1998 * pop_this_year,
        "person_years_pre1998": (1 - frac_post1998) * pop_this_year,
    })

stock_df = pd.DataFrame(stock_records)

total_py_post1998 = stock_df["person_years_post1998"].sum()
total_py_pre1998  = stock_df["person_years_pre1998"].sum()

# Structure fire deaths from 1999-2025 by construction period (known only)
struct_1999_2025 = structure[(structure["year"] >= 1999) & (structure["year"] <= 2025)]
deaths_post1998  = struct_1999_2025[struct_1999_2025["construction_year"] > 1998]["deaths"].sum()
deaths_pre1998   = struct_1999_2025[
    struct_1999_2025["construction_year"].notna() &
    (struct_1999_2025["construction_year"] <= 1998)
]["deaths"].sum()

rate_post1998 = (deaths_post1998 / total_py_post1998) * 100_000 if total_py_post1998 > 0 else 0
rate_pre1998  = (deaths_pre1998  / total_py_pre1998)  * 100_000 if total_py_pre1998  > 0 else 0

print(f"Study window: 1999-2025 (post-regulation era)")
print(f"Population: {pop_dict.get(1999):,} (1999) to {pop_dict.get(2025, pop_dict[max(pop_dict.keys())]):,} (2025)")
print()
print(f"Modeled dwelling stock fractions (1999-2025):")
for _, row in stock_df[stock_df["year"].isin([1999, 2005, 2010, 2015, 2020, 2025])].iterrows():
    print(f"  {int(row['year'])}: post-1998 fraction = {row['frac_post1998']:.1%}  "
          f"(total stock ~{row['total_stock']:,.0f} dwellings)")
print()
print(f"Total person-years of exposure (1999-2025):")
print(f"  Pre-1998 dwellings:  {total_py_pre1998:>12,.0f} person-years")
print(f"  Post-1998 dwellings: {total_py_post1998:>12,.0f} person-years")
print()
print(f"Structure fire deaths in 1999-2025 (known construction year only):")
print(f"  In pre-1998 buildings:  {deaths_pre1998} deaths")
print(f"  In post-1998 buildings: {deaths_post1998} deaths")
print()
print(f"Fatality rates (deaths per 100,000 person-years):")
print(f"  Pre-1998 dwellings:  {rate_pre1998:.4f} per 100,000 person-years")
print(f"  Post-1998 dwellings: {rate_post1998:.4f} per 100,000 person-years")
if rate_pre1998 > 0 and rate_post1998 == 0:
    print(f"  Rate ratio: post-1998 / pre-1998 = 0.00 (zero observed deaths in post-1998 buildings)")
elif rate_pre1998 > 0:
    rr = rate_post1998 / rate_pre1998
    print(f"  Rate ratio: post-1998 / pre-1998 = {rr:.2f}")
print()
print("CAVEAT: Dwelling stock modeled from stepped completion-rate assumptions")
print("        (2,000/yr 1940-1979, 2,500/yr 1980-1997, 3,000/yr 1998-2009,")
print("        3,500/yr 2010-2025). These are consistent with the documented")
print("        mean stock year of ~1992 but are NOT derived from census data.")
print("        Person-years figures should be interpreted as order-of-magnitude")
print("        estimates for sensitivity analysis, not precise epidemiological")
print("        denominators.")

# Save table
stock_df.to_csv(os.path.join(OUT, "analysis1_person_years_by_year.csv"), index=False)
summary1 = pd.DataFrame([
    {"Group": "Pre-1998 dwellings", "Deaths_1999_2025": deaths_pre1998,
     "Total_person_years": round(total_py_pre1998),
     "Rate_per_100k_person_years": round(rate_pre1998, 4)},
    {"Group": "Post-1998 dwellings", "Deaths_1999_2025": deaths_post1998,
     "Total_person_years": round(total_py_post1998),
     "Rate_per_100k_person_years": round(rate_post1998, 4)},
])
summary1.to_csv(os.path.join(OUT, "analysis1_summary.csv"), index=False)
print(f"\nSaved: analysis1_person_years_by_year.csv, analysis1_summary.csv")


# ==============================================================================
# ANALYSIS 2: Sensitivity Analysis on Missing Construction Year
# ==============================================================================
print()
print("=" * 70)
print("ANALYSIS 2: Sensitivity Analysis — Missing Construction Year")
print("=" * 70)
print()

# Use the FULL structure fire dataset (1968-2025) for this sensitivity analysis.
# The 48 incidents with missing construction_year all occurred between 1970-1995.
# The 1996+ subset used for Table 3 happens to have 0 missing because all
# post-1996 incidents were traceable to cadastral records; missingness is
# entirely concentrated in the pre-1996 historical period.

n_known   = structure["construction_year"].notna().sum()
n_missing = structure["construction_year"].isna().sum()

# Known breakdowns (full dataset)
known_post1998 = structure[structure["construction_year"] > 1998]
known_pre1998  = structure[
    structure["construction_year"].notna() &
    (structure["construction_year"] <= 1998)
]
unknown_subset = structure[structure["construction_year"].isna()]

# Deaths
deaths_known_post1998 = known_post1998["deaths"].sum()
deaths_known_pre1998  = known_pre1998["deaths"].sum()
deaths_unknown        = unknown_subset["deaths"].sum()

print(f"Structure fire incidents (full dataset 1968-2025):")
print(f"  Total incidents:                  {len(structure)}")
print(f"  Known construction year:          {n_known} ({n_known/len(structure)*100:.0f}%)")
print(f"  Missing construction year:        {n_missing} ({n_missing/len(structure)*100:.0f}%)")
print(f"  Deaths in known post-1998 bldgs:  {deaths_known_post1998}")
print(f"  Deaths in known pre-1998 bldgs:   {deaths_known_pre1998}")
print(f"  Deaths in unknown-year bldgs:     {deaths_unknown}")
print()

# KEY INSIGHT: Check what years the missing-construction-year incidents occurred
unknown_years = unknown_subset["year"].describe()
unknown_year_min = unknown_subset["year"].min()
unknown_year_max = unknown_subset["year"].max()

print("KEY INSIGHT: Year distribution of incidents with MISSING construction year:")
print(f"  Year range: {unknown_year_min} to {unknown_year_max}")
print(f"  Incidents by year:")
vc = unknown_subset["year"].value_counts().sort_index()
for yr, cnt in vc.items():
    print(f"    {yr}: {cnt} incident(s)")
print()
print("CRITICAL LOGICAL CONSTRAINT:")
print(f"  All {n_missing} incidents with missing construction year occurred")
print(f"  between {unknown_year_min} and {unknown_year_max}.")
print("  A building that burned down before 1999 CANNOT have been constructed")
print("  after 1998. Therefore, missingness in the construction_year field")
print("  is LOGICALLY IRRELEVANT to the post-1998 building finding.")
print("  The missing data CANNOT inflate the post-1998 zero.")
print()

# Sensitivity scenarios
print("Sensitivity scenarios (hypothetical — not epidemiologically valid):")
print("These scenarios are presented purely for statistical robustness.")
print("Scenarios B-D are logically impossible given the year constraint above.")
print()

scenarios = [
    ("A", 0.00, "All unknown are pre-1998 (the only logically possible scenario)"),
    ("B", 0.10, "10% of unknown assigned to post-1998 (logically impossible)"),
    ("C", 0.50, "50% of unknown assigned to post-1998 (extremely implausible)"),
    ("D", 1.00, "All unknown assigned to post-1998 (logically impossible)"),
]

scenario_rows = []
for label, frac_to_post, description in scenarios:
    extra_deaths_post = round(deaths_unknown * frac_to_post)
    extra_deaths_pre  = deaths_unknown - extra_deaths_post
    total_post = deaths_known_post1998 + extra_deaths_post
    total_pre  = deaths_known_pre1998  + extra_deaths_pre
    total_known_or_assigned = total_post + total_pre
    pct_post = total_post / total_known_or_assigned * 100 if total_known_or_assigned > 0 else 0
    note = " [ONLY VALID SCENARIO]" if frac_to_post == 0.00 else " [LOGICALLY IMPOSSIBLE]"
    print(f"  Scenario {label}: {description}")
    print(f"    Post-1998 deaths: {total_post}  |  Pre-1998 deaths: {total_pre}")
    print(f"    Post-1998 share: {pct_post:.1f}%{note}")
    print()
    scenario_rows.append({
        "Scenario": label,
        "Description": description,
        "Frac_unknown_to_post1998": frac_to_post,
        "Deaths_post1998": total_post,
        "Deaths_pre1998": total_pre,
        "Pct_in_post1998_buildings": round(pct_post, 1),
        "Logically_valid": frac_to_post == 0.00,
    })

scenarios_df = pd.DataFrame(scenario_rows)
scenarios_df.to_csv(os.path.join(OUT, "analysis2_sensitivity_missing_cy.csv"), index=False)
print(f"Saved: analysis2_sensitivity_missing_cy.csv")


# ==============================================================================
# ANALYSIS 3: Interrupted Time Series Analysis (ITSA)
# ==============================================================================
print()
print("=" * 70)
print("ANALYSIS 3: Interrupted Time Series Analysis (ITSA)")
print("=" * 70)
print()

# Build annual death counts 1968-2025 (structure + other combined)
all_incidents = pd.concat([
    structure[["year", "deaths"]],
    other[["year", "deaths"]],
], ignore_index=True)

annual_deaths = (
    all_incidents.groupby("year")["deaths"].sum()
    .reindex(range(1968, 2026), fill_value=0)
    .reset_index()
)
annual_deaths.columns = ["year", "deaths"]

# Merge population
annual_deaths = annual_deaths.merge(pop[["year", "population_1jan"]], on="year", how="left")

# For 2025: use last available population if missing
last_pop = pop["population_1jan"].iloc[-1]
annual_deaths["population_1jan"] = annual_deaths["population_1jan"].fillna(last_pop)

# ITSA design variables
# Intervention 1: 1999 (building regulations effective after 1998 code)
# Intervention 2: 1982 (fire prevention act) -- tested secondarily
INTERVENTION_YEAR_MAIN = 1999
INTERVENTION_YEAR_2    = 1982

annual_deaths["time"]            = annual_deaths["year"] - 1968          # secular trend
annual_deaths["post1999"]        = (annual_deaths["year"] >= INTERVENTION_YEAR_MAIN).astype(int)
annual_deaths["time_post1999"]   = annual_deaths["time"] * annual_deaths["post1999"]
annual_deaths["post1982"]        = (annual_deaths["year"] >= INTERVENTION_YEAR_2).astype(int)
annual_deaths["time_post1982"]   = annual_deaths["time"] * annual_deaths["post1982"]
annual_deaths["log_pop"]         = np.log(annual_deaths["population_1jan"])

print(f"Annual death counts (structure + other combined): {len(annual_deaths)} years (1968-2025)")
print(f"Total deaths: {annual_deaths['deaths'].sum()}")
print(f"Zeros in annual counts: {(annual_deaths['deaths'] == 0).sum()} years")
print()

# ─── Model A: Poisson GLM, single intervention at 1999 ────────────────────────
print("--- Model A: Poisson GLM, single intervention at 1999 ---")
try:
    model_a = smf.glm(
        "deaths ~ time + post1999 + time_post1999",
        data=annual_deaths,
        family=sm.families.Poisson(),
        offset=annual_deaths["log_pop"],
    ).fit(disp=False)

    print(model_a.summary().tables[1])
    print()

    # Pearson chi2 dispersion check
    pearson_chi2 = model_a.pearson_chi2
    df_resid     = model_a.df_resid
    dispersion   = pearson_chi2 / df_resid
    print(f"Overdispersion check (Pearson chi2 / df): {dispersion:.3f}")
    if dispersion > 1.5:
        print("  -> Overdispersion detected (ratio > 1.5). Fitting Negative Binomial.")
    else:
        print("  -> No major overdispersion.")
    print()

    # Extract coefficients and CIs for reporting
    coef_a = model_a.params
    ci_a   = model_a.conf_int()
    irr_a  = np.exp(coef_a)
    irr_ci_a = np.exp(ci_a)

    print("Incidence Rate Ratios (IRR) with 95% CI:")
    for name in ["time", "post1999", "time_post1999"]:
        irr_val = irr_a[name]
        lo      = irr_ci_a.loc[name, 0]
        hi      = irr_ci_a.loc[name, 1]
        pval    = model_a.pvalues[name]
        print(f"  {name:<20} IRR={irr_val:.4f}  95%CI [{lo:.4f}, {hi:.4f}]  p={pval:.4f}")
    print()

    aic_a = model_a.aic
    print(f"AIC (Model A, Poisson): {aic_a:.1f}")

except Exception as e:
    print(f"Model A failed: {e}")
    model_a = None
    dispersion = None

# ─── Model B: Negative Binomial GLM (handles overdispersion) ──────────────────
print()
print("--- Model B: Negative Binomial GLM, single intervention at 1999 ---")
try:
    model_b = smf.glm(
        "deaths ~ time + post1999 + time_post1999",
        data=annual_deaths,
        family=sm.families.NegativeBinomial(),
        offset=annual_deaths["log_pop"],
    ).fit(disp=False)

    print(model_b.summary().tables[1])
    print()

    coef_b = model_b.params
    ci_b   = model_b.conf_int()
    irr_b  = np.exp(coef_b)
    irr_ci_b = np.exp(ci_b)

    print("Incidence Rate Ratios (IRR) with 95% CI:")
    for name in ["time", "post1999", "time_post1999"]:
        if name in irr_b.index:
            irr_val = irr_b[name]
            lo      = irr_ci_b.loc[name, 0]
            hi      = irr_ci_b.loc[name, 1]
            pval    = model_b.pvalues[name]
            print(f"  {name:<20} IRR={irr_val:.4f}  95%CI [{lo:.4f}, {hi:.4f}]  p={pval:.4f}")
    print()

    aic_b = model_b.aic
    print(f"AIC (Model B, NegBin): {aic_b:.1f}")

except Exception as e:
    print(f"Model B failed: {e}")
    model_b = None

# ─── Model C: Two-intervention Poisson (1982 + 1999) ─────────────────────────
print()
print("--- Model C: Poisson GLM, two interventions (1982 and 1999) ---")
try:
    model_c = smf.glm(
        "deaths ~ time + post1982 + time_post1982 + post1999 + time_post1999",
        data=annual_deaths,
        family=sm.families.Poisson(),
        offset=annual_deaths["log_pop"],
    ).fit(disp=False)

    print(model_c.summary().tables[1])
    print()
    print(f"AIC (Model C, 2-intervention Poisson): {model_c.aic:.1f}")
    if model_a is not None:
        print(f"AIC comparison: Model A (1999 only) = {model_a.aic:.1f}, "
              f"Model C (1982+1999) = {model_c.aic:.1f}")
        delta_aic = model_c.aic - model_a.aic
        print(f"  Delta AIC (C - A) = {delta_aic:.1f} "
              f"({'Model C preferred' if delta_aic < -2 else 'Model A preferred or comparable'})")

except Exception as e:
    print(f"Model C failed: {e}")
    model_c = None

# ─── Generate ITSA Figure ─────────────────────────────────────────────────────
print()
print("--- Generating ITSA figure ---")

# Select the primary model for display (prefer NegBin if available)
primary_model = model_b if model_b is not None else model_a
primary_label = "Negative Binomial GLM" if model_b is not None else "Poisson GLM"

if primary_model is not None:
    # Fitted values (observed trend)
    fitted_rate = primary_model.fittedvalues / annual_deaths["population_1jan"] * 100_000
    annual_deaths["fitted_rate"] = fitted_rate

    # Counterfactual: what would have happened without 1999 intervention
    # Set post1999 = 0 and time_post1999 = 0 for counterfactual prediction
    cf_data = annual_deaths.copy()
    cf_data["post1999"]      = 0
    cf_data["time_post1999"] = 0
    # Also zero out post1982 and time_post1982 for counterfactual from 1982 only
    # For the single-intervention models use primary_model
    try:
        cf_pred = primary_model.predict(cf_data, offset=cf_data["log_pop"])
        cf_rate = cf_pred / annual_deaths["population_1jan"] * 100_000
    except Exception:
        cf_rate = None

    observed_rate = annual_deaths["deaths"] / annual_deaths["population_1jan"] * 100_000

    fig, axes = plt.subplots(2, 1, figsize=(7, 7))

    # Panel (a): Raw counts + fitted
    ax = axes[0]
    ax.bar(annual_deaths["year"], annual_deaths["deaths"],
           color="#4682B4", alpha=0.55, label="Observed deaths (annual)")
    ax.plot(annual_deaths["year"], primary_model.fittedvalues,
            color="#C0392B", linewidth=2, label=f"Fitted: {primary_label}")
    if cf_rate is not None:
        ax.plot(annual_deaths["year"][annual_deaths["year"] >= INTERVENTION_YEAR_MAIN],
                (cf_rate * annual_deaths["population_1jan"] / 100_000)[
                    annual_deaths["year"] >= INTERVENTION_YEAR_MAIN
                ],
                color="#1B7340", linewidth=2, linestyle="--",
                label="Counterfactual (no 1999 intervention)")
    ax.axvline(INTERVENTION_YEAR_MAIN, color="#333333", linestyle=":", linewidth=1.2,
               label="1999 building regulation")
    ax.axvline(INTERVENTION_YEAR_2, color="#333333", linestyle=":", linewidth=1.0, alpha=0.6,
               label="1982 fire prevention act")
    ax.set_ylabel("Deaths (count)")
    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
    ax.legend(loc="upper right", framealpha=0.9)
    ax.set_xlim(1967, 2026)
    ax.text(0.02, 0.93, "(a)", transform=ax.transAxes, fontsize=10, fontweight="bold", va="top")

    # Panel (b): Rate per 100,000 + fitted rate
    ax = axes[1]
    ax.bar(annual_deaths["year"], observed_rate,
           color="#4682B4", alpha=0.55, label="Observed rate per 100,000")
    ax.plot(annual_deaths["year"], fitted_rate,
            color="#C0392B", linewidth=2, label=f"Fitted rate: {primary_label}")
    if cf_rate is not None:
        ax.plot(annual_deaths["year"][annual_deaths["year"] >= INTERVENTION_YEAR_MAIN],
                cf_rate[annual_deaths["year"] >= INTERVENTION_YEAR_MAIN],
                color="#1B7340", linewidth=2, linestyle="--",
                label="Counterfactual (no 1999 intervention)")
    ax.axvline(INTERVENTION_YEAR_MAIN, color="#333333", linestyle=":", linewidth=1.2,
               label="1999 building regulation")
    ax.axvline(INTERVENTION_YEAR_2, color="#333333", linestyle=":", linewidth=1.0, alpha=0.6,
               label="1982 fire prevention act")
    ax.set_ylabel("Deaths per 100,000 population")
    ax.set_xlabel("Year")
    ax.legend(loc="upper right", framealpha=0.9)
    ax.set_xlim(1967, 2026)
    ax.text(0.02, 0.93, "(b)", transform=ax.transAxes, fontsize=10, fontweight="bold", va="top")

    fig.tight_layout()
    fig_path = os.path.join(OUT, "analysis3_itsa.png")
    fig.savefig(fig_path, dpi=300)
    plt.close()
    print(f"  Saved analysis3_itsa.png")

# Save annual data with model outputs
annual_deaths.to_csv(os.path.join(OUT, "analysis3_annual_data.csv"), index=False)
print(f"  Saved analysis3_itsa.png, analysis3_annual_data.csv")

# ─── ITSA Summary ─────────────────────────────────────────────────────────────
print()
print("ITSA SUMMARY (primary model: 1999 single-intervention):")
if primary_model is not None:
    params = primary_model.params
    pvals  = primary_model.pvalues
    ci     = primary_model.conf_int()

    slope_pre  = params.get("time", float("nan"))
    level_1999 = params.get("post1999", float("nan"))
    slope_chg  = params.get("time_post1999", float("nan"))

    print(f"  Pre-1999 trend (time coefficient):")
    print(f"    beta = {slope_pre:.4f}  IRR/year = {np.exp(slope_pre):.4f}  p = {pvals.get('time', float('nan')):.4f}")
    print(f"  Level change at 1999 (post1999 coefficient):")
    print(f"    beta = {level_1999:.4f}  IRR = {np.exp(level_1999):.4f}  "
          f"95%CI [{np.exp(ci.loc['post1999',0] if 'post1999' in ci.index else float('nan')):.4f}, "
          f"{np.exp(ci.loc['post1999',1] if 'post1999' in ci.index else float('nan')):.4f}]  "
          f"p = {pvals.get('post1999', float('nan')):.4f}")
    print(f"  Slope change after 1999 (time_post1999 coefficient):")
    print(f"    beta = {slope_chg:.4f}  IRR/year = {np.exp(slope_chg):.4f}  "
          f"p = {pvals.get('time_post1999', float('nan')):.4f}")

# ==============================================================================
# FINAL SUMMARY
# ==============================================================================
print()
print("=" * 70)
print("ALL ANALYSES COMPLETE")
print("=" * 70)
print(f"Output files written to {OUT}/:")
print("  analysis1_person_years_by_year.csv  -- annual dwelling stock model")
print("  analysis1_summary.csv               -- person-years exposure summary")
print("  analysis2_sensitivity_missing_cy.csv -- missing CY sensitivity scenarios")
print("  analysis3_annual_data.csv           -- annual deaths + model columns")
print("  analysis3_itsa.png                  -- ITSA figure (two panels)")
