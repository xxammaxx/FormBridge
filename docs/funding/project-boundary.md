# Projektgrenze: Bestandsarbeit vs. potenzieller Fördergegenstand

**Datum:** 13.11.2026 (erstmals festgelegt im Feldexa-2.0-Repo, Issue #167; hierher migriert) · **Status:** verbindlich für dieses Repository

Diese Datei trennt nachweisbar, was bereits existiert, was bis Förderbeginn unabhängig entsteht, und was — nur bei Förderung — neuer Gegenstand wäre. Sie verhindert die Umdeklaration vorhandener Arbeit als künftige Förderleistung.

## A. Bestandsarbeit (existiert bereits, vor Bewerbung/Förderbeginn)

| Leistung | Ort / Datum | Status |
|---|---|---|
| Feldexa-2.0-Produktentwicklung (Flutter/Dart-App, T0xx-Tasks, MVP-Spezifikation) | `xxammaxx/Feldexa_2.0`, läuft unabhängig weiter | reguläre Produktarbeit, **kein** Fördergegenstand |
| Prior-Art-Recherche Runden I–IV (dokumentbasiert) | Feldexa_2.0 Issue #167, 13.11.2026 | abgeschlossen |
| Prior-Art-**Quellcode-Audit** (13 Projekte, geklont, SHAs, file:line-Belege) | Feldexa_2.0 `docs/research-167-prior-art-audit` @ `cb122fe…`, PR #168, 13.11.2026 | abgeschlossen, hierher migriert |
| Referenzfall Fürth-PDF ↔ FIM S00000159v1.4 (Download, Hashes, Parsing, Defekt-Nachweis 170 Fehler, Normalisierung, Instanz-Validierung) | dito | abgeschlossen, hierher migriert |
| 30-Felder-Referenzdatensatz (synthetisch) | dito | abgeschlossen, hierher migriert |
| Innovationsbewertung, Modul-Spezifikation, Förder-Machbarkeit, Bewerbungsbausteine, Entscheidungsbericht | dito; 2 unabhängige Reviews eingearbeitet | abgeschlossen, hierher migriert |
| Dieses Repository (Setup, Doku-Migration, Validierung) | `xxammaxx/FormBridge`, 13.11.2026 | abgeschlossen — **Recherche-/Infrastrukturarbeit, keine Modul-Implementierung** |

## B. Potenzieller Fördergegenstand (existiert NICHT; nur bei Förderung, unter Bedingungen)

Das in [`docs/research/technical-specification.md`](../research/technical-specification.md) spezifizierte Modul (Erkennung, Zuordnungs-Engine, Review-Gate, Provenienz-Manifest FB-1, Validierung, Verifier, Schema-Hygiene) **wurde nicht implementiert** und wird vor einem Förderbescheid nicht implementiert. Sechs-Monatsplan und Abnahmekriterien siehe Spezifikation §6–7. Bedingungen B1–B6 siehe [`decision-report.md`](decision-report.md).

## C. Explizite Verbotsliste bis zu einem Förderbescheid

1. Keine produktiven oder prototypischen Quellcodedateien in diesem Repository (auch keine "Beispiel"-Implementierungen).
2. Keine Behauptung, irgendein Forschungsziel sei erreicht; alle Formulierungen bleiben Forschungsziele.
3. Keine Verwendung von Feldexa-Produktcode (auch nicht "als Ausgangsbasis").
4. Keine Vorab-Erledigung von Meilensteinen aus Spezifikation §7 (diese würden sonst als Förderleistungen verloren).
5. Kein Merge von Feldexa_2.0 PR #152/#168 durch FormBridge-Arbeit; keine Änderung an RepairProbe oder Issue #165.

## D. Nachführungspflicht

Entwickelt der Maintainer vor Förderbeginn (unabhängig von dieser Recherche) Funktionalität, die mit dem geplanten Modul überschneidet, ist §A/B hier und die Spezifikation transparent nachzuführen (Vorgabe aus Prototype-Fund-Handbuch 2026: klare Abgrenzung, "Verbesserung der bestehenden Software" ist nicht förderfähig). Protokollierung: Änderungen dieser Datei mit Datum + Anlass.

## E. Provenienz der migrierten Dokumente

Alle unter `docs/research/` und `docs/funding/` liegenden Analysen wurden am **13.11.2026** im Feldexa-2.0-Repository erstellt (Commit `cb122fe2f96a8f5cbde2f075e0b6529342caf676`, PR #168) und am gleichen Tag hierher überführt. Inhaltliche Änderungen bei der Migration beschränken sich auf: Pfade/Dateinamen, Entfernung der redistribuierten XSD-Ableitung (Lizenz unklar; Verfahren dokumentiert in reference-case-wohngeld.md §Reproduktion), Ergänzungen um diese Grenzdokumentation. Keine Forschungsergebnisse wurden inhaltlich verändert.

**Abgrenzungs-Offenlegung (Validierung 13.11.2026, Review B/B1):** Die Ein-Schema-Normalisierung von S00000159V1.4 (Defektnachweis + validierende Instanz) ist **bereits erledigte Forschungsvorarbeit** (§A) und wird im Förderplan (Spec M1, RF2) **nicht** als Förderleistung wiederholt — förderfähig wäre nur das deterministische Werkzeug, die CI-Automatisierung und der ≥5-Schemata-Korpus. Diese Trennung ist im Antrag explizit auszuweisen.
