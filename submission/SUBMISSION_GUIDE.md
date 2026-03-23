# Fire Technology — Submission Guide

**Last updated:** 4 March 2026 (post peer-review R2)

## Your Submission Package

Everything you need is in this folder (`fire_technology/`):

| File | Purpose |
|------|---------|
| `manuscript.qmd` | Manuscript source (Quarto — single source of truth) |
| `manuscript.pdf` | Rendered PDF (run `quarto render manuscript.qmd --to pdf`) |
| `manuscript.docx` | Rendered DOCX (run `quarto render manuscript.qmd --to docx`) |
| `references.bib` | BibTeX bibliography (22 entries) |
| `figures/fig1_annual_deaths.png` | Fig. 1 — Annual deaths trend |
| `figures/fig2_monthly_seasonality.png` | Fig. 2 — Monthly seasonality |
| `figures/fig3_structure_deaths_by_construction_year.png` | Fig. 3 — Construction year distribution |
| `figures/fig4_itsa.png` | Fig. 4 — Interrupted time series analysis |
| `STROBE_checklist_cross_sectional.md` | Supplementary File S1 |
| `data/` | CSV data files (for reproducibility/data availability) |

---

## Pre-Submission Tasks (DO THESE FIRST)

### Task 1: Verify the Hjarðarhagi 2025 Incident

The manuscript contains a footnote (Section 4.2) about a May 2025 fatal fire in Hjarðarhagi, Reykjavík. Before submitting:

1. Check HMS Mannvirkjaskrá or police report for the building's construction year
2. If pre-1998: the post-1998 finding is unaffected; optionally add the year to the footnote
3. If post-1998: update the registry, revise Section 3.3/4.2, and adjust the core finding
4. If still unverified: the current footnote is sufficient

### Task 2: Confirm UNAK Affiliation

The Springer Nature / Iceland Consortium OA agreement covers the APC — but you need an eligible affiliation. Your manuscript currently says "Independent Researcher (affiliated with Háskólinn á Akureyri)."

1. **Contact your co-author at UNAK** and confirm they will be listed as a co-author or that you have a formal affiliation (e.g., adjunct, research associate, guest researcher).
2. **Contact the UNAK library** (bokasafn@unak.is) and ask:
   - "Is UNAK part of the Springer Nature Iceland Consortium agreement for open access publishing?"
   - "As an affiliated researcher, am I eligible to publish OA with APC covered?"
3. **If eligible:** Make sure you use your UNAK email address (or that UNAK is listed as your institution) during the submission — the system matches your affiliation to the agreement automatically.
4. **If not directly eligible:** Ask if the UNAK academic you're working with can be corresponding author (they would need to submit, and their UNAK affiliation triggers the OA agreement).

### Task 3: Prepare GitHub Reproducibility Repository

The manuscript references a public repository [8]. Before submission, ensure:

1. The reproducibility repo is public at a permanent URL (GitHub)
2. It contains the data exports, analysis scripts, and generated figures
3. The GAGNÍS deposit (DOI: 10.34881/I5WGJU) is accessible

---

## Step-by-Step Submission Process

### Step 1: Create an Account on Editorial Manager

