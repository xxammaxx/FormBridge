# Feldexa-2.0-Implementierungsnachweis (für den Fördervergleich)

**Datum:** 13.11.2026 · **Repository:** `xxammaxx/Feldexa_2.0` · **main:** `a34456f` (Merge PR #166) · **Zweck:** Trennung „demonstriert" von „geplant" für den Vergleich mit RepairProbe. **Keine Produktänderung.**

## 1. Ausgeführter Testlauf

```bash
cd apps/feldexa_app && ~/flutter/bin/flutter test
cd packages/feldexa_core && ~/flutter/bin/flutter test
cd packages/feldexa_ports && ~/flutter/bin/flutter test
cd packages/feldexa_testkit && ~/flutter/bin/flutter test
cd packages/feldexa_ui && ~/flutter/bin/flutter test
```

| Paket | Tests | Ergebnis |
|---|---:|---|
| `apps/feldexa_app` | 56 | PASS |
| `packages/feldexa_core` | 24 | PASS |
| `packages/feldexa_ports` | 33 | PASS |
| `packages/feldexa_testkit` | 110 | PASS |
| `packages/feldexa_ui` | 17 | PASS |
| **Summe** | **240** | **PASS** |

Fünf Pakete (`feldexa_adapters_android`, `feldexa_adapters_simulated`, `feldexa_application`, `feldexa_export`, `feldexa_recognition`) haben **keine** Testdateien; `flutter test` meldet dort „Test directory 'test' does not appear to contain any test files."

**Umgebung:** Flutter 3.47.7 (stable), Dart 3.13.5, Linux. `flutter pub get` wurde ausgeführt; keine Produktdatei geändert.

## 2. Codeumfang

| Metrik | Wert |
|---|---:|
| Produktions-Dart-Dateien (`lib/`) | 23 |
| Produktionszeilen (`lib/`) | ~3.760 |
| Test-Dart-Dateien (`test/`) | 20 |
| Testzeilen (`test/`) | ~4.800 |
| Pakete mit Produktcode | `feldexa_core` (2), `feldexa_ports` (4), `feldexa_testkit` (12), `feldexa_ui` (2), App-Shell |
| Pakete ohne Produktcode | `feldexa_recognition`, `feldexa_export`, `feldexa_application`, `feldexa_adapters_android`, `feldexa_adapters_simulated` |

## 3. Was die Tests belegen — und was nicht

**Belegt:**

- Geometrie-Wertobjekte (Punkt/Größe/Rechteck), Serialisierung, Validierung.
- Fehler-Taxonomie und Evidenzklassen (`CapabilityEvidence`), Redaktion/Privacy-Regeln.
- Fixture-Katalog/-Loader, SHA-256-Referenzen, reproduzierbare Testdaten, simulierte UI-Banner.
- App-Shell, deutsche Lokalisierung, Font-Bundles, Backup-Regeln, Smoke-Tests.

**Nicht belegt:**

- PDF-Import, Felderkennung/OCR, interaktives Ausfüllen, Overlay-Export.
- Proof Bundle, unabhängiger Verifier, FIM-Zuordnung, Signatur-/Provenienzprüfung.
- Ende-zu-Ende-Lauf auf einem echten Android-Gerät.
- Nutzenmessung (Zeit gespart, Fehler reduziert, Behördenentlastung).
- Produktionsreife, Akzeptanz durch Behörden, Rechtsgültigkeit einer Einreichung.

## 4. Einordnung für die Förderentscheidung

Die 240 Tests sind ein **positives Signal für Testdisziplin und Architektur**, aber **kein Beweis für einen funktionsfähigen Prototyp**. Die Pipeline, die im Mittelpunkt der Feldexa-/FormBridge-Bewerbung steht, ist noch nicht implementiert. Für die Jury muss der Antrag daher klar sagen: „Diese Tests existieren; die Förderleistung beginnt dort, wo die Pipeline noch fehlt." Das ist eine Stärke (Transparenz) und ein Risiko (kein Demo-Code).

## 5. Reproduktionsgrenzen

- Die Zählung ist eine lokale Aufnahme; sie kann sich mit neuen Commits ändern.
- Der Testlauf nutzt die vorhandene Flutter-/Dart-Toolchain; die genauen Versionen sind oben genannt.
- Es wurden keine privaten Daten, keine Portal-Inhalte und keine RepairProbe-Inhalte verwendet.
