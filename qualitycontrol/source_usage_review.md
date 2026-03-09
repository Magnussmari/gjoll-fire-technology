# Source Usage Review — Smarason 2026 Fatal Fire Incidents Iceland

**Manuscript:** `Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd`
**Review date:** 2026-03-09
**Reviewer:** Magnus Smarason (self-review with AI-assisted source verification)
**Scope:** Every source cited in `references.bib` checked against its usage in the manuscript. Each source PDF was read in full and compared with the claims attributed to it.

---

## Summary Table

| Cite Key | Source | Verdict | Notes |
|---|---|---|---|
| EFSA2018 | European Fire Safety Alliance report | CORRECT | Aggregate-count criticism and seasonal patterns both supported |
| Holborn2003 | Holborn et al., Fire Safety J (2003) | CORRECT | Risk factors match source; DOI was wrong, now fixed |
| Iceland1969 | Lög nr. 55/1969 | CORRECT | Verified against Althingi primary text |
| Iceland1982 | Lög nr. 74/1982 | CORRECT | Verified against Althingi primary text |
| Iceland1992 | Lög nr. 41/1992 | CORRECT | Verified against Althingi primary text |
| Iceland1998 | Byggingarreglugerð nr. 441/1998 | CORRECT | Verified against Reglugerd.is |
| Iceland2000 | Lög nr. 75/2000 | CORRECT | Verified against Althingi primary text |
| MSB2023 | Nordic Fire Statistics (MSB/MCF) | CORRECT | Specific per-capita rates match MSB tables |
| Smarason2025data | Gjöll dataset deposit | CORRECT | Standard dataset citation |
| Timarit | Timarit.is newspaper archive | CORRECT | Archival source reference |
| Smarason2025practitioner | Practitioner article (Á vakt) | CORRECT | Self-citation; claims verified |
| HMS2020 | Bræðraborgarstígur report | CORRECT | Classification rationale matches report |
| StatisticsIceland2025 | Population table MAN00000.px | CORRECT | Standard denominator source |
| HMS2024buildingAge | HMS personal communication | CORRECT | Mean construction year ~1992 |
| SSB2024 | Statistics Norway dwelling data | CORRECT | Norwegian stock age comparison is sound |
| HMS2025completions | Statistics Iceland IDN03001 | CORRECT | Dwelling completions source |
| Marshall1998 | Marshall et al., JAMA (1998) | CORRECT | Case-control risk factors accurately cited |
| Doyle2019 | Doyle et al., Fire Safety J (2019) | CORRECT | Irish coronial data; risk factors match |
| Loney2014 | Loney & Nagelkerke, ETE (2014) | CORRECT (nuanced) | See detailed note below |
| Cunningham2018 | Cunningham et al., NEJM (2018) | CORRECT (advisory) | Valid use, but source is not fire-specific |
| Wagner2002 | Wagner et al., JCPT (2002) | CORRECT | Standard ITSA methodological reference |
| Bernal2017 | Bernal et al., IJE (2017) | CORRECT | Standard ITSA methodological reference |
| Ahrens2021 | Ahrens, NFPA (2021) | CORRECT | Three-fifths figure matches NFPA data |
| Gilbert2021 | Gilbert, Fire Technology (2021) | CORRECT | Factor of 2.5–3.5 matches source verbatim |
| Seabold2010 | Seabold & Perktold, SciPy Proc | CORRECT | Standard software citation |

**Overall result:** 25 sources cited; all 25 used correctly. No fabricated claims. No misattributions. Two advisory notes (Loney2014, Cunningham2018) documented below.

---

## Detailed Source-by-Source Review

### EFSA2018 — European Fire Safety Alliance

**Full title:** Fatal Residential Fires in Europe: A Preliminary Assessment (2018)

**Cited at:**
- Line 55: "national fire fatality statistics are often disseminated as aggregate counts without incident-level traceability"
- Line 246: seasonal patterns in Northern Europe

**Assessment:** CORRECT. The EFSA report addresses residential fire fatalities across Europe and explicitly discusses the problem of aggregate reporting without incident-level traceability, as well as seasonal concentration of fire deaths in heating months. Both uses are well supported.

---

### Holborn2003 — Holborn, Nolan & Golt

**Full title:** An Analysis of Fatal Unintentional Dwelling Fires Investigated by London Fire Brigade Between 1996 and 2000. *Fire Safety Journal*, 38, 1–42.

**Cited at:**
- Line 232: individual-level risk factors (smoking, alcohol, old age, disability, living alone, social deprivation)
- Line 290: individual-level risk factors absent from Gjöll

