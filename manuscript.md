# Fatal Fire Incidents in Iceland, 1968–2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation

## Title Page

**Title:** Fatal Fire Incidents in Iceland, 1968–2025: Long-Run Trends, Building Age, and the Effectiveness of Fire Safety Regulation

**Authors:** Magnús Smári Smárason¹ (ORCID: 0009-0008-2050-021X)

**Affiliations:**
¹ Independent Researcher (affiliated with Háskólinn á Akureyri / University of Akureyri), Iceland

**Correspondence:** Magnús Smári Smárason, magnus@smarason.is; https://www.gjoll.is

---

## Abstract

Fire-related fatalities are rare events that require long observation windows for meaningful trend analysis. This study presents a 58-year national dataset of all fatal fire incidents in Iceland (1968–2025), compiled through systematic historical source review with cross-verification across independent sources. The Gjöll incident registry contains 113 fatal incidents resulting in 145 deaths. Structure fires account for 93 incidents (116 deaths, 80%), while other fire-related incidents (maritime, vehicle) account for 20 incidents (29 deaths, 20%). Fatal incidents cluster in the October–March heating season (58% of incidents and deaths). Decade-aggregated mortality peaked in the 1970s (21.9 deaths per million population per year) and declined substantially to approximately 4–7 deaths per million from the 1990s onward. Construction year is missing for 52% of structure-fire incidents overall but is complete from 1996 onward (0% missing); in this complete subset, no fatal incidents occurred in buildings constructed after 1998—the year Iceland adopted modern prescriptive fire safety requirements including mandatory smoke detectors and portable extinguishers in all dwellings. A sensitivity analysis confirms that all missing construction-year records predate 1996, making it logically impossible for any to represent post-1998 buildings. A person-years exposure approximation yields a fatality rate of 0.57 per 100,000 person-years in pre-1998 dwellings versus 0.00 in post-1998 dwellings over approximately 2.08 million person-years of exposure. Interrupted time series analysis using segmented Poisson regression identifies a significant pre-existing declining trend (IRR = 0.93 per year, *p* < 0.001) and a significant level decrease at the 1999 regulatory intervention (IRR = 0.11, *p* = 0.010). These findings are consistent with—though cannot conclusively demonstrate—the cumulative effectiveness of Iceland's fire safety regulatory framework. The small absolute number of events, confounding by correlated technological and sociodemographic changes, and reliance on modeled rather than census-derived denominators limit causal interpretation. Persistent seasonal risk and emerging challenges including unauthorized residential use of commercial buildings and arson targeting vulnerable populations are also documented.

**Keywords:** fire fatalities; fire safety regulation; building codes; building age; fire statistics; Iceland; Nordic countries; fire prevention

---

## 1 Introduction

Effective fire safety regulation depends on reliable, long-term data to evaluate outcomes and direct prevention resources. However, national fire fatality statistics are often disseminated as aggregate counts without incident-level traceability, limiting their value for trend analysis and policy evaluation [1, 2]. This is particularly true for small nations where annual counts are low and year-to-year variation is large.

Iceland provides a useful case for studying the long-run effectiveness of fire safety regulation. Its small population (approximately 200,000 in 1968, growing to 388,000 by 2025) enables national-scale compilation of incident-level data, while its well-documented regulatory history allows trends to be interpreted against known policy changes. Iceland's fire safety framework has evolved through several major legislative milestones: the establishment of a national fire authority (Brunamálastofnun) under Act No. 55/1969, comprehensive fire prevention legislation (Act No. 74/1982), an updated building regulation in 1992 (nr. 441/1992), a substantially revised building regulation (Byggingarreglugerð nr. 441/1998) that introduced mandatory smoke detectors and portable extinguishers in all dwellings, and the current fire prevention act (Act No. 75/2000) [3–6]. The scale of the original challenge is illustrated by the 1968 fire prevention bill (Þingskjal 121), which noted that insurance payouts for fire damages during 1960–1967 equalled the cost of a major hydroelectric project, and that per-capita fire losses were two to three times higher than in neighbouring countries [3, 10].

In a Nordic context, published fire-death counts from the MSB Nordic Fire Statistics collaboration indicate that Iceland typically records the lowest per-capita fire mortality among the Nordic countries, though year-to-year variation remains substantial and some figures are noted as pending revision [7]. Cross-country comparisons should be interpreted cautiously due to differences in definitions, follow-up practice, and ongoing harmonization.

