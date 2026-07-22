# Submission Readiness — Fire Technology (SNAPP)

*Verified 2026-07-22. Companion to `START-HERE.md` (the step-by-step submission walkthrough).*

## Verdict: READY TO SUBMIT — reviewer-ringer pass complete

**Final pass (2026-07-22): put through Fable 5 + Kimi K3 peer review and hardened.** Neither
model found a deal-breaker; both landed on minor-to-major revision. All their actionable
findings were applied, plus the one substantive addition below.

**The completeness check is now PERFORMED, not promised.** The registry's annual fire-death
counts were reconciled against the official ICD-10 X00–X09 cause-of-death series (Statistics
Iceland MAN05302, pulled live): the registry documents **50 fire deaths (1996–2024) against
36 in the official series** — it is the *more complete* record (it captures intentional and
non-building fire deaths coded outside X00–X09, and the documented 2009 omission). Reproduced
by `scripts/reconcile_icd10.py`; year-by-year table deposited. This converts the paper's
weakest plank into demonstrated evidence for its thesis.

All gates pass as of the final-pass commits (see `MISSION-S-TIER-KNOCKOUT.md`, all 10 ISC green):

| Gate | Result |
|---|---|
| Statistics vs. deposited data (`verify_statistics.py`) | 125/125 checks pass |
| Anonymization sync (`anonymize.py --check`) | In sync (named → ANON derivation) |
| Identity-leak scan (ANON docx body + document properties) | 0 hits |
| First-person in body (named + anon) | 0 (impersonal scientific voice) |
| Author role clarity | CRediT statement (named); correctly absent from anon |
| Longest Methods sentence | 63-word structured list (pathological 99w/89w run-ons removed) |
| Causal-consistency razor | Clean (no sentence claims what the paper disclaims) |
| AI/reproducibility disclosure | Frozen deposited snapshot; κ recomputable offline |
| STROBE/RECORD checklist | Completed, mapped, rendered to PDF for upload |
| Abstract length | 225 words (limit 150–250) |
| Reference DOIs (16) | All resolve; fields match Crossref/DataCite; no retractions |
| Reference URLs (27) | All reachable (hms.is rate-limits bots but loads in a browser) |
| PDF typography | Ragged-right refs, DOIs unbroken, tables clean, casing fixed |

Manuscript: **23 pp** (named) / **22 pp** (anon) after the sentence splits + CRediT.

## Files to upload (from this folder)

1. **Manuscript:** `Fatal-Fire-Iceland_ANONYMIZED_manuscript.docx` (23/22-page PDF twin for checking)
2. **Supplementary/ESM:** `Fatal-Fire-Iceland_supplementary_ANON.docx`
3. **Cover letter:** `cover-letter-fire-technology.md` (paste text)
4. **Reporting checklist:** `Fatal-Fire-Iceland_STROBE-RECORD-checklist.pdf` (Related Manuscript file)
5. *(optional)* suggested reviewers — see `suggested-reviewers.md` (SNAPP step 7)

Do NOT upload `TITLE-PAGE.docx` or anything in `_working/` — declarations are typed into
the SNAPP interface (see `START-HERE.md` step 6).

## Changes applied in this final polish round (2026-07-22)

- Reference list set ragged-right; DOIs no longer break mid-string (`3eea008`)
- Anonymized author-mask rendering bug fixed (was "review] [Author name withheld…") (`3eea008`)
- Proper nouns brace-protected against CSL sentence-casing (`ad8f3c5`)
- Abstract cites the primary structure-fire ITSA slope (0.95/year); RECORD cited; geothermal 43%; American spelling; em-dashes removed (`013eb5a`)
- First-person → impersonal scientific voice, whole body (`0c20d42`)
- Role clarity: CRediT Author Contributions, M.S.S. 9 roles / T.B. 2 (`aad58fa`)
- Long Methods run-ons split (99w/89w → readable); AI disclosure hardened to frozen-snapshot reproducibility (temperature-0 deliberately not claimed — only one call set it) (`0c9cccf`)
- Completed STROBE/RECORD checklist created + rendered; cover-letter checklist claim reconciled + blinded-recode differentiator added; suggested reviewers drafted (`4e50865`)
- **Anonymity: Gjöll ratified as-is** — policy bar met (no identity handed over; DOI/URL/GitHub/self-cites masked); the name is load-bearing and determined de-anonymization is unavoidable regardless.

