# Owner-Checkliste — FormBridge-Bewerbung

**Stand:** 14.11.2026 · **Zweck:** Nur die Punkte, die der Owner persönlich entscheiden, bestätigen oder ergänzen muss. **Keine persönlichen Daten in diesem Repository.**
**Legende:** `BLOCKER` = Einreichung/Förderung ohne Klärung nicht möglich · `PLANUNG` = beeinflusst Qualität/Umfang · `FORMAL` = bei Bewilligung erforderlich

## A. Harte persönliche Voraussetzungen

| # | Frage | Was der Owner tun muss | Status |
|---|---|---|---|
| M1 | Mindestalter 18? | Eigene Bestätigung | **BESTÄTIGT (25.11.2026)** |
| M2 | Wohnsitz in Deutschland + Steuern in DE? | Eigene Bestätigung; ggf. Nachweis | **BESTÄTIGT (25.11.2026)** |
| M3a | Selbstständig oder freiberuflich? | Registrierung **vor Förderbeginn (01.06.2027) und vor dem formalen BMFTR-Antrag** einplanen; BMFTR-RL/FAQ verlangen den Status, das JG03-Handbuch nennt ihn nicht unter den zwingenden Förderbedingungen. | **PLAN ERFÜLLT / STICHTAG OFFEN** |
| M3b | Angestellt + (anteilige) Arbeitgeber-Freistellung für 01.06.–30.11.2027? | Schriftliche Freistellung klären | **BLOCKER**, falls nicht freigestellt |
| M3c | Aufnahme der Tätigkeit 2027 geplant? | Registrierung vor dem PTF-bestätigten formalen Antragstermin einplanen (nicht erst 01.06.2027); Stichtag bestätigen lassen; Analyse: [q2-employment-status.md](../decision/q2-employment-status.md) | **PLAN ERFÜLLT / STICHTAG OFFEN** |
| M4 | Notwendige Programmierkenntnisse vorhanden (KI nur Werkzeug)? | Eigene Bestätigung; ggf. Code-/Projektnachweise | **BLOCKER** |
| M5 | Einschlägige Vorarbeiten + umfassende Kenntnisse nachweisbar? | Bewerbungstext §11/§14 ergänzen; Nachweise | **BLOCKER**, falls kein Nachweis |
| M6 | De-minimis: < 300.000 € Beihilfen in den letzten **rollierenden** 3 Jahren? | De-minimis-Erklärung im formalen Antrag | **BESTÄTIGT: 0 € (25.11.2026)** |
| M7 | Kapazität für 950 h / 6 Monate (~158 h/Monat im Durchschnitt (Plan 150–165 h/Monat))? | Kalender prüfen; sonst 850-h-Variante wählen | **BESTÄTIGT/GEPLANT (25.11.2026)** |
| M8 | Kontoauszug-Saldo ≥ 2.493,75 € (2.500 € empfohlen) zur Bewilligung? | Kontoauszug zum Bewilligungszeitpunkt | **BESTÄTIGT/GEPLANT (25.11.2026)** |
| M9 | Second Stage beantragen? | Ja/Nein entscheiden; Konzept liegt vor | **ENTschieden: Ja (25.11.2026)** |

## B. Persönliche Angaben für das Portal

| Feld | Platzhalter / Hinweis |
|---|---|
| Projekttitel | `FormBridge` |
| Accountname | `[OWNER_ANGABE_ERFORDERLICH]` |
| Vorname / Name | `[OWNER_ANGABE_ERFORDERLICH]` |
| E-Mail | `[OWNER_ANGABE_ERFORDERLICH]` |
| Wohnsitzland/-ort | `[OWNER_ANGABE_ERFORDERLICH]` |
| Persönlicher GitHub-/Bitbucket-Link | `[OWNER_ANGABE_ERFORDERLICH]` |
| Projektlink (Q6) | `https://github.com/xxammaxx/FormBridge` (öffentlich) |
| Bisherige Projekte (max. 3) | **ERLEDIGT 25.11.2026** — §11 final (77 W.): Feldexa 2.0, FormBridge, Umliva-Vorarbeit mit Links |
| Motivation/persönlicher Bezug | **ERLEDIGT 25.11.2026** — §14 final (83 W.): technischer Autodidakt, Praxis, Prüfanspruch, Formularerfahrung |
| Q4: Gesellschafter*in/GmbH/Verein/Institut? | **Nein** (Owner-Bestätigung 25.11.2026) — FINAL |
| Q5: Falls ja, Trennung erläutern | **entfällt (Q4 = Nein)**; Vorlagetext 11 W. — FINAL |
| Team | Nein (Solo) — bestätigen |
| Arbeitsstunden | **950 entschieden (25.11.2026)** |
| Q19a: 18+ / Hauptwohnsitz DE | **zugesagt (25.11.2026)** — Portal-Checkbox noch zu setzen |
| Q19b: FOSS-Lizenz-Zusage | **zugesagt (25.11.2026)** — Portal-Checkbox noch zu setzen |

## C. Owner-Entscheidungen

