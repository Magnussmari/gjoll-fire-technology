# Interrupted Time Series Regression: A Tutorial

**Full citation:** Bernal, J.L., Cummins, S., Gasparrini, A. (2017). Interrupted time series regression for the evaluation of public health interventions: a tutorial. *International Journal of Epidemiology*, 46(1), 348-355.

**DOI:** [10.1093/ije/dyw098](https://doi.org/10.1093/ije/dyw098)

**Type:** Journal article (methodological tutorial)

**Bib key:** Bernal2017

## Abstract

Tutorial paper on interrupted time series (ITS) regression, a quasi-experimental design for evaluating public health interventions using population-level data. Provides a step-by-step guide to conducting ITS analysis, addressing key methodological issues such as seasonality, autocorrelation, and overdispersion. Includes a worked example using the Italian smoking ban and acute coronary event (ACE) hospital admissions.

## Key Findings

- ITS is appropriate when a well-defined intervention occurs at a known time point, with sufficient pre- and post-intervention data.
- Step-by-step framework: (1) determine if ITS is appropriate, (2) propose an impact model, (3) perform descriptive analysis, (4) fit regression model, (5) address methodological issues.
- Standard segmented regression model: Y_t = beta_0 + beta_1*T + beta_2*X_t + beta_3*T*X_t + epsilon_t, where T = time, X_t = intervention indicator.
- Key methodological issues: seasonality (Fourier terms or indicator variables), autocorrelation (Durbin-Watson test, Newey-West standard errors), overdispersion (negative binomial as alternative to Poisson), non-linear trends, and lagged effects.
- Worked example: Italian smoking ban associated with reduction in ACE admissions.

## Key Data Points

- Segmented regression formula: Y_t = beta_0 + beta_1*T + beta_2*X_t + beta_3*T*X_t
- beta_2 = level change at intervention; beta_3 = slope change post-intervention
- Recommends visual inspection of data before model fitting
- Addresses overdispersion via negative binomial distribution

## Usage in Manuscript

- **Where cited:** Methods, Analysis section (line 89)
- **What it supports:** Cited alongside Wagner2002 as the methodological basis for the interrupted time series analysis (ITSA) using segmented Poisson regression with log-link and population offset. The manuscript follows the Bernal2017 framework for specifying level-change and slope-change terms at the 1999 regulatory intervention.
- **Accuracy check:** Correct. Appropriately cited as a methodological reference for the ITSA approach.
