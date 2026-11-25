# Lizenz-Entscheidung — Apache-2.0 (entschieden am 25.11.2026)

**Analyse:** 13.11.2026 · **Entscheidung des Eigentümers:** 25.11.2026 · **Status:** `DECIDED`

**Entschieden: Apache-2.0.** Der vollständige Lizenztext liegt als [`LICENSE`](../../LICENSE) im Wurzelverzeichnis (kanonischer Apache-2.0-Text, 202 Zeilen, SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`), SPDX-Kennung `Apache-2.0`, Copyright-Zeile: „Copyright 2026 xxammaxx“. Die Lizenz gilt für **eigene** Inhalte dieses Repositories. Amtliche Quellen (Fürther Wohngeld-PDF, FIM-XSD) und der daraus extrahierte FIM-Metadatenindex bleiben ausgenommen (siehe „Drittmaterial bleibt außen vor“).

## Entscheidungsgrundlage: Apache-2.0

**Begründung (gegen die geprüften Alternativen):**

| Kriterium | Apache-2.0 | MIT | MPL-2.0 |
|---|---|---|---|
| Patentklausel (Schutz für Verwaltungs-Nutzer/Dienstleister) | ✅ explizit | ❌ keine | ✅ eingeschränkt (auf Dateien) |
| Kompatibilität mit künftiger Feldexa-2.0-Integration | ✅ (Feldexa-Repo aktuell ohne LICENSE; Apache kompatibel zu GPL-3 über §11, breit integrierbar) | ✅ maximal liberal | ⚠️ file-level Copyleft — okay für Bibliotheksdateien, aber stärkere Pflichten für Integratoren |
| Öffentlicher Sektor / Behörden-Adoption | ✅ verbreiteter De-facto-Standard (u. a. viele FITKO-nahe Projekte) | ✅ verbreitet | ✅ in EU-Verwaltungskontexten etabliert (Formularagent nutzt MPL-2.0) |
| Copyleft-Pflichten für Wiederverwender | ❌ keine | ❌ keine | ⚠️ Änderungen an MPL-Dateien offenlegen |
| Trademark/Beitrittsregelungen für Community-Wachstum | ✅ (§6) | ❌ | ⚠️ (nur die MPL selbst) |
| Risiko unbeabsichtigter Lizenzkonflikte mit künftigen Abhängigkeiten | gering | gering | gering-mittel |

**Entscheidende Punkte:**
1. Die Patentausschluss-/Patentlizenz-Klausel der Apache-2.0 ist für ein Infrastrukturprojekt im öffentlichen Verwaltungskontext der stärkste Schutz vor Patent-Risiken für Wiederverwender.
2. MPL-2.0 wäre passend, falls künftig Bausteine unter MPL-2.0 (z. B. Formularagent-Muster) direkt übernommen würden — aktuell wird **kein** Code aus MPL-Projekten übernommen (nur Dokument-Recherche).
3. MIT ist maximal einfach, verzichtet aber auf die explizite Patentregelung.

**Hinweise zur Entscheidung:**
- Erst bei Auswahl: LICENSE-Datei (Apache-2.0-Text) + Copyright-Zeile "Copyright 2026 xxammaxx" committen und README-Lizenzabschnitt aktualisieren; SPDX-ID `Apache-2.0` ergänzen.
- **Drittmaterial bleibt außen vor:** Apache-2.0 gilt nur für eigene Inhalte. FIM-XSD/PDF (amtlich, Lizenz unklar) werden nicht redistribuiert; die Analysen der geprüften Fremdprojekte (Apache-2.0/MIT/MPL-2.0/MIT-ähnlich) sind Zitate/Analyse mit Quellenangabe, keine Übernahme lizenzpflichtigen Codes.
- Feldexa-2.0-Seite: sobald FormBridge lizenziert ist, sollte Feldexa_2.0 eine kompatible LICENSE erhalten (derzeit keine vorhanden — Bestandteil der Owner-Entscheidung).

**Wirkung der Entscheidung:** Die Nutzung, Weitergabe und Veränderung eigener Repository-Inhalte ist ab 25.11.2026 unter Apache-2.0 zulässig (Namensnennung, Lizenzbeilage, Änderungshinweis, Patentklausel). Die frühere Aussage „Nur-Lese-Veröffentlichung ohne Lizenzierung“ ist damit überholt. Offen bleibt allein die **Rechteklärung für Drittmaterial** (amtliche PDFs/XSDs, FIM-Metadatenindex) — sie ist keine Lizenzfrage dieses Repositories.
