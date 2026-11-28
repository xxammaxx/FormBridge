# RF1: lokale Forschungssteuerung, LoRA-Adapter und Offline-Nachweis

> **Aktualisierung 28.11.2026 – maßgebliche RF1-Neuausrichtung:** PX-51 Delta, inkrementelle Kontextverdichtung und kontrollierte Inferenz ohne Gewichtsänderungen ersetzen den bisherigen optionalen Adapterarm. A = Regeln (Pflicht), B = unverändertes lokales Modell, C = dasselbe Modell mit Protokollsteuerung. LoRA/Weightspace bleibt separate historische Vergleichsforschung, kein Pflichtdeliverable. Der Eigentümer berichtet praktischen Skill-Einsatz; Protokolltreue, Tokenbedarf, Peak RAM/VRAM, Laufzeit und FIM-Zuordnungsqualität sind auf identischen ungesehenen Fällen zu messen. Protokollversion, Validator, Kontextbudget und Modell-/Tokenizerhash dokumentieren. UNKNOWN, menschliche Freigabe, Netzsperre, unabhängiger Verifier, bestehende Stunden und Fördergrenzen bleiben verbindlich. RF1 bleibt NOT_RUN. Die nachfolgenden historischen Adapterdetails sind archivierte Planung, keine aktuellen Anforderungen.


Stand 20.11.2026 · **PLAN / NOT_RUN** · Fördergegenstand ausschließlich FormBridge, keine Vorimplementierung, kein zusätzlicher Förderbetrag.

## Leitfrage und Abgrenzung

Kann ein kleines lokales LLM mit direkt berechnetem, reversiblen LoRA-Adapter eine konkret beobachtete FIM-Disambiguierungsfehlerklasse gegenüber dem regelbasierten Muss-Kern und unverändertem lokalem Modell verbessern, ohne neue Cloud-Abhängigkeit oder kritische Regression? Ressourcensparsamkeit und Nutzen sind Hypothesen. Kein Gradiententraining im primären Arm, keine allgemeine programmierbare LLM-Plattform. A (Regeln) ist verpflichtend; B (unverändertes lokales Modell) ist wissenschaftlicher Kontrollarm; C (lokal erzeugter Adapter) optional. Nur nachgewiesener C-Pfad darf ausgeliefert werden, sonst A. Rechte der Modell-/Adapter-/Datensatzartefakte vor Veröffentlichung prüfen. Keine Scans, Behördenübermittlung, Feldexa-Integration oder private Echtdaten.

## Getrennte Vorarbeit: Homelab

Berichtete praktische Erfahrungen aus den vom Antragsteller im Gespräch geteilten lokalen Testberichten/Terminalausgaben (nicht unabhängig neu ausgeführt; keine vertraulichen Dokumente, Adressen, Job-IDs, Hostdetails oder Rohlogs veröffentlichen):

| Datum | Berichteter Befund | Aussagegrenze |
|---|---|---|
| 13.11.2026 | Lokaler Qwen3 1.7B-Test auf dem Rechner mit erkannter GTX 1070 mit korrektem JSON, berichtete 15,8 s beim Erstaufruf und 3,9 s Auswertung. | Einzelner synthetischer Smoke; keine Genauigkeitsquote oder Adapterwirkung. |
| 14.11.2026 | Realer Scanner→SFTP→Watcher-Pfad, OCR auf zwei Seiten (8,6 s, zweite Seite als leer erkannt), Qwen3.5 4B lokaler Vorschlag (21,4 s). | Klassifikation verwechselte Rechnung und Mahnung; Review notwendig. Kein vollständiger E2E-Erfolg. |
| 15.11.2026 | Berichtete GPU-Prüfung, Queue, Rückgabe von GPU-Speicher und 24/24 Tests im Homelab. | Testumfang aus Nutzerbericht, kein unabhängiger Audit und kein RF1-Gate. |
| 16.11.2026 | Nutzer berichtet korrekte Inhaltserkennung eines Scans, jedoch fehlende Datenübertragung und nur einseitigen Scan. | OCR-Erkennung allein ist kein automatisierter Importnachweis. |
| 18.11.2026 | Terminalbericht: Qwen3.5:4b, Ollama 0.40.16, 3,1 GB, Kontext 4096, `ollama ps` 100 % GPU auf NVIDIA GTX 1070 (8 GB). | Modellladung/GPU-Ausführung berichtet; keine garantierte Durchsatz-/Qualitätsmessung und kein LoRA-Nachweis. |

**Status:** `OWNER_REPORTED_LOCAL_LLM_SMOKE` / `RF1_NOT_RUN`. Ein bestätigter GitHub-Quellstand des Homelab-Berichts liegt für diese Notiz nicht vor. Vor geplanter Veröffentlichung können anonymisierte, vom Antragsteller freigegebene Terminal-/Testbelege und Modell-/Runtime-Revision beigefügt werden. Die Vorarbeit dokumentiert praktische Erfahrungen mit lokaler Infrastruktur und Grenzen, ersetzt weder den eigenen Kompetenznachweis noch FormBridge-E2E, den Netzsperrentest oder Adaptermessungen. Keine Doppelabrechnung; unabhängig von Feldexa, getrenntes Projekt.

## Zwei getrennte Vertrauensbereiche

**Lokale Zone:** kleines LLM auf GTX 1070 (Startkandidat Qwen3.5-0.8B; 4B nur bei Ressourcenfreigabe), lokaler Controller/Agent, Python-Skripte, Modell- und Adapterdateien, synthetische Fixtures, Holdout, Auswertungen. Modell schlägt Hypothesen vor bzw. verarbeitet nur lokal; deterministische Skripte sind allein für Rechen-/IO-/Testoperationen zuständig. Kein Cloud-Endpunkt, kein automatischer Fallback, keine ausgehenden Netzverbindungen während RF1-Ausführung.

**Optionale externe Entwicklungszone:** leistungsfähiges LLM z. B. Astra über vorhandenes Kontingent nur nach Freigabe, ausschließlich zur Hypothesen-/Codeunterstützung auf öffentlichen Modellinformationen und eigens synthetischen Aufgaben, niemals reale Dokumente, OCR-Text, davon abgeleitete Daten, private Prompts/Aktivierungen, unbereinigte Logs, Gewichte, Holdout oder Zugangsdaten. Es erhält keinen SSH-/Shell-/Netz-/Dateizugriff auf die lokale Zone. Keine maschinelle Auslagerung der technologischen Umsetzung. Der Antragsteller versteht, schreibt/prüft und verantwortet Umsetzung und Tests; bei fehlender Kompetenz/Prüfbarkeit abbrechen. Keine zusätzlichen API-Ausgaben.

**Freigabegateway:** Keine direkte Fernsteuerung. Ein externer Vorschlag ist als untrusted Datensatz zu behandeln, kein ausführbarer Shell-Code. Nur vorab zugelassene abstrakte Felder (experiment_id, model_revision, operation, layer_id, direction_id, rank, scale, test_suite_id), syntaktisch und semantisch streng geprüft. Der lokale Controller verwendet lediglich die freigegebene Operation; lokale Skripte erzwingen Tensorformen, Modell-/Adapterhash, Whitelist, Norm-/Zeit-/Speichergrenzen und menschliche Freigabe. Unbekannte Operationen, Pfad-/URL-/Command-Felder, ungültige/inkompatible Tensoren, unzulässige Skalen werden abgewiesen. Rückmeldung nach außen nur separat freigegebene synthetische Testaufgaben/Messzusammenfassungen, niemals eine Zusammenfassung echter Formulardaten. Kein automatischer bidirektionaler Zugang, keine Telemetrie. Nur offline/quarantänisierte Artefakte in die lokale Zone übernehmen, nicht die Netzsperre für den Modellpfad lockern. Bei nicht sicher trennbarer Schnittstelle läuft RF1 ohne externe KI oder entfällt.

## Verbindlicher Nachweis bei späterer Umsetzung

Alle Prüfungen sind geplant, `NOT_RUN`; kein zusätzlicher Pflichtumfang. Für RF1 innerhalb des bestehenden M4-Zeitbudgets; Integration und Veröffentlichung im bestehenden M5/M6-Arbeitsumfang. Der Pflichtkern hat seine eigenen Offline- und Verifier-Gates unabhängig von RF1.

