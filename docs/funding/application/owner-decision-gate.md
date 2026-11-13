# Owner-Decision-Gate — FormBridge-Bewerbung

**Stand:** 13.11.2026 · **Status:** `EXTERNAL_CONFIRMATION_REQUIRED` (Gründungsstrategie) / `READY_FOR_OWNER_INPUT` (Bewerbung)
**Zweck:** Die minimale Menge an Entscheidungen, die der Owner treffen muss, bevor die Bewerbung final eingereicht werden kann. **Keine persönlichen Daten in diesem Dokument.**

## 1. Gate-Stufen

| Stufe | Bedeutung | Erreichbar? |
|---|---|---|
| **READY_FOR_OWNER_INPUT** | Bewerbung vollständig vorbereitet; offen sind Owner-Angaben/Entscheidungen und externe Klärungen | **Ja, aktuell** |
| **READY_FOR_FINAL_APPROVAL** | Alle Pflichtangaben ergänzt; Q2/Q3 geklärt; Portal-Live-Abgleich erfolgt; Lizenz/Stunden/Second Stage entschieden | Nein, erst nach Owner-Input |
| **EXTERNAL_CONFIRMATION_REQUIRED** | Q2/Gründungsförderung hängen von PTF/Jobcenter/BA-Antworten ab | **Ja, Q2** |
| **VALIDATION_FAILED** | Materialer Fehler ungelöst | Nein |
| **BLOCKED** | Zugriff/Technik verhindert Arbeit | Nein (Portal-Login ist Owner-Blocker, kein Arbeitsblocker) |

## 2. Minimale Owner-Entscheidungen

| # | Entscheidung | Optionen | Auswirkung | Fällig |
|---|---|---|---|---|
| G1 | **Q2-Anfrage senden?** | ja/nein | Klärt Bewerbungszeitpunkt/Selbstständigkeit; formaler Antrag **Ende Feb 2027** | vor 30.11.2026 |
| G2 | **PTF-Bewerbung einreichen?** | ja/nein | Start des Verfahrens | 30.11.2026 |
| G3 | **Leistungsweg** | Grundsicherungsgeld/Jobcenter · ALG I/Agentur · keiner | Einstiegsgeld/GZ-Strategie | nach Auswahl |
| G4 | **Gründungsvariante** | A (nach Auswahl) / B (früher) / C (keine) | Risiko/Zeitplan | nach Q2 |
| G5 | **Stunden** | 950 (Default) / 850 | Förderhöhe/Kapazität | vor Einreichung |
| G6 | **Second Stage** | Ja (Default) / Nein | §16/§17 | vor Einreichung |
| G7 | **Lizenz** | Apache-2.0 (Empfehlung) / andere OSI / offen | FOSS-Zusage | vor Einreichung |
| G8 | **Projektfassung** | F3 FormBridge (Empfehlung) / F1 / F2 / RepairProbe | Antragsobjekt | vor Einreichung |
| G9 | **Q3/Q3b-Anfrage** | ja/nein | Maximalausschöpfung | optional |
| G10 | **Held-out-PDF/Rechte** | vorhanden/beschaffen/Fallback | Evaluationsqualität | vor Förderbeginn |

## 3. Was der Owner liefern muss

- M1–M6: Ja/Nein-Bestätigungen (Alter, Wohnsitz/Steuern, Status/Freistellung, Programmierkenntnisse, Vorarbeiten, De-minimis).
- M7: Kapazität 950/850.
- M8: Kontoauszug-Saldo ≥ 2.493,75 € (950 h; 2.500 € empfohlen).
- M9: Second Stage Ja/Nein.
- Lizenz, Stunden, Projektfassung.
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

- Bewerbung: **READY_FOR_OWNER_INPUT**.
- Gründungsstrategie: **EXTERNAL_CONFIRMATION_REQUIRED** (Q2 widersprüchlich: JG03-Handbuch/FAQ vs. JG02-Wiki; Leistungsstatus, Gründungsförderung).
- Keine Einreichung, keine Anfrage, keine Anmeldung, keine Lizenzentscheidung.