| # | Entscheidung | Optionen | Empfehlung | Status |
|---|---|---|---|---|
| O1 | **Lizenz** | Apache-2.0 / MPL-2.0 / andere OSI-Lizenz | **Apache-2.0** entschieden (25.11.2026), `LICENSE` committet | **ERLEDIGT** |
| O2 | **Stunden** | 950 (Default) / 850 (bewusste Änderung) | **950 entschieden (25.11.2026)** | **ERLEDIGT** |
| O3 | **Second Stage** | Ja / Nein | **Ja entschieden (25.11.2026)**; §16/§17 sind final | **ERLEDIGT** |
| O4 | **Feldexa-Fassung** | F1 App / F2 ProofLayer / F3 FormBridge / RepairProbe | Bedingte Empfehlung F3; Owner entscheidet | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
| O5 | **Q1/Q2/Q3-Anfragen** | senden / nicht senden | Q2 ist kritisch; Q3 nur für Maximalausschöpfung | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |

## D. Formale/externe Klärungen

| # | Punkt | Warum | Status |
|---|---|---|---|
| F1 | Q2: Selbstständigkeit ab Förderbeginn | Einzige potenziell harte formale Hürde | `[PTF_BESTÄTIGUNG_ERFORDERLICH]` |
| F2 | Q1: zwei parallele Förderungen | Nur relevant, falls beide Projekte aktiv | `[PTF_BESTÄTIGUNG_ERFORDERLICH]` |
| F3 | Q3/Q3b: 47.500 vs. 47.381,25; 31.667 vs. 31.570,87 | Konservative Planung möglich; Maximalausschöpfung offen | `[PTF_BESTÄTIGUNG_ERFORDERLICH]` |
| F4 | Held-out-Wohngeld-PDF (anderes Bundesland) + Rechte | Generalisierbarkeit und `copy:no`-Rechtslage | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
| F5 | Rechte an Fürther PDF/FIM-XSD für Tests | Redistribution/Testnutzung | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
| F6 | 10-Monats-Option | Nur falls 10 Monate gewollt | `[PTF_BESTÄTIGUNG_ERFORDERLICH]` |
| F7 | Portal-Zeichenlimits/Pflichtfelder | Portal login-geschützt; keine authentifizierte Sitzung | `[PORTAL_UNVERIFIED]` |
| F8 | Materielle Selbstständigkeitsvoraussetzung | FAQ/Bewerbungsseite: ja; JG03-Handbuch: nicht in zwingenden Förderbedingungen; Online-Fragen: kein Feld | `[PTF_BESTÄTIGUNG_ERFORDERLICH]` |

## E. Vor der Einreichung abzuhaken

- [ ] M1–M6 positiv geklärt; M8 planbar. **M3a/M3c: materielles Q2-Risiko dokumentiert und entschieden.**
- [x] O1 Lizenz entschieden: Apache-2.0 (25.11.2026), `LICENSE` im Wurzelverzeichnis; FOSS-Zusage in Q19b bleibt zusätzlich erforderlich.
- [ ] O2 Stunden entschieden; Budget/Plan konsistent.
- [ ] O3 Second Stage entschieden; §16/§17 entfernt oder final.
- [ ] O4 Projektfassung final bestätigt (F3 empfohlen).
- [ ] O5 Q2-Anfrage gestellt oder bewusst zurückgestellt. **Schnellster Kanal: Bewerbungssprechstunde 16.11.2026, 17:00 Uhr.**
- [ ] Q4 (Ja/Nein) und Q5 (max. 60 Wörter) getrennt beantwortet.
- [ ] Q19a (18+/Hauptwohnsitz DE) und Q19b (FOSS-Zusage) bestätigt.
- [ ] Persönliche Felder aus B ergänzt; keine Platzhalter mehr im Portaltext.
- [ ] Portal-Live-Fragen/Wortlimits geprüft; Abweichungen in `portal-field-mapping.md` nachgezogen. Der Live-Login ist eine einmalige Owner-Aktion; siehe [portal-preflight-2026-11-14.md](portal-preflight-2026-11-14.md).
- [ ] `application-final-de.md` von Platzhaltern befreit (außer bewusst markierten).
- [ ] Keine sensiblen Daten im öffentlichen Repo.
- [ ] RepairProbe-Portal-Draft unverändert.
- [ ] Bewerbung nicht vor Owner-Freigabe abgesendet.

## F. Was der Owner nicht tun muss

- Keine Offenlegung von Vermögenswerten über den Eigenanteils-Saldo hinaus.
- Keine Offenlegung privater Dokumente, die nicht für die Förderung erforderlich sind.
- Keine Festlegung auf eine Lizenz, bevor er/sie es will — aber die FOSS-Zusage im Antrag muss stehen.
- Keine Bestätigung von Zahlen, die nur der Agent geprüft hat; die Quellen liegen offen.

## Ergänzung 19.11.2026: RF1-LoRA

- [ ] Eigene Entwicklungs-/Programmierkompetenz und Verantwortlichkeit belegen; KI nur als Hilfsmittel (PTF-FAQ).
- [ ] Bei beabsichtigter GPU-/API-Miete vor Nutzung die Behandlung in bestehender Gemeinkostenpauschale schriftlich klären und separates Ausgabenlimit genehmigen; keine Antragserhöhung. Andernfalls lokal/zulässig separat finanzieren. [RF1-Versuchsgrenze](lora-research-extension-2026-11-19.md).
- [ ] Vorarbeiten/Überschneidungen vor Förderbeginn nachführen; keine FormBridge-Implementierung vor Freigabe.
