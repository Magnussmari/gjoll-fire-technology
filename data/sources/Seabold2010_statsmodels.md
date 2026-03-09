# Statsmodels: Econometric and Statistical Modeling with Python

**Full citation:** Seabold, S., Perktold, J. (2010). Statsmodels: Econometric and Statistical Modeling with Python. *Proceedings of the 9th Python in Science Conference*, 92-96.

**DOI:** [10.25080/Majora-92bf1922-011](https://doi.org/10.25080/Majora-92bf1922-011)

**Type:** Conference paper (software)

**Bib key:** Seabold2010

## Abstract

Introduces the statsmodels Python library for econometric and statistical modeling. The library provides classes and functions for estimating statistical models, conducting statistical tests, and performing data exploration. Built on NumPy, SciPy, and pandas, statsmodels follows a test-driven development (TDD) process and aims to complement SciPy's statistical functionality with a more comprehensive modeling framework.

## Key Findings

- Provides OLS (ordinary least squares), GLS (generalized least squares), WLS (weighted least squares) regression models.
- Includes GLM (generalized linear models) with multiple distribution families: Gaussian, Poisson, Negative Binomial, Binomial, Gamma, Inverse Gaussian.
- Supports discrete choice models (Logit, Probit, Multinomial Logit, Poisson regression).
- Includes time series analysis tools (AR, ARMA), robust standard errors, and diagnostic tests.
- Test-driven development (TDD) process with validation against R and Stata outputs.
- Open-source, BSD-licensed, integrated with the Python scientific computing ecosystem.

## Key Data Points

- GLM families include Poisson and Negative Binomial (used in the manuscript's ITSA)
- Validated against R and Stata results
- Available at: https://www.statsmodels.org

## Usage in Manuscript

- **Where cited:** Methods, Analysis section (line 89)
- **What it supports:** Cited as the software reference for the statistical analyses. The manuscript states: "Analyses were performed in Python 3 using statsmodels." Specifically, the Poisson GLM and Negative Binomial GLM from statsmodels were used for the interrupted time series segmented regression models.
- **Accuracy check:** Correct. Standard software citation for the statistical computing library used.
