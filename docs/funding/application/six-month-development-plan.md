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
| **M5** Oktober | 155 | Emit, Validierung, FB-1-Manifest, unabhängiger Verifier, Negativtests, ≥ 3 FIM-XSDs (5 als Stretch) | `D5`: validierte Ausgabe; Verifier; 10 Manipulations-Negativtests; Schema-Korpus | Ausgabe validiert gegen dokumentiert normalisierte Schema-Variante; Verifier reproduziert 100 %; alle Negativfälle erkannt |
| **M6** November | 150 | Review-Zeit-Messung, Dokumentation DE/EN, FOSS-Release, Abschlussbericht, Demo | `D6`: Version 0.1; Doku; Messbericht; Demo ohne App/Cloud | Release öffentlich; Tests/Doku vollständig; alle Messwerte und Grenzen dokumentiert |
| **Summe** | **950** | | | |

**Puffer:** In den Monatsstunden sind ca. 8–10 % für Integration, Bugfixes und unerwartete Schema-Effekte enthalten. Es gibt keinen separaten „Reserve-Monat“.

## 3. Alternative 850 h

Falls die verfügbare Kapazität 950 h nicht realistisch trägt, wird der Umfang über eine **eigene, vorab definierte 850-h-Muss-Tabelle** reduziert (§6.2). Tests werden nicht stillschweigend gestrichen; die niedrigeren Muss-Werte werden im Antrag offengelegt.

| Monat | Stunden | Reduktion |
|---|---:|---|
| M1 | 140 | weniger Schema-Korpus im ersten Lauf |
| M2 | 145 | Regelkatalog nur für Kernabschnitte |
| M3 | 145 | Goldstandard ≥ 100 statt ≥ 120 (Stretch 200 entfällt) |
| M4 | 145 | Held-out-Auswertung qualitativ oder ein Dokument |
| M5 | 140 | 8 statt 10 Negativtests; 2 statt 3 XSDs (3 als Stretch) |
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

## 5. Teststrategie und Evaluationsprotokoll

| Ebene | Inhalt | Werkzeug |
|---|---|---|
| Unit | Geometrie, Parser, Regel-Matching, Confidence, Manifest-Hashing | `pytest` |
| Golden Files | Referenz-PDF → erwartete Kandidaten; Held-out-PDF → erwartete Grenzen | versionierte Fixtures |
| Negativ | manipulierte Manifeste, fehlende Dateien, falsche Hashes, Schema-Abweichungen | `pytest` + CLI |
| E2E | `map → review → emit → verify` ohne Netz | CLI in CI |
| Reproduzierbarkeit | zweimaliger Lauf erzeugt identische Hashes/Reports | CI-Vergleich |
| Messung | Precision/Recall, UNKNOWN-Anteil, Review-Zeit, kritische Fehler | Messbericht |

**CI-Regel:** Kein Test benötigt Netzwerk, Cloud, Behördenzugang oder Feldexa. Externe Testpersonen werden nicht in CI simuliert; ihre Messungen werden separat dokumentiert.

### 5.1 Primärmetrik und Zähleinheit

- **Zähleinheit:** ein sichtbares PDF-Feld. Strukturelle Expansionen (1 PDF-Feld → mehrere FIM-Knoten) werden separat als ein Feld mit mehreren Zielen gezählt, nicht als mehrere Felder.
- **Primärmetrik:** Top-1-Zuordnung PDF-Feld → FIM-Datenfeld-ID. Zusätzlich wird Recall@3 (richtige ID unter den ersten drei Kandidaten) berichtet.
- **UNKNOWN:** wird als eigene Klasse berichtet und **nicht** in den Precision-Nenner aufgenommen. Es zählt als sichere Enthaltung, nicht als falsche Zuordnung. Die Coverage wird separat ausgewiesen.
- **Kritische Felder:** Identität (Name, Geburtsdatum, Anschrift, Steuer-ID, IBAN/Konto), Beträge (Einkommen, Miete, Leistungen) und Pflicht-/Ja-Nein-Erklärungen. Die vollständige Liste steht in Anhang A des Messberichts.
- **Stille kritische Fehlzuordnung:** eine kritische Zuordnung, die ohne Review-Gate und ohne UNKNOWN in die Endausgabe gelangt. Vor Review dürfen kritische Felder nur als Kandidat mit Review-Pflicht erscheinen.

