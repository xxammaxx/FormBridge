# FormBridge — Bewerbung Prototype Fund 2027, Jahrgang 03, Förderlinie Innovation

**Status:** Einreichungsentwurf zur Owner-Freigabe · **Datum:** 13.11.2026 · **Frist:** 30.11.2026, 15:00 Uhr MEZ
**Förderzeitraum:** 01.06.2027–30.11.2027 · **Antragstellerin:** Einzelperson · **Projekt:** FormBridge
**Wichtig:** Dieser Text enthält Platzhalter für persönliche Angaben. Er ist **kein** eingereichter Antrag. Es wurden keine persönlichen Daten erfunden. Exakte Portal-Zeichenlimits sind `PORTAL_UNVERIFIED`.

**Wortlimits:** aus dem offiziellen PTF-Handbuch Jahrgang 03 (Fragen 2–19). Die hier angegebenen Wortzahlen nutzen einen einfachen Whitespace-Tokenizer; das Portal kann anders zählen und zusätzlich Zeichenlimits erzwingen. Diese wurden nicht eingesehen.

---

## 1. Projekt in einem Satz (max. 30 Wörter)

FormBridge ist ein geplantes freies, lokal laufendes Softwaremodul, das statische Behörden-PDFs analysiert, Formularfelder nachvollziehbar versionierten FIM-Datenfeldern zuordnet und prüfbare, strukturierte Ergebnisse bereitstellt.

**Wörter:** 22 / 30 · **Status:** FINAL

---

## 2. Projektbeschreibung (max. 100 Wörter)

Im Förderzeitraum entsteht ein eigenständiges Open-Source-Modul mit Bibliothek und CLI. Es erkennt Formularfelder in nicht interaktiven, born-digitalen Behörden-PDFs, schlägt Zuordnungen zu versionierten FIM-Datenfeldern vor und markiert Unsicherheit ausdrücklich als UNKNOWN. Menschen prüfen und korrigieren die Vorschläge. Ein versioniertes Provenienz-Manifest und ein unabhängiger Verifier machen Quelle, Schema-Version, Koordinaten und Review-Entscheidungen nachprüfbar. Eine gegen die dokumentiert normalisierte Schema-Variante validierte Ausgabe und ein Abdeckungsbericht runden den Kern ab. Referenz ist der Wohngeldantrag S00000159; Scans, Produkt-UI und Behördenanschluss sind nicht Teil des Vorhabens. Selbst erstellter Code und Dokumentation werden FOSS; amtliche PDFs/XSDs und abgeleitete FIM-Metadaten nur nach Rechteklärung per URL/Hash.

**Wörter:** 96 / 100 · **Status:** FINAL

---

## 3. Gesellschaftliche Herausforderung (max. 175 Wörter)

Ein Teil der amtlichen Formulare wird als statische PDF bereitgestellt und ist nicht interaktiv ausfüllbar. Wer sie digital bearbeiten will, muss Felder manuell nachbauen, Werte doppelt erfassen oder Cloud-Dienste mit sensiblen Daten beauftragen. Der eGovernment MONITOR 2026 zeigt: 50 % der Befragten erledigten ihr letztes Anliegen vollständig offline, 24 % nutzten einen Medienbruch; 68 % der Medienbrüche waren unfreiwillig. Im geprüften Referenzfall, dem Fürther Wohngeldantrag, liegt genau ein solches statisches PDF vor. Gleichzeitig fehlt in den geprüften offenen Projekten eine offene, prüfbare Brücke zwischen dem sichtbaren PDF und den versionierten FIM-Datenfeldern, die Verwaltungsverfahren bereits beschreiben.

Besonders relevant ist diese Lücke für Anträge mit sensiblen Daten, etwa Sozialleistungen, sowie für Beratungsstellen und Kommunen. FormBridge setzt nicht beim Endnutzer, sondern bei der Software an, die solche Anträge baut: Wenn Zuordnungen nachvollziehbar und unsicherheitsbewusst sind, können darauf aufbauende Anwendungen Medienbrüche reduzieren, ohne vertrauliche Daten an einen zentralen Dienst zu geben. Das ist kein Ersatz für Rechtsberatung oder Behördenentscheidungen, sondern eine technische Grundlage für verlässlichere digitale Verfahren.

**Wörter:** 163 / 175 · **Status:** FINAL

---

