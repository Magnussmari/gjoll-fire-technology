#!/usr/bin/env python3
"""
Revision analyses addressing the Fire Technology peer review (Fable 5, 2026-07-02).

Fixes:
  M4  Negative binomial refit with dispersion (alpha) estimated by ML, plus a
      quasi-Poisson robustness check (SEs scaled by sqrt of Pearson dispersion),
      plus residual-autocorrelation diagnostics (Durbin-Watson, Ljung-Box).
  M5  ITSA re-run on STRUCTURE-fire deaths and on STRUCTURE-fire INCIDENTS
      (the intervention is a dwelling regulation, so the all-fire series is the
      wrong outcome for attributing the level change).
  M6  Zero-event Poisson probability recomputed on INCIDENTS (not deaths), which
      respects within-incident clustering.
  M2  Worst-case reclassification sensitivity: count BOTH borderline post-1998
      cases (2014 nursing-home CY 2001; Studlar/Fossaleyni CY 1996) as post-1998
      structure-fire deaths and recompute the fatality rate + one-sided bound.

Run from the fire_technology/ directory:
    python scripts/revision_analyses.py

Output -> output/generated/revision_*.csv and console.

Author: Magnús Smári Smárason | smarason.is
Data:   DOI 10.34881/I5WGJU  | https://www.gjoll.is
"""

import os
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.discrete.discrete_model import NegativeBinomial
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import acorr_ljungbox
from scipy import stats

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")
OUT  = os.path.join(BASE, "output", "generated")
os.makedirs(OUT, exist_ok=True)

structure = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_structure.csv"))
other     = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_other.csv"))
pop       = pd.read_csv(os.path.join(DATA, "population_1jan_MAN00000_1968_2025.csv"))

# Person-years denominators from Analysis 1 (modeled dwelling stock)
PY_POST1998 = 2_080_213
PY_PRE1998  = 6_636_536
DEATHS_PRE1998 = 38          # structure-fire deaths 1999-2025, recorded CY <= 1998

def hr(title):
    print("\n" + "=" * 72 + f"\n{title}\n" + "=" * 72)


# ==========================================================================
# Build the annual series (shared)
# ==========================================================================
pop_year = pop.set_index("year")["population_1jan"]
last_pop = pop_year.iloc[-1]

def annual_counts(df, value="deaths"):
    """Annual sum of `value` (deaths) or incident counts, reindexed 1968-2025."""
    if value == "incidents":
        s = df.groupby("year").size()
    else:
        s = df.groupby("year")[value].sum()
    s = s.reindex(range(1968, 2026), fill_value=0)
    out = pd.DataFrame({"year": s.index, "y": s.values})
    out["population_1jan"] = out["year"].map(pop_year).fillna(last_pop)
    out["time"]          = out["year"] - 1968
    out["post1999"]      = (out["year"] >= 1999).astype(int)
    # CORRECT segmented (Wagner 2002) coding: the post-intervention trend term is
    # "years since the intervention" (0 before 1999), NOT time*post1999. This makes
    # the post1999 coefficient the level change AT the 1999 breakpoint. Using
    # time*post1999 (time measured from 1968) would instead make it the vertical
    # gap at 1968 -- an arbitrary-origin artifact, not the intervention level change.
    out["time_since_1999"] = (out["year"] - 1999).clip(lower=0)
    out["log_pop"]       = np.log(out["population_1jan"])
    return out

all_incidents = pd.concat([structure[["year", "deaths"]],
                           other[["year", "deaths"]]], ignore_index=True)

series = {
    "all_deaths":        annual_counts(all_incidents, "deaths"),
    "structure_deaths":  annual_counts(structure, "deaths"),
    "structure_incidents": annual_counts(structure, "incidents"),
}


# ==========================================================================
# M4 — corrected distributional robustness on the ALL-DEATHS series
# ==========================================================================
hr("M4 — Poisson vs ML-estimated Negative Binomial vs quasi-Poisson")

df = series["all_deaths"]
formula = "y ~ time + post1999 + time_since_1999"

# --- Poisson GLM (baseline) ---
pois = smf.glm(formula, data=df, family=sm.families.Poisson(),
               offset=df["log_pop"]).fit()
pearson_disp = pois.pearson_chi2 / pois.df_resid
print(f"Poisson AIC = {pois.aic:.1f} | Pearson dispersion = {pearson_disp:.3f}")

# --- Negative Binomial with alpha estimated by ML (discrete model) ---
# discrete.NegativeBinomial estimates the dispersion parameter alpha jointly.
X = sm.add_constant(df[["time", "post1999", "time_since_1999"]].astype(float))
nb = NegativeBinomial(df["y"].astype(float), X, offset=df["log_pop"].values,
                      loglike_method="nb2").fit(disp=False, maxiter=200)