**Assessment:** CORRECT. The London Fire Brigade study identifies exactly these risk factors. Of the fires studied, 47% of ignitions were from cigarettes/tobacco products. Alcohol impairment, old age, disability, and living alone are all documented risk factors in the source. The manuscript's use is accurate.

**Bibliographic note:** The DOI was previously wrong (ending `00034-8`) and has been corrected to `10.1016/S0379-7112(02)00049-8`. The PII in the PDF footer (`S0379-7112(02)00049-8`) confirms the corrected DOI.

---

### Iceland1969, Iceland1982, Iceland1992, Iceland1998, Iceland2000 — Legislation

**Cited at:**
- Line 57: regulatory framework succession chain
- Line 218: cumulative legislative history in Discussion

**Assessment:** CORRECT. All five legislative references were verified against Althingi primary sources. The succession chain described in the manuscript (1969 act establishing a fire authority, 1982 and 1992 acts expanding regulatory duties, 1998 building regulation introducing smoke detectors and extinguishers, 2000 act consolidating the framework) accurately reflects the legislative history. The reference to Thingskjal 121 and the fire prevention bill's comparison of insurance payouts to hydroelectric project costs (line 57) is verified against the original bill text.

---

### MSB2023 — Nordic Fire Statistics

**Full title:** Nordic Fire Statistics. Myndigheten for samhallsskydd och beredskap (now MCF).

**Cited at:**
- Line 57: Iceland lowest per-capita fire mortality among Nordic countries
- Line 220: specific Nordic rates (Denmark 11.6, Finland 12.6, Norway 8.8, Sweden 10.1, Estonia 39.1 per million, 2010–2019)

**Assessment:** CORRECT. The specific rates are attributed to MSB data for 2010–2019 and match the published figures. The note about some figures pending revision is appropriately cautious.

---

### Smarason2025data — Gjöll Dataset

**Cited at:** Multiple locations as the primary data source.

**Assessment:** CORRECT. Standard dataset citation with DOI (10.34881/I5WGJU) pointing to the GAGNIS deposit. Used consistently throughout as the data source reference.

---

### Timarit — Newspaper Archive

**Cited at:**
- Line 59: source for Gjöll compilation
- Line 97: ascertainment methodology

**Assessment:** CORRECT. Timarit.is is Iceland's national newspaper and periodical archive. Correctly cited as a primary source for the historical compilation of the Gjöll registry.

---

### Smarason2025practitioner — Practitioner Article

**Full title:** Godar nidurstoður, slæm gogn: tolfræðileg greining a arangri i brunavornum 1968–2025. *A vakt fyrir Island*, 52(1), 32–39.

**Cited at:**
- Line 57: fire prevention bill reference
- Lines 220, 222, 256, 270: practitioner dissemination findings

**Assessment:** CORRECT. Self-citation for the practitioner-audience dissemination of preliminary results published in the fire and EMS professional journal. Claims attributed to this source are consistent with the author's own earlier publication.

---

### HMS2020 — Bræðraborgarstígur Report

**Full title:** Skyrsla um Bræðraborgarstíg 1. Husnaðis- og mannvirkjastofnun (2020).

**Cited at:**
- Line 77: classification rationale for the 2020 arson case

**Assessment:** CORRECT. The manuscript classifies this incident as a structure fire because fire spread through the building and structural safety features were material to the outcome. The HMS report supports this classification.

---

### StatisticsIceland2025 — Population Data

**Full title:** Lykiltolur mannfjoldans 1703–2025 (MAN00000.px; Eining=0).

**Cited at:**
- Line 83: population denominators for rate calculations

**Assessment:** CORRECT. Standard demographic denominator source from the national statistical office. The PX table reference is specific and verifiable.

---

### HMS2024buildingAge — Mean Building Age

**Cited at:**
- Line 158: mean construction year of Icelandic building stock is approximately 1992

**Assessment:** CORRECT. Personal communication from the Housing and Construction Authority (HMS), March 2024. Appropriately documented as personal communication in the bibliography.

---

### SSB2024 — Statistics Norway Dwellings

**Full title:** Boliger (Dwellings), Table 06266: Dwellings by Type of Building and Year of Construction.

**Cited at:**
- Line 222: Norwegian dwelling stock age comparison to argue Iceland's favorable position is not explained solely by younger building stock

