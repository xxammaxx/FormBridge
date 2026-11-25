# FormBridge

**Verifizierbare Zuordnung statischer Behörden-PDFs zu versionierten FIM-Datenfeld-Identifikatoren.**

FormBridge ist ein unabhängiges, anwendungsübergreifendes Open-Source-**Forschungs- und Infrastrukturprojekt** (Forschungsstufe). Es verbindet sichtbare Felder in alten, nicht ausfüllbaren Verwaltungs-PDFs mit den versionierten Datenfeld-Identifikatoren des föderalen Informationsmanagements (FIM) — mit nachprüfbarer Unsicherheit (Konfidenz + explizites UNKNOWN), menschlicher Freigabe, maschinenlesbarer Provenienz und validierter strukturierter Ausgabe, lokal und ohne Cloud-Dienst.

> **Status: RESEARCH_STAGE — keine Implementierung.** Dieses Repository enthält aktuell **Ausschließlich** Forschungsdokumentation, Evidenz und Spezifikation. Es existiert **kein** produktiver oder prototypischer Quellcode; jede Formulierung über künftige Fähigkeiten ist ein Forschungsziel, keine zugesagte Funktion.

## Repository-Stand

`main` ist der **einheitliche, maßgebliche Stand** dieses Repositories: Forschungsdokumentation, Evidenz, technische Spezifikation und das vollständige Prototype-Fund-Bewerbungspaket (`docs/funding/application/**`) liegen gemeinsam hier. Der Merge von `docs/funding-decision-2026-11-13` nach `main` (25.11.2026) hat den früheren Baseline-Zustand abgelöst; Commit `5ad209a` bleibt als **historischer Ausgangsstand vom 13.11.2026** dokumentiert. Die Website (`gh-pages`) verweist damit auf aktuelle Dokumente.

## Warum?

Viele amtliche Vordrucke existieren nur als statisches PDF. FIM standardisiert die Verwaltungsdaten dahinter — aber kein geprüftes freies Projekt verbindet beides nachprüfbar. In unserer [Quellcodeprüfung vom 13.11.2026](docs/research/prior-art-audit.md) (13 Projekte, u. a. Formularagent, OpenForm/KIWO, CommonForms, FITKO-Ökosystem) wurde die Brücke nicht gefunden; das offizielle Referenz-XSD (Wohngeld S00000159 v1.4) ist zudem nachweislich nicht standardkonform kompilierbar (170 Parser-Fehler — [Referenzfall](docs/research/reference-case-wohngeld.md)).

## Dokumentation

