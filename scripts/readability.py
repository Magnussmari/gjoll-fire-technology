# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "textstat",
# ]
# ///
"""Flesch-Kincaid readability analysis of manuscript.qmd."""

import re
import sys
from pathlib import Path

import textstat


def extract_prose(qmd_path: str) -> str:
    """Extract prose text from a Quarto manuscript, stripping YAML, LaTeX, code, and markdown syntax."""
    text = Path(qmd_path).read_text(encoding="utf-8")

    # Remove YAML front matter
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

    # Remove raw LaTeX blocks
    text = re.sub(r"```\{=latex\}.*?```", "", text, flags=re.DOTALL)

    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Remove LaTeX math
    text = re.sub(r"\$[^$]+\$", "", text)

    # Remove image/figure lines
    text = re.sub(r"!\[.*?\]\(.*?\)\{.*?\}", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)

    # Remove citation keys [@...] but keep surrounding text
    text = re.sub(r"\[@[^\]]+\]", "", text)

    # Remove cross-references (@fig-..., @tbl-..., @sec-...)
    text = re.sub(r"@(fig|tbl|sec)-\w+", "", text)

    # Remove markdown headers
    text = re.sub(r"^#+\s.*$", "", text, flags=re.MULTILINE)

    # Remove markdown formatting
    text = re.sub(r"\{[^}]*\}", "", text)  # {#sec-id .unnumbered}
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # bold
    text = re.sub(r"\*([^*]+)\*", r"\1", text)  # italic
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links
    text = re.sub(r"\[\^[^\]]+\]", "", text)  # footnote refs
    text = re.sub(r"^\[\^[^\]]+\]:.*$", "", text, flags=re.MULTILINE)  # footnote defs

    # Remove Quarto divs
    text = re.sub(r"^:::.*$", "", text, flags=re.MULTILINE)

    # Remove numbered list markers
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)

    # Collapse whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


def main():
    qmd_path = sys.argv[1] if len(sys.argv) > 1 else "manuscript.qmd"

    if not Path(qmd_path).exists():
        print(f"Error: {qmd_path} not found")
        sys.exit(1)

    prose = extract_prose(qmd_path)

    word_count = textstat.lexicon_count(prose, removepunct=True)
    sentence_count = textstat.sentence_count(prose)
    syllable_count = textstat.syllable_count(prose)

    print("=" * 60)
    print(f"  Readability Analysis: {qmd_path}")
    print("=" * 60)
    print()
    print("BASIC COUNTS")
    print(f"  Words:          {word_count:,}")
    print(f"  Sentences:      {sentence_count:,}")
    print(f"  Syllables:      {syllable_count:,}")
    print(f"  Avg words/sent: {word_count / sentence_count:.1f}")
    print(f"  Avg syll/word:  {syllable_count / word_count:.2f}")
    print()
    print("READABILITY SCORES")
    print(f"  Flesch-Kincaid Grade Level:  {textstat.flesch_kincaid_grade(prose):.1f}")
    print(f"  Flesch Reading Ease:         {textstat.flesch_reading_ease(prose):.1f}")
    print(f"  Gunning Fog Index:           {textstat.gunning_fog(prose):.1f}")
    print(f"  Coleman-Liau Index:          {textstat.coleman_liau_index(prose):.1f}")
    print(f"  Automated Readability Index: {textstat.automated_readability_index(prose):.1f}")
    print(f"  Dale-Chall Readability:      {textstat.dale_chall_readability_score(prose):.1f}")
    print()

    fk = textstat.flesch_kincaid_grade(prose)
    fre = textstat.flesch_reading_ease(prose)

    print("INTERPRETATION")
    print(f"  FK Grade {fk:.1f} = ~{int(fk)}th grade US reading level")
    if fk >= 12:
        print("  -> College-level or above (typical for academic papers)")
    elif fk >= 10:
        print("  -> Advanced high school level")

    if fre < 30:
        print(f"  FRE {fre:.0f} = Very difficult (college graduate level)")
    elif fre < 50:
        print(f"  FRE {fre:.0f} = Difficult (college level)")
    elif fre < 60:
        print(f"  FRE {fre:.0f} = Fairly difficult (10th-12th grade)")

    print()
    print("FIRE TECHNOLOGY CONTEXT")
    print("  Academic journals typically score FK 12-17, FRE 20-40.")
    print("  Fire Technology papers average ~FK 14, FRE ~25.")
    if 12 <= fk <= 18 and fre < 45:
        print("  -> Your manuscript is within normal range for the journal.")
    elif fk > 18:
        print("  -> Consider simplifying some sentences for clarity.")
    elif fk < 12:
        print("  -> Unusually accessible — good, if technical precision is maintained.")


if __name__ == "__main__":
    main()
