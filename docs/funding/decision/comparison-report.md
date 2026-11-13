# Vergleichsbericht: Feldexa 2.0 / FormBridge vs. RepairProbe

**Datum:** 13.11.2026 · **Auftrag:** Entscheidungsgrundlage für **genau eine** Prototype-Fund-Bewerbung (Jahrgang 03, Förderlinie Innovation, Frist 30.11.2026, 15:00 CET) · **Charakter:** **bedingte Empfehlung**, **keine** Entscheidung für den Owner · **Vertraulichkeit:** nur öffentlich verifizierbare RepairProbe-Quellen; das private Produkt-Repo und der Portal-Draft wurden nicht eingesehen.

**Verwandte Dokumente:** [Scoring-Matrix (Hilfsinstrument)](scoring-matrix.md) · [Review A (alt)](review-A-formbridge.md) · [Review B RepairProbe (alt)](review-B-repairprobe.md) · [Quellen](sources-evidence.md) · [Finanzmodell](financial-model.md) · [Q3](q3-clarification.md) · [Owner-Fragen](owner-questions-status.md)

## 0. Namens- und Gegenstandsabgrenzung (wichtig)

Die vorhandene Forschung verwendet zwei Namen, die nicht deckungsgleich sind:

| Begriff | Bedeutung | Konsequenz |
|---|---|---|
| **Feldexa 2.0** | Die Flutter/Dart-Produktanwendung (PDF-Import, Felderkennung, Ausfüllen, Export, Signatur-/Provenienzprüfung) | Endnutzer-Produkt; besitzt App-Gerüst und Tests, aber **keine verifizierte E2E-Pipeline** |
| **FormBridge** | Das in [`project-boundary.md`](../project-boundary.md) abgegrenzte, eigenständige Open-Source-Infrastrukturmodul (PDF → FIM-Datenfeld-IDs, Provenienz, Verifier) | Der **engere, förderfähige Innovationsgegenstand**; eigenes Repo/Modul, keine App-Abhängigkeit |
| **Feldexa ProofLayer** | Die in PR #152 skizzierte Integritäts-/Provenienzschicht (Proof Bundle, Verifier, PDF-Signaturrisiko) | Alternative enge Förderfassung; überschneidet sich mit FormBridge, ist aber nicht identisch |

**Dieser Bericht vergleicht daher drei Feldexa-Fassungen mit RepairProbe:**

- **F1 — Feldexa 2.0 Produkt:** die Endnutzer-App (PDF ausfüllen, lokal, Unterschrift, Integrität).
- **F2 — Feldexa ProofLayer:** die Integritäts-/Provenienz-Infrastruktur aus PR #152.
- **F3 — FormBridge:** die FIM-Zuordnungs-/Verifier-Infrastruktur aus PR #168 (gegenwärtige Forschung).
- **RP — RepairProbe:** die Reparaturdiagnose-App.

Die **bedingte Empfehlung** bezieht sich auf **F3 als Fördergegenstand** für die Innovationslinie; F1 ist die stärkere Nutzergeschichte, aber die schwächere Innovations-/Abgrenzungsposition; F2 ist eine mittlere Option. Der Owner entscheidet, welche Fassung – oder ob RP – eingereicht wird.

## 1. Evidenzlage und ihre Grenzen

### Feldexa 2.0 / FormBridge

