# Validierungsbericht FormBridge-Repository — 13.11.2026

**Umfang:** Vollvalidierung der migrierten Forschung und des neuen Repositories vor und nach Veröffentlichung.
**Methode:** Zwei unabhängige Reviewer (A: Technik/Evidenz; B: Funding/Compliance, adversarial) + eigene mechanische Checks. Review-Protokolle: [`review-A-technical-evidence.md`](review-A-technical-evidence.md), [`review-B-funding-compliance.md`](review-B-funding-compliance.md).

## V1 — Research-Integrität: PASS

- Diff der migrierten `docs/research/prior-art-audit.md` gegen das Original (Feldexa_2.0 `cb122fe…`) ergab ausschließlich Pfad-Anpassungen (`docs/funding/evidence/` → `docs/research/appendix/`); keine Änderung von Befunden.
- Anhang-Raw-Audits: byte-identisch migriert; Provenienz-Fußzeilen ergänzt.
- Alle genannten Clone-SHAs verifiziert: KIWO `c40bb34`, Formularagent `4085c46`, CommonForms `f5f4007` (keine LICENSE-Datei — bestätigt), ozg `e6732e5`, GSA pdf-filler `405ed8b`.
- 13 Projekte dokumentiert (7 in Matrix, 6 in Abschnitten/Anhang — Zählung konsistent).

## V2 — Technische Aussagen: PASS

7/7 stichprobenartig geprüfte Datei/Zeilen-Zitate exakt verifiziert (u. a. `converter.py:43-44`, `src/sources/fim/read/read.py:14-18`, `fim/interpret/interpret.py:86`, `ir_builder/sections.py:159-160`, `inference.py:274-290`) gegen die tatsächlichen geklonten Repositories.

## V3 — PDF/XSD-Evidenz: PASS (mit präziser Unterscheidung)

- SHA-256 beider Originalquellen verifiziert (PDF `57f4f3f9…`, XSD `36250e69…`).
- PDF-Eigenschaften reproduziert: PDF 1.6, 8 Seiten, AES `copy:no`, 1× AcroForm-Marker, **0 Widget-Felder**, Textlage vorhanden.
- Original-XSD: **exakt 170 Parser-Fehler** reproduziert (libxml2/xmllint) → das offizielle XSD ist **nicht** standardkonform kompilierbar.
- Normalisierung (D1/D2/D3/D4) vom Reviewer **unabhängig** aus den dokumentierten Schritten reproduziert (D1×1, D2×170, D3×21, D4×4) → `synthetic-instance.xml` **validiert** (exit 0).
- **Klare Unterscheidung (kein Beweisvertausch):** Der Validierungserfolg belegt ausschließlich die **normalisierte Variante**, niemals die Gültigkeit des offiziellen Original-XSD. Das Original bleibt defekt; die Defekt-Tabelle unterscheidet jetzt zwischen 170 betroffenen Elementen und 169 gemeldeten D2-Fehlermeldungen (eine unterdrückt).
- D3-Vollständigkeit: die 21 fehlenden Typ-IDs exakt bestätigt.

## V4 — Dokumentations-Konsistenz: PASS (nach Fixes)

- Relative Links: 22 → nach Ergänzungen **0 broken** (2 Prüfläufe).
- Externe GitHub-Links (Issues #165/#167, PR #168): HTTP 200.
- Zahlenkonsistenz (13 Projekte, 30 Felder mit 7/7/4/4/2/3/3-Klassifikation, 640/185/88 Knoten, 170/169 Fehler) über alle Dokumente konsistent.
- Korrigiert während der Validierung: Universal-Negativbehauptung im Bewerbungstext korpus-spezifisch umformuliert; B1–B4→B1–B6; Typos; truncierte Zitation; Anchor-Format der Provenienz-Links.

## V5 — Lizenz & Datenschutz: PASS (nach Fixes)

- **Kein** LICENSE-File committet (OWNER_DECISION_REQUIRED, README + `docs/governance/license-decision.md` konsistent); Empfehlung Apache-2.0 dokumentiert, nicht bindend.
- **0 Geheimnisse** (ghp_/github_pat/AKIA/Private-Key-Scan leer).
- **Keine personenbezogenen Daten** — nur erkennbar synthetische Werte (Mustermann/Musterstadt/`max@example.com`/synthetische IBAN); `reference-dataset.json` enthält keine Werte, nur Koordinaten/Klassifikationen.
- **Keine urheberrechtlich geschützten Drittassets:** PDF-Bytes und Original-/Normalisierungs-XSD sind **nicht** im Repo (URL + SHA-256 + Reproduktionsbefehle stattdessen); Zitate auf Fremdcode max. einzeilig mit Quellenangabe.
- `fim-fields-S00000159V1.4.json` (136 KB, vollständiger Metadaten-Index): Provenienz + Lizenz-Unklarheit + Entfernungs-Fallback explizit in [`docs/research/evidence/EVIDENCE.md`](../research/evidence/EVIDENCE.md) dokumentiert — verbleibender Rest: rechtliche Klärung vor Förderbeginn (Owner-Aktion).

## V6 — Repository-Unabhängigkeit: PASS

18 Dateien, ausschließlich Markdown/JSON/XML-Dokumentation; **kein** Produkt- oder Prototyp-Code, keine Build-/CI-/Manifest-Dateien, keine Feldexa-Abhängigkeit in beide Richtungen; ADR-001 verankert die Unabhängigkeit.

## V7 — Funding-Integrität: PASS (nach Fixes)

- Bestandsarbeit (A) vs. Fördergegenstand (B) sauber getrennt (`docs/funding/project-boundary.md` §A–E, mit Verbotensliste §C und Nachführungspflicht §D).
- Provenienz konsistent: `cb122fe…`, PR #168, 13.11.2026 — über README, ADR-001, boundary, EVIDENCE.
- Keine verfrühte Implementierung; Meilensteine bleiben Forschungsziele; CONDITIONAL_GO + B1–B6 über alle Dokumente konsistent (Fix: Überschrift B1–B4 → B1–B6).

## V8 — GitHub-Veröffentlichung: siehe [`v8-publication-verification.md`](v8-publication-verification.md)

## Restrisiken (offen, nicht verheimlicht)

1. **Lizenz unentschieden** (Owner-Entscheidung) — bis dahin ist der Inhalt rechtlich nicht weiterlizenziert.
2. **fim-fields-Index:** Redistribution rechtlich vor Förderbeginn zu klären; Entfernungs-Fallback dokumentiert.
3. **Archivierung der Fürther Quelle:** URL-Drift-Risiko; Rights-cleared Archivierung ist Owner-Aufgabe.
4. **Handbuch-Drift:** Prototype-Fund-Kriterien können sich ändern; Vor-Abgabe-Check im Portal erforderlich.
5. „Keine weiteren Fehler gefunden" ist **kein** Beweis für Fehlerfreiheit — die Prüfungen decken die genannten Klassen ab, nicht alle denkbaren Defekte.