The Gjöll project was initiated to address the lack of a consolidated, incident-level dataset for fatal fires in Iceland. The resulting registry, compiled through systematic review of archival newspapers (notably the timarit.is digital collection), yearbooks, and official reports, covers the period 1968–2025 with source references for each record [8, 9]. All 113 incidents were verified against at least two independent sources. The registry and its preliminary descriptive results have also been disseminated to practitioner audiences (fire and EMS) in Iceland [10].

This study uses the Gjöll registry export to describe (i) long-run trends in fatal fire incidents and deaths, (ii) seasonal patterning, and (iii) the distribution of fatal structure fires by building construction year, with particular attention to the role of building age and regulatory change in fire fatality outcomes.

## 2 Data and Methods

### 2.1 Data Source

We used two exported tables (CSV) from the Gjöll incident registry: fatal structure fires (*n* = 93 incidents) and other fatal fire-related incidents (*n* = 20 incidents). The export metadata indicates a 2025-09-15 export date [8]. The unit of analysis is the fatal incident. All fatal fire incidents in the export for 1968–2025 were included; no sampling was performed.

### 2.2 Variables

Each incident record includes incident date, calendar year, and number of deaths. Structure-fire records additionally include municipality, address/postal code (when available), and building construction year (missing for 48 of 93 structure-fire incidents). Other fatal fire-related incidents include a coarse subtype (e.g., ship fire or vehicle fire).

### 2.3 Incident Classification

Incidents were classified into two categories: fatal fires in structures (93 incidents, 116 deaths) and other fire-related deaths involving ships, vehicles, and other non-building settings (20 incidents, 29 deaths). Classification was based on whether building fire safety features were relevant to the incident outcome.

Borderline cases required judgment. For example, a 2014 nursing home fire (building constructed 2001) where an elderly resident died was classified as "other" because the building's fire safety systems were not implicated in the fatality mechanism. Conversely, a criminal arson incident at Bræðraborgarstígur, Reykjavík, in 2020 (original construction year 1906, 3 deaths) was classified as a structure fire because building safety features were material to the outcome [11].

### 2.4 Analysis

Descriptive summaries were computed for incident severity (deaths per incident), decade totals (incidents and deaths), seasonal patterns by calendar month and by heating season (October–March) versus non-heating season (April–September), and construction-year bands for fatal structure fires.

For population-adjusted rates, annual population on 1 January was obtained from Statistics Iceland (PX table MAN00000.px, Eining = 0) for 1968–2025 [12]. For each period bin, "mean population" is the mean of annual 1 January population counts across years in that bin. Crude annualized deaths per million population are reported by decade for Nordic comparability. To illustrate rare-event uncertainty for short observation windows, exact Poisson 95% confidence intervals are reported for selected rates.

**Person-years exposure approximation.** To address the absence of a census-based housing-stock denominator stratified by construction period, we approximated person-years of exposure in pre-1998 versus post-1998 dwellings for the 1999–2025 period. Annual dwelling completions were modeled using stepped rates consistent with Iceland's construction history and the documented mean building-stock construction year of approximately 1992 [13, 15]: 500/year prior to 1940, 2,000/year 1940–1979, 2,500/year 1980–1997, 3,000/year 1998–2009, and 3,500/year 2010–2025. Population was allocated to building-age strata proportionally to the modeled stock fraction. These are order-of-magnitude approximations, not census-derived denominators.

**Sensitivity analysis for missing construction year.** Construction year is missing for 48 of 93 structure-fire incidents (52%). We examined the temporal distribution of incidents with missing construction year to assess whether missingness could affect the post-1998 finding.

**Interrupted time series analysis (ITSA).** To move beyond purely descriptive assessment, we fitted segmented regression models to annual fire death counts (structure and other combined) using generalized linear models with a Poisson distribution and log-link, with the natural logarithm of the annual population as an offset [20, 21]. The primary model specified an intervention at 1999 (the effective year of Byggingarreglugerð nr. 441/1998) with three terms: secular trend (*time*), level change (*post1999*), and slope change (*time_post1999*). A secondary model added an intervention at 1982 (Brunavarnalög nr. 74/1982). Overdispersion was assessed by the Pearson chi-squared dispersion ratio; a negative binomial model was fitted as a robustness check. Model comparison used Akaike's Information Criterion (AIC). Incidence rate ratios (IRR) with 95% confidence intervals are reported. Analyses were performed in Python 3 using statsmodels [22].

