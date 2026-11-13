# Review B — Förderrecht, Evidenz und strategischer Vergleich (Runde 3)

**Reviewer:** unabhängiger Agent-Prozess, frischer Kontext, read-only · **Datum:** 13.11.2026
**Geprüfter Candidate:** `fe3bd6ec891575fdae6f05d717de7697819302cd` (Branch `docs/funding-decision-2026-11-13`)
**Verdict:** **PASS** — Rechts-/Evidenz-/Vergleichskern quellenfest; alle MEDIUM-Befunde aus Runde 1 behoben. Verbleibend nur LOW-Präzisierungen (nicht blockierend).

> Der Reviewer hat HEAD/Branch/Working Tree geprüft (clean), den Diff `562fff7..fe3bd6e` gelesen, die Primärquellen erneut selbst abgerufen, die vier Wettbewerber-Belege aufgelöst, die Testsuite selbst ausgeführt (109/109 OK) und einen Linkcheck durchgeführt. Private RepairProbe-Inhalte und der Portal-Draft wurden nicht eingesehen.

## 1. Primärquellen-Prüfung (Auszug)

| Behauptung | Quelle (live, 13.11.2026) | Status |
|---|---|---|
| RL Nr. 4: 6/10 Monate, Eigenmittel per Bankunterlagen | BMFTR-RL 07.11.2024 | **BESTÄTIGT (wortgleich)** |
| RL Nr. 5: PK+GK; 50.000/100.000 €; zweite Phase 33.337/66.674 €; 95 % | ebd. | **BESTÄTIGT (wortgleich)** |
| Nr. 5 durch Ä1 (01.12.2025) und Ä2 (25.06.2026) unverändert | beide Änderungsbekanntmachungen | **BESTÄTIGT** |
| Ä2: Nr. 2/3/7.2.1/8; Nachwuchs-Satz; 30.11.2026; bis 30.06.2031 | Ä2-Volltext | **BESTÄTIGT** |
| De-minimis 300.000 €/3 Jahre; Aufbewahrung 3 Jahre | RL Anlage Nr. 1 | **BESTÄTIGT** |
| Rollierender Dreijahreszeitraum | EUR-Lex direkt nicht erreichbar; Erwägungsgrund 11 (PDF-Snippet) + Anlage | **BESTÄTIGT (mittelbar)**; im Dokument als solches ausgewiesen |
| FAQ: 47.500/79.167; 95.000/158.000; 5 % GK; 95 %; 31.667/633 h; 50-€-Cap | prototypefund.de/faq (28 Blöcke) | **BESTÄTIGT (wortgleich)** |
| Handbuch F14: 950/1.900 h, „insgesamt"; <250 h; Second-Stage-Stunden; keine Code-Meilensteine | PTF_Handbuch_2026.pdf | **BESTÄTIGT** |
| Detailseite: Daten, Beträge, „sechs- oder zehnmonatig", 30.11.2026 15:00 CET | bewerbung/details | **BESTÄTIGT** |
| Innovationsseite: nur 6 Monate | prototypefund.de/innovation | **BESTÄTIGT** |
| RepairVision: „provisional labels", Hazard-Screen, 199 Tests | dev.to 08.10.2026 + GitHub | **BESTÄTIGT** |
| FixBot: Sprach-/Bilddiagnose, 125k Anleitungen | ifixit.com/News/114700 | **BESTÄTIGT** |
| NORA: Repair-Café-KI, Nieder-Olm | repaircafe-groebenzell.de, 23.03.2026 | **BESTÄTIGT** |
| AugRep/GYVA: DBU 41431/01, Pilot Freiburg 17.10.2026, Uni Freiburg | dbu.de/projektdatenbank/41431-01/ | **BESTÄTIGT** |
| RP: 24 (llms.txt) vs. 44 (technical-baseline.html); n=1; 850 h; nicht eingereicht | öffentliche Seiten | **BESTÄTIGT** |

## 2. Q3 / Second Stage / De-minimis / 10 Monate

- **Q3:** korrekt **UNRESOLVED** und nicht einreichungsblockierend. 950 h × 50 = 47.500 PK; GK 2.375; G 49.875; F 47.381,25; EA 2.493,75; Δ 118,75 = 5 % × 2.375. Keine Scheinlösung; Anfrage nicht versendet.
- **Second Stage:** 633 h = 31.570,87; 634 h = 31.620,75; Cap 31.670,15; 635 h Cap-Verstoß. Quellen getrennt: Stundenregel Handbuch-Intro, 50-€-Cap FAQ 01, keine Code-Meilensteine Handbuch Q16.
- **De-minimis:** 300.000 € / rollierende 3 Jahre; Second Stage zählt mit; 3-Jahres-Aufbewahrung; Kumulierungsverbot. Register/Erklärungspflicht korrekt differenziert (R11 nach LOW-Fix).
- **10 Monate:** 83.337 € / 79.170,15 €; FAQ 79.167 = 47.500 + 31.667; Team 158.000 ≠ 158.333 ≠ 158.340,30 dokumentiert. Nur Innovationsseite schweigt zur 10-Monats-Option.

## 3. Vergleich Feldexa 2.0/FormBridge vs. RepairProbe

**Fairness und Evidenz:**