| Evidenz | Stand | Belastbarkeit |
|---|---|---|
| Öffentliches Monorepo `xxammaxx/Feldexa_2.0`, main `a34456f`; PRs #152/#168 offen (Draft) | VERIFIED (git/gh, 13.11.2026) | hoch für Repository-Zustand |
| 23 Produktions-Dart-Dateien, ~3.760 Zeilen; 20 Test-Dateien, ~4.800 Zeilen | VERIFIED (eigene Zählung) | hoch für Umfang, **nicht** für Funktionsfähigkeit |
| `flutter test`: App 56, core 24, ports 33, testkit 110, ui 17 = **240 Tests PASS**; 4 Pakete ohne Tests | VERIFIED (eigener Lauf, 13.11.2026) | hoch für Unit-/Widget-/Fixture-Ebene; **keine** E2E-Aussage |
| App-`main.dart` ist eine Shell; `feldexa_recognition`, `feldexa_export`, `feldexa_application`, Adapter haben **keinen** Produktcode | VERIFIED (Code-Inspektion) | hoch; die Pipeline ist **nicht** implementiert |
| Spezifikation `specs/001-scanned-form-workflow/spec.md` Status **Draft**; FR-001… beschreiben Import/Erkennung/Export | VERIFIED (Datei) | hoch für Planung, nicht für Umsetzung |
| Prior-Art-Audit 13 Projekte, Referenzfall Fürth/Wohngeld, 170 XSD-Parser-Fehler, 30-Feld-Datensatz | VERIFIED (Dokumente; Reproduktion im Repo dokumentiert) | hoch für Forschungsleistung; **keine** Nutzermessung |
| Keine gemessene Entlastung von Behörden/Bürgern; keine Nutzertests; kein E2E-Pilot | VERIFIED (explizit in der Forschung dokumentiert) | hohe Ehrlichkeit; schwache Wirkungsevidenz |
| Lizenz: keine LICENSE; Owner-Entscheidung offen | VERIFIED | Förderrisiko (FOSS-Zusage nötig) |

### RepairProbe

| Evidenz | Stand | Belastbarkeit |
|---|---|---|
| Öffentliche Org `RepairProbe`; Produkt-Repo `repair-probe` **privat**, Apache-2.0, Python ~63 KB, 5 Testdateien, letzter Push 30.10.2026 | VERIFIED (gh API-Metadaten, 13.11.2026) | hoch für Metadaten; **kein** Inhalt geprüft |
| Öffentliche Website: Messereignisformat, Validator, Mock-Adapter, anfügbarer Evidenzspeicher, Replay, passive Safety-Baseline | VERIFIED (öffentliche Website/README) | Selbstdarstellung; nicht unabhängig reproduziert |
| Testzahl: **24** in `llms.txt`, **44** auf `technical-baseline.html` (gleicher Commit) | **CONTRADICTED** (öffentliche Quellen widersprechen sich) | Die frühere Forschung zitierte 44; das ist nicht belastbar. Die private Suite ist nicht einsehbar. |
| 850 h / 6 Monate; Second Stage vorgesehen; Bewerbung nicht eingereicht | VERIFIED (öffentliche Website/llms.txt) | hoch für Planung |
| n=1-explorative Rückmeldung; Schmerz „verlorener Kontext" selten; Info-/Teilesuche und Zugang häufiger; keine Pilotpartner | VERIFIED (öffentliche Website) | ehrlich, aber **widerspricht** der Nutzenhypothese |
| Kein öffentlicher Prior-Art-Audit; externe Review fand iFixit FixBot, NORA, AugRep/GYVA, RepairVision (gleicher USP), YProbe/ARBoard/PCBSpot, ORDS/ORA | VERIFIED (Review B, öffentliche Quellen) | hohe Konkurrenz; Novelty nicht belegt |
| Keine Wirkungs-/KI-Qualitätsnachweise; Produkt-Repo privat | VERIFIED (Selbstauskunft) | schwache Verifizierbarkeit für die Jury |

## 2. Zehn Kriterien im direkten Vergleich

Bewertung: **stark / mittel / schwach / unbekannt**; keine Addition zu einem „Sieger-Score". Die Begründung nennt die Evidenz und die Unsicherheit.

