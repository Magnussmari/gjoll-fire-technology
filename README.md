# Fatal Fire Incidents in Iceland, 1968-2025

Reproducibility package for:

> **Fatal Fire Incidents in Iceland, 1968-2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation**
>
> Magnus Smari Smarason (ORCID: 0009-0008-2050-021X)
>
> Submitted to *Fire Technology*

## Data

The Gjoll registry export is deposited at **GAGNIS - Gagnathjónusta felagsvísinda** (University of Iceland Social Science Data Service):

- **DOI:** [10.34881/I5WGJU](https://doi.org/10.34881/I5WGJU)
- **Public interface:** [gjoll.is](https://www.gjoll.is)

This repository contains the analyzed export tables:

| File | Description | Records |
|------|-------------|---------|
| `data/fire_incidents_deaths_structure.csv` | Fatal structure fire incidents | 93 |
| `data/fire_incidents_deaths_other.csv` | Other fatal fire-related incidents | 20 |
| `data/population_1jan_MAN00000_1968_2025.csv` | Population (1 Jan), Statistics Iceland | 58 years |
| `data/export-metadata.json` | Export timestamp and row counts | -- |

## Reproduce

All manuscript tables and figures can be regenerated from the data:

```bash
pip install -r requirements.txt
python scripts/reproduce_tables_figures.py
python scripts/advanced_analyses.py
```

Output is written to `generated/`. The scripts also print all key claims and verify them against manuscript values.

## Manuscript

The manuscript source is `manuscript.qmd` (Quarto). To render:

```bash
quarto render manuscript.qmd --to pdf
quarto render manuscript.qmd --to docx
```

Requirements: [Quarto](https://quarto.org/) with a LaTeX distribution (TeX Live recommended).

## Repository Structure

```
fire_technology/
├── manuscript.qmd                            # Manuscript source (Quarto)
├── references.bib                            # BibTeX bibliography (22 entries)
├── springer-fire-technology.csl              # Citation style (Springer numeric)
├── STROBE_checklist_cross_sectional.md       # Supplementary File S1
├── SUBMISSION_GUIDE.md                       # Step-by-step submission instructions
├── requirements.txt                          # Python dependencies
├── data/
│   ├── fire_incidents_deaths_structure.csv
│   ├── fire_incidents_deaths_other.csv
│   ├── population_1jan_MAN00000_1968_2025.csv
│   └── export-metadata.json
├── figures/                                  # Manuscript figures (as submitted)
│   ├── fig1_annual_deaths.png
│   ├── fig2_monthly_seasonality.png
│   ├── fig3_structure_deaths_by_construction_year.png
│   └── fig4_itsa.png
├── scripts/
│   ├── reproduce_tables_figures.py           # Regenerates tables & figures 1-3
│   └── advanced_analyses.py                  # Person-years, sensitivity, ITSA (fig 4)
└── generated/                                # Script output (gitignored)
```

## Key Findings

- **113** fatal fire incidents, **145** deaths (1968-2025)
- **Zero** fatal structure fires in post-1998 buildings (where construction year is known)
- Mean construction year of fatal structure fire buildings: **1957** (1996+ complete subset)
- **58%** of incidents and deaths occur in October-March heating season
- Iceland's fire mortality rate (~5.5/million, 2010-2021) is the **lowest in the Nordic countries**
- ITSA: significant pre-existing decline (IRR = 0.93/year) and level decrease at 1999 (Poisson p = 0.010; NegBin p = 0.12)

## License

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Citation: Smarason, M.S. (2025). Godar nidurstoður, slæm gögn: tölfræðileg greining a arangri i brunavörnum 1968-2025. *A vakt fyrir Island*, 52(1), 32-39.

## Contact

Magnus Smari Smarason -- magnus@smarason.is -- [gjoll.is](https://www.gjoll.is)
