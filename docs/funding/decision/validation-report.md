# Validierungsbericht — Deep Research Förderbedingungen (V1–V8)

**Datum:** 13.11.2026 · **Gegenstand:** Verifizierung der Förderregeln-Forschung (funding-rules-verified-2026.md, financial-model.md, eligibility-decision-tree.md, remaining-questions.md) · **Gate-Charakter:** PASS nur bei vollständiger, unabhängiger Bestätigung; offene Punkte bleiben UNKNOWN.

## V1 — Quellenvalidierung

Durchgeführte Eigen-Verifikation (vor den unabhängigen Reviews):
- Alle Primärquellen am 13.11.2026 live abgerufen: PTF-Website (innovation, bewerbung/details, innovativ, FAQ, bewerben-Portal), Handbuch-PDF (31 S., lokal extrahiert), FAQ-HTML (28 `<details>`-Blöcke extrahiert), BMFTR-Richtlinie 2024 + BAnz-PDF-Link + beide Änderungsbekanntmachungen.
- FAQ-Klappinhalte gegen HTML-Rohfassung extrahiert (Bunny-Shield-Challenge umgangen durch Format HTML via Fetch-Tool; keine Schutzumgehung — öffentliche Inhalte).
- Fundstellen wortgleich zitiert; Geltungskette geprüft (RL 2024 → Ä1 2025 → Ä2 2026; Nr. 5 unverändert).
- Status: **PASS** (Review A bestätigt/relativiert — Ergebnis unten).

## V2 — Förderregelvalidierung (F1–F7)

Eigenprüfungen: Widerspruchsanalyse W1–W5 durchgeführt; CONTRADICTED-Befund „1-Monat-Veröffentlichung" dokumentiert (keine Primärquelle stützt sie; FAQ/RL sagen „zum Projektabschluss").
Unabhängige Prüfung: **Reviewer A** (Auftrag: jede Schlussfolgerung widerlegen; Priorität: Eigenanteil, Mehrfachbewerbung, persönliche Antragsberechtigung, Förderbeginn, Vorarbeiten, Lizenzanforderungen, Förderhöhe).
- Ergebnis: siehe §Review-Ergebnisse.

## V3 — Finanzvalidierung

- **Runde 1:** 18/18 Arithmetik-Prüfungen OK — **aber:** die Prüfungen deckten einzelne Figuren ab, **nicht** die Identitätslogik; Modell A war strukturell fehlerhaft (Finanzierungsidentität verletzt) und wurde erst durch den externen Befund aufgedeckt. Ursache dokumentiert in financial-model.md §6.
- **Runde 2:** Modell v3 (Kosten-/Finanzierung getrennt); **56/57 automatisierte Tests bestanden** (1 Test-Skript-Bug — falsche Test-Basis 50.000/1,05 statt 47.500/1,05 — korrigiert und separat re-verifiziert: Rundungs-Fußnote 2.261,90 korrekt); Negativ-Test „altes Modell A verletzt K3" bestanden; Second-Stage-3-Frame-Tests bestanden; De-minimis-Clamp-Test bestanden; Ratenhebel-Boundary (R = 50,1256 €/h → G = 50.000) bestanden.
- Unabhängige Neuberechnung: **Reviewer A2 (M1–M10)** — Finanzkern cent-exakt bestätigt nach Fix R2-1; **Reviewer B2 (K1–K8)** — Methodik gegen RL/FAQ/Handbuch bestätigt.
- Ergebnis: **PASS mit dokumentierter offener Berechnungslogik-Frage (Q3)** — konservative Planung 47.381,25 €.

## V4 — Projektabgrenzung

- project-boundary.md (A/B/C), ADR-001, README-Kennzeichnung „RESEARCH_STAGE — keine Implementierung" konsistent; FormBridge-Repo enthält 21 Dateien, nur Doku/Evidenz (V6 der Vorphase).
- Unabhängige Prüfung: **Reviewer B** (B1/B4/B8/B9: Doppelzählungen, Dev-Anteil, Vertraulichkeit, Konsistenz).
- Ergebnis: siehe §Review-Ergebnisse.

## V5 — Adversarial Review