| # | Kriterium | Feldexa 2.0 / FormBridge (F3) | RepairProbe (RP) | Evidenz / Unsicherheit |
|---|---|---|---|---|
| 1 | **Öffentlicher Nutzen & Zielgruppen** | **Mittel–stark:** Medienbruch bei Verwaltungsformularen; Bürger*innen, Beratungsstellen, Kommunen; lokale Verarbeitung schützt sensible Daten. Aber: Nutzen indirekt (Infrastruktur), keine Messung. | **Mittel:** Reparatur-Cafés/offene Werkstätten, Nachhaltigkeit/Right-to-Repair; direkter Endnutzerkontakt. Aber: n=1 widerspricht dem Kernschmerz; keine Pilotpartner. | F3: D21-2026-Zahlen, Referenzfall; RP: öffentliche Website, n=1. Beide ohne Wirkungsmessung. |
| 2 | **Digitalisierung / Verwaltungsentlastung** | **Stark konzeptionell:** adressiert genau den Medienbruch und die manuelle Nacherfassung; FIM-Anbindung ist ein echter Hebel. Aber: keine Behördeneinbindung, keine Prozessmessung. | **Schwach–mittel:** digitalisiert Reparaturwissen, aber keine Verwaltungsentlastung; Wirkung auf Reparaturerfolg unbewiesen. | F3: Forschungsdokument „Entlastung nicht gemessen"; RP: eigene Website. |
| 3 | **Technische Neuheit / Abgrenzbarkeit** | **Mittel:** Die Kombination statisches PDF → versionierte FIM-IDs → Provenienz/Unsicherheit → Verifier ist in der geprüften OSS-Landschaft nicht gefunden; aber Einzelbausteine (CommonForms, GSA pdf-filler, SurveyJS, MACH, OZG-Designer, FIM-Portal) existieren. Kein exklusiver Neuheitsnachweis. | **Schwach:** Evidenzklassen (OBSERVED/MEASURED/RETRIEVED/INFERRED/CONFIRMED) sind etablierte Methodik (FTA/FMEA, CBR); RepairVision hat ein sehr ähnliches „provisorische Labels"-Prinzip; FixBot/NORA/AugRep sind aktiv. | F3: 13-Projekte-Audit; RP: Review B. Beide: Jury-Urteil bleibt. |
| 4 | **Open-Source-Eignung / Wiederverwendung** | **Stark:** CLI/Bibliothek/Verifier, app-unabhängig, öffentliches Repo, FIM-Standards; Lizenz offen (Apache-2.0 empfohlen). | **Mittel:** Apache-2.0, aber Hauptcode **privat**; geplante FOSS-Veröffentlichung erst zum Projektabschluss; Vorarbeit für die Jury nicht verifizierbar. | F3: ADR-001/project-boundary; RP: gh-Metadaten/Website. |
| 5 | **Prototyp-Machbarkeit im Förderzeitraum** | **Mittel–schwach:** 6-Monats-Plan, aber **kein** Pipeline-Code; Abhängigkeiten von PDF-Varianten, FIM-Schemata, OCR/Detektion, Lizenzrechten; Scope-Risiko hoch. | **Mittel:** vorhandene Baseline (Format/Validator/Store/Replay/Safety) ist ein echter Startvorteil; aber KI-/Bildverständnis, Quellenrechte und Evaluation sind ungelöst; 850 h. | F3: Code-Inspektion; RP: öffentliche Baseline-Beschreibung. Beide: keine E2E-Prototypen. |
| 6 | **Verifizierter Implementierungsfortschritt** | **Schwach–mittel:** 240 Tests, aber überwiegend Infrastruktur/Fixtures/Geometrie; App-Shell; **keine** PDF-Import-/Erkennungs-/Export-/Verifier-Implementierung. | **Mittel (behauptet):** 24–44 Tests für Messereignisformat/Validator/Store/Replay; **privat**, daher nicht unabhängig prüfbar; öffentliche Testzahl widersprüchlich. | F3: eigener Testlauf + Code; RP: öffentliche Angaben, keine Einsicht. |
| 7 | **Technische Abhängigkeiten & Lieferrisiken** | **Hoch:** PDF-Varianten, FIM-Schema-Versionen, OCR-Qualität, Rechte an amtlichen PDFs (`copy:no`), Scope-Drift; keine gehostete Infrastruktur nötig (positiv). | **Hoch:** multimodale KI-Qualität, Datenminimierung vs. externe API, Quellen-Copyright, Evaluationsdesign, lokale VLM-Machbarkeit; keine Cloud-Pflicht (positiv). | F3: technische Spec; RP: eigene Risikoliste/Review B. |
| 8 | **Förderfähigkeit nach den Regeln** | **Mittel–stark:** Software-Infrastruktur, „neues Modul", hoher Entwicklungsanteil, FOSS-Zusage möglich; aber F3 hat noch keinen Code und die Abgrenzung muss die Jury überzeugen. F1 (Endnutzer-App) ist linienferner. | **Mittel–schwach:** Endnutzer-Werkzeug; Innovation-Linie argumentabel, aber nicht so wortlautnah wie F3; FOSS-Zusage möglich; privates Repo muss geöffnet werden. | F3: FAQ Grundlagen 02/ Bewerbung 05; RP: Review B. |
| 9 | **Finanzielle Machbarkeit / Eigenanteil / Cash-Flow** | **Mittel:** 950 h → F 47.381,25 €, EA 2.493,75 €; Konto 2.500 €; Peak-Vorfinanzierung 23.690,62 €; 950 h Kapazität ist hoch. | **Mittel:** 850 h → PK 42.500 €, GK 2.125 €, G 44.625 €, F **42.393,75 €**, EA 2.231,25 €; etwas niedrigere Förderung, etwas geringere Stundenlast; Second Stage proportional. | F3: Finanzmodell v4; RP: eigene Rechnung nach denselben Regeln, 850 h aus öffentlicher Website. |
| 10 | **Evidenz-/Narrativstärke der Bewerbung** | **Stark:** vollständiger Bewerbungsentwurf, Quellenkette, Referenzfall, Audit, 170-Fehler-Befund, klare Grenzen; aber „kein Code" ist ein Jury-Argument. | **Mittel:** ehrliche, kriterienbewusste Öffentlichkeitsarbeit, fertiger Portal-Draft (nicht einsehbar), aber kein Prior-Art-Audit, widersprüchliche Testzahl, private Baseline. | F3: Repo-Dokumente; RP: Website/Review B. |

