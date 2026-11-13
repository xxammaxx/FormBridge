# Portal-Preflight — Jahrgang 03 Innovation (Stand 14.11.2026)

**Zweck:** Den tatsächlichen Stand der Online-Bewerbung dokumentieren, die öffentlich belegbaren Portalfelder gegen die vorhandene Fassung prüfen und die verbleibenden Owner-Aktionen benennen. **Keine Einreichung, keine Kontoerstellung, keine E-Mail.**
**Status:** **READY_WITH_EXPLICIT_BLOCKERS** — Bewerbungstext und Feldvorlage sind vorbereitet; der Live-Abgleich ist ohne Owner-Login nicht möglich, persönliche Angaben fehlen, und die formale Q2-Zulassungsvoraussetzung ist derzeit **nicht erfüllt**.

## 1. Portalzugriff — tatsächlich geprüft

| Prüfung | Ergebnis |
|---|---|
| `https://bewerben.prototypefund.de/` | HTTP 200; öffentliche Landingpage mit „Log in or Sign up“ |
| `https://bewerben.prototypefund.de/jahrgang-03-innovation/` | Redirect auf `/auth/?next=/jahrgang-03-innovation/` |
| Bestehende authentifizierte Sitzung | **nein**; keine Tabs/Session, keine Zugangsdaten |
| Login/Registrierung | **nicht durchgeführt** — einmalige Owner-Aktion; kein Konto angelegt |
| Formularfelder live | **nicht eingesehen** — `PORTAL_UNVERIFIED` |
| Zeichenlimits live | **nicht eingesehen** — `PORTAL_UNVERIFIED` |
| Pflichtfeldmarkierungen live | **nicht eingesehen** — `PORTAL_UNVERIFIED` |
| RepairProbe-Draft | **nicht geöffnet, nicht verändert** |

**Einmalige Owner-Aktion:** Im Portal anmelden bzw. ein Konto anlegen, Jahrgang 03 Innovation öffnen und den Live-Abgleich durchführen. Der Agent darf kein Konto anlegen und keine Zugangsdaten verarbeiten.

**Schnellster Q2-Kanal:** Bewerbungssprechstunde am **16.11.2026, 17:00 Uhr** (online, siehe Detailseite). Dort kann die materielle Selbstständigkeitsfrage vor der Einreichung geklärt werden.

## 2. Verifizierte offizielle Fragen und Limits

| Quelle | Prüfung | Ergebnis |
|---|---|---|
| Fragen-PDF Innovation, 8 S. | SHA-256 | `1d6848c41ebddf0e381c0708e89b7e23c0644234bf36c7ace9fd1891e2c4fb74` — unverändert |
| Fragen-PDF | Feldumfang | Allgemeine Angaben; Projekt 1–9; Team/Erfahrung 1–7; Second Stage 1–3; **kein Steuernummer-/Selbstständigkeitsfeld** |
| Handbuch JG03 (Sept. 2026) | Wortlimits | 30 / 100 / 175 / 175 / 100 / optional / 100 / 100 / 100 / 30 / 100 / 60 / Zahl / 100 / Ja-Nein / 175 / 100 |
| Handbuch JG03 | zwingende Förderbedingungen | FOSS, Einzelpersonen/Teams ≤ 4, keine Unternehmen/Hochschulen/Institute/Vereine, verständlich, Wortlimits; **Selbstständigkeit nicht genannt** |
| Bewerbungsseite/FAQ | materielle Voraussetzung | Einzelpersonen „selbstständig oder Freiberufler*innen“ **oder** Arbeitgeber-Freistellung |
| Detailseite | Frist/Ablauf | Bewerbung bis 30.11.2026, 15:00 MEZ; Auswahl Dez 2026–Feb 2027; Rückmeldung März; Antragswerkstatt März; zugleich „bis Ende Februar“ |

## 3. Feldvorlage — Status je Feld

### A. Allgemeine Angaben

| # | Feld | Vorlage | Status |
|---|---|---|---|
| A1 | Projekttitel | „FormBridge“ | **FINAL** |
| A2 | Accountname | `[OWNER_ANGABE]` | **OWNER** |
| A3 | Vorname / Name | `[OWNER_ANGABE]` | **OWNER** |
| A4 | E-Mail-Adresse | `[OWNER_ANGABE]` | **OWNER** |
| A5 | Persönlicher GitHub-/Bitbucket-Link | `[OWNER_ANGABE]` | **OWNER** |
| A6 | Link zum Projekt (Q6) | `https://github.com/xxammaxx/FormBridge` | **FINAL** |

### B. Dein Projekt

| # | Frage | Limit | Vorlage | Status |
|---|---|---:|---|---|
| P1 | Projekt in einem Satz | 30 W. | §1 (22 W.) | **FINAL** |
| P2 | Projekt kurz beschreiben | 100 W. | §2 (96 W.) | **FINAL** |
| P3 | Gesellschaftliche Herausforderung | 175 W. | §3 (169 W.) | **FINAL** |
| P4 | Technische Umsetzung | 175 W. | §4 (133 W.) | **FINAL** |
| P5 | Aktueller Stand/Neuerungen | 100 W. | §5 (81 W.) | **FINAL** |
| P6 | Link zum bestehenden Projekt | optional | §6 | **FINAL** |
| P7 | Innovation/Abgrenzung | 100 W. | §7 (92 W.) | **FINAL** |
| P8 | Zielgruppe/Zugang | 100 W. | §8 (90 W.) | **FINAL** |
| P9 | Meilensteine | 100 W. | §9 (68 W.) | **FINAL** |

### C. Team und Erfahrung