This study follows the STROBE guidelines for cross-sectional studies; a completed checklist is provided as supplementary material.

**Reproducibility:** The analyzed tables, scripts, and generated outputs are available in the accompanying repository [8]. The package regenerates all tables, figures, and supplementary analyses from the exported data.

### 2.5 Ascertainment and Completeness

The registry was compiled through systematic historical source review with cross-verification across independent sources where available [8, 9]. We did not perform a formal validation against national cause-of-death registers and cannot quantify completeness of ascertainment. Under-ascertainment is plausible, particularly in earlier decades.

## 3 Results

### 3.1 Overall Burden and Incident Severity

Across 1968–2025 (58 calendar years), the export contains 113 fatal incidents resulting in 145 deaths (mean: 1.28 deaths per incident). Most incidents involve a single fatality (93/113, 82%) (Table 1).

### 3.2 Long-Run Trends

Decade aggregation shows the highest burden in the 1970s (35 incidents, 47 deaths), followed by a sustained lower level from the 1990s onward (Table 2; Fig. 1). Using Statistics Iceland denominators, crude annualized deaths per million population peak in the 1970s (21.9) and fall substantially to the range of 4–7 from the 1990s onward. Within the study period, eight calendar years record zero deaths (1984, 1987, 1992, 2000, 2003, 2007, 2011, 2015).

The apparent uptick in 2020–2025 reflects a six-year observation window and rare-event variability. An exact Poisson 95% confidence interval for the 2020–2025 crude annualized rate is approximately 3.8–11.1 deaths per million population per year, overlapping a corresponding interval for the 2010s (approximately 2.6–7.6).

### 3.3 Building Age and Fatal Structure Fires

Construction year is recorded for 45 of 93 structure-fire incidents (48%). Missingness is concentrated in earlier decades; among structure-fire incidents from 1996 onward, construction year is complete (0 missing). Among incidents with known construction year, no fatal structure-fire incidents occurred in buildings constructed after 1998 (Table 3; Fig. 3). In the 1996–2025 subset where construction year is complete, the mean construction year of buildings involved in fatal structure fires is 1957, whereas the mean construction year of the Icelandic building stock overall is 1992, according to data from the Housing and Construction Authority (Húsnæðis- og mannvirkjastofnun) [13].

### 3.4 Person-Years Exposure and Construction-Period Fatality Rates

Using the modeled dwelling-stock approximation (Section 2.4), the 1999–2025 period yields approximately 6.64 million person-years in pre-1998 dwellings and 2.08 million person-years in post-1998 dwellings. During this period, 38 structure-fire deaths occurred in pre-1998 buildings (among incidents with known construction year), yielding an approximate fatality rate of 0.57 per 100,000 person-years. Zero deaths occurred in post-1998 buildings (rate: 0.00 per 100,000 person-years; rate ratio = 0). While the dwelling-stock model is approximate, the zero numerator for post-1998 buildings is robust to any reasonable adjustment of the denominator.

### 3.5 Sensitivity Analysis: Missing Construction Year

All 48 incidents with missing construction year occurred between 1970 and 1995. Because a building that burned before 1999 cannot have been constructed after 1998, the missing data are logically irrelevant to the post-1998 finding: regardless of how missing values are imputed, the observed zero in post-1998 buildings is unaffected. The missingness is missing-not-at-random but in a direction that strengthens rather than undermines the key finding.

### 3.6 Interrupted Time Series Analysis

