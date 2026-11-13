# Owner-Fragen M1–M9 — Klassifikation und Blockadestatus

**Stand:** 13.11.2026 · **Regel:** Es werden **keine** persönlichen Umstände, Vermögenswerte, Selbstständigkeitsstatus oder früheren Beihilfen angenommen. Jede persönliche Frage bleibt offen, bis der Owner sie belegt. Dieses Dokument ist kein Eligibility-Assessment der Person.

**Legende:** `VERIFIED` (öffentlich belegt, nicht personenbezogen) · `REQUIRES_OWNER_INPUT` (nur der Owner kann antworten) · `REQUIRES_AUTHORITY_CLARIFICATION` (PTF/BMFTR muss antworten) · `NOT_APPLICABLE` · `BLOCKER` (verhindert Einreichung/Förderung, solange nicht erfüllt) · `PLANNING` (Planungsunsicherheit, kein formaler Blocker)

## M1–M9

| ID | Frage | Klassifikation | Blockiert? | Begründung / Quelle | Was der Owner tun muss |
|---|---|---|---|---|---|
| M1 | Mindestalter 18? | REQUIRES_OWNER_INPUT | **BLOCKER** | RL Nr. 3; FAQ Bewerbung 02 | Eigene Bestätigung; kein Nachweis im Repo nötig |
| M2 | Wohnsitz Deutschland + Steuern in DE? | REQUIRES_OWNER_INPUT | **BLOCKER** | FAQ Bewerbung 02 | Eigene Bestätigung; ggf. Melde-/Steuernachweis |
| M3a | Selbstständig oder freiberuflich? | REQUIRES_OWNER_INPUT | **BLOCKER**, falls weder a noch b noch c | FAQ Bewerbung 02 | Status klären |
| M3b | Angestellt + (anteilige) Arbeitgeber-Freistellung für die Laufzeit? | REQUIRES_OWNER_INPUT | **BLOCKER**, falls nicht freigestellt | FAQ Bewerbung 02 FN** | Freistellung schriftlich klären |
| M3c | Selbstständigkeit erst ab Förderbeginn geplant? | REQUIRES_AUTHORITY_CLARIFICATION | **POTENZIELLER BLOCKER** | Nicht explizit geregelt (Q2) | PTF-Anfrage; Gewerbe-/Finanzamt-Timing |
| M4 | Notwendige Programmierkenntnisse vorhanden (KI nur Werkzeug)? | REQUIRES_OWNER_INPUT | **BLOCKER** | FAQ Förderung 08 | Eigene Bestätigung; ggf. Code-/Projektnachweise |
| M5 | „Einschlägige Vorarbeiten + umfassende Kenntnisse" nachweisbar? | REQUIRES_OWNER_INPUT (öffentliche Vorarbeiten belegt; persönliche Kenntnisse nicht) | **BLOCKER**, falls kein Nachweis | RL Nr. 3; öffentliches FormBridge-/Feldexa-Repo = Vorarbeit | Bewerbungstext „Stand/Motivation"; Nachweise zusammenstellen |
| M6 | De-minimis-Historie: < 300.000 € Beihilfen in den letzten **rollierenden** 3 Jahren? | REQUIRES_OWNER_INPUT | **BLOCKER**, falls überschritten | RL Anlage Nr. 1; VO 2023/2831 Art. 3 | Alle Beihilfen der letzten 3 Jahre auflisten; De-minimis-Erklärung |
| M7 | Kapazität ~158 h/Monat im Durchschnitt (Plan 150–165 h/Monat) (950 h/6 M.) real leistbar? | REQUIRES_OWNER_INPUT | **PLANNING** (kein formaler Blocker, aber Realismusrisiko) | FAQ Förderung 01; Handbuch Frage 14 | Kalender-/Kapazitätsplan; ggf. Stunden reduzieren |
| M8 | Kontoauszug mit Saldo >= Eigenanteil (2.493,75 €; 2.500 € deckt alle Lesarten) zur Bewilligung? | REQUIRES_OWNER_INPUT | **BLOCKER bei Bewilligung**, nicht bei Einreichung | RL Nr. 4; FAQ Auswahl 03 | Liquidität prüfen; Kontoauszug zum richtigen Zeitpunkt |
| M9 | Second Stage beantragen? | REQUIRES_OWNER_INPUT | **Kein Blocker** (optional) | Handbuch Frage 16; Detailseite | Strategische Entscheidung; nur jetzt möglich |

