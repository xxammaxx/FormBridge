# Review A — Finanzielle und numerische Korrektheit (Runde 3)

**Reviewer:** unabhängiger Agent-Prozess, frischer Kontext, read-only · **Datum:** 13.11.2026
**Geprüfter Candidate:** `fe3bd6ec891575fdae6f05d717de7697819302cd` (Branch `docs/funding-decision-2026-11-13`)
**Verdict:** **PASS** — Finanzkern korrekt, reproduzierbar; keine materiellen Findings. Verbleibende Punkte sind LOW/NONBLOCKING.

> Der Reviewer hat HEAD, Branch und Working Tree geprüft (`git status --porcelain` leer, `git diff --quiet HEAD` exit 0) und alle Werte unabhängig mit Python `decimal` (Precision 50, kein `float`) nachgerechnet. Er hat die Autorentests nicht als Beweis übernommen.

## 1. Unabhängige Nachrechnung (Auszug)

| Größe | Dokument | Eigene Rechnung | Status |
|---|---:|---:|---|
| PK (950 × 50) | 47.500,00 | 47.500,00 | ✅ |
| GK (5 % PK) | 2.375,00 | 2.375,00 | ✅ |
| G = PK + GK | 49.875,00 | 49.875,00 | ✅ |
| F = floor(0,95 × G) | 47.381,25 | 47.381,25 | ✅ |
| EA = G − F | 2.493,75 | 2.493,75 | ✅ |
| Q3-Differenz zu 47.500 | 118,75 | 118,75 = 5 % × 2.375 | ✅ |
| A: 950 h ohne GK | 45.125,00 F | 45.125,00 | ✅ |
| D 700/800/850/950 h | 34.912,50 / 39.900,00 / 42.393,75 / 47.381,25 | identisch | ✅ |
| F 200 h | 9.975,00 F | 9.975,00 | ✅ |
| C exakter Satz | 50,1253132832… €/h → G 50.000,00 | identisch | ✅ |
| C 50,1253 | G 49.999,99; F 47.499,99 | identisch | ✅ |
| C 50,13 | G 50.004,67; Cap-Verstoß | identisch | ✅ |
| Second Stage 633/634/635 h | 31.570,87 / 31.620,75 / Cap-Verstoß | identisch | ✅ |
| Second-Stage-Cap 33.337 × 0,95 | 31.670,15 | 31.670,15 | ✅ |
| 10 Monate 950+634 h | G 83.160; F 79.002; EA 4.158 | identisch | ✅ |
| 10-Monats-Cap | 83.337 / 79.170,15 | identisch | ✅ |
| Cash-Raten | 7.896,87 / 23.690,62 / 15.793,76 | Summe 47.381,25 | ✅ |
| Kumulativer Peak 30.09. | 25.353,13 (extern 23.690,63; eigen 1.662,50) | 4 × 8.312,50 − 7.896,87 | ✅ |
| Erstes Monatsloch / EA-Floor | 415,63 / 415,62 | identisch | ✅ |
| De-minimis 260.000 | F 40.000; EA 9.875 | identisch | ✅ |
| Kombination regular+second | 79.002 | 47.381,25 + 31.620,75 | ✅ |

**K5-Kombinationsprüfung:** 600 h regulär + 634 h Second Stage → `compliant=False`, `K5_second_stage_hours_exceed_regular_phase`. 633 h + 633 h → `compliant=True`. 600 h + 635 h → `compliant=False`, Kind-Violations (`second:total_cost_cap_exceeded`) sichtbar. Alle drei Fälle korrekt.

## 2. Testlauf und Testqualität

**Befehl:**

```bash
cd /home/xxammaxx/Schreibtisch/feldexa_forderung/FormBridge
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s docs/funding/decision/validation -p 'test_*.py' -v
```

**Ergebnis:** `Ran 109 tests in 0.008s — OK` — **109/109 bestätigt**. Die 109 Test-IDs stimmen exakt mit `validation/test-output.txt` überein (sortierter Diff leer). Klassenverteilung 15+13+17+11+11+14+8+8+12 = 109 stimmt mit `RUNBOOK.md`.

**Qualität:** Die Kernwerte sind Literale, nicht aus der Implementierung abgeleitet. Die neuen K5-/Cash-Flow-Tests sind substanziell. `test_cost_cap_50000_01_rejected` nutzt jetzt den exakten Satz für G = 50.000,01; `test_second_stage_633_funding_rate` prüft das Literal 31.570,87; die Float-Ratio wurde durch Decimal ersetzt. Die Negativtests für F > 95 %/EA < 5 % sind Arithmetik-Nachweise; die Doku sagt das jetzt ausdrücklich. `scenario-report.md` ist mit dem Modell byte-identisch reproduzierbar.