## 4. Technische Umsetzung (max. 175 Wörter)

Geplant ist ein Python-3.12-Modul mit CLI und Bibliotheks-API. Die PDF-Textlage wird mit pypdfium2 oder pdfminer.six extrahiert; Layout- und Abschnittsanalyse erfolgen regelbasiert. Ein versionierter Regelkatalog (YAML/JSON) beschreibt Labelmuster, Kontextbedingungen, Zielpfade und Confidence-Beiträge. Kandidaten werden gegen versionierte FIM-Schemata geprüft; Codelisten werden aus Schema-Facetten gebunden. Jede Ausgabe enthält lokale Feld-ID, Seite, Koordinaten, Label, Kandidaten, Confidence und Zustand PROPOSED/UNKNOWN/REJECTED. Ein Review-Schritt speichert menschliche Entscheidungen.

Das Provenienz-Manifest FB-1 enthält SHA-256 von PDF und Schema, Tool-/Regelversion, Normalisierungsschritte und Review-Hashes; ein separater Verifier prüft es ohne App-Abhängigkeit. Die Ausgabe wird mit lxml gegen die dokumentiert normalisierte, verlustbehaftete Schema-Variante validiert; wo verfügbar, ist FITKO-JSON-Schema der primäre Pfad. Die Laufzeit ist offline; Schema und optionale Modellgewichte werden lokal bereitgestellt und gehasht. Cloud-Dienste und ein produktiver Behördenanschluss sind ausgeschlossen. Ein kleines lokales ML-Modell ist optional, nicht Voraussetzung. Die Architektur bleibt ohne Feldexa-Abhängigkeit nutzbar.

**Wörter:** 133 / 175 · **Status:** FINAL

---

## 5. Aktueller Stand und geplante Neuerungen (max. 100 Wörter)

Die Idee ist erforscht, aber das Modul ist nicht implementiert. Vorhanden sind ein öffentlicher Prior-Art-Audit über 13 Projekte, ein Referenzfall zum Fürther Wohngeldantrag und FIM S00000159 v1.4, ein 30-Feld-Referenzdatensatz, eine technische Spezifikation sowie der Nachweis von 170 Parser-Fehlern im amtlichen XSD (1 NCName + 169 D2-Meldungen). Diese Arbeiten sind Vorarbeit und werden nicht als Förderleistung abgerechnet. Im Förderzeitraum entstehen die eigenständige Codebasis, der Regelkatalog, die Review- und Verifier-Komponenten sowie der Testkorpus. Die Feldexa-App bleibt ein unabhängiges Produkt und wird nicht verändert.

**Wörter:** 81 / 100 · **Status:** FINAL

---

## 6. Link zum bestehenden Projekt (optional)

https://github.com/xxammaxx/FormBridge

**Hinweis:** Das Repository ist derzeit Forschungsstand (Dokumentation, Evidenz, Spezifikation); es enthält **keinen** Produktcode für die geplante Pipeline.

---

## 7. Innovation (max. 100 Wörter)

Die untersuchte Kombination ist: statisches Behörden-PDF → versionierte FIM-Datenfeld-IDs → explizite Unsicherheit/UNKNOWN → menschliche Freigabe → prüfbares Provenienz-Manifest → unabhängiger Verifier. Einzelne Bausteine existieren: Formularagent migriert Formulardefinitionen ohne PDF-Eingang; KIWO extrahiert Werte cloudbasiert ohne FIM-Koordinaten; CommonForms erkennt Felder ohne Lizenz und Semantik; FITKO betreibt Schema-Infrastruktur und Konverter, aber keine PDF→FIM-Zuordnung. In unserem 13-Projekte-Audit (Quellcode, wo verfügbar) haben wir diese Kette nicht gefunden. Kein einzelner Baustein deckt die Kette ab; die Kombination ist Eigenarbeit. Wir behaupten keine weltweite Erstmaligkeit; die Förderung testet, ob die Kombination praktisch trägt.

**Wörter:** 86 / 100 · **Status:** FINAL

---

## 8. Zielgruppe und Zugang (max. 100 Wörter)

