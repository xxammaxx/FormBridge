# Quellen- und Evidenzverzeichnis — Förderentscheid FormBridge vs. RepairProbe

**Stand:** 13.11.2026 · Alle Quellen am 13.11.2026 abgerufen/geprüft. Einstufung je Quelle: VERIFIED / INTERPRETATION / UNKNOWN.

## A. Offizielle Prototype-Fund-Quellen (Förderlinie Innovation)

| # | Quelle | Abruf | Kerninhalt | Status |
|---|---|---|---|---|
| S1 | https://bewerben.prototypefund.de/ | 13.11.2026 | Frist 30.11.2026; Linien Innovation/Resilienz/Up and Coming | VERIFIED |
| S2 | https://www.prototypefund.de/innovation | 13.11.2026 | Linienprofil Datensicherheit + Software-Infrastruktur; Antragsberechtigung (18+, Wohnsitz DE solo, Team ≤4 GbR); FOSS-Pflicht; 47.500 €/95.000 € | VERIFIED |
| S3 | https://www.prototypefund.de/bewerbung/details | 13.11.2026 | Förderperiode 01.06.–30.11.2027; Second Stage 01.12.2027–31.03.2028; 31.667 €/63.333 €; Zeitplan; Sprechstunden 16./19.11.2026; „hoher Entwicklungsanteil", „nur Doku/Release/Marketing nicht förderfähig" | VERIFIED |
| S4 | https://www.prototypefund.de/innovativ | 13.11.2026 | Innovationsbegriff inkl. „neues Modul für bestehende Software"; Kriterien Datensparsamkeit/Anwendungsfreundlichkeit/Adaptierbarkeit/Open Source | VERIFIED |
| S5 | PTF-Handbuch Jahrgang 03: https://www.prototypefund.de/uploads/Publikationen_und_Onepager/PTF_Handbuch_2026.pdf (31 S., lokal extrahiert) | 13.11.2026 | Bestandsprojekte zulässig bei klarer Abgrenzung; „Verbesserung der bestehenden Software nicht ausreichend"; Max. Förderung 47.500 €/Person (Handbuch S.~870 des Textextrakts) | VERIFIED |
| S6 | Eigenanteil ≥ 5 % des Gesamtaufwands (47.500 € + 2.500 €) | Feldexa_2.0-Doku (`docs/funding/deep-research-2026-11-13.md`, Branch `docs/prototype-fund-2027-feldexa-concept`) | im Handbuch-Textextrakt nicht direkt gefunden | **INTERPRETATION** — im Bewerbungsportal prüfen |

## B. FormBridge (Kandidat 1)

| # | Quelle | Status |
|---|---|---|
| S7 | https://github.com/xxammaxx/FormBridge — public; Head `5ad209a…` → Branch `docs/funding-decision-2026-11-13` | VERIFIED (gh repo view + frischer Clone, V8-Verfahren) |
| S8 | `docs/research/prior-art-audit.md` + Appendix: 13 Projekte mit Clone-SHAs (u. a. KIWO `c40bb34`, Formularagent `4085c46`) | VERIFIED (Reviews 13.11.2026, V1/V2) |
| S9 | `docs/research/reference-case-wohngeld.md`: Fürth-PDF SHA-256 `57f4f3f9…`; FIM-XSD SHA-256 `36250e69…`; 170 Parser-Fehler; Normalisierung+Instanz-Validierung reproduziert | VERIFIED (V3, unabhängige Reproduktion) |
| S10 | `docs/funding/application-draft-de.md` (Bewerbungsbausteine) — **noch nicht ins PTF-Portal übertragen** | VERIFIED (Datei) / Portal-Status: UNKNOWN |
| S11 | Lizenz: **OWNER_DECISION_REQUIRED**, keine LICENSE committet | VERIFIED |
| S12 | Implementierungsstand: kein Code (21 Dateien, nur Docs/Evidenz) | VERIFIED (V6/V8) |

## C. RepairProbe (Kandidat 2)

| # | Quelle | Status |
|---|---|---|
| S13 | GitHub-Org https://github.com/RepairProbe — Repos: `repair-probe` (**PRIVATE**, Apache-2.0, Python ~63 KB, erstellt 2026-08-28, letzter Push 2026-10-30, 5 Testdateien); `RepairProbe.github.io` (PUBLIC, Apache-2.0); `.github` (PUBLIC) | VERIFIED (gh API, 13.11.2026) |
| S14 | Öffentliches Org-README (raw.githubusercontent.com/RepairProbe/.github/main/profile/README.md): Zielgruppe Repair-Cafés/Werkstätten; „kleine Python-Baseline" vorhanden; „Reparaturerfolg, Bildverständnis und KI-Qualität … nicht nachgewiesen"; Prototyp geplant, **noch nicht öffentlich**; PTF-Antrag „in Vorbereitung und noch nicht eingereicht"; Repair-Café-Rückmeldung **explorativ n=1** | VERIFIED (öffentliches Artefakt, eigene Aussage des Projekts) |
| S15 | Öffentliche Website https://repairprobe.github.io/ (index/evidenzmodell/roadmap/technical-baseline) | VERIFIED (Abruf 13.11.2026) |
| S16 | 850-Stunden-Bewerbungsentwurf als **Draft im deutschen PTF-Portal** (nicht eingereicht) | INTERPRETATION — übernommen aus `docs/funding/research-formbridge-verwaltungsentlastung-2026-11-13.md` §8 („Stand letzter verifizierter Nachweis"); **Portal ist owner-only, Text dieser Prüfung nicht zugänglich** |
| S17 | „offenes Reparaturevidenz- und Sicherheitsmodell", Apache-2.0-Lizenz | VERIFIED (S14/S13); fachlicher Gehalt des Modells: **UNKNOWN** (nicht öffentlich detailliert) |
| S18 | Prior-Art-/Konkurrenz-Audit für RepairProbe | **UNKNOWN** — kein solches Dokument in verfügbaren Quellen gefunden |

## D. Vertraulichkeit

Das Haupt-Repository `RepairProbe/repair-probe` ist **privat**; sein Inhalt wird in diesem Bericht nur in dem Umfang referenziert, der aus öffentlichen Quellen (S13–S15) oder strukturmetrisch (S13) belegbar ist. Der PTF-Portal-Entwurf (S16) ist owner-only und wurde **nicht** eingesehen; es wurden keine Antragsinhalte zitiert. Öffentlicher Berichtsort: FormBridge-Repo (Branch) — enthält nur öffentlich verifizierbare Informationen.

## E. Nicht einsehbare Punkte (ehrliche Lücken)

1. Volltext/Qualität des RepairProbe-Antrags (Portal-Draft) — UNKNOWN.
2. Persönliche Antragsberechtigung, Kapazität, Mehrfachbewerbungs-Regelung (zwei Anträge einer Person im deutschen PTF) — laut S6-Quelle „OFFEN"; nicht recherchierbar ohne Anfrage ans PTF-Team.
3. Tatsächliche Jury-Gewichtung — die hier verwendeten Gewichte sind ein strukturiertes Entscheidungsinstrument, **keine** Förderwahrscheinlichkeitsaussage.
