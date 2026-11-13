# Validierungs-Runbook — Finanzmodell v4

**Zweck:** Jede Zahl in [financial-model.md](../financial-model.md) muss von
Dritten ohne Spezialumgebung nachgerechnet werden können. Dieses Runbook
archiviert Befehl, Eingaben, Rundungsregeln und Ergebnis.

## 1. Umgebung

| Punkt | Wert |
|---|---|
| Datum | 13.11.2026 |
| Python | 3.12 (stdlib `unittest`, `decimal`) |
| Externe Abhängigkeiten | keine |
| Betriebssystem | Linux |
| Arbeitsverzeichnis | Repository-Root (`FormBridge/`) |

## 2. Befehl

```bash
python3 -m unittest discover \
  -s docs/funding/decision/validation \
  -p 'test_*.py' -v
```

Ausgabe in [`test-output.txt`](test-output.txt). Erwartet:

```text
Ran 102 tests in ...s

OK
```

## 3. Szenariotabelle erzeugen

```bash
cd docs/funding/decision/validation
python3 financial_model.py > scenario-report.md
```

## 4. Eingabeannahmen

| Annahme | Wert | Quelle |
|---|---|---|
| Stundensatz | 50,00 €/h | FAQ Förderung 01; Handbuch Frage 14 |
| Max. Stunden (regulär) | 950 h | Handbuch Frage 14 |
| Gemeinkostenpauschale | 5 % der Personalkosten | FAQ Förderung 02 |
| Förderquote | 95 % | RL Nr. 5 |
| Gesamtkosten-Cap (regulär) | 50.000,00 € | RL Nr. 5 |
| Gesamtkosten-Cap (Second Stage) | 33.337,00 € | RL Nr. 5 |
| Gesamtkosten-Cap (10 Monate) | 83.337,00 € | RL Nr. 5 (Summe) |
| De-minimis | 300.000,00 € / rollierende 3 Jahre | RL Anlage Nr. 1; VO 2023/2831 |
| Kommunizierte Maximalförderung | 47.500,00 € | FAQ Förderung 01 |
| Kommunizierte Second-Stage-Förderung | 31.667,00 € | FAQ Förderung 01 |
| Kommunizierte 10-Monats-Förderung | 79.167,00 € | FAQ Grundlagen 01 |

## 5. Rundungsregeln (kurz)

- PK: Half-up auf Cent.
- GK: **Floor** auf Cent (nie > 5 % PK).
- G: exakte Summe PK + GK.
- F: **Floor** auf Cent (nie > 95 % G).
- EA: G − F (exakt).
- Quartalsraten: Floor, letzte Rate = Rest.

Vollständige Begründung: [financial-model.md](../financial-model.md) §2.

## 6. Was die Suite prüft

| Klasse | Inhalt | Tests |
|---|---|---:|
| `TestBaseline` | 950-h-Baseline, Identitäten, 118,75-Differenz | 15 |
| `TestScenarios` | A–F, Ratenhebel, FAQ-Frame E, 1.000-h-Alternative | 13 |
| `TestCapsAndBoundaries` | 950/951 h, 50.000/50.000,01 €, 5 % GK, Rate > 50 | 17 |
| `TestRounding` | Half-up/Floor, Quartalssummen, Cent-Exaktheit | 11 |
| `TestSecondStage` | 633/634/635 h, 31.667-Differenz, Rate-Cap | 11 |
| `TestCashFlow` | Raten, Monats-/Quartalskosten, Peak | 10 |
| `TestDeminimis` | 0/260k/299,9k/300k/310k, Kombination regular+second | 8 |
| `TestInvalidModels` | alte/fehlerhafte Modelle, 95-%-Verletzungen | 8 |
| `TestTenMonth` | 83.337-Cap, 79.170,15, Kombination | 9 |
| **Summe** | | **102** |

## 7. Grenzen

- Das Modell prüft **Arithmetik und Regelkonsistenz**, nicht die Rechtsgültigkeit einer Förderzusage.
- Es prüft **nicht**, ob das Portal die FAQ- oder die strenge Logik anwendet (Q3).
- Es prüft **nicht** die persönliche Förderfähigkeit (M1–M9).
- Es prüft **nicht** die Zweckmäßigkeit oder Jury-Chancen des Projekts.
- Die 10-Monats-Option ist als Szenario I abgebildet, nicht als Baseline.

## 8. Reproduktionsnachweis

| Datei | SHA-256 |
|---|---|
| `financial_model.py` | `b849c9d3723a2741bb6389f17c3555780624a886a9d8e11eeca55f233b231244` |
| `test_financial_model.py` | `c7a5f363a01581e09bc9b99ea2afc0a120b16fa2e65f761dd86762c1a9d8bbeb` |
| `scenario-report.md` | `8eb7a084fb421ce7d7e485dc2f66608ef7a59a511b77f03473b3f41f665eb8f8` |

Diese Hashes beziehen sich auf den Stand **vor** dem finalen Commit; nach dem
Commit werden sie in [`final-validation-report.md`](../final-validation-report.md)
mit dem Candidate-SHA erneut ausgewiesen.
