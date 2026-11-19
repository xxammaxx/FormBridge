# FormBridge — Bewerbung Prototype Fund 2027, Jahrgang 03, Förderlinie Innovation

**Status:** Einreichungsentwurf zur Owner-Freigabe · **Datum:** 19.11.2026 (LoRA-Delta) · **Frist:** 30.11.2026, 15:00 Uhr MEZ
**Förderzeitraum:** 01.06.2027–30.11.2027 · **Antragstellerin:** Einzelperson · **Projekt:** FormBridge
**Wichtig:** Dieser Text enthält Platzhalter für persönliche Angaben. Er ist **kein** eingereichter Antrag. Es wurden keine persönlichen Daten erfunden. Exakte Portal-Zeichenlimits sind `PORTAL_UNVERIFIED`.

**Wortlimits:** aus dem offiziellen PTF-Handbuch Jahrgang 03 (Fragen 2–19). Die hier angegebenen Wortzahlen nutzen einen einfachen Whitespace-Tokenizer; das Portal kann anders zählen und zusätzlich Zeichenlimits erzwingen. Diese wurden nicht eingesehen.

---

## 1. Projekt in einem Satz (max. 30 Wörter)

FormBridge ist ein geplantes freies, lokal laufendes Softwaremodul, das statische Behörden-PDFs analysiert, Formularfelder nachvollziehbar versionierten FIM-Datenfeldern zuordnet und prüfbare, strukturierte Ergebnisse bereitstellt.

**Wörter:** 22 / 30 · **Status:** FINAL

---

## 2. Projektbeschreibung (max. 100 Wörter)

Im Förderzeitraum entsteht eine eigenständige Open-Source-Bibliothek mit CLI. Sie erkennt Formularfelder in nicht interaktiven, born-digitalen Behörden-PDFs, schlägt versionierte FIM-Zuordnungen vor und markiert Unsicherheit als UNKNOWN. Menschen prüfen Vorschläge. Ein Provenienz-Manifest und unabhängiger Verifier machen Quelle, Schema-Version, Koordinaten und Review-Entscheidungen nachprüfbar. Eine validierte strukturierte Ausgabe und ein Abdeckungsbericht ergänzen den Kern. Optional wird untersucht, ob ein gezielt berechneter LoRA-Adapter auf einem kleinen lokalen Sprachmodell mehrdeutige Feldzuordnungen verbessert. Referenz ist Wohngeld S00000159; Scans, Produkt-UI und Behördenanschluss bleiben ausgeschlossen. Eigene Ergebnisse werden FOSS; Drittmaterial nur nach Rechteklärung.

**Wörter:** 84 / 100 · **Status:** FINAL (Entwurf)

---

## 3. Gesellschaftliche Herausforderung (max. 175 Wörter)

Ein Teil der amtlichen Formulare wird als statische PDF bereitgestellt und ist nicht interaktiv ausfüllbar. Wer sie digital bearbeiten will, muss Felder manuell nachbauen, Werte doppelt erfassen oder Cloud-Dienste mit sensiblen Daten beauftragen. Der eGovernment MONITOR 2026 zeigt: 50 % erledigten ihr letztes Anliegen vollständig offline, 24 % nutzten einen Medienbruch; 68 % davon unfreiwillig. Die Studie misst Medienbrüche allgemein, nicht PDFs als Ursache. Im geprüften Referenzfall, dem Fürther Wohngeldantrag, liegt genau ein solches statisches PDF vor. Gleichzeitig fehlt in den geprüften offenen Projekten eine offene, prüfbare Brücke zwischen dem sichtbaren PDF und den versionierten FIM-Datenfeldern, die Verwaltungsverfahren bereits beschreiben.

Besonders relevant ist diese Lücke für Anträge mit sensiblen Daten, etwa Sozialleistungen, sowie für Beratungsstellen und Kommunen. FormBridge setzt nicht beim Endnutzer, sondern bei der Software an, die solche Anträge baut: Wenn Zuordnungen nachvollziehbar und unsicherheitsbewusst sind, können darauf aufbauende Anwendungen Medienbrüche reduzieren, ohne vertrauliche Daten an einen zentralen Dienst zu geben. Das ist kein Ersatz für Rechtsberatung oder Behördenentscheidungen, sondern eine technische Grundlage für verlässlichere digitale Verfahren.

**Wörter:** 168 / 175 · **Status:** FINAL

---

## 4. Technische Umsetzung (max. 175 Wörter)

