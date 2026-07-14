#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["textstat"]
# ///
"""Readability analysis for the Fire Technology manuscript.

Strips Quarto/YAML frontmatter and markdown formatting before scoring.
Fire Technology target: Flesch-Kincaid Grade 12-17, Flesch Reading Ease 20-40.
"""

import re
import sys
from pathlib import Path

import textstat


def strip_yaml_frontmatter(text: str) -> str:
    """Remove YAML frontmatter between --- delimiters."""
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)


def strip_markdown(text: str) -> str:
    """Remove markdown/Quarto artifacts, keeping prose."""
    # Remove include directives
    text = re.sub(r"\{\{<\s*include\s+.*?>\}\}", "", text)
    # Remove cross-references
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"\{#[\w-]+\}", "", text)
    text = re.sub(r"@sec-\w+", "", text)
    # Remove footnote markers
    text = re.sub(r"\[\^[\w]+\]", "", text)
    # Remove inline footnote definitions
    text = re.sub(r"\[\^[\w]+\]:.*$", "", text, flags=re.MULTILINE)
    # Remove images
    text = re.sub(r"!\[.*?\]\(.*?\)\{.*?\}", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Remove LaTeX math
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    text = re.sub(r"\$.*?\$", "", text)
    # Remove table rows
    text = re.sub(r"^\|.*\|$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^:.*\{#tbl-.*\}$", "", text, flags=re.MULTILINE)
    # Remove headers but keep as sentence boundaries
    text = re.sub(r"^#{1,6}\s+.*$", "", text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r"\*{1,2}(.*?)\*{1,2}", r"\1", text)
    # Remove Quarto divs
    text = re.sub(r"^:::.*$", "", text, flags=re.MULTILINE)
    # Remove URLs
    text = re.sub(r"<https?://[^>]+>", "", text)
    text = re.sub(r"https?://\S+", "", text)
    # Remove citation brackets
    text = re.sub(r"\[[-;@\w\s,]+\]", "", text)
    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"  +", " ", text)
    return text.strip()


def analyze_file(path: Path) -> dict:
    """Analyze a single QMD file."""
    text = path.read_text(encoding="utf-8")
    text = strip_yaml_frontmatter(text)
    prose = strip_markdown(text)

    words = textstat.lexicon_count(prose)
    sentences = textstat.sentence_count(prose)

    return {
        "file": path.name,
        "words": words,
        "sentences": sentences,
        "fk_grade": textstat.flesch_kincaid_grade(prose),
        "fre": textstat.flesch_reading_ease(prose),
        "gunning_fog": textstat.gunning_fog(prose),
        "smog": textstat.smog_index(prose),
        "coleman_liau": textstat.coleman_liau_index(prose),
        "ari": textstat.automated_readability_index(prose),
    }


def main():
    manuscript_dir = Path(__file__).parent.parent / "manuscript"

    # Chapter files in order
    chapters = sorted(manuscript_dir.glob("[0-9][0-9]-*.qmd"))
    if not chapters:
        print("No chapter files found. Checking for monolithic QMD...")
        chapters = list(manuscript_dir.glob("Smarason_*.qmd"))

    if not chapters:
        print("ERROR: No QMD files found in", manuscript_dir)
        sys.exit(1)

    # Analyze each chapter
    results = []
    combined_text = ""
    for ch in chapters:
        text = ch.read_text(encoding="utf-8")
        text = strip_yaml_frontmatter(text)
        combined_text += strip_markdown(text) + "\n\n"
        results.append(analyze_file(ch))

    # Combined analysis
    combined_words = textstat.lexicon_count(combined_text)
    combined_sentences = textstat.sentence_count(combined_text)
    combined_fk = textstat.flesch_kincaid_grade(combined_text)
    combined_fre = textstat.flesch_reading_ease(combined_text)

    # Fire Technology targets
    FK_MIN, FK_MAX = 12, 17
    FRE_MIN, FRE_MAX = 20, 40

    # Output
    print("=" * 72)
    print("READABILITY ANALYSIS: Fatal Fire Incidents in Iceland (1968-2025)")
    print("=" * 72)
    print()

    # Per-chapter table
    print(f"{'Chapter':<30} {'Words':>6} {'Sents':>6} {'FK Grade':>9} {'FRE':>6}")
    print("-" * 60)
    for r in results:
        fk_flag = " *" if not (FK_MIN <= r["fk_grade"] <= FK_MAX) else ""
        print(f"{r['file']:<30} {r['words']:>6} {r['sentences']:>6} {r['fk_grade']:>8.1f}{fk_flag} {r['fre']:>6.1f}")

    print("-" * 60)
    print(f"{'COMBINED':<30} {combined_words:>6} {combined_sentences:>6} {combined_fk:>8.1f}  {combined_fre:>6.1f}")
    print()

    # Detailed metrics
    print("DETAILED METRICS (Combined)")
    print(f"  Flesch-Kincaid Grade:       {combined_fk:.1f}  (target: {FK_MIN}-{FK_MAX})")
    print(f"  Flesch Reading Ease:        {combined_fre:.1f}  (target: {FRE_MIN}-{FRE_MAX})")
    print(f"  Gunning Fog Index:          {textstat.gunning_fog(combined_text):.1f}")
    print(f"  SMOG Index:                 {textstat.smog_index(combined_text):.1f}")
    print(f"  Coleman-Liau Index:         {textstat.coleman_liau_index(combined_text):.1f}")
    print(f"  Automated Readability:      {textstat.automated_readability_index(combined_text):.1f}")
    print()

    # Verdict
    fk_ok = FK_MIN <= combined_fk <= FK_MAX
    fre_ok = FRE_MIN <= combined_fre <= FRE_MAX

    if fk_ok and fre_ok:
        print("VERDICT: PASS -- Within Fire Technology target range")
    elif fk_ok or fre_ok:
        print("VERDICT: MARGINAL -- Partially within target range")
        if not fk_ok:
            print(f"  FK Grade {combined_fk:.1f} outside {FK_MIN}-{FK_MAX}")
        if not fre_ok:
            print(f"  FRE {combined_fre:.1f} outside {FRE_MIN}-{FRE_MAX}")
    else:
        print("VERDICT: OUTSIDE TARGET -- Review readability")
        print(f"  FK Grade {combined_fk:.1f} outside {FK_MIN}-{FK_MAX}")
        print(f"  FRE {combined_fre:.1f} outside {FRE_MIN}-{FRE_MAX}")


if __name__ == "__main__":
    main()
