# Innovations- und Wettbewerbsprüfung — FormBridge

**Stand:** 13.11.2026 · **Grundlage:** [Prior-Art-Audit](../../research/prior-art-audit.md), [Innovationsbewertung](../../research/innovation-assessment.md), [Referenzfall](../../research/reference-case-wohngeld.md), [technische Spezifikation](../../research/technical-specification.md)
**Zweck:** Belegte Aussagen von Hypothesen trennen. Keine weltweite Erstmaligkeitsbehauptung.

## 1. Das Problem, präzise gefasst

Statische, nicht interaktive Behörden-PDFs enthalten sichtbare Felder, aber keine maschinenlesbaren Felddefinitionen. Wer sie digital verarbeiten will, muss Felder manuell nachbauen oder Werte aus einem PDF in ein anderes System übertragen. Gleichzeitig existieren mit FIM versionierte Verwaltungsdatenfelder und mit FITKO eine Schema-Infrastruktur. Die offene Frage ist, ob eine **lokale, prüfbare Kette** vom sichtbaren PDF-Feld zu einer versionierten FIM-ID praktisch tragfähig ist — inklusive Unsicherheit, menschlicher Freigabe und Provenienz.

## 2. Was bereits existiert (belegt)

| Projekt / Baustein | Was es tut | Was es für FormBridge bedeutet | Beleg |
|---|---|---|---|
| **Formularagent** (MPL-2.0) | Migriert vorhandene Formulardefinitionen (FIM-XML, form.io, Excel) in valides Formular-JSON; Migrationsbericht | Kein PDF-Eingang, keine PDF-Koordinaten; Unsicherheit nur kategorial | Quellcode-Audit, Commit `4085c46` (13.11.2026) |
| **KIWo / OpenForm** (Apache-2.0) | Extrahiert Werte mit Cloud-KI, Review-UI | Kein FIM-Bezug, keine Feldkoordinaten, Cloud-Anbindung | Quellcode-Audit, Commit `c40bb34` |
| **CommonForms** | Erkennt Formularfelder, macht PDFs ausfüllbar | Keine Lizenzdatei im geprüften Stand; keine FIM-Semantik, keine Provenienz | Quellcode-Audit |
| **FITKO / FIM** | Versionierte Schemata, XDF/XSD, Schema-Repository, **FIM-Portal-Datenschema-Konverter (XDF2/XDF3 ↔ JSON Schema/XSD)** | Infrastruktur und Konverter, aber keine PDF→FIM-Zuordnung; der Konverter repariert nicht das bereits veröffentlichte defekte S00000159-XSD | fimportal.de/arbeitsmittel + /releases, 13.11.2026 |
| **Öffentliche Formularserver / kommerzielle IDP** (Bundesverwaltungsamt FMS, Landesformularserver, Adobe/ABBYY/Azure/LlamaParse) | Formularstrecken, Dokumentenerkennung/-extraktion | **DOC_ONLY, nicht im Quellcode-Audit**; keine geprüfte offene PDF→FIM-Kette | Dokumentenprüfung, 13.11.2026 |
| **GSA pdf-filler** | Füllt auch nicht interaktive PDFs über Koordinaten | PDF-Overlay ist Stand der Technik, keine semantische Zuordnung | Quellcode-Audit |
| **SurveyJS AI Form Response Extractor** | Extrahiert Scans/PDFs in JSON, lokal via Ollama möglich | „PDF zu JSON" allein ist nicht neu; keine FIM-Versionierung/Provenienz; die AI-Extractor-Zeile ist **nicht** durch den geklonten `survey-pdf`-Audit gedeckt | Quellcode-/Produktdokumentation |
| **MACH Formsolutions / OZG-Formulardesigner** | Kommerzielle/offene Formularstrecken und Antragsassistenten | **DOC_ONLY**; bestehende Formularprozesse, keine automatische PDF→FIM-Zuordnung; FormBridge setzt bei vorgegebenen alten PDFs an | Dokumentenprüfung |
| **C2PA, pyHanko, PDF-Signaturwerkzeuge** | Provenienz-/Signaturprüfung | **Verwandte Standards, nicht im FormBridge-Plan integriert**; FormBridge prüft Feld-/PDF-Konsistenz, keine amtliche Authentizität | Standarddokumentation |

**Wichtig:** Die Tabelle ist eine Prüfung von **13 Projekten (Quellcode, wo verfügbar; zwei dokumentbasiert)**, keine vollständige Weltmarktübersicht. „Nicht gefunden" heißt nicht „existiert nicht".

