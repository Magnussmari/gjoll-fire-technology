#!/usr/bin/env python3
"""Derive the double-anonymous manuscript + supplement from the named sources.

Fire Technology is double-anonymous: the ANONYMIZED .qmd files are what get
submitted, so they must always match the named manuscript's science. Maintaining
two files by hand invites drift (it did). This script regenerates the ANON files
from the named ones by applying a MINIMAL, fixed set of blinding transforms, then
asserts that no author-identifying marker survives.

Usage:  python scripts/anonymize.py        # regenerate + self-check
        python scripts/anonymize.py --check # verify existing ANON is in sync (CI)
"""
import re, sys, pathlib

M = pathlib.Path(__file__).resolve().parent.parent / "manuscript"
NAMED_MAIN = M / "Smarason_2026_BriefCommunication.qmd"
ANON_MAIN  = M / "Smarason_2026_ANONYMIZED.qmd"
NAMED_SUPP = M / "supplementary.qmd"
ANON_SUPP  = M / "supplementary_ANON.qmd"

# --- the blinded replacements (exactly as the established ANON renders them) ---
BIO_NAMED = ("The lead author served as a firefighter and paramedic and was formerly "
    "chair of the national firefighter and paramedic union (Landssamband "
    "slökkviliðs- og sjúkraflutningamanna, LSS). He was also formerly employed at the "
    "institution responsible for fire safety oversight (the Housing and Construction "
    "Authority, Húsnæðis- og mannvirkjastofnun, HMS). "
    "This experience informs interpretation, but did not drive the classification:")
BIO_ANON = ("One author has prior professional experience in fire and rescue services "
    "and, previously, in the national fire-safety oversight body examined in this "
    "study; this potential conflict of interest is disclosed in full on the title "
    "page. This experience informs interpretation but did not drive the classification:")

TAIL_ANON = """# Compliance with Ethical Standards {.unnumbered}

**Competing interests:** One author has a prior professional association with the regulatory body examined in this study. In accordance with the journal's double-anonymous policy, the full disclosure --- together with author identities, affiliations, funding, author contributions, acknowledgments, and data-availability identifiers --- is provided on the separate Title Page.

**Data availability:** The registry data and the reproducibility code (including a script that recomputes every reported statistic) are publicly deposited; the access identifiers that would reveal author identity are listed on the Title Page and are openly available.

# References {.unnumbered}"""

# markers that must NEVER appear in an anonymized file (author identity)
LEAK_MARKERS = [
    "Magnús Smári", "Smárason", "Thomas Barry", "magnus@smarason.is", "smarason.is",
    "0009-0008-2050", "0000-0002-0633", "github.com/Magnussmari",
    "The lead author served", "held elected leadership", "M.S.S.", "T.B. declares",
    "MSS conceived", "Author Contributions",
]

def strip_author_yaml(text):
    # remove the YAML author: block (from 'author:' up to the next top-level key)
    return re.sub(r"\nauthor:\n(?: .*\n|  .*\n)+(?=\w+:)", "\n", text, count=1)

def anonymize_main(text):
    orig = text
    text = strip_author_yaml(text)
    assert "\nauthor:\n" not in text, "author YAML block not removed (main)"
    assert BIO_NAMED in text, "firefighter-bio anchor not found (main) — did the wording change?"
    text = text.replace(BIO_NAMED, BIO_ANON)
    # collapse tail: Acknowledgments ... Data Availability  ->  blinded compliance + References
    text = re.sub(r"# Acknowledgments \{\.unnumbered\}.*?# References \{\.unnumbered\}",
                  TAIL_ANON, text, count=1, flags=re.DOTALL)
    assert text != orig and "# Acknowledgments" not in text, "tail not collapsed (main)"
    return text

def anonymize_supp(text):
    text = strip_author_yaml(text)
    assert "\nauthor:\n" not in text, "author YAML block not removed (supp)"
    return text

def leak_check(text, label):
    hits = [m for m in LEAK_MARKERS if m in text]
    if hits:
        sys.exit(f"IDENTITY LEAK in {label}: {hits}")

def run(check_only):
    outputs = [
        (NAMED_MAIN, ANON_MAIN, anonymize_main, "ANONYMIZED main"),
        (NAMED_SUPP, ANON_SUPP, anonymize_supp, "ANON supplement"),
    ]
    drift = False
    for named, anon, fn, label in outputs:
        produced = fn(named.read_text(encoding="utf-8"))
        leak_check(produced, label)
        if check_only:
            current = anon.read_text(encoding="utf-8") if anon.exists() else ""
            if produced.strip() != current.strip():
                print(f"OUT OF SYNC: {anon.name} does not match {named.name}")
                drift = True
            else:
                print(f"in sync: {anon.name}")
        else:
            anon.write_text(produced, encoding="utf-8")
            print(f"wrote {anon.name}  (leak-check passed)")
    if check_only and drift:
        sys.exit("anonymized files are stale; run: python scripts/anonymize.py")
    print("OK")

if __name__ == "__main__":
    run("--check" in sys.argv)