The Poisson ITSA model (AIC = 216.3; Pearson dispersion ratio = 1.15, indicating no major overdispersion) reveals a significant pre-1999 declining trend in fire mortality (IRR per year = 0.932, 95% CI 0.910–0.955, *p* < 0.001), a significant level decrease at the 1999 intervention (IRR = 0.106, 95% CI 0.019–0.586, *p* = 0.010), and a significant positive slope change post-1999 (IRR per year = 1.084, 95% CI 1.037–1.132, *p* < 0.001). The positive post-1999 slope change reflects a partial attenuation of the pre-1999 decline—not an increase in the absolute rate, which remains at historically low levels. A negative binomial robustness check yielded similar point estimates but wider confidence intervals, with the level change no longer significant (*p* = 0.12), consistent with the low statistical power inherent in rare-event data. A two-intervention model adding a 1982 breakpoint showed no improvement over the single-intervention model (ΔAIC = +3.4), suggesting that the 1999 regulation is the more parsimonious breakpoint for the observed mortality reduction. Figure 4 presents the ITSA model fit with observed counts, fitted values, and the counterfactual trajectory.

### 3.7 Seasonality

Fatal incidents occur year-round but concentrate in the heating season. October–March accounts for 66 of 113 fatal incidents (58%) and 84 of 145 deaths (58%) (Fig. 2).

### 3.8 Non-Structure Fatal Incidents

Non-structure incidents contribute 29 deaths across 20 incidents. Maritime incidents are prominent: ship fires account for 15 deaths across seven incidents, and vehicle fires account for three deaths across three incidents.

## 4 Discussion

### 4.1 Long-Run Effectiveness of Fire Safety Regulation

The Gjöll dataset documents a clear and sustained decline in fatal fire incidence in Iceland since the 1970s. This decline aligns with the cumulative introduction of fire safety legislation and building regulation over the study period: the 1969 fire authority act, the 1982 fire prevention act, the 1998 building regulation introducing residential smoke detectors and extinguishers, and the 2000 fire prevention act [3–6].

In population-adjusted terms, Iceland's crude annualized mortality rate in the 1990s–2010s is approximately 4–6 deaths per million population per year. For Nordic context, MSB reports mean rates for 2010–2019 of approximately 11.6 (Denmark), 12.6 (Finland), 8.8 (Norway), and 10.1 (Sweden), while Estonia is substantially higher at 39.1 [7]. Extending the window to 2010–2021, the practitioner dissemination reports a rate of approximately 5.5 deaths per million for Iceland [10], still the lowest in the Nordic comparison. MSB data extending to 2024 do not yet include Iceland pending revision, but the practitioner-derived rate is consistent with Iceland's sustained low position. Cross-country differences in definitions and follow-up practice warrant caution.

Notably, Iceland's favourable position is unlikely to be explained solely by a younger building stock. Statistics Norway data indicate that the majority of Norwegian dwellings predate 1980, implying a mean building age broadly comparable to Iceland's [14], yet Norway records a substantially higher fire mortality rate (8.8 per million). While this comparison is descriptive and does not control for other determinants, it suggests that Iceland's outcomes reflect the combined effect of regulatory design, enforcement, fire service response, and public education rather than building age alone [10].

### 4.2 Building Construction Year as a Risk Indicator

The finding that no fatal structure-fire incidents occurred in post-1998 buildings (among records with known construction year) aligns with the intent of modern prescriptive fire safety requirements. Byggingarreglugerð nr. 441/1998 mandates smoke detectors and approved portable extinguishers in each dwelling, supporting the plausibility of improved detection and early response as contributors to the safety gains observed in the post-1990s period [5].

However, interpretation requires substantial caution, and the absence of fatalities in post-1998 buildings should not be attributed solely—or even primarily—to the 1998 regulation. Several methodological concerns apply:

First, **exposure time bias**: post-1998 buildings represent a smaller and more recently exposed share of the housing stock, so the absence of fatal incidents may partly reflect limited exposure time. The person-years approximation (Section 3.4) addresses this concern quantitatively: post-1998 dwellings accumulated approximately 2.08 million person-years of exposure during 1999–2025, yet recorded zero fatalities, compared with a rate of 0.57 per 100,000 person-years in pre-1998 dwellings over the same period. While the dwelling-stock model is approximate, the zero numerator is robust to any reasonable denominator adjustment. The ITSA further confirms a significant level decrease at the 1999 intervention point (IRR = 0.106, *p* = 0.010 in the Poisson model), consistent with a structural break beyond the pre-existing secular trend.

