#!/usr/bin/env python3
"""Deterministische Prüfungen für EAM-AI-ADMBw-Extractor (ohne LLM).

Prüft ohne LLM-Aufruf:
 1. KB-Statistiken (Stereotypes/Topology/Viewpoints/Connectors) gegen die dokumentierten Zahlen
 2. SHA-256-Hashes der vier MDG-KB-Dateien (Stereotypes, Topology, Viewpoints, TagTypes)
 3. Topologie-Lesart korrigiert (client = Quelle, supplier = Ziel)
 4. 🔒-Markierungen der 44 abstrakten Stereotype vorhanden
 5. Prompt/README/ANLEITUNG enthalten die korrigierten Zahlen; keine 443/203/53-Altbehauptungen
 6. Prompt: maschinenprüfbare Kanten-Validierungstabelle + Few-Shot + Leerinput-Regel

Exit-Code 0 = alle Checks PASS, 1 = mindestens ein FAIL.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail and not ok else ""))


def parse_stereotypes(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 6 or cells[1] == "Stereotype" or not cells[1]:
            continue
        rows.append((cells[1], cells[2], cells[3], cells[4], cells[5] if len(cells) > 5 else ""))
    return rows


def parse_topology(text):
    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 5 or cells[1] in ("", "Stereotype"):
            continue
        rows.append((cells[1], cells[2], cells[3], cells[4] if len(cells) > 4 else ""))
    return rows


def main():
    st_text = (ROOT / "ADMBw-Knowledge-Stereotypes.md").read_text(encoding="utf-8")
    tp_text = (ROOT / "ADMBw-Knowledge-Topology.md").read_text(encoding="utf-8")
    vp_text = (ROOT / "ADMBw-Knowledge-Viewpoints.md").read_text(encoding="utf-8")
    tt_text = (ROOT / "ADMBw-Knowledge-TagTypes.md").read_text(encoding="utf-8")
    co_text = (ROOT / "ADMBw-Knowledge-Connectors.md").read_text(encoding="utf-8")

    # ---------- 1. KB-Statistiken ----------
    st = parse_stereotypes(st_text)
    toolbox = [r for r in st if r[3] == "ToolboxPage"]
    abstract = [r for r in st if "🔒" in r[4]]
    junk = [r for r in st if r[0] == "L2-Operational Constraints"]
    usable = [r for r in st if r[3] not in ("", "ToolboxPage")]
    check("Stereotypes: 318 Tabellenzeilen", len(st) == 318, f"ist {len(st)}")
    check("Stereotypes: 0 ToolboxPage-Einträge", len(toolbox) == 0, f"ist {len(toolbox)}")
    check("Stereotypes: 44 abstrakte Stereotype (🔒)", len(abstract) == 44, f"ist {len(abstract)}")
    check("Stereotypes: 0 Nicht-Stereotype/Artefakte", len(junk) == 0, f"ist {len(junk)}")
    check("Stereotypes: 293 nutzbare", len(usable) == 293, f"ist {len(usable)}")
    check("Stereotypes: Header nennt 318 und 44 abstrakt", "318 Stereotype" in st_text and "44 abstrakt" in st_text)

    tp = parse_topology(tp_text)
    complete = [r for r in tp if r[1] and r[2]]
    roles_only = [r for r in tp if not (r[1] and r[2])]
    check("Topology: 203 Zeilen", len(tp) == 203, f"ist {len(tp)}")
    check("Topology: 133 Regeln mit beiden Enden", len(complete) == 133, f"ist {len(complete)}")
    check("Topology: 70 reine Rollen-Zeilen", len(roles_only) == 70, f"ist {len(roles_only)}")
    check("Topology: Lesart 'Quelle = client/source/end[0]/informationSource'",
          "client, source, end[0].role oder informationSource" in tp_text)
    check("Topology: Spaltenköpfe Quelle/Ziel normalisiert",
          "| Stereotype | Erlaubte Quellen (client/source/end[0]) | Erlaubte Ziele (supplier/target/end[1]) | Weitere Rollen |" in tp_text)

    vp_headings = [l for l in vp_text.splitlines() if l.startswith("## ")]
    check("Viewpoints: 52 Überschriften", len(vp_headings) == 52, f"ist {len(vp_headings)}")
    check("Viewpoints: 'Business Process'-Artefakt entfernt",
          not any("Business Process" in h for h in vp_headings))

    tt_rows = [l for l in tt_text.splitlines() if l.startswith("|")][2:]
    check("TagTypes: 27 Property-Typen", len(tt_rows) == 27, f"ist {len(tt_rows)}")
    check("TagTypes: Header nennt 27 Property-Typen", "27 Property-Typen" in tt_text)

    check("Connectors: Dependency (100)", "**Dependency** (100)" in co_text)
    check("Connectors: Class (68)", "**Class** (68)" in co_text)
    check("Connectors: Activity (6)", "**Activity** (6)" in co_text)
    check("Connectors: Connector (3)", "**Connector** (3)" in co_text)

    # ---------- 2. Hashes ----------
    hashes = {}
    for f in ["ADMBw-Knowledge-Stereotypes.md", "ADMBw-Knowledge-Topology.md",
              "ADMBw-Knowledge-Viewpoints.md", "ADMBw-Knowledge-TagTypes.md"]:
        data = (ROOT / f).read_bytes()
        hashes[f] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    check("Hashes: vier MDG-KB-Dateien berechnet", len(hashes) == 4)

    # ---------- 3.-6. Prompt & Doku ----------
    prompt = (ROOT / "system_prompt.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    anleitung = (ROOT / "ANLEITUNG.md").read_text(encoding="utf-8")

    docs = prompt + "\n" + readme + "\n" + anleitung
    check("Doku: keine Alt-Behauptung '443 eindeutige'", "443 eindeutige" not in docs)
    check("Doku: keine Alt-Behauptung '203 Beziehungsregeln'", "203 Beziehungsregeln" not in docs)
    check("Doku: keine Alt-Behauptung '53 Viewpoints'", "53 Viewpoints" not in docs)
    check("Doku: '8/8 ✓' entfernt", "8/8" not in prompt)
    check("Prompt: Topologie-Lesart dokumentiert", "Quelle = client/source/end[0].role/informationSource" in prompt)
    check("Prompt: Kanten-Validierungstabelle (source_stereotype/connector/target_stereotype/PASS/FAIL)",
          all(k in prompt for k in ["source_stereotype", "connector", "target_stereotype", "PASS/FAIL"]))
    check("Prompt: Zählung 'X/Y Kanten PASS' statt Pauschal-Claim",
          "Topologie-Prüfung: **X/Y Kanten PASS**" in prompt)
    check("Prompt: Few-Shot enthalten", "FEW-SHOT" in prompt and "Topologie-Prüfung: 3/3 Kanten PASS" in prompt)
    check("Prompt: Leerinput-Regel enthalten", "LEERER / UNLESBARER INPUT" in prompt)
    check("README: korrigierte Zahlen (318/293/133/52)",
          all(k in readme for k in ["318 Katalog-Stereotype", "293 nutzbar", "133 vollständige", "52 Viewpoints"]))
    check("ANLEITUNG: korrigierte Zahlen", "133 vollständige Topologie-Regeln, 52 Viewpoints" in anleitung)
    check("README: PDF-Version von MDG getrennt",
          ("Version 2025.10" in readme) and ("MDG 2026.05" in readme) and ("nicht** inhaltsgleich" in readme))
    check("README: KB-Sync auf Parserstand 2026-10-19", "KB-Sync-Status (2026-10-19): PENDING" not in readme)
    check("README: keine PENDING-Formulierung", "Parser-Nachlieferung ausstehend" not in (readme + anleitung + prompt))

    # ---------- Ergebnis ----------
    report = {
        "kb": {
            "stereotypes": {"rows": len(st), "toolbox": len(toolbox), "abstract": len(abstract),
                            "usable": len(usable), "junk": len(junk)},
            "topology": {"rows": len(tp), "complete_rules": len(complete), "roles_only": len(roles_only)},
            "viewpoints": len(vp_headings),
            "hashes": hashes,
        },
        "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in results],
        "all_pass": all(o for _, o, _ in results),
    }
    out = ROOT / "checks" / "deterministic-checks.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nReport: {out}")
    print(f"Gesamt: {sum(1 for _, o, _ in results if o)}/{len(results)} PASS")
    sys.exit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
