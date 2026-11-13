# Revalidierungsbericht — FormBridge-Bewerbung (final)

**Review-PASS Bewerbungspaket:** `9ed862253da0be133157540ae0891d26bf65ade9` · **Q2/Owner-Input-Delta:** `d98e80eb892027d65067f2626b437a99e5048883` (dokumentations-only) · **Branch:** `docs/funding-decision-2026-11-13` · **Datum:** 13.11.2026
**Reviewer Bewerbungspaket:** A **PASS**, B **PASS** ([Review-Bericht](review-report.md)) · **Reviewer Gründungs-Delta:** A **PASS (bedingt, `STRATEGY_CONDITIONALLY_VALID`)**, B **PASS (bedingt, `EXTERNAL_CONFIRMATION_REQUIRED`)** · **Tests:** 109/109 PASS · **Relative Links:** 0 gebrochen
**Gate:** **READY_WITH_EXPLICIT_BLOCKERS** für den Portal-Preflight — Bewerbungstext und Feldvorlage sind vollständig vorbereitet; offen sind der authentifizierte Live-Abgleich, persönliche Angaben, die Second-Stage-/Stundenentscheidung und die materielle Q2-Klärung. Das Bewerbungspaket selbst bleibt `READY_FOR_OWNER_INPUT`.

## 1. Was geprüft wurde

| Bereich | Ergebnis |
|---|---|
| Offizielle Fragen Jahrgang 03 Innovation | Vollständig gemappt (Fragen-PDF, 8 S., SHA-256 `1d6848c4…4fb74`) |
| Wortlimits | Aus Handbuch Jahrgang 03; alle Abschnitte innerhalb der Limits; Portal-Tokenizer `PORTAL_UNVERIFIED` |
| Q19-Bestätigungen | Handbuch Q19: über 18/Hauptwohnsitz DE und FOSS-Zusage; **nicht im Fragen-PDF Innovation**, Portal-Checkbox `PORTAL_UNVERIFIED` |
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
| M3a/b/c | Selbstständig/freiberuflich oder Freistellung; M3c Aufnahme erst 2027 | `[OWNER_BESTÄTIGUNG]` / `[PTF_BESTÄTIGUNG]` | Status + PTF-Antwort (Q2); **formale Zulassungsvoraussetzung derzeit nicht erfüllt**; falls Zustimmung: Registrierung vor PTF-bestätigtem formalem Antrag |
| Q2 | Materielle Selbstständigkeitsvoraussetzung und Nachweiszeitpunkt | `[PTF_BESTÄTIGUNG]` | **CONTRADICTED:** JG03-FAQ/Bewerbungsseite verlangen Selbstständigkeit/Freistellung; JG03-Handbuch nennt sie nicht unter den zwingenden Förderbedingungen; Online-Fragen ohne Statusfeld; JG02-Wiki verlangt Steuernummer zum formalen Antrag. Analyse: [q2-employment-status.md](../decision/q2-employment-status.md) |
| M4 | Programmierkenntnisse | `[OWNER_BESTÄTIGUNG]` | Eigene Bestätigung |
| M5 | Vorarbeiten/Kenntnisse | `[OWNER_ANGABE]` | §11/§14 personalisieren |
| M6 | De-minimis-Historie | `[OWNER_ANGABE]` | Beihilfen der letzten 3 Jahre addieren |
| M8 | Kontoauszug ≥ 2.493,75 € | `[OWNER_BESTÄTIGUNG]` | Erst bei Bewilligung formal |

**Q2/M3c** ist das zentrale materielle Risiko. **Keine Anfrage versendet.** Die Quellenlage ist **widersprüchlich**: FAQ/Bewerbungsseite verlangen Selbstständigkeit/Freistellung; das JG03-Handbuch listet sie nicht unter den zwingenden Förderbedingungen und spricht von „Privatperson“; die Online-Fragen enthalten kein Statusfeld. Das JG02-Wiki verlangt eine Steuernummer/Anmeldung zum **formalen Antrag**. „Erst zum 01.06.2027" ist **nicht sicher**; konservativ: Registrierung **vor dem PTF-bestätigten formalen Antragstermin** oder Arbeitgeber-Freistellung. Die materielle Förderfähigkeit bleibt offen.

### 3.2 Portal-Live-Prüfung

- Exakte Zeichenlimits, Pflichtfeldmarkierungen, Q19-Checkbox-Formulierung: `PORTAL_UNVERIFIED`.
- Portal ist login-geschützt; die öffentliche Landingpage ist erreichbar, `/jahrgang-03-innovation/` leitet auf `/auth/`.
- **Keine authentifizierte Sitzung** am 14.11.2026; Login ist eine einmalige Owner-Aktion.
- Vor „Submit“: Live-Fragen und Limits gegen [portal-field-mapping.md](portal-field-mapping.md) und [portal-preflight-2026-11-14.md](portal-preflight-2026-11-14.md) prüfen.

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

