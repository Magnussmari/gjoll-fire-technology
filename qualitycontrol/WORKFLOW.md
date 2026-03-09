# Quality Control Workflow

**Manuscript:** Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd
**Target journal:** Fire Technology (Springer)
**Last run:** 2026-03-09

---

## Pre-Submission Checklist

### 1. References Verification (`references_report.txt`)
- Cross-reference check: all bib entries vs manuscript citations
- Field completeness: DOI, URL, year, author for each entry
- DOI verification: HTTP status check for all DOIs
- URL verification: HTTP status check for all URLs
- Local source inventory: which PDFs/MDs are on disk

**Run:** Manual review + `curl` status checks on DOIs/URLs.

### 2. Source Usage Review (`source_usage_review.md`)
- For each cited source: read the actual paper
- Verify claims attributed to each source match the source content
- Flag any misattributions, unsupported claims, or missing citations
- Note advisory items (one-sided use, weaker sources, unused findings)

**Run:** Read all PDFs in `data/sources/`, cross-reference against manuscript text.

### 3. Readability Analysis (`readability_report.txt`)
- Word/sentence/syllable counts
- Flesch-Kincaid Grade Level (target: 12-17 for academic)
- Flesch Reading Ease (target: 20-40 for Fire Technology)
- Gunning Fog, Coleman-Liau, ARI, Dale-Chall

**Run:** Text extraction from rendered manuscript, standard readability formulas.

### 4. Source Files (`data/sources/`)
- Naming convention: `BibKey_short_description.{pdf,md}`
- Each PDF should have a companion `.md` reference summary
- Summary format: citation, abstract, key findings, manuscript usage, accuracy check

---

## Workflow Sequence

```
1. Edit manuscript (.qmd)
2. Update references.bib
3. Render to PDF (quarto render)
4. Run references verification
5. Run source usage review (after any new citations added)
6. Run readability analysis (after substantive text changes)
7. Log all edits in edits/edits.md
8. Commit and push
```

## File Structure

```
qualitycontrol/
  WORKFLOW.md                 # This file
  references_report.txt       # Bib/DOI/URL verification
  source_usage_review.md      # Citation accuracy review
  readability_report.txt      # Readability scores

data/sources/
  BibKey_description.pdf      # Source PDFs
  BibKey_description.md       # Reference summaries

edits/
  Tom_review_080326.md        # Co-author review comments
  insert_plan.md              # Edit plan (pre-execution)
  edits.md                    # Edit execution log
```
