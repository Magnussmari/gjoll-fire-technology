# Fatal Fire Incidents in Iceland, 1968–2025

**A National Registry Study of Building Construction Period and Fire Mortality**

Magnús Smári Smárason & Thomas Barry · University of Akureyri (Háskólinn á Akureyri)
Target journal: **Fire Technology** (Springer Nature) · Article type: **Research**

## Status (2026-07-03): submission-ready

Blind multi-model peer review (five frontier models) converged on **Minor Revision, no rejections**. Every reported statistic reproduces from the deposited data via `scripts/verify_statistics.py` (**108/108 checks pass**, enforced in CI on the public repo). Remaining before submission: co-author (T.B.) sign-off + optional UNAK open-access confirmation. Full status: `reports/STATUS.md`.

## The submission package → `Final-version/`

Everything needed to submit is in **`Final-version/`** (start with its `SUBMISSION-GUIDE.md`): the double-anonymous manuscript, separate title page, anonymized supplement, cover letter, and the draft emails to the co-author and the UNAK library. Fire Technology is double-anonymous and submits via SNAPP.

## Repository layout

```
manuscript/     current manuscript (Quarto): Smarason_2026_BriefCommunication.qmd
                + Smarason_2026_ANONYMIZED.qmd (double-blind) + supplementary[_ANON].qmd
data/           deposited registry CSVs + population + IDN03001 dwelling completions
scripts/        analysis + verification (verify_statistics.py, advanced_analyses.py,
                revision_analyses.py, denominator_from_completions.py,
                reproduce_tables_figures.py, blinded_second_coding.py, multi_peer_review.py)
figures/        publication figures (PNG)
output/         generated tables/figures (regenerable; gitignored)
reports/        peer reviews, STATUS.md, MORNING-REPORT
research/        source PDFs + paired notes
Final-version/  the submission package (see above)
_archive/       superseded material (full-length manuscript, March submission, edits, review rounds)
```

## Reproduce

```bash
pip install -r scripts/requirements.txt
python scripts/verify_statistics.py        # 108/108 — recomputes every manuscript number
python scripts/reproduce_tables_figures.py
python scripts/advanced_analyses.py
python scripts/revision_analyses.py
python scripts/denominator_from_completions.py
```

Data: DOI **10.34881/I5WGJU** · public interface **https://www.gjoll.is** · code **https://github.com/Magnussmari/gjoll-fire-technology**

## Directory-deviation notes (per 02_publications template)

- `manuscript/` holds the **current** (compact) manuscript; the superseded full-length draft is in `_archive/manuscript-full-length-superseded/`.
- `Final-version/` is the current submission package (kept at root by request); the old March submission attempt is in `_archive/submission-march-2026/`.
