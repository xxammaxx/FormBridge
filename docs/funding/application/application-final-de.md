# FormBridge — Bewerbung Prototype Fund 2027, Jahrgang 03, Förderlinie Innovation

**Status:** Einreichungsentwurf zur Owner-Freigabe · **Datum:** 20.11.2026 (RF1-Offline-Nachweis) · **Wortzählung verifiziert:** 25.11.2026 · **§11/§14/E2–E4/S1/Q19 final:** 25.11.2026 · **Frist:** 30.11.2026, 15:00 Uhr MEZ
**Förderzeitraum:** 01.06.2027–30.11.2027 · **Antragstellerin:** Einzelperson · **Projekt:** FormBridge
**Lizenz:** Apache-2.0 (Eigentümerentscheidung 25.11.2026; `LICENSE` im Repository, SPDX `Apache-2.0`). Die FOSS-Zusage in §18 bleibt unabhängig davon erforderlich.
**Wichtig:** Dieser Text enthält Platzhalter für persönliche Angaben. Er ist **kein** eingereichter Antrag. Es wurden keine persönlichen Daten erfunden. Exakte Portal-Zeichenlimits sind `PORTAL_UNVERIFIED`.

**Wortlimits:** aus dem offiziellen PTF-Handbuch Jahrgang 03 (Fragen 2–19). **Zählregel (reproduzierbar, Stand 25.11.2026):** gezählt wird der Antworttext eines Abschnitts ohne die `**Wörter:**`-Metazeile, getrennt an Whitespace (`len(text.split())`); Platzhalter in eckigen Klammern zählen mit und werden zusätzlich getrennt ausgewiesen. Das Portal kann anders zählen und zusätzlich Zeichenlimits erzwingen; diese wurden nicht eingesehen (`PORTAL_UNVERIFIED`). Alle Abschnitte liegen innerhalb der dokumentierten Limits.

---

## 1. Projekt in einem Satz (max. 30 Wörter)

FormBridge ist ein geplantes freies, lokal laufendes Softwaremodul, das statische Behörden-PDFs analysiert, Formularfelder nachvollziehbar versionierten FIM-Datenfeldern zuordnet und prüfbare, strukturierte Ergebnisse bereitstellt.

**Wörter:** 22 / 30 · **Status:** FINAL

---

## 2. Projektbeschreibung (max. 100 Wörter)

Im Förderzeitraum entsteht eine eigenständige Open-Source-Bibliothek mit CLI. Sie erkennt Formularfelder in nicht interaktiven, born-digitalen Behörden-PDFs und ordnet sie nachvollziehbar versionierten FIM-Datenfeldern zu. Unsicherheit bleibt UNKNOWN; Menschen prüfen kritische Vorschläge. Parallel zur regelbasierten Modulentwicklung untersuche ich optional, ob direkt berechnete LoRA-Adapter kleine lokale Sprachmodelle ohne erneutes Gradiententraining gezielt verbessern. Die Inferenz bleibt offline; ein unabhängiger Verifier prüft die Provenienz. Entstehende eigene Analyse-, Adapter- und Testwerkzeuge werden nach Rechteklärung offen veröffentlicht, auch bei negativen Ergebnissen. Referenz ist Wohngeld S00000159. Scans, Produkt-UI und Behördenanschluss bleiben ausgeschlossen; der Kern ist ohne KI nutzbar.

**Wörter:** 90 / 100 · **Status:** FINAL (Entwurf)

---

## 3. Gesellschaftliche Herausforderung (max. 175 Wörter)

Ein Teil der amtlichen Formulare wird als statische PDF bereitgestellt und ist nicht interaktiv ausfüllbar. Bei der digitalen Bearbeitung können manuelle Felderfassung, doppelte Eingaben oder externe Dienste erforderlich werden. Der eGovernment MONITOR 2026 zeigt: 50 % erledigten ihr letztes Anliegen vollständig offline, 24 % nutzten einen Medienbruch; 68 % davon unfreiwillig. Die Studie misst Medienbrüche allgemein, nicht PDFs als Ursache. Im geprüften Referenzfall, dem Fürther Wohngeldantrag, liegt genau ein solches statisches PDF vor. Gleichzeitig fehlt in den geprüften offenen Projekten eine offene, prüfbare Brücke zwischen dem sichtbaren PDF und den versionierten FIM-Datenfeldern, die Verwaltungsverfahren bereits beschreiben.

