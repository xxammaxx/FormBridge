# V8 — Veröffentlichungs-Verifikation

**Datum/Uhrzeit:** 13.11.2026 (direkt nach Push) · **Methode:** `gh repo view` + **frischer** Clone von `https://github.com/xxammaxx/FormBridge.git` in isoliertes Verzeichnis, Prüfung gegen die lokalen Erwartungen.

| Prüfung | Ergebnis |
|---|---|
| Repository existiert, ist **public** | ✅ `visibility: PUBLIC`, URL https://github.com/xxammaxx/FormBridge |
| Owner/Name korrekt | ✅ `xxammaxx/FormBridge`, Default-Branch `main` |
| Remote-Commit == lokaler Head | ✅ `78d7fc3ccccb53551e20520ff41dc034049d8741` |
| Erwartete Dateien vollständig (10 Struktur-Pflichtdateien) | ✅ alle vorhanden |
| Dateibestand sauber | ✅ 21 Dateien, ausschließlich `.md`/`.json`/`.xml` — kein Code, keine Build-/CI-Dateien |
| Keine Geheimnisse im veröffentlichten Stand | ✅ Scan (ghp_/github_pat_/AKIA/Private-Key) leer |
| Keine unerlaubten Drittassets | ✅ kein PDF, kein Original-/Normalisierungs-XSD (nur URL+SHA-256+Reproduktion) |
| Referenzen auflösbar | ✅ relative Links 0 broken (lokaler Lauf vor Push); externe Feldexa-Links HTTP 200 |

**Bekannte Grenze:** Der frische-Clone-Scan prüft Inhalte und Struktur; das Rendering von Markdown-Ankern wurde nur gegen GitHub-Konventionen geprüft, nicht im Browser-Rendering verifiziert.
