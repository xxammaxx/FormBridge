# Lizenz-Empfehlung — Status: OWNER_DECISION_REQUIRED

**Datum:** 13.11.2026 · **Keine Lizenz wurde binding committet.** Diese Datei dokumentiert Analyse und Empfehlung; die verbindliche Wahl obliegt dem Repository-Eigentümer. Bis zur Entscheidung ist der Repository-Inhalt rechtlich **nicht lizenziert** (Vorbehaltsurheberrecht) — Dritte dürfen lesen, aber nicht beliebig weiterverwenden.

## Empfehlung: Apache-2.0

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

**Vorläufige Wirkung bis zur Owner-Entscheidung:** Nur-Lese-Veröffentlichung (public repo) ersetzt keine Lizenzierung; kommerzielle/behördliche Nutzung vor Lizenzwahl separat anfragen.