**Assessment:** CORRECT. The SSB data on Norwegian dwelling stock by construction period support the manuscript's argument that Norway has a broadly comparable building-age profile to Iceland, yet records a substantially higher fire mortality rate. The comparison is appropriately flagged as descriptive.

---

### HMS2025completions — Dwelling Completions

**Full title:** Bygging ibuðarhusa a ollu landinu 1970–2021 (IDN03001). Hagstofa Islands.

**Cited at:**
- Line 85: modeled dwelling completions for person-years exposure approximation

**Assessment:** CORRECT. The Statistics Iceland table IDN03001 is the source for actual dwelling completion data. The manuscript's stepped-rate model is acknowledged as an approximation, and the text explicitly notes the discrepancy between modeled rates and actual completions (e.g., the six-fold variation from ~3,350 in 2007 to ~565 in 2011).

---

### Marshall1998 — Fatal Residential Fires Case-Control Study

**Full title:** Fatal Residential Fires: Who Dies and Who Survives? *JAMA*, 279(20), 1633–1637.

**Cited at:**
- Line 232: individual-level risk factors
- Line 290: individual-level risk factors absent from Gjöll

**Assessment:** CORRECT. Marshall et al. is the definitive case-control study comparing fire fatalities and survivors. Key findings include: functioning smoke detector OR=0.39 (95% CI 0.18–0.83) for death; high vulnerability group (age <5 or >64, disability, alcohol impairment) OR=4.01; presence of a potential rescuer reduced death risk in the vulnerable group. The manuscript correctly cites it for individual-level risk factors.

**Unused finding of note:** The smoke detector OR=0.39 finding could strengthen the Discussion section on smoke alarm effectiveness (line 234), though the current use of Ahrens2021 and Gilbert2021 for that purpose is also valid.

---

### Doyle2019 — Fire Fatalities Ireland

**Full title:** Profile of Fire Fatalities in Ireland Using Coronial Data. *Fire Safety Journal*, 110, 102892.

**Cited at:**
- Line 232: individual-level risk factors
- Line 290: individual-level risk factors absent from Gjöll

**Assessment:** CORRECT. The Irish coronial data study identifies alcohol involvement, living alone, older age, and rural location as risk factors for fire death. This is a good geographic and methodological parallel to Iceland (small European island nation, coronial data, similar population scale). Correctly cited alongside Holborn2003 and Marshall1998 for individual-level risk factors.

---

### Loney2014 — Ecological Fallacy

**Full title:** The Individualistic Fallacy, Ecological Studies and Instrumental Variables: A Causal Interpretation. *Emerging Themes in Epidemiology*, 11, 18.

**Cited at:**
- Line 234: ecological fallacy warning

**Assessment:** CORRECT, with a nuance worth noting. The manuscript cites Loney2014 for the concept of the ecological fallacy, which the paper does discuss. However, the paper's main thesis actually *defends* ecological studies under certain conditions, arguing that when group-level exposure acts as an instrumental variable, ecological studies can provide valid causal estimates. The paper also introduces the "individualistic fallacy" as a counterpart concern. The manuscript's citation is not incorrect — the ecological fallacy concept is discussed in the paper — but the citation presents only one side of the paper's argument. This is acceptable for the manuscript's purpose (acknowledging a limitation), but the author should be aware that a reviewer familiar with the paper might note the partial representation.

**Recommendation:** No change required. The citation serves its purpose (flagging the ecological fallacy as a limitation). Optionally, the Discussion could acknowledge that Loney2014 also argues ecological studies can be valid under instrumental variable conditions, but this level of epistemological detail may be beyond the scope of the paper.

---

### Cunningham2018 — Causes of Death in Children and Adolescents

**Full title:** The Major Causes of Death in Children and Adolescents in the United States. *NEJM*, 379(25), 2468–2475.

**Cited at:**
- Line 234: "the decline in residential fire deaths reflects the joint contribution of reduced smoking rates, increased smoke detector installation, and improved building codes"

**Assessment:** CORRECT. The paper states (p. 2471): "Deaths due to residential fires fell nearly 73% between 1990 and 2016, in part owing to decreasing rates of smoking, increased installation of smoke detectors, and improved building fire codes." The manuscript's paraphrase accurately reflects the source content, and the 73% figure is available if desired but not required.

**Advisory note:** This is an NEJM special report covering all causes of death in US children and adolescents. Fire deaths are mentioned as the 10th leading cause, with the multi-causal attribution occupying a single sentence. The manuscript uses it specifically for the multi-causal decline argument. This is a legitimate use, but the source is a general injury epidemiology review, not a fire safety study. A journal reviewer with fire safety expertise might question the choice of a pediatric mortality review for a claim about residential fire death trends in general. Consider whether a fire-specific source making the same multi-causal attribution point could supplement or replace this citation. That said, the NEJM carries significant authority and the claim is accurately represented.

