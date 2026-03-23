# GitHub Push & Public Checklist

**Repo:** https://github.com/Magnussmari/gjoll-fire-technology
**Current visibility:** PRIVATE
**Status:** All today's work is uncommitted locally

---

## 1. Review what goes public

These files ARE part of the reproducibility package (push these):

- `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd` — manuscript source
- `references.bib` — bibliography
- `figures/*.png` — all 4 figures (now 300 DPI)
- `scripts/reproduce_tables_figures.py` — figure/table generation
- `scripts/advanced_analyses.py` — ITSA, person-years, sensitivity
- `scripts/readability.py` — readability analysis
- `scripts/verify_references.py` — reference verification
- `STROBE_checklist_cross_sectional.md` — supplementary material

These files are internal prep (do NOT push):

- `submission_packages_springer_2026-03-08/` — submission guide, cover letters, packages
- `edits/` — edit logs, transcript, PDFs
- `Smarason_2026_ANONYMOUS.*` — anonymized versions (for submission only)
- `references-anon.bib` — anonymized bibliography
- `Prompt_self_improvement.md` — unrelated

## 2. Update .gitignore

```bash
cat >> .gitignore << 'EOF'
submission_packages_springer_2026-03-08/
edits/
Smarason_2026_ANONYMOUS.*
references-anon.bib
Prompt_self_improvement.md
*.tex
EOF
```

## 3. Update README title

The README still says "Long-Run Trends" — update to "Long-Term Trends" and add Thomas Barry as co-author.

## 4. Commit and push

```bash
git add Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd references.bib figures/ scripts/ .gitignore
git commit -m "Update manuscript: add co-author, institutional effectiveness framing, 300 DPI figures"
git push origin main
```

## 5. Make repo public

```bash
gh repo edit Magnussmari/gjoll-fire-technology --visibility public
```

Or: GitHub.com → Settings → Danger Zone → Change visibility → Public

## 6. Verify

- [ ] Visit https://github.com/Magnussmari/gjoll-fire-technology — should be accessible without login
- [ ] No submission packages, edit logs, or anonymized files visible
- [ ] README shows both authors and correct title
- [ ] Data DOI link works: https://doi.org/10.34881/I5WGJU


I checked the repo state. Two important findings:

The README already uses **“Long-Term Trends”** and already lists **Thomas Barry** as co-author, so that item appears to be fixed in the current remote README .

What is *not* public-ready yet is that the README still contains collaborator-facing material, an edit-log link to `edits/edits.md`, and references to internal repo docs like `SUBMISSION_GUIDE.md` and `GITHUB_SETUP.md`, which makes the repo look like a working submission workspace rather than a clean public reproducibility package . Also, `.gitignore` does not yet exclude the internal prep material you listed .

What I would change before making it public:

Replace the README with a public-facing version that does only six things:

1. states the paper title and authors,
2. explains what the repo contains,
3. links the data DOI and Gjöll website,
4. shows how to reproduce figures/tables,
5. lists the core files,
6. gives a short contact/license note.

Remove from README:

* edit log section
* collaborator Git instructions
* issue/pull request tutorial
* references to `edits/`
* references to `SUBMISSION_GUIDE.md`
* references to `GITHUB_SETUP.md`

Update `.gitignore` to include:

```gitignore
submission_packages_springer_2026-03-08/
edits/
Smarason_2026_ANONYMOUS.*
references-anon.bib
Prompt_self_improvement.md
*.tex
```

Also remove these from the tracked public repo if they are already committed:

* `SUBMISSION_GUIDE.md`
* `GITHUB_SETUP.md`
* `qualitycontrol/` if you do not want internal QC artifacts public

A clean public README you can drop in:

````md
# Fatal Fire Incidents in Iceland, 1968–2025

Reproducibility package for:

**Fatal Fire Incidents in Iceland, 1968–2025: Long-Term Trends, Building Age, and the Effectiveness of Fire Safety Regulation**

Magnús Smári Smárason (ORCID: 0009-0008-2050-021X)  
Thomas Barry (ORCID: 0000-0002-0633-3602)

Target journal: *Fire Technology*

## Overview

This repository contains the manuscript source, reproducibility scripts, figures, and supporting materials for the analysis of fatal fire incidents in Iceland from 1968 to 2025.

## Data

The Gjöll registry export is deposited at **GAGNÍS – Gagnaþjónusta félagsvísinda**:

- DOI: https://doi.org/10.34881/I5WGJU
- Public interface: https://www.gjoll.is

## Repository contents

- `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd` — manuscript source
- `references.bib` — bibliography
- `figures/` — manuscript figures
- `scripts/reproduce_tables_figures.py` — tables and figures
- `scripts/advanced_analyses.py` — ITSA, person-years, sensitivity analysis
- `scripts/readability.py` — readability checks
- `scripts/verify_references.py` — bibliography/reference checks
- `STROBE_checklist_cross_sectional.md` — supplementary material

## Reproducibility

Install dependencies and run:

```bash
pip install -r requirements.txt
python scripts/reproduce_tables_figures.py
python scripts/advanced_analyses.py
````

## Render manuscript

```bash
quarto render Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd --to pdf
quarto render Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd --to docx
```

## Key findings

* 113 fatal fire incidents and 145 deaths, 1968–2025
* Zero fatal structure fires observed in post-1998 buildings where construction year is known
* Fatalities are concentrated in older building stock
* 58% of incidents and deaths occur during the October–March heating season

## License

Data: CC BY 4.0

## Contact

Magnús Smári Smárason
[magnus@smarason.is](mailto:magnus@smarason.is)
[https://www.gjoll.is](https://www.gjoll.is)

````

Then the cleanup sequence should be:

```bash
cat >> .gitignore << 'EOF'
submission_packages_springer_2026-03-08/
edits/
Smarason_2026_ANONYMOUS.*
references-anon.bib
Prompt_self_improvement.md
*.tex
EOF

