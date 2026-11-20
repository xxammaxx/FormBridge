# FormBridge — Kurzbeschreibung

## Kurzfassung

FormBridge ist eine geplante freie Software-Infrastruktur für statische, nicht interaktive deutsche Behördenformulare. Sie erkennt Formularfelder in born-digitalen PDFs und schlägt nachvollziehbare Zuordnungen zu versionierten FIM-Datenfeldern vor. Parallel zur Modulentwicklung prüft ein optionaler Vergleich, ob direkt berechnete LoRA-Adapter kleine, ausschließlich lokal ausgeführte Modelle auf vorhandener Hardware für die semantische Zuordnung verbessern. Der Pflicht-Regelkern bleibt ohne Modell nutzbar. Eigene daraus entstehende Analyse-, Adapter- und Testwerkzeuge sollen offen veröffentlicht werden, damit auch andere Digitalisierungsprojekte lokale Modelle gezielt und überprüfbar anpassen können. Unsichere Fälle werden ausdrücklich als `UNKNOWN` markiert und menschlich geprüft. Ein versioniertes Provenienz-Manifest und ein unabhängiger Verifier machen Quelle, Schema-Version, Koordinaten und Review-Entscheidungen prüfbar. FormBridge ist als Bibliothek und CLI für Entwickler*innen freier Verwaltungssoftware angelegt; eine Endnutzer-App oder ein Behördenanschluss ist nicht Teil des Vorhabens.

## Ein Absatz

FormBridge adressiert den Medienbruch bei amtlichen PDF-Formularen: Viele Vordrucke sind nicht ausfüllbar und enthalten keine maschinenlesbaren Felddefinitionen. Gleichzeitig existieren mit FIM versionierte Verwaltungsdatenfelder, aber im begrenzten Prior-Art-Audit wurde keine vollständige offene, prüfbare Zuordnungskette vom sichtbaren PDF-Feld dorthin gefunden. FormBridge soll diese Brücke als lokale Open-Source-Infrastruktur bauen: Feldkandidaten mit Koordinaten, regelbasierte FIM-Zuordnung mit Confidence und `UNKNOWN`, menschliches Review, ein hashbasiertes Provenienz-Manifest und ein unabhängiger Verifier. Ein kleiner lokaler Modell-/LoRA-Vergleich für mehrdeutige Felder ist optional und nur bei nachgewiesenem Mehrwert für die Kernpipeline vorgesehen. Entstehende eigene Forschungswerkzeuge und dokumentierte Negativergebnisse sollen für weitere freie Digitalisierungsprojekte nachnutzbar sein. Der Prototyp bleibt bewusst auf eine Verfahrensfamilie und born-digital PDFs begrenzt; Scans, Produkt-UI und Behördenintegration sind spätere Schritte.

## Abgrenzung

- **Nicht** die Feldexa-App, **nicht** ProofLayer, **nicht** RepairProbe.
- **Kein** Produktcode im Forschungsstand; die Pipeline ist spezifiziert, nicht implementiert.
- **Keine** Behauptung von Behördenakzeptanz oder Rechtsgültigkeit.

**Nachweis:** Lokale Modell- und Adaptertests bei gesperrtem Netzzugang, versionierte Artefakte und reproduzierbare Messberichte; [Strategie und Vorarbeiten](local-llm-evidence-strategy-2026-11-20.md). Kein Modell- oder Ressourcenvorteil vor eigener Messung behauptet.
