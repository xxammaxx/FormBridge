# Finaler Validierungsbericht — Runde 3

**Status: DRAFT / PENDING REVIEWS.** Dieser Bericht wird nach Abschluss der unabhängigen Reviews A und B mit den tatsächlichen Verdicts, Findings und dem finalen Candidate-SHA gefüllt. Bis dahin sind die unten genannten Zahlen die geprüften Autorenwerte, **keine** unabhängig bestätigten Reviewer-Ergebnisse.

## 1. Finanzielle Baseline

| Größe | Wert |
|---|---:|
| Personalkosten (950 h × 50 €) | 47.500,00 € |
| Gemeinkosten (5 % PK) | 2.375,00 € |
| Gesamtkosten | 49.875,00 € |
| Förderung (95 %) | 47.381,25 € |
| Eigenanteil (5 %) | 2.493,75 € |
| Kommunizierte Maximalförderung | 47.500,00 € |
| Q3-Differenz | 118,75 € |

**Status:** 47.381,25 € ist die konservative Planungsbasis; Q3 bleibt **UNRESOLVED** und ist bei konservativer Planung nicht einreichungsblockierend.

## 2. Testevidenz

- Befehl: `python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v`
- Ergebnis: **109/109 PASS**
- Archiv: [`validation/test-output.txt`](validation/test-output.txt), [`validation/scenario-report.md`](validation/scenario-report.md), [`validation/RUNBOOK.md`](validation/RUNBOOK.md)
- Frühere 56/57-Behauptung: **nicht reproduzierbar**, ersetzt.

## 3. Reviewer A — Finanzen

**Verdict: PENDING.** Findings/Schweregrad/Korrekturen: nach Review.

## 4. Reviewer B — Förderrecht/Evidenz/Vergleich

**Verdict: PENDING.** Findings/Schweregrad/Korrekturen: nach Review.

## 5. Korrekturzyklus

**Status: PENDING.** Nach den Reviews werden Befunde, kleinste Korrekturen, Re-Tests und der neue Candidate-SHA hier dokumentiert.

## 6. Verbleibende Owner-Entscheidungen

- M1–M9: [owner-questions-status.md](owner-questions-status.md); Q2 ist der kritischste Punkt.
- F1/F2/F3 vs. RepairProbe: Owner entscheidet; bedingte Empfehlung F3 in [comparison-report.md](comparison-report.md).
- Q3-Anfrage: Entwurf in [q3-clarification.md](q3-clarification.md), **nicht versendet**.

## 7. Candidate-SHA / Branch / PR

- Branch: `docs/funding-decision-2026-11-13`
- Candidate: wird nach dem Commit eingetragen.
- PR: wird nach dem Commit erstellt/aktualisiert.

## 8. Gate

**Vorläufig:** `VALIDATED_WITH_OPEN_QUESTIONS` — Q3/Q3b offen, aber quantifiziert und nicht blockierend; finale Reviewer-Verdicts stehen aus.
