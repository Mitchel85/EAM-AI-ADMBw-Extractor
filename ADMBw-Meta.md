# ADMBw-MDG-Extraktion — Metadaten

- **MDG-Datei:** `tests/fixtures/NAFv4-ADMBw-MDG-2026.05.xml`
- **MDG-Version (aus Dateiname):** NAFv4-ADMBw-MDG-2026.05.xml
- **Extrahiert am:** – (ohne Zeitstempel)
- **Stereotype im Katalog:** 318 (nur UMLProfiles)
- **Davon im Modell nutzbar (mit AppliesTo):** 293
- **Davon mit Metatype:** 313 (5 ohne: ActualServiceSpecificationRole, BWRequirement, ElementCatalogue, ServiceExchange, SuccessorOf)
- **Abstrakte Stereotype (🔒, nicht instanziierbar):** 44
  - davon ohne AppliesTo (reine Platzhalter): 25
  - davon mit AppliesTo (fachlich zu spezialisieren): 19
- **Stereotype mit Topologie-Regeln:** 203 (davon 133 vollständig mit Quelle und Ziel)
- **Viewpoints:** 52 (DiagramProfile ohne Diagramm-Artefakt „Business Process“)
- **Property-Typen:** 27
- **Stereotyp-Tags:** 225 an 66 Stereotypen

Die Markierung 🔒 steht in der Stereotyp-Tabelle und in `admbw-stereotypes.json` (`abstract: true`). Ein Modell darf kein Element mit einem abstrakten Stereotyp tragen.

Zählweise: Die MDG enthält die Stereotype in drei getrennten Bereichen —
318 Deklarationen in UMLProfiles (das Modellprofil, der eigentliche Katalog),
271 Elemente in UIToolboxes (125 UI-Toolbox-Seiten, keine Modell-Stereotype) und
53 Einträge in DiagramProfile (52 Viewpoints + 1 Diagramm-Artefakt „Business Process“).
Der Katalog zählt ausschließlich die UMLProfiles-Stereotype; Toolbox-Seiten
und Viewpoints werden nicht (bzw. separat) extrahiert.

Diese Dateien wurden automatisch aus der offiziellen ADMBw-MDG-Technologie erzeugt
(https://www.bundeswehr.de/de/organisation/ausruestung-baainbw/vergabe/methode-architektur).
Bei einem MDG-Update einfach den Parser erneut ausführen.