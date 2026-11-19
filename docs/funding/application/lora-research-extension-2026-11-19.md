# Erweiterung RF1: lokal programmierte LoRA-Adapter (optionaler Vergleichsversuch)

**Stand:** 19.11.2026 · **Status:** `PROPOSED / NOT_RUN` · **Antragsgegenstand:** FormBridge, Förderlinie Innovation, Jahrgang 03. Kein eigenständiges KI-Forschungsprojekt, kein zusätzlicher Förderbetrag, keine Implementierungsfreigabe.

## 1. Abgrenzung und Zweck

Der neue Versuch untersucht ausschließlich die semantische Disambiguierung bereits erkannter Felder born-digitaler Wohngeld-PDFs auf versionierte FIM-Datenfeld-IDs (RF1). Beispiel: gleichlautende Namenslabels in Antragsteller- und Vermieterabschnitten. Der regelbasierte Kern ist Muss; lokale KI ist ein optionaler Kandidaten-Ranker, keine Entscheidungsinstanz. Keine OCR/Scans, keine App-Integration, kein eigenständiger allgemeiner LLM-, Strata- oder MindLoop-Forschungsauftrag, keine Änderung von Rechtsform-/Signatur-/Behördenanschlussgrenzen. Der unabhängige Verifier, UNKNOWN und menschliche Bestätigung kritischer Felder bleiben zwingend.

Die Idee, Modellgewichtsdeltas gezielt zu berechnen, stammt aus der aktuellen Weight-Space-Programming-Forschung. MIT CSAIL berichtete für Qwen3.5-0.8B einen gezielten Patch gegen Denk-Wiederholungen; das ist weder ein Nachweis besserer Formularzuordnung noch ein Nachweis von Vorteil auf Pascal. LoRA kann niedrigrangige Gewichtsdeltas als getrennten Adapter darstellen, ohne das Basismodell zu ändern. Der Ansatz ist hier eine **zu testende Hypothese**; keine Leistungsaussage für FormBridge. Vorhandene externe und eigene Konzeptvorarbeiten werden transparent als Vorarbeit dokumentiert, nicht als künftige Förderleistung.

## 2. Enger Versuch und prüfbare Artefakte

| Arm | Vorgehen |
|---|---|
| A | Regelkatalog, Kontext und Validator ohne Modell (Muss) |
| B | A + unverändertes kleines lokales Qwen (nur Kandidaten-Ranking; striktes Schema) |
| C | B + analytisch berechneter, separat aktivierbarer LoRA-Adapter; kein Gradiententraining |

Zuerst A und B auf identischem, lizenzgeklärtem Dev-Split und versioniertem Modell/Tokenizer messen; nur bei konkretem, reproduzierbarem Fehlermuster C auf **einem** Fehlertyp erproben. Qwen3.5-0.8B ist ein Kandidat, keine endgültige Modellauswahl. Basismodell, Adapter-Tensorformen, Rank/Skalierung, Modellrevision, Prüfsummen, Sampling, Runtime und Datensatzhash dokumentieren. Bewertung vor menschlichem Review: Top-1-Precision/Recall auf mapping-fähiger Teilmenge, Coverage, UNKNOWN, Gap-Erkennung, kritische Fehlzuordnung, Laufzeit, Peak VRAM/RAM; Review-Zeit separat. Holdout bis zum eingefrorenen Kandidaten unangetastet lassen. Modellvorschläge müssen auf gültige FIM-Zielpfade und konkrete Feld-/Abschnittsevidenz eingeschränkt sein; Herkunft (Modell-/Adapter-Hash und Entscheidung) auditierbar. Keine personenbezogenen Echtdaten, keine Übermittlung an Behörden oder externe Inferenzdienste. Der Prototyp bleibt ohne Modell und ohne Netz nutzbar.

