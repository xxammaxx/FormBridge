# Revalidierung — RF1-LoRA-Delta (19.11.2026)

**Status:** `DELTA_VALIDATED_WITH_BLOCKERS` · Basis: `d8dff21ea65b8ebe706b0ad02987559f6812fcba`. Dokumentarische Prüfung, keine Modell- oder Fördervalidierung und keine neuen unabhängigen Reviewer-A/B-Reviews. Historische Reviews beziehen sich auf ihre jeweiligen Basis-SHAs.

## Prüfungen

| Prüfung | Ergebnis |
|---|---|
| Bestehender Finanzmodell-Regressionslauf (`python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -q`) | 109/109 PASS; unveränderte Finanzlogik |
| 950 h | 47.381,25 € geplante Förderung, 2.493,75 € Eigenanteil; RF1 max. 30/160 h M4 |
| 850 h alternativ | 42.393,75 € geplante Förderung, 2.231,25 € Eigenanteil; RF1 max. 15/145 h M4 |
| Wortlimits, finale Textfelder (Whitespace, ohne Owner-Platzhalter) | §1: 22/30; §2: 84/100; §3: 168/175; §4: 133/175; §5: 67/100; §7: 82/100; §8: 90/100; §9: 62/100; §10: 7/30; §16: 98/175; §17: 29/100; alle innerhalb der dokumentierten Limits |
| Relative Markdown-Linkziele | 98 Verweise in den geänderten Dokumenten geprüft, 0 fehlende Ziele (Pfadauflösung im Kandidatenbaum) |
| RF1-Scope | A Pflicht; B/C optional; Kernmeilensteine, UNKNOWN, menschliche Bestätigung und Verifier unverändert |
| Technische Evidenz | Weight-Space Programming als Hypothese für FIM; kein belegter Modellnutzen, keine Trainings-/Cloudpflicht |
| Vorarbeiten | vor Förderbeginn keine FormBridge-Implementierung; getrennte allgemeine Forschung, keine Doppelabrechnung |
| Förderregeln | FAQ (KI als Werkzeug, eigenverantwortliche Entwicklung; 5 % GK auf PK) und Förderlinien (ca. 80 % Entwicklung) abgeglichen; keine bestätigte GPU-/API-Förderfähigkeit |

Die tatsächliche Portalzählung, Förderentscheidung, Nutzbarkeit/Leistung auf realer GTX 1070 sowie der Adapterversuch sind ausdrücklich **nicht verifiziert**. Der Versuch bleibt `PROPOSED / NOT_RUN`. GPU-Ausgaben erfordern schriftliche Kostenklärung und separate Owner-Freigabe; keine Ausgaben ausgelöst.

## Offene Gates

Persönliche Angaben und Programmierkompetenz, Q2/Selbstständigkeit, Q3/Q3b, Stundenvariante, Lizenz und Second Stage, Live-Portalabgleich, Owner-Freigabe. Kein Merge, keine Einreichung, keine Implementierung und keine Fremdbeauftragung.

Details: [RF1-Ergänzung](lora-research-extension-2026-11-19.md), [Budget](budget-final.md), [Gate](owner-decision-gate.md).
