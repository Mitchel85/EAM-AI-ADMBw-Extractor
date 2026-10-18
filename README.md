# EAM-AI-ADMBw-Extractor

![Status](https://img.shields.io/badge/Status-Active-success)
![Standard](https://img.shields.io/badge/Standard-ADMBw%2FNAFv4-blue)
![MDG](https://img.shields.io/badge/Regelbasis-MDG%202026.05-orange)
![Plattform](https://img.shields.io/badge/Platform-OpenWebUI%20%2F%20jedes%20LLM-purple)

**KI-gestützter Assistent, der aus natürlichsprachlichen Architekturtexten ADMBw-konforme Stereotype, Beziehungen und Viewpoints extrahiert** — als Mermaid-Diagramme und Mapping-Tabellen zum Nachmodellieren in Sparx EA.

> ⚠️ **Keine importierbaren Dateien.** Der Output ist eine Modellierungshilfe für das manuelle Nachmodellieren in Sparx EA.

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

Vier Knowledge-Dateien, erzeugt vom [EAM-ADMBw-MDG-Parser](https://github.com/Mitchel85/EAM-ADMBw-MDG-Parser) aus der offiziellen MDG-Technologie der Bundeswehr (Stand **2026.05**):

| Datei | Inhalt |
|-------|--------|
| `ADMBw-Knowledge-Stereotypes.md` | **443 eindeutige Stereotype** mit AppliesTo |
| `ADMBw-Knowledge-Viewpoints.md` | **53 Viewpoints** mit Properties |
| `ADMBw-Knowledge-Topology.md` | **203 Beziehungsregeln** (Source → Connector → Target) |
| `ADMBw-Knowledge-Connectors.md` | EA-Metatypen + Connector-Übersicht (kuratiert) |

> Bei einem MDG-Update der Bundeswehr werden diese Dateien neu generiert — nicht von Hand gepflegt.

---

## ✅ Validierung (8-fach)

Jeder Output wird gegen alle vier Knowledge-Dateien geprüft:

| # | Check | Quelle |
|---|-------|--------|
| 1 | AppliesTo: Stereotype auf korrekte Metaklasse? | Stereotypes |
| 2 | Viewpoint-Konformität: Nur erlaubte Elemente? | Viewpoints |
| 3 | Konnektor-Metatyp korrekt? | Connectors |
| 4 | Metaconstraint: Source→Target erlaubt? | Topology |
| 5 | Vollständigkeit: Alle Prosa-Entitäten erfasst? | Prosa-Dokument |
| 6 | Namenskonsistenz über alle Artefakte | — |
| 7 | Metamodell: ALLE Typen + Beziehungen im Diagramm? | Viewpoints + Topology |
| 8 | Topologie-Richtung: Jede Kante Source→Connector→Target? | Topology |

**Eiserne Regeln:**
- ❌ Keine eigenen Stereotype erfinden
- ❌ Abstrakte Basisklassen (🔒) nie direkt verwenden

---

## 🔧 Einfache Anleitung (Open-WebUI)

1. **Modell anlegen:** Inhalt von `system_prompt.md` ins Feld **System Prompt** kopieren.
2. **Knowledge einbinden:** Die vier `ADMBw-Knowledge-*.md`-Dateien hochladen und mit dem Modell verknüpfen.
3. **Prosa eingeben:** Deinen Architekturtext (z. B. Dokument, Textauszug, Stichpunkte) an das Modell schicken.
4. **Option wählen:** Auf die eine Einstiegsfrage antworten (Viewpoints / ADMBw-Modell / Metamodell / Stakeholder-Concern).
5. **Ergebnis prüfen:** Mermaid-Diagramme + Mapping-Tabellen auf Vollständigkeit und Korrektheit gegenprüfen, dann in Sparx EA nachmodellieren.

> 💡 Die beiliegende PDF-Dokumentation **nicht** in Knowledge laden — die MD-Dateien sind token-effizienter und inhaltlich identisch.

---

## 📦 Repository

| Datei | Zweck |
|-------|-------|
| `system_prompt.md` | System-Prompt (Kernlogik, 4 Modi + 8 Validierungs-Checks) |
| `ADMBw-Knowledge-Stereotypes.md` | Stereotyp-Katalog (MDG-generiert) |
| `ADMBw-Knowledge-Viewpoints.md` | Viewpoint-Regeln (MDG-generiert) |
| `ADMBw-Knowledge-Topology.md` | Topologie-Regeln (MDG-generiert) |
| `ADMBw-Knowledge-Connectors.md` | Konnektor-Regeln (kuratiert) |
| `Dokumentation-ADMBw-v2025.10.pdf` | Offizielle Bw-Dokumentation (Referenz) |

---

**Autor:** Michael Estel (mit KI-Agent) · Teil der **EAM-Toolfamilie** — [github.com/Mitchel85](https://github.com/Mitchel85)