alpha_hat = nb.params["alpha"]
# CI for alpha
alpha_ci = nb.conf_int().loc["alpha"]
print(f"NB(ML) AIC = {nb.aic:.1f} | alpha_hat = {alpha_hat:.4f} "
      f"95%CI [{alpha_ci[0]:.4f}, {alpha_ci[1]:.4f}]")
print(f"  -> AIC gap vs Poisson = {nb.aic - pois.aic:+.1f} "
      f"(nested model: must be >= -~2; the old fixed-alpha=1 NB gave +24.6)")

# NB level-change IRR
b_post = nb.params["post1999"]
ci_post = nb.conf_int().loc["post1999"]
print(f"  NB level change post1999: IRR = {np.exp(b_post):.4f} "
      f"95%CI [{np.exp(ci_post[0]):.4f}, {np.exp(ci_post[1]):.4f}] p = {nb.pvalues['post1999']:.4f}")

# --- Quasi-Poisson: scale SEs by sqrt(pearson_disp) ---
scale = np.sqrt(pearson_disp)
print(f"\nQuasi-Poisson (SEs x sqrt({pearson_disp:.3f}) = x{scale:.3f}):")
qp_rows = []
for name in ["time", "post1999", "time_since_1999"]:
    b  = pois.params[name]
    se = pois.bse[name] * scale
    lo, hi = b - 1.96 * se, b + 1.96 * se
    z = b / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    print(f"  {name:<16} IRR = {np.exp(b):.4f}  95%CI [{np.exp(lo):.4f}, {np.exp(hi):.4f}]  p = {p:.4f}")
    qp_rows.append({"term": name, "IRR": np.exp(b), "lo": np.exp(lo), "hi": np.exp(hi), "p": p})

# --- Residual autocorrelation diagnostics on Poisson Pearson residuals ---
resid = pois.resid_pearson
dw = durbin_watson(resid)
lb = acorr_ljungbox(resid, lags=[1, 3], return_df=True)
print(f"\nResidual autocorrelation (Poisson Pearson residuals):")
print(f"  Durbin-Watson = {dw:.3f} (≈2 => no first-order autocorrelation)")
print(f"  Ljung-Box lag1 p = {lb['lb_pvalue'].iloc[0]:.3f} | lag3 p = {lb['lb_pvalue'].iloc[1]:.3f}")

pd.DataFrame(qp_rows).to_csv(os.path.join(OUT, "revision_M4_quasipoisson.csv"), index=False)
pd.DataFrame([{
    "model": "Poisson", "AIC": round(pois.aic, 1), "alpha": np.nan,
    "post1999_IRR": round(np.exp(pois.params["post1999"]), 4),
    "post1999_p": round(pois.pvalues["post1999"], 4),
}, {
    "model": "NegBin(ML alpha)", "AIC": round(nb.aic, 1), "alpha": round(alpha_hat, 4),
    "post1999_IRR": round(np.exp(b_post), 4), "post1999_p": round(nb.pvalues["post1999"], 4),
}]).to_csv(os.path.join(OUT, "revision_M4_model_comparison.csv"), index=False)


# ==========================================================================
# M5 — ITSA on structure-only deaths and structure-only incidents
# ==========================================================================
hr("M5 — ITSA on STRUCTURE-only series (deaths and incidents)")

def fit_itsa(dframe, label):
    m = smf.glm(formula, data=dframe, family=sm.families.Poisson(),
                offset=dframe["log_pop"]).fit()
    disp = m.pearson_chi2 / m.df_resid
    print(f"\n[{label}]  (Poisson, dispersion={disp:.3f}, AIC={m.aic:.1f})")
    for name in ["time", "post1999", "time_since_1999"]:
        b = m.params[name]; ci = m.conf_int().loc[name]
        print(f"  {name:<16} IRR = {np.exp(b):.4f}  95%CI [{np.exp(ci[0]):.4f}, {np.exp(ci[1]):.4f}]  p = {m.pvalues[name]:.4f}")
    return m, disp

m_sd, _ = fit_itsa(series["structure_deaths"],   "Structure-fire DEATHS")
m_si, _ = fit_itsa(series["structure_incidents"], "Structure-fire INCIDENTS")

rows = []
for label, m in [("structure_deaths", m_sd), ("structure_incidents", m_si)]:
    for name in ["time", "post1999", "time_since_1999"]:
        b = m.params[name]; ci = m.conf_int().loc[name]
        rows.append({"series": label, "term": name, "IRR": round(np.exp(b), 4),
                     "lo": round(np.exp(ci[0]), 4), "hi": round(np.exp(ci[1]), 4),
                     "p": round(m.pvalues[name], 4)})
pd.DataFrame(rows).to_csv(os.path.join(OUT, "revision_M5_structure_itsa.csv"), index=False)
print("\nNote: the pre-1999 secular decline (time IRR) is the robust, replicable")
print("signal across ALL outcome definitions; the 1999 LEVEL change is not")
print("interpreted as an effect of the 1998 regulation (stock share ~0 in 1999).")


