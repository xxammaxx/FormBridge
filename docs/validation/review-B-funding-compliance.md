# Review B — Adversarial Funding- & Compliance-Audit (unabhängig)

**Reviewer:** unabhängiger adversarial Auditor (separater Agent-Prozess)
**Datum:** 13.11.2026 · **Protokoll:** vollständige Notizen in der Recherche-Umgebung (`formbridge-review-B.md`)
**Scope:** Lizenzierung, Datenschutz, Funding-Grenzen, irreführende Antrags-/Neuheits-Sprache.

## Ergebnis: V5 PASS · V7 PASS (conditional auf V7-1, inzwischen aufgelöst)

**Verifiziert:**
- V5: kein LICENSE (konsistent OWNER_DECISION_REQUIRED in README + license-decision.md); 0 Geheimnisse; keine personenbezogenen Daten (nur synthetische Werte); keine Drittassets (PDF/XSD-Bytes fehlen absichtlich; nur URL+SHA-256+Reproduktionsbefehle); XSD-Zitate einzeilig mit Beleg.
- V7: Provenienz konsistent (cb122fe, PR #168, 13.11.2026) über README/ADR-001/boundary/EVIDENCE; Grenze A/B/C explizit; B1–B6 in Spec §6/§7 verankert; **keine Implementierung** (keine Code-/Manifest-/CI-Dateien).
- Adversarial 1–6: keine Treffer — keine Funktions-Claims als vorhanden/getarnt; Neuheits-Sprache korpus-spezifisch; Feldexa-Unabhängigkeit beidseitig korrekt; Lizenz-Status erklärt; Fremdattribution sauber (URLs+SHAs, keine Lizenztext-Kopien).

**Befunde → Behoben:**
- **MAJOR V7-1:** Referenzen auf leeres `docs/validation/` (README, ADR-001) + „Validierung abgeschlossen" ohne Artefakte → Validierungsberichte wurden committet (dieses Verzeichnis); boundary-§A damit wahr.
- MINOR V7-2: „B1–B4" vs. Tabelle B1–B6 → Überschrift/Text korrigiert.
- MINOR V7-3/4: trunzierte Zitation (`innovation-assessment-…`) → voller Pfad; Typos (Docs--only; fehlendes Leerzeichen; Großschreibung Satzbeginn) → korrigiert.
- MINOR V5-1: fim-fields-JSON als **vollständiger** Metadaten-Index korrekt beschrieben (kein „Excerpt") + explizite Vorbehalt-Entscheidung mit Entfernungs-Fallback in EVIDENCE.md.
- MINOR V5-2: verwaistes Leer-Verzeichnis `{docs/` (Shell-Brace-Artefakt) → entfernt.

**Residuum:** Lizenz- und fim-fields-Redistribution-Entscheidung bleiben Owner-Aktionen; README-Formulierung „kein geprüftes freies Projekt…" bewusst korpus-spezifisch belassen (Qualifier + Audit-Link vorhanden).