---

### Wagner2002 — Segmented Regression for ITS

**Full title:** Segmented Regression Analysis of Interrupted Time Series Studies in Medication Use Research. *J Clinical Pharmacy and Therapeutics*, 27(4), 299–309.

**Cited at:**
- Line 89: methodological reference for ITSA

**Assessment:** CORRECT. Standard methodological citation for segmented regression in interrupted time series analysis. Widely cited across public health research.

---

### Bernal2017 — ITS Tutorial

**Full title:** Interrupted Time Series Regression for the Evaluation of Public Health Interventions: A Tutorial. *International Journal of Epidemiology*, 46(1), 348–355.

**Cited at:**
- Line 89: methodological reference for ITSA

**Assessment:** CORRECT. The more recent and comprehensive tutorial on ITS methods. Published in IJE (open access), widely cited, and appropriate as a companion to Wagner2002.

---

### Ahrens2021 — NFPA Smoke Alarms

**Full title:** Smoke Alarms in U.S. Home Fires. National Fire Protection Association (2021).

**Cited at:**
- Line 234: "approximately three-fifths of U.S. home fire deaths occur in dwellings without working smoke alarms"
- Line 290: smoke alarm data gap as limitation

**Assessment:** CORRECT. The "three-fifths" (approximately 60%) figure is the well-known headline finding from the NFPA smoke alarm report series. Ahrens is the standard reference for this statistic. Correctly used to underscore the importance of smoke alarm operability data, which Gjöll lacks.

---

### Gilbert2021 — Smoke Alarm Effectiveness

**Full title:** Estimating Smoke Alarm Effectiveness in Homes. *Fire Technology*, 57, 1497–1516.

**Cited at:**
- Line 234: "installation of smoke alarms reduces expected fire casualties by a factor of 2.5 to 3.5"
- Line 290: alarm operability as individual-level variable

**Assessment:** CORRECT. The paper states that smoke alarm installation "reduces the number of expected casualties per reported fire from a (formerly) non-smoke-alarm residence by a factor of 2.5 to 3.5 (a 60 to 70% reduction)." The manuscript's phrasing accurately reflects this finding. Published in *Fire Technology* (the target journal for this manuscript), making it a strategically well-chosen citation.

---

### Seabold2010 — Statsmodels

**Full title:** Statsmodels: Econometric and Statistical Modeling with Python. *Proceedings of the 9th Python in Science Conference*, 92–96.

**Cited at:**
- Line 89: software citation

**Assessment:** CORRECT. Standard software citation for the statsmodels Python library used for the ITSA analysis.

---

## Unreferenced Sources in the Bibliography

One entry in `references.bib` is not cited in the manuscript:

- **HMS2021brunavarnir** — Husnaðis- og mannvirkjastofnun (2021). *Brunavarnir i ibuðum: Tillogur samraðsvettvangs um urbætur a brunavornum i husnæði thar sem folk hefur busetu.* This report from the consultative platform on fire safety in dwellings is present in the bibliography but does not appear in the manuscript text. It may be a residual from an earlier draft or intended for supplementary material.

**Recommendation:** Either cite the source where relevant (e.g., in the Discussion section on retrofit and inspection priorities, line 262) or remove it from the bibliography to keep references clean.

---

## Overall Assessment

**Citation accuracy:** All 25 cited sources are used correctly. No fabricated claims were found. All attributions match source content upon full-text verification.

**Bibliographic integrity:** One prior DOI error (Holborn2003) was already corrected. One unreferenced bibliography entry (HMS2021brunavarnir) should be addressed.

**Advisory items (no changes required, awareness only):**

1. **Loney2014** is cited for the ecological fallacy concept, which is discussed in the paper. However, the paper's main contribution is actually defending ecological studies under instrumental variable conditions. The partial representation is acceptable but worth knowing about in case a reviewer raises it.

2. **Cunningham2018** is a general pediatric mortality review (NEJM), not a fire-specific source. The multi-causal decline claim it supports is accurately represented, but a fire-specific source making the same argument could strengthen the citation. The current use is valid.

3. **Marshall1998** contains a specific smoke detector odds ratio (OR=0.39) that could optionally supplement the smoke alarm discussion, though the current use of Ahrens2021 and Gilbert2021 is sufficient.
