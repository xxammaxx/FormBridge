# Validierungs-Runbook — Finanzmodell v4

**Zweck:** Jede Zahl in [financial-model.md](../financial-model.md) muss von
Dritten ohne Spezialumgebung nachgerechnet werden können. Dieses Runbook
archiviert Befehl, Eingaben, Rundungsregeln und Ergebnis.

## 1. Umgebung

| Punkt | Wert |
|---|---|
| Datum | 13.11.2026 |
| Python | 3.14.8 (getestet); 3.12-kompatibel (nur stdlib `unittest`, `decimal`) |
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
Ran 109 tests in ...s

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
| `TestCashFlow` | Raten, Monats-/Quartalskosten, kumulativer Peak | 14 |
| `TestDeminimis` | 0/260k/299,9k/300k/310k, Kombination regular+second | 8 |
| `TestInvalidModels` | alte/fehlerhafte Modelle, 95-%-Verletzungen | 8 |
| `TestTenMonth` | 83.337-Cap, 79.170,15, Kombination, K5 | 12 |
| **Summe** | | **109** |

## 7. Grenzen

- Das Modell prüft **Arithmetik und Regelkonsistenz**, nicht die Rechtsgültigkeit einer Förderzusage.
- Es prüft **nicht**, ob das Portal die FAQ- oder die strenge Logik anwendet (Q3).
- Es prüft **nicht** die persönliche Förderfähigkeit (M1–M9).
- Es prüft **nicht** die Zweckmäßigkeit oder Jury-Chancen des Projekts.
- Die 10-Monats-Option ist als Szenario I abgebildet, nicht als Baseline.

## 8. Reproduktionsnachweis

| Datei | SHA-256 |
|---|---|
| `financial_model.py` | `1b4e281e01910991a93bee05006f165274d335d8276565cb437b26093fe0939d` |
| `test_financial_model.py` | `a60bcc4a305d470d41cc970ffc887991f1075ce99d44d10a372606e75bfdd579` |
| `scenario-report.md` | `2a05539028a36d5d73b36b91e4d08f39b15ae5c069695622e82d23a484561383` |

Diese Hashes sind die **Candidate-Hashes** des geprüften Modell-/Teststands. Der finale Dokumentations-Commit kann die Hashes nicht selbst enthalten (Self-Reference); der geprüfte Candidate ist in [`final-validation-report.md`](../final-validation-report.md) §9 genannt.