## 3.5 Q2, Gründungsstrategie und Portal-Preflight (Stand 14.11.2026)

| Punkt | Ergebnis |
|---|---|
| Materielle Teilnahmevoraussetzung | **Formale Zulassungsvoraussetzung derzeit nicht erfüllt:** BMFTR-RL Nr. 3 und JG03-FAQ/Bewerbungsseite verlangen selbstständige Programmierer*innen bzw. Freiberuflichkeit oder Arbeitgeber-Freistellung. Das JG03-Handbuch listet Selbstständigkeit **nicht** unter den zwingenden Förderbedingungen (Redaktionslücke), spricht von „Privatperson“. **Materielles Risiko**, PTF-Anfrage nötig. |
| Nachweiszeitpunkt | Offizielle Online-Fragen (Innovation) enthalten **kein** Steuernummer-/Selbstständigkeitsfeld. JG03-Checkliste für Einzelpersonen: keine Solo-Steuernummer; JG02-Wiki: zum formalen Antrag. **Offen.** |
| Formaler Antrag | Antragswerkstatt **März 2027**; Detailseite nennt zugleich „bis Ende Februar“. **Terminwiderspruch**, PTF-bestätigen lassen. |
| „Erst zum 01.06.2027“ | **nicht sicher**; formaler Antrag liegt vor Förderbeginn; Registrierung ≠ Aufnahme |
| Empfohlene Variante | **A**: Bewerbung ohne falschen Status; nach Auswahl Registrierung **vor dem PTF-bestätigten formalen Antragstermin**; vor Tätigkeitsaufnahme (01.06.2027) Jobcenter/BA kontaktieren |
| Q2-Status | **CONTRADICTED / EXTERNAL_CONFIRMATION_REQUIRED**; kanonische Anfrage in [external-inquiry-drafts.md](../decision/external-inquiry-drafts.md) §A, **nicht versendet** |
| Portal-Preflight | **READY_WITH_EXPLICIT_BLOCKERS**: Text/Feldvorlage vorbereitet; keine authentifizierte Sitzung; persönliche Angaben fehlen; Q2 materiell offen. Siehe [portal-preflight-2026-11-14.md](portal-preflight-2026-11-14.md). |
| Gründungsförderung | Einstiegsgeld (§16b SGB II) und §16c SGB II sind Ermessensleistungen; Gründungszuschuss (§§93–94 SGB III) setzt ALG I, 150 Tage, Hauptberuflichkeit und Tragfähigkeit voraus; **keine pauschale Kumulierbarkeit** mit PTF. Nachgelagert: [post-selection-founding-plan.md](../decision/post-selection-founding-plan.md). |
| Persönliche Daten | keine im Repo; Owner-Input nur über Platzhalter/geschützten Bereich |

**Wichtig:** Die Projektzuwendung ist **kein frei verfügbares Nettoeinkommen**. Anrechnung, Doppelförderung, Liquidität und Steuern sind individuell mit Jobcenter/BA/Steuerberatung zu klären.

## 4. Test- und Reproduktionsnachweis

```bash
python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v
# Ran 109 tests ... OK
```

- Relative Links: 0 gebrochen.
- `git ls-files` enthält keine `.pyc`/`__pycache__`.
- Bewerbungspaket-Candidate `9ed86225`; Gründungs-Delta docs-only mit separatem Review (Candidate `d062d9db`, [Review](../decision/review-founder-strategy-2026-11-13.md)); Working Tree clean.
- Keine Einreichung, keine E-Mail, keine Portaländerung, keine Lizenzfestlegung, kein Merge.

## 5. Gate-Begründung

**READY_WITH_EXPLICIT_BLOCKERS** für den Portal-Preflight (Bewerbungspaket: `READY_FOR_OWNER_INPUT`), weil:

- alle öffentlich prüfbaren Anforderungen erfüllt sind, soweit öffentlich belegbar, und beide Reviews PASS sind;
- aber M1–M6, **die materielle Q2-Frage**, die Portal-Live-Prüfung (kein Login) und die Lizenz-/Second-Stage-Entscheidung echte Owner-/externe Voraussetzungen sind;
- Q3/Q3b bewusst offen, aber quantifiziert und bei konservativer Planung nicht einreichungsblockierend.

**Nicht** `READY_FOR_PORTAL_OWNER_APPROVAL`, solange Q2/M3c, die persönlichen Pflichtangaben und der Live-Abgleich nicht geklärt sind. **Nicht** `VALIDATION_FAILED`; es gibt keinen ungelösten materiellen Fehler. **Nicht** `BLOCKED`; die offenen Punkte sind Owner-Input, nicht fehlender Zugriff.