Geplant ist ein Python-Modul mit CLI und Bibliotheks-API. PDF-Textlage und Layout werden extrahiert; ein versionierter Regelkatalog ordnet Label und Abschnittskontext FIM-Zielpfaden zu. Kandidaten werden gegen Schema und Codelisten geprüft; jede Ausgabe enthält Koordinaten, Confidence und PROPOSED/UNKNOWN/REJECTED. Menschen bestätigen kritische Zuordnungen. Optional vergleiche ich einen regelbasierten Ansatz, ein kleines unverändertes Qwen-Modell und einen gezielt berechneten LoRA-Adapter ohne Gradiententraining, ausschließlich für mehrdeutige Feldzuordnungen. Das Modell darf nur Kandidaten vorschlagen; keine Umgehung von UNKNOWN, Review oder Schema-Prüfung. Bei fehlendem Mehrwert bleibt es deaktiviert. Das Provenienz-Manifest FB-1 enthält PDF-/Schema-Hashes, Versionen, Normalisierungsschritte, Review-Hashes und gegebenenfalls Adapterprovenienz. Ein unabhängiger Verifier prüft es. Ausgabevalidierung erfolgt gegen dokumentiert normalisiertes XSD bzw. FITKO-JSON-Schema. Die Anwendung selbst läuft offline; rechenintensive Forschungsversuche auf gemieteter Hardware sind nur optional, mit synthetischen Daten und nach gesonderter Kostenfreigabe. Die Entwicklungsarbeit bleibt eigenverantwortlich. Keine Feldexa-Abhängigkeit, keine produktive Cloud-Anbindung.

**Wörter:** 133 / 175 · **Status:** FINAL (Entwurf)

---

## 5. Aktueller Stand und geplante Neuerungen (max. 100 Wörter)

Die Idee ist erforscht, aber das Modul ist nicht implementiert. Vorarbeit: öffentlicher Prior-Art-Audit über 13 Projekte, Referenzfall Fürther Wohngeldantrag/FIM S00000159 v1.4, 30-Feld-Referenzdatensatz, Spezifikation und Nachweis von 170 XSD-Parser-Fehlern (1 NCName + 169 D2-Meldungen). Der LoRA-Versuch ist bislang nur konzipiert; keine Adapterwirkung ist belegt. Vorarbeiten werden nicht abgerechnet. Im Förderzeitraum entstehen eigenständige Codebasis, Regelkatalog, Review, Verifier, Testkorpus und optional der lokale Adapter-Vergleich. Feldexa bleibt unabhängiges, nicht gefördertes Produkt.

**Wörter:** 67 / 100 · **Status:** FINAL (Entwurf)

---

## 6. Link zum bestehenden Projekt (optional)

https://github.com/xxammaxx/FormBridge

**Hinweis:** Das Repository ist derzeit Forschungsstand (Dokumentation, Evidenz, Spezifikation); es enthält **keinen** Produktcode für die geplante Pipeline.

---

## 7. Innovation (max. 100 Wörter)

FormBridge kombiniert statisches Behörden-PDF, versionierte FIM-Datenfeld-IDs, UNKNOWN, menschliche Freigabe, überprüfbare Provenienz und unabhängigen Verifier. Formularagent migriert Definitionen ohne PDF-Eingang, KIWO extrahiert cloudbasiert ohne FIM-Koordinaten, CommonForms erkennt Felder ohne FIM-Semantik und FITKO betreibt Schema-Infrastruktur ohne diese Zuordnungskette. Im begrenzten 13-Projekte-Audit wurde die Kette nicht gefunden. Zusätzlich wird geprüft, ob ein gezielt berechneter LoRA-Adapter die lokale Kontextzuordnung ohne Training verbessert. Dieses Experiment ist optional, kein Nachweis einer neuen Modellfähigkeit; die Innovation ist die prüfbare Infrastruktur, nicht LoRA an sich. Keine weltweite Erstmaligkeit wird behauptet.

**Wörter:** 82 / 100 · **Status:** FINAL (Entwurf)

---

## 8. Zielgruppe und Zugang (max. 100 Wörter)

Primär: Entwickler*innen und Maintainer freier Verwaltungssoftware, Entwickler*innen in Kommunen und IT-Dienstleistern sowie die FIM-/OZG-Community. Sie erhalten eine Bibliothek und CLI, die sie in eigene Produkte integrieren können. Erreicht werden sie über das öffentliche GitHub-Repository, technische Dokumentation, Vorträge und Austausch im FIM-/FITKO-Umfeld sowie über bestehende Open-Source-Netzwerke. Open Source, damit andere die Infrastruktur prüfen, erweitern und unabhängig betreiben können. Sekundär profitieren Bürger*innen und Verwaltungsmitarbeitende über Anwendungen, die FormBridge einsetzen. Eine direkte Endnutzer-UI ist nicht Teil des Vorhabens; Feldexa 2.0 ist die vorgesehene erste Anwendung, aber nicht integriert und nicht Teil des Förderumfangs.

