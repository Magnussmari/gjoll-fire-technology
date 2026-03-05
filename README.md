# Fatal Fire Incidents in Iceland, 1968–2025

Reproducibility package for:

> **Fatal Fire Incidents in Iceland, 1968–2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation**
>
> Magnús Smári Smárason (ORCID: 0009-0008-2050-021X)
>
> Submitted to *Fire Technology*

## Data

The Gjöll registry export is deposited at **GAGNÍS – Gagnaþjónusta félagsvísinda** (University of Iceland Social Science Data Service):

- **DOI:** [10.34881/I5WGJU](https://doi.org/10.34881/I5WGJU)
- **Public interface:** [gjoll.is](https://www.gjoll.is)

This repository contains the analyzed export tables:

| File | Description | Records |
|------|-------------|---------|
| `data/fire_incidents_deaths_structure.csv` | Fatal structure fire incidents | 93 |
| `data/fire_incidents_deaths_other.csv` | Other fatal fire-related incidents | 20 |
| `data/population_1jan_MAN00000_1968_2025.csv` | Population (1 Jan), Statistics Iceland | 58 years |
| `data/export-metadata.json` | Export timestamp and row counts | — |

## Reproduce

All manuscript tables and figures can be regenerated from the data:

```bash
pip install pandas matplotlib
python scripts/reproduce_tables_figures.py
```

Output is written to `generated/`. The script also prints all key claims and verifies them against manuscript values.

## Repository Structure

```
fire_technology/
├── manuscript.md                          # Manuscript source (Markdown)
├── manuscript_revised_r2.docx             # Manuscript (Word, submission-ready)
├── STROBE_checklist_cross_sectional.md    # Supplementary File S1
├── SUBMISSION_GUIDE.md                    # Step-by-step submission instructions
├── data/
│   ├── fire_incidents_deaths_structure.csv
│   ├── fire_incidents_deaths_other.csv
│   ├── population_1jan_MAN00000_1968_2025.csv
│   └── export-metadata.json
├── figures/                               # Manuscript figures (as submitted)
│   ├── fig1_annual_deaths.png
│   ├── fig2_monthly_seasonality.png
│   └── fig3_structure_deaths_by_construction_year.png
├── scripts/
│   └── reproduce_tables_figures.py        # Regenerates all tables & figures
└── generated/                             # Script output (not tracked in git)
```

## Key Findings

- **113** fatal fire incidents, **145** deaths (1968–2025)
- **Zero** fatal structure fires in post-1998 buildings (where construction year is known)
- Mean construction year of fatal structure fire buildings: **1957** (1996+ complete subset)
- **58%** of incidents and deaths occur in October–March heating season
- Iceland's fire mortality rate (~5.5/million, 2010–2021) is the **lowest in the Nordic countries**

## License

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Citation: Smárason, M.S. (2025). Góðar niðurstöður, slæm gögn: tölfræðileg greining á árangri í brunavörnum 1968–2025. *Á vakt fyrir Ísland*, 52(1), 32–39.

## Contact

Magnús Smári Smárason — magnus@smarason.is — [gjoll.is](https://www.gjoll.is)