Second, **confounding by correlated improvements**: construction year serves as a proxy for a bundle of changes that co-evolved with regulation. Post-1998 buildings have newer electrical systems and wiring standards, modern appliances with improved safety features, and updated materials with better fire resistance. Owners and occupants of newer housing may also differ systematically from those in older stock—for example, in socioeconomic resources, smoking prevalence, and alcohol use patterns—all of which are established individual-level risk factors for fire fatality [2, 16, 17]. The present data cannot disentangle the contribution of mandatory smoke detectors and extinguishers from these concurrent technological and sociodemographic changes.

Third, **ecological fallacy**: this study reports aggregate associations between building construction period and fatality counts. Drawing individual-level causal inferences from such aggregate data risks the ecological fallacy [18]—the observed absence of fatalities in newer buildings may reflect population-level confounding rather than a direct protective effect of the 1998 building regulation per se. As Cunningham et al. [19] note in a broader injury context, the decline in residential fire deaths reflects the joint contribution of reduced smoking rates, increased smoke detector installation, and improved building codes, and isolating the independent effect of any single intervention from observational trend data alone is not possible.

The post-1998 finding is therefore best interpreted as consistent with—but not proof of—the effectiveness of modern prescriptive fire safety requirements. It documents a striking empirical pattern that merits further investigation using individual-level data linking building characteristics, occupant demographics, and fire safety equipment status.

Additionally, construction year is missing for 52% of all structure-fire incidents, though missingness is confined entirely to incidents prior to 1996—from 1996 onward, construction year is complete for all incidents.¹

¹ A fatal residential fire at Hjarðarhagi, Reykjavík (May 2025, 2 deaths) is included in the registry with a construction year of 1967, consistent with the post-1998 finding.

### 4.3 Seasonality and the Heating Season

The concentration of fatalities in October–March is consistent with established seasonal patterns in fire-death data across Northern Europe, commonly attributed to increased heating demand, longer periods spent indoors, extended darkness affecting detection and escape, and reduced nighttime escape margins [1]. In the Nordic context, these mechanisms may be particularly pronounced due to sustained winter heating demand and extended polar darkness.

### 4.4 Emerging Challenges

Despite the overall positive trend, the data reveal emerging risk patterns that merit attention from fire safety practitioners:

**Unauthorized residential use of commercial buildings.** Recent fatalities at Funahöfði and Stangarhyl (both 2023) involved deaths in buildings designed for commercial or industrial use but occupied as dwellings. Such buildings typically lack residential fire safety provisions (adequate egress, compartmentation, and detection), creating elevated risk that current inspection regimes may not adequately capture.

**Criminal arson.** The Bræðraborgarstígur incident in 2020 (3 deaths in a building originally constructed in 1906 with undocumented modifications) illustrates how arson—combined with vulnerable populations in substandard housing—creates risk that prescriptive building codes alone cannot address [11].

Both patterns disproportionately affect vulnerable populations including low-income residents, immigrants, and marginalized individuals who may have limited housing options [10]. As the practitioner dissemination notes, the benefits of decades of fire safety progress accrue primarily to those in compliant housing, while those with the fewest resources face the greatest residual risk [10]. This underscores that effective fire safety requires not only regulatory standards for new construction but also active enforcement, inspection of existing building stock, and coordination between fire services, building authorities, social services, and law enforcement.

### 4.5 Implications for Fire Safety Practice

Three practical directions follow from these descriptive findings:

1. **Targeted retrofit and inspection of older housing stock.** The concentration of fatalities in pre-1998 buildings supports prioritizing inspection and retrofit programs—particularly smoke detector installation and egress improvement—in older dwellings.

2. **Heating-season prevention campaigns.** The clear October–March concentration supports targeted seasonal campaigns addressing heating safety, smoke alarm maintenance, and escape planning.

3. **Cross-domain prevention.** The maritime concentration among non-structure incidents (15 of 29 deaths) highlights prevention opportunities in occupational fire safety outside the residential domain. Similarly, the emerging pattern of fatalities in unauthorized residential use of commercial buildings calls for improved interagency coordination.

### 4.6 Data Quality and Registry Value

