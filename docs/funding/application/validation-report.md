# Revalidierungsbericht — FormBridge-Bewerbung (final)

**Review-PASS Bewerbungspaket:** `9ed862253da0be133157540ae0891d26bf65ade9` · **Gründungs-Delta:** `d062d9db` · **Readiness-Delta:** `ef968f9` · **Branch:** `docs/funding-decision-2026-11-13` (25.11.2026 nach `main` konsolidiert) · **Datum:** 14.11.2026
**Reviewer Bewerbungspaket:** A **PASS**, B **PASS** ([Review-Bericht](review-report.md)) · **Reviewer Readiness/Gründung:** A **PASS**, B **PASS** ([Readiness-Review](review-application-readiness-2026-11-14.md)) · **Tests:** 109/109 PASS · **Relative Links:** 251, 0 gebrochen (Stand Nachführungs-Commit `58edd9f`; nach der Konsolidierung ist `main` maßgeblich)
**Hinweis:** Die A/B-PASS-Zeilen oben gelten für ihre jeweiligen Baseline-SHAs (`9ed8622`, `d062d9d`, `ef968f9`). Die Nachführung von Wortzahlen und Metriken erfolgte in `58edd9f`; spätere Deltas (Owner-Texte, Entscheidungen, Evidenzsuite) sind dokumentarisch belegt bzw. ausgeführt, aber nicht erneut unabhängig reviewt. Seit dem Merge vom 25.11.2026 ist `main` der maßgebliche Stand; die aktuellen Metriken stehen in §0.
**Gate:** **READY_FOR_PORTAL_FIELDS** — Bewerbungstext und Feldvorlage sind vollständig vorbereitet; §11–§15 und §18 sind seit 25.11.2026 final, **M1–M9 sind beantwortet** (M6: 0 € De-minimis-Vorbelastung; M7: Kapazität bestätigt; M8: Liquidität ≥ 2.500 € geplant). Offen sind nur die **Portal-Stammdaten A2–A5a**, der authentifizierte Live-Abgleich und die **Stichtagsfrage** aus Q2 (Registrierung vor Förderbeginn geplant).

## 0. Nachführung auf den Branch-Tip (25.11.2026)

| Prüfung | Ergebnis (Stand Tip) |
|---|---|
| Nachführungs-Commit | `58edd9f73bf986d688bc6e241446c57b5b782d59` — alle Metriken dieser Tabelle gelten für diesen Baum; danach folgt nur noch eine Kennzeichnungs-Ergänzung ohne Inhaltsänderung |
| Tests | **109/109 PASS** (`python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -q`) |
| Relative Links (Markdown, Branch-Baum) | **251 geprüft, 0 gebrochen** |
| Wortzahlen §1–§18 | nachgezählt mit der in [application-final-de.md](application-final-de.md) dokumentierten Zählregel; alle Abschnitte innerhalb der Limits |
| Owner-Texte §11 (E1) / §14 (E5) | **final** (25.11.2026): 77/100 bzw. 83/100 Wörter, Status FINAL, Platzhalter entfernt; synchronisiert in `portal-field-mapping.md`, `portal-preflight-2026-11-14.md`, `owner-checklist.md` |
| Owner-Entscheidungen §12 (E2/E3), §13 (E4), §15 (S1), §18 (Q19a/b) | **final** (25.11.2026): E2 = Nein (E3 entfällt, Vorlagetext 11 W.), 950 h, Second Stage = Ja (§16/§17 final), beide Q19-Zusagen erteilt |
| Evidenz-Integritätssuite | **19/19 PASS** (`python3 -m unittest discover -s docs/research/evidence -p 'test_*.py' -q`); Hashregister in [EVIDENCE.md](../../research/evidence/EVIDENCE.md) |
| Q5/E3-Wortzahl | **31 W. inkl. Platzhalterhinweis (11 W. Antworttext) / 60** — einheitlich in application-final-de.md, portal-field-mapping.md, portal-preflight-2026-11-14.md |
| Überschriebene Abweichungen | frühere Zahlen aus älteren Baselines (`§2 97`, `§3 169`, `§4 133`, `Q5 21` als Fehlzählung) sind in [portal-field-mapping.md](portal-field-mapping.md) durch die verifizierten Werte ersetzt; der Preflight-Snapshot kennzeichnet seine Zahlen als historisch |

