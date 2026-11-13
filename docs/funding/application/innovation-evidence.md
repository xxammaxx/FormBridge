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
| **FITKO / FIM** | Versionierte Schemata, XDF/XSD, Schema-Repository, Konvertierungspfad „in der Konzeption" | Infrastruktur, keine PDF→FIM-Zuordnung | docs.fitko.de, 13.11.2026 |
| **GSA pdf-filler** | Füllt auch nicht interaktive PDFs über Koordinaten | PDF-Overlay ist Stand der Technik, keine semantische Zuordnung | Quellcode-Audit |
| **SurveyJS AI Form Response Extractor** | Extrahiert Scans/PDFs in JSON, lokal via Ollama möglich | „PDF zu JSON" allein ist nicht neu; keine FIM-Versionierung/Provenienz | Quellcode-Audit |
| **MACH Formsolutions / OZG-Formulardesigner** | Kommerzielle/offene Formularstrecken und Antragsassistenten | Bestehende Formularprozesse; FormBridge setzt bei vorgegebenen alten PDFs an | Quellcode-/Dokumentenprüfung |
| **C2PA, pyHanko, PDF-Signaturwerkzeuge** | Provenienz-/Signaturprüfung | Werden wiederverwendet, nicht neu erfunden; FormBridge prüft Feld-/PDF-Konsistenz, keine amtliche Authentizität | Standarddokumentation |

**Wichtig:** Die Tabelle ist eine Prüfung von 13 Projekten (Prior-Art-Audit), keine vollständige Weltmarktübersicht. „Nicht gefunden" heißt nicht „existiert nicht".

## 3. Die geprüfte Lücke

FormBridge kombiniert sieben Elemente in einer Kette:

1. statisches Behörden-PDF (born-digital, Textlage),
2. Feldkandidaten mit Koordinaten und sichtbarem Label,
3. versionierte FIM-Datenfeld-IDs,
4. explizite Confidence und `UNKNOWN` statt stillschweigender Entscheidung,
5. menschliches Review-Gate,
6. Provenienz-Manifest mit Hashes, Regelversion und Review-Entscheidungen,
7. unabhängiger Verifier und validierte Ausgabe.

**Behauptung:** In den 13 geprüften Projekten wurde diese **Kette** nicht gefunden. Einzelne Elemente sind vorhanden; die Kombination und die Prüfbarkeit sind die Forschungshypothese.

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
| H2: XSD-Normalisierung ist über ≥ 5 FIM-Schemata reproduzierbar | Compile-Erfolg, Reparaturprotokolle | **TEILWEISE BELEGT** für S00000159 (170 Fehler), Korpus offen |
| H3: Manifest + Verifier erkennen Manipulationen | Reproduzierbarkeit, 10 Negativfälle | **SPEZIFIZIERT**, nicht implementiert |
| H4: Review-Aufwand bleibt tragbar | Median-Zeit je Feld mit 2–3 externen Personen | **UNGEMESSEN** |

## 6. Gesellschaftlicher Nutzen — belegt vs. plausibel

**Belegt:**
- 50 % der Befragten erledigten ihr letztes Anliegen vollständig offline; 24 % nutzten einen Medienbruch; 68 % der Medienbruch-Betroffenen hätten es lieber vollständig digital (eGovernment MONITOR 2026, D21).
- FIM ist ein offizieller Standard für Verwaltungsdaten; FITKO dokumentiert den Konvertierungspfad als „in der Konzeption".
- Das amtliche S00000159-XSD ist im geprüften Stand nicht standardkonform kompilierbar (170 Parser-Fehler, libxml2/xmllint).

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
| Prior-Art-Audit, 13 Projekte, Clone-SHAs | Wettbewerbsabgrenzung | VERIFIED (Quellcode geprüft) |
| Referenzfall Fürth ↔ FIM S00000159 v1.4 | Problem-/Machbarkeitsbeleg | VERIFIED (Hashes, 170 Fehler, Instanzvalidierung) |
| Technische Spezifikation | Förderumfang | SPECIFIED, nicht implementiert |
| eGovernment MONITOR 2026 (D21) | Problemgröße | VERIFIED (Sekundärquelle; Zahlen zitiert) |
| FITKO-Dokumentation | FIM/Schema-Kontext | VERIFIED (Dokumentation, 13.11.2026) |
| PTF-FAQ/Handbuch/RL | Förderbedingungen | VERIFIED (Primärquellen, siehe Quellenregister) |

**Aktualitätsgrenze:** Der Prior-Art-Audit ist vom 13.11.2026. Bis zur Einreichung am 30.11.2026 wird die Suche fortgesetzt; neue Funde werden im Antrag als „nicht abschließend geprüft" markiert, nicht verschwiegen.

## 8. Fazit

FormBridge ist **keine weltweit neue Erfindung**, sondern eine sorgfältig abgegrenzte Infrastruktur-Hypothese: die prüfbare Kette von statischen Behörden-PDFs zu versionierten FIM-Datenfeldern mit Unsicherheit, menschlicher Kontrolle und Provenienz. Ob diese Kette praktisch trägt, ist die Forschungsfrage — nicht eine Vorab-Behauptung.