A secondary but important finding concerns data quality. The Gjöll registry was compiled because existing official statistics lacked incident-level traceability and contained documented errors (e.g., the year 2009 recorded as having zero fire deaths in official statistics, despite a confirmed fatal fire at Kljáströnd in Eyjafjörður that year). As detailed in the practitioner dissemination [10], these quality problems appear to stem in part from repeated institutional transfers of the fire safety portfolio—first from Brunamálastofnun to Mannvirkjastofnun and subsequently to Húsnæðis- og mannvirkjastofnun (HMS)—resulting in fragmented record-keeping, no shared database, and no systematic linkage of incidents to building characteristics such as construction year. The registry approach—with source references for each incident—supports auditable trend analysis and reproducible research. Making the dataset publicly available [8] enables independent verification and extension.

### 4.7 Limitations

This study is descriptive and subject to several limitations.

First, **small sample size and rare-event instability**: 145 deaths across 58 years constitutes a small dataset by epidemiological standards. Decade-level estimates are sensitive to individual high-casualty incidents—for example, the Bræðraborgarstígur arson in 2020 (3 deaths) accounts for 20% of the 2020–2025 death total, substantially inflating that period's apparent rate. The Poisson confidence intervals reported in Section 3.2 illustrate this instability, and readers should interpret decade-level comparisons as indicative trends rather than precise estimates.

Second, the dataset includes only fatal incidents; trends in non-fatal fire incidence cannot be assessed.

Third, completeness of ascertainment cannot be quantified; under-ascertainment is plausible, particularly in earlier decades when archival sources may be incomplete. Any systematic under-counting in earlier periods would bias the observed decline, making the true peak-to-trough reduction appear larger or smaller than it actually was.

Fourth, **missing construction-year data**: construction year is missing for 48 of 93 structure-fire incidents (52%), concentrated entirely in pre-1996 incidents. This missing-not-at-random pattern means that the full-period construction-year analysis (Table 3, full dataset columns) is statistically weak and potentially biased. However, the sensitivity analysis (Section 3.5) demonstrates that all 48 missing-data incidents occurred between 1970 and 1995—a temporal constraint that makes it logically impossible for any of these buildings to have been constructed after 1998. The post-1998 zero is therefore unaffected by the missingness.

Fifth, the post-1998 finding relies on a modeled housing-stock denominator rather than census-derived dwelling counts stratified by construction period (Section 3.4). The person-years approximation provides an order-of-magnitude exposure estimate but cannot substitute for a proper population-at-risk denominator. Until Statistics Iceland or HMS publish dwelling-stock data cross-tabulated by construction year, the separation of improved building design, reduced exposure time, and correlated sociodemographic differences among occupants of newer versus older buildings remains approximate.

Sixth, key determinants of individual fatality risk (smoke alarm presence, alcohol involvement, smoking, mobility limitations, occupancy load) are not captured as structured variables in the registry and should not be inferred from aggregate trends. Individual-level studies in other jurisdictions have consistently identified alcohol impairment, living alone, advanced age, and impaired mobility as dominant risk factors for fire death [2, 16, 17]; the absence of these variables from the Gjöll registry precludes any assessment of their contribution to the observed patterns.

## 5 Conclusions

The Gjöll fatal incident registry for 1968–2025 documents a substantial long-run decline in fire fatalities in Iceland, consistent with—though not causally attributable to—the cumulative introduction of fire safety legislation and building regulation over the study period. Interrupted time series analysis confirms a significant pre-existing declining trend and a significant level decrease at the 1999 regulatory intervention, while a sensitivity analysis demonstrates that the 52% missing construction-year data cannot affect the post-1998 finding. A person-years exposure approximation estimates zero fatalities across approximately 2.08 million person-years in post-1998 dwellings, compared with 0.57 per 100,000 person-years in pre-1998 dwellings. The remaining fatal fire burden is concentrated in structure fires involving older building stock (mean construction year 1957) and shows clear heating-season concentration. However, construction year is a proxy for multiple correlated changes in building technology, occupant demographics, and safety equipment, and the modeled dwelling-stock denominator is approximate. The small absolute number of events introduces substantial statistical uncertainty, and individual high-casualty incidents can materially affect period-level estimates. The dataset is publicly deposited to enable reproducible monitoring and independent verification.

## Acknowledgments

The author acknowledges the use of generative AI tools for assistance with analytical code development; all code outputs and results were independently verified by the author.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Declarations

**Conflict of Interest:** The author declares no competing interests.