### 5.2 Coverage- und UNKNOWN-Grenzen

Damit „alles UNKNOWN“ keine triviale Lösung ist, gelten Mindest-Coverage und Obergrenzen:

| Größe | 950-h-Muss | 850-h-Muss |
|---|---:|---:|
| Nicht-kritische Felder mit automatischem Top-1-Vorschlag (Confidence ≥ Schwelle) | ≥ 60 % | ≥ 50 % |
| UNKNOWN-Anteil bei nicht-kritischen Feldern | ≤ 40 % | ≤ 50 % |
| Kritische Felder ohne Review/Gate in Endausgabe | 0 | 0 |
| Stille kritische Fehlzuordnungen in Endausgabe | 0 | 0 |

Die Confidence-Schwelle wird im Messbericht vor der Auswertung festgelegt und nicht nachträglich an die Ergebnisse angepasst.

### 5.3 Goldstandard und Zweitannotation

- Seed: 30-Feld-Referenzdatensatz (Vorarbeit) + ≥ 90 neue Felder für 950 h (≥ 70 für 850 h).
- **Zweitannotation:** mindestens 30 % der Felder werden von einer zweiten Person unabhängig annotiert; Cohen's κ ≥ 0,80; Abweichungen werden dokumentiert und adjudiziert.
- Die Autorenannotation wird offengelegt. Der Held-out-Test ist die externe Gegenprobe; ohne vollständige Held-out-Annotation wird er als qualitative Grenzprüfung ausgewiesen, nicht als P/R-Zahl.
- Der Regelkatalog wird nicht auf dem Held-out-Dokument entwickelt. Wird das Held-out-Dokument nachträglich einbezogen, wird es als „nicht mehr held-out“ markiert.

### 5.4 Held-out-Dokument

- Ziel: eine Wohngeld-Variante eines anderen Bundeslandes, vollständig annotiert (≥ 50 Felder) oder mindestens qualitativ geprüft.
- Ist das Dokument nicht rechtzeitig/rechtssicher beschaffbar, wird eine synthetische Variante plus ein öffentlich verfügbares Alternativdokument genutzt; die Generalisierbarkeit wird dann ausdrücklich als schwach belegt bezeichnet.
- P/R-Muss gilt für das Referenzdokument; für das Held-out gilt P/R nur, wenn es vollständig annotiert ist. Sonst gilt eine qualitative Grenzprüfung (keine stillen kritischen Fehler, UNKNOWN korrekt).

### 5.5 Review-Zeit

- Ziel: **< 15 s/Feld** für die verbleibende, nicht automatisch zugeordnete Menge.
- Messung mit 2–3 externen Testpersonen, pro Person und pro Feld/Dokument; Setup-Zeit wird getrennt ausgewiesen.
- Bei n = 1 wird das Ergebnis als **Fallstudie** bezeichnet, nicht als belastbare Messung. Der Muss-Bericht enthält die tatsächliche n-Zahl und die Einschränkung.

### 5.6 Schema-Hygiene: Compile ist notwendig, nicht hinreichend

- Gemessen wird nicht nur „kompiliert“, sondern auch der **Semantikverlust**: entfernte `type`-Attribute, `xs:string`-Stubs, entfernte Regex-Anker, fehlende Constraints.
- Jede Normalisierung erzeugt ein maschinenlesbares Diff-/Reparaturprotokoll. Muss: keine stillschweigende Entfernung required/constraint-relevanter Informationen; jede Ausnahme wird dokumentiert.
- 6-Monats-Muss: **≥ 3** amtliche FIM-XSDs normalisiert und kompiliert; **5** ist Stretch/Second-Stage-Ziel. Die Spec nennt ≥ 5; diese Abweichung wird offen begründet (M5-Entlastung). **Reihenfolge:** Verifier und Emit zuerst, XSD-Korpus danach; JSON-Schema-Pfad ist primär, XSD-Normalisierung der Legacy-Baustein.

### 5.7 Manifest und Trust Model

