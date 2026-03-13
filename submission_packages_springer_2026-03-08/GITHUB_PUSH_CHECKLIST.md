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
