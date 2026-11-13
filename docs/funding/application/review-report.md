# Unabhängige Reviews — FormBridge-Bewerbung (Runde 3, final)

**Geprüfter Candidate:** `9ed862253da0be133157540ae0891d26bf65ade9` · **Q2/Owner-Input-Delta:** `d98e80eb892027d65067f2626b437a99e5048883` (dokumentations-only) · **Branch:** `docs/funding-decision-2026-11-13`
**Verdicts:** Reviewer A **PASS** · Reviewer B **PASS**
**Charakter:** Zwei getrennte, read-only Reviewer-Prozesse mit eigenen Primärquellen-Abrufen. Keine Selbstrezension. Keine Förderzusage.

## Review A — Förderfähigkeit, Formalia und Finanzen

**Verdict: PASS**

**Geprüft:** offizielle Fragen (Fragen-PDF, 8 S., SHA-256 `1d6848c4…4fb74`), Handbuch Jahrgang 03 (31 S., SHA-256 `d3d19613…44f21`), Detail-/FAQ-/Innovationsseite, BMFTR-RL 2024 + Ä1/Ä2, Finanzmodell, Owner-Gates, FOSS, Vorarbeit/Förderbeginn, Portal-Erreichbarkeit (`PORTAL_UNVERIFIED`).

**Kernbefunde:**

- Alle offiziellen Felder A1–A6, P1–P9, T1/T2, E1–E5, S1–S3 und Q19a/b sind gemappt; keine fehlende/falsch nummerierte Frage.
- Wortlimits eingehalten (Whitespace-Zählung); §2 96/100 und §7 82/100 sind knapp, aber zulässig. Portal-Tokenizer bleibt `PORTAL_UNVERIFIED`.
- Q19-Bestätigungen (18+/Hauptwohnsitz DE; FOSS-Lizenz) vorhanden.
- Q4/Q5 korrekt getrennt; Q5 ist bedingt („nur falls Q4 = Ja“), keine unbestätigte persönliche Negativaussage.
- 950 h: PK 47.500,00 €; GK 2.375,00 €; G 49.875,00 €; F **47.381,25 €**; EA **2.493,75 €**.
- 850 h: **42.393,75 €** F; 800 h nur Sensitivität, keine Antragsoption.
- Q3/Q3b **UNRESOLVED**, konservativ geplant; 118,75 € / 96,13 € / 46,25 € dokumentiert.
- FOSS-Zusage ohne Lizenzfestlegung; amtliche PDFs/XSDs und abgeleitete FIM-Metadaten nur nach Rechteklärung.
- Kein Modulcode; Vorarbeit wird nicht als Förderleistung abgerechnet.
- 109/109 Tests; 0 gebrochene relative Links; keine `__pycache__`-Dateien mehr.

**Frühere Findings F1–F18/N1–N7:** alle materialen behoben (Q19, Allgemeine Angaben, Q4/Q5, Q7-Vollwortlaut, E1-Links, 800-h-Demotion, FOSS-Qualifier, Vorarbeit, Quellen, Scope-Note, Q5-Konditional, `.pycache`, D21-Item-Basis, 170-Terminologie, Spec ≥3/≥5).

**Residual LOW:** Wortzahlen 1–4 Wörter je nach Tokenizer; §2/§7 knapp; Q5-Wortzahl nach Owner-Befüllung neu zählen; 950/850-Statuslabel in Owner-Checkliste/Runbook angleichen; abgeleitete FIM-Metadaten-Exception präzisieren; E1-Links nach Owner-Befüllung prüfen.

## Review B — Innovation, Technik und Glaubwürdigkeit

**Verdict: PASS**

**Geprüft:** Problem/Zielgruppe/Nutzen, Neuheit und Abgrenzung, technische Machbarkeit, 6-Monats-Plan, Messbarkeit, Implementierungsstand, Datenschutz/Integrität, Feldexa-/ProofLayer-Abgrenzung, Prior Art.

**Kernbefunde:**