## 3. Was ist demonstriert, was ist geplant?

### Feldexa 2.0 / FormBridge

| Fähigkeit | Status | Beleg |
|---|---|---|
| Flutter-App-Gerüst (Android/Web), deutsche Lokalisierung, Shell | **DEMONSTRIERT** | `main.dart`, 56 App-Tests |
| Geometrie-/Evidenz-/Fehler-Modell, Fixture-Loader, Testkit, simulierte UI-Banner | **DEMONSTRIERT** | core/ports/testkit/ui, 240 Tests |
| PDF-Import, Felderkennung, Ausfüllen, Overlay-Export | **NICHT DEMONSTRIERT** (spezifiziert) | `feldexa_recognition`/`feldexa_export` ohne Produktcode |
| Proof Bundle / unabhängiger Verifier / FIM-Zuordnung | **NICHT DEMONSTRIERT** (Forschung/Spec) | FormBridge-Repo = RESEARCH_STAGE, kein Code |
| Lokale Verarbeitung / Datenschutz | **PLANUNG** (Architekturprinzip) | Spec/ADR; kein E2E-Netzwerktest |
| Reduktion repetitiver Arbeit / Behördenentlastung | **NICHT GEMESSEN** | Forschungsdokument sagt explizit „nicht gemessen" |
| Dokumentintegrität / Originalbytes unverändert | **TEILWEISE DEMONSTRIERT** (Hash-/Fixture-Logik), **nicht** als PDF-E2E | core/testkit; keine PDF-Pipeline |