**Wörter:** 90 / 100 · **Status:** FINAL

---

## 9. Meilensteine im Förderzeitraum (max. 100 Wörter)

1. Monat: CLI-Grundgerüst, PDF-Textlage, Schema-Hash, FB-1, Normalisierung und CI.
2. Monat: Regelkatalog, Feldkandidaten, Confidence/UNKNOWN, erste End-to-End-Tests.
3. Monat: Goldstandard, Review-CLI, Codelisten, Baseline; externe Testpersonen gewinnen.
4. Monat: Abschnitts-Disambiguierung, Hard Gates, Held-out-PDF; optionaler begrenzter LoRA-Vergleich bei gesichertem Kernfortschritt.
5. Monat: Emit/Validate/Verify, 10 Negativtests, ≥ 3 FIM-XSDs (5 Stretch).
6. Monat: Review-Zeit, Dokumentation, FOSS-Release, Abschlussbericht.
Jeder Meilenstein endet mit reproduzierbarem Testlauf und öffentlichem Bericht.

**Wörter:** 62 / 100 · **Status:** FINAL (Entwurf)

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

**Wörter Q5:** 11 / 60 (Antworttext; Owner-Ergänzung bei Q4=Ja) · **Status:** OWNER_BESTÄTIGUNG_ERFORDERLICH

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

Nach dem Prototyp braucht FormBridge vor allem Adoption und Pflege, nicht mehr Funktionsumfang. In vier Monaten will ich: (1) eine externe Integration begleiten und optional eine kommunale Testumgebung prüfen; Feldexa 2.0 bleibt optionaler Consumer, nicht geförderte Integration; (2) Integrationsrezepte, stabile Schnittstellen und Beispieldaten veröffentlichen; (3) eine kleine Regelkatalog- und Schema-Community aufbauen, mit dokumentiertem Review- und Release-Prozess; (4) Nutzertests zur Verständlichkeit von UNKNOWN und zur Review-Zeit durchführen; (5) einen Wartungsplan und eine Governance-Skizze für die Zeit nach der Förderung erstellen. Erfolg wäre: mindestens eine externe Integration, eine veröffentlichte Version 0.2 und ein dokumentierter Pflegeweg. Keine neuen Kernfunktionen, keine Produkt-UI.

**Wörter:** 98 / 175 · **Status:** FINAL (bei Second Stage = Ja; S1 bleibt Owner-Entscheidung)

---

## 17. Second Stage — Meilensteine (max. 100 Wörter)

1. Monat: Integrationsgespräche, Anforderungsaufnahme, stabile Schnittstellenversion.
2. Monat: Erste externe Integration, Integrationsrezepte und Beispieldaten.
3. Monat: Nutzertests zu UNKNOWN/Review-Zeit, Community-Austausch, Dokumentation.
4. Monat: Version 0.2, Wartungs- und Governance-Skizze, Abschlussbericht.

**Wörter:** 29 / 100 · **Status:** FINAL (bei Second Stage = Ja; S1 bleibt Owner-Entscheidung)

---

## 18. Bestätigungen (Handbuch Q19; Portal-Checkbox unverified)

- [ ] „Ich bin über 18 Jahre alt und habe meinen Hauptwohnsitz in Deutschland.“ (Handbuch JG03, Q19, Sept. 2026)
- [ ] „Ich bin damit einverstanden, die Projektergebnisse unter einer Open-Source-Lizenz (z. B. MIT-Lizenz), öffentlich zugänglich (z. B. über Github/Gitlab/Codeberg) zur Verfügung zu stellen.“ (Handbuch JG03, Q19, Sept. 2026)

**Status:** OWNER_BESTÄTIGUNG_ERFORDERLICH · **Hinweis:** Q19 steht **nicht** im Fragen-PDF Innovation, sondern im Handbuch und in der Portal-Checkbox; die exakte Live-Formulierung ist `PORTAL_UNVERIFIED`.

---

## Anhang: Was hier bewusst nicht steht

- Keine Behauptung, FormBridge sei bereits implementiert.
- Keine Behauptung, Feldexa 2.0 sei bereits integriert.
- Keine Behauptung, eine Behörde akzeptiere die Ausgabe.
- Keine weltweite Erstmaligkeitsbehauptung.
- Keine erfundenen persönlichen Angaben, Zeichenlimits oder Portalfragen.
- Der optionale LoRA-Vergleich ist im [RF1-Ergänzungsblatt](lora-research-extension-2026-11-19.md) begrenzt; keine zusätzliche Förderforderung, keine Zusage von Modellverbesserung oder Cloud-Förderfähigkeit.
