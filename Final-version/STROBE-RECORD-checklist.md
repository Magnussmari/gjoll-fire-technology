# STROBE + RECORD reporting checklist (completed)

**Manuscript:** Fatal Fire Incidents in Iceland, 1968–2025: A National Registry Study of
Building Construction Period and Fire Mortality
**Design:** Observational, national incident-level registry (ecological/cohort description)
**Guidelines:** STROBE (von Elm et al. 2007) with the RECORD extension for routinely-collected
observational data (Benchimol et al. 2015). Items are mapped to manuscript sections; section
names are stable across revisions (line numbers are not, so sections are cited).

| # | Item (STROBE / **RECORD** extension) | Reported? | Where |
|---|--------------------------------------|-----------|-------|
| 1 | Title/abstract: design in title or abstract; summary of what was done/found | Yes | Title; Abstract |
| **1.1** | **Type of data and databases named in title/abstract** | Yes | Title ("National Registry Study"); Abstract (Gjöll registry) |
| **1.2** | **Geographic region and timeframe named** | Yes | Title/Abstract (Iceland, 1968–2025) |
| **1.3** | **If linkage was done, stated in abstract** | N/A | No individual-level linkage; aggregate cross-check only (Methods) |
| 2 | Background/rationale | Yes | Introduction |
| 3 | Objectives / specific hypotheses | Yes | Introduction (final paragraph: aims i–iii) |
| 4 | Study design early in paper | Yes | Data and Methods (first paragraph); Fig 1 |
| 5 | Setting, locations, relevant dates | Yes | Data and Methods; 1968–2025, Iceland, registry finalized 31 Dec 2025 |
| 6 | Eligibility / participants | Yes | Data and Methods (all fatal fire incidents, no sampling) |
| **6.1** | **Population selection from routine data described** | Yes | Data and Methods (systematic archival review; ≥2 sources) |
| **6.2** | **Codes/algorithms to classify used; validation** | Yes | Data and Methods (relevance-based classification rule; blinded LLM re-code validation, κ=0.93) |
| **6.3** | **Data linkage flow diagram** | N/A | No record linkage; Fig 1 gives the compilation/analysis pipeline |
| 7 | Variables: outcomes, exposures, confounders | Yes | Data and Methods (fatal incident; construction-period cohorts; confounders enumerated) |
| **7.1** | **Classification codes/algorithms listed** | Yes | Data and Methods; classification rule + Supplementary §S2 |
| 8 | Data sources / measurement | Yes | Data and Methods (Tímarit.is, yearbooks, investigation reports, court records, Registers Iceland, Statistics Iceland) |
| 9 | Bias | Yes | Data and Methods (ascertainment/circularity risk); Limitations |
| 10 | Study size | Yes | Results (113 incidents, 145 deaths); no power calculation (full population) |
| 11 | Quantitative variables / groupings | Yes | Data and Methods (pre-/post-1998 cohorts; decade bins; construction-year bands) |
| 12 | Statistical methods | Yes | Data and Methods (exact Poisson rate ratios; segmented Poisson ITSA; NB/quasi-Poisson robustness; Durbin–Watson) |
| **12.1** | **Methods for cleaning routine data** | Yes | Data and Methods; Supplementary (denominator derivation) |
| **12.2** | **Linkage methods** | N/A | No linkage |
| **12.3** | **Sensitivity analyses** | Yes | Results (three classification conventions; halved-denominator; anchor 140k–155k); Supplementary |
| 13 | Participants (numbers at each stage) | Yes | Results (opening paragraph); construction-year completeness stated |
| **13.1** | **Detail of selection from routine data; flow** | Yes | Fig 1; Results (missingness by decade) |
| 14 | Descriptive data | Yes | Results; Table 1 |
| 15 | Outcome data | Yes | Results (deaths/incidents by period and cohort) |
| 16 | Main results (estimates, CIs) | Yes | Results; Table 2 (exact Poisson rate ratios + 95% CIs) |
| 17 | Other analyses (subgroups, sensitivity) | Yes | Results (ITSA; adversarial denominator); Supplementary |
| 18 | Key results | Yes | Discussion (first paragraph); Conclusions |
| 19 | Limitations | Yes | Limitations (six enumerated); Discussion |
| 20 | Interpretation | Yes | Discussion (descriptive-not-causal framing held throughout) |
| 21 | Generalisability | Yes | Discussion (small-state caveats; transferable method) |
| 22 | Funding | Yes | Funding statement (none) |
| **22.1** | **Accessibility of protocol, raw data, and code** | Yes | Data Availability (DATICE DOI 10.34881/I5WGJU; Gjöll interface; public code repo with verification script) |

**RECORD note on data access.** The analyzed registry tables are deposited (DOI
10.34881/I5WGJU) and browseable at the Gjöll interface; all analysis and a statistic-by-
statistic verification script are openly available in the reproducibility repository. The
blinded second-coding outputs are deposited as a frozen snapshot so the reported agreement
and Cohen's κ are recomputable offline without re-querying any model.
