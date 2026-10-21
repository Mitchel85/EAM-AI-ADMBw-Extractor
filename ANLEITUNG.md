# EAM-AI-ADMBw-Extractor — In 5 Minuten

**Was macht er?** Aus Architektur-Prosa (Text, Stichpunkte, Dokumente) macht er ADMBw-konforme **Stereotype, Beziehungen und Viewpoints** — als Mermaid-Diagramme und Tabellen.

**Was brauchst du?** Ein LLM mit Knowledge/RAG-Funktion (z. B. Open-WebUI, ChatGPT mit Dateianhang, Claude).

## Schritt 1 — Dateien holen (1 Minute)

Lade aus dem Repository:
- `system_prompt.md`
- die vier `ADMBw-Knowledge-*.md`-Dateien
- `ADMBw-Stereotypes.json` und `ADMBw-Aliases.json` (für die Auflösung abstrakter Typen)

## Schritt 2 — Modell einrichten (2 Minuten)

**Open-WebUI:**
1. Neues Modell anlegen → Inhalt von `system_prompt.md` als **System Prompt** einfügen.
2. Die Knowledge-Dateien und beide JSON-Dateien hochladen und mit dem Modell verknüpfen.

**Andere LLMs:** System-Prompt als erste Nachricht senden, danach die Knowledge- und JSON-Dateien anhängen mit dem Hinweis: „Beachte diese Regeln bei allen folgenden Antworten."

## Schritt 3 — Prosa einschicken (1 Minute)

Architekturtext eingeben. Der Extraktor stellt genau **eine** Frage — wähle:

| Option | Wann |
|---|---|
| Viewpoints modellieren | Du willst passende NAFv4-Sichten |
| ADMBw-Modell | Du willst Prosa → Stereotyp-Mapping |
| Metamodell (generisch) | Du willst ein Typ-Modell der Domäne |
| Stakeholder-Concern | Du willst eine spezifische Frage beantworten |

## Schritt 4 — Ergebnis prüfen (1 Minute)

- Stimmen die Stereotype (keine erfunden, kein Element mit 🔒)?
- Sind abstrakte Endpunkte in Regeln korrekt auf konkrete Subtypen aufgelöst (Spalte „Auflösung")?
- Sind alle Prosa-Entitäten erfasst?
- Steht in der **Topologie-Validierungstabelle** für jede Kante eine Regelzeile mit PASS (client = Quelle, supplier = Ziel)?
- Stimmt die Zählung („Topologie-Prüfung: X/Y Kanten PASS")?

Dann in Enterprise Architect nachmodellieren.

## Häufige Fragen

**Kann der Extraktor direkt in Enterprise Architect importieren?**
Nein — er liefert Modellierungs-Vorlagen (Diagramme + Tabellen). Die Umsetzung im Modell übernimmst du manuell (oder automatisiert mit dem [EAM-AI-ADMBw-Script-Maker](https://github.com/Mitchel85/EAM-AI-ADMBw-Script-Maker)).

**Was sind abstrakte Stereotype?**
44 der 318 Stereotype sind Platzhalter (🔒). Sie dürfen nie als Element oder Konnektor verwendet werden. Erlaubt eine Regel einen solchen Typ, gilt sie für alle konkreten Subtypen — z. B. `ResourcePerformer` für `CapabilityConfiguration`, `PhysicalResource`, `Software`; `{REQUIREMENT}` wird als `FunctionalRequirement` oder `NonfunctionalRequirement` modelliert. Die Liste steht in `ADMBw-Stereotypes.json` unter `concreteDescendants`.

**Woher kommen die Regeln?**
Aus der offiziellen ADMBw-MDG der Bundeswehr, extrahiert vom [EAM-ADMBw-MDG-Parser](https://github.com/Mitchel85/EAM-ADMBw-MDG-Parser) (Stand 2026.05: 318 Katalog-Stereotype — davon 293 nutzbar und 44 abstrakt —, 133 vollständige Topologie-Regeln, 52 Viewpoints).

**Gibt es die Bw-Dokumentation als PDF dazu?**
Nein. Bundeswehr-Dokumente liegen bewusst nicht im Repository — die Quelle der Wahrheit ist die Seite „Methode Architektur“ beim BMVg. Die Knowledge-Dateien sind aus der MDG 2026.05 erzeugt.

**Kostet das etwas?**
Nein. Die Dateien sind lokal und Open Source; du brauchst nur ein LLM deiner Wahl.
