# Scoring-Matrix & Sensitivitätsanalyse — FormBridge vs. RepairProbe

**Datum:** 13.11.2026 · **Verfahren:** Erstbewertung aus verifizierten Quellen (vor den adversarial Reviews), danach **symmetrische** Nachjustierung mit Einzeldokumentation jeder Änderung. Punkte 0–10. Arithmetik programmatisch berechnet (Skript in der Recherche-Umgebung; Nachrechnung unten angegeben). Die Zahlen sind ein Entscheidungsinstrument, **keine** Förderwahrscheinlichkeiten.

## Gewichte (vorgegeben)

| Kriterium | Gewicht |
|---|---|
| K1 Innovationshöhe und Abgrenzbarkeit | 25 % |
| K2 Gesellschaftlicher Nutzen | 20 % |
| K3 Technische Machbarkeit | 20 % |
| K4 Open-Source-Wiederverwendbarkeit | 15 % |
| K5 Förderfähigkeit und rechtliche Risiken | 15 % |
| K6 Qualität der Bewerbung und Evidenz | 5 % |

## Erstbewertung (vor adversarial Reviews)

| Kriterium | FB | RP | Begründung FB (Quellen) | Begründung RP (Quellen) |
|---|---|---|---|---|
| K1 | 7,0 | 4,5 | Korpus-falsifizierte Lücke (13-Repos-Quellcode-Audit, SHAs); XSD-Defekt 170 Fehler unabhängig reproduziert (reference-case §3) | Kein Prior-Art-Audit auffindbar (sources S18); „KI-Qualität nicht nachgewiesen" (eigenes Org-README S14) |
| K2 | 6,5 | 7,0 | D21 eGov-Monitor 2026 (50 % offline / 24 % Medienbruch); Nutzen indirekt, ohne Nutzertests | Konkrete Gruppe Repair-Cafés; Nachhaltigkeitsnarrativ; Evidenz nur n=1 (S14) |
| K3 | 6,0 | 7,0 | Kein Code; Detektions-Lizenzrisiko (CommonForms ohne LICENSE) | Öffentlich dokumentierte Python-Baseline (24–44 Tests, Quellen widersprüchlich; privat nicht verifizierbar); KI/Bildverständnis unbewiesen (S14) |
| K4 | 7,0 | 6,0 | Infrastruktur-Design (CLI/Bibliothek/Verifier, ADR-001); öffentliches Repo; Lizenz offen | Apache-2.0 fixiert; Hauptcode privat (S13) |
| K5 | 8,0 | 6,0 | Lehrbuch-Linien-Passung („Software-Infrastruktur", „neues Modul", S4); Grenze A/B/C sauber; Risiko nur Lizenz-Offenheit | Endnutzer-Werkzeug → Linien-Passung argumentabel; privater Code muss erst FOSS werden |
| K6 | 7,0 | 6,0 | Vollständiger Entwurf + Evidenzkette im Repo; nicht im Portal | Portal-Draft vorhanden (S16, Draft); Qualität nicht einsehbar; öffentliche Testzahl widersprüchlich (24 vs. 44) |
| **Σ** | **6,85** | **6,025** | | |

## Nachjustierung nach den adversarial Reviews (symmetrisch, jede Änderung belegt)

