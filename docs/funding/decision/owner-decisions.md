# Offene Owner-Entscheidungen (Liste)

**Stand:** 13.11.2026 · **Kontext:** Bedingte Empfehlung **F3 (FormBridge im Feldexa-Kontext)** (siehe [comparison-report.md](comparison-report.md)); Frist 30.11.2026, 15:00 CET. Nur der Repository-Eigentümer kann diese Punkte entscheiden/ausführen; der Bericht wurde ohne sie finalisiert, aber die Einreichung hängt an ihnen.

## Entscheidungs-Block A — zwingend vor Einreichung FormBridge

| # | Entscheidung/Aktion | Warum | Deadline-Empfehlung |
|---|---|---|---|
| A1 | **Lizenz verbindlich wählen** (Empfehlung Apache-2.0 liegt in `docs/governance/license-decision.md`) und LICENSE-Datei committen | PTF: FOSS-Pflicht | bis 20.11. |
| A2 | **PTF-Team schriftlich anfragen:** (a) zulässig zwei Anträge einer Person (FormBridge + RepairProbe-Draft) im selben Jahrgang? (b) Eigenanteil-Modell (≥5 %?) bestätigen; (c) Q3: 47.500 vs. 47.381,25 und Second Stage 31.667 vs. 31.570,87; (d) Selbstständigkeit ab Förderbeginn (Q2) | deep-research-Doku markiert diese Punkte OFFEN; Schweizer FAQ nicht übertragbar; Q3-Anfrageentwurf liegt vor | bis 18.11. (Antwortzeit!) |
| A3 | **Held-out-Wohngeld-PDF** (anderes Bundesland) beschaffen + Rechte prüfen (inkl. Klärung `copy:no`-Rechtslage der Fürther Quelle; ggf. Behördenanfrage um Nutzungsgenehmigung) | Review A: HIGH-Risiko Ein-Dokument-Evidenz | bis 24.11. |
| A4 | **Bewerbungstext-Ergänzungen** einarbeiten: RF-Messabsatz, Document-AI-/LLM-Abgrenzung, XSD-Verbraucher-Argument, Adaptierbarkeits-Story (2. Schema-Demo-Pfad) | Review A Vektoren 1/2/6/7 | bis 26.11. |
| A5 | **Feldexa-Fassung (F1/F2/F3) vs. RepairProbe final bestätigen** (dieser Bericht = bedingte Empfehlung F3; ggf. RepairProbe-Portal-Draft bewusst ruhen lassen) | Auftrag: genau ein Antrag; **Owner entscheidet, nicht der Agent** | bis 27.11. |
| A6 | **Portal-Eintragung** (FormBridge-Bausteine übertragen, Fragen des Live-Portals gegen Vorlage prüfen) | Frist 30.11. 15:00 CET — Puffer einplanen | bis 28.11. |

## Entscheidungs-Block B — optional/strategisch

| # | Frage | Optionen | Abwägung |
|---|---|---|---|
| B1 | **Mini-PoC vor Einreichung?** | (a) kleines regelbasiertes Demo-Script auf Referenz-PDF (senkt Trivialitäts-Risiko, schafft aber Vorarbeit, die vom Förderumfang abgezogen werden muss) · (b) kein PoC (volle Förderbreite bleibt; Mitigation über Evidenz-Demo: 170-Fehler-Normalisierung + validierende Instanz als „Wegbuch" im Antrag) | Review A nennt Trivialität als Tötungsrisiko; EVIDENZ-Demo ist bereits vorhanden — Empfehlung des Berichts: zuerst (b) mit sehr explizitem Anhang; (a) nur wenn Owner das Vorarbeit-Risiko geringer gewichtet |
| B2 | **RepairProbe-Pfad** falls FormBridge nicht eingereicht wird | Portal-Draft fertigstellen/einreichen (Review-B-Risiken dann aktiv adressieren: Konkurrenz-, Bedarfs-, Linien-Argumente) | Dieser Bericht triftt keine Aussage für andere Fördertöpfe |
| B3 | **Zweitantrag klären** — falls PTF zwei Anträge erlaubt: beide einreichen? | chancen-neutrale Option; Kapazität (6 Monate Vollzeit) spricht gegen parallele Zusagen | erst nach A2-Antwort |
| B4 | **fim-fields-Index + Fürth-PDF-Archivierung** rechtlich klären (Redistribution) | Lizenzrisiko fürs öffentliche Repo/Förderfall | vor Förderbeginn |

## Zur Erinnerung (aus vorherigen Phasen, weiterhin offen)

- ADR-001/Boundary bleiben verbindlich: **keine FormBridge-Implementierung vor Förderbescheid** (B1-Option (a) wäre eine bewusste, dokumentierte Ausnahme — Vorarbeit-Kennzeichnung zwingend).
- RepairProbe unverändert; kein Merge der Feldexa-PRs #152/#168; Issue #165 unberührt.