## Projektknoten P1–P6 (objektiv, nicht personenbezogen)

| ID | Prüfung | Status | Anmerkung |
|---|---|---|---|
| P1 | Softwareprojekt, nicht nur Doku/Marketing | VERIFIED (Regel) / IMPLEMENTIERUNG OFFEN | FormBridge hat Spec, aber **keinen** Produktcode für die Pipeline; Feldexa hat App-Gerüst + 240 Tests, aber keine verifizierte E2E-Pipeline |
| P2 | Themenfeld Software-Infrastruktur | VERIFIED (Definition) / JURY-INTERPRETATION | FAQ Grundlagen 02 passt auf CLI/Bibliothek/Verifier |
| P3 | Innovativ / „neues Modul für bestehende Software" | VERIFIED (Regel) / JURY-INTERPRETATION | FAQ Bewerbung 05; Prior-Art-Audit liegt vor |
| P4 | Bestehendes Projekt klar abgrenzbar | VERIFIED (Mechanik) / QUALITÄT = JURY | project-boundary.md A/B/C |
| P5 | FOSS-Zusage möglich | VERIFIED (Regel) / OWNER-ENTSCHEIDUNG | Lizenz noch offen |
| P6 | Hoher Entwicklungsanteil + realistische Stunden | VERIFIED (Plan) / JURY-INTERPRETATION | 6-Monats-Plan; 950 h Baseline; 250-h-Heuristik |

## Welche Fragen sind echte Eligibility-Blocker?

**Harte formale Blocker (vor Einreichung zu klären):**

1. **M1** (Alter) — trivial, aber formal.
2. **M2** (Wohnsitz/Steuern DE).
3. **M3a/M3b/M3c** (Selbstständigkeit/Freistellung; M3c ist der einzige unklare Fall).
4. **M4** (Programmierkenntnisse; Vibe-Coding ausgeschlossen).
5. **M5** (Vorarbeiten/Kenntnisse) — Nachweis ist Pflicht, aber die öffentliche Vorarbeit ist vorhanden; die persönliche Darstellung entscheidet.
6. **M6** (De-minimis) — nur Blocker, wenn die 300.000-€-Grenze überschritten ist.

**Formaler Blocker erst bei Bewilligung:**

- **M8** (Kontoauszug/Liquidität). Für die Einreichung nicht nötig, für die Bewilligung schon.

**Keine Eligibility-Blocker, nur Planung:**

- **M7** (Kapazität): beeinflusst Realismus und Stundenumfang, nicht die formale Zulässigkeit.
- **M9** (Second Stage): optional.
- **Q1/Q3/Q3b/Q4/Q5/Q7**: Klärungen, die die Planung verbessern; Q3 ist bei konservativer Planung nicht blockierend.
- **Q6**: gegenstandslos.

## Besonders kritisch: M3c + Q2

Die einzige Kombination, die eine sonst förderfähige Person **hart** ausschließen könnte, ist: derzeit nicht selbstständig/freiberuflich, keine Arbeitgeber-Freistellung, und die Selbstständigkeit soll erst zum Förderbeginn aufgenommen werden. Ob das akzeptiert wird, ist öffentlich **nicht** geregelt. Deshalb ist Q2 die wichtigste Anfrage; sie ist im [Anfrageentwurf](ptf-inquiry-draft.md) enthalten.

## Was der Owner **nicht** beantworten muss

- Keine Offenlegung von Vermögenswerten über den Eigenanteils-Saldo hinaus.
- Keine Offenlegung privater Dokumente, die für die Förderung nicht erforderlich sind.
- Keine Festlegung auf eine Lizenz, bevor der Owner die Lizenzentscheidung treffen will (aber die FOSS-Zusage muss im Antrag stehen).

**Status:** Alle persönlichen Fragen bleiben **offen**. Dieses Dokument ersetzt keine rechtliche Beratung und keine Prüfung durch den Projektträger.
