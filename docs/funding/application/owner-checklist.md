# Owner-Checkliste — FormBridge-Bewerbung

**Stand:** 13.11.2026 · **Zweck:** Nur die Punkte, die der Owner persönlich entscheiden, bestätigen oder ergänzen muss. **Keine persönlichen Daten in diesem Repository.**
**Legende:** `BLOCKER` = Einreichung/Förderung ohne Klärung nicht möglich · `PLANUNG` = beeinflusst Qualität/Umfang · `FORMAL` = bei Bewilligung erforderlich

## A. Harte persönliche Voraussetzungen

| # | Frage | Was der Owner tun muss | Status |
|---|---|---|---|
| M1 | Mindestalter 18? | Eigene Bestätigung | **BLOCKER** |
| M2 | Wohnsitz in Deutschland + Steuern in DE? | Eigene Bestätigung; ggf. Nachweis | **BLOCKER** |
| M3a | Selbstständig oder freiberuflich? | Status bestätigen | **BLOCKER**, falls weder a/b/c |
| M3b | Angestellt + (anteilige) Arbeitgeber-Freistellung für 01.06.–30.11.2027? | Schriftliche Freistellung klären | **BLOCKER**, falls nicht freigestellt |
| M3c | Selbstständigkeit erst ab Förderbeginn geplant? | PTF-Anfrage Q2; **sichere Planung: Registrierung vor formalem Antrag (Ende Februar 2027)** oder Freistellung; „erst 01.06.2027" ist nicht sicher; Analyse: [q2-employment-status.md](../decision/q2-employment-status.md) | **POTENZIELLER BLOCKER** |
| M4 | Notwendige Programmierkenntnisse vorhanden (KI nur Werkzeug)? | Eigene Bestätigung; ggf. Code-/Projektnachweise | **BLOCKER** |
| M5 | Einschlägige Vorarbeiten + umfassende Kenntnisse nachweisbar? | Bewerbungstext §11/§14 ergänzen; Nachweise | **BLOCKER**, falls kein Nachweis |
| M6 | De-minimis: < 300.000 € Beihilfen in den letzten **rollierenden** 3 Jahren? | Alle Beihilfen auflisten; De-minimis-Erklärung | **BLOCKER**, falls überschritten |
| M7 | Kapazität für 950 h / 6 Monate (~158 h/Monat im Durchschnitt (Plan 150–165 h/Monat))? | Kalender prüfen; sonst 850-h-Variante wählen | **PLANUNG** |
| M8 | Kontoauszug-Saldo ≥ 2.493,75 € (2.500 € empfohlen) zur Bewilligung? | Liquidität prüfen | **FORMAL** |
| M9 | Second Stage beantragen? | Ja/Nein entscheiden; Konzept liegt vor | **PLANUNG** |

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
| Bisherige Projekte (max. 3) | `[OWNER_ANGABE_ERFORDERLICH]` — Name, Link, Rolle/Umfang |
| Motivation/persönlicher Bezug | `[OWNER_ANGABE_ERFORDERLICH]` — max. 100 Wörter |
| Q4: Gesellschafter*in/GmbH/Verein/Institut? | `[OWNER_BESTÄTIGUNG_ERFORDERLICH]` — Ja/Nein |
| Q5: Falls ja, Trennung erläutern | `[OWNER_BESTÄTIGUNG_ERFORDERLICH]` — max. 60 Wörter |
| Team | Nein (Solo) — bestätigen |
| Arbeitsstunden | 950 oder 850 — entscheiden |
| Q19a: 18+ / Hauptwohnsitz DE | `[OWNER_BESTÄTIGUNG_ERFORDERLICH]` — Checkbox |
| Q19b: FOSS-Lizenz-Zusage | `[OWNER_BESTÄTIGUNG_ERFORDERLICH]` — Checkbox |

## C. Owner-Entscheidungen

| # | Entscheidung | Optionen | Empfehlung | Status |
|---|---|---|---|---|
| O1 | **Lizenz** | Apache-2.0 / MPL-2.0 / andere OSI-Lizenz | **Apache-2.0** empfohlen; **keine Festlegung ohne Owner-Freigabe** | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
| O2 | **Stunden** | 950 (Default) / 850 (bewusste Änderung) | 950 nur bei gesicherter Vollzeitkapazität; sonst 850 | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
| O3 | **Second Stage** | Ja / Nein | Ja, wenn Integration/Community gewollt; sonst Nein und §16/§17 entfernen | `[OWNER_ENTSCHEIDUNG_ERFORDERLICH]` |
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
| F7 | Portal-Zeichenlimits/Pflichtfelder | Portal login-geschützt | `[PORTAL_UNVERIFIED]` |

## E. Vor der Einreichung abzuhaken

- [ ] M1–M6 positiv geklärt; M8 planbar.
- [ ] O1 Lizenz entschieden (oder bewusst offen bis nach Auswahl; FOSS-Zusage bleibt).
- [ ] O2 Stunden entschieden; Budget/Plan konsistent.
- [ ] O3 Second Stage entschieden; §16/§17 entfernt oder final.
- [ ] O4 Projektfassung final bestätigt (F3 empfohlen).
- [ ] O5 Q2-Anfrage gestellt oder bewusst zurückgestellt.
- [ ] Q4 (Ja/Nein) und Q5 (max. 60 Wörter) getrennt beantwortet.
- [ ] Q19a (18+/Hauptwohnsitz DE) und Q19b (FOSS-Zusage) bestätigt.
- [ ] Persönliche Felder aus B ergänzt; keine Platzhalter mehr im Portaltext.
- [ ] Portal-Live-Fragen/Wortlimits geprüft; Abweichungen in `portal-field-mapping.md` nachgezogen.
- [ ] `application-final-de.md` von Platzhaltern befreit (außer bewusst markierten).
- [ ] Keine sensiblen Daten im öffentlichen Repo.
- [ ] RepairProbe-Portal-Draft unverändert.
- [ ] Bewerbung nicht vor Owner-Freigabe abgesendet.

## F. Was der Owner nicht tun muss

- Keine Offenlegung von Vermögenswerten über den Eigenanteils-Saldo hinaus.
- Keine Offenlegung privater Dokumente, die nicht für die Förderung erforderlich sind.
- Keine Festlegung auf eine Lizenz, bevor er/sie es will — aber die FOSS-Zusage im Antrag muss stehen.
- Keine Bestätigung von Zahlen, die nur der Agent geprüft hat; die Quellen liegen offen.
