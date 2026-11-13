# Verbleibende Fragen an den Prototype Fund — Statusregister

**Stand:** 13.11.2026 · **Prinzip:** Eine nicht gefundene Verbotsregel ist kein Nachweis einer Erlaubnis. Gelistet werden nur Punkte, die öffentlich nicht beantwortbar sind und deren Klärung eine Entscheidung beeinflussen. **Keine Anfrage wurde versendet.**

**Klassifikation:** `REQUIRES_OWNER_INPUT` · `REQUIRES_AUTHORITY_CLARIFICATION` · `VERIFIED` · `NOT_APPLICABLE` · `NONBLOCKING`

## Übersicht

| ID | Frage | Klassifikation | Blockiert die Einreichung? | Wirkung |
|---|---|---|---|---|
| Q1 | Mehrere gleichzeitige Förderungen einer Person | REQUIRES_AUTHORITY_CLARIFICATION | Nein, für **eine** Einreichung; ja, wenn beide Projekte parallel gefördert werden sollen | Strategie |
| Q2 | Selbstständigkeit erst ab Förderbeginn | REQUIRES_AUTHORITY_CLARIFICATION | **Ja, potenziell harte Hürde** | Formale Antragsberechtigung |
| Q3 | 47.500 € vs. 47.381,25 € (GK-/95-%-Logik) | **UNRESOLVED / REQUIRES_AUTHORITY_CLARIFICATION** | Nein, bei konservativer Planung; ja nur für Maximalausschöpfung | 118,75 € |
| Q3b | Second Stage 31.667 € vs. 31.570,87 € | **UNRESOLVED / REQUIRES_AUTHORITY_CLARIFICATION** | Nein, bei konservativer Planung | 96,13 € |
| Q4 | Erwarteter Nachweisgrad „Vorarbeiten/Kenntnisse" | REQUIRES_AUTHORITY_CLARIFICATION | Nein (weiche Bewertung) | Bewerbungstext |
| Q5 | Lizenzzeitpunkt im formalen Antrag | REQUIRES_AUTHORITY_CLARIFICATION | Nein; Owner-Lizenzentscheidung separat | Formalie |
| Q6 | Unbenutzter RepairProbe-Portal-Draft | NOT_APPLICABLE / Beobachtung | Nein | Plattformmechanik |
| Q7 | 10-Monats-Option in der Innovationslinie | REQUIRES_AUTHORITY_CLARIFICATION | Nein, nur falls 10 Monate beantragt werden | Laufzeit/Finanzierung |

## Q1 — Mehrere gleichzeitige Förderungen einer Person (F2.4)