**Ethics:** The analyzed export contains no direct personal identifiers. Address-level fields are present for some incidents as part of the historical record but were not analyzed at the individual-household level.

**Data Availability:** The analyzed data tables are deposited at GAGNÍS – Gagnaþjónusta félagsvísinda (DOI: 10.34881/I5WGJU) and are also available through the public Gjöll interface at https://www.gjoll.is. Reproducibility scripts and generated outputs are available in the accompanying repository [8].

## References

1. European Fire Safety Alliance. Fatal residential fires in Europe: a preliminary assessment. European Fire Safety Alliance, 2018. https://www.europeanfiresafetyalliance.org/wp-content/uploads/2018/11/20181120-Fatal-residential-fires-in-Europe.pdf. Accessed 2 Jan 2026
2. Holborn PG, Nolan PF, Golt J (2003) An analysis of fatal unintentional dwelling fires investigated by London Fire Brigade between 1996 and 2000. Fire Saf J 38:1–42
3. Republic of Iceland. Lög um Brunamálastofnun ríkisins nr. 55/1969
4. Republic of Iceland. Brunavarnalög nr. 74/1982
5. Republic of Iceland. Byggingarreglugerð nr. 441/1998 (repealed). https://www.reglugerd.is/reglugerdir/allar/nr/441-1998. Accessed 2 Jan 2026
6. Republic of Iceland. Lög um brunavarnir nr. 75/2000
7. Myndigheten för samhällsskydd och beredskap (MSB) [now Swedish Civil Defence and Resilience Agency (MCF)]. Nordic Fire Statistics. 2023. https://www.mcf.se/en/about-us/research-and-statistics/nordic-fire-statistics/. Accessed 4 Mar 2026
8. Smárason MS. Fatal Fire Incidents in Iceland 1968–2025 (Gjöll dataset export; version 1.0.0). GAGNÍS – Gagnaþjónusta félagsvísinda, 2025. DOI: 10.34881/I5WGJU. https://gagnis.hi.is/dataset.xhtml?persistentId=doi:10.34881/I5WGJU. Accessed 4 Mar 2026
9. Tímarit.is. Dagblöð og tímarit. https://timarit.is. Accessed 2 Jan 2026
10. Smárason MS (2025) Góðar niðurstöður, slæm gögn: tölfræðileg greining á árangri í brunavörnum 1968–2025. Á vakt fyrir Ísland (blað Landssambands slökkviliðs- og sjúkraflutningamanna) 52(1):32–39
11. Húsnæðis- og mannvirkjastofnun (HMS). Skýrsla um Bræðraborgarstíg 1. 2020. https://fundur.reykjavik.is/sites/default/files/agenda-items/20_skyrsla_hms_-_braedraborgarstigur_0.pdf. Accessed 2 Jan 2026
12. Hagstofa Íslands (Statistics Iceland). Lykiltölur mannfjöldans 1703–2025 (MAN00000.px; Eining=0). 2025. https://px.hagstofa.is/pxis/api/v1/is/Ibuar/mannfjoldi/1_yfirlit/Yfirlit_mannfjolda/MAN00000.px. Accessed 2 Jan 2026
13. Húsnæðis- og mannvirkjastofnun (2024) Upplýsingar um meðalbyggingarár íslenskra mannvirkja [personal communication, March 2024]
14. Statistisk sentralbyrå (Statistics Norway). Boliger (Dwellings), table 06266: Dwellings by type of building and year of construction. 2024. https://www.ssb.no/en/bygg-bolig-og-eiendom/bolig-og-boforhold/statistikk/boliger. Accessed 4 Mar 2026. See also TABULA/EPISCOPE Norwegian building typology: https://episcope.eu/building-typology/country/no/
15. Húsnæðis- og mannvirkjastofnun (HMS). Fjöldi fullbúinna íbúða (Dwelling completions). 2025. https://hms.is. Accessed 4 Mar 2026
16. Marshall SW, Runyan CW, Bangdiwala SI, Linzer MA, Sacks JJ, Butts JD (1998) Fatal residential fires: who dies and who survives? JAMA 279(20):1633–1637. https://doi.org/10.1001/jama.279.20.1633
17. Doyle A, Lyons S, Lynn E (2019) Profile of fire fatalities in Ireland using coronial data. Fire Saf J 110:102892. https://doi.org/10.1016/j.firesaf.2019.102892
18. Loney T, Nagelkerke N (2014) The individualistic fallacy, ecological studies and instrumental variables: a causal interpretation. Emerg Themes Epidemiol 11:18. https://doi.org/10.1186/1742-7622-11-18
19. Cunningham RM, Walton MA, Carter PM (2018) The major causes of death in children and adolescents in the United States. N Engl J Med 379(25):2468–2475. https://doi.org/10.1056/NEJMsr1804754
20. Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D (2002) Segmented regression analysis of interrupted time series studies in medication use research. J Clin Pharm Ther 27(4):299–309. https://doi.org/10.1046/j.1365-2710.2002.00430.x
21. Bernal JL, Cummins S, Gasparrini A (2017) Interrupted time series regression for the evaluation of public health interventions: a tutorial. Int J Epidemiol 46(1):348–355. https://doi.org/10.1093/ije/dyw098
22. Seabold S, Perktold J (2010) Statsmodels: econometric and statistical modeling with Python. In: Proceedings of the 9th Python in Science Conference, pp 92–96. https://doi.org/10.25080/Majora-92bf1922-011