Primär: Entwickler*innen und Maintainer freier Verwaltungssoftware, Entwickler*innen in Kommunen und IT-Dienstleistern sowie die FIM-/OZG-Community. Sie erhalten eine Bibliothek und CLI, die sie in eigene Produkte integrieren können. Erreicht werden sie über das öffentliche GitHub-Repository, technische Dokumentation, Vorträge und Austausch im FIM-/FITKO-Umfeld sowie über bestehende Open-Source-Netzwerke. Open Source, damit andere die Infrastruktur prüfen, erweitern und unabhängig betreiben können. Sekundär profitieren Bürger*innen und Verwaltungsmitarbeitende über Anwendungen, die FormBridge einsetzen. Eine direkte Endnutzer-UI ist nicht Teil des Vorhabens; Feldexa 2.0 ist die vorgesehene erste Anwendung, aber nicht integriert und nicht Teil des Förderumfangs.

**Wörter:** 90 / 100 · **Status:** FINAL

---

## 9. Meilensteine im Förderzeitraum (max. 100 Wörter)

1. Monat: Repository, CLI-Grundgerüst, PDF-Textlage, Schema-Laden/Hash, FB-1-Spezifikation; Normalisierungswerkzeug und CI für den XSD-Korpus.
2. Monat: Regelkatalog v1, Feldkandidaten, Confidence/UNKNOWN, erste End-to-End-Tests.
3. Monat: Goldstandard, Review-CLI, Codelisten, Precision/Recall-Baseline; externe Testpersonen gewinnen.
4. Monat: Abschnitts-Disambiguierung, Hard Gates für Identität/Betrag, Held-out-PDF, Messung.
5. Monat: Emit/Validate/Verify, 10 Manipulations-Negativtests, ≥ 3 FIM-XSDs (5 als Stretch).
6. Monat: Review-Zeit-Messung, Dokumentation, FOSS-Release, Abschlussbericht.
Jeder Meilenstein endet mit einem reproduzierbaren Testlauf und einem kurzen öffentlichen Bericht.

**Wörter:** 68 / 100 · **Status:** FINAL

---

## 10. Team — Ja/Nein (zweiter Teil nur bei Team; max. 30 Wörter)

**Antwort:** Nein, ich bewerbe mich als Einzelperson.

**Wörter:** 7 / 30 · **Status:** FINAL

---

## 11. Bisherige Softwareprojekte (max. 100 Wörter; max. 3 Beispiele)

Seit [JAHR] arbeite ich an [PROJEKT] und habe dort [ROLLE/UMFANG] verantwortet. Öffentlich: Feldexa 2.0 (Flutter/Dart), https://github.com/xxammaxx/Feldexa_2.0, und das FormBridge-Research-Repo, https://github.com/xxammaxx/FormBridge. [OWNER_ANGABE_ERFORDERLICH: max. 3 Projekte, Links, Rolle und Umfang; keine erfundenen Angaben].

**Wörter:** 16 + Platzhalter / 100 · **Status:** OWNER_ANGABE_ERFORDERLICH

---

## 12. Förderfähigkeit — Q4 Ja/Nein und Q5 Erläuterung

**Q4 — Bist du Gesellschafter*in einer GmbH/anderen Unternehmensform, hast du einen Verein/eine Organisation gegründet oder arbeitest du für einen thematisch verbundenen Verein, ein Forschungsinstitut o. Ä.?**

**Antwort:** [OWNER_BESTÄTIGUNG_ERFORDERLICH: Ja/Nein]

**Q5 — nur falls Q4 = Ja: Wenn ja, erläutere, weshalb das Projekt nicht dazu dient, eine für den eigenen Geschäftsbetrieb benötigte Software zu entwickeln (max. 60 Wörter).**

[OWNER_BESTÄTIGUNG_ERFORDERLICH: Falls Q4 = Ja, Beteiligung/Anstellung nennen und die klare Trennung zum Projekt erläutern. Falls Q4 = Nein, Q5 entfällt.] FormBridge ist ein eigenständiges Gemeinwohlprojekt und keine Auftragsentwicklung für einen Geschäftsbetrieb.

**Wörter Q5:** 21 / 60 · **Status:** OWNER_BESTÄTIGUNG_ERFORDERLICH

---

## 13. Arbeitsstunden (Zahl)

**Antwort:** 950

**Begründung:** 950 h entsprechen der maximalen Stundenzahl für Einzelpersonen; die Aufteilung ist im [Sechs-Monats-Plan](six-month-development-plan.md) dokumentiert. Eine realistische 850-h-Variante liegt in [budget-final.md](budget-final.md).

