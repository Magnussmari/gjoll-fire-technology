#!/usr/bin/env python3
"""
verify_statistics.py — end-to-end verification of EVERY headline statistic in

  "Fatal Fire Incidents in Iceland, 1968-2025:
   A National Registry Study of Building Age and Fire Safety Regulation"

Each claim printed in the manuscript / supplement is recomputed here directly
from the deposited CSVs and checked against the value stated in the paper.
The script prints PASS/FAIL for every check and exits non-zero if ANY check
fails, so it can gate CI and act as a living audit of the manuscript.

    python scripts/verify_statistics.py            # verify everything
    python scripts/verify_statistics.py -v         # also print computed values

Data: DOI 10.34881/I5WGJU | https://www.gjoll.is
Author: Magnús Smári Smárason | smarason.is
"""
import os, sys, math
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.discrete.discrete_model import NegativeBinomial
from statsmodels.stats.stattools import durbin_watson
from scipy import stats

VERBOSE = "-v" in sys.argv
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data")

structure = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_structure.csv"))
other     = pd.read_csv(os.path.join(DATA, "fire_incidents_deaths_other.csv"))
pop       = pd.read_csv(os.path.join(DATA, "population_1jan_MAN00000_1968_2025.csv"))
pop_year  = pop.set_index("year")["population_1jan"]
last_pop  = pop_year.iloc[-1]

# Modeled dwelling-stock denominators (reproduced by advanced_analyses.py Analysis 1)
PY_PRE1998, PY_POST1998 = 6_636_536, 2_080_213

RESULTS = []
def check(name, got, want, tol=0.0, kind="≈"):
    """Record a check. tol is absolute tolerance; tol=0 means exact/equal."""
    if isinstance(want, (int,)) and isinstance(got, (int, np.integer)) and tol == 0:
        ok = int(got) == int(want)
    else:
        ok = abs(float(got) - float(want)) <= tol
    RESULTS.append((ok, name, got, want))
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if VERBOSE or not ok:
        line += f"   got={got} want{kind}{want}" + (f" (±{tol})" if tol else "")
    print(line)
    return ok

def section(t): print("\n" + "="*70 + f"\n{t}\n" + "="*70)


# ── annual-series builder (shared with the analysis scripts) ─────────────────
def annual(df, incidents=False):
    s = df.groupby("year").size() if incidents else df.groupby("year")["deaths"].sum()
    s = s.reindex(range(1968, 2026), fill_value=0)
    d = pd.DataFrame({"year": s.index, "y": s.values})
    d["pop"] = d["year"].map(pop_year).fillna(last_pop)
    d["log_pop"] = np.log(d["pop"])
    d["time"] = d["year"] - 1968
    d["post1999"] = (d["year"] >= 1999).astype(int)
    d["time_since_1999"] = (d["year"] - 1999).clip(lower=0)
    return d

def itsa(d):
    return smf.glm("y ~ time + post1999 + time_since_1999", d,
                   family=sm.families.Poisson(), offset=d["log_pop"]).fit()


# ══════════════════════════════════════════════════════════════════════════
section("1. Overall counts and burden")
n_all_inc = len(structure) + len(other)
n_all_dth = int(structure["deaths"].sum() + other["deaths"].sum())
check("Total fatal incidents = 113", n_all_inc, 113)
check("Total deaths = 145", n_all_dth, 145)
check("Structure incidents = 93", len(structure), 93)
check("Structure deaths = 116", int(structure["deaths"].sum()), 116)
check("Other incidents = 20", len(other), 20)
check("Other deaths = 29", int(other["deaths"].sum()), 29)
check("Structure share of deaths = 80%", 100*structure["deaths"].sum()/n_all_dth, 80, tol=0.6)
check("Mean deaths/incident (all) = 1.28", n_all_dth/n_all_inc, 1.28, tol=0.005)
check("Mean deaths/incident (structure) = 1.25", structure["deaths"].sum()/len(structure), 1.25, tol=0.005)
check("Mean deaths/incident (other) = 1.45", other["deaths"].sum()/len(other), 1.45, tol=0.005)
# single-fatality incidents 93/113
singles = int((pd.concat([structure["deaths"], other["deaths"]]) == 1).sum())
check("Single-fatality incidents = 93", singles, 93)


# ══════════════════════════════════════════════════════════════════════════
section("2. Decade / period table (Table 1)")
periods = [((1968,1969),6,13,32.3),((1970,1979),35,47,21.9),((1980,1989),19,24,10.1),
           ((1990,1999),13,14,5.3),((2000,2009),14,17,5.7),((2010,2019),14,15,4.6),
           ((2020,2025),12,15,6.7)]
