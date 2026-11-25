# Owner-Decision-Gate — FormBridge-Bewerbung

**Stand:** 19.11.2026 (RF1-Delta) · **Status:** `EXTERNAL_CONFIRMATION_REQUIRED` (Gründungsstrategie) / `READY_WITH_EXPLICIT_BLOCKERS` (Portal-Preflight)
**Zweck:** Die minimale Menge an Entscheidungen, die der Owner treffen muss, bevor die Bewerbung final eingereicht werden kann. **Keine persönlichen Daten in diesem Dokument.**

## 1. Gate-Stufen

| Stufe | Bedeutung | Erreichbar? |
|---|---|---|
| **READY_FOR_OWNER_INPUT** | Bewerbungstext/Feldvorlage vollständig vorbereitet; offen sind Owner-Angaben/Entscheidungen und externe Klärungen | **Ja** |
| **READY_WITH_EXPLICIT_BLOCKERS** | Portal-Preflight vorbereitet; Live-Login, persönliche Angaben und materielles Q2-Risiko bleiben offen | **Ja, aktuell** |
| **READY_FOR_FINAL_APPROVAL** | Alle Pflichtangaben ergänzt; Q2/Q3 geklärt; Portal-Live-Abgleich erfolgt; Lizenz/Stunden/Second Stage entschieden | Nein, erst nach Owner-Input |
| **EXTERNAL_CONFIRMATION_REQUIRED** | Q2/Gründungsförderung hängen von PTF/Jobcenter/BA-Antworten ab | **Ja, Q2** |
| **VALIDATION_FAILED** | Materialer Fehler ungelöst | Nein |
| **BLOCKED** | Zugriff/Technik verhindert Arbeit | Nein (Portal-Login ist Owner-Blocker, kein Arbeitsblocker) |

## 2. Minimale Owner-Entscheidungen

| # | Entscheidung | Optionen | Auswirkung | Fällig |
|---|---|---|---|---|
| G1 | **Q2-Anfrage senden?** | ja/nein | Klärt **materielle Selbstständigkeitsvoraussetzung** und Nachweiszeitpunkt; formaler Antrag März/Ende Feb (Widerspruch) | vor 30.11.2026 |
| G2 | **PTF-Bewerbung einreichen?** | ja/nein | Start des Verfahrens | 30.11.2026 |
| G3 | **Leistungsweg** | Grundsicherungsgeld/Jobcenter · ALG I/Agentur · keiner | Einstiegsgeld/GZ-Strategie | nach Auswahl |
| G4 | **Gründungsvariante** | A (nach Auswahl) / B (früher) / C (keine) | Risiko/Zeitplan | nach Q2 |
| G5 | **Stunden** | 950 (Default) / 850 | Förderhöhe/Kapazität | **ERLEDIGT: 950 (25.11.2026)** |
| G6 | **Second Stage** | Ja (Default) / Nein | §16/§17 | **ERLEDIGT: Ja (25.11.2026)** |
| G7 | **Lizenz** | Apache-2.0 (Empfehlung) / andere OSI / offen | FOSS-Zusage | **ERLEDIGT: Apache-2.0 (25.11.2026)** |
| G8 | **Projektfassung** | F3 FormBridge (Empfehlung) / F1 / F2 / RepairProbe | Antragsobjekt | **ERLEDIGT: F3 exklusiv (25.11.2026), keine RepairProbe-Bewerbung** |
| G9 | **Q3/Q3b-Anfrage** | ja/nein | Maximalausschöpfung | optional |
| G10 | **Held-out-PDF/Rechte** | vorhanden/beschaffen/Fallback | Evaluationsqualität | vor Förderbeginn |
| G11 | **Optionale GPU-/API-Ausgaben** (RF1) | lokal / nach schriftlicher Kostenklärung und gesonderter Budgetfreigabe / zulässig separat finanziert | keine Erhöhung, kein Hindernis für regelbasierten Kern | vor Ausgabe |

## 3. Was der Owner liefern muss

- M1–M9: **beantwortet** (M1/M2/M4/M5/M9 bestätigt bzw. im Antragstext belegt, M3a–c Registrierungsplan, M6 0 €, M7/M8 bestätigt).
- M7: Kapazität 950 h bestätigt/geplant (158 h/Monat im Schnitt).
- M8: Kontoauszug-Saldo ≥ 2.493,75 € (2.500 € empfohlen) bestätigt/geplant — Vorlage bei Bewilligung.
- M9: Second Stage **Ja** (entschieden 25.11.2026).
- Lizenz (Apache-2.0), Stunden (950) und Projektfassung (F3 exklusiv) sind entschieden; offen sind nur Portal-Stammdaten, Live-Abgleich und der Q2-Stichtag.
- Q4/Q5 (Beteiligungen) und Q19a/b im Portal.
- Keine sensiblen Werte im Repo.

## 4. Was der Agent nicht entscheiden darf

- Keine Selbstständigkeit/Gewerbe/Finanzamt-Anmeldung.
- Keine Jobcenter-/BA-Anträge.
- Keine E-Mail/Portal-Einreichung.
- Keine Lizenzfestlegung.
- Keine rechtsverbindliche Erklärung.
- Keine Merge-Entscheidung.

## 5. Freigabepfad

1. Owner füllt `owner-input-request.md` aus.
2. Q2-Antwort liegt vor (oder Owner akzeptiert konservative Variante A ohne Bestätigung).
3. Stunden/Lizenz/Second Stage entschieden.
4. Portal-Login + Live-Abgleich; Platzhalter ersetzen.
5. Final-Check: 109/109 Tests, 0 Links, Q19, Wortlimits.
6. **READY_FOR_FINAL_APPROVAL**.
7. Einreichung durch Owner.

## 6. Aktueller Status

- Bewerbung: **READY_FOR_OWNER_INPUT**; Portal-Preflight: **READY_WITH_EXPLICIT_BLOCKERS**.
- Gründungsstrategie: **EXTERNAL_CONFIRMATION_REQUIRED** (Q2 materiell widersprüchlich: JG03-FAQ/Bewerbungsseite vs. JG03-Handbuch/JG02-Wiki; Leistungsstatus, Gründungsförderung).
- Keine Einreichung, keine Anfrage, keine Anmeldung, keine Lizenzentscheidung.
