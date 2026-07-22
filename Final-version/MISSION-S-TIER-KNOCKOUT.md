<!--
@artifact      Mission: Fire paper → S-tier knockout, submission-ready
@orchestrator  Magnus Smárason | smarason.is
@created       2026-07-22
@status        COMPLETE — all ISC green; staged for submission (Gjöll ratified as-is)
@target        Fire Technology (Springer, SNAPP double-anonymous)
-->

# MISSION — Fatal-Fire Iceland: knock it out of the park

**Goal.** Take the fire paper from "submission-ready" to *unimpeachable* — an S-tier
resubmission-proof draft that a hostile reviewer cannot dent on craft, reproducibility, or
causal discipline — then submit. Scope is now **substantive edits allowed** (the
micro-changes-only constraint is lifted), but the science is signed off by both authors:
we sharpen exposition, rigor, and reproducibility, we do **not** change findings, numbers,
or study design.

**Why now.** A sister paper's peer review (a separate manuscript) surfaced the exact
failure modes reviewers punish — undefined constructs, unreconstructable methods, causal
overreach, weak AI/repro disclosure, long unpunctuated sentences. This fire paper is
already ahead on most of them. This mission closes the remaining gaps *before* a reviewer
finds them.

---

## PHASE 1 — CURRENT STATE (verified 2026-07-22)

**Already delivered and committed this cycle:**
- PDF typography fixed (ragged-right reference list, unbroken DOIs, clean tables) — `3eea008`
- Anonymized author-mask rendering bug fixed — `3eea008`
- Proper-noun casing protected against CSL sentence-casing — `ad8f3c5`
- Review findings applied: primary ITSA slope in abstract, RECORD citation added, geothermal figure aligned, American spelling, em-dashes removed — `013eb5a`
- SUBMISSION-READINESS report with all 43 references verified + clickable — `833895c`
- First-person → impersonal scientific voice across the body (0 first-person) — `0c20d42`
- Role clarity to S-tier: CRediT Author Contributions (M.S.S. 9 roles, T.B. 2) — `aad58fa`

**Standing gates (all currently green):**
`verify_statistics.py` 125/125 · `anonymize.py --check` in sync · 0 identity leaks in ANON
docx/pdf · 0 first-person in body · 43 refs verified · abstract 225/250 words.

**Known-good infrastructure:**
- Reproducibility repo public: `github.com/Magnussmari/gjoll-fire-technology` (200)
- Data DOI (DataCite-verified): `10.34881/I5WGJU`
- Blinded LLM re-code deposited: `data/blinded_recode_codings_1996_2025.csv` + README;
  run at **temperature 0** (deterministic), κ = 0.933 recomputable offline.

---

## PHASE 2 — IDEAL STATE

A draft where: every sentence is reconstructable on first read; the AI/reproducibility
disclosure pre-empts the toughest methods reviewer; not one sentence claims what the paper
disclaims about causality; every figure legend stands alone; the anonymity posture is a
deliberate, documented decision; and the full submission package assembles with every gate
green. A reviewer's honest verdict is "accept / minor revision," and they cannot point to a
single craft defect.

---

## PHASE 3 — IDEAL STATE CRITERIA (ISC) — binary, testable

| # | Criterion | Test | Status |
|---|-----------|------|--------|
| ISC-1 | No body sentence exceeds ~40 words without justified structure | sentence-length script over qmd body; longest ≤ ~40w (tables/lists exempt) | ✅ |
| ISC-2 | AI-disclosure asserts: model versions archived, prompts archived, raw outputs archived, outputs a **frozen deposited snapshot**, κ recomputable offline. (Temperature-0 claim deliberately DROPPED: only the GPT-5.5 call set it; the Claude call used the API default. Frozen-snapshot framing is true and a stronger guarantee.) | ✅ |
| ISC-3 | Causal-consistency razor: no sentence asserts the 1998 regulation's *independent causal effect*; describe/suggest/identify boundary held everywhere | forbidden-construction grep + full human pass | ✅ |
| ISC-4 | Every figure legend is self-contained (units, source, defined terms) | read all 3 main + supplementary figure legends | ✅ |
| ISC-5 | Anonymity: **ratified as-is** (Gjöll retained). Policy bar met (manuscript hands over no identity; DOI/URL/GitHub/self-cites masked); name is load-bearing to the paper's identity and determined de-anon is unavoidable regardless | ✅ |
| ISC-6 | STROBE + RECORD checklist exists, complete, and is in the submission package | file present; every item mapped to a line/section | ✅ |
| ISC-7 | Cover letter names the reproducibility/verification infrastructure as a differentiator | read cover-letter-fire-technology.md | ✅ |
| ISC-8 | 2–3 suggested reviewers prepared (SNAPP step 7), no COI/co-authorship | list drafted (optional to submit) | ✅ |
| ISC-9 | All standing gates green after every edit; SUBMISSION-READINESS refreshed | run full gate sweep; update report | ✅ |
| ISC-10 | Final rendered PDFs (named + anon) + DOCX shipped to Final-version; 0 leaks | render + leak scan + copy | ✅ |