| Gate | Verfahren | PASS nur wenn |
|---|---|---|
| L0 Basis ohne Modell | Cold start mit lokalen, rechtegeklärten Schema-/Testdateien, Modellpfad deaktiviert, kein Netz | Regelkern, UNKNOWN, Review, Emit/Verify funktionieren gemäß Muss-Gates. |
| L1 Reeller Offline-Modelllauf | Modell und Adapter vorab lokal bereitstellen; isolierte Laufzeit mit technisch gesperrtem externem Egress (inkl. DNS); Netzsperre mit negativem Verbindungsversuch testen; loopback/IPC nur falls nötig | RF1-Inferenz und lokale SQL/Datei-/Skriptverarbeitung laufen ohne Netz; keine erfolgreichen externen Verbindungen. Keine Abhängigkeit von Download/Remote-API zur Laufzeit. |
| L2 Negativkontrollen | Remote-Endpunkt, fehlende Dateien, falsche Basismodellrevision, unbekannter Operationstyp, abweichender Adapterhash | Fail-closed oder dokumentierter lokaler Regel-Fallback; keine stille Cloud-Nutzung. |
| L3 Provenienz | Versionen und SHA-256 von Code, Basismodell, Tokenizer, Adapter, erlaubten Änderungsskripten und Datensatz; Quantisierung, Rank/Skala, Seed, Sampling, Runtime/GPU; separate Netzkonfiguration und tatsächliche Prozess-/GPU-Evidenz | Reproduzierbar nachvollziehbarer lokaler Betriebsweg; getrennte Artefakte, Rückkehr zur unveränderten Basis. Hashes belegen Integrität, nicht allein lokale Ausführung oder manipulationssichere Authentizität. |
| L4 A/B/C & Holdout | Gleiches synthetisches/öffentliches, rechtegeklärtes Dev-/Holdout-Manifest, eingefrorener Kandidat, blindes Holdout; P/R, Coverage, UNKNOWN, kritische Fehler, Review-Zeit, Laufzeit, Peak RAM/VRAM | Vorab definierter Nutzen gegenüber Regelbaseline/Modellkontrolle und keine kritische Regression; Prüfer getrennt von Auswahl; sonst NO_BENEFIT/NOT_RUN. |
| L5 Gateway | Synthetische Testbefehle prüfen; verbotene Felder, absichtliche Exportversuche, Schemafehler, unzulässige Operationen negativ testen; erlaubte synthetische Evidenz separat prüfen | Keine privaten Daten in externer Nachricht/Log; keine externe Aktion ohne menschliche Freigabe und lokale Validierung. |
| L6 Bericht | Quellstand, Hashes, anonymisierte Messwerte, Skript-/Konfigurationsversionen, tatsächliche Einschränkungen; ggf. kurze Offline-Demo | Dritte können Verfahren auf passender Hardware wiederholen; keine unberechtigte Weitergabe der Quelldokumente/Modelle, keine Behauptung universeller Datenschutzgarantie. |

Keine Messung des Stromverbrauchs behaupten, solange keine Messgeräte/Messmethode vorliegen; optional Laufzeit und Peak-RAM/VRAM als Ressourcenindikatoren, Energie nur bei tatsächlich gemessener Leistungsaufnahme. Kein Vorgriff auf Förderbeginn, keine neue Pflichtfunktion, kein zusätzlicher Kostenansatz.

## Parallelität und Kosten

M1–M3: bestehende Pflichtarbeit (Baseline, Datensatz, Regeln, Fehlermuster). M4: genau eine RF1-Fehlerklasse parallel zur weiteren FormBridge-Entwicklung; max. 30 h in 950 h oder 15 h in 850 h einschließlich Offline-Test und Evaluation. M5/M6: nur freigegebene Ergebnisse in bestehendem Integrations-/Berichtsaufwand übernehmen/veröffentlichen. Kein zusätzlicher Forschungsblock. Allgemeine Gewichtsraum-/MindLoop-/Hypernetz- und etwaige externe GPU-Forschung im separaten Research Lab, getrennte Zeiten und Finanzen; keine FormBridge-Cloud-Referenzläufe, keine Doppelförderung. Nicht vor bewilligtem Förderbeginn implementieren.

Quellen: [RF1-Ergänzungsblatt](lora-research-extension-2026-11-19.md), [Monatsplan](six-month-development-plan.md), [Prototype Fund KI-Richtlinien](https://www.prototypefund.de/blog/ki-beim-prototype-fund), [FAQ](https://www.prototypefund.de/faq).