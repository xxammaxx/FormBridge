# Review A — Adversarial Audit FormBridge (unabhängig)

**Reviewer:** separater Agent-Prozess mit Auftrag „widerlege die Innovations- und Förderargumente von FormBridge"; führte Eigeneigenverifikation durch (XSD-Hash + 170 xmllint-Fehler reproduziert; Repo-Inventar geprüft: 3 Docs-Commits, 0 Code-Dateien).
**Datum:** 13.11.2026 · **Ziel:** Jury-Angriffe vorwegnehmen; keine Annahmen des Autors übernehmen.

## Angriffsvektoren → Urteile → Restrisiko

| # | Vektor | Urteil | Restrisiko |
|---|---|---|---|
| 1 | Prior-Art-Lücken (LLM-Document-AI-Welle: LlamaParse/Reducto; akademisch: FormNet/FUNSD; form.io-Ökosystem) | WEAK — Lücken real, treffen nur die **breite** Claim; AI-Dienste sind proprietäre Cloud-SaaS, FIM-fremd; Frontier-Modelle scheitern laut ExtractBench an großen Schemata (369 Felder → 0 %) | MED |
| 2 | XSD-Defekt als Rabbit-Hole | WEAK — Defekt echt & dauerhaft (immutable URL); aber fimportal.de listet inzwischen einen XDF↔XSD-Konverter → „wer braucht die XSD?" ohne benannten Verbraucher offen | MED (Validitätsrisiko LOW) |
| 3 | CommonForms-Lizenzrisiko | REFUTED — Scope auf born-digitale Textlagen begrenzt; Referenzfall bereits ohne CommonForms bewiesen | LOW |
| 4 | Zero-Code/Docs-only als Red Flag | WEAK — PTF sanktioniert Ideen-Stadium nicht; Risiko ist eher „Produkt-Spin-off-Optik" | MED |
| 5 | Fehlende Realwelt-Validierung | **SUPPORTED** — nur 1 kommunales PDF, kopierbeschränkt (`copy:no`, Rechte ungeklärt), Held-out-Dokument nicht beschafft | **HIGH** (konditional) |
| 6 | Übertragbarkeit (1 Verfahrensfamilie) | WEAK — ehrlicher Scope; aber PTF-Kriterium „Adaptierbarkeit" nur schwach bedient | MED |
| 7 | Trivial-Kombinations-Wahrnehmung | **SUPPORTED** — geförderter Kern IST pdftotext+Regelkatalog+xmllint; ohne Code keine Demo; RF-Messlogik muss in den Antragstext | **HIGH** |

## Gesamteinschätzung des Reviewers

Kernclaims überstehen die Falsifikation (XSD-Defekt echt, enge Prior-Art-Lücke haltbar, Lizenzrisiko entschärft). Am ehesten killen die Anwendung: (1) Trivialitäts-Wahrnehmung ohne Mini-PoC, (2) Ein-Dokument-Evidenzbasis mit ungeklärter `copy:no`-Rechtslage, (3) Nischen-/Spin-off-Optik, (4) Schweigen zur Document-AI-Welle. Netto: **antragsfähig mit 3 harten Pre-Submission-Bedingungen** — sonst Nachteil gegenüber einem physisch demonstrierbaren RepairProbe.

## Umsetzung im Entscheidungsprozess

Die 3 Bedingungen sind in comparison-report.md §6.5 und owner-decisions.md als Pflichtaktionen vor Einreichung übernommen. Matrix-Folge: K1 7,0→6,5, K6 7,0→6,5 (Bedingungen), K3 6,0→6,5 (Angriff 3 REFUTED), K4 7,0→6,5 (Angriff 6).