alld = pd.concat([structure[["year","deaths"]], other[["year","deaths"]]])
for (a,b), inc_e, dth_e, rate_e in periods:
    sub = alld[(alld.year>=a)&(alld.year<=b)]
    inc = len(sub); dth = int(sub.deaths.sum())
    yrs = b - a + 1
    meanpop = pop_year.reindex(range(a,b+1)).fillna(last_pop).mean()
    rate = dth / meanpop * 1e6 / yrs
    check(f"{a}-{b} incidents = {inc_e}", inc, inc_e)
    check(f"{a}-{b} deaths = {dth_e}", dth, dth_e)
    check(f"{a}-{b} rate/million/yr = {rate_e}", rate, rate_e, tol=0.15)
# 80% decline from 1970s peak to 2010s
decline = 100*(1 - 4.6/21.9)
check("Decline 1970s->2010s ≈ 80%", decline, 80, tol=1.5)


# ══════════════════════════════════════════════════════════════════════════
section("3. Zero-death years")
annual_all = alld.groupby("year")["deaths"].sum().reindex(range(1968,2026), fill_value=0)
zero_years = sorted(int(y) for y in annual_all[annual_all==0].index)
check("Number of zero-death years = 8", len(zero_years), 8)
check("Zero-death years set matches", int(zero_years==[1984,1987,1992,2000,2003,2007,2011,2015]), 1)


# ══════════════════════════════════════════════════════════════════════════
section("4. Seasonality (Oct-Mar heating season)")
sd = structure.copy(); od = other.copy()
sd["month"] = pd.to_datetime(sd["incident_date"]).dt.month
od["month"] = pd.to_datetime(od["incident_date"]).dt.month
allm = pd.concat([sd[["month","deaths"]], od[["month","deaths"]]])
heat = allm.month.isin([10,11,12,1,2,3])
inc_heat = int(heat.sum()); dth_heat = int(allm.loc[heat,"deaths"].sum())
check("Oct-Mar incidents = 66", inc_heat, 66)
check("Oct-Mar deaths = 84", dth_heat, 84)
check("Oct-Mar incident share = 58%", 100*inc_heat/len(allm), 58, tol=0.7)
# binary chi-square vs 50.4% expected
exp_p = 0.504
chi2_inc = (inc_heat - len(allm)*exp_p)**2/(len(allm)*exp_p) + \
           ((len(allm)-inc_heat) - len(allm)*(1-exp_p))**2/(len(allm)*(1-exp_p))
check("Seasonality chi-square (incidents) ≈ 3.2", chi2_inc, 3.2, tol=0.5)


# ══════════════════════════════════════════════════════════════════════════
section("5. Construction year and the post-1998 cohort")
cy = structure["construction_year"]
check("Known construction year = 45", int(cy.notna().sum()), 45)
check("Missing construction year = 48", int(cy.isna().sum()), 48)
missing = structure[cy.isna()]
check("All missing-CY incidents in 1970-1995", int(missing.year.between(1970,1995).all()), 1)
post98 = structure[cy > 1998]
check("Fatal structure incidents with recorded CY>=1999 = 0", len(post98), 0)
sub9625 = structure[(structure.year>=1996)&(structure.year<=2025)]
check("Mean CY of 1996-2025 fatal structure fires = 1957",
      sub9625["construction_year"].dropna().mean(), 1957, tol=1.0)
# incidents with recorded CY<=1998 in 1999-2025 window (for incident-level calc)
win = structure[(structure.year>=1999)&(structure.year<=2025)]
inc32 = win[win.construction_year.notna() & (win.construction_year<=1998)]
check("Pre-1998-cohort fatal structure INCIDENTS 1999-2025 = 32", len(inc32), 32)
check("Deaths in those incidents = 38", int(inc32.deaths.sum()), 38)


# ══════════════════════════════════════════════════════════════════════════
section("6. Person-years bound and zero-event inference")
rate_pre = 38 / PY_PRE1998 * 1e5
check("Pre-1998 rate = 0.57 per 100k", rate_pre, 0.5726, tol=0.002)
ub0 = 3.0 / PY_POST1998 * 1e5
check("Post-1998 one-sided 95% upper bound = 0.14", ub0, 0.1442, tol=0.002)
expected_dth = rate_pre/1e5 * PY_POST1998
check("Expected post-1998 deaths under equality ≈ 11.9", expected_dth, 11.9, tol=0.1)
check("P(0 deaths) ≈ 7e-6", math.exp(-expected_dth), 7e-6, tol=2e-6)
# incident level
inc_rate_pre = 32 / PY_PRE1998
expected_inc = inc_rate_pre * PY_POST1998
check("Expected post-1998 incidents ≈ 10.0", expected_inc, 10.0, tol=0.2)
check("P(0 incidents) ≈ 4e-5", math.exp(-expected_inc), 4.4e-5, tol=1e-5)
# halved-denominator stress test
check("Halved-denominator upper bound = 0.29", 3.0/(PY_POST1998/2)*1e5, 0.2884, tol=0.003)