# ==========================================================================
# M6 — zero-event probability computed on INCIDENTS (respects clustering)
# ==========================================================================
hr("M6 — Zero-event Poisson probability on INCIDENTS, not deaths")

# Structure-fire INCIDENTS 1999-2025 in buildings with recorded CY <= 1998
s = structure.copy()
s99 = s[(s["year"] >= 1999) & (s["year"] <= 2025)]
inc_pre1998 = s99[s99["construction_year"].notna() & (s99["construction_year"] <= 1998)].shape[0]
deaths_pre1998_chk = int(s99[s99["construction_year"].notna() & (s99["construction_year"] <= 1998)]["deaths"].sum())

inc_rate_pre1998 = inc_pre1998 / PY_PRE1998            # incidents per person-year
expected_inc_post1998 = inc_rate_pre1998 * PY_POST1998 # expected incidents in post-1998 stock
p0_incidents = np.exp(-expected_inc_post1998)

# for comparison, the death-level expected count
expected_deaths_post1998 = (DEATHS_PRE1998 / PY_PRE1998) * PY_POST1998
p0_deaths = np.exp(-expected_deaths_post1998)

mean_deaths_per_incident = deaths_pre1998_chk / inc_pre1998
print(f"Structure-fire INCIDENTS 1999-2025, recorded CY<=1998: {inc_pre1998}")
print(f"  (deaths in those incidents: {deaths_pre1998_chk}; "
      f"mean {mean_deaths_per_incident:.2f} deaths/incident)")
print(f"Pre-1998 incident rate: {inc_rate_pre1998*100_000:.4f} per 100,000 PY")
print(f"Expected post-1998 INCIDENTS under rate equality: {expected_inc_post1998:.2f}")
print(f"  P(0 incidents) = e^-{expected_inc_post1998:.2f} = {p0_incidents:.2e}")
print(f"Compare death-level: expected deaths {expected_deaths_post1998:.2f}, "
      f"P(0) = {p0_deaths:.2e}")
print("Conclusion unchanged: the observed zero is highly informative even after")
print("collapsing to incidents (clustering: mean 1.25 deaths/structure incident).")

pd.DataFrame([{
    "unit": "incidents", "pre1998_count": inc_pre1998,
    "pre1998_rate_per100k": round(inc_rate_pre1998*100_000, 4),
    "expected_post1998": round(expected_inc_post1998, 2),
    "P_zero": p0_incidents,
}, {
    "unit": "deaths", "pre1998_count": DEATHS_PRE1998,
    "pre1998_rate_per100k": round(DEATHS_PRE1998/PY_PRE1998*100_000, 4),
    "expected_post1998": round(expected_deaths_post1998, 2),
    "P_zero": p0_deaths,
}]).to_csv(os.path.join(OUT, "revision_M6_zero_event_incidents.csv"), index=False)


# ==========================================================================
# M2 — worst-case reclassification sensitivity
# ==========================================================================
hr("M2 — Worst-case: both borderline cases counted as post-1998 structure deaths")

# One-sided 95% exact-Poisson upper bound: lambda_U = 0.5 * chi2_{0.95, 2(k+1)}.
# For k=0 this is 0.5*chi2.ppf(0.95,2) = 2.996 ~ the rule-of-3, matching the
# convention used for the zero-event bound elsewhere in the paper. (Using the
# 0.975 quantile would be a *two-sided* 95% bound and is inconsistent with it.)
def rate_and_bound(deaths, py):
    rate = deaths / py * 100_000
    ub   = 3.0 / py * 100_000 if deaths == 0 else stats.chi2.ppf(0.95, 2*(deaths+1))/2 / py * 100_000
    return rate, ub

scenarios = [
    ("Primary (recorded CY>=1999)", 0),
    ("Worst-case (+nursing-home 2014, +Studlar/Fossaleyni)", 2),
]
rows = []
for label, d in scenarios:
    rate, ub = rate_and_bound(d, PY_POST1998)
    ratio_to_pre = rate / (DEATHS_PRE1998/PY_PRE1998*100_000) if rate > 0 else 0.0
    fold_below = (DEATHS_PRE1998/PY_PRE1998*100_000) / rate if rate > 0 else float("inf")
    print(f"{label}:")
    print(f"  deaths={d}  rate={rate:.4f}/100k  one-sided 95% upper bound={ub:.4f}/100k")
    if rate > 0:
        print(f"  = {fold_below:.1f}x BELOW the pre-1998 rate (0.5726); upper bound still < 0.5726")
    else:
        print(f"  upper bound 0.144/100k still < 0.5726 pre-1998 rate")
    rows.append({"scenario": label, "deaths": d, "rate_per100k": round(rate, 4),
                 "upper_bound_per100k": round(ub, 4), "fold_below_pre1998": round(fold_below, 1) if rate>0 else None})
    print()
pd.DataFrame(rows).to_csv(os.path.join(OUT, "revision_M2_worstcase.csv"), index=False)

hr("DONE — revision_*.csv written to output/generated/")