| # | Frage | Limit | Vorlage | Status |
|---|---|---:|---|---|
| T1 | Team? | 30 W. | §10: Nein (7 W.) | **FINAL** |
| T2 | Teammitglieder | dasselbe Feld | nicht ausgefüllt (Solo) | **N/A** |
| E1 | Bisherige Softwareprojekte | 100 W. | §11 (16 W. + Platzhalter) | **OWNER** |
| E2 | GmbH/Verein/Institut? | Ja/Nein | §12 Q4 | **OWNER** |
| E3 | Falls ja: Abgrenzung | 60 W. | §12 Q5 (21 W.) | **OWNER/BEDINGT** |
| E4 | Arbeitsstunden | Zahl ≤ 950 | 950 | **FINAL (950)** |
| E5 | Erfahrung/Motivation | 100 W. | §14 (77 W. + Platzhalter) | **OWNER** |

### D. Second Stage

| # | Frage | Limit | Vorlage | Status |
|---|---|---:|---|---|
| S1 | Second Stage beantragen? | Ja/Nein | Ja | **OWNER-ENTSCHEIDUNG** |
| S2 | Schwerpunkt | 175 W. | §16 (99 W.) | **FINAL (bei Ja)** |
| S3 | Meilensteine | 100 W. | §17 (29 W.) | **FINAL (bei Ja)** |

### E. Bestätigungen

| # | Bestätigung | Status |
|---|---|---|
| Q19a | 18+ und Hauptwohnsitz Deutschland | **OWNER** |
| Q19b | FOSS-Lizenz-Zusage | **OWNER** |

## 4. Noch fehlende persönliche Angaben (gesammelt)

1. **Accountname** für die Plattform.
2. **Vorname/Name** der Hauptansprechperson.
3. **E-Mail-Adresse** (regelmäßig geprüft).
4. **Wohnsitzland/-ort** (Deutschland).
5. **Persönlicher GitHub-/Bitbucket-Link**.
6. **Bisherige Softwareprojekte** (max. 3; Name, Link, Rolle/Umfang) für §11.
7. **Motivation/persönlicher Bezug** für §14.
8. **Q4** (GmbH/Verein/Institut/Anstellung): Ja/Nein; falls Ja, Q5-Abgrenzung.
9. **Second Stage:** Ja/Nein.
10. **Q19a/Q19b:** Checkboxen (Handbuch; nicht im Fragen-PDF).
11. **Optional:** 950 vs. 850 Stunden; Lizenz; Projektfassung F3.

**Nicht in das Repository:** Klarname, Anschrift, E-Mail, Steuernummer, Kontoauszug, De-minimis-Daten. Diese Angaben gehören ausschließlich in das Portal/den geschützten Owner-Bereich.

## 5. Materielles Q2-Risiko

| Aspekt | Befund | Konsequenz |
|---|---|---|
| Materielle Voraussetzung | BMFTR-RL Nr. 3 und FAQ/Bewerbungsseite: selbstständige Programmierer*innen bzw. Freiberuflichkeit oder Freistellung. JG03-Handbuch: nicht in den zwingenden Förderbedingungen; „als Privatperson“. | **Formale Zulassungsvoraussetzung derzeit nicht erfüllt**; Ablehnung möglich |
| Nachweiszeitpunkt | Online-Fragen: kein Steuernummerfeld. JG03-Checkliste: keine Solo-Steuernummer. JG02-Wiki: zum formalen Antrag. | offen |
| Formaler Antrag | März 2027 vs. „bis Ende Februar“ | Terminwiderspruch |
| Tätigkeitsbeginn | geplant 01.06.2027; Registrierung ≠ Aufnahme | nicht sicher |

**Regel:** Keine falsche Statusangabe. Falls das Live-Portal nach Selbstständigkeit fragt, wahrheitsgemäß „nicht selbstständig“ angeben. Die Bewerbung kann vorbereitet werden; die materielle Förderfähigkeit bleibt ein offenes Risiko.

## 6. Reihenfolge für den Owner (nach Login)

1. Jahrgang 03 Innovation öffnen; Live-Fragen mit dieser Tabelle vergleichen.
2. Abweichungen bei Wortlaut, Zeichenlimits, Pflichtfeldern hier notieren.
3. A1–A5 ausfüllen; P1–P9 aus `application-final-de.md` übertragen.
4. T1/E1–E5 ausfüllen; Q4/Q5 getrennt beantworten.
5. S1–S3 ausfüllen.
6. Q19a/Q19b bestätigen.
7. Entwurf speichern (falls das Portal dies unterstützt) und Vollständigkeit prüfen.
8. **Nicht absenden** ohne ausdrückliche Owner-Freigabe.

## 7. Gate

**Aktuell:** `READY_WITH_EXPLICIT_BLOCKERS`.

**Für `READY_FOR_PORTAL_OWNER_APPROVAL` fehlen:**

- authentifizierter Live-Abgleich der Felder, Zeichenlimits und Pflichtfelder;
- vollständige persönliche Angaben (A2–A5 inkl. Wohnsitz, E1, E5, Q4/Q5, Q19);
- Entscheidung zu Second Stage, Stunden und ggf. Lizenz;
- hinreichende Klärung der materiellen Q2-Voraussetzung oder bewusste Owner-Entscheidung, das Risiko zu tragen;
- Nutzung der Bewerbungssprechstunde am 16.11.2026, 17:00 Uhr (empfohlen).

**Tests/Links:** 109/109 Tests, 0 gebrochene relative Links (Stand vor diesem Dokument; nach Dokumentänderung erneut geprüft).

**Keine Einreichung, keine Kontoerstellung, keine E-Mail, keine Anmeldung, kein Merge.**