## 3. Die geprüfte Lücke

FormBridge kombiniert sieben Elemente in einer Kette:

1. statisches Behörden-PDF (born-digital, Textlage),
2. Feldkandidaten mit Koordinaten und sichtbarem Label,
3. versionierte FIM-Datenfeld-IDs,
4. explizite Confidence und `UNKNOWN` statt stillschweigender Entscheidung,
5. menschliches Review-Gate,
6. Provenienz-Manifest mit Hashes, Regelversion und Review-Entscheidungen,
7. unabhängiger Verifier und eine gegen die dokumentiert normalisierte Schema-Variante validierte Ausgabe.

**Behauptung:** In den 13 geprüften Projekten wurde diese **Kette** nicht gefunden. Einzelne Elemente sind vorhanden; die Kombination und die Prüfbarkeit sind die Forschungshypothese.

**Warum nicht auf ihnen aufbauen?** Formularagent hat keinen PDF-Eingang; KIWO hat keinen FIM-Bezug und keine Feldkoordinaten; CommonForms hat keine Lizenz und keine Semantik; FITKO liefert Schemata und Konverter, aber keine PDF→FIM-Zuordnung. Kein geprüfter Baustein liefert PDF-Koordinaten, FIM-Versionierung, UNKNOWN-Gate und Provenienz zugleich.

**Keine Behauptung:** weltweite Erstmaligkeit, vollständige Abdeckung aller Formulare, Behördenakzeptanz, Rechtsgültigkeit, Produktreife.

## 4. Abgrenzung im Detail

| Naheliegender Einwand | Antwort |
|---|---|
| „CommonForms erkennt Felder doch schon." | Ja, für ausfüllbare PDFs. FormBridge braucht zusätzlich FIM-Semantik, Koordinaten, Unsicherheit, Review und Provenienz; CommonForms hat im geprüften Stand keine Lizenzdatei und keine FIM-Zuordnung. |
| „FITKO liefert JSON-Schemata, wozu XSD?" | FormBridge nutzt den JSON-Pfad, wo vorhanden. Die XSD-Normalisierung ist ein eigenständiger Beitrag für XSD-basierte Fachverfahren; das amtliche S00000159-XSD ist nachweislich nicht standardkonform kompilierbar (170 Parser-Fehler). |
| „Das ist nur pdftotext + Regeln." | Der Kern ist die messbare Disambiguierung (mehrere „Name"-Kontexte, Beträge, Codelisten), das UNKNOWN-Gate, das Manifest und der Verifier — nicht ein einzelner Extraktionsschritt. |
| „Ein LLM löst das in einem Wochenende." | Ein LLM kann Vorschläge machen, aber keine reproduzierbare, prüfbare Zuordnung mit Schema-Version, Koordinaten und Review-Historie garantieren. FormBridge ist bewusst regelbasiert und lokal; ein lokales ML-Modell ist optional. |
| „C2PA/pyHanko machen Provenienz." | Sie prüfen Signaturen/Provenienz von Artefakten, nicht die semantische Beziehung PDF-Feld → FIM-ID → Review-Entscheidung. FormBridge wiederverwendet Hash-/Signaturstandards, erfindet sie nicht neu. |

## 5. Was während der Förderung getestet wird (Hypothesen)

| Hypothese | Messung | Status vor Förderung |
|---|---|---|
| H1: Abschnitts-Kontext löst Mehrdeutigkeiten ausreichend auf | Precision/Recall, UNKNOWN-Anteil, kritische Fehler | **UNGETESTET**; Referenzfall zeigt 7 Kontext-Mehrdeutigkeiten |
| H2: XSD-Normalisierung ist über ≥ 3 FIM-Schemata (Stretch 5) reproduzierbar | Compile-Erfolg, Semantikverlust-Protokoll | **TEILWEISE BELEGT** für S00000159 (170 Fehler), Korpus offen |
| H3: Manifest + Verifier machen Inkonsistenzen sichtbar | Reproduzierbarkeit, 10 Negativfälle | **SPEZIFIZIERT**, nicht implementiert; kein Tamper-Proof-Anspruch |
| H4: Review-Aufwand bleibt tragbar | Median-Zeit je Feld mit 2–3 externen Personen | **UNGEMESSEN** |

## 6. Gesellschaftlicher Nutzen — belegt vs. plausibel