- Das FB-1-Manifest ist ein **Audit-Artefakt**: Es macht Inkonsistenzen und versehentliche Veränderungen sichtbar.
- Es ist **kein** Schutz gegen einen Angreifer, der PDF und Manifest konsistent neu berechnet. Ohne Signatur, externen Timestamp oder Trust Anchor wird **keine** Manipulationsfestigkeit behauptet.
- Optionale Härtung: Detached Signature/pyHanko oder externer Timestamp, falls im Zeitbudget; sonst als „nicht implementiert“ dokumentieren.
- Das Manifest enthält Tool-/Library-Versionen, Kanonisierungsregeln, Schema-Hash und Review-Hashes.

## 6. Messbare Abnahmekriterien

### 6.1 950-h-Muss

1. End-to-End-Lauf auf Referenz-PDF und mindestens einem Held-out-Dokument (vollständig annotiert oder qualitativ geprüft).
2. Goldstandard **≥ 120 annotierte Felder** (Seed 30 + ≥ 90 neue), stratifiziert nach Feldklassen.
3. Precision **≥ 0,90**, Recall **≥ 0,85** (Top-1) auf dem Referenzdokument; Held-out separat, sofern vollständig annotiert.
4. Coverage/UNKNOWN-Grenzen aus §5.2 eingehalten.
5. **0 stille kritische Fehlzuordnungen** in der Endausgabe; kritische Felder nur mit Review/Gate.
6. Schema-Hygiene: **≥ 3** FIM-XSDs normalisiert/kompiliert mit Semantikverlust-Protokoll; 5 als Stretch.
7. Manifest-Verifier reproduziert 100 % der Artefakte; **≥ 10** Negativfälle für Inkonsistenzen erkannt.
8. Review-Zeit mit 2–3 externen Testpersonen gemessen; n und Einschränkungen dokumentiert.
9. FOSS-Release der selbst erstellten Code-/Dokumentationsergebnisse, Dokumentation DE/EN, reproduzierbare Tests.

### 6.2 850-h-Muss (eigene Tabelle)

1. End-to-End-Lauf auf Referenz-PDF und einem Held-out-Dokument (qualitativ oder vollständig annotiert).
2. Goldstandard **≥ 100 annotierte Felder** (Seed 30 + ≥ 70 neue).
3. Precision **≥ 0,85**, Recall **≥ 0,80** (Top-1) auf dem Referenzdokument.
4. Coverage/UNKNOWN-Grenzen aus §5.2 eingehalten.
5. 0 stille kritische Fehlzuordnungen.
6. Schema-Hygiene: **≥ 2** FIM-XSDs mit Semantikverlust-Protokoll; 3 als Stretch.
7. Verifier 100 % Reproduktion; **≥ 8** Negativfälle.
8. Review-Zeit mit mindestens 2 externen Personen oder n=1 als Fallstudie, klar gelabelt.
9. FOSS-Release, Dokumentation, Tests.

### 6.3 Stretch (nicht Muss)

≥ 200 Felder, Precision ≥ 0,95, Recall ≥ 0,90, ≥ 5 FIM-XSDs. Das sind die Messziele aus Spec §6; sie werden **nicht** als „Spec-Stretch“ umetikettiert. Die Anwendung setzt für den 6-Monats-Kern bewusst niedrigere Muss-Werte und begründet die Abweichung mit der Ein-Personen-Kapazität und der M5-Entlastung.

### 6.4 Berichtsregel bei Nichterreichung

Wird ein Muss-Kriterium nicht erreicht, wird das im Abschlussbericht als Abweichung mit Ist-Wert, Ursache und Konsequenz dokumentiert. Es wird **nicht** stillschweigend abgesenkt und **nicht** als „Stretch“ umdeklariert.

## 7. Technische Risiken und Fallbacks

| Risiko | Wirkung | Fallback |
|---|---|---|
| Keine lizenzsichere Felddetektionsbasis | Detection muss eigenständig gebaut werden | Regelbasierte Detektion für born-digital PDFs; Scans explizit außerhalb des Scopes |
| FIM-Schemata weiterer Verfahren sind defekt | Schema-Korpus blockiert | 3 XSDs als Muss, 5 als Stretch; Defekte und Semantikverlust dokumentieren |
| Held-out-PDF nicht beschaffbar/rechtlich unklar | Generalisierbarkeit schwach belegt | Synthetische Variante + öffentlich verfügbares Alternativdokument; qualitativ labeln, Grenze berichten |
| Kritische Fehlzuordnung | Vertrauensverlust | Hard Gates für Identität/Betrag/Pflichtfeld; `UNKNOWN`-Default; doppelte Annotation |
| Externe Testpersonen fallen aus | RF4 nicht belastbar | mindestens eine externe Person + separate Autor-Messung; n=1 als Fallstudie labeln |
| Zeitüberlauf | Muss-Ziele gefährdet | Stretch zuerst streichen; Kern (M1–M5) priorisieren; 850-h-Variante nur als bewusste Owner-Entscheidung vor Einreichung |
| Scope-Drift Richtung Produkt-UI | Fördergegenstand verwässert | schriftliche Scope-Grenze in README/ADR; UI bleibt außerhalb |

