# Sechs-Monats-Entwicklungsplan — FormBridge

**Förderzeitraum:** 01.06.2027–30.11.2027 · **Basis:** 950 h · **Alternative:** 850 h · **Status:** Planungshypothese, keine Förderzusage
**Grundsatz:** Der Fördergegenstand ist das eigenständige FormBridge-Modul. Vorhandene Forschung (Prior-Art-Audit, Referenzfall, 30-Feld-Datensatz, Spezifikation) ist **Vorarbeit** und wird nicht als Förderleistung abgerechnet. Es wird **kein** Feldexa-Produktcode verwendet oder verändert.

## 1. Förderfähiger Kern

FormBridge wird eine lokal ausführbare Software-Infrastruktur mit:

1. PDF-Textlage- und Layoutanalyse für **born-digital** Behörden-PDFs (keine Scans/OCR im Förderzeitraum).
2. Feldkandidaten mit Seite, Koordinaten, sichtbarem Label und Zustand.
3. Regelbasierter Zuordnung zu versionierten FIM-Datenfeldern, inklusive Confidence und explizitem `UNKNOWN`.
4. Menschlichem Review-Gate mit versionierten Entscheidungen.
5. Provenienz-Manifest `FB-1` und unabhängigem Verifier.
6. Validierter strukturierter Ausgabe und Abdeckungsbericht.
7. Bibliothek, CLI, Tests, Dokumentation und FOSS-Release.

**Nicht Fördergegenstand:** Endnutzer-UI, Scans/OCR-Qualität, produktiver Behördenanschluss, Feldexa-Integration, ProofLayer-Implementierung, Betrieb einer Cloud.

## 2. Monatsplan (950 h)

| Monat | Stunden | Fokus | Deliverable | Akzeptanzkriterium |
|---|---:|---|---|---|
| **M1** Juni | 160 | Fundament, PDF-Textlage, Schema-Laden/Hash, FB-1-Spezifikation, Normalisierungswerkzeug + CI | `D1`: lauffähiges CLI-Grundgerüst; FB-1-Spec v1; CI-Normalisierungslauf für S00000159 | CLI startet ohne Netz; Schema-Hash und Normalisierungsprotokoll werden erzeugt; ein Testlauf ist reproduzierbar |
| **M2** Juli | 165 | Felderkennung, Abschnittssegmentierung, Regelkatalog v1, Kandidaten-Engine, Confidence/UNKNOWN | `D2`: End-to-End-Kandidaten auf Referenz-PDF; Regelkatalog v1 | mindestens 30 Felder erkannt; jeder Kandidat hat Zustand/Confidence; unklare Fälle sind `UNKNOWN` |
| **M3** August | 160 | Goldstandard, Review-CLI, Codelisten, Precision/Recall-Baseline, externe Testpersonen | `D3`: Goldstandard ≥ 120 Felder (Stretch 200); Review-CLI; Baseline-Bericht | Baseline auf Referenzdokument gemessen; Review-Entscheidungen versioniert; 2–3 externe Testpersonen gewonnen |
| **M4** September | 160 | Abschnitts-Disambiguierung, Hard Gates für Identität/Betrag/Pflichtfeld, Held-out-PDF, Fehleranalyse | `D4`: Disambiguierungs-Messung; Held-out-Auswertung; Fehlerkatalog | Mindestprecision/Recall erreicht oder Abweichung dokumentiert; 0 stille kritische Fehlzuordnungen |
| **M5** Oktober | 155 | Emit, Validierung, FB-1-Manifest, unabhängiger Verifier, Negativtests, ≥ 5 FIM-XSDs | `D5`: validierte Ausgabe; Verifier; 10 Manipulations-Negativtests; Schema-Korpus | Ausgabe validiert gegen normalisiertes XSD; Verifier reproduziert 100 %; alle Negativfälle erkannt |
| **M6** November | 150 | Review-Zeit-Messung, Dokumentation DE/EN, FOSS-Release, Abschlussbericht, Demo | `D6`: Version 0.1; Doku; Messbericht; Demo ohne App/Cloud | Release öffentlich; Tests/Doku vollständig; alle Messwerte und Grenzen dokumentiert |
| **Summe** | **950** | | | |