Besonders relevant ist diese Lücke für Anträge mit sensiblen Daten, etwa Sozialleistungen, sowie für Beratungsstellen und Kommunen. FormBridge setzt nicht beim Endnutzer, sondern bei der Software an, die solche Anträge baut: Wenn Zuordnungen nachvollziehbar und unsicherheitsbewusst sind, können darauf aufbauende Anwendungen Medienbrüche reduzieren, ohne vertrauliche Daten an einen zentralen Dienst zu geben. Das ist kein Ersatz für Rechtsberatung oder Behördenentscheidungen, sondern eine technische Grundlage für verlässlichere digitale Verfahren. Nachnutzbare Werkzeuge können weitere Digitalisierungsprojekte unterstützen.

**Wörter:** 170 / 175 · **Status:** FINAL

---

## 4. Technische Umsetzung (max. 175 Wörter)

FormBridge entsteht als Python-Bibliothek mit CLI und API. PDF-Textlage und Layout werden extrahiert; ein versionierter Regelkatalog ordnet Label und Abschnittskontext gültigen FIM-Zielpfaden zu. Kandidaten werden gegen Schema und Codelisten geprüft, mit Koordinaten und Confidence. Unsicherheit bleibt UNKNOWN; kritische Zuordnungen erfordern menschliche Freigabe. Der obligatorische Regelkern funktioniert offline ohne KI. Parallel zur weiteren Entwicklung untersuche ich optional kleine lokale Modelle mit direkt berechneten, reversiblen LoRA-Adaptern ohne Gradiententraining. Verglichen werden Regeln, unverändertes Modell und Adapter bei einer Mehrdeutigkeitsklasse. Bei fehlendem Mehrwert auf ungesehenen Fällen bleibt KI deaktiviert. Inferenz und Adapterversuche bleiben lokal. Ein Controller koordiniert Modell und deterministische Skripte. Externe KI liefert höchstens maschinenlesbare Hypothesen zu synthetischen Tests; reale Dokumente, OCR-Texte und daraus abgeleitete Daten bleiben lokal. Ich verantworte und prüfe die Entwicklung. Netzgesperrte Abnahme, Modell-/Adapterhashes und reproduzierbare Messberichte belegen den Betriebsweg. Das FB-1-Manifest und ein unabhängiger Verifier dokumentieren PDF-, Schema-, Review- und gegebenenfalls Adapterprovenienz. Ausgabevalidierung erfolgt gegen dokumentiert normalisiertes XSD bzw. FITKO-JSON-Schema. Eigene entstandene Forschungswerkzeuge und Ergebnisse werden nach Rechteklärung offen veröffentlicht. Keine Feldexa-Abhängigkeit, keine Behördenübermittlung.

**Wörter:** 165 / 175 · **Status:** FINAL (Entwurf)

---

## 5. Aktueller Stand und geplante Neuerungen (max. 100 Wörter)

Die Idee ist erforscht, das Modul ist nicht implementiert. Vorarbeit: Prior-Art-Audit über 13 Projekte, Fürther Wohngeldantrag/FIM S00000159 v1.4, 30-Feld-Referenzdatensatz, Spezifikation und 170 XSD-Parser-Meldungen (1 NCName + 169 D2). Separate Homelab-Erfahrungen mit lokaler Dokumentenverarbeitung und Qwen illustrieren vorhandene praktische Infrastruktur; sie sind kein FormBridge- oder Adapter-Nutzennachweis. Der LoRA-Versuch ist konzipiert, nicht ausgeführt. Vorarbeiten werden nicht abgerechnet. Im Förderzeitraum entstehen eigenständiger Regelkern, Review, Verifier, Testkorpus und optional der lokale Adaptervergleich mit nachnutzbaren Forschungswerkzeugen. Feldexa bleibt unabhängiges, nicht gefördertes Produkt.