---

## PHASE 4 — WORKSTREAMS

### WS-A · Sentence surgery (ISC-1) — *substantive, no science change*
Break the Methods offenders and sweep Discussion/Limitations for the same:
- 99-word chain: "This experience informs interpretation… as an automated reproducibility check." → split into 3–4 sentences.
- 89-word chain: "To guard against this, the two cases that fall near the boundary…" → split.
- 69-word ITSA sentence, 58-word classification-convention sentence, 54-word person-years sentence → split each.
Preserve every citation, number, and hedge verbatim; only punctuation/structure changes.

### WS-B · AI + reproducibility disclosure hardening (ISC-2)
In the Methods AI paragraph and the Acknowledgments, state explicitly:
- exact model versions + prompts are archived in the repo (already partially there);
- outputs are a **frozen, deposited snapshot**, so run-to-run LLM non-determinism cannot
  affect the reported κ (temperature-0 NOT claimed — only one of the two calls set it;
  the snapshot guarantee is stronger and true regardless);
- κ and agreement are **recomputable offline** from the deposited per-incident codings
  without re-querying any model.
This pre-empts the "AI is unreproducible" reviewer entirely. All claims are true of the
current run (verified against `blinded_second_coding.py` + README).

### WS-C · Causal-consistency razor (ISC-3)
Full-paper adversarial pass for any sentence that drifts from description to causal claim
about the 1998 regulation. Grep candidates ("caused", "due to the regulation", "the
regulation reduced", "attributable to") then read every Discussion/Conclusion sentence.
Expected near-clean (this is the paper's strength); fix any drift found.

### WS-D · Figure self-containment (ISC-4)
Read all figure legends (main + supplementary). Confirm each states units, source, and
defines any term a reader needs (e.g. construction-year bands in Fig 3). Fix any that lean
on the body to be understood.

### WS-E · Anonymity decision (ISC-5) — *DECISION REQUIRED FROM MAGNÚS*
"Gjöll" appears 13× in the ANON manuscript and is the one string that de-anonymizes
casually (DOI/URL/GitHub/self-cites are already masked). Options:
- **(a) Ratify as-is** — accept that a determined reviewer de-anonymizes regardless; the
  policy bar (manuscript hands over no identity) is already met. One-line rationale here.
- **(b) Neutralize the name in the ANON build only** — teach `anonymize.py` to swap
  "Gjöll"→"the national registry" / "[registry name withheld]" and drop the mythology
  footnote in ANON; named build keeps Gjöll intact. Reversible, anon-only.
Recommendation: **(b)** as cheap hygiene, but it changes the anon reading and the name is
an identity choice — Magnús decides. Default if silent: **(a) ratify**, since it's
policy-compliant and Gjöll is load-bearing to the paper's identity.

### WS-F · Checklist + cover letter + reviewers (ISC-6, 7, 8)
- Verify the STROBE/RECORD checklist file exists and is complete; create/complete if not.
- Polish the cover letter to foreground the reproducibility instrument (verification script
  that recomputes every statistic; public repo; DataCite DOI) as the paper's differentiator.
- Draft 2–3 suggested reviewers (fire-safety-engineering or injury-epidemiology, no UNAK,
  no recent co-authorship).

### WS-G · Final assembly + gates (ISC-9, 10)
Re-render all four documents (PDF+DOCX), run the full gate sweep after every WS, leak-scan
the ANON build, ship to Final-version, refresh SUBMISSION-READINESS, then submit per
START-HERE.

---

## PHASE 5 — SEQUENCING

1. **WS-E decision** (unblocks the anon build; one question to Magnús) — parallel with WS-A.
2. **WS-A** sentence surgery → render → gates.
3. **WS-B** AI disclosure → render → gates.
4. **WS-C** causal razor + **WS-D** figures (read-mostly) → fix any → render → gates.
5. **WS-F** checklist + cover letter + reviewers.
6. **WS-G** final assembly, SUBMISSION-READINESS refresh, submit.

Each WS commits independently on the working branch with gates green before the next.

---

## PHASE 6 — VERIFICATION GATES (run after every WS)

```
python3 scripts/verify_statistics.py      # 125/125
python3 scripts/anonymize.py --check       # in sync
python3 scripts/verify_references.py        # DOIs resolve
# + leak scan on ANON docx/pdf (0 hits)
# + first-person scan on body (0)
# + sentence-length scan (ISC-1 threshold)
```

## PHASE 7 — DEFINITION OF DONE

All 10 ISC boxes checked; all gates green; Final-version holds the final rendered set with
0 leaks; SUBMISSION-READINESS refreshed to this state; anonymity posture documented; and
the paper is either submitted or staged for a one-word GO to submit. Report delivered as
"did X, verified by Y" — never as a question.

---

### Open decision blocking full-auto
**WS-E (anonymity):** ratify "Gjöll" as-is, or mask it in the ANON build only? Default on
silence: ratify. Everything else proceeds without a gate.
