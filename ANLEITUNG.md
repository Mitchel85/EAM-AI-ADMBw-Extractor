# EAM-AI-ADMBw-Extractor — In 5 Minuten

**Was macht er?** Aus Architektur-Prosa (Text, Stichpunkte, Dokumente) macht er ADMBw-konforme **Stereotype, Beziehungen und Viewpoints** — als Mermaid-Diagramme und Tabellen.

**Was brauchst du?** Ein LLM mit Knowledge/RAG-Funktion (z. B. Open-WebUI, ChatGPT mit Dateianhang, Claude).

## Schritt 1 — Dateien holen (1 Minute)

Lade aus dem Repository:
- `system_prompt.md`
- die vier `ADMBw-Knowledge-*.md`-Dateien

## Schritt 2 — Modell einrichten (2 Minuten)

**Open-WebUI:**
1. Neues Modell anlegen → Inhalt von `system_prompt.md` als **System Prompt** einfügen.
2. Die vier Knowledge-Dateien hochladen und mit dem Modell verknüpfen.

**Andere LLMs:** System-Prompt als erste Nachricht senden, danach die vier Knowledge-Dateien anhängen mit dem Hinweis: „Beachte diese Regeln bei allen folgenden Antworten."

## Schritt 3 — Prosa einschicken (1 Minute)

Architekturtext eingeben. Der Extraktor stellt genau **eine** Frage — wähle:

| Option | Wann |
|---|---|
| Viewpoints modellieren | Du willst passende NAFv4-Sichten |
| ADMBw-Modell | Du willst Prosa → Stereotyp-Mapping |
| Metamodell (generisch) | Du willst ein Typ-Modell der Domäne |
| Stakeholder-Concern | Du willst eine spezifische Frage beantworten |

## Schritt 4 — Ergebnis prüfen (1 Minute)

- Stimmen die Stereotype (keine erfunden, keine 🔒-abstrakten)?
- Sind alle Prosa-Entitäten erfasst?
- Steht in der **Topologie-Validierungstabelle** für jede Kante eine Regelzeile mit PASS (client = Quelle, supplier = Ziel)?
- Stimmt die Zählung („Topologie-Prüfung: X/Y Kanten PASS")?

Dann in **Sparx EA** nachmodellieren.

## Häufige Fragen

**Kann der Extraktor direkt in Sparx EA importieren?**
Nein — er liefert Modellierungs-Vorlagen (Diagramme + Tabellen). Die Umsetzung im Modell übernimmst du manuell (oder automatisiert mit dem [EAM-AI-ADMBw-Script-Maker](https://github.com/Mitchel85/EAM-AI-ADMBw-Script-Maker)).

**Woher kommen die Regeln?**
Aus der offiziellen ADMBw-MDG der Bundeswehr, extrahiert vom [EAM-ADMBw-MDG-Parser](https://github.com/Mitchel85/EAM-ADMBw-MDG-Parser) (Stand 2026.05: 318 Katalog-Stereotype — davon 293 nutzbar und 44 abstrakt —, 133 vollständige Topologie-Regeln, 52 Viewpoints).

**Was ist die PDF?**
Die offizielle Bw-Dokumentation — nur als Referenz, nicht für Knowledge nötig.

**Kostet das etwas?**
Nein. Die Dateien sind lokal und Open Source; du brauchst nur ein LLM deiner Wahl.