**Puffer:** In den Monatsstunden sind ca. 8–10 % für Integration, Bugfixes und unerwartete Schema-Effekte enthalten. Es gibt keinen separaten „Reserve-Monat“.

## 3. Alternative 850 h

Falls die verfügbare Kapazität 950 h nicht realistisch trägt, wird der Umfang **nicht** durch Streichung von Tests, sondern durch Verschiebung des Stretch-Ziels reduziert:

| Monat | Stunden | Reduktion |
|---|---:|---|
| M1 | 140 | weniger Schema-Korpus im ersten Lauf |
| M2 | 145 | Regelkatalog nur für Kernabschnitte |
| M3 | 145 | Goldstandard ≥ 100 statt ≥ 120 (Stretch 200 entfällt) |
| M4 | 145 | Held-out-Auswertung mit einem statt zwei Dokumenten |
| M5 | 140 | 8 statt 10 Negativtests; 4 statt 5 XSDs |
| M6 | 135 | Doku/Release unverändert, weniger Demo-Ausarbeitung |
| **Summe** | **850** | **Kern bleibt: lokale Pipeline, UNKNOWN, Review, Manifest, Verifier, FOSS** |

**Finanzielle Wirkung:** siehe [budget-final.md](budget-final.md). 850 h → 42.500 € PK, 2.125 € GK, 44.625 € G, **42.393,75 € F**, 2.231,25 € EA.

## 4. Meilenstein-Abhängigkeiten

```text
M1 Fundament ──► M2 Kandidaten ──► M3 Goldstandard/Review ──► M4 Disambiguierung
                                                              │
                                                              ▼
                                                   M5 Emit/Validate/Verify ──► M6 Release
```

- M3 kann nicht vor M2 abgeschlossen werden (Goldstandard braucht Kandidatenformat).
- M5 kann nicht vor M3 abgeschlossen werden (Verifier braucht Review-Entscheidungen).
- M6 ist ohne M5 nicht releasefähig.

## 5. Teststrategie

| Ebene | Inhalt | Werkzeug |
|---|---|---|
| Unit | Geometrie, Parser, Regel-Matching, Confidence, Manifest-Hashing | `pytest` |
| Golden Files | Referenz-PDF → erwartete Kandidaten; Held-out-PDF → erwartete Grenzen | versionierte Fixtures |
| Negativ | manipulierte Manifeste, fehlende Dateien, falsche Hashes, Schema-Abweichungen | `pytest` + CLI |
| E2E | `map → review → emit → verify` ohne Netz | CLI in CI |
| Reproduzierbarkeit | zweimaliger Lauf erzeugt identische Hashes/Reports | CI-Vergleich |
| Messung | Precision/Recall, UNKNOWN-Anteil, Review-Zeit, kritische Fehler | Messbericht |

**CI-Regel:** Kein Test benötigt Netzwerk, Cloud, Behördenzugang oder Feldexa. Externe Testpersonen werden nicht in CI simuliert; ihre Messungen werden separat dokumentiert.

## 6. Messbare Abnahmekriterien

**Mindestziel (Muss):**

1. End-to-End-Lauf auf dem Referenz-PDF und mindestens einem Held-out-Dokument.
2. Goldstandard **≥ 120 annotierte Felder** (Seed 30 + ≥ 90 neue).
3. Feld-Precision **≥ 0,90**, Recall **≥ 0,85** auf dem Goldstandard; Messwerte getrennt für Referenz und Held-out.
4. **0 stille kritische Fehlzuordnungen** in Identität/Betrag/Pflichtfeld; alle unsicheren Fälle `UNKNOWN` + Review.
5. Schema-Hygiene: ≥ 5 amtliche FIM-XSDs normalisiert und kompiliert, mit vollständigen Reparaturprotokollen.
6. Manifest-Verifier reproduziert 100 % der Artefakte; ≥ 10 Manipulations-Negativfälle erkannt.
7. Review-Zeit mit 2–3 externen Testpersonen gemessen; Median und Ausreißer dokumentiert.
8. FOSS-Release, Dokumentation DE/EN, reproduzierbare Tests.