**Übernahmegate:** reproduzierbarer Vorteil in mindestens einer vorab gewählten Zielmetrik auf ungesehenen Fällen, keine Verschlechterung der verbindlichen Sicherheits-/Qualitätsgates und kein materieller Laufzeit-/Ressourcenrückschritt innerhalb vorab definierter Grenzen; echte GTX 1070 (8 GB VRAM) als lokale Abnahme. Wenn dies nicht gelingt: `NO_BENEFIT` oder `NOT_RUN` dokumentieren, Modell deaktiviert lassen; Kern-Release bleibt unverändert. Ein positiver Modellnutzen wird nicht versprochen. Selbst entwickelte Skripte/Adapter/Tests und Dokumentation nur bei geklärten Rechten unter offener Lizenz veröffentlichen; keine ungeklärte Weitergabe von Modell-/FIM-Drittmaterial.

## 3. Aufwand und Finanzierung

M4 (Abschnitts-Disambiguierung): maximal **30 h von bestehenden 160 h** bei 950 h Gesamtumfang bzw. **15 h von bestehenden 145 h** bei der alternativ wählbaren 850-h-Variante. Kein zusätzlicher Zeitansatz, kein Ersatz von Muss-Aufgaben oder Sicherheits-/Holdout-Tests. Priorität: Pflichtlieferungen; bei Kapazitätsdruck entfällt zuerst C, dann B. Die Zeit ist eigene Entwicklungs-/Messarbeit, nicht unbeaufsichtigte Laufzeit eines Agenten oder einer GPU. Der reguläre Entwicklungsrichtwert ist ca. 80 %; der Versuch wird als konkrete Entwicklung/Evaluation der Zuordnungsengine geführt, keine allgemeine Grundlagensuche.

Primär lokale Ausführung. Wenn nach Förderbeginn mathematische Analysen oder Batch-Referenzläufe die vorhandene Hardware überlasten, kommt **optional** kurzzeitige GPU-Rechenmiete für öffentliche/synthetische Fälle in Betracht. Das ist keine Cloud-Abhängigkeit im ausgelieferten Modul. Vor jeder Miete separate Owner-Budgetfreigabe, Anbieter-/Datenschutz-/Lizenzprüfung, Kostengrenze und automatische Abschalt-/Nachweislogik; kein einziger Euro zusätzlicher Förderforderung. Die offiziellen Regeln nennen projektbezogene Personal- und pauschal 5 % Gemeinkosten auf PK; direkte GPU- oder API-Kosten sind nicht gesondert zugesagt. Schriftlich klären, ob und wie sie ggf. in bestehender Gemeinkostenpauschale berücksichtigt werden können; andernfalls nur gesondert finanzierte zulässige Ressourcen oder lokale Alternative. Keine Doppelförderung, keine stillen Ausgaben. KI darf Werkzeug sein, nicht eigenverantwortliche Entwicklungsleistung ersetzen; Antragsteller muss Programmierkompetenz und eigene überprüfbare Entwicklungs-/Testarbeit belegen. Keine Fremdimplementierung.

**Bis zum Förderbescheid und Förderbeginn:** keine vorgezogene FormBridge-Modul-/Adapterimplementierung. Allgemeine, separat finanzierte Vorarbeiten werden transparent dokumentiert und dürfen nicht als geförderte Arbeit angerechnet werden; bei Überschneidung Umfang/Zeiterfassung/Materialgrenze aktualisieren. Vor Freigabe nur Dokumentation.

## 4. Quellen (Stand 19.11.2026)

- Prototype Fund, FAQ (Kosten, KI-Nutzung): https://www.prototypefund.de/faq
- Förderlinien (Richtwert Entwicklungsanteil, Kompetenzen): https://www.prototypefund.de/foerderlinien
- Förderlinie Innovation: https://www.prototypefund.de/innovation
- MIT CSAIL, Weight-Space Programming: https://rikiyat.github.io/blog/weight-space-programming/
- Experimentprotokolle: https://github.com/RikiyaT/lm_understand-logs/tree/main/exp8_math
- LoRA-Paper: https://arxiv.org/abs/2106.09685

**Freigabestatus:** Arbeitspaket in Entwurf aufgenommen; Förder-/Kostenfähigkeit, persönliche Berechtigung, Portalabgleich, Antragseinreichung und konkrete Ausführung bleiben offen. Keine Änderung des Budgets oder der bestehenden Pflichtmeilensteine.