---

## Tables

**Table 1** Overall burden of fatal fire incidents in Iceland (1968–2025)

| Category | Incidents (*n*) | Deaths (*n*) | Deaths per incident (mean) |
|---|---:|---:|---:|
| Structure fires | 93 | 116 | 1.25 |
| Other fire-related deaths | 20 | 29 | 1.45 |
| **Total** | **113** | **145** | **1.28** |

**Table 2** Period totals and crude mortality rates for fatal fire incidents in Iceland

| Period | Incidents (*n*) | Deaths (*n*) | Mean population (1 Jan) | Annualized deaths per million population |
|---|---:|---:|---:|---:|
| 1968–1969* | 6 | 13 | 201,488 | 32.3 |
| 1970–1979 | 35 | 47 | 214,495 | 21.9 |
| 1980–1989 | 19 | 24 | 238,886 | 10.1 |
| 1990–1999 | 13 | 14 | 264,973 | 5.3 |
| 2000–2009 | 14 | 17 | 296,399 | 5.7 |
| 2010–2019 | 14 | 15 | 325,140 | 4.6 |
| 2020–2025 | 12 | 15 | 370,941 | 6.7 |

*The 1968–1969 bin covers 2 years; the rate is unstable due to the short observation window.

**Table 3** Fatal structure fires by building construction year

| Construction year band | Incidents (*n*), full dataset (*n* = 93) | Deaths (*n*), full | Incidents (*n*), 1996–2025 subset (*n* = 35) | Deaths (*n*), 1996–2025 |
|---|---:|---:|---:|---:|
| 1900–1919 | 7 | 13 | 4 | 6 |
| 1920–1939 | 3 | 3 | 1 | 1 |
| 1940–1959 | 18 | 19 | 13 | 14 |
| 1960–1979 | 11 | 12 | 11 | 12 |
| 1980–1997 | 6 | 8 | 6 | 8 |
| Unknown | 48 | 61 | 0 | 0 |
| **Total** | **93** | **116** | **35** | **41** |

The 1996–2025 subset is reported because construction year is complete from 1996 onward. In both the full dataset (where known) and the 1996–2025 subset, there are zero fatal structure-fire incidents in buildings constructed after 1998.

---

## Figure Captions

**Fig. 1** Annual fire-related deaths in Iceland (1968–2025) from the Gjöll registry export. The rolling mean illustrates the long-run decline despite substantial year-to-year variability.

**Fig. 2** Monthly distribution of fatal fire incidents (deaths and incident counts). The October–March heating season accounts for 58% of both incidents and deaths.

**Fig. 3** Fatal structure-fire incidents and deaths by building construction-year band, showing concentration of fatalities in older building stock.

**Fig. 4** Interrupted time series analysis of annual fire-related deaths in Iceland (1968–2025). Upper panel: observed annual deaths with fitted values from the negative binomial segmented regression model and counterfactual trajectory (no 1999 intervention). Lower panel: corresponding mortality rates per 100,000 population. Vertical lines indicate the 1982 fire prevention act and the 1999 building regulation.
