# Finaler Validierungsbericht — Runde 3 (13.11.2026)

**Status:** **FINAL (Dokumentation)** · **Geprüfter Candidate:** `fe3bd6ec891575fdae6f05d717de7697819302cd` · **Branch:** `docs/funding-decision-2026-11-13` · **Reviewer:** A (Finanzen) **PASS**, B (Förderrecht/Evidenz/Vergleich) **PASS**

> **Gate:** **VALIDATED_WITH_OPEN_QUESTIONS** — Finanzkern, Quellenbasis und Vergleich sind unabhängig geprüft; Q3/Q3b bleiben als **nicht blockierende, quantifizierte** Unsicherheiten offen. Das ist **keine** Förderzusage, **keine** Bestätigung der persönlichen Förderfähigkeit und **keine** Entscheidung für den Owner.

## 1. Finanzielle Baseline

| Größe | Wert |
|---|---:|
| Personalkosten (950 h × 50 €) | 47.500,00 € |
| Gemeinkosten (5 % PK, Floor) | 2.375,00 € |
| Gesamtkosten G | 49.875,00 € |
| Förderung F (95 %, Floor) | 47.381,25 € |
| Eigenanteil EA (5 %) | 2.493,75 € |
| Kommunizierte Maximalförderung | 47.500,00 € |
| **Q3-Differenz** | **118,75 €** |
| Kontoauszug-Saldo (Empfehlung) | 2.500,00 € |
| Kumulativer Cash-Peak (30.09.2027) | 25.353,13 € (extern 23.690,63 €; eigen 1.662,50 €) |

**Planungsregel:** 950 h beantragen; Förderung mit **47.381,25 €** planen, nicht mit 47.500 €. Falls das Portal die FAQ-Logik abbildet, wird automatisch bis 47.500 € ausgeschöpft. Die absolute Untergrenze ohne anerkannte GK ist 45.125,00 €.

## 2. Testevidenz

- **Befehl:** `python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v`
- **Ergebnis:** **109/109 PASS** (`Ran 109 tests … OK`)
- **Archiv:** [`validation/test-output.txt`](validation/test-output.txt), [`validation/scenario-report.md`](validation/scenario-report.md), [`validation/RUNBOOK.md`](validation/RUNBOOK.md), [`validation/financial_model.py`](validation/financial_model.py), [`validation/test_financial_model.py`](validation/test_financial_model.py)
- **Frühere 56/57-Behauptung:** nicht reproduzierbar (Skript nicht archiviert), ersetzt durch 109/109.
- **Abdeckung:** Baseline, A–I, Caps, Rundung, Second Stage, Cash-Flow, De-minimis, 10-Monats-Option, negative Altmodelle, K5-Kombination.

## 3. Reviewer A — Finanzielle und numerische Korrektheit

**Verdict: PASS** · [Vollständiger Bericht](review-A-financial-2026-11-13.md)

- Alle Kernwerte unabhängig per `decimal` nachgerechnet; cent-exakt.
- K5 im 10-Monats-Modell jetzt erzwungen (600+634 fail, 633+633 pass, Kind-Violations sichtbar).
- Cash-Peak korrekt: 25.353,13 € total / 23.690,63 € extern / 1.662,50 € eigen; 24.937,50 € ist nur die Quartalsausgabe.
- 109/109 Tests unabhängig bestätigt; Testqualität nicht abgeschwächt.
- Keine blockierenden Findings; nur LOW-Dokumentationspunkte, im finalen Commit bereinigt.
- **Fokussierter Re-Check:** **PASS** für `b85ef7e2ae9ced55ef3b393399688fb8b03b3ce1` (finaler SHA; nur LOW-Dokumentations-/Annotationskorrekturen gegenüber `fe3bd6e`).

## 4. Reviewer B — Förderrecht, Evidenz und Vergleich

**Verdict: PASS** · [Vollständiger Bericht](review-B-funding-2026-11-13.md)

- RL Nr. 4/5, Ä1/Ä2, De-minimis-Anlage, FAQ, Handbuch und Detailseite unabhängig geprüft; Nr. 5 unverändert.
- Q3 korrekt UNRESOLVED und nicht einreichungsblockierend; Second Stage 31.570,87/31.620,75; 10 Monate 83.337/79.170,15.
- Wettbewerber RepairVision, FixBot, NORA, AugRep/GYVA mit URL/Datum belegt; RP-K1-Abwertung darauf gestützt, nicht auf ungeprüfte Namenslisten.
- Vergleich fair: F1/F2/F3/RP getrennt, demonstriert vs. geplant, 24–44-Test-Widerspruch offengelegt, keine Owner-Entscheidung.
- Keine blockierenden Findings; vier LOW-Präzisierungen im finalen Commit bereinigt.
- **Fokussierter Re-Check:** **PASS** für `b85ef7e2ae9ced55ef3b393399688fb8b03b3ce1` (finaler SHA; nur LOW-Dokumentations-/Annotationskorrekturen gegenüber `fe3bd6e`).

## 5. Korrekturzyklus (Runde 3)

| Runde | Candidate | Reviewer A | Reviewer B | Ergebnis |
|---|---|---|---|---|
| 1 | `562fff77` | FAIL (HIGH/MEDIUM/LOW) | FAIL (MEDIUM/LOW) | K5-Lücke, Cash-Peak, Q1/Q2-Text, Wettbewerber-Belege, Konsistenz |
| 2 | `fe3bd6ec` | **PASS** | **PASS** | Alle Pflichtkorrekturen umgesetzt; LOW-Housekeeping im finalen Commit |