### RepairProbe

| Fähigkeit | Status | Beleg |
|---|---|---|
| Messereignisformat, Validator, Mock-Adapter, Evidenzspeicher, Replay, Safety-Baseline | **DEMONSTRIERT (laut Projekt)** | öffentliche Website; 24–44 Tests, privat |
| Smartphone-Erfassung, lokaler Reparaturfall, geführte Diagnose | **GEPLANT** | Roadmap |
| KI-/Bildverständnis, Quellenanbindung, Austauschformat | **GEPLANT/UNBEWIESEN** | eigene Website |
| Reparaturerfolg / Umweltwirkung | **NICHT GEMESSEN** | eigene Website |
| Open-Source-Veröffentlichung | **GEPLANT** (Produkt-Repo privat) | eigene Website |

## 4. Fairness-Check: Wo der Vergleich hinken könnte

1. **F3 hat keinen Code, RP hat privaten Code.** Das ist ein echter Nachteil für F3 bei „technischer Machbarkeit", aber ein Transparenzproblem für RP bei „Evidenz". Beide werden getrennt bewertet; keine Addition verdeckt den Unterschied.
2. **RP hat einen Portal-Draft, F3 nicht.** Der Draft ist nicht einsehbar; seine Qualität ist **UNKNOWN**. Ein exzellenter Draft könnte RP in Kriterium 10 heben, aber nicht die Novelty-/Bedarfsprobleme lösen.
3. **Die 44-Test-Zahl von RP ist nicht belastbar.** Öffentliche Quellen nennen 24 und 44; die frühere Forschung übernahm 44. Dieser Bericht verwendet **„24–44, nicht unabhängig verifiziert"**. Das ist keine Abwertung der Arbeit, sondern eine Evidenzgrenze.
4. **F3s 240 Tests sind keine Produktreife.** Sie belegen Infrastruktur, nicht die PDF-Pipeline. Die Formulierung „240 Tests" darf nicht als „Prototyp funktioniert" gelesen werden.
5. **Die 47.381,25-€-Zahl ist eine konservative Rechnung, keine Förderzusage.** Q3 ist offen; die 118,75-€-Differenz ist quantifiziert.
6. **Die Scoring-Matrix ist ein Hilfsinstrument, kein Jury-Modell.** Sie wurde aus der Forschung übernommen und mit den neuen Evidenzgrenzen annotiert; sie entscheidet nicht.

## 5. Trennung: Förderfähigkeit ≠ technische Machbarkeit ≠ sozialer Nutzen

| Dimension | Feldexa 2.0 / FormBridge (F3) | RepairProbe (RP) |
|---|---|---|
| **Formale Förderfähigkeit** | Hoch, sofern M1–M9 erfüllt; Linienfit „Software-Infrastruktur" wortlautnah; FOSS-Zusage möglich | Mittel; Endnutzer-Tool, Linienfit argumentabel; FOSS-Zusage möglich; privates Repo muss geöffnet werden |
| **Technische Machbarkeit** | Mittel–schwach: kein Pipeline-Code; hohe Integrations-/Rechteabhängigkeiten | Mittel: Baseline vorhanden; KI-/Bildqualität und Quellenrechte ungelöst |
| **Sozialer Nutzen** | Konzeptionell breit (Medienbruch, Datenschutz, Verwaltung), aber **nicht gemessen** | Direkter Zielgruppenbezug (Repair-Cafés), aber **n=1 widerspricht** dem Kernschmerz; keine Wirkungsmessung |
| **Bewerbungsreife** | Stark (Dokumente, Evidenzkette), aber kein Code | Mittel (Portal-Draft, ehrliche Kommunikation), aber Evidenz widersprüchlich |

## 6. Bedingte Empfehlung