**Belegt:**
- 50 % der Befragten erledigten ihr letztes Anliegen vollständig offline; 24 % nutzten einen Medienbruch; 68 % der Medienbrüche waren unfreiwillig (eGovernment MONITOR 2026, D21/TUM, Erhebung April/Mai 2026, n = 5.725; https://initiatived21.de/uploads/03_Studien-Publikationen/eGovernment-MONITOR/2026/D21-eGovMon2026.pdf, abgerufen 13.11.2026).
- FIM ist ein offizieller Standard für Verwaltungsdaten; das FIM-Portal betreibt Schemata und einen Datenschema-Konverter (XDF2/XDF3/JSON Schema/XSD). Der Konverter repariert jedoch kein bereits veröffentlichtes defektes XSD und liefert keine PDF→FIM-Zuordnung.
- Das amtliche S00000159-XSD ist im geprüften Stand nicht standardkonform kompilierbar (170 betroffene Elemente; 169 xmllint-Meldungen zu D2; libxml2/xmllint).

**Wichtig zur Reichweite:** Die D21-Zahlen belegen Medienbrüche allgemein, **nicht** die Prävalenz statischer PDFs als Ursache. Der Referenzfall belegt einen konkreten Fall; die Verallgemeinerung ist eine Forschungshypothese. **RF2** ist daher die Reparatur/deterministische Normalisierung bereits veröffentlichter defekter XSDs mit Semantikverlust-Protokoll — nicht die Behauptung, es fehle ein allgemeiner Schema-Konverter.

**Plausibel, aber nicht gemessen:**
- FormBridge reduziert repetitive Arbeit in Softwareprojekten, die Verwaltungsformulare digitalisieren.
- Darauf aufbauende Anwendungen reduzieren Medienbrüche und manuelle Nacherfassung.
- Lokale Verarbeitung senkt Datenschutzrisiken gegenüber Cloud-Diensten.

**Nicht behauptet:**
- FormBridge senkt Behördenkosten um X Prozent.
- FormBridge beschleunigt Genehmigungen.
- FormBridge ist rechtssicher oder von Behörden akzeptiert.

## 7. Quellen und Prüfstatus

| Quelle | Verwendung | Status |
|---|---|---|
| Prior-Art-Audit, 13 Projekte, Clone-SHAs; Quellcode, wo verfügbar, zwei dokumentbasiert | Wettbewerbsabgrenzung | VERIFIED (gescoped; keine Weltmarktübersicht) |
| Referenzfall Fürth ↔ FIM S00000159 v1.4 | Problem-/Machbarkeitsbeleg | VERIFIED (Hashes, 170 betroffene Elemente, Instanzvalidierung) |
| Technische Spezifikation | Förderumfang | SPECIFIED, nicht implementiert |
| eGovernment MONITOR 2026 (D21/TUM) | Problemgröße | VERIFIED (Sekundärquelle; URL/Abrufdatum; Medienbrüche allgemein) |
| FIM-Portal/FITKO: Schemata, Konverter, Releases | FIM/Schema-Kontext | VERIFIED (fimportal.de/arbeitsmittel + /releases, 13.11.2026) |
| PTF-FAQ/Handbuch/RL | Förderbedingungen | VERIFIED (Primärquellen, siehe Quellenregister) |

**Aktualitätsgrenze:** Der Prior-Art-Audit ist vom 13.11.2026. Bis zur Einreichung am 30.11.2026 wird die Suche fortgesetzt; neue Funde werden im Antrag als „nicht abschließend geprüft" markiert, nicht verschwiegen.

## 8. Integritätsgrenze (Trust Model)

Das FB-1-Manifest ist ein **Audit-Artefakt**, kein Sicherheitsanker. Es erkennt Inkonsistenzen und versehentliche Veränderungen, aber **nicht** einen Angreifer, der PDF und Manifest konsistent neu berechnet. Ohne Signatur, externen Timestamp oder Trust Anchor wird keine Manipulationsfestigkeit behauptet. C2PA/pyHanko sind verwandte Standards, aber im 6-Monats-Plan **nicht integriert**; eine optionale Signatur ist eine Härtung, keine Voraussetzung.

## 9. Fazit

FormBridge ist **keine weltweit neue Erfindung**, sondern eine sorgfältig abgegrenzte Infrastruktur-Hypothese: die prüfbare Kette von statischen Behörden-PDFs zu versionierten FIM-Datenfeldern mit Unsicherheit, menschlicher Kontrolle und Provenienz. Ob diese Kette praktisch trägt, ist die Forschungsfrage — nicht eine Vorab-Behauptung.