**Wichtig:** Die Reviewer haben selbst gerechnet und die Primärquellen selbst abgerufen; die Autorentests wurden nicht als Beweis übernommen. Die Reviewer-Berichte sind keine Selbstrezension.

## 6. Q3 — Status und Wirkung

| Frage | Status | Wirkung |
|---|---|---|
| 47.500 vs. 47.381,25 | **UNRESOLVED** | 118,75 €; nicht blockierend bei konservativer Planung; blockierend nur für Maximalausschöpfung |
| Second Stage 31.667 vs. 31.570,87 | **UNRESOLVED** | 96,13 € (633 h) / 46,25 € (634 h); nicht blockierend |
| 10-Monats-Option | **VERIFIED (RL)**; Kommunikation inkonsistent | Nur relevant, falls 10 Monate beantragt werden |

**Anfrage:** Entwurf in [q3-clarification.md](q3-clarification.md) §7; **nicht versendet**. Owner-Freigabe erforderlich. Keine der fünf Erklärungen (E1–E5) wird als offizielle Klärung dargestellt.

## 7. Vergleich und bedingte Empfehlung

**Vergleich:** [comparison-report.md](comparison-report.md) mit F1 (Feldexa-App), F2 (ProofLayer), F3 (FormBridge) und RP (RepairProbe). **Keine Entscheidung für den Owner.**

**Bedingte Empfehlung:** Für die **Innovationslinie** ist **F3 (FormBridge im Feldexa-Kontext)** die stärkere Bewerbungshypothese — wegen Linienfit (Software-Infrastruktur), Evidenzdisziplin (13-Projekte-Audit, Referenzfall) und vollständigem Bewerbungsnarrativ. Das ist **keine** Aussage, dass F3 technisch reifer ist: F3 hat **keinen Pipeline-Code**; die Feldexa-App hat 240 Tests, aber keine verifizierte E2E-PDF-Pipeline. **RepairProbe** hat die reifere öffentlich behauptete Baseline (24–44 Tests, privat) und eine direktere Endnutzer-Geschichte, aber schwächere Novelty-/Bedarfs-evidenz und eine schwächere Linienpassung.

**Wenn der Owner technische Demonstrierbarkeit höher gewichtet als Linienfit/Novelty, ist RP rational.** Wenn der Owner den direkten Bürgernutzen der App priorisiert, ist F1 die stärkere Geschichte, aber die Innovationslinie der schwächere Weg. Der Owner entscheidet.

## 8. Verbleibende Owner-Entscheidungen

Vollständige Klassifikation: [owner-questions-status.md](owner-questions-status.md).

**Harte formale Blocker:** M1 (Alter), M2 (Wohnsitz/Steuern), M3a/b/c (Selbstständigkeit/Freistellung), M4 (Programmierkenntnisse), M5 (Vorarbeiten/Kenntnisse), M6 (De-minimis). **M8** (Kontoauszug) ist erst bei Bewilligung formal. **M7** (Kapazität) und **M9** (Second Stage) sind Planung, keine formalen Blocker.

**Kritischste Klärung:** **Q2/M3c** — Selbstständigkeit erst ab Förderbeginn. Öffentlich nicht geregelt; potenziell harte Hürde. **Q3/Q3b** sind finanziell, nicht einreichungsblockierend.

## 9. Branch / Commit / PR

- **Branch:** `docs/funding-decision-2026-11-13`
- **Erst geprüfter Candidate:** `fe3bd6ec891575fdae6f05d717de7697819302cd`
- **Final geprüfter Candidate:** `b85ef7e2ae9ced55ef3b393399688fb8b03b3ce1` (Reviewer A/B: PASS im fokussierten Re-Check)
- **Finaler Dokumentations-Commit:** fügt nach diesem Re-Check nur die Re-Check-Notiz und LOW-Wortlautkorrekturen hinzu; der geprüfte Code-/Zahlenstand bleibt `b85ef7e2`.
- **PR:** [#1](https://github.com/xxammaxx/FormBridge/pull/1) (Draft, `MERGEABLE`, `CLEAN`); die Draft-PRs #152/#168 im Feldexa-Repo bleiben unverändert.
- **Nicht geändert:** Feldexa-App-Code, RepairProbe-Repo/Portal-Draft, Lizenzen, Anwendungen.

## 10. Gate-Ergebnis

| Kriterium | Status |
|---|---|
| Finanzberechnungen unabhängig verifiziert | ✅ Reviewer A PASS; 109/109 |
| Tests reproduzierbar | ✅ 109/109, archiviert |
| Beide unabhängigen Reviews | ✅ A PASS, B PASS |
| Feldexa-2.0/FormBridge-vs-RepairProbe-Vergleich | ✅ vollständig, evidenzbasiert, keine Owner-Entscheidung |
| Q3 | ⚠️ UNRESOLVED, aber nicht blockierend; 118,75 € quantifiziert |
| Owner-Fragen | ⚠️ M1–M9 offen, klar getrennt |
| Dokumentation konsistent | ✅ Linkcheck 0 broken, Zahlen abgeglichen |

**Fazit:** **VALIDATED_WITH_OPEN_QUESTIONS** — kein uneingeschränkter PASS, solange Q3/Q3b offen sind; für die Einreichung mit konservativer Planung ist der Stand belastbar. **Keine Förderzusage.**
