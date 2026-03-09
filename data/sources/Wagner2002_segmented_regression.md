# Segmented Regression Analysis of Interrupted Time Series

**Full citation:** Wagner, A.K., Soumerai, S.B., Zhang, F., Ross-Degnan, D. (2002). Segmented regression analysis of interrupted time series studies in medication use research. *Journal of Clinical Pharmacy and Therapeutics*, 27(4), 299-309.

**DOI:** [10.1046/j.1365-2710.2002.00430.x](https://doi.org/10.1046/j.1365-2710.2002.00430.x)

**Type:** Journal article (methodological)

**Bib key:** Wagner2002

## Abstract

Foundational methodological paper on segmented regression analysis for interrupted time series (ITS) studies. Provides a practical introduction to the design, analysis, and interpretation of ITS studies, originally framed in the context of medication use research but widely applicable to public health intervention evaluation. Addresses specification of level and trend changes, multiple intervention points, and key analytical concerns.

## Key Findings

- Defines the core ITS parameters: level change (immediate shift after intervention) and trend change (change in slope after intervention).
- Segmented regression allows testing for both immediate and gradual effects of interventions.
- Multiple change points can be modeled when multiple interventions occur at different times.
- Recommends a minimum of 12 data points before and after each intervention for adequate statistical power.
- Addresses autocorrelation (Durbin-Watson statistic, autoregressive error models), seasonality (seasonal indicators or harmonic terms), and lagged effects.
- Emphasizes the importance of the counterfactual: what would have happened without the intervention.

## Key Data Points

- Minimum 12 data points recommended before and after intervention
- Segmented regression model: Y_t = beta_0 + beta_1*time + beta_2*intervention + beta_3*time_after_intervention
- Level change = beta_2; trend change = beta_3
- Autocorrelation diagnostics: Durbin-Watson test

## Usage in Manuscript

- **Where cited:** Methods, Analysis section (line 89)
- **What it supports:** Cited alongside Bernal2017 as the foundational methodological reference for the segmented regression approach used in the ITSA. The manuscript's model specification (level change, slope change, population offset) follows the Wagner2002 framework.
- **Accuracy check:** Correct. Standard methodological citation for ITS segmented regression.