- F1/F2/F3/RP sind in §0 sauber definiert; die Empfehlung ist ausdrücklich bedingt und **keine Owner-Entscheidung**.
- Demonstriert vs. geplant ist getrennt (§3); „240 Tests ≠ Produktreife" explizit; 184 ohne App / 240 gesamt korrekt.
- Eligibility ≠ Technik ≠ Wirkung als Dreispaltentabelle (§5).
- RepairProbe fair: 24–44 offengelegt, n=1 als Widerspruch zur Nutzenhypothese, privates Repo nicht zitiert, Second Stage nicht „proportional", sondern durch 33.337-€-Cap begrenzt.
- Wettbewerber: vier tragende Projekte mit URL/Datum belegt; YProbe/ARBoard/PCBSpot und ORDS/ORA ausdrücklich nur Kontext, nicht Beweis. Die RP-K1-Abwertung ruht auf RepairVision/FixBot/NORA/AugRep.
- Bewertungsarithmetik: FB 6,725 / RP 5,45; Sensitivitäten S1–S4 stimmen; selbst mit RP-K1 = 4,5 bliebe RP bei 5,575 < 6,725.

## 4. Dokumentationskonsistenz

- Tests selbst ausgeführt: **109/109 OK**; Klassenverteilung 15+13+17+11+11+14+8+8+12 = 109; keine „102"-Reste.
- SHA-256 in `RUNBOOK.md` stimmen mit den Dateien überein.
- Cash-Peak 25.353,13 / 1.662,50 / 23.690,63; Rate 2 = 23.690,62 mit 1-Cent-Rest dokumentiert.
- F5–F7, F10, F12, F13 behoben (R1→Ä2; Mentor nur Up-and-Coming; M1→RL 2024; Quellenhierarchie nicht-normativ; W8/W9).
- Relative Links: 0 gebrochen.
- Statuslabels: `final-validation-report.md` DRAFT/PENDING; Reviews jetzt PASS; Runde 2 historisch markiert.

## 5. Findings

**Keine CRITICAL/HIGH/MEDIUM-Findings.** LOW/NONBLOCKING aus dem Review, im finalen Dokumentations-Commit bereinigt:

| # | Severity | Fundstelle | Befund | Behandlung |
|---|---|---|---|---|
| F1 | LOW | `comparison-report.md` | Zeile 50 führte YProbe/ORDS in einer VERIFIED-Zeile, obwohl §4a sie als ungeprüft markiert | Auf vier belegte Projekte reduziert; Rest nur Kontext |
| F2 | LOW | `validation-report.md` | „79.167 gerundet" statt additive Herleitung | Auf 47.500 + 31.667 korrigiert |
| F3 | LOW | `validation-report.md` | `TestTenMonth` mit 9 statt 12 Tests | Auf 12 korrigiert |
| F4 | LOW | `source-register` R11 | „Pflicht der Bewilligungsstelle, nicht des Antragstellers" zu absolut | Registerführung vs. Erklärungspflicht differenziert |

## 6. Residual risks / nonblocking

1. EUR-Lex direkt nicht erreichbar; Art. 3 Abs. 2 über RL-Anlage, Erwägungsgrund 11 über Snippet belegt; Art. 6 (Register) inhaltlich, nicht nummerisch unmittelbar geprüft.
2. Q3/Q3b bleiben UNRESOLVED; nur Maximalausschöpfung (118,75 € / 96,13 €).
3. Q1/Q2-Anfrage ist Entwurf; Q1 offenbart gegenüber PTF einen zweiten Portal-Entwurf — Owner-Abwägung vor Versand.
4. M1–M9 offen; Q2 ist die einzige potenziell harte Hürde.
5. Team-Pfad W9 (Unternehmen vs. GbR) dokumentiert, nicht aufgelöst; für Solo-Baseline irrelevant.
6. Feldexa-Kennzahlen (240 Tests, 23 Dateien) wurden nicht nachgefahren (Flutter/Fremd-Repo), aber intern konsistent.
7. Nits: „Evaluationspflicht neu" könnte als Ä2-Neuheit gelesen werden (sie bestand 2024); „Amtssprache Deutsch" unterschlägt englische Bewerbungen (FAQ Bewerbung 08). Beide im finalen Commit präzisiert.

## 7. Required corrections before final PASS

**Keine blockierenden Korrekturen.** Der Candidate ist PASS-fähig. Die vier LOW-Punkte wurden im finalen Dokumentations-Commit bereinigt; sie ändern keine Rechtsaussage, Zahl oder Rangfolge.

## 8. Commands and sources

```bash
git rev-parse HEAD   # fe3bd6ec891575fdae6f05d717de7697819302cd
git status --porcelain=v1   # leer
python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v
# Ran 109 tests ... OK
sha256sum financial_model.py test_financial_model.py scenario-report.md  # == RUNBOOK
```

**Primärquellen:** BMFTR-RL 2024 + Ä1/Ä2; PTF-FAQ, Handbuch, Details, Innovation; VO (EU) 2023/2831; RepairVision/FixBot/NORA/AugRep-GYVA; RepairProbe `llms.txt`/`technical-baseline.html`/Org-README. Vollständige URLs im [Quellenregister](source-register-2026-11-13.md) und in [comparison-report.md](comparison-report.md) §4a.
