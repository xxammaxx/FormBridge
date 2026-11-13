# Review — Bewerbungsreife JG03 Innovation (14.11.2026)

**Geprüfter Candidate:** `ef968f9652069c0f92051db8f91d0125ed70ec1e` · **Branch:** `docs/funding-decision-2026-11-13`
**Charakter:** Zwei unabhängige, read-only Reviews. Keine Selbstrezension, keine Einreichung, kein Portal-Login, keine E-Mail.
**Status:** **`READY_WITH_EXPLICIT_BLOCKERS`** — nicht `READY_FOR_PORTAL_OWNER_APPROVAL`.

## Ergebnis

| Reviewer | Prüfgebiet | Ergebnis |
|---|---|---|
| **A** | Formale Anforderungen, Fristen, Teilnahmevoraussetzungen, Portal-Mapping, Q2 | **PASS** |
| **B** | Projektqualität, Innovation, technische Glaubwürdigkeit, Budget, Second Stage | **PASS** |

**Kein blockierender Residualbefund.** Die verbleibenden Punkte sind Owner-Aktionen oder externe Klärungen, keine ungelösten Dokumentfehler.

## Geprüfter Umfang

- `application-final-de.md` (Fragen 1–19, Wortlimits, Q19)
- `portal-field-mapping.md` und `portal-preflight-2026-11-14.md`
- `owner-checklist.md`, `owner-input-request.md`, `owner-decision-gate.md`
- `validation-report.md`, `submission-runbook.md`
- `six-month-development-plan.md`, `budget-final.md`, `innovation-evidence.md`
- `q2-employment-status.md`, `prototype-fund-q2-verification.md`
- `founder-strategy-2026-2027.md`, `post-selection-founding-plan.md`
- `jobcenter-grants-assessment.md`, `financial-model.md`

## Bestätigte Kernaussagen

- **Frist:** 30.11.2026, 15:00 Uhr MEZ; Förderlinie Innovation; Förderzeitraum 01.06.–30.11.2027; Second Stage 01.12.2027–31.03.2028.
- **Portal:** Keine authentifizierte Sitzung; `/jahrgang-03-innovation/` leitet auf `/auth/`. Login ist eine einmalige Owner-Aktion.
- **Fragen/Limits:** Offizielles Fragen-PDF Innovation (SHA-256 `1d6848c4…4fb74`) und Handbuch JG03 (Sept. 2026) abgeglichen. Q19 steht **nicht** im Fragen-PDF, nur im Handbuch/Portal.
- **Q2:** BMFTR-RL Nr. 3 und JG03-FAQ/Bewerbungsseite verlangen selbstständige Programmierer*innen bzw. Freiberuflichkeit oder Arbeitgeber-Freistellung. Der Owner erfüllt diese formale Zulassungsvoraussetzung **derzeit nicht**. Das JG03-Handbuch listet sie nicht unter den zwingenden Förderbedingungen (Redaktionslücke). Der Nachweiszeitpunkt und die Frage Online-Bewerbung vs. formaler Antrag bleiben offen. **Materielles Risiko.**
- **Formaler Antrag:** März 2027 (Antragswerkstatt) vs. „bis Ende Februar“ auf derselben Detailseite — Terminwiderspruch, PTF-bestätigen lassen.
- **Finanzen:** 950 h / 47.500 PK / 2.375 GK / 49.875 G / 47.381,25 F / 2.493,75 EA; Projekt-Cash-Peak 25.353,13 €; kein persönliches Nettoeinkommen.
- **Gründungsphase:** separat in `post-selection-founding-plan.md`; keine Leistung/Kombination als bewilligt vorausgesetzt.
- **Keine Falschangabe:** Kein bestehender Selbstständigkeitsstatus behauptet; keine persönlichen Daten im Repo.

## Verbleibende explizite Blocker

1. **Portal-Login/Live-Abgleich:** Felder, Zeichenlimits und Pflichtfeldmarkierungen sind ohne Owner-Sitzung `PORTAL_UNVERIFIED`.
2. **Persönliche Angaben:** Accountname, Vorname/Name, E-Mail, Wohnsitzland/-ort, persönlicher GitHub-Link, §11-Projekte, §14-Motivation, Q4/Q5, Q19.
3. **Q2:** formale Zulassungsvoraussetzung derzeit nicht erfüllt; PTF-Antwort oder bewusste Owner-Risikoentscheidung nötig. Schnellster Kanal: Bewerbungssprechstunde **16.11.2026, 17:00 Uhr**.
4. **Owner-Entscheidungen:** Second Stage Ja/Nein, 950/850 h, ggf. Lizenz.

## Verifikation

- **Tests:** 109/109 PASS
- **Relative Links:** 200, 0 gebrochen
- **Arbeitsbaum:** clean
- **Keine Einreichung, keine Kontoerstellung, keine E-Mail, keine Anmeldung, kein Merge**

## Geltungsbereich

Die Reviews gelten für den Inhalt von `ef968f9`. Dieser Record ist ein **docs-only Metadata-Follow-up**; er ändert keine Bewerbungsinhalte. Frühere Reviews (`9ed86225` für das Bewerbungspaket, `d062d9db` für das Gründungs-Delta) bleiben historisch gültig.