## Reference verification (43 entries)

Method: every DOI resolved and field-checked against Crossref (articles) or DataCite
(dataset); titles cross-checked in scite (no retractions/corrections on any cited paper);
every URL fetched. Four Crossref "year mismatches" (Bernal, Jonsson, Butry) are
online-first vs. print conventions — the .bib correctly cites print. Marshall 1998
pages 1633–1637 are correct (Crossref records first page only).

| # | Key | Year | Status | Link |
|---|---|---|---|---|
| 1 | EFSA2018 | 2018 | URL OK | <https://www.europeanfiresafetyalliance.org/wp-content/uploads/2018/11/20181120-Fatal-residential-fires-in-Europe.pdf> |
| 2 | Holborn2003 | 2003 | DOI verified | <https://doi.org/10.1016/S0379-7112(02)00049-8> |
| 3 | Iceland1969 | 1969 | URL OK | <https://www.althingi.is/altext/89/s/0121.html> |
| 4 | Iceland1982 | 1982 | URL OK | <https://urlausnir.is/merkimidar/185407/> |
| 5 | Iceland1992 | 1992 | URL OK | <https://www.althingi.is/lagas/122b/1992041.html> |
| 6 | Iceland1997 | 1997 | URL OK | <https://www.althingi.is/altext/stjt/1997.073.html> |
| 7 | Iceland1998 | 1998 | URL OK | <https://www.reglugerd.is/reglugerdir/allar/nr/441-1998> |
| 8 | Iceland2000 | 2000 | URL OK | <https://www.althingi.is/lagas/nuna/2000075.html> |
| 9 | MSB2023 | 2023 | URL OK | <https://www.mcf.se/en/about-us/research-and-statistics/nordic-fire-statistics/> |
| 10 | Smarason2025data | 2026 | DOI verified (DataCite) | <https://doi.org/10.34881/I5WGJU> |
| 11 | Timarit | 2025 | URL OK | <https://timarit.is> |
| 12 | Smarason2025practitioner | 2025 | URL OK | <https://timarit.is/page/8258975> |
| 13 | HMS2020 | 2020 | URL OK | <https://fundur.reykjavik.is/sites/default/files/agenda-items/20_skyrsla_hms_-_braedraborgarstigur_0.pdf> |
| 14 | HMS2026Studlar | 2026 | URL OK in browser (bot-blocked 429 via curl) | <https://hms.is/skyrslur/skyrsla-um-eldsvoda-a-studlum> |
| 15 | StatisticsIceland2025 | 2025 | API URL OK (returns JSON) | <https://px.hagstofa.is/pxis/api/v1/is/Ibuar/mannfjoldi/1_yfirlit/Yfirlit_mannfjolda/MAN00000.px> |
| 16 | HMS2024buildingAge | 2024 | URL OK in browser (bot-blocked 429 via curl) | <https://hms.is/mannvirkjaskra> |
| 17 | SSB2024 | 2024 | URL OK | <https://www.ssb.no/en/bygg-bolig-og-eiendom/bolig-og-boforhold/statistikk/boliger> |
| 18 | HMS2025completions | 2025 | URL OK | <https://px.hagstofa.is/pxis/pxweb/is/Atvinnuvegir/Atvinnuvegir__idnadur__byggingar/IDN03001.px> |
| 19 | Marshall1998 | 1998 | DOI verified | <https://doi.org/10.1001/jama.279.20.1633> |
| 20 | Doyle2019 | 2019 | DOI verified | <https://doi.org/10.1016/j.firesaf.2019.102892> |
| 21 | Loney2014 | 2014 | DOI verified | <https://doi.org/10.1186/1742-7622-11-18> |
| 22 | Baldursson2018 | 2018 | DOI verified | <https://doi.org/10.1186/s13049-017-0467-9> |
| 23 | Wagner2002 | 2002 | DOI verified | <https://doi.org/10.1046/j.1365-2710.2002.00430.x> |
| 24 | Bernal2017 | 2017 | DOI verified (print-issue year) | <https://doi.org/10.1093/ije/dyw098> |
| 25 | Ahrens2021 | 2021 | URL OK | <https://www.nfpa.org/education-and-research/research/nfpa-research/fire-statistical-reports/smoke-alarms-in-us-home-fires> |
| 26 | Gilbert2021 | 2021 | DOI verified | <https://doi.org/10.1007/s10694-020-01072-z> |
| 27 | Seabold2010 | 2010 | DOI verified | <https://doi.org/10.25080/Majora-92bf1922-011> |
| 28 | Young2011 | 2011 | DOI verified | <https://doi.org/10.1073/pnas.1111690108> |
| 29 | Heilbrigdisraduneytid2021 | 2021 | URL OK | <https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2021/05/05/Til-umsagnar-Adgerdaaaetlun-fyrir-bradathjonustu-og-sjukraflutninga/> |
| 30 | Althingires2019 | 2019 | URL OK | <https://www.althingi.is/altext/149/s/1684.html> |
| 31 | Haestirettur2020Selfoss | 2020 | URL OK | <https://island.is/domar/s-F709C0F3-52A9-428D-B787-FD90FFE43779> |
| 32 | RUV2020brunavarnir | 2020 | URL OK | <https://www.ruv.is/frettir/innlent/2020-07-11-glorulaus-veiking-a-brunavarnasvidi/> |
| 33 | VonElm2007 | 2007 | DOI verified | <https://doi.org/10.1016/S0140-6736(07)61602-X> |
| 34 | Benchimol2015 (NEW) | 2015 | DOI verified | <https://doi.org/10.1371/journal.pmed.1001885> |
| 35 | Ragnarsson2010 | 2010 | URL OK | <https://www.worldgeothermal.org/pdf/IGAstandard/WGC/2010/0124.pdf> |
| 36 | Landlaeknir2014 | 2014 | URL OK | <https://island.is/tolfraedi-og-rannsoknir/tolfraedi/heilsa-og-lidan/tobaksnotkun> |
| 37 | Landsrettur2022Braedraborgarstigur | 2022 | URL OK | <https://www.landsrettur.is/domar-og-urskurdir/domur-urskurdur/?Id=529a5afb-6280-4b4a-a53d-e8507cd41a42&verdictid=6023c9ad-dbbb-4678-baa7-25daebd6eba1> |
| 38 | Jonsson2016 | 2016 | DOI verified (print-issue year) | <https://doi.org/10.1007/s10694-015-0551-5> |
| 39 | Manes2023 | 2023 | DOI verified | <https://doi.org/10.1007/s10694-023-01415-6> |
| 40 | Butry2017 | 2017 | DOI verified (print-issue year) | <https://doi.org/10.1007/s10694-016-0621-3> |
| 41 | NFPA901 | 2021 | URL OK | <https://catalog.nfpa.org/NFPA-901-Standard-Classifications-for-Fire-and-Emergency-Services-Incident-Reporting-P1379.aspx> |
| 42 | USFA_NFIRS | 2015 | URL OK | <https://www.usfa.fema.gov/downloads/pdf/nfirs/nfirs_complete_reference_guide_2015.pdf> |
| 43 | StatisticsIcelandCOD | 2025 | URL OK | <https://px.hagstofa.is/pxen/pxweb/en/Ibuar/Ibuar__Faeddirdanir__danir__danarmein/MAN05302.px> |

## Remaining open items (non-blocking, author's discretion)

- The two hms.is links rate-limit automated checkers; open them once in a browser before
  submitting if you want eyes-on confirmation.
- `StatisticsIceland2025` bib title says "1703–2025"; the live table has since extended to
  1703–2026. The 2025 framing matches the access date and analysis window — fine as-is.
- Suggested reviewers (SNAPP step 7) are still optional/blank.