- **Bekannt:** Mehrere Bewerbungen gleichzeitig sind ausdrücklich zulässig (FAQ Bewerbung 06: „Ja."). Ein RepairProbe-Draft liegt faktisch parallel.
- **Fehlt:** Ob **zwei gleichzeitige Förderzusagen** (zwei geförderte Projekte desselben Antragstellers im selben Zeitraum) möglich sind und ob Stundenkapazität/Haftung begrenzen.
- **Relevanz:** Bestimmt, ob Feldexa/FormBridge und RepairProbe theoretisch parallel laufen könnten.
- **Verbindlich nötig?** Nein für **eine** Einreichung; ja, wenn beide aktiv gehalten werden.
- **Abhängige Entscheidung:** Owner-Strategie A5/B3 (`owner-decisions.md`).

## Q2 — Selbstständigkeit: Bewerbung, formaler Antrag, Förderbeginn (CONTRADICTED)

- **Bekannt:** Bewerbung setzt „selbstständig oder freiberuflich“ voraus; Angestellte mit (anteiliger) Freistellung sind ausdrücklich zulässig (FAQ Bewerbung 02 FN**). **JG03-Handbuch/FAQ:** Bewerbung „als Privatperson“; keine Solo-Steuernummer in der Bewilligungs-Checkliste; formaler Antrag bis **Ende Februar 2027**. **JG02-Wiki** (03.03.2026) verlangt dagegen Steuernummer/Anmeldung zum formalen Antrag. Historische Seiten (2020/2022): „spätestens bei Projektbeginn“. **Widerspruch.**
- **Fehlt:** Ob die Selbstständigkeit bereits zur **Jury-Bewerbung** (Nov 2026) bestehen muss, ob sie bis zum **formalen Antrag** (Frühjahr 2027) genügt oder ob eine Aufnahme **erst zum Förderbeginn** (01.06.2027) akzeptiert wird — und welcher Nachweis zu welchem Zeitpunkt.
- **Tendenz (keine Rechtsaussage):** Der aktuelle Wiki-Eintrag spricht für eine Registrierung **vor dem formalen Antrag**; „erst zum Förderbeginn“ ist **nicht sicher** tragfähig.
- **Relevanz:** Entscheidend, falls der Owner derzeit nicht selbstständig/freiberuflich ist und keine Freistellung hat.
- **Verbindlich nötig?** **Ja — potenziell harte formale Hürde.**
- **Vollständige Analyse:** [q2-employment-status.md](q2-employment-status.md).
- **Abhängige Entscheidung:** A2 (PTF-Query) und Gewerbe-/Finanzamt-Timing; Owner-Checkliste M3c.

## Q3 — Berechnungslogik 47.500 € vs. 47.381,25 € (UNRESOLVED)

- **Bekannt:** FAQ Förderung 01 nennt 47.500 € „950 h × 50 €"; RL Nr. 5 sagt 95 % der Personal- und Gemeinkosten, Gesamtkosten <= 50.000 €; FAQ Förderung 02 sagt GK-Pauschale 5 % **der Personalkosten** und Eigenanteil >= 5 %.
- **Fehlt:** Die exakte Kombination. Bei 950 h + 5 % GK auf PK ist die strenge Förderung **47.381,25 €** (G = 49.875 €). Die 47.500 € erfordern G = 50.000 € — z. B. durch 1.000 Gesamtstunden ohne GK, GK = 5 % des Gesamtbudgets (2.500 €) oder einen nachgewiesenen Satz ab 50,125313 €/h. Keine dieser Varianten ist offiziell als die gemeinte bestätigt.
- **Differenz:** **118,75 €** (5 % der GK-Pauschale).
- **Relevanz:** Bestimmt die maximale Antragshöhe; die Stundenplanung (950 h) ist in beiden Lesarten zulässig.
- **Verbindlich nötig?** Nein für die Einreichung (konservativ 47.381,25 € planen); ja für Maximalausschöpfung.
- **Vollständige Analyse + Anfrageentwurf:** [q3-clarification.md](q3-clarification.md).

## Q3b — Second Stage 31.667 € vs. 31.570,87 € (UNRESOLVED)

- **Bekannt:** FAQ nennt 31.667 € und „gerundet 633 h × 50 €"; RL Nr. 5 begrenzt die zweite Phase auf 33.337 € Gesamtkosten; 95 % davon sind 31.670,15 €.
- **Fehlt:** Wie das Portal 31.667 € berechnet. 633 h × 50 € = 31.650 € sind **Personalkosten**, nicht Förderung; mit 5 % GK sind es 31.570,87 €. 634 h ergeben 31.620,75 €.
- **Differenz:** 96,13 € (633 h) bzw. 46,25 € (634 h).
- **Verbindlich nötig?** Nein, bei konservativer Planung; ja für Maximalausschöpfung.
- **Abhängige Entscheidung:** Second Stage beantragen (M9) und Budgetplanung.

## Q4 — „Vorarbeiten und umfassende Kenntnisse" — Erwarteter Nachweisgrad (F7)

- **Bekannt:** RL Nr. 3 verlangt „einschlägige Vorarbeiten und umfassende Kenntnisse im Bereich der Softwareentwicklung"; Nachwuchs mit geringen Erfahrungen ist ausdrücklich zulässig; PTF betont Ideas-Stage-Freundlichkeit.
- **Fehlt:** Konkrete Erwartung (GitHub-Historie? Berufserfahrung? reicht das öffentliche Forschungs-Repo?).
- **Relevanz:** Bewerbungsfelder „Stand des Projekts" und „Motivation/Wild Card".
- **Verbindlich nötig?** Nein — Risikominimierung; Antwort formt die Selbstbeschreibung.

## Q5 — Lizenz-Zeitpunkt formal (F5)

- **Bekannt:** FOSS-Zusage bei Bewerbung; Veröffentlichung „zum Projektabschluss"; keine Regel verlangt eine Lizenzdatei zur Bewerbung.
- **Fehlt:** Ob im **formalen Antrag** (nach Jury-Auswahl) eine konkrete Lizenz benannt sein muss.
- **Relevanz:** Bestimmt, wie spät die Owner-Lizenzentscheidung fallen kann (Apache-2.0-Empfehlung liegt vor).
- **Verbindlich nötig?** Nein; Empfehlung: Lizenz vor Einreichung fixieren, kostet nichts.

## Q6 — RepairProbe-Portal-Draft in Ruhe lassen

- **Bekannt:** Der Draft bleibt unangetastet; keine Einreichung.
- **Fehlt:** Ob ein ungenutzter Entwurf im Portal bei einer anderen Einreichung stört (Plattformmechanik).
- **Verbindlich nötig?** Nein; Beobachtungspunkt.

## Q7 — 10-Monats-Option in der Innovationslinie

- **Bekannt:** RL Nr. 4 erlaubt 10 Monate (6 + 4) bei besonders verwertungsstarken Projekten; FAQ Grundlagen 01 nennt 79.167 €/158.000 €; Detailseite verlangt die Angabe „sechs- oder zehnmonatig".
- **Fehlt:** Ob die Innovationslinie im Jahrgang 03 die 10-Monats-Option tatsächlich öffnet (die Innovationsseite nennt nur 6 Monate) und ob die zweite Phase separat beantragt/ausgewählt wird.
- **Relevanz:** Nur falls der Owner 10 Monate anstrebt; für die 6-Monats-Baseline irrelevant.
- **Verbindlich nötig?** Nein für die 6-Monats-Einreichung; ja für die 10-Monats-Planung.

**Fazit:** Q2 ist die einzige potenziell **harte** formale Hürde. Q1/Q3/Q3b/Q4/Q5/Q7 sind Klärungen, die die Planung verbessern, aber eine Einreichung mit konservativer Planung nicht blockieren. Q6 ist gegenstandslos. **Keine Anfrage wurde versendet.**