1. Go to: **https://www.editorialmanager.com/fire/default.aspx**
   (This is Fire Technology's submission portal on Editorial Manager)
2. Click **"Register Now"** if you don't have an account
3. Fill in your details — use your UNAK-affiliated email if possible
4. Set your ORCID: `0009-0008-2050-021X`

### Step 2: Start a New Submission

1. Log in to Editorial Manager
2. Click **"Submit New Manuscript"**
3. Select article type: **"Original Research"** (sometimes called "Regular Manuscript")
4. Fill in the metadata:
   - **Title:** Fatal Fire Incidents in Iceland, 1968–2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation
   - **Authors:** Magnús Smári Smárason (+ co-author from UNAK if applicable)
   - **Keywords:** fire fatalities; fire safety regulation; building codes; building age; fire statistics; Iceland; Nordic countries; fire prevention
   - **Abstract:** Copy from the manuscript

### Step 3: Upload Files

Upload the following files in this order:

1. **Manuscript** → `manuscript.docx` or `manuscript.pdf` (file type: "Manuscript")
2. **Figure 1** → `fig1_annual_deaths.png` (file type: "Figure")
3. **Figure 2** → `fig2_monthly_seasonality.png` (file type: "Figure")
4. **Figure 3** → `fig3_structure_deaths_by_construction_year.png` (file type: "Figure")
5. **Figure 4** → `fig4_itsa.png` (file type: "Figure")
6. **Supplementary** → STROBE checklist (file type: "Supplementary Material")

### Step 4: Write a Cover Letter

When prompted, paste a cover letter. Here is a draft:

---

Dear Editor,

We submit the enclosed manuscript, "Fatal Fire Incidents in Iceland, 1968–2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation," for consideration as an Original Research article in Fire Technology.

The manuscript presents a 58-year national dataset of all fatal fire incidents in Iceland, compiled through systematic historical source review with cross-verification across independent sources. The key finding is that no fatal structure-fire incidents occurred in buildings constructed after 1998—the year modern prescriptive fire safety requirements were adopted—while fatalities concentrate in older building stock (mean construction year 1957) and during the October–March heating season. The dataset is publicly deposited (DOI: 10.34881/I5WGJU) with full reproducibility scripts and a public GitHub repository.

We believe this work is of interest to Fire Technology readers because it provides a rare, complete national case study demonstrating the long-run effectiveness of building fire safety regulation, while also documenting emerging challenges (unauthorized residential use of commercial buildings, arson targeting vulnerable populations) that require interdisciplinary responses.

The manuscript has not been published elsewhere and is not under consideration by another journal. All authors have approved the manuscript.

Sincerely,
Magnús Smári Smárason
magnus@smarason.is
https://www.gjoll.is

---

### Step 5: Complete Required Statements

Editorial Manager will ask you to confirm several statements during submission:

- **Conflict of Interest:** "The author declares no competing interests."
- **Data Availability:** "Data deposited at GAGNÍS (DOI: 10.34881/I5WGJU), https://www.gjoll.is, and [GitHub repo URL]. Reproducibility scripts regenerate all tables and figures from the deposited data."
- **Ethics:** "No personal identifiers. Historical address-level data not analyzed at individual level."
- **Funding:** "No specific funding received."
- **AI Disclosure:** "Generative AI tools used for analytical code development; all outputs independently verified by the author."

### Step 6: Select Open Access (Springer Nature / Iceland Consortium)

After your paper is accepted, you will be asked about publishing options:

1. Select **"Open Access"** (Gold OA)
2. The system should automatically detect your UNAK affiliation and apply the Iceland Consortium agreement
3. If it doesn't auto-detect, select the agreement manually or contact oa.verification@springernature.com
4. License: Choose **CC BY 4.0** (standard for fully funded OA)

### Step 7: Review and Submit

1. Editorial Manager will generate a PDF proof of your submission
2. Review it carefully — check that figures rendered correctly, tables are intact, and special characters (Icelandic letters) display properly
3. Click **"Approve Submission"**

---

## Timeline Expectations

- **Submission to first decision:** ~46 days (median for Fire Technology)
- **Typical review cycle:** 2–3 months including revisions
- **Publication after acceptance:** ~2–4 weeks online

## Key Contacts

| Who | Email | When to contact |
|-----|-------|-----------------|
| Fire Technology editorial office | Via Editorial Manager | Submission questions |
| UNAK library | bokasafn@unak.is | OA agreement eligibility |
| Springer Nature OA verification | oa.verification@springernature.com | If OA agreement not auto-detected |

## Checklist Before You Hit Submit

- [ ] Hjarðarhagi building age verified (or footnote confirmed as sufficient)
- [ ] Co-author / affiliation at UNAK confirmed
- [ ] OA eligibility confirmed with UNAK library
- [ ] GitHub reproducibility repo is public
- [ ] Editorial Manager account created with ORCID
- [ ] Manuscript uploaded (.docx from `quarto render manuscript.qmd --to docx`)
- [ ] All 4 figures uploaded separately (PNG)
- [ ] STROBE checklist uploaded as supplementary
- [ ] Cover letter pasted
- [ ] All declaration statements completed
- [ ] PDF proof reviewed and approved

## Revision History

| Date | What changed |
|------|-------------|
| Sep 2025 | Initial manuscript and submission package |
| Mar 4, 2026 | Incorporated practitioner article [10] per R1 review: 1968 bill context, 1992 regulation, Norway building age comparison, vulnerable populations, institutional data silos |
| Mar 4, 2026 | R2 fixes: Hjarðarhagi footnote, exposure quantification, MSB→MCF URL, fixed dead IHA link (→SSB [14]), added HMS completions ref [15] |
| Mar 4, 2026 | Bibliography audit: all 15 refs verified, URLs tested, citation cross-check passed |
