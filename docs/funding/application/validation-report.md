# Revalidierungsbericht — FormBridge-Bewerbung (final)

**Candidate:** `9ed862253da0be133157540ae0891d26bf65ade9` · **Branch:** `docs/funding-decision-2026-11-13` · **Datum:** 13.11.2026
**Reviewer:** A **PASS**, B **PASS** ([Review-Bericht](review-report.md)) · **Tests:** 109/109 PASS · **Relative Links:** 0 gebrochen
**Gate:** **APPLICATION_READY_WITH_BLOCKERS** — Bewerbung vollständig vorbereitet; die verbleibenden Punkte sind ausschließlich Owner-Angaben, Owner-Entscheidungen, Portal-Live-Prüfung und ausdrücklich benannte externe Klärungen.

## 1. Was geprüft wurde

| Bereich | Ergebnis |
|---|---|
| Offizielle Fragen Jahrgang 03 Innovation | Vollständig gemappt (Fragen-PDF, 8 S., SHA-256 `1d6848c4…4fb74`) |
| Wortlimits | Aus Handbuch Jahrgang 03; alle Abschnitte innerhalb der Limits; Portal-Tokenizer `PORTAL_UNVERIFIED` |
| Q19-Bestätigungen | 18+/Hauptwohnsitz DE und FOSS-Lizenz vorhanden |
| Finanzen 950 h | PK 47.500,00 / GK 2.375,00 / G 49.875,00 / F **47.381,25** / EA **2.493,75** |
| Finanzen 850 h | PK 42.500,00 / GK 2.125,00 / G 44.625,00 / F **42.393,75** / EA **2.231,25** |
| 800 h | Nur Sensitivität, ausdrücklich keine Antragsoption |
| Q3/Q3b | **UNRESOLVED**; 118,75 € / 96,13 € / 46,25 €; konservativ geplant |
| Second Stage | 633 h 31.570,87 €; 634 h 31.620,75 €; Cap 31.670,15 € |
| De-minimis | 300.000 € / rollierende 3 Jahre; 3 Jahre Aufbewahrung |
| FOSS | Zusage vorhanden; **keine Lizenz festgelegt**; Apache-2.0 nur Empfehlung |
| Vorarbeit/Förderbeginn | Kein Modulcode; Vorarbeit nicht abgerechnet; Feldexa nicht integriert |
| Implementierungsstand | **NICHT IMPLEMENTIERT**; nur Forschung/Spezifikation |
| Reviewer A | **PASS** |
| Reviewer B | **PASS** |

## 2. Wesentliche Korrekturen der Review-Runden

| Befund | Korrektur |
|---|---|
| Q19-Bestätigungen fehlten | Application §18, Portal-Mapping E, Owner-Checkliste, Runbook ergänzt |
| Allgemeine Angaben zu grob | A1–A6 einzeln gemappt (Projekttitel, Accountname, Name, E-Mail, persönlicher GitHub-Link, Projektlink) |
| Q4/Q5 vermischt | Q4 Ja/Nein; Q5 nur falls Q4 = Ja; keine unbestätigte persönliche Negativaussage |
| Q7 unvollständig | Vollwortlaut inkl. „warum nicht auf ihnen aufbauen“; §7 beantwortet es |
| E1 ohne Link-Anforderung | Vollwortlaut; §11 mit Repository-Links |
| 800 h inkonsistent | Nur Sensitivität; 950/850 sind die Antragsoptionen |
| Evaluationsmetriken unklar | Mapping-fähige Felder vs. Gap/UNMATCHED; P/R vor Review; End-to-End separat; Coverage/Gap-Grenzen |
| 20-%-Gap-Blockade | 120 total/≥96 mapping-fähig (850: 100/≥80); P/R nur auf mapping-fähig |
| FITKO „in der Konzeption“ veraltet | FIM-Portal-Konverter live; RF2 = Reparatur veröffentlichter defekter XSDs |
| Manifest overclaim | Audit-Artefakt, kein Tamper-Proof; C2PA/pyHanko nicht integriert |
| FOSS zu absolut | Nur eigene Ergebnisse; amtliche PDFs/XSDs und abgeleitete FIM-Metadaten nur nach Rechteklärung |
| Feldexa-Status unklar | Vorgesehene erste Anwendung, nicht integriert, nicht Förderumfang |
| D21-Formulierung | 68 % der Medienbrüche unfreiwillig; Item-Basis n=5.725, Gesamt n=8.091 (Gesamt-n nicht unabhängig geprüft) |
| 170-Terminologie | 170 Parser-Fehler = 1 NCName + 169 D2-Meldungen |
| `__pycache__` eingecheckt | Entfernt; `.gitignore` ergänzt |
| Decision-PASS vs. Application-PASS | Scope-Hinweis im Decision-Report |

