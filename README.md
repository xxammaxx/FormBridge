# FormBridge – öffentliche Projektwebsite

Der Branch `gh-pages` enthält die statische Projektpräsentation, den Erklärfilm und die Simulation mit fiktiven Daten. Die Forschungsdokumentation liegt auf `main`.

## Prüfen

- `node --check demo.js && node --check film.js`
- `node --test demo.test.cjs`
- `python -m unittest discover -p 'test_*.py' -v` mit Python Playwright und Chromium. Optional setzt `CHROMIUM_EXECUTABLE` den Pfad zu einer bestehenden Chromium-Installation.