| Kriterium | FB alt→neu | Anlass (Review A) | RP alt→neu | Anlass (Review B) |
|---|---|---|---|---|
| K1 | 7,0→**6,5** | Trivialitäts-Wahrnehmung SUPPORTED/HIGH („pdftotext+Regeln+xmllint", kein Code als Demo) | 4,5→**4,0** | Konkurrenz SUPPORTED/HIGH: RepairVision mit identischem USP („provisional labels"; https://dev.to/priyansh_narang_c1b96ab75/repairvision-an-intelligent-repair-cafe-platform-for-multimodal-fault-diagnosis-and-sustainable-4jm2); iFixit FixBot; NORA; AugRep/GYVA Live-Pilot |
| K2 | — | — | 7,0→**6,0** | Bedarfs-Evidenz SUPPORTED/HIGH: n=1 widerspricht Schmerzpunkt; keine Pilotpartner |
| K3 | 6,0→**6,5** | Lizenz-Angriff REFUTED (Born-digital-Scope; Referenzfall bewiesen ohne CommonForms) | 7,0→**6,5** | Machbarkeits-Angriff WEAK (Baseline), aber KI-Qualität/Quellenrechte-M4 unbelegt |
| K4 | 7,0→**6,5** | Adaptierbarkeit nur schwach bedient (MED) | 6,0→**5,5** | FOSS-Kriterium formal LOW, aber Glaubwürdigkeit MED (privates Repo) |
| K5 | — | — | 6,0→**5,5** | Linien-Passung angegriffen (Reparatur-App ≠ Datensicherheit/Infrastruktur) |
| K6 | 7,0→**6,5** | Entwurf braucht RF-Mess-/Abgrenzungs-Ergänzungen (3 Bedingungen) | — | — |

## Ergebnis-Matrix (nach Reviews)

| Kriterium | Gew. | FB | RP |
|---|---|---|---|
| K1 | 25 % | 6,5 | 4,0 |
| K2 | 20 % | 6,5 | 6,0 |
| K3 | 20 % | 6,5 | 6,5 |
| K4 | 15 % | 6,5 | 5,5 |
| K5 | 15 % | 8,0 | 5,5 |
| K6 | 5 % | 6,5 | 6,0 |
| **Weighted Total** | 100 % | **6,725** | **5,45** |

## Sensitivitätsanalyse

| Szenario | K1 | K2 | K3 | K4 | K5 | K6 | FB | RP | Rangfolge |
|---|---|---|---|---|---|---|---|---|---|
| Basis | 25 | 20 | 20 | 15 | 15 | 5 | **6,725** | 5,45 | FB |
| S1 Innovation betont | 40 | 16 | 16 | 12 | 12 | 4 | **6,68** | 5,16 | FB (Abstand ↑) |
| S2 Nutzen betont | 20 | 35 | 16 | 12 | 12 | 5 | **6,68** | 5,56 | FB (Abstand ↓) |
| S3 Technisches Risiko betont | 20 | 17 | 35 | 10 | 13 | 5 | **6,695** | 5,66 | FB (minimaler Abstand) |
| S4 Streng: unbelegte Aussagen bestraft | 25 | 20 | 20 | 15 | 15 | 5 | **6,725** | 5,325* | FB (Abstand ↑↑) |

\* S4: Score-Anpassung statt Gewichtsverschiebung — RP K1 4,0→3,5 (Novelty-Behauptungen durch Konkurrenz impliziert); FB unverändert, weil seine Kernbehauptungen korpus-falsifiziert/quellenbelegt sind.

**Nachrechnung (Basis):** FB = 0,25·6,5 + 0,20·6,5 + 0,20·6,5 + 0,15·6,5 + 0,15·8,0 + 0,05·6,5 = 1,625 + 1,30 + 1,30 + 0,975 + 1,20 + 0,325 = **6,725** · RP = 0,25·4,0 + 0,20·6,0 + 0,20·6,5 + 0,15·5,5 + 0,15·5,5 + 0,05·6,0 = 1,00 + 1,20 + 1,30 + 0,825 + 0,825 + 0,30 = **5,45**.

## Interpretationsgrenzen

1. Gewichte und Punkte sind ein strukturiertes Instrument des Auftraggebers-Vorgehens, nicht Kalibrierungen gegen echte Jury-Urteile.
2. RepairProbe-Antragsqualität (K6) ist wegen Portal-Zugriffsbeschränkung nur begrenzt beurteilbar — ein exzellenter Portal-Text könnte K6/RP heben (Enthaltung: +0,5…1,0 Punktmöglichkeitsraum, wäre aber noch nicht einmal in S2/S3 ausreichend zur Umkehr).
3. Die Stabilität der Rangfolge über alle vier Szenarien ist das eigentliche Ergebnis; Punktabstände sind nicht als Präzision zu lesen.
4. **Aktualisierung 13.11.2026:** Die frühere RepairProbe-Baseline „44 Tests" ist öffentlich nicht eindeutig; `llms.txt` nennt 24, `technical-baseline.html` nennt 44 (gleicher Commit). Die Matrix bewertet daher „24–44, nicht unabhängig verifiziert". Das ist eine Evidenz-, keine Qualitätsaussage.
5. **Die Matrix ist kein Entscheidungsautomat.** Die bedingte Empfehlung im [Vergleichsbericht](comparison-report.md) beruht auf der qualitativen Zehn-Kriterien-Analyse, nicht auf dem gewichteten Total. Der Owner entscheidet.