**Für die Innovationslinie spricht derzeit mehr für F3 (Feldexa-2.0-Kontext / FormBridge) als für RP** — nicht weil F3 technisch reifer ist (das ist es nicht), sondern weil:

1. **Linienfit:** F3 ist Software-Infrastruktur im Wortlaut der FAQ; RP ist ein Endnutzer-Werkzeug.
2. **Evidenzdisziplin:** F3s Neuheitsbehauptung wurde aktiv gegen 13 Projekte geprüft; RPs Neuheit ist ungeprüft und durch aktive Konkurrenz belastet.
3. **Bewerbungsnarrativ:** F3 hat eine vollständige, quellenbelegte Geschichte; RP hat einen guten, aber privaten Baseline- und einen nicht einsehbaren Portal-Draft.

**Die Empfehlung ist ausdrücklich bedingt:**

- **B1:** M1–M9 müssen positiv geklärt sein; Q2 (Selbstständigkeit) ist der kritischste Punkt.
- **B2:** Der Owner muss F1/F2/F3/RP wählen; dieser Bericht entscheidet nicht.
- **B3:** F3 muss als eigenständiges Repo/Modul isoliert werden; kein Feldexa-Produktcode im Förderumfang.
- **B4:** Falsifikation bis 30.11.2026 fortsetzen; bei Widerlegung PIVOT auf ein schmaleres Schema-Hygiene-/Provenienzvorhaben.
- **B5:** De-Overclaim-Pass; keine „weltweit neu"- oder „behördentauglich"-Aussagen.
- **B6:** Held-out-PDF und externe Testpersonen für die Evaluation; kein Zirkelschluss.

**Wenn der Owner technische Demonstrierbarkeit und eine existierende Baseline höher gewichtet als Linienfit/Novelty, ist RP die rationalere Wahl.** Dann müssen die RP-Risiken (Konkurrenz, n=1, privates Repo, KI-Qualität) im Antrag offen adressiert werden. **Wenn der Owner den direkten Bürgernutzen der Feldexa-App** in den Vordergrund stellt, ist F1 die stärkere Geschichte — aber die Innovation-Linie ist dafür der schwächere Förderweg; F1 müsste die Abgrenzung zur bestehenden App und zu CommonForms/GSA/SurveyJS besonders scharf zeigen.

**Kein Automatismus:** Die Rangfolge ist in den Sensitivitätsszenarien der Scoring-Matrix stabil, aber die Matrix ist kein Jury-Modell. Der Owner entscheidet auf Basis der hier offengelegten Unsicherheiten.

## 7. Was die Empfehlung umkippen würde

| Ereignis | Wirkung |
|---|---|
| F3-Prior-Art-Audit findet ein Projekt, das die volle Kette bereits implementiert | F3-Novelty bricht; PIVOT/NO_GO für F3 |
| RP legt eine öffentliche, reproduzierbare Testsuite und eine belastbare Bedarfsstudie vor | RP-Evidenz steigt; Rangfolge kann kippen |
| Q2 wird negativ beantwortet (Selbstständigkeit erst ab Förderbeginn nicht akzeptiert) | F3 **und** RP nur mit Freistellung/aktueller Selbstständigkeit |
| F3 bekommt vor der Frist einen demonstrierbaren Mini-PoC | F3-Technikrisiko sinkt; Empfehlung stärker |
| RP Portal-Draft erweist sich als exzellent und die Jury gewichtet Endnutzer-Nutzen stärker | RP kann in Kriterium 10 aufholen; Innovationsrückstand bleibt |

## 8. Was dieser Bericht nicht ist

- Keine Förderzusage, keine Erfolgsprognose, keine Jury-Simulation.
- Keine Entscheidung für den Owner; keine Aussage, RP sei „schlecht".
- Keine Aussage über andere Förderprogramme (für RP können reparaturspezifische Töpfe besser passen).
- Keine Offenlegung privater RP-Inhalte; keine Änderung an RP-Repo oder Portal-Draft.
