# FormBridge – öffentliche Projektwebsite

Der Branch `gh-pages` enthält die statische Projektpräsentation, den Erklärfilm und die Simulation mit fiktiven Daten. Er enthält **keine** Forschungsdokumentation.

## Wo liegt die Dokumentation?

| Ort | Inhalt | Status |
|---|---|---|
| `main` | Forschungsdokumentation, Evidenz, technische Spezifikation **und** das vollständige Prototype-Fund-Bewerbungspaket (`docs/funding/application/**`, `docs/funding/decision/**`) sowie `LICENSE` (Apache-2.0) | **maßgeblich** |
| `docs/funding-decision-2026-11-13` | Arbeitsbranch der Bewerbungsvorbereitung; am 25.11.2026 nach `main` gemergt, Inhalt identisch | historisch / identisch |
| `5ad209a` | Ursprünglicher Recherche-Baseline-Stand (13.11.2026) | historischer Ausgangsstand |

Die Dokumentationslinks dieser Website (`blob/main/...`) verweisen damit auf den **aktuellen** Stand: ADR-001, Lizenz-Entscheidung, Prior-Art-Audit, Referenzfall, technische Spezifikation und Referenzdatensatz sind nach dem Merge vom 25.11.2026 unverändert gültig.

## Prüfen

- `node --check demo.js && node --check film.js`
- `node --test demo.test.cjs`
- `python -m unittest discover -p 'test_*.py' -v` mit Python Playwright und Chromium. Optional setzt `CHROMIUM_EXECUTABLE` den Pfad zu einer bestehenden Chromium-Installation.