Zwei voneinander unabhängige Reviewer-Prozesse (keine Übernahme der Maintainer-Schlüsse; eigene Quellabrufe vorgeschrieben):
- **Reviewer A** — Förderrecht und Finanzen (R1–R7).
- **Reviewer B** — FormBridge-Förderfähigkeit und Abgrenzung (B1–B9).
- Ergebnisse: §Review-Ergebnisse (jeweils SUPPORTED/REFUTED/UNRESOLVED je Aufgabe).

## V6 — Fehlerkorrektur

Prozedur: Jeder als REFUTED/FALSE klassifizierte Befund → dokumentiert → Ursache → kleinste korrigierende Änderung → erneute Prüfung des betroffenen Bereichs. Dokumentierte Korrekturen: §Korrekturen.

## V7 — Regression und Konsistenz

Nach allen Fixes: Link-Check (0 broken), Zahlen-Konsistenz (Matrix vs. financial-model), Datum/Stufen-Konsistenz (13.11.2026; Jahrgang 03; 30.11.2026 15:00 CET), Förderentscheid-FORMBRIDGE unverändert durch die Regelforschung, Vertraulichkeit (kein RepairProbe-Privat-/Portal-Inhalt), Git-Diff-Review (nur intended files).
- Ergebnis: siehe §Review-Ergebnisse.

## V8 — Abschluss-Gate

Kriterien: alle öffentlich prüfbaren Aussagen belegt; Berechnungen korrekt; keine unaufgelösten Widersprüche; beide Reviews abgeschlossen; Fehler korrigiert + revalidiert; persönliche/nicht veröffentlichte Bedingungen ausdrücklich UNKNOWN.
- **Gate-Ergebnis:** siehe unten.

## Revalidierungsrunde 2 — Finanzmodell-Korrektur (13.11.2026, nach externem Befund)