**Stretch-Ziel (Kann, aus Spezifikation §6):** ≥ 200 Felder, Precision ≥ 0,95, Recall ≥ 0,90. Wird das Stretch-Ziel nicht erreicht, werden die tatsächlichen Werte und Fehlergrenzen veröffentlicht; die Muss-Ziele bleiben unverändert.

## 7. Technische Risiken und Fallbacks

| Risiko | Wirkung | Fallback |
|---|---|---|
| Keine lizenzsichere Felddetektionsbasis | Detection muss eigenständig gebaut werden | Regelbasierte Detektion für born-digital PDFs; Scans explizit außerhalb des Scopes |
| FIM-Schemata weiterer Verfahren sind defekt | Schema-Korpus blockiert | Normalisierer als eigenständiges Ergebnis; Korpus auf ≥ 3 statt 5 erweitern, Defekte dokumentieren |
| Held-out-PDF nicht beschaffbar/rechtlich unklar | Generalisierbarkeit schwach belegt | Synthetische Variante + öffentlich verfügbares Alternativdokument; Grenze im Bericht |
| Kritische Fehlzuordnung | Vertrauensverlust | Hard Gates für Identität/Betrag/Pflichtfeld; `UNKNOWN`-Default; doppelte Annotation |
| Externe Testpersonen fallen aus | RF4 nicht belastbar | mindestens eine externe Person + separate Autor-Messung; Einschränkung dokumentieren |
| Zeitüberlauf | Muss-Ziele gefährdet | Stretch zuerst streichen; Kern (M1–M5) priorisieren; 850-h-Variante |
| Scope-Drift Richtung Produkt-UI | Fördergegenstand verwässert | schriftliche Scope-Grenze in README/ADR; UI bleibt außerhalb |

## 8. Dokumentation und Veröffentlichung

- `README.md`: Problem, Scope, Installation, CLI-Beispiele, Grenzen.
- `docs/architecture.md`: Pipeline, Datenfluss, Vertrauensgrenzen.
- `docs/fb-1-manifest.md`: Format, Kanonisierung, Hashes, Verifikation.
- `docs/rule-catalog.md`: Regelformat, Versionierung, Belegbeispiele.
- `docs/evaluation.md`: Goldstandard, Metriken, Held-out, Fehlerkatalog.
- `docs/integration.md`: Bibliothek/CLI für Dritte; keine Feldexa-Abhängigkeit.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, Lizenz (Owner-Entscheidung; Empfehlung Apache-2.0).
- Release `v0.1.0` mit reproduzierbarem Testlauf und Signatur/Hash.

## 9. Abgrenzung und Förderbedingungen

- **Vor Förderbeginn:** keine Modulimplementierung; nur Forschung/Dokumentation. Die bestehende Forschung ist Vorarbeit.
- **Während der Förderung:** eigenständige Codebasis, keine Feldexa-Änderungen, keine RepairProbe-Änderungen.
- **Nach der Förderung:** FOSS-Veröffentlichung, Projektbericht, Wartungsplan (Second Stage oder Anschlussfinanzierung).
- **Keine Zusage:** Behördenakzeptanz, Rechtsgültigkeit einer Einreichung, flächendeckende Formularunterstützung.

## 10. Zeitliche Machbarkeit — kritische Prüfung

Der Plan ist für eine Einzelperson ambitioniert, aber machbar, weil:

- der Scope auf **eine Verfahrensfamilie** und **born-digital PDFs** begrenzt ist;
- die Detektion regelbasiert und nicht von einem trainierten Modell abhängig ist;
- die vorhandene Forschung (Referenzfall, 30-Feld-Datensatz, Spezifikation) als Startpunkt dient, aber nicht als Förderleistung zählt;
- die Muss-Ziele gegenüber dem Spec-Stretch (200/0,95/0,90) auf 120/0,90/0,85 abgesenkt sind;
- jeder Monat ein prüfbares Artefakt liefert und der Umfang bei 850 h zuerst am Stretch gekürzt wird.

**Nicht machbar wäre:** viele Verfahren, Scans/OCR, eine fertige UI, Behördenintegration und ein vollständiges Regelwerk für alle Länder. Diese Punkte sind ausdrücklich außerhalb des Förderumfangs.