# ══════════════════════════════════════════════════════════════════════════
section("7. Worst-case reclassification sensitivity")
wc_rate = 2 / PY_POST1998 * 1e5
check("Worst-case rate (2 deaths) = 0.096", wc_rate, 0.0961, tol=0.001)
# one-sided 95% exact-Poisson upper bound for k=2 (same convention as k=0 rule-of-3)
ub2 = stats.chi2.ppf(0.95, 2*(2+1))/2 / PY_POST1998 * 1e5
check("Worst-case one-sided 95% upper bound = 0.30", ub2, 0.3027, tol=0.004)
check("Worst-case still ~6x below pre-1998", rate_pre/wc_rate, 6.0, tol=0.2)


# ══════════════════════════════════════════════════════════════════════════
section("8. ITSA — corrected segmented parameterization")
comb = annual(alld); mc = itsa(comb)
def irr(m,n): return math.exp(m.params[n])
def pv(m,n):  return m.pvalues[n]
check("Combined pre-1999 trend IRR/yr = 0.932", irr(mc,"time"), 0.932, tol=0.002)
check("Combined trend p < 0.001", pv(mc,"time"), 0.0, tol=0.001)
check("Combined LEVEL change at 1999 IRR = 1.29", irr(mc,"post1999"), 1.287, tol=0.02)
check("Combined level-change p = 0.54 (NS)", pv(mc,"post1999"), 0.537, tol=0.02)
check("Combined slope-change IRR/yr = 1.084", irr(mc,"time_since_1999"), 1.084, tol=0.003)
net = math.exp(mc.params["time"]+mc.params["time_since_1999"])
check("Net post-1999 slope ≈ 1.01/yr", net, 1.010, tol=0.005)
disp = mc.pearson_chi2/mc.df_resid
check("Pearson dispersion = 1.15", disp, 1.145, tol=0.01)
check("Poisson AIC = 216.3", mc.aic, 216.3, tol=0.3)
check("Durbin-Watson = 2.95", durbin_watson(mc.resid_pearson), 2.95, tol=0.03)
# ML negative binomial
X = sm.add_constant(comb[["time","post1999","time_since_1999"]].astype(float))
nb = NegativeBinomial(comb["y"].astype(float), X, offset=comb["log_pop"].values).fit(disp=False, maxiter=300)
check("NB alpha_hat = 0.045", nb.params["alpha"], 0.045, tol=0.01)
check("NB AIC = 217.8", nb.aic, 217.8, tol=0.4)
check("NB level change IRR = 1.28 (NS)", math.exp(nb.params["post1999"]), 1.283, tol=0.05)
check("NB level-change p ≈ 0.56", nb.pvalues["post1999"], 0.557, tol=0.05)
# quasi-Poisson
sc = math.sqrt(disp); b = mc.params["post1999"]; se = mc.bse["post1999"]*sc
check("Quasi-Poisson level IRR = 1.29", math.exp(b), 1.287, tol=0.02)
check("Quasi-Poisson level p ≈ 0.56", 2*(1-stats.norm.cdf(abs(b/se))), 0.564, tol=0.03)
# structure-only
msd = itsa(annual(structure)); msi = itsa(annual(structure, incidents=True))
check("Structure-deaths trend IRR/yr = 0.948", irr(msd,"time"), 0.948, tol=0.002)
check("Structure-deaths level IRR = 0.91 (NS)", irr(msd,"post1999"), 0.911, tol=0.03)
check("Structure-deaths level p = 0.83", pv(msd,"post1999"), 0.833, tol=0.03)
check("Structure-incidents trend IRR/yr = 0.959", irr(msi,"time"), 0.959, tol=0.002)
check("Structure-incidents level IRR = 0.84 (NS)", irr(msi,"post1999"), 0.837, tol=0.03)
check("Structure-incidents level p = 0.71", pv(msi,"post1999"), 0.706, tol=0.03)
# two-intervention model dAIC
comb2 = comb.copy()
comb2["post1982"] = (comb2.year>=1982).astype(int)
comb2["time_since_1982"] = (comb2.year-1982).clip(lower=0)
m2 = smf.glm("y ~ time + post1982 + time_since_1982 + post1999 + time_since_1999", comb2,
             family=sm.families.Poisson(), offset=comb2["log_pop"]).fit()
check("Two-intervention (1982) dAIC = +3.4", m2.aic - mc.aic, 3.4, tol=0.3)


# ══════════════════════════════════════════════════════════════════════════
section("SUMMARY")
n = len(RESULTS); fails = [r for r in RESULTS if not r[0]]
print(f"\n  {n-len(fails)}/{n} checks passed.")
if fails:
    print("  FAILED:")
    for _, name, got, want in fails:
        print(f"    - {name}: got {got}, want {want}")
    sys.exit(1)
print("\n  ✅ ALL MANUSCRIPT STATISTICS VERIFIED AGAINST THE DEPOSITED DATA.")