Diese Nachführung ändert keine Bewertung, keine Frist und keine Förderzusage; sie beseitigt ausschließlich Zahlen- und Baseline-Drift zwischen den Dokumenten.

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
| FOSS | Zusage vorhanden; **Lizenz entschieden: Apache-2.0** (25.11.2026), `LICENSE` committet, SPDX `Apache-2.0` |
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
| M1 | Alter ≥ 18 | **BEANTWORTET (25.11.2026)** | Owner-Bestätigung liegt vor |
| M2 | Wohnsitz DE + Steuern DE | **BEANTWORTET (25.11.2026)** | Owner-Bestätigung liegt vor |
| M3a/b/c | Selbstständig/freiberuflich oder Freistellung; M3c Aufnahme 2027 | Plan: **Registrierung vor Förderbeginn (01.06.2027)** und vor dem formalen BMFTR-Antrag | Offen ist nur der exakte **Stichtag** (Online-Bewerbung vs. formaler Antrag März 2027) — PTF-Auskunft ausstehend; nicht blockierend bei Registrierung vor Förderbeginn |
| Q2 | Materielle Selbstständigkeitsvoraussetzung und Nachweiszeitpunkt | `[PTF_BESTÄTIGUNG]` | **CONTRADICTED:** JG03-FAQ/Bewerbungsseite verlangen Selbstständigkeit/Freistellung; JG03-Handbuch nennt sie nicht unter den zwingenden Förderbedingungen; Online-Fragen ohne Statusfeld; JG02-Wiki verlangt Steuernummer zum formalen Antrag. Analyse: [q2-employment-status.md](../decision/q2-employment-status.md) |
| M4 | Programmierkenntnisse | **belegt (25.11.2026)** | §14 beschreibt Praxis, Datenmodelle, Skripte und automatisierte Tests |
| M5 | Vorarbeiten/Kenntnisse | **erledigt (25.11.2026)** | §11/§14 final personalisiert (77 bzw. 83 W.) |
| M6 | De-minimis-Historie | **BEANTWORTET (25.11.2026): 0 €** | De-minimis-Erklärung im formalen Antrag |
| M7 | Kapazität 950 h / 6 Monate (158 h/Monat) | **BEANTWORTET (25.11.2026): bestätigt/geplant** | Kapazitätsplan bei Bedarf nachführen |
| M8 | Kontoauszug ≥ 2.493,75 € | **BEANTWORTET (25.11.2026): bestätigt/geplant** | Vorlage erst bei Bewilligung formal |

**Q2/M3c** bleibt die einzige offene Zulassungsfrage — als **Stichtagsfrage**, nicht als Erfüllungsfrage. Die Quellenlage ist **widersprüchlich**: FAQ/Bewerbungsseite verlangen Selbstständigkeit/Freistellung; das JG03-Handbuch listet sie nicht unter den zwingenden Förderbedingungen und spricht von „Privatperson“; die Online-Fragen enthalten kein Statusfeld; das JG02-Wiki verlangt eine Steuernummer/Anmeldung zum **formalen Antrag**. Der Plan erfüllt die Voraussetzung, indem die selbstständige/freiberufliche Registrierung **vor dem formalen Förderbeginn (01.06.2027)** und **vor dem formalen BMFTR-Antrag** erfolgt; nur der exakte Stichtag ist noch zu bestätigen. **Keine Anfrage versendet.**

### 3.2 Portal-Live-Prüfung

- Exakte Zeichenlimits, Pflichtfeldmarkierungen, Q19-Checkbox-Formulierung: `PORTAL_UNVERIFIED`.
- Portal ist login-geschützt; die öffentliche Landingpage ist erreichbar, `/jahrgang-03-innovation/` leitet auf `/auth/`.
- **Keine authentifizierte Sitzung** am 14.11.2026; Login ist eine einmalige Owner-Aktion.
- Vor „Submit“: Live-Fragen und Limits gegen [portal-field-mapping.md](portal-field-mapping.md) und [portal-preflight-2026-11-14.md](portal-preflight-2026-11-14.md) prüfen.

### 3.3 Owner-Entscheidungen

- ~~Lizenz~~ — **entschieden: Apache-2.0 (25.11.2026)**, `LICENSE` committet.
- ~~950 oder 850 h~~ — **entschieden: 950 h (25.11.2026)**.
- ~~Second Stage Ja/Nein~~ — **entschieden: Ja (25.11.2026)**, §16/§17 final.
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
| Materielle Teilnahmevoraussetzung | **Plan erfüllt; offen ist der Stichtag:** BMFTR-RL Nr. 3 und JG03-FAQ/Bewerbungsseite verlangen selbstständige Programmierer*innen bzw. Freiberuflichkeit oder Arbeitgeber-Freistellung. Die selbstständige/freiberufliche Registrierung ist **vor Förderbeginn (01.06.2027) und vor dem formalen BMFTR-Antrag** eingeplant; zu bestätigen ist nur der exakte Stichtag. Das JG03-Handbuch listet die Voraussetzung **nicht** unter den zwingenden Förderbedingungen (Redaktionslücke) und spricht von „Privatperson“. |
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
- Bewerbungspaket-Basis `9ed86225`; Gründungs-Delta `d062d9db`; Readiness-Delta `ef968f9` (A/B PASS, [Readiness-Review](review-application-readiness-2026-11-14.md)); Working Tree clean.
- Keine Einreichung, keine E-Mail, keine Portaländerung, keine Lizenzfestlegung im Rahmen dieses Reviews, kein Merge. *(Die Lizenz wurde separat durch den Eigentümer am 25.11.2026 auf Apache-2.0 festgelegt.)*

## 5. Gate-Begründung

**READY_WITH_EXPLICIT_BLOCKERS** für den Portal-Preflight (Bewerbungspaket: `READY_FOR_OWNER_INPUT`), weil:

- alle öffentlich prüfbaren Anforderungen erfüllt sind, soweit öffentlich belegbar, und beide Reviews PASS sind;
- aber M1–M6, **die materielle Q2-Frage**, die Portal-Live-Prüfung (kein Login) und die Lizenz-/Second-Stage-Entscheidung echte Owner-/externe Voraussetzungen sind;
- Q3/Q3b bewusst offen, aber quantifiziert und bei konservativer Planung nicht einreichungsblockierend.

**Nicht** `READY_FOR_PORTAL_OWNER_APPROVAL`, solange Q2/M3c, die persönlichen Pflichtangaben und der Live-Abgleich nicht geklärt sind. **Nicht** `VALIDATION_FAILED`; es gibt keinen ungelösten materiellen Fehler. **Nicht** `BLOCKED`; die offenen Punkte sind Owner-Input, nicht fehlender Zugriff.