**Wörter:** 77 / 100 · **Status:** FINAL (Entwurf)

---

## 6. Link zum bestehenden Projekt (optional)

https://github.com/xxammaxx/FormBridge

**Hinweis:** Das Repository ist derzeit Forschungsstand (Dokumentation, Evidenz, Spezifikation); es enthält **keinen** Produktcode für die geplante Pipeline.

---

## 7. Innovation (max. 100 Wörter)

FormBridge kombiniert statisches Behörden-PDF, versionierte FIM-IDs, UNKNOWN, menschliche Freigabe, überprüfbare Provenienz und unabhängigen Verifier. Formularagent migriert Definitionen ohne PDF-Eingang, KIWO extrahiert cloudbasiert ohne FIM-Koordinaten, CommonForms erkennt Felder ohne FIM-Semantik; FITKO liefert Schema-Infrastruktur. Im begrenzten 13-Projekte-Audit fehlte die Gesamtkette; geeignete Bausteine werden nach Rechteprüfung nachgenutzt. Parallel untersucht RF1, ob direkt berechnete LoRA-Adapter auf verfügbarer älterer Hardware lokal einen messbaren Zuordnungsvorteil bringen. Offene, reproduzierbare Adapter- und Prüfwerkzeuge könnten anderen Digitalisierungsprojekten ressourcenschonende KI-Anpassungen ermöglichen. Auch negative Befunde werden dokumentiert. Keine behauptete Erstmaligkeit, kein bereits belegter Modell- oder Ressourcenvorteil.

**Wörter:** 85 / 100 · **Status:** FINAL (Entwurf)

---

## 8. Zielgruppe und Zugang (max. 100 Wörter)

Primär: Entwickler*innen und Maintainer freier Verwaltungssoftware, Entwickler*innen in Kommunen und IT-Dienstleistern sowie die FIM-/OZG-Community. Sie erhalten eine Bibliothek und CLI, die sie in eigene Produkte integrieren können. Erreicht werden sie über das öffentliche GitHub-Repository, technische Dokumentation, Vorträge und Austausch im FIM-/FITKO-Umfeld sowie über bestehende Open-Source-Netzwerke. Open Source, damit andere Infrastruktur und gegebenenfalls entstehende Adapterwerkzeuge prüfen, erweitern und unabhängig betreiben können. Sekundär profitieren Bürger*innen und Verwaltungsmitarbeitende über Anwendungen, die FormBridge einsetzen. Eine direkte Endnutzer-UI ist nicht Teil des Vorhabens; Feldexa 2.0 ist die vorgesehene erste Anwendung, aber nicht integriert und nicht Teil des Förderumfangs.

**Wörter:** 93 / 100 · **Status:** FINAL

---

## 9. Meilensteine im Förderzeitraum (max. 100 Wörter)

1. Monat: CLI-Grundgerüst, PDF-Textlage, Schema-Hash, FB-1, Normalisierung und CI.
2. Monat: Regelkatalog, Feldkandidaten, Confidence/UNKNOWN, erste End-to-End-Tests.
3. Monat: Goldstandard, Review-CLI, Codelisten, Baseline; externe Testpersonen gewinnen.
4. Monat: Abschnitts-Disambiguierung, Hard Gates, Held-out-PDF; parallel optionaler lokaler LoRA-Vergleich samt Offline-Nachweis bei gesichertem Kernfortschritt.
5. Monat: Emit/Validate/Verify, 10 Negativtests, ≥ 3 FIM-XSDs (5 Stretch).
6. Monat: Review-Zeit, Dokumentation, FOSS-Release, Abschlussbericht einschließlich nachnutzbarer RF1-Artefakte und negativer Ergebnisse, sofern der Versuch stattfindet.
Jeder Meilenstein endet mit reproduzierbarem Testlauf und öffentlichem Bericht.

