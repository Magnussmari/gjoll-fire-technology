# Fatal Fire Incidents in Iceland, 1968-2025

Reproducibility package for:

> **Fatal Fire Incidents in Iceland, 1968-2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation**
>
> Magnus Smari Smarason (ORCID: 0009-0008-2050-021X)
>
> Target journal: *Fire Technology* (Springer Nature)

---

## For Collaborators: How to Review and Comment

This section explains how to work with this repository as a collaborator. No prior Git experience is assumed. If you get stuck at any point, just message Magnus.

### What you need to install (one-time setup)

1. **Git** (version control)
   - **Mac:** Open Terminal and run `xcode-select --install` (Git comes with the Xcode tools)
   - **Windows:** Download from [git-scm.com](https://git-scm.com/download/win) and install with default settings

2. **A text editor** (to read and comment on the manuscript)
   - [VS Code](https://code.visualstudio.com/) is free and excellent. It highlights Quarto/Markdown syntax and shows Git changes visually.
   - Alternatively, any text editor works (even TextEdit or Notepad), but VS Code makes everything easier.

3. **GitHub account** -- You should already have one if Magnus added you as a collaborator.

### Getting the repository onto your computer

Open a terminal (Mac: Terminal.app; Windows: Git Bash) and run:

```bash
# Navigate to where you want the project folder
cd ~/Documents

# Clone the repository (this downloads everything)
git clone https://github.com/Magnussmari/gjoll-fire-technology.git

# Enter the project folder
cd gjoll-fire-technology
```

You now have a local copy of the entire project: manuscript, data, scripts, and figures.

### The manuscript file

The manuscript is a single file:

```
Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd
```

This is a Quarto Markdown file -- it looks like plain text with some formatting codes. You can read and edit it in any text editor. The actual prose is easy to find: it reads like a normal paper, with sections, paragraphs, and references in `[@AuthorYear]` format.

If you prefer Word, a `.docx` version is available (ask Magnus or render it yourself with Quarto).

### How to give feedback

There are three ways to comment, from simplest to most powerful. Use whichever feels comfortable.

#### Option A: GitHub Issues (simplest, no Git needed)

Go to [github.com/Magnussmari/gjoll-fire-technology/issues](https://github.com/Magnussmari/gjoll-fire-technology/issues) in your browser and click **New Issue**. Write your feedback as free text. You can reference specific sections ("In Section 3.4, the Poisson CI...") or quote specific lines.

This is the easiest option if you just want to write comments without touching any files.

#### Option B: Edit directly on GitHub (easy, no local tools needed)

1. Go to the repository on GitHub
2. Click on `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd`
3. Click the pencil icon (Edit this file) in the top right
4. Make your changes or add comments directly in the text (use `<!-- Tom: your comment here -->` for comments that should not appear in the final paper)
5. Scroll down, write a brief description of what you changed (e.g., "Suggested rewording of Discussion paragraph 2")
6. Select **"Create a new branch for this commit and start a pull request"**
7. Click **Propose changes**

This creates a "pull request" -- a proposed set of changes that Magnus can review, discuss, and accept or modify. It is the academic equivalent of track changes, but with a full audit trail.

#### Option C: Local editing with Git (most powerful)

This is the standard workflow for collaborative research. It gives you full control and works offline.

```bash
# 1. Make sure you have the latest version
git pull

# 2. Create a branch for your review
#    (this keeps your changes separate from the main manuscript until they are ready)
git checkout -b tom-review

# 3. Open the manuscript in your editor and make changes
#    In VS Code:
code Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd

# 4. When you are done, save the file, then:
git add Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd
git commit -m "Tom: suggested edits to Discussion and Limitations sections"

# 5. Push your branch to GitHub
git push -u origin tom-review

# 6. Go to GitHub -- it will show a banner offering to create a pull request.
#    Click it, add a description, and submit.
```

Magnus will then see your proposed changes as a clear diff (additions in green, removals in red), can comment line-by-line, and merge what works.

### Commenting conventions

When adding comments inside the manuscript text, use HTML comment syntax:

```markdown
<!-- Tom: I think this paragraph could be tightened. The point about
     socioeconomic selection is strong but gets buried in the middle. -->
```

These comments are invisible in the rendered PDF/DOCX but visible in the source file. This lets you annotate freely without affecting the output.

For suggested rewording, you can either:
- Replace the text directly (the Git diff will show exactly what changed), or
- Add a comment with your suggested alternative:

```markdown
<!-- Tom: Consider replacing the above with:
"The zero-event finding, while statistically informative, should be
interpreted in light of the substantial confounding discussed above." -->
```

### Understanding the project structure

```
gjoll-fire-technology/
|
|-- Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd   <-- THE MANUSCRIPT (start here)
|-- references.bib                                    <-- Bibliography (BibTeX)
|-- springer-fire-technology.csl                      <-- Citation style
|
|-- data/                          <-- Raw data exports from Gjoll registry
|   |-- fire_incidents_deaths_structure.csv    (93 structure fire incidents)
|   |-- fire_incidents_deaths_other.csv        (20 other fire-related incidents)
|   |-- population_1jan_MAN00000_1968_2025.csv (population denominators)
|   +-- export-metadata.json
|
|-- figures/                       <-- Manuscript figures
|   |-- fig1_annual_deaths.png
|   |-- fig2_monthly_seasonality.png
|   |-- fig3_structure_deaths_by_construction_year.png
|   +-- fig4_itsa.png
|
|-- scripts/                       <-- Analysis code (Python)
|   |-- reproduce_tables_figures.py    (tables + figures 1-3)
|   |-- advanced_analyses.py           (person-years, sensitivity, ITSA)
|   |-- readability.py                 (Flesch-Kincaid analysis)
|   +-- verify_references.py          (DOI and bibliography verification)
|
|-- qualitycontrol/                <-- QC reports
|   |-- readability_report.txt
|   +-- references_report.txt
|
|-- STROBE_checklist_cross_sectional.md   <-- Supplementary File S1
|-- SUBMISSION_GUIDE.md                   <-- Fire Technology submission instructions
|-- GITHUB_SETUP.md                       <-- Repo setup notes
+-- requirements.txt                      <-- Python dependencies
```

### Why Git instead of Word track changes?

This is worth explaining because it is a different workflow from what most academics are used to.

**Track changes in Word** works well for two people editing one document back and forth. It breaks down when:
- Multiple people edit simultaneously
- You want to see the full history of every change ever made
- You need to reproduce the analysis from the same version of the code
- You want to revert a change from three weeks ago without losing everything since

**Git** solves all of these. Every change is recorded with who made it, when, and why. You can work on your own branch without interfering with anyone else. Changes are proposed as pull requests, discussed line-by-line, and merged when ready. The entire history is preserved forever.

For this project specifically, Git also keeps the manuscript, data, analysis scripts, and figures in one place with a shared version history. When we submit, reviewers can trace any number in the paper back through the scripts to the raw data -- that level of reproducibility is increasingly expected in quantitative research.

The learning curve is real but short. After one or two rounds of edits, the workflow becomes natural. And the skills transfer to any future collaborative research project.

### Quick Git reference

| What you want to do | Command |
|---|---|
| Get the latest changes | `git pull` |
| See what you have changed | `git status` |
| See the actual changes | `git diff` |
| Save your changes locally | `git add -A && git commit -m "description"` |
| Send changes to GitHub | `git push` |
| Create a new branch | `git checkout -b branch-name` |
| Switch back to main | `git checkout main` |
| Undo changes to a file | `git checkout -- filename` |

If something goes wrong, `git status` will almost always tell you what to do next. And you cannot break anything permanently -- Git keeps everything.

---

## Data

The Gjoll registry export is deposited at **GAGNIS - Gagnathjónusta felagsvísinda** (University of Iceland Social Science Data Service):

- **DOI:** [10.34881/I5WGJU](https://doi.org/10.34881/I5WGJU)
- **Public interface:** [gjoll.is](https://www.gjoll.is)

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

Output is written to `generated/`.

## Render the Manuscript

The manuscript source is `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd` (Quarto). To render:

```bash
quarto render Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd --to pdf
quarto render Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd --to docx
```

Requirements: [Quarto](https://quarto.org/) with a LaTeX distribution (TeX Live recommended).

## Key Findings

- **113** fatal fire incidents, **145** deaths (1968-2025)
- **Zero** fatal structure fires in post-1998 buildings (where construction year is known)
- Mean construction year of fatal structure fire buildings: **1957** (1996+ complete subset)
- **58%** of incidents and deaths occur in October-March heating season
- Iceland's fire mortality rate (~5.5/million, 2010-2021) is the **lowest in the Nordic countries**
- ITSA: significant pre-existing decline (IRR = 0.93/year) and level decrease at 1999 (Poisson p = 0.010; NegBin p = 0.12)

## License

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Contact

Magnus Smari Smarason -- magnus@smarason.is -- [gjoll.is](https://www.gjoll.is)