- Innovationskern (statisches PDF → versionierte FIM-IDs → UNKNOWN → Human Review → Provenienz-Manifest → Verifier) ist korpus-spezifisch belegt; keine weltweite Erstmaligkeitsbehauptung.
- FITKO/FIM-Portal-Konverter ist jetzt korrekt als live, aber ohne PDF→FIM-Zuordnung und ohne Reparatur des veröffentlichten defekten XSD dargestellt; RF2 ist auf Reparatur/normalisierte Semantikverlust-Prüfung verengt.
- Evaluationsprotokoll ist operational: mapping-fähige Felder vs. `COVERAGE_GAP`/`UNMATCHED`; P/R nur auf mapping-fähigen Feldern; `UNKNOWN` = Miss; Gap-Erkennung separat; P/R vor Review als Muss, End-to-End nach Review separat; 120 total/≥96 mapping-fähig (850: 100/≥80); Gap-Erkennung ≥90/85 %.
- 20-%-Gap-Blockade mathematisch aufgelöst; Recall ≥0,85 auf 96 mapping-fähigen Feldern erreichbar.
- 950-h-Muss 120/0,90/0,85/3 XSDs; 850-h-Muss 100/0,85/0,80/2 XSDs/8 Negativtests; Spec-Ziele 200/0,95/0,90/5 werden nicht als „Stretch“ umetikettiert.
- Manifest ist Audit-Artefakt, kein Tamper-Proof; C2PA/pyHanko nicht integriert; keine Sicherheitsüberclaim.
- FOSS nur eigene Ergebnisse; amtliche Artefakte per URL/Hash; abgeleitete FIM-Metadaten nur nach Rechteklärung.
- Feldexa 2.0: vorgesehene erste Anwendung, nicht integriert, nicht Förderumfang; zählt nicht als externe Integration.
- 109/109 Tests; 168 relative Links, 0 gebrochen; keine `__pycache__`.

**Residual LOW:** erwarteter Betriebspunkt Coverage/Recall explizit nennen; Mindestzahl Gap-Felder im Goldstandard; FOSS-Exception Plan/Anwendung angleichen; 170-Terminologie vereinheitlichen; D21-Gesamt-n=8.091 als nicht unabhängig geprüft kennzeichnen; M5-Tightness und Held-out-PDF bleiben Risiken.

## Nachtrag — Readiness JG03 Innovation (14.11.2026)

Der aktuelle Bewerbungsstand wurde nach den Q2-/Portal-/Budget-Korrekturen erneut von zwei unabhängigen Reviewern geprüft.

| Reviewer | Prüfgebiet | Ergebnis |
|---|---|---|
| A | Formalia, Fristen, Teilnahmevoraussetzungen, Portal-Mapping, Q2 | **PASS** |
| B | Projektqualität, Innovation, Technik, Budget, Second Stage | **PASS** |

**Geprüfter Candidate:** `ef968f9652069c0f92051db8f91d0125ed70ec1e` · **Status:** `READY_WITH_EXPLICIT_BLOCKERS` · **Details:** [Readiness-Review](review-application-readiness-2026-11-14.md).

## Nachtrag — Gründungsstrategie/Q2 (docs-only Delta)

Das Gründungs-Delta (Q2-Verifikation, Gründungsstrategie, Jobcenter/BA-Assessment, Zeitplan, Owner-Gate, kanonische Anfrage) wurde **separat** von zwei unabhängigen Reviewern geprüft. Geprüfter Candidate: `d062d9dbf4a05b0e4bac38506a3a0b4deedc191c`; Einzelbefunde: [Review Gründungsstrategie](../decision/review-founder-strategy-2026-11-13.md).

| Reviewer | Verdikt | Ergebnis |
|---|---|---|
| A — Förderrecht | `STRATEGY_CONDITIONALLY_VALID` | **PASS mit Auflagen** |
| B — Sozialrecht/Finanzen | `EXTERNAL_CONFIRMATION_REQUIRED` | **PASS mit Auflagen** |

**Wichtig:** Das Gründungs-Delta ändert keine Finanzzahlen und keine Falschangabe zum Selbstständigkeitsstatus. Q2 bleibt `CONTRADICTED / EXTERNAL_CONFIRMATION_REQUIRED`; die Anfrage ist **nicht versendet**.

## Gemeinsames Fazit

**PASS/PASS** für Candidate `9ed86225`. Die Bewerbung ist inhaltlich, finanziell und formal prüfbar; die verbleibenden Punkte sind Owner-Angaben, Portal-Live-Prüfung und die ausdrücklich offenen Q2/Q3/Q3b-Klärungen. **Keine Einreichung, keine E-Mail, keine Lizenzfestlegung, kein Merge.**