git rm -r --cached submission_packages_springer_2026-03-08 edits 2>/dev/null || true
git rm --cached SUBMISSION_GUIDE.md GITHUB_SETUP.md 2>/dev/null || true
git rm --cached references-anon.bib Prompt_self_improvement.md 2>/dev/null || true

git add .gitignore README.md
git add Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd references.bib figures/ scripts/ STROBE_checklist_cross_sectional.md
git commit -m "Prepare public reproducibility repo"
git push origin main
````

After that, switch visibility to public.

One thing I could not do from here was directly push those changes into the repo, because I do not have your current local uncommitted files in this session. But I was able to verify what the current remote README and `.gitignore` look like, and the main public-facing fix is clearly the README cleanup plus stricter ignore rules .


Good—this is the right moment to be precise. I’ll list the **exact edits needed** to make your repo *publication-grade*, not just “clean enough”.

---

# 🔴 1. README — must be rewritten (major)

## Problems identified

From the current version:

* Contains **internal workflow instructions** (issues, PRs, collaborators) → not appropriate
* Mentions:

  * `edits/edits.md` ❌
  * `SUBMISSION_GUIDE.md` ❌
  * `GITHUB_SETUP.md` ❌
* Reads like a **project workspace**, not a **scientific reproducibility package**

## Required edits

### ❌ Remove entirely:

* “Recent Changes / Revision History”
* “Contributor Notes”
* “For Collaborators”
* Any mention of:

  * `edits/`
  * submission workflow
  * GitHub usage instructions
* Any dev instructions unrelated to reproduction

### ✅ Add / keep:

* Clean title + authors (with Thomas Barry)
* Short **scientific description**
* Data DOI + Gjöll link
* Reproducibility instructions
* Minimal structure overview
* Key findings (tight, not verbose)

👉 Outcome: README becomes a **paper companion**, not a lab notebook

---

# 🟡 2. `.gitignore` — incomplete (critical)

## Current issue

It does **not exclude sensitive/internal files**.

## Required additions

```gitignore
# Submission / journal material
submission_packages_springer_2026-03-08/

# Internal work
edits/

# Anonymous submission versions
Smarason_2026_ANONYMOUS.*
references-anon.bib

# Personal / irrelevant
Prompt_self_improvement.md

# Build artifacts
*.tex
generated/
```

👉 This prevents accidental exposure when you push

---

# 🔴 3. Remove already-tracked sensitive files (if present)

Even with `.gitignore`, Git will still track files already committed.

## Required actions

Remove from repo:

* `SUBMISSION_GUIDE.md`
* `GITHUB_SETUP.md`
* `edits/`
* `submission_packages_springer_2026-03-08/`
* anonymized manuscript files

```bash
git rm -r --cached submission_packages_springer_2026-03-08 edits
git rm --cached SUBMISSION_GUIDE.md GITHUB_SETUP.md
git rm --cached Smarason_2026_ANONYMOUS.* references-anon.bib
```

👉 These are **submission artifacts**, not reproducibility materials

---

# 🟡 4. Repository structure — tighten to “scientific core”

## Keep (correct)

✔ manuscript `.qmd`
✔ `references.bib`
✔ `figures/`
✔ `scripts/`
✔ STROBE checklist
✔ data/ (if included)

## Optional (decide deliberately)

* `requirements.txt` → ✔ keep (good practice)
* `qualitycontrol/` → ❓ remove unless you want transparency

👉 Rule: *If a reviewer wouldn’t need it, don’t include it*

---

# 🟡 5. File naming consistency (important for journal credibility)

## Issue

You currently mix:

* `manuscript.qmd`
* `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd`

## Fix

Choose **ONE canonical filename**:

👉 Recommended:

```
Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd
```

Then update:

* README
* scripts (if referenced)
* render commands

---

# 🟡 6. Reproducibility instructions — tighten

## Current issue

Instructions exist but are slightly inconsistent.

## Fix

Make them minimal and deterministic:

```bash
pip install -r requirements.txt
python scripts/reproduce_tables_figures.py
python scripts/advanced_analyses.py
```

Optional:

* Add expected outputs (e.g., `generated/fig1.png`)

---

# 🟡 7. Remove submission-specific language

From README and repo:

### ❌ Remove:

* “Submitted to Fire Technology”
* Editorial Manager references
* Cover letter language
* OA agreement notes

### Why:

Public repo = **timeless artifact**, not submission snapshot

---

# 🟡 8. Data availability alignment

Ensure consistency between:

* README
* manuscript
* DOI statement

Must all say:

* DOI link works
* Gjöll site works
* repo URL will be inserted

---

# 🟢 9. Small polish (high impact)

### Fix typography:

* Use **en dash consistently** (1968–2025 or 1968-2025 — pick one)
* Avoid mixed ASCII/Unicode inconsistencies

### Authors:

* Include both:

  * names
  * ORCID (optional but strong signal)

---

# 🟢 10. Final verification checklist (before public)

Run this mentally:

* [ ] No `edits/` folder visible
* [ ] No submission packages
* [ ] No anonymized files
* [ ] README is clean and academic
* [ ] Scripts run without manual fixes
* [ ] Figures match manuscript
* [ ] DOI link works
* [ ] Repo understandable in <30 seconds

---

# 🔥 Bottom line

Right now your repo is:

> **“working research environment”**

After edits it becomes:

> **“journal-grade reproducibility artifact”**

---

If you want, I can next:

* audit your actual file tree (paste `tree -L 2`)
* or rewrite your README *perfectly tuned for reviewers* (slightly sharper than the draft above)