| Bereich | Datei |
|---|---|
| Architekturentscheidung (Unabhängigkeit) | [`docs/architecture/ADR-001.md`](docs/architecture/ADR-001.md) |
| Prior-Art-Quellcode-Audit (13 Projekte) | [`docs/research/prior-art-audit.md`](docs/research/prior-art-audit.md) |
| Innovationsbewertung (Falsifikation) | [`docs/research/innovation-assessment.md`](docs/research/innovation-assessment.md) |
| Technische Forschungsspezifikation | [`docs/research/technical-specification.md`](docs/research/technical-specification.md) |
| Referenzfall Fürth ↔ FIM S00000159 v1.4 | [`docs/research/reference-case-wohngeld.md`](docs/research/reference-case-wohngeld.md) |
| Raw-Audits (Anhang) | [`docs/research/appendix/`](docs/research/appendix/) |
| Evidenz (Datensatz, Feldindex, Instanz) | [`docs/research/evidence/`](docs/research/evidence/) |
| Prototype-Fund-Machbarkeit | [`docs/funding/prototype-fund-feasibility.md`](docs/funding/prototype-fund-feasibility.md) |
| Aktueller Bewerbungsentwurf (DE) | [`application-final-de.md`](docs/funding/application/application-final-de.md) · [historischer Entwurf](docs/funding/application-draft-de.md) |
| [Lokaler LLM-/LoRA-Nachweis und Homelab-Vorarbeit](docs/funding/application/local-llm-evidence-strategy-2026-11-20.md) | Geplante parallele Forschung, keine Ausführung |
| Optionaler RF1-LoRA-Vergleich (19.11.2026) | [`lora-research-extension-2026-11-19.md`](docs/funding/application/lora-research-extension-2026-11-19.md) — geplant, nicht ausgeführt |
| Projektgrenze (Bestand vs. Fördergegenstand) | [`docs/funding/project-boundary.md`](docs/funding/project-boundary.md) |
| Entscheidungsbericht (CONDITIONAL_GO F3) | [`docs/funding/decision-report.md`](docs/funding/decision-report.md) |
| Lizenz-Empfehlung | [`docs/governance/license-decision.md`](docs/governance/license-decision.md) |
| Förderentscheid vs. RepairProbe | [`docs/funding/decision/comparison-report.md`](docs/funding/decision/comparison-report.md) (+ [Scoring-Matrix](docs/funding/decision/scoring-matrix.md), [Reviews A/B (alt)](docs/funding/decision/review-A-formbridge.md), [Quellen](docs/funding/decision/sources-evidence.md), [Owner-Entscheidungen](docs/funding/decision/owner-decisions.md)) |
| Verifizierte Förderregeln & Finanzmodell (13.11.2026) | [`funding-rules-verified-2026.md`](docs/funding/decision/funding-rules-verified-2026.md) · [`financial-model.md`](docs/funding/decision/financial-model.md) · [`eligibility-decision-tree.md`](docs/funding/decision/eligibility-decision-tree.md) · [`remaining-questions.md`](docs/funding/decision/remaining-questions.md) · [`source-register-2026-11-13.md`](docs/funding/decision/source-register-2026-11-13.md) · [`q3-clarification.md`](docs/funding/decision/q3-clarification.md) |
| Reproduzierbare Finanztests | [`validation/RUNBOOK.md`](docs/funding/decision/validation/RUNBOOK.md) · [`validation/test-output.txt`](docs/funding/decision/validation/test-output.txt) · [`validation/scenario-report.md`](docs/funding/decision/validation/scenario-report.md) |
| Validierungsberichte | [`docs/validation/`](docs/validation/) · [`validation-report.md`](docs/funding/decision/validation-report.md) · [`final-validation-report.md`](docs/funding/decision/final-validation-report.md) · [Review A (Finanzen)](docs/funding/decision/review-A-financial-2026-11-13.md) · [Review B (Förderrecht)](docs/funding/decision/review-B-funding-2026-11-13.md) |

## Bezug zu Feldexa 2.0

FormBridge ist **unabhängig** von [Feldexa 2.0](https://github.com/xxammaxx/Feldexa_2.0) (kein Code-Austausch, keine Abhängigkeit). Feldexa 2.0 ist als **vorgesehene erste Anwendung** des künftigen Moduls vorgesehen, aber **nicht integriert** und **nicht Teil des Förderumfangs** (siehe ADR-001). Die ursprüngliche Forschung entstand im Feldexa-2.0-Repository (Issue [#167](https://github.com/xxammaxx/Feldexa_2.0/issues/167), Draft-PR [#168](https://github.com/xxammaxx/Feldexa_2.0/pull/168), Commit `cb122fe2f96a8f5cbde2f075e0b6529342caf676`, 13.11.2026) und wurde hierher migriert — Herkunft ist je Datei ausgewiesen.

## Lizenz

**Apache-2.0** — Der Repository-Inhalt ist unter der Apache License 2.0 lizenziert (SPDX: `Apache-2.0`); der vollständige Lizenztext liegt als [`LICENSE`](LICENSE) im Wurzelverzeichnis. Die Entscheidung des Eigentümers, die Begründung gegen MIT/MPL-2.0 und die Abgrenzung zu Drittmaterial stehen in [`docs/governance/license-decision.md`](docs/governance/license-decision.md). Copyright 2026 xxammaxx. Amtliche Quellen (PDF, XSD) und daraus abgeleitete FIM-Metadaten sind **nicht** Teil der Lizenzierung (siehe Drittmaterial unten).

## Drittmaterial

Amtliche Quellen (Fürther Wohngeld-PDF, FIM-XSD) werden **nicht** redistribuiert; es gelten URL + SHA-256 + reproduzierbare Befehle (siehe [Referenzfall](docs/research/reference-case-wohngeld.md) und [`docs/research/evidence/EVIDENCE.md`](docs/research/evidence/EVIDENCE.md)).
