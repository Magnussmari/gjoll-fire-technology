# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "bibtexparser>=1.4,<2",
# ]
# ///
"""Verify DOIs and URLs in references.bib, and cross-check against manuscript.qmd citations."""

import re
import sys
from pathlib import Path

import bibtexparser
import httpx


def parse_bib(bib_path: str) -> dict:
    """Parse .bib file and return entries keyed by citation key."""
    text = Path(bib_path).read_text(encoding="utf-8")
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    library = bibtexparser.loads(text, parser=parser)
    entries = {}
    for entry in library.entries:
        entries[entry["ID"]] = entry
    return entries


def extract_citations(qmd_path: str) -> set[str]:
    """Extract all @CiteKey references from manuscript.qmd."""
    text = Path(qmd_path).read_text(encoding="utf-8")
    # Remove YAML front matter (which contains 'bibliography:' etc.)
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    # Match [@Key1; @Key2] and standalone @Key patterns
    bracket_cites = re.findall(r"\[@([^\]]+)\]", text)
    keys = set()
    for group in bracket_cites:
        for part in group.split(";"):
            part = part.strip()
            if part.startswith("@"):
                part = part[1:]
            keys.add(part)
    # Standalone @Key (not in brackets, not @fig- @tbl- @sec-)
    standalone = re.findall(r"(?<!\w)@(\w+)", text)
    for key in standalone:
        if not key.startswith(("fig", "tbl", "sec")):
            keys.add(key)
    return keys


def verify_doi(doi: str, client: httpx.Client) -> tuple[bool, int, str]:
    """Check if a DOI resolves via doi.org. Returns (ok, status_code, final_url)."""
    url = f"https://doi.org/{doi}"
    try:
        resp = client.head(url, follow_redirects=True, timeout=15)
        return resp.status_code == 200, resp.status_code, str(resp.url)
    except httpx.TimeoutException:
        return False, 0, "TIMEOUT"
    except httpx.HTTPError as e:
        return False, 0, str(e)


def verify_url(url: str, client: httpx.Client) -> tuple[bool, int]:
    """Check if a URL is reachable. Returns (ok, status_code)."""
    try:
        resp = client.head(url, follow_redirects=True, timeout=15)
        if resp.status_code == 405:  # HEAD not allowed, try GET
            resp = client.get(url, follow_redirects=True, timeout=15)
        return resp.status_code < 400, resp.status_code
    except httpx.TimeoutException:
        return False, 0
    except httpx.HTTPError:
        return False, 0


def main():
    bib_path = sys.argv[1] if len(sys.argv) > 1 else "manuscript/references.bib"
    qmd_path = sys.argv[2] if len(sys.argv) > 2 else "manuscript/Smarason_2026_Fatal_Fire_Incidents_Iceland.qmd"

    if not Path(bib_path).exists():
        print(f"Error: {bib_path} not found")
        sys.exit(1)

    entries = parse_bib(bib_path)
    citations = extract_citations(qmd_path) if Path(qmd_path).exists() else set()

    print("=" * 70)
    print(f"  Reference Verification: {bib_path}")
    print(f"  Manuscript: {qmd_path}")
    print("=" * 70)
    print()

    # --- Cross-reference check ---
    bib_keys = set(entries.keys())
    print(f"CROSS-REFERENCE CHECK")
    print(f"  Bib entries:       {len(bib_keys)}")
    print(f"  Manuscript cites:  {len(citations)}")

    unused = bib_keys - citations
    missing = citations - bib_keys

    if unused:
        print(f"  WARN: In .bib but not cited in manuscript: {', '.join(sorted(unused))}")
    if missing:
        print(f"  ERROR: Cited in manuscript but not in .bib: {', '.join(sorted(missing))}")
    if not unused and not missing:
        print(f"  OK: Perfect match between .bib and manuscript citations.")
    print()

    # --- Field completeness ---
    print("FIELD COMPLETENESS")
    print(f"  {'Key':<25} {'Type':<15} {'DOI':<5} {'URL':<5} {'Year':<5} {'Author':<5}")
    print(f"  {'-'*25} {'-'*15} {'-'*5} {'-'*5} {'-'*5} {'-'*5}")

    issues = []
    for key, entry in entries.items():
        has_doi = "doi" in entry
        has_url = "url" in entry
        has_year = "year" in entry
        has_author = "author" in entry
        entry_type = entry.get("ENTRYTYPE", "unknown")

        doi_mark = "Y" if has_doi else "-"
        url_mark = "Y" if has_url else "-"
        year_mark = "Y" if has_year else "!"
        author_mark = "Y" if has_author else "!"

        print(f"  {key:<25} {entry_type:<15} {doi_mark:<5} {url_mark:<5} {year_mark:<5} {author_mark:<5}")

        if not has_doi and not has_url:
            if entry_type in ("article", "inproceedings"):
                issues.append(f"  WARN: {key} ({entry_type}) has neither DOI nor URL")
        if not has_year:
            issues.append(f"  ERROR: {key} missing year")
        if not has_author:
            issues.append(f"  ERROR: {key} missing author")

    print()
    if issues:
        print("COMPLETENESS ISSUES")
        for issue in issues:
            print(issue)
        print()

    # --- DOI verification ---
    doi_entries = {k: v["doi"] for k, v in entries.items() if "doi" in v}
    url_entries = {k: v["url"] for k, v in entries.items()
                   if "url" in v and "doi" not in v}

    if doi_entries:
        print(f"DOI VERIFICATION ({len(doi_entries)} entries)")
        errors = 0
        client = httpx.Client(
            headers={"User-Agent": "ReferenceVerifier/1.0 (academic manuscript check)"},
        )
        try:
            for key, doi in doi_entries.items():
                ok, status, final_url = verify_doi(doi, client)
                if ok:
                    print(f"  OK   {key:<25} doi:{doi}")
                else:
                    print(f"  FAIL {key:<25} doi:{doi}  -> status={status} url={final_url}")
                    errors += 1
        finally:
            client.close()

        print()
        if errors:
            print(f"  {errors} DOI(s) failed to resolve!")
        else:
            print(f"  All {len(doi_entries)} DOIs verified.")
        print()

    # --- URL verification (entries without DOI) ---
    if url_entries:
        print(f"URL VERIFICATION ({len(url_entries)} entries without DOI)")
        errors = 0
        client = httpx.Client(
            headers={"User-Agent": "ReferenceVerifier/1.0 (academic manuscript check)"},
        )
        try:
            for key, url in url_entries.items():
                ok, status = verify_url(url, client)
                if ok:
                    print(f"  OK   {key:<25} {url}")
                else:
                    print(f"  FAIL {key:<25} {url}  -> status={status}")
                    errors += 1
        finally:
            client.close()

        print()
        if errors:
            print(f"  {errors} URL(s) failed!")
        else:
            print(f"  All {len(url_entries)} URLs verified.")
        print()

    # --- Summary ---
    total_issues = len(issues) + (len(missing))
    print("=" * 70)
    if total_issues == 0 and not unused:
        print("  RESULT: All checks passed.")
    else:
        print(f"  RESULT: {total_issues} issue(s) found. Review above.")
    print("=" * 70)


if __name__ == "__main__":
    main()
