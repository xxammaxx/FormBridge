# Entscheidungsbaum: Persönliche Förderfähigkeit + Projektpassung (FormBridge, Jahrgang 03)

**Datum:** 13.11.2026 · Nutze diesen Baum vor der Einreichung. Jeder Knoten nennt die Prüf-Quelle. Keine Annahme über die Person des Owners — alle *persönlichen* Knoten enden in Owner-Prüfungen.

## Phase 1 — Projektknoten (FormBridge, objektiv)

```
P1 Ist es ein Software-Projekt (nicht nur Doku/Marketing)?
   → JA: Spec/6-Monatsplan = 100 % Entwicklung + Evaluierung. [Handbuch; FAQ Förderung-ähnlich: „hoher Entwicklungsanteil", details-Seite]
   ↓ JA
P2 Themenfeld „Software-Infrastruktur"?
   → JA: FAQ Grundlagen 02 („Codebibliotheken … für Entwickler*innen, nicht Endanwender*innen") trifft FormBridge (CLI/Bibliothek/Verifier). [RULE_CONFIRMED; Jury-Urteil bleibt PROJECT_FIT_INTERPRETATION]
   ↓ JA
P3 Innovativ? „Neues Modul für bestehende Software" gilt ausdrücklich.
   → JA-Argumentation vorhanden (innovation-assessment, prior-art-audit). [FAQ Bewerbung 05, /innovativ]
   ↓ JA
P4 Bestehendes Projekt klar abgrenzbar?
   → JA: project-boundary.md (A/B/C-Struktur + Verbotensliste). [FAQ Bewerbung 05, Handbuch]
   ↓ JA
P5 FOSS-Zusage im Antrag möglich? (Lizenz muss NICHT zur Bewerbung feststehen; Veröffentlichung zum Projektabschluss)
   → JA, sobald Owner die Lizenz wählt (Empfehlung Apache-2.0 vorbereitet). [FAQ Förderung 06/07; /innovation]
   ↓ JA (nach Owner-Entscheidung A1)
P6 Hoher Entwicklungsanteil + realistische Stundenplanung?
   → 6-Monatsplan mit messbaren Abnahmekriterien; Stunden im angemessenen Verhältnis (Handbuch Frage 14: 250–950 h; Jury bewertet Realismus).
   ↓ JA (Empfehlung: 700–950 h; Förderhöhe streng gerechnet siehe financial-model.md v4, Szenarien D/B)
→ PROJEKTSEITIG: Alle öffentlich prüfbaren Voraussetzungen erfüllt bzw. vorbereitet.
```

## Phase 2 — Persönliche Knoten (Owner prüft; STATUS je nachweisabhängig)

```
M1 Alter ≥ 18?                                        [RL Ä2 Nr. 3; FAQ Bewerbung 02]  → JA/NEIN
M2 Wohnsitz Deutschland + Steuerzahlung in DE?        [FAQ Bewerbung 02]               → JA/NEIN
M3 (a) Selbstständig oder freiberuflich?
    (b) ODER angestellt + (anteilige) Arbeitgeber-Freistellung für die Laufzeit?
    (c) ODER geplante Selbstständigkeit ab Förderbeginn? → NICHT explizit geregelt = UNKNOWN,
        vor Einreichung im Portal/Sprechstunde klären.  [FAQ Bewerbung 02 FN**]
M4 Programmierkenntnisse vorhanden (KI nur als Werkzeug, kein „Vibe-Coding")?
   → JA/NEIN [FAQ Förderung 08]
M5 „Einschlägige Vorarbeiten + umfassende Kenntnisse" nachweisbar?
   → FormBridge-Repo + Feldexa-Arbeit + eigene Entwicklungsbiografie als Nachweismaterial.
   [RL 2024 Nr. 3 (seit 2024); von Ä2 2026 neu gefasst + Nachwuchs-Satz ergänzt]  → JA mit Material / prüfen
M6 De-minimis-Historie: < 300.000 € Beihilfen in den letzten 3 Jahren (alle „eine Unternehmereinheit" bildenden Unternehmen)?
   → De-minimis-Erklärung wird bei Bewilligung verlangt. [RL Nr. 1.3/5 + EU-VO]
M7 Kapazität: ~159–167 h/Monat real leistbar (6 Monate); bei Teilzeit-Anstellung Arbeitsschutz-Grenzen?
   → [FAQ Förderung 01; Handbuch]
M8 Kontoauszug mit Saldo ≥ Eigenanteil (streng gerechnet 2.493,75 € bei 950 h; **2.500 € deckt alle Lesarten ab**) verfügbar/beschaffbar zur Bewilligung?
   → [FAQ Auswahl 03; RL Nr. 4]
M9 (Optional) Second Stage beantragen? Nur JETZT entscheidbar; keine Code-Meilensteine dort.
   → [Handbuch Frage 16]
```

## Auswertung

- **M1–M4 + M5–M8 alle „JA"** → Persönliche Förderfähigkeit nach veröffentlichten Kriterien erfüllt (Nachweispflichten bleiben formal).
- **Ein „NEIN" in M1–M4** → INDIVIDUAL_ELIGIBILITY_UNKNOWN → Sprechstunde 16.11.2026 oder info@prototypefund.de.
- **M3c „UNKNOWN"** → explizite Anfrage (siehe ptf-inquiry-draft.md).
- **M6 nein** → Förderhöhe ggf. durch De-minimis-Freiraum begrenzt (individuell rechnen).

## Verhältnis zur bisherigen Empfehlung

Die bedingte Empfehlung F3 (FormBridge im Feldexa-Kontext, comparison-report.md) basierte auf Projektvergleich. Dieser Baum bestätigt: Es existiert **keine** öffentliche Regel, die FormBridge ausschließt; die offenen Punkte sind ausschließlich persönlich (M1–M9) und zum Teil nur durch PTF-Anfrage auflösbar. Die detaillierte Klassifikation steht in [owner-questions-status.md](owner-questions-status.md).
