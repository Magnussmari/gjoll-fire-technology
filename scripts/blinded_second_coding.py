#!/usr/bin/env python3
"""
Blinded independent second coding of the structure-vs-other classification
(peer-review item M4). Two frontier models act as independent second coders,
each shown ONLY the fire-mechanism description of every fatal incident in the
1996-2025 window (municipality, address, incident type, and free-text notes) —
with the construction year and the original label withheld — and asked to apply
the paper's predefined relevance rule. Agreement with the lead author's original
coding is summarised as raw agreement and Cohen's kappa.

    python scripts/blinded_second_coding.py

Keys read at run time from env / Vault-Secrets (never printed).
Author: Magnús Smári Smárason | smarason.is
"""
import os, re, json, glob, pathlib, urllib.request
import pandas as pd

HERE = pathlib.Path(__file__).parent
DATA = HERE.parent / "data"
OUT = HERE.parent / "output" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

structure = pd.read_csv(DATA / "fire_incidents_deaths_structure.csv")
other = pd.read_csv(DATA / "fire_incidents_deaths_other.csv")

# Build the blinded 1996-2025 coding set (construction_year and label withheld)
def recs(df, label):
    df = df[(df.year >= 1996) & (df.year <= 2025)].copy()
    out = []
    for _, r in df.iterrows():
        out.append({
            "id": r["id"][:8],
            "year": int(r["year"]),
            "municipality": r.get("municipality", ""),
            "location": r.get("address", "") if "address" in df.columns else "",
            "incident_type": r.get("incident_type", r.get("type_of_fire", "")),
            "type_of_fire": r.get("type_of_fire", ""),
            "notes": "" if pd.isna(r.get("notes")) else str(r.get("notes", "")),
            "_orig": label,
        })
    return out

records = recs(structure, "structure") + recs(other, "other")
blind = [{k: v for k, v in r.items() if k != "_orig"} for r in records]
orig = [r["_orig"] for r in records]
print(f"Blinded coding set: {len(records)} incidents (1996-2025), "
      f"{orig.count('structure')} structure / {orig.count('other')} other (original).")

RULE = (
    "You are independently coding fatal fire incidents for a study. For EACH incident, "
    "classify it as 'structure' or 'other' using ONLY this predefined rule:\n"
    "- 'structure': the fire originated in or spread THROUGH a building's structure, so that "
    "building-integrated fire safety features (egress, compartmentation, detection, suppression) "
    "were relevant to the fatality.\n"
    "- 'other': the fatality occurred in a ship, vehicle, motorhome, tent, shed, open explosion, "
    "or was a localized ignition in which structural fire spread was NOT the mechanism.\n"
    "You are NOT told the building's construction year; classify purely on the fire mechanism. "
    "Return ONLY a JSON array of objects {\"id\": <id>, \"code\": \"structure\"|\"other\"}, one per incident, no prose."
)


def vault_key(fname, prefix):
    for f in glob.glob(os.path.expanduser(f"~/Vault-Secrets/Apps/{fname}")):
        m = re.search(prefix + r"[A-Za-z0-9\-_]+", pathlib.Path(f).read_text(errors="ignore"))
        if m:
            return m.group(0)
    return None


def code_with(model_name, provider, slug):
    payload_msg = RULE + "\n\nIncidents:\n" + json.dumps(blind, ensure_ascii=False)
    if provider == "anthropic":
        key = vault_key("skuggi-anthropic.md", "sk-ant-")
        body = {"model": slug, "max_tokens": 8000,
                "messages": [{"role": "user", "content": payload_msg}]}
        req = urllib.request.Request("https://api.anthropic.com/v1/messages",
                                     data=json.dumps(body).encode(),
                                     headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                                              "content-type": "application/json"})
        r = json.loads(urllib.request.urlopen(req, timeout=300).read())
        text = "".join(b.get("text", "") for b in r["content"] if b.get("type") == "text")
    else:  # openrouter
        key = vault_key("openrouter-api.md", "sk-or-v1-")
        body = {"model": slug, "max_tokens": 8000, "temperature": 0,
                "messages": [{"role": "user", "content": payload_msg}]}
        req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",
                                     data=json.dumps(body).encode(),
                                     headers={"Authorization": f"Bearer {key}", "content-type": "application/json"})
        r = json.loads(urllib.request.urlopen(req, timeout=300).read())
        text = r["choices"][0]["message"]["content"]
    m = re.search(r"\[.*\]", text, re.S)
    coded = {d["id"]: d["code"] for d in json.loads(m.group(0))}
    return [coded.get(r["id"], "?") for r in blind]


def cohen_kappa(a, b):
    n = len(a)
    cats = ["structure", "other"]
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


CODERS = [("Sonnet 5", "anthropic", "claude-sonnet-5"),
          ("GPT-5.5", "openrouter", "openai/gpt-5.5")]
rows = []
per_incident = {"id": [r["id"] for r in records], "year": [r["year"] for r in records],
                "municipality": [r["municipality"] for r in records], "orig_coding": list(orig)}
col_name = {"Sonnet 5": "claude_sonnet5", "GPT-5.5": "openai_gpt55"}
for name, prov, slug in CODERS:
    try:
        coded = code_with(name, prov, slug)
        per_incident[col_name.get(name, name)] = coded
        po, k = cohen_kappa(orig, coded)
        disagreements = [(records[i]["year"], records[i]["municipality"], orig[i], coded[i])
                         for i in range(len(orig)) if orig[i] != coded[i]]
        print(f"\n[{name}] raw agreement {po*100:.1f}% ({sum(o==c for o,c in zip(orig,coded))}/{len(orig)}), "
              f"Cohen's kappa = {k:.3f}")
        for d in disagreements:
            print(f"    disagree: {d[0]} {d[1]} (orig={d[2]}, {name}={d[3]})")
        rows.append({"coder": name, "n": len(orig), "raw_agreement": round(po, 4),
                     "cohen_kappa": round(k, 3), "n_disagree": len(disagreements)})
    except Exception as e:
        print(f"[{name}] FAILED: {type(e).__name__}: {e}")
pd.DataFrame(rows).to_csv(OUT / "blinded_second_coding.csv", index=False)
# deposit the per-incident codings so the kappa is reproducible offline
# (verify_statistics.py recomputes it from this table; no API keys needed)
if len(per_incident) > 4:
    pd.DataFrame(per_incident).to_csv(DATA / "blinded_recode_codings_1996_2025.csv", index=False)
    print(f"Deposited -> {DATA / 'blinded_recode_codings_1996_2025.csv'}")
print(f"\nSaved -> {OUT / 'blinded_second_coding.csv'}")