## 3. Verbleibende Blocker (Owner/extern)

### 3.1 Harte persönliche/formale Blocker

| # | Blocker | Status | Was fehlt |
|---|---|---|---|
| M1 | Alter ≥ 18 | `[OWNER_BESTÄTIGUNG]` | Eigene Bestätigung |
| M2 | Wohnsitz DE + Steuern DE | `[OWNER_BESTÄTIGUNG]` | Eigene Bestätigung |
| M3a/b/c | Selbstständig/freiberuflich oder Freistellung; M3c Selbstständigkeit ab Förderbeginn | `[OWNER_BESTÄTIGUNG]` / `[PTF_BESTÄTIGUNG]` | Status + ggf. PTF-Antwort (Q2) |
| M4 | Programmierkenntnisse | `[OWNER_BESTÄTIGUNG]` | Eigene Bestätigung |
| M5 | Vorarbeiten/Kenntnisse | `[OWNER_ANGABE]` | §11/§14 personalisieren |
| M6 | De-minimis-Historie | `[OWNER_ANGABE]` | Beihilfen der letzten 3 Jahre addieren |
| M8 | Kontoauszug ≥ 2.493,75 € | `[OWNER_BESTÄTIGUNG]` | Erst bei Bewilligung formal |

**Q2/M3c** ist die einzige potenziell harte externe Hürde. **Keine Anfrage versendet.**

### 3.2 Portal-Live-Prüfung

- Exakte Zeichenlimits, Pflichtfeldmarkierungen, Q19-Checkbox-Formulierung: `PORTAL_UNVERIFIED`.
- Portal ist login-geschützt; die öffentliche Landingpage ist erreichbar, `/jahrgang-03-innovation/` leitet auf `/auth/`.
- Vor „Submit“: Live-Fragen und Limits gegen [portal-field-mapping.md](portal-field-mapping.md) prüfen.

### 3.3 Owner-Entscheidungen

- Lizenz (Apache-2.0 empfohlen, nicht festgelegt).
- 950 oder 850 h (Default 950; 850 nur bewusste Änderung).
- Second Stage Ja/Nein (Default Ja; §16/§17 sonst entfernen).
- Projektfassung F1/F2/F3 vs. RepairProbe.
- Q3/Q3b-Anfrage senden oder zurückstellen.
- Held-out-PDF/Rechte; Fürther PDF/FIM-XSD-Rechte.

### 3.4 Bewusst offene, nicht blockierende Fragen

- Q3: 47.500 vs. 47.381,25 (118,75 €).
- Q3b: 31.667 vs. 31.570,87/31.620,75 (96,13/46,25 €).
- 10-Monats-Option (nur falls gewollt).
- Held-out-PDF nicht gesichert; Fallback qualitativ.
- M5-Tightness (155 h) und externe Testpersonen (n=2–3) bleiben Risiken.
- Kein benannter Adopter/Pilotpartner.

## 4. Test- und Reproduktionsnachweis

```bash
python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v
# Ran 109 tests ... OK
```

- Relative Links: 0 gebrochen.
- `git ls-files` enthält keine `.pyc`/`__pycache__`.
- Candidate `9ed86225`; Working Tree clean.
- Keine Einreichung, keine E-Mail, keine Portaländerung, keine Lizenzfestlegung, kein Merge.

## 5. Gate-Begründung

**APPLICATION_READY_WITH_BLOCKERS**, weil:

- alle öffentlich prüfbaren Anforderungen erfüllt und beide Reviews PASS sind;
- aber M1–M6, Q2, die Portal-Live-Prüfung und die Lizenz-/Second-Stage-Entscheidung echte Owner-/externe Voraussetzungen sind;
- Q3/Q3b bewusst offen, aber quantifiziert und bei konservativer Planung nicht einreichungsblockierend.

**Nicht** `APPLICATION_READY_FOR_OWNER_REVIEW`, solange Q2/M3c und die persönlichen Pflichtangaben nicht geklärt sind. **Nicht** `VALIDATION_FAILED`; es gibt keinen ungelösten materiellen Fehler. **Nicht** `BLOCKED`; die offenen Punkte sind Owner-Input, nicht fehlender Zugriff.