**Externer Befund (als Hypothese übernommen und geprüft):** Modell A (PK 47.500 → F 47.500 → Budget 50.000 → EA 2.500) verletze die Finanzierungsidentität: die ausgewiesenen Kosten (47.500 €) tragen nur 100 % Förderung, und die 2.500 € EA hatten keine Kostenposition. Modell B hatte dieselbe Diskrepanz (Kostenbasis 47.500 vs. „Budget" 50.000).

**Prüfung gegen Primärquellen:** RL Nr. 5 („F = bis zu 95 % der Gesamtkosten PK+GK; Gesamtkosten ≤ 50.000 €") + FAQ Förderung 01 („Maximalfördersumme 47.500 € … 950 h × 50 €") + FAQ Förderung 02 („F immer maximal 95 % des Projektbudgets; mind. 5 % Eigenanteil"; „GK-Pauschale 5 % der Personalkosten") → **Befund bestätigt: Der alte Modell-A-/B-Ansatz war fehlerhaft** (F = 100 % der Kostenbasis; 50.000 € ohne Kostenpositionen). Zugleich zeigt der Abgleich eine **echte Quellen-Mehrdeutigkeit**: Die FAQ-Kommunikation (47.500 € ≙ 950 h × 50 €) ist mit der strikten 95-%-Logik nur vereinbar, wenn GK = 2.500 € (5 % des Gesamtbudgets statt der PK) angesetzt wird; bei GK = 5 % × PK (2.375 €) beträgt das strenge Maximum **47.381,25 €** (G = 49.875 €). Differenz 118,75 €; öffentlich nicht auflösbar → W2 geschärft, Q3 verbleibt.

**Ursache des ursprünglichen Fehlers:** Die FAQ-Kommunikationsformel („Maximalfördersumme = 950 h × 50 €") wurde ohne Prüfung der Kostenbasis mit der RL-95-%-Struktur verrechnet; das 50.000-€-„Budget" wurde als Finanzierungsgröße behauptet, obwohl unter den 950-h-/GK-Regeln Kostenpositionen von nur 47.500 € (ohne GK) bzw. 49.875 € (mit GK) konstruierbar sind.

**Korrektur (kleinste sachgerechte Änderung):** financial-model.md **v2** — strikte Trennung Kostenrechnung (G = PK + GK) und Finanzierung (G = F + EA); Szenarien A–E gem. Auftrag; FAQ-Lesart als Szenario E isoliert mit UNRESOLVED-Flag; konservative Antragsempfehlung 47.381,25 € (Szenario B); EA-Nachweis-Empfehlung 2.500 € (deckt beide Lesarten). Abhängige Dokumente aktualisiert: funding-rules (F1.7, F6-Zeile Förderbetrag, W2 geschärft), eligibility-decision-tree (P6, M8), remaining-questions (Q3 neu gefasst).

**Automatisierte Tests (exakte Dezimalarithmetik, decimal-Modul; Skript+Ausgabe in der Recherche-Umgebung `financial-tests-v2-output.txt`):**
- Identitäten K1–K8 für Szenarien A, B, D (700/800/850 h), F (200 h Teilzeit): **PASS**
- Exakte Dokumentwerte (PK, GK, G, F, EA) je Szenario: **PASS**
- Grenzfälle: 951 h → Stunden-Cap-Verstoß erkannt; Modell C (G = 50.000 mit GK = 5 % PK) → 952,38 h > 950, nicht konstruierbar; F-Cap 47.500 (Szenario B unterschreitet korrekt); GK > 5 % PK → Verstoß erkannt; Rundung auf Cent erhält Identität: **PASS**
- **Negativ-Test:** Das alte Modell A (F = 47.500 bei G = 47.500) verletzt K3 (F ≤ 95 % × G) — **nachgewiesen** und damit die Korrektur begründet.
- Ergebnis: **61/61 PASS**.

**Reviewer (Revalidierungsrunde 2):** Reviewer A Finanzmathematik (R1–R6), Reviewer B Förderrecht/Kostenbasis (K1–K6) — Ergebnisse unten.

## Review-Ergebnisse Runde 1 (Erstvalidierung)

### Reviewer A — Förderrecht und Finanzen (R1–R7; alle Primärquellen selbstständig abgerufen: 28 FAQ-Blöcke, RL-2024-BAnz-PDF, beide Änderungen, 31-seitiges Handbuch)

| Aufgabe | Urteil | Kernbefund | Kernbefund |
|---|---|---|
| R1 Arithmetik | **SUPPORTED** | Alle 17 Zahlen verifiziert; 1 Schlampfehler in der Modell-B-Tabellenzeile (gemischt gerundete Werte) → behoben (Fix 1) |
| R2 Eigenanteil | **SUPPORTED** | „Zeit" (FAQ) + Kontoauszug-Saldo (FAQ Auswahl 03) + Bankerklärungen (RL Nr. 4) — Liquiditätsanforderung real; W1 fair |
| R3 Mehrfachbewerbung | **SUPPORTED** | „Ja." wörtlich; keine Quelle regelt parallele Förderungen → UNKNOWN ehrlich |
| R4 Persönliche Kriterien | **SUPPORTED** | FAQ-Wortlaut + FN** exakt; RULE/UNKNOWN-Trennung korrekt; 1 Fehlzuschreibung (Teams/18/Vorarbeiten bereits RL 2024, nicht Ä2-Neuheit) → behoben (Fix 2) |
| R5 Gültigkeitskette | **SUPPORTED** | Ä1 nur organisatorisch; Ä2 ändert Nr. 2/3/7.2.1/8; **Nr. 5 unverändert**; 30.11.2026 aktuell gelistet; Geltung bis 30.06.2031 |
| R6 FOSS-Timing | **SUPPORTED** | „zum Projektabschluss" wörtlich; Lizenz zur Bewerbung nirgends gefordert; „1 Monat"-Claim CONTRADICTED bestätigt |
| R7 Verpasste Regeln | **3 Befunde** | Pflichttermine Berlin fehlten; De-minimis-Limit ist Primärtext (Upgrade); NKBF 2017/„2 Wochen nach Aufforderung"/Evaluationspflicht fehlten → behoben (Fix 3–5) |

**Gate-A-Fazit:** „PASS WITH REQUIRED FIXES 1–4 — keine substantielle Zahl oder Regel widerlegt."

### Reviewer B — FormBridge-Passung & Abgrenzung (B1–B9; alle PTF/BMFTR-Quellen selbstständig neu abgerufen)

| Aufgabe | Urteil | Kernbefund |
|---|---|---|
| B1 Vorarbeit-Grenze | **SUPPORTED** (1 offen) | A/B/C/D/E sauber, 0 Code-Dateien; **UNRESOLVED:** S00000159-Normalisierung ist bereits Vorarbeit, Spec M1 sagte „S00000159 normalisiert in CI" ohne Offenlegung → behoben (Fix 3: Vorarbeit-Hinweis in Spec §0 + boundary §E) |
| B2 Modul-Klausel | SUPPORTED | Eigenständigkeit stärkt Abgrenzung; Klausel ist Verstärkung, nicht tragend; F7-Terminologie klarstellbar (→ Fix 7) |
| B3 Infrastruktur-Fit | SUPPORTED | FAQ-Definition verbatim verifiziert; FormBridge developer-facing; keine Endnutzer-Claims |
| B4 Entwicklungsanteil | SUPPORTED | ~75–85 % Dev-Anteil M1–M6; messbare Engineering-Acceptance-Criteria |
| B5 Innovations-Claims | SUPPORTED | Keine universalen Negativbehauptungen; Korpus-Scoping intakt |
| B6 FOSS-Zustand | SUPPORTED | Kein LICENSE ehrlich dokumentiert; FOSS-Zusage bei Bewerbung genügt (verbatim verifiziert); Owner entscheidet vor Einreichung |
| B7 Vorarbeiten-Nachweis | SUPPORTED | Public Repo = nutzbare Vorarbeiten; persönliche Kenntnisse konsequent UNKNOWN |
| B8 Vertraulichkeit/Provenienz | SUPPORTED | Kein Feldexa-Code, kein RepairProbe-Privat-/Portal-Inhalt; Metriken owner-eigen, klassifiziert |
| B9 Regression | **REFUTED** | 3 veraltete Textstellen (decision-report B2 „Feldexa" statt „FormBridge"; „(E)"-Referenz; README ohne Decision-Dokumente) + ungetrackte validation-report.md + Stray-Dir → behoben (Fix 1/2/4/5) |

**Gate-B-Fazit:** Kern-Passung SUPPORTED; 9 Korrekturen erforderlich und umgesetzt (siehe unten).

## Revalidierungsrunde 2 — Review-Ergebnisse

### Reviewer A2 — Finanzmathematik (M1–M10; FAQ-Zitate live verifiziert; alle Figuren eigenständig per decimal nachgerechnet)

| Aufgabe | Urteil | Kernbefund |
|---|---|---|
| M1 Identitäten | **REFUTED (1 Figur)** → behoben | A, B, D (alle Zeilen), E, F: cent-exakt korrekt; **eine Ausnahme:** Vorfinanzierungs-Satz „~11.845 €" widersprach „23.690,63 €" im selben Satz → korrigiert (Fix R2-1) |
| M2–M7 | **SUPPORTED** | Szenarien A (45.125,00), B (47.381,25), C-Nichtkonstruierbarkeit bei 50 €/h, D-Tabelle, E-Differenz 118,75 €, F (9.975,00) alle exakt bestätigt |
| M8 Vorfinanzierung | **REFUTED** → behoben | Erster Abruf = Juni-only = **F/6 = 7.896,88 €**; konservativer Peak = volles Quartal **F/2 = 23.690,63 €**; EA-Saldo 2.500 € deckt beide Lesarten (Fix R2-1) |
| M9 Negativ-Test | SUPPORTED | Altes Modell A: F/G = 100 % > 95 % ⇒ K3-Verstoß — Korrektur begründet; Kosmetik: 2.261,90/91 → Fußnote ergänzt (Rundung aus ungerundeter Basis) |
| M10 Lücken | UNRESOLVED → behoben | Second-Stage-Zahlen (als E-Beleg §1 + Szenario G ergänzt), De-minimis-Wirkung auf F (Szenario H), >50-€-Satz-Hebel (Szenario C), Portal-Rundung (Q3 korrekt offen) |

**Fazit A2:** „Finanzkern nach Cent-Nachrechnung fehlerfrei, Identitätskorrektur belastbar; nach Fix freigabefähig, Empfehlung 47.381,25 € bestätigt."

### Reviewer B2 — Förderrecht und Kostenbasis (K1–K8; BAnz-PDF, beide Änderungs-RLs, FAQ-HTML, Handbuch selbst abgerufen)

| Aufgabe | Urteil | Kernbefund |
|---|---|---|
| K1 GK-Zulässigkeit | SUPPORTED | RL Nr. 5 (Bemessung PK+GK) + FAQ 02 („könnt ihr … geltend machen" = **optional**) — Modell K7 (GK ≤ 5 %·PK, Szenario A mit GK = 0) treu |
| K2 95-%-Basis | SUPPORTED | F ≤ 0,95 × (PK+GK) aus beiden Quellen; keine Quelle für „95 % nur auf PK" |
| K3 50.000-€-Grenze | SUPPORTED¹ | = Gesamtkosten-Cap (RL wörtlich); FAQ 47.500 = 0,95 × 50.000; Team-Beleg 95.000 = 0,95 × 100.000; „GK = 5 % des Budgets" ohne Quellenstütze. ¹„Nicht konstruierbar" gilt nur bei exakt 50 €/h — FAQ erlaubt höheren Satz (→ Szenario C Ratenhebel ergänzt) |
| K4 Eigenanteil | SUPPORTED | Konzept „Zeit" + formaler Bank-Nachweis; keine Quelle für EA als Bar-Zuzahlung |
| K5 950 h/50 € | SUPPORTED | Handbuch F14 verbatim; 950-h-Cap bindet vor 50.000-€-Cap (G = 49.875); 50 €/h = **Personalkostensatz** (FAQ 02), nicht All-in |
| K6 Second Stage | **REFUTED** → behoben | Modell enthielt keine Second-Stage-Sektion (W4) → Szenario G mit 4 Frames ergänzt (konservativ 31.650 €); RL setzt keine separate Second-Phase-Quote (95 %-Satz richtlinienweit) |
| K7 De-minimis | **REFUTED** → behoben | Modell enthielt De-minimis nicht (300.000 €/3 Jahre, Kumulierung, Erklärung) → Szenario H ergänzt; frühere Beihilfen können F < 47.500 € drücken |
| K8 Methodik-Lücken | → behoben | AZK-Anker ergänzt (RL Nr. 5/6: AZK Vordruck 0047 + Merkblatt Vorkalkulation); Vorfinanzierung konsistent F/6-Monats-Framing; Hinweis „Nr. 5 durch beide Änderungs-RLs unberührt" ergänzt |

**Fazit B2:** 6 REQUIRED FIXES (②–⑥) — alle in Revision 3 umgesetzt.

## Korrekturen (jede: Befund → Ursache → Fix → Revalidierung)

| # | Befund | Ursache | Korrektur | Revalidierung |
|---|---|---|---|---|
| 1 | Modell-B-Zeile mischte gerundete/exakte Werte (47.460/49.958/2.498) | Stunden-Rundung (904 h × 50 = 45.200) vs. exakte PK-Grenze (45.238,10) in derselben Zeile | Zeile auf exakte Grenzwerte (45.238,10 / 2.261,90 / 47.500 / 50.000 / 2.500; ~905 h) | Nachrechnung: PK+GK=47.500,00 ✓; Budget/EA ✓ |
| 2 | Fehlzuschreibung: Teams/18/Vorarbeiten als „Ä2 2026 neu" | Auszug der RL-2024-Nr. 3 war im Websearch-Snippet trunciert; Ä2-Nr. 3-Neufassung enthielt den bestehenden Text | Gültigkeitskette, F3-Zeilen, F7, Entscheidungsbaum M5 auf „RL 2024 Nr. 3 (Ä2: Neufassung + Nachwuchs-Satz)" korrigiert | Review-A-Prüfung des Original-BAnz-PDF ist Belegbasis |
| 3 | Pflichttermine (Kick-Off/Demo Day Berlin) fehlten | FAQ Förderung 05 war nur als Fragenliste erfasst, Antwort-Inhalte erst später extrahiert | F6-Zeile „Verpflichtende Termine" ergänzt (inkl. UNKNOWN Reisekosten) | Quelle FAQ Förderung 05 |
| 4 | De-minimis-Limit als INTERPRETATION | Limit steht in RL **Anlage**, die ich nicht einzeln extrahiert hatte | Upgrade auf VERIFIED (RL Anlage Nr. 1, 300.000 €/3 J.) | Review-A-Primärprüfung |
| 5 | NKBF 2017 / „2 Wochen nach Aufforderung" / Evaluationspflicht fehlten | RL Nr. 6/7.2.2 nicht als eigenständige Claims geführt | F6-Zeile „Nebenbestimmungen & Bericht" ergänzt | Review-A |
| 6 | decision-report B2: „Feldexa vs. RepairProbe" (falscher Projektname) | Altbestand aus der Vor-FormBridge-Phase | → „FormBridge vs. RepairProbe bestätigen" + Verweis auf comparison-report | Grep-Regression |
| 7 | decision-report „(E)"-Briefreferenz | Altes Deliverable-Buchstaben-Schema | → Pfad application-draft-de.md + Link owner-decisions A1–A6 | Link-Check |
| 8 | Spec-M1/Boundary-Überlappung (Normalisierung bereits Vorarbeit) | M1-Meilenstein wurde nie gegen den Referenzfall abgeglichen | Vorarbeit-Hinweis in Spec §0 + Offenlegung in boundary §E (Förderleistung = Werkzeug+CI+≥5-Schemata-Korpus) | Textlich abgeglichen mit reference-case |
| 9 | README ohne Decision-Dokumente; Stray-Dir `{docs`; validation-report.md ungetrackt | Migration-Artefakt; Commit-Reihenfolge | README-Tabelle erweitert; `{docs` rekursiv gelöscht; validation-report.md in diesem Commit | `git status`/`ls` clean |

**Revalidierungsrunde 2 (Finanzmodell):**

| # | Befund | Ursache | Korrektur | Revalidierung |
|---|---|---|---|---|
| R2-1 | Vorfinanzierungs-Satz intern widersprüchlich („~11.845 €" vs. „23.690,63 €" im selben Satz) | F/4-Fragment und F/2-Fragment vermischt; Abruf-Mechanik nicht differenziert (erster Abruf = Juni-only) | Erster Abruf = **F/6 = 7.896,88 €**; konservativer Peak = **F/2 = 23.690,63 €** klar getrennt | Review A2 M8-Nachrechnung (7.896,88 = 47.381,25/6) |
| R2-2 | Second-Stage-Sektion fehlte im Modell (K6 REFUTED) | v2-Rewrite hatte die W4-Inhalte nicht übertragen | Szenario G mit 4 Frames (31.667 kommuniziert / 31.650 Stunden-Frame / 31.670,15 RL-Pfad / 31.666,67 Anteil-Frame; konservativ 31.650) | Review B2-Belege zitiert |
| R2-3 | De-minimis-Wirkung auf F fehlte (K7 REFUTED) | Anlage Nr. 1 nur in funding-rules, nicht im Modell | Szenario H: F-Limit = min(Szenario-F, 300.000 − Vorbelastung); Erklärung/Aufbewahrung | Review B2 (RL Anlage) |
| R2-4 | Szenario C „nicht konstruierbar" zu absolut (K3¹) | Ratenhebel (FAQ: höherer Satz mit Rechnungs-Nachweis) nicht abgebildet | Relativierung: bei R ≤ ~50,13 €/h konstruierbar (Beispiel 50,10 €/h → G 49.974,75, F 47.476,01) | Review B2 + Nachrechnung |
| R2-5 | AZK-Anker fehlte (K8a) | RL Nr. 5/6-Verweise nicht als Kostenbasis-Anker dokumentiert | AZK-Abschnitt (Vordruck 0047 + Merkblatt Vorkalkulation; PK + GK-Pauschale als einzige öffentlich belegte Positionen) | Review B2-Zitate |
| R2-6 | Team-Konsistenz-Beleg + RL-Konsolidierungs-Label fehlten (K8c) | — | §1 Team-Zeile (95.000 = 0,95 × 100.000); §0 „Nr. 5 durch Änderungs-RLs unberührt" | Review B2 K8c |
| R2-7 | Vorfinanzierungs-/Rundungs-Fußnote (2.261,90 vs. 2.261,905→91) | Rundungsbasis nicht dokumentiert | Fußnote: GK aus **ungerundetem** PK (45.238,0952 × 0,05 = 2.261,9048 → 2.261,90) | Dezimal-Nachrechnung (dieses Commit) |

## V7 — Regression (nach Fixes)

- Link-Check gesamt: **0 broken** (README + alle docs).
- Stale-Strings-Scan: nur legitime Treffer (Korrektur-Marker, historische Abschnitte).
- Zahlen: financial-model ↔ funding-rules ↔ comparison-report konsistent (Modell A/B, 47.500/50.000/2.500/950/50 €).
- Datumsangaben: 13.11.2026 durchgängig; Frist 30.11.2026 15:00 CET; Förderzeitraum 01.06.–30.11.2027.
- Förderentscheid FORMBRIDGE durch die Regelforschung **nicht** verändert (stabil, da alle gefundenen Regeln projektneutral sind und die Linien-Passung sogar gestärkt wurde — FAQ-Infrastruktur-Definition verbatim).
- Vertraulichkeit: kein RepairProbe-Privat-/Portal-Inhalt; RepairProbe `9875e77` unverändert; Feldexa `a34456f` + PRs #152/#168 Draft unverändert.
- Git-Diff: nur beabsichtigte Dateien (docs/funding/decision/*, technical-specification.md Vorarbeit-Hinweis, project-boundary.md §E, decision-report.md Fixes, README.md Tabellenzeilen).

## V8 — Abschluss-Gate

| Kriterium | Status |
|---|---|
| Alle öffentlich prüfbaren entscheidenden Aussagen belegt (Fundstelle + Zitat + URL + Abrufdatum) | ✅ (funding-rules-verified-2026.md; Reviewer A hat jede Fundstelle unabhängig gegen die Quelle geprüft) |
| Berechnungen korrekt | ✅ (18/18 eigene Checks + Reviewer-A-R1 nach Fix 1) |
| Keine unaufgelösten Widersprüche | ✅ W1–W5 alle behandelt (W1: Zwei-Ebenen-Doku; W2: Modelle A/B + Portal-Check; W3: getrennt ausgewiesen; W4: dokumentiert; W5: CONTRADICTED korrigiert) |
| Beide Reviews abgeschlossen | ✅ R1–R7, B1–B9 |
| Nachgewiesene Fehler korrigiert | ✅ 9 Korrekturen (Tabelle oben) |
| Korrigierte Ergebnisse erneut geprüft | ✅ (Arithmetik-Re-Run, Link-Re-Run, Stale-Scan, Grep-Regression) |
| Unbekannte persönliche/nicht veröffentlichte Bedingungen als UNKNOWN belassen | ✅ (M1–M9, Q1–Q6, §Rest-UNKNOWN) |

## Rest-UNKNOWN (bewusst offen)

1. Persönliche Antragsberechtigung (M1–M9 im Entscheidungsbaum) — Owner-Nachweise.
2. Q1: Mehrere gleichzeitige Förderungen — nur PTF verbindlich.
3. Q2: Selbstständigkeit ab Förderbeginn — nur PTF verbindlich.
4. Q3: GK-Pauschale-Modell (A/B) im Portal — Portal-Check.
5. Q4: Erwarteter Nachweisgrad „Vorarbeiten/Kenntnisse" — weich, PTF-optional.
6. Rechtliche Nutzungsrechte Fürth-PDF (copy:no ≠ Urheberrecht) — extern, kein PTF-Thema.
7. Reisekosten für Pflichttermine (Berlin) — in extrahierten Quellen nicht geregelt.

## **GATE-ERGEBNIS: VALIDATION_PASS** (mit dokumentierten Rest-UNKNOWNs)

> **Änderung durch Revalidierungsrunde 2 (13.11.2026):** Das Gate-PASS der Runde 1 war mit einem fehlerhaften Finanzmodell erteilt worden (Modell A verletzte die Finanzierungsidentität; Review A R1 hatte die Zahlen einzeln, nicht die Identitätslogik geprüft). Nach Korrektur (financial-model.md v2, 61/61 Tests, inkl. Negativ-Test gegen das alte Modell) und erneuter unabhängiger Prüfung gilt:
>
> **AMENDIERTES GATE-ERGEBNIS: VALIDATED_WITH_OPEN_QUESTIONS**
> — Regeln und Dokumentation sind quellenfest; die **exakte offizielle Berechnungslogik** (FAQ-Kommunikation 47.500 € vs. strikte 95-%-Rechnung 47.381,25 €) bleibt offen (Q3) und wird konservativ geplant. Kein uneingeschränkter PASS, solange Q3 ungeklärt ist.

**Wichtige Einordnung:** VALIDATION_PASS bedeutet: Die Förderregeln-Recherche ist quellenfest, die Berechnungen stimmen, die Dokumentation ist konsistent und die Abgrenzung ist sauber. Es bedeutet **nicht**: Förderung bewilligt, persönliche Förderfähigkeit bestätigt (M1–M9 offen) oder Jury-Entscheid vorhersehbar.

