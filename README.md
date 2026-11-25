# FormBridge – öffentliche Projektwebsite

Der Branch `gh-pages` enthält die statische Projektpräsentation, den Erklärfilm und die Simulation mit fiktiven Daten. Er enthält **keine** Forschungsdokumentation.

## Wo liegt welche Dokumentation?

| Ort | Inhalt | Status |
|---|---|---|
| `main` | Ursprünglicher Recherche-Baseline-Stand (13.11.2026, 3 Commits) | **Baseline**, nicht mehr aktuell |
| `docs/funding-decision-2026-11-13` | Aktive Forschung, Prototype-Fund-Bewerbungspaket (`docs/funding/application/**`) und Entscheidungsdokumente (`docs/funding/decision/**`) | **maßgeblich**, offener Draft-PR [#1](https://github.com/xxammaxx/FormBridge/pull/1) |

Bis PR #1 gemergt ist, sind die Dokumentationslinks auf dieser Website (`blob/main/...`) an den **Baseline-Stand auf `main`** gebunden. Sie können daher von der aktuellen Forschung abweichen; maßgeblich ist der Branch `docs/funding-decision-2026-11-13`. Nach dem Merge werden die Links auf den dann aktuellen `main`-Stand umgestellt.

## Prüfen

- `node --check demo.js && node --check film.js`
- `node --test demo.test.cjs`
- `python -m unittest discover -p 'test_*.py' -v` mit Python Playwright und Chromium. Optional setzt `CHROMIUM_EXECUTABLE` den Pfad zu einer bestehenden Chromium-Installation.
