# Gjöll fatal-fire reproducibility package
# Quick start:  make setup && make verify
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
.PHONY: help setup verify refs reproduce analyses manuscript all clean

help:              ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

setup:             ## Install the Python dependencies
	$(PIP) install -r requirements.txt

verify:            ## Recompute every reported statistic from the deposited data (the gate)
	$(PYTHON) scripts/verify_statistics.py

refs:              ## Check that every reference DOI resolves (needs network)
	$(PYTHON) scripts/verify_references.py

reproduce:         ## Regenerate all tables and figures from the data
	$(PYTHON) scripts/reproduce_tables_figures.py

analyses:          ## Re-run the full analysis pipeline (denominator, ITSA, sensitivities)
	$(PYTHON) scripts/denominator_from_completions.py
	$(PYTHON) scripts/advanced_analyses.py
	$(PYTHON) scripts/revision_analyses.py
	$(PYTHON) scripts/reconcile_icd10.py

manuscript:        ## Render the manuscript + supplement to PDF (requires Quarto + LaTeX)
	quarto render manuscript/Smarason_2026_BriefCommunication.qmd --to pdf
	quarto render manuscript/supplementary.qmd --to pdf

all: verify reproduce analyses  ## Verify, then regenerate everything

clean:             ## Remove generated output
	rm -rf output/generated/* manuscript/*_files
