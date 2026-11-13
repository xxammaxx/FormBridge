# FormBridge — Kurzbeschreibung

## In fünf Sätzen

FormBridge ist eine geplante freie Software-Infrastruktur für statische, nicht interaktive deutsche Behördenformulare. Sie erkennt Formularfelder in born-digitalen PDFs und schlägt nachvollziehbare Zuordnungen zu versionierten FIM-Datenfeldern vor. Unsichere Fälle werden ausdrücklich als `UNKNOWN` markiert und menschlich geprüft. Ein versioniertes Provenienz-Manifest und ein unabhängiger Verifier machen Quelle, Schema-Version, Koordinaten und Review-Entscheidungen prüfbar. FormBridge ist als Bibliothek und CLI für Entwickler*innen freier Verwaltungssoftware angelegt; eine Endnutzer-App oder ein Behördenanschluss ist nicht Teil des Vorhabens.

## Ein Absatz

FormBridge adressiert den Medienbruch bei amtlichen PDF-Formularen: Viele Vordrucke sind nicht ausfüllbar und enthalten keine maschinenlesbaren Felddefinitionen. Gleichzeitig existieren mit FIM versionierte Verwaltungsdatenfelder, aber keine offene, prüfbare Brücke vom sichtbaren PDF-Feld dorthin. FormBridge soll diese Brücke als lokale Open-Source-Infrastruktur bauen: Feldkandidaten mit Koordinaten, regelbasierte FIM-Zuordnung mit Confidence und `UNKNOWN`, menschliches Review, ein hashbasiertes Provenienz-Manifest und ein unabhängiger Verifier. Der Prototyp bleibt bewusst auf eine Verfahrensfamilie und born-digital PDFs begrenzt; Scans, Produkt-UI und Behördenintegration sind spätere Schritte.

## Abgrenzung

- **Nicht** die Feldexa-App, **nicht** ProofLayer, **nicht** RepairProbe.
- **Kein** Produktcode im Forschungsstand; die Pipeline ist spezifiziert, nicht implementiert.
- **Keine** Behauptung von Behördenakzeptanz oder Rechtsgültigkeit.