**Regel:** Fallbacks dürfen Muss-Kriterien nicht stillschweigend absenken. Sie ändern die **Berichtsform** (z. B. qualitativ statt P/R), nicht das zugesagte Ziel. Die 850-h-Variante ist kein Fallback, sondern eine vorab gewählte Alternative mit eigener Muss-Tabelle.

## 8. Dokumentation und Veröffentlichung

- `README.md`: Problem, Scope, Installation, CLI-Beispiele, Grenzen.
- `docs/architecture.md`: Pipeline, Datenfluss, Vertrauensgrenzen.
- `docs/fb-1-manifest.md`: Format, Kanonisierung, Hashes, Verifikation, Trust-Model-Grenzen.
- `docs/rule-catalog.md`: Regelformat, Versionierung, Belegbeispiele.
- `docs/evaluation.md`: Goldstandard, Metriken, Held-out, Fehlerkatalog, Zweitannotation.
- `docs/schema-normalization.md`: Reparaturprotokoll, Semantikverlust, Diff.
- `docs/integration.md`: Bibliothek/CLI für Dritte; keine Feldexa-Abhängigkeit.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, Lizenz (Owner-Entscheidung; Empfehlung Apache-2.0).
- Release `v0.1.0` mit reproduzierbarem Testlauf und Hash.

**FOSS-Umfang:** Nur selbst erstellte Code-/Dokumentationsergebnisse werden unter eine OSI-Lizenz gestellt. Amtliche PDFs/XSDs werden nicht redistribuiert, sondern per URL/Hash referenziert, solange die Rechte nicht geklärt sind.

## 9. Abgrenzung und Förderbedingungen

- **Vor Förderbeginn:** keine Modulimplementierung; nur Forschung/Dokumentation. Die bestehende Forschung ist Vorarbeit.
- **Während der Förderung:** eigenständige Codebasis, keine Feldexa-Änderungen, keine RepairProbe-Änderungen.
- **Feldexa 2.0:** vorgesehene erste Anwendung, aber **nicht integriert** und **nicht Teil des Förderumfangs**. Eine spätere Integration zählt nicht als externe Integration in der Second Stage.
- **Nach der Förderung:** FOSS-Veröffentlichung der eigenen Ergebnisse, Projektbericht, Wartungsplan (Second Stage oder Anschlussfinanzierung).
- **Keine Zusage:** Behördenakzeptanz, Rechtsgültigkeit einer Einreichung, flächendeckende Formularunterstützung.

## 10. Zeitliche Machbarkeit — kritische Prüfung

Der Plan ist für eine Einzelperson ambitioniert, aber machbar, weil:

- der Scope auf **eine Verfahrensfamilie** und **born-digital PDFs** begrenzt ist;
- die Detektion regelbasiert und nicht von einem trainierten Modell abhängig ist;
- die vorhandene Forschung (Referenzfall, 30-Feld-Datensatz, Spezifikation) als Startpunkt dient, aber nicht als Förderleistung zählt;
- der 6-Monats-Kern gegenüber Spec §6 (200/0,95/0,90/5 XSD) auf 120/0,90/0,85/3 XSD abgesenkt und die Abweichung offen begründet ist;
- M5 entlastet wird: Verifier vor XSD-Korpus, 3 XSDs als Muss, 5 als Stretch/Second Stage;
- jeder Monat ein prüfbares Artefakt liefert und der Umfang bei 850 h über eine eigene Muss-Tabelle reduziert wird.

**Nicht machbar wäre:** viele Verfahren, Scans/OCR, eine fertige UI, Behördenintegration und ein vollständiges Regelwerk für alle Länder. Diese Punkte sind ausdrücklich außerhalb des Förderumfangs.