## 3. Findings

**Keine CRITICAL/HIGH/MEDIUM-Findings.** LOW/NONBLOCKING:

| Severity | Fundstelle | Befund | Behandlung |
|---|---|---|---|
| LOW | `validation-report.md` R2-Korrekturabschnitt | „61/61 PASS" ohne Historisch-Banner | Historisch-Banner ergänzt; keine aktuelle Aussage |
| LOW | `final-validation-report.md` | Candidate-Platzhalter im DRAFT | Wird nach finalem Commit mit SHA gefüllt |
| LOW | `validation/RUNBOOK.md` | Satz zu „Pre-final-Hashes" stale | Auf Candidate-Hashes umformuliert |
| LOW | `validation-report.md` | „Reviews A/B stehen in …" bei PENDING-Platzhaltern | Nach Review durch die Reports ersetzt |
| LOW | `financial_model.py` | Rückgabetyp `list[str]`, tatsächlich `tuple` | Auf `tuple[str, ...]` korrigiert |
| LOW | `financial_model.py` | `four_month_ea` nutzte Half-up statt Floor | Auf `floor_money` korrigiert; Baseline unverändert |
| LOW | `validation-report.md` | Vorwärtsverweis „Review A3/B3" | Auf „Review A/B (Runde 3)" korrigiert |

## 4. Q3 / Second Stage / De-minimis / 10 Monate

- **Q3:** korrekt **UNRESOLVED** und nicht blockierend. 47.381,25 € sind aus RL Nr. 5 + FAQ Förderung 02 sauber hergeleitet; 118,75 = 5 % × 2.375. Keine Variante wird als offizielle Klärung ausgegeben; die Anfrage ist nicht versendet.
- **Second Stage:** 633 h = 31.570,87 €; 634 h = 31.620,75 €; 635 h = Cap-Verstoß. 31.650 € sind PK, nicht Förderung. 50-€/h-Cap und keine Code-Meilensteine korrekt.
- **De-minimis:** 300.000 € / rollierende 3 Jahre korrekt (RL Anlage; VO 2023/2831 Art. 3 Abs. 2, Erwägungsgrund 11). Kombination regular+second korrekt. Kein Datumsfenster im Modell; `prior_deminimis` ist manuell zu liefern — dokumentiert.
- **10 Monate:** 83.337 € / 79.170,15 € korrekt; FAQ 79.167 = 47.500 + 31.667. Beispiel 950+634 h korrekt. Portalverfügbarkeit bleibt offen.

## 5. Residual risks / nonblocking

- Q3/Q3b offen (118,75 € / 96,13 €); nur Maximalausschöpfung.
- 10-Monats-Portalverfügbarkeit (Innovationsseite vs. Detailseite).
- M1–M9 owner-abhängig.
- De-minimis-Historie manuell zu addieren.
- LOW-Doku-Punkte oben; keine Finanzzahl betroffen.

## 6. Required corrections before final PASS

**Keine blockierenden Korrekturen.** Alle sieben Pflichtkorrekturen aus Runde 1 sind umgesetzt:

1. K5 + Child-Violations im 10-Monats-Modell ✅
2. Gate-Tabelle nicht mehr „Reviews abgeschlossen" ✅
3. Stale 31.650/7.896,88/23.690,63/50,1256 markiert/aktualisiert ✅
4. Cash-Flow-Peak 25.353,13 / 1.662,50 / 23.690,63 ✅
5. 415,63 vs. 415,62 getrennt ✅
6. Scenario-Report/Hashes/Python 3.14.8 ✅
7. Testqualität (50.000,01, Literal, Decimal) ✅

## 7. Commands and environment

```bash
git rev-parse HEAD   # fe3bd6ec891575fdae6f05d717de7697819302cd
git status --porcelain=v1   # leer
python3 --version   # 3.14.8
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s docs/funding/decision/validation -p 'test_*.py' -v
# Ran 109 tests ... OK
sha256sum financial_model.py test_financial_model.py scenario-report.md
# dbf3fdec… / a60bcc4a… / 2a055390… (Snapshot `fe3bd6e`; finaler Modellhash `1b4e281e…`, RUNBOOK)
```

**Quellen:** BMFTR-Richtlinie „Software Sprint" (BAnz AT 15.11.2024 B4; Ä1 01.12.2025; Ä2 25.06.2026), PTF-FAQ, PTF-Handbuch, VO (EU) 2023/2831. Details im [Quellenregister](source-register-2026-11-13.md).