**Wörter:** 75 / 100 · **Status:** FINAL (Entwurf)

---

## 10. Team — Ja/Nein (zweiter Teil nur bei Team; max. 30 Wörter)

**Antwort:** Nein, ich bewerbe mich als Einzelperson.

**Wörter:** 7 / 30 · **Status:** FINAL

---

## 11. Bisherige Softwareprojekte (max. 100 Wörter; max. 3 Beispiele)

Als Alleinentwickler konzipiere, implementiere und teste ich:
1. Feldexa 2.0 (https://github.com/xxammaxx/Feldexa_2.0): Android-App für digitale Formulare mit PDF-Import, lokaler Verarbeitung und verschlüsselter Ablage (Überführung meiner privaten Vorarbeit Umliva in modulare Open-Source-Bausteine).
2. FormBridge (https://github.com/xxammaxx/FormBridge): Öffentliche Vorarbeiten zur Zuordnung statischer Wohngeld-PDFs zu FIM-Datenfeldern inkl. XSD-Defektanalyse, Referenzdatensatz und Prior-Art-Audit. Parallel bereite ich dort einen lokalen Vergleichsversuch vor, der prüft, ob ein kleines Offline-Sprachmodell mit direkt berechnetem, reversiblem LoRA-Adapter mehrdeutige Formularfelder besser zuordnen kann als regelbasierte Zuordnung oder das unveränderte Modell.

**Wörter:** 77 / 100 · **Status:** FINAL

---

## 12. Förderfähigkeit — Q4 Ja/Nein und Q5 Erläuterung

**Q4 — Bist du Gesellschafter*in einer GmbH/anderen Unternehmensform, hast du einen Verein/eine Organisation gegründet oder arbeitest du für einen thematisch verbundenen Verein, ein Forschungsinstitut o. Ä.?**

**Antwort:** Nein. *(Owner-Bestätigung 25.11.2026)*

**Q5 — nur falls Q4 = Ja: Wenn ja, erläutere, weshalb das Projekt nicht dazu dient, eine für den eigenen Geschäftsbetrieb benötigte Software zu entwickeln (max. 60 Wörter).**

Entfällt (Q4 = Nein). Vorlagetext, nur relevant, falls sich diese Angabe ändert: „FormBridge ist ein eigenständiges Gemeinwohlprojekt und keine Auftragsentwicklung für einen Geschäftsbetrieb.“

**Wörter Q5:** entfällt bei Q4 = Nein (Vorlagetext 11 / 60) · **Status:** FINAL (entfällt bei Nein / Vorlagetext nur falls relevant)

---

## 13. Arbeitsstunden (Zahl)

**Antwort:** 950

**Begründung:** 950 h entsprechen der maximalen Stundenzahl für Einzelpersonen; die Aufteilung ist im [Sechs-Monats-Plan](six-month-development-plan.md) dokumentiert. Eine realistische 850-h-Variante liegt in [budget-final.md](budget-final.md).

**Status:** FINAL (950; Owner-Entscheidung 25.11.2026)

---

## 14. Motivation / Wild Card (max. 100 Wörter)

Ich bin technischer Autodidakt mit praktischer Erfahrung in CNC-Zerspanung, Elektronik, Reparatur und Automatisierung. Aus dieser Praxis bringe ich den Anspruch an klare Toleranzen und reproduzierbare Prüfungen in meine Softwareprojekte ein: Ich formuliere Anforderungen, entwickle Datenmodelle, Skripte und automatisierte Tests und prüfe Ergebnisse systematisch anhand konkreter Anwendungsfälle. Diese experimentelle Arbeitsweise bringe ich auch in die parallele Offline-LoRA-Forschung ein. Aus eigener Erfahrung kenne ich die Hürden beim Ausfüllen von Behördenformularen. Mit FormBridge möchte ich die Verarbeitung solcher Formulare nachvollziehbar machen und sensible Daten lokal halten.

**Wörter:** 83 / 100 · **Status:** FINAL

---

## 15. Second Stage — Ja/Nein

**Antwort:** Ja. *(Owner-Entscheidung 25.11.2026)*

**Begründung:** FormBridge ist Infrastruktur; der Prototyp allein erzeugt noch keine Nutzung. Die Second Stage ist für Integration, Dokumentation und Pflege sinnvoll.

**Status:** FINAL (Ja)

---

## 16. Second Stage — Schwerpunkt (max. 175 Wörter)

Nach dem Prototyp braucht FormBridge vor allem Adoption und Pflege, nicht mehr Funktionsumfang. In vier Monaten will ich: (1) eine externe Integration begleiten und optional eine kommunale Testumgebung prüfen; Feldexa 2.0 bleibt optionaler Consumer, nicht geförderte Integration; (2) Integrationsrezepte, stabile Schnittstellen und Beispieldaten veröffentlichen; (3) eine kleine Regelkatalog- und Schema-Community aufbauen, mit dokumentiertem Review- und Release-Prozess; (4) Nutzertests zur Verständlichkeit von UNKNOWN und zur Review-Zeit durchführen; (5) einen Wartungsplan und eine Governance-Skizze für die Zeit nach der Förderung erstellen. Erfolg wäre: mindestens eine externe Integration, eine veröffentlichte Version 0.2 und ein dokumentierter Pflegeweg. Keine neuen Kernfunktionen, keine Produkt-UI.

**Wörter:** 98 / 175 · **Status:** FINAL (Second Stage = Ja)

---

## 17. Second Stage — Meilensteine (max. 100 Wörter)

1. Monat: Integrationsgespräche, Anforderungsaufnahme, stabile Schnittstellenversion.
2. Monat: Erste externe Integration, Integrationsrezepte und Beispieldaten.
3. Monat: Nutzertests zu UNKNOWN/Review-Zeit, Community-Austausch, Dokumentation.
4. Monat: Version 0.2, Wartungs- und Governance-Skizze, Abschlussbericht.

**Wörter:** 29 / 100 · **Status:** FINAL (Second Stage = Ja)

---

## 18. Bestätigungen (Handbuch Q19; Portal-Checkbox unverified)

- [x] „Ich bin über 18 Jahre alt und habe meinen Hauptwohnsitz in Deutschland.“ (Handbuch JG03, Q19, Sept. 2026)
- [x] „Ich bin damit einverstanden, die Projektergebnisse unter einer Open-Source-Lizenz (z. B. MIT-Lizenz), öffentlich zugänglich (z. B. über Github/Gitlab/Codeberg) zur Verfügung zu stellen.“ (Handbuch JG03, Q19, Sept. 2026)

**Status:** FINAL (Owner-Bestätigung 25.11.2026; beide Zusagen erteilt, Portal-Checkbox noch zu setzen) · **Hinweis:** Q19 steht **nicht** im Fragen-PDF Innovation, sondern im Handbuch und in der Portal-Checkbox; die exakte Live-Formulierung ist `PORTAL_UNVERIFIED`.

---

## Anhang: Was hier bewusst nicht steht

- Keine Behauptung, FormBridge sei bereits implementiert.
- Keine Behauptung, Feldexa 2.0 sei bereits integriert.
- Keine Behauptung, eine Behörde akzeptiere die Ausgabe.
- Keine weltweite Erstmaligkeitsbehauptung.
- Keine erfundenen persönlichen Angaben, Zeichenlimits oder Portalfragen.
- Der optionale LoRA-Vergleich ist im [RF1-Ergänzungsblatt](lora-research-extension-2026-11-19.md) begrenzt; keine zusätzliche Förderforderung, keine Zusage von Modellverbesserung oder Ressourceneinsparung; RF1 ausschließlich lokal. Die Nachnutzung eigener Forschungsartefakte ist ein zusätzlicher Gemeinwohlbeitrag, kein zweiter Fördergegenstand.
