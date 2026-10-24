> **Archiviert (24.10.2026).** Dieses Repository wird nicht mehr weiterentwickelt.
> Die aktive Quelle ist [Mitchel85/EAM-Platform](https://github.com/Mitchel85/EAM-Platform)
> (ein MDG-Leser, eine Wissensbasis, alle Auslieferungen).
> Der letzte Stand bleibt als Tag `pre-consolidation-2026-10` lesbar.

# EAM-AI-ADMBw-Extractor

![Status](https://img.shields.io/badge/Status-Active-success)
![Standard](https://img.shields.io/badge/Standard-ADMBw%2FNAFv4-blue)
![MDG](https://img.shields.io/badge/Regelbasis-MDG%202026.05-orange)
![Plattform](https://img.shields.io/badge/Platform-OpenWebUI%20%2F%20jedes%20LLM-purple)

**KI-gestützter Assistent, der aus natürlichsprachlichen Architekturtexten ADMBw-konforme Stereotype, Beziehungen und Viewpoints extrahiert** — als Mermaid-Diagramme und Mapping-Tabellen zum Nachmodellieren in Sparx Systems Enterprise Architect.

> ⚠️ **Keine importierbaren Dateien.** Der Output ist eine Modellierungshilfe für das manuelle Nachmodellieren in Enterprise Architect.

---

## 🚀 Ablauf (4 Optionen)

Der Extraktor stellt ZU BEGINN genau eine Frage:

| # | Option | Ergebnis |
|---|--------|----------|
| 1 | **Viewpoints modellieren** | KI schlägt Viewpoints vor, modelliert sie nacheinander (Metamodell + Instanz-Diagramm) |
| 2 | **ADMBw-Modell** | Prosa-Elemente direkt auf ADMBw-Stereotype gemappt (Mapping-Tabelle + Diagramm) |
| 3 | **Metamodell (generisch)** | Übertragbares Typ-Modell einer Architekturdomäne — keine Instanzen |
| 4 | **Stakeholder-Concern** | Fokussierte Modellierung eines spezifischen Erkenntnisinteresses |

Die KI wählt den jeweils besten Mermaid-Diagrammtyp selbst (`classDiagram`, `graph TD`, `sequenceDiagram`, `stateDiagram`, `gantt`, …).

---

## 📚 Wissensbasis (automatisch aus der offiziellen MDG)

Vier MDG-generierte Knowledge-Dateien, erzeugt vom [EAM-ADMBw-MDG-Parser](https://github.com/Mitchel85/EAM-ADMBw-MDG-Parser) aus der offiziellen MDG-Technologie der Bundeswehr (Stand **2026.05**), plus eine kuratierte Connector-Übersicht:

| Datei | Inhalt |
|-------|--------|
| `ADMBw-Knowledge-Stereotypes.md` | **318 Katalog-Stereotype** (293 nutzbar · 44 abstrakt 🔒, davon 19 nur fachlich zu spezialisieren); Toolboxen/Artefakte sind nicht enthalten |
| `ADMBw-Knowledge-Viewpoints.md` | **52 Viewpoints** mit MDG-Beschreibung (keine erfundenen Properties) |
| `ADMBw-Knowledge-Topology.md` | **133 vollständige Kanten-Regeln** (Quelle/Ziel über client/source/end[0] bzw. supplier/target/end[1]) + 70 reine Rollen-Beschränkungen |
| `ADMBw-Knowledge-TagTypes.md` | **27 Property-Typen** (Tagged-Value-Definitionen) |
| `ADMBw-Knowledge-Connectors.md` | EA-Metatypen + Connector-Übersicht (kuratiert) |
| `ADMBw-Stereotypes.json` | Derselbe Katalog maschinenlesbar: `abstract`, `parents`, `concreteDescendants` — Grundlage der Subtyp-Auflösung |
| `ADMBw-Aliases.json` | Schreibvarianten (`PropertySetGeneralisation` → `PropertySetGeneralization`, `ServiceSpecificationGeneralization` → `ServiceGeneralization`) |

> Bei einem MDG-Update der Bundeswehr werden diese Dateien neu generiert — nicht von Hand gepflegt.
>
> **KB-Sync-Status (2026-10-20): aktuell.** Vier MDG-Dateien neu erzeugt aus `eam-mdg-parser` (`ea0765f`) mit Abstrakt-Markierung und Subtyp-Auflösung; Tag-Typen und Hashes in `checks/deterministic-checks.json`.

---

## ✅ Validierung (maschinenprüfbar)

Jeder Output weist **jede Kante einzeln** gegen die Topologie-KB aus — statt pauschaler Selbstbehauptung:

| Kante | source_stereotype | connector | target_stereotype | Topologie-Regel (client→supplier) | Metaklasse | PASS/FAIL |
|---|---|---|---|---|---|---|
| … | OperationalActivity | ActivitySupportsService | ServiceSpecification | OperationalActivity→ServiceSpecification | Realisation | PASS |

- PASS bei exaktem Namens-Match **oder** wenn ein Ende ein konkreter Subtyp eines erlaubten abstrakten Endpunkts ist; die Auflösung wird ausgewiesen
- Ein Element oder Konnektor mit 🔒-Stereotyp ist immer **FAIL**
- Abschlusszeile: „Topologie-Prüfung: X/Y Kanten PASS" — nur nach Einzelprüfung jeder Kante
- Element-Checks: Stereotype nutzbar (kein 🔒), Metaklasse = AppliesTo, keine erfundenen Namen, Subtyp-Auflösung belegt
- Viewpoint-Konformität wird **nicht behauptet**, weil die MDG 2026.05 keine erlaubten Elemente je Viewpoint definiert

**Eiserne Regeln:**
- ❌ Keine eigenen Stereotype erfinden
- ❌ Abstrakte Stereotype (🔒) nie direkt verwenden — konkreten Subtyp wählen

---

## 🔧 Einfache Anleitung (Open-WebUI)

1. **Modell anlegen:** Inhalt von `system_prompt.md` ins Feld **System Prompt** kopieren.
2. **Knowledge einbinden:** Die vier MDG-generierten `ADMBw-Knowledge-*.md`-Dateien plus `ADMBw-Knowledge-Connectors.md` hochladen und mit dem Modell verknüpfen.
3. **Prosa eingeben:** Deinen Architekturtext (z. B. Dokument, Textauszug, Stichpunkte) an das Modell schicken.
4. **Option wählen:** Auf die eine Einstiegsfrage antworten (Viewpoints / ADMBw-Modell / Metamodell / Stakeholder-Concern).
5. **Ergebnis prüfen:** Mermaid-Diagramme + Mapping-Tabellen auf Vollständigkeit und Korrektheit gegenprüfen, dann in Enterprise Architect nachmodellieren.

> 💡 Die Knowledge-Dateien stammen aus der **MDG 2026.05**. Bundeswehr-Dokumente werden bewusst **nicht** mitgeliefert — die Quelle der Wahrheit ist die Seite „Methode Architektur“ beim BMVg.

---

## ✅ Deterministische Prüfung

`python3 checks/verify.py` prüft ohne LLM:

- KB-Statistiken (318/293/44/133/70/52/27) und SHA-256-Hashes der vier MDG-KB-Dateien
- Topologie-Lesart („client = Quelle") und 🔒-Markierungen vorhanden
- Abstrakt-Auflösung: `concreteDescendants` im JSON, Abschnitt „Abstrakte Endpunkte“ in der Topologie
- Prompt/README enthalten die korrigierten Zahlen (keine 443/203/53-Reste)

---

## 📦 Repository

| Datei | Zweck |
|-------|-------|
| `system_prompt.md` | System-Prompt (Kernlogik, 4 Modi + Kanten-Validierung + Few-Shot) |
| `ADMBw-Knowledge-Stereotypes.md` | Stereotyp-Katalog (MDG-generiert) |
| `ADMBw-Knowledge-Viewpoints.md` | Viewpoint-Regeln (MDG-generiert) |
| `ADMBw-Knowledge-Topology.md` | Topologie-Regeln (MDG-generiert) |
| `ADMBw-Knowledge-TagTypes.md` | Property-Typen (MDG-generiert) |
| `ADMBw-Knowledge-Connectors.md` | Konnektor-Regeln (kuratiert) |
| `ADMBw-Stereotypes.json` | Maschinenlesbarer Katalog inkl. `concreteDescendants` |
| `ADMBw-Aliases.json` | Alt-Schreibweisen → kanonischer Name |
| `checks/verify.py` | Deterministische Prüfungen (ohne LLM) |

---

---

## Rechtliches

Der EAM-AI-ADMBw-Extractor ist ein unabhängiges Drittanbieter-Produkt. Es ist nicht mit der Sparx Systems Pty Ltd verbunden, wird von dieser nicht unterstützt und nicht gesponsert. „Sparx Systems“ und „Enterprise Architect“ sind Marken oder eingetragene Marken der Sparx Systems Pty Ltd.

**Autor:** Michael Estel (mit KI-Agent) · Teil der **EAM-Toolfamilie** — [github.com/Mitchel85](https://github.com/Mitchel85)

## Rechtliches

EAM Extractor ist ein unabhängiges Drittanbieter-Werkzeug. Es ist nicht mit der Sparx Systems Pty Ltd
verbunden, wird von dieser nicht unterstützt und nicht gesponsert. „Sparx Systems" und
„Enterprise Architect" sind Marken oder eingetragene Marken der Sparx Systems Pty Ltd.
Alle weiteren Marken sind Eigentum ihrer jeweiligen Inhaber.
