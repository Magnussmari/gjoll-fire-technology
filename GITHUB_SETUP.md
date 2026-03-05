# GitHub Repository Setup

Run these commands from the `fire_technology/` folder on your Mac.

## Prerequisites

Make sure you have `gh` installed and authenticated:

```bash
brew install gh        # if not already installed
gh auth login          # follow prompts to authenticate
```

## Create and Push

```bash
cd ~/path/to/Gjoll_Gagnis/fire_technology

# Initialize (skip if .git/ already exists)
git init -b main

# Stage all files
git add README.md .gitignore requirements.txt manuscript.qmd references.bib \
  springer-fire-technology.csl STROBE_checklist_cross_sectional.md SUBMISSION_GUIDE.md \
  data/ figures/ scripts/

# Commit
git commit -m "Initial commit: Gjöll fatal fire incidents analysis (1968–2025)

Reproducibility package for Fire Technology submission.
Data: DOI 10.34881/I5WGJU | https://www.gjoll.is
113 incidents, 145 deaths, zero post-1998 fatalities."

# Create public repo and push
gh repo create gjoll-fire-technology --public --source=. --push \
  --description "Reproducibility package: Fatal Fire Incidents in Iceland 1968–2025"
```

## After Pushing

1. Go to https://github.com/YOUR_USERNAME/gjoll-fire-technology
2. Verify all files are present
3. Add the repo URL to the manuscript's Data Availability statement
4. Update Reference [8] if the repo URL should be cited separately

## Optional: Add Topics

```bash
gh repo edit gjoll-fire-technology --add-topic fire-safety,iceland,fire-fatalities,building-codes,open-data,reproducibility
```