**Status:** FINAL (950)

---

## 14. Motivation / Wild Card (max. 100 Wörter)

Das Problem begleitet mich [OWNER_ANGABE: persönlicher Bezug]. Entscheidend ist für mich, dass digitale Verwaltung nicht bedeutet, sensible Daten an intransparente Dienste zu geben. FormBridge verbindet technische Sorgfalt mit einem konkreten öffentlichen Nutzen: nachvollziehbare Zuordnungen, offene Standards und Werkzeuge, die andere wiederverwenden können. Ich möchte die förderfähige Zeit nutzen, um die offene Lücke zwischen amtlichen PDFs und FIM-Datenfeldern belastbar zu schließen und die Ergebnisse vollständig zu veröffentlichen. Ich bin bereit, die für eine Förderung erforderlichen formalen Schritte rechtzeitig einzuleiten. [OWNER_ANGABE: Erfahrung/Motivation ergänzen].

**Wörter:** 77 + Platzhalter / 100 · **Status:** OWNER_ANGABE_ERFORDERLICH

---

## 15. Second Stage — Ja/Nein

**Antwort:** Ja. [OWNER_ENTSCHEIDUNG_ERFORDERLICH: Falls Nein, §15 auf „Nein“ setzen und §16/§17 entfernen.]

**Begründung:** FormBridge ist Infrastruktur; der Prototyp allein erzeugt noch keine Nutzung. Die Second Stage ist für Integration, Dokumentation und Pflege sinnvoll.

**Status:** OWNER_ENTSCHEIDUNG_ERFORDERLICH

---

## 16. Second Stage — Schwerpunkt (max. 175 Wörter)

Nach dem Prototyp braucht FormBridge vor allem Adoption und Pflege, nicht mehr Funktionsumfang. In vier Monaten will ich: (1) zwei Integrationen begleiten, darunter eine kommunale Testumgebung und optional Feldexa 2.0 als Consumer, nicht als geförderte Integration; (2) Integrationsrezepte, stabile Schnittstellen und Beispieldaten veröffentlichen; (3) eine kleine Regelkatalog- und Schema-Community aufbauen, mit dokumentiertem Review- und Release-Prozess; (4) Nutzertests zur Verständlichkeit von UNKNOWN und zur Review-Zeit durchführen; (5) einen Wartungsplan und eine Governance-Skizze für die Zeit nach der Förderung erstellen. Erfolg wäre: mindestens eine externe Integration, eine veröffentlichte Version 0.2 und ein dokumentierter Pflegeweg. Keine neuen Kernfunktionen, keine Produkt-UI.

**Wörter:** 99 / 175 · **Status:** FINAL (bei Second Stage = Ja)

---

## 17. Second Stage — Meilensteine (max. 100 Wörter)

1. Monat: Integrationsgespräche, Anforderungsaufnahme, stabile Schnittstellenversion.
2. Monat: Erste externe Integration, Integrationsrezepte und Beispieldaten.
3. Monat: Nutzertests zu UNKNOWN/Review-Zeit, Community-Austausch, Dokumentation.
4. Monat: Version 0.2, Wartungs- und Governance-Skizze, Abschlussbericht.

**Wörter:** 30 / 100 · **Status:** FINAL (bei Second Stage = Ja)

---

## 18. Bestätigungen (Pflichtfelder im Portal)

- [ ] Ich bin mindestens 18 Jahre alt und habe meinen Hauptwohnsitz in Deutschland.
- [ ] Ich sage zu, das im Förderzeitraum erstellte Softwareprojekt unter einer Freien-/Open-Source-Lizenz zu veröffentlichen.

**Status:** OWNER_BESTÄTIGUNG_ERFORDERLICH · **Hinweis:** Die beiden Bestätigungen sind im Handbuch (Q19) dokumentiert; die exakte Portal-Checkbox-Formulierung ist `PORTAL_UNVERIFIED`.

---

## Anhang: Was hier bewusst nicht steht

- Keine Behauptung, FormBridge sei bereits implementiert.
- Keine Behauptung, Feldexa 2.0 sei bereits integriert.
- Keine Behauptung, eine Behörde akzeptiere die Ausgabe.
- Keine weltweite Erstmaligkeitsbehauptung.
- Keine erfundenen persönlichen Angaben, Zeichenlimits oder Portalfragen.
