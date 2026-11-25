# Evidenz-Manifest — docs/research/evidence/

**Stand:** 13.11.2026 · Diese Datei dokumentiert Herkunft, Lizenzstatus und Reproduktion jedes hier abgelegten Artefakts. **Amtliche Originaldateien (PDF, XSD) werden bewusst nicht redistribuiert.**

| Artefakt | Was ist es? | Erstellt | Herkunft / Provenienz | Lizenzstatus |
|---|---|---|---|---|
| `reference-dataset.json` | 30 Referenzfelder des Fürther Wohngeld-Vordrucks mit PDF-Koordinaten (pdftotext -bbox-layout), FIM-Zielpfaden und Klassifikation (MAPPED/CONTEXT_REQUIRED/VALUE_CODELIST/STRUCTURAL_*/AMBIGUOUS_SEMANTIC/COVERAGE_GAP/UNMATCHED). **Werte rein synthetisch.** | 13.11.2026 | eigene Analyse (Feldexa_2.0 `cb122fe…`); Quellen: Fürth-PDF (URL+SHA-256, siehe reference-case-wohngeld.md §1) + FIM-XSD (immutable URL) | eigene Arbeit; Referenz auf amtliche Quellen via Hash/URL |
| `fim-fields-S00000159V1.4.json` | Struktur-Index des FIM-Schemas: 640 Knoten (Feld-IDs als Elementnamen, Pfade, deutsche Labels, Typen) — ein **vollständiger, maschinell extrahierter Metadaten-Index** des Schemas (keine Schematexte/Regeln, nur Kurzlabels), benötigt als wiederverwendbare Goldstandard-Referenz für die Feldzuordnung | 13.11.2026 | extrahiert aus https://schema.fim.fitko.net/immutable/schemas/S00000159V1.4_2024-01-22-1705942219513.xsd (SHA-256 `36250e69…`) | abgeleitete Metadaten eines amtlichen Artefakts mit **unklarer Lizenzangabe**. Entscheidung für die Veröffentlichung dieses Index: er ist rein faktischer Metadaten-Inhalt (IDs/Labels/Typen) mit klarer Quellenangabe — **vorbehaltlich** einer rechtlichen Prüfung durch den Eigentümer vor dem Förderfall; falls diese negativ ausfällt: Datei entfernen (Reproduktion: Extraktion aus dem Original-XSD nach dokumentierten Schritten in reference-case-wohngeld.md) |
| `synthetic-instance.xml` | Synthetische XML-Testinstanz (nur Fantasiedaten: „Mustermann" etc.), validiert gegen eine **lokal erzeugte, normalisierte** Schemavariante — **nicht** gegen das offizielle Original | 13.11.2026 | eigene Arbeit (Feldexa_2.0 `cb122fe…`) | eigene Arbeit; FIM-Feld-IDs als Referenzen |

**Nicht in diesem Repository (bewusst):**
- Fürther Wohngeld-PDF (amtlich, kopierbeschränkt `copy:no`) — Referenz: URL + SHA-256 `57f4f3f98671a3c659f131cfd6d58abf5eb80a0a2c585ddd575761fe60c21463`
- Original-FIM-XSD (amtlich) — Referenz: URL + SHA-256 `36250e69a5954b6e233f49a75c021e5cf2cf69a6f26a72c59829fc496ecda6d3`
- Normalisierte XSD-Variante (Derivat des amtlichen XSD; Lizenz unklar) — **Reproduktionsverfahren** dokumentiert in reference-case-wohngeld.md (4 deterministische Schritte + Validierungsbefehl)

## Hashregister der lokalen Artefakte (Stand 25.11.2026)

Diese Tabelle ist die **Quelle der Wahrheit** für die Unverändertheit der veröffentlichten Forschungsartefakte. Sie wird automatisiert geprüft:

```bash
python3 -m unittest discover -s docs/research/evidence -p 'test_*.py' -v
```

| Artefakt | Bytes | Zeilen | SHA-256 |
|---|---:|---:|---|
| `reference-dataset.json` | 9009 | 422 | `91799582ac2d46e62a761893354dd280a12c7e5d5b52df89b0e961b6e186380d` |
| `fim-fields-S00000159V1.4.json` | 136657 | 5122 | `663cd4a266c8c8c029e718472edcf08f83c55ffc8cfe53167803c9ad5018a5e5` |
| `synthetic-instance.xml` | 4391 | 145 | `f02e032c51b1eae58aa8f755c08c93726b566370a7d429c32404ac8634deb5b6` |

Das Register belegt **Integrität, nicht Urheberschaft**: es zeigt, dass die Dateien unverändert sind; es ersetzt keine rechtliche Prüfung der abgeleiteten FIM-Metadaten (siehe Vorbehalt oben). Die Prüfungen decken Struktur, Klassifikationsverteilung, Feldindex-Invarianten und die Bindung der synthetischen Instanz an den Index ab; sie implementieren **keine** FormBridge-Pipeline (`project-boundary.md` §C.1).

**Reproduktionsbefehle:** siehe [reference-case-wohngeld.md](../reference-case-wohngeld.md) §Reproduktion.
