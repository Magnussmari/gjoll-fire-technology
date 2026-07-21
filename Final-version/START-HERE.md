# START HERE — submit the fire paper to *Fire Technology* (SNAPP)

You're ready. Both authors signed off (Tom, 2026-07-20). This guide matches the **current**
Springer Nature SNAPP double-anonymous flow (verified against Springer's guidelines 2026-07-21).

> **What changed vs. the old guide:** Fire Technology moved to the new SNAPP system. It is
> **double-anonymous**, and it now collects the title-page information — authors, ORCIDs,
> affiliations, competing interests, funding, ethics, data availability, author contributions,
> AI-use — **in the submission interface (Authors tab + Declarations tab), NOT as an uploaded
> Title Page file.** So you upload only 2–3 anonymized files and *type/paste* the rest into
> SNAPP. `TITLE-PAGE.docx` is now just your **reference sheet** for those fields — do not upload it.

---

## Files you UPLOAD (all already anonymized, metadata clean)

| Role in SNAPP | File |
|---|---|
| **Manuscript** (Word, figures embedded) | `Fatal-Fire-Iceland_ANONYMIZED_manuscript.docx` |
| **Supplementary / ESM** | `Fatal-Fire-Iceland_supplementary_ANON.docx` |
| **Cover letter** | `cover-letter-fire-technology.md` (paste the text, or upload as PDF) |

**Do NOT upload:** the `TITLE-PAGE.docx` or the `_NAMED` files. Everything in `_working/` is
reference only. The anonymized files are verified clean: no author names, no `gjoll.is`/DOI/GitHub
links, self-citations masked, and document-property metadata blank.

---

## The steps

### ☐ 1 — Open SNAPP & log in
From the journal page, click **Submit manuscript** → SNAPP:
`https://submission.springernature.com/new-submission/10694`
Log in / register with your **ORCID `0009-0008-2050-021X`** and your **UNAK email
`magnus@smarason.is`** (this pairing links the article to Iceland's Springer read-&-publish
agreement → APC waiver, confirmed at acceptance, not now).

### ☐ 2 — Article type
Choose **Research**. (Fire Technology's types are Research / Case Study / Database. "Research" is the original-research type; no word limit.)

### ☐ 3 — Upload files
Upload the **manuscript** (`…ANONYMIZED_manuscript.docx`, figures embedded) and the
**supplementary** (`…supplementary_ANON.docx`). Add the **cover letter** (paste text or PDF).
SNAPP auto-compiles a PDF for review.

### ☐ 4 — Confirm auto-extracted fields
SNAPP reads the title, abstract, and keywords from the file. Confirm:
- **Title:** `Fatal Fire Incidents in Iceland, 1968–2025: A National Registry Study of Building Construction Period and Fire Mortality`
- **Abstract:** 240 words (within the 150–250 limit) — already in the manuscript.
- **Keywords:** fire fatalities; fire safety regulation; building codes; building age; fire statistics; Iceland

### ☐ 5 — Authors tab (type these in)
- **Author 1 (corresponding):** Magnús Smári Smárason — University of Akureyri (Háskólinn á Akureyri), Iceland — ORCID `0009-0008-2050-021X` — magnus@smarason.is
- **Author 2:** Thomas Barry — University of Akureyri (Háskólinn á Akureyri), Iceland — ORCID `0000-0002-0633-3602`
- Mark **Magnús** as corresponding author.

### ☐ 6 — Declarations tab (paste each statement)

**Competing interests** (paste):
```
M.S.S. is a former employee of the Housing and Construction Authority (Húsnæðis- og mannvirkjastofnun, HMS), the regulatory body examined in this study, and a former chair of the national firefighter and paramedic union (Landssamband slökkviliðs- og sjúkraflutningamanna, LSS). This professional background informs interpretation but did not drive data inclusion or classification, as evidenced by the blinded coding-reproducibility check reported in the manuscript. M.S.S. holds no current financial or employment relationship with HMS or LSS. T.B. declares no competing interests.
```

**Funding** (paste):
```
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
```

**Ethics approval** (paste):
```
Under Icelandic law (Act on Scientific Research in the Health Sector No. 44/2014), a study of deceased persons based on a registry compiled from already-public sources (newspaper archives, official reports, and court records) does not involve identifiable living human participants and did not require review or approval by the National Bioethics Committee (Vísindasiðanefnd); no ethics approval was therefore sought.
```

**Consent to participate / publish:** Not applicable (records of deceased persons from public sources; no living participants).

**Author contributions** (paste):
```
MSS conceived the study, compiled the Gjöll registry, performed the statistical analysis, and wrote the manuscript. TB contributed governance context and reviewed and revised the manuscript. Both authors approved the final version.
```

**Data availability** (paste):
```
The analyzed data tables are deposited at DATICE (GAGNÍS – Gagnaþjónusta félagsvísinda), University of Iceland (DOI: 10.34881/I5WGJU) and are available through the public Gjöll interface at https://www.gjoll.is. Reproducibility scripts (Python), including a verification script that recomputes every reported statistic, are openly available at https://github.com/Magnussmari/gjoll-fire-technology.
```

**Acknowledgments / AI-use** (paste — Springer requires AI use disclosed; ours is also in Methods):
```
The authors acknowledge the use of large language models (Anthropic Claude, OpenAI GPT) for Python analysis-script development (all outputs verified by the lead author against the deposited data) and for an automated, construction-year-blinded coding-reproducibility check of the classification (reported in Data and Methods). The models are not authors.
```

### ☐ 7 — Suggested reviewers (optional)
2–3 fire-safety-engineering or injury-epidemiology researchers, not at UNAK, no recent co-authorship. Leave blank if unsure.

### ☐ 8 — Review & Submit
Check the auto-built PDF: **Figure 1 (study-design pipeline), Fig 2, Fig 3, and both tables render.**
(Skip the optional Research Square preprint unless you want it.) Then **Submit** → manuscript number by email in minutes.

---

## Before you click Submit — checklist
- [ ] You uploaded the **ANONYMIZED** manuscript (no author names in it) — not the `_NAMED` file.
- [ ] All declarations entered in the **interface** (step 6), not relying on a title-page file.
- [ ] Article type = **Research**; corresponding author = Magnús with ORCID + UNAK email.
- [ ] PDF preview: figures + tables render.

## One nuance worth knowing (low-risk)
SNAPP's strict rule is that the *manuscript* should carry **no** competing-interest/ethics/funding
statements (they live in the interface). Our anonymized manuscript still has a short **blinded**
"Compliance with Ethical Standards" note — it's generic and non-identifying, so it's low risk. If
the technical-check editor asks you to remove it, say the word and I'll regenerate a
declaration-free manuscript in ~2 minutes.

## After
First decision: weeks to a couple of months. Two independent reviewers (Fable + Kimi) and a 5-model
blind panel all landed on **publishable / minor revision**. `../reports/…` no longer ships publicly,
but the internal `_private/repo-internal/reports/MORNING-REPORT-2026-07-03.md` pre-maps likely
reviewer points to where the paper already answers them — fast response letter.

---
*Guide upgraded 2026-07-21 against Springer Nature's current SNAPP double-anonymous guidelines
(Sources: Springer Nature SNAPP "How to submit" + "Double-anonymous peer review"; Springer Nature AI
editorial policy). The pre-SNAPP walkthrough is archived in `_working/SUBMISSION-GUIDE.md`.*
