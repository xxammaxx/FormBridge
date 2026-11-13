# Review B — Adversarial Audit RepairProbe (unabhängig)

**Reviewer:** separater Agent-Prozess mit Auftrag „widerlege die Innovations- und Förderargumente von RepairProbe"; alle RepairProbe-Quellen selbstständig neu abgerufen und verbatim verifiziert; PTF-Kriterien von prototypefund.de gezogen; Websuche nach Konkurrenz.
**Datum:** 13.11.2026 · **Datenschutz:** nur öffentliche Quellen; privates Repo/Portal-Entwurf nicht einsehbar.

> **Korrektur-Marker (13.11.2026, Runde 3):** Die im Dokument genannte „44-Test-Baseline" ist öffentlich nicht eindeutig. `technical-baseline.html` nennt 44, `llms.txt` nennt 24 (gleicher Commit). Das private Repo ist nicht einsehbar. Der aktuelle Vergleich verwendet **„24–44, nicht unabhängig verifiziert"**. Der Befund „Baseline vorhanden" bleibt, die exakte Zahl nicht.

## Angriffsvektoren → Urteile → Restrisiko

| # | Vektor | Urteil | Restrisiko |
|---|---|---|---|
| 1 | Existierende Konkurrenz | **SUPPORTED** — iFixit FixBot (09.12.2025, Stimme+Vision, 125k Anleitungen: https://www.ifixit.com/News/114700/introducing-fixbot); NORA (deutscher Repair-Café-KI-Assistent, 23.03.2026: https://repaircafe-groebenzell.de/blog/ki-im-repair-cafe/); AugRep/GYVA (DBU-gefördert, Live-Pilot Freiburg ab 17.10.2026: https://www.dbu.de/projektdatenbank/41431-01/); **RepairVision** (Hackathon 08.10.2026, „provisional labels" + modellunabhängiger Hazard-Screen = exaktes Differenzierungsmerkmal: https://dev.to/priyansh_narang_c1b96ab75/repairvision-an-intelligent-repair-cafe-platform-for-multimodal-fault-diagnosis-and-sustainable-4jm2). YProbe/ARBoard/PCBSpot und ORDS/ORA sind **nicht im Detail geprüft** und werden nicht als belegte direkte Konkurrenz gewertet. PTF-Jury-Kriterium fragt wörtlich nach „ähnlichem FOSS-Produkt" — Antwort: ja | **HIGH** |
| 2 | Technische Neuheit | **SUPPORTED (Angriff steht)** — Provenienz-getrennte Evidenzklassen etabliert (FTA/FMEA, Case-Based Reasoning; DML–LLM-Hybrid-FDD 2026: auditable Provenienz 96 %, LLM-Output initiiert nie Aktionen); neu ist nur die FOSS-Verpackung für Konsumentenreparatur | **HIGH** |
| 3 | KI-Abhängigkeit | SUPPORTED — externe multimodale API vs. Datensparsamkeit + wlanarme Cafés; lokale Qualitäts-VLM solo in 6 Monaten unrealistisch; PTF-Blog „Public Money, Public AI?" zeigt Sensibilität. Steelman: KI-optionaler Offline-Kern | MED |
| 4 | Praktische Umsetzbarkeit | WEAK — getrimmter Scope, öffentlich dokumentierte Baseline (24–44 Tests, widersprüchlich); Engpässe: Quellen-Copyright M4, Evaluationsdesign M6 | MED |
| 5 | Zielgruppe & Nutzen | **SUPPORTED** — **entscheidend**: einzige Rückmeldung (n=1) berichtet verlorenen Reparaturkontext als *selten* und nennt Leiden (Infosuche, Teile, Zugang), die FixBot/Teilemärkte bereits bedienen; keine Pilotpartner; Netzwerk-Reparatur-KI-Diskurs läuft ohne RepairProbe | **HIGH** |
| 6 | Open-Source-Wirkung | WEAK — FOSS-Veröffentlichung erst 1 Monat nach Förderbeginn nötig; aber privates Repo macht „eigene Vorarbeiten" für die Jury unverifizierbar (bewertetes Kriterium) — FormBridge gewinnt diesen Vergleich | LOW formal / MED Glaubwürdigkeit |

> **Korrektur-Marker (13.11.2026, Revalidierung):** Die Aussage „FOSS-Veröffentlichung erst 1 Monat nach Förderbeginn" konnte in **keiner** aktuellen Primärquelle bestätigt werden und ist als **CONTRADICTED/UNVERIFIED** einzustufen. Aktuelle Primärquellen: FAQ Förderung 06 („Veröffentlichung des Codes in einem offen zugänglichen Repository **zum Projektabschluss**") und RL (Ergebnisse „auf Open-Source-Plattformen … unter offener Lizenz bereitgestellt"). Vektor 6 bleibt im Kern (privates Repo → Jury kann Vorarbeiten nicht verifizieren) gültig; das zeitliche Detail wird gestrichen. Siehe funding-rules-verified-2026.md §W5.
| 7 | Antragsqualität | UNRESOLVED — Jury-Proben: Abgrenzung, Foto→KI-Datenfluss, Quellenrechte, Adoption/Pflege, KI-Eval-Metriken, Linien-Passung, ORDS-Duplizierung | MED |
| 8 | Sicherheit/Haftung | WEAK — beratende FOSS ist keine regulierte Klasse; Blockier-Gates defensiv; Risiko nur bei Überbehauptung des „Sicherheitsmodells" | MED |

## Gesamteinschätzung des Reviewers

Am wahrscheinlichsten killen die Bewerbung **Doppelstrukturen/Innovationsgrad** (konvergierende Idee, mehrere aktive FOSS-/Near-FOSS-Rivalen, etablierte Methodik), verstärkt durch **Bedarfsevidenz, die den Schmerzpunkt widerspricht**, und argumentabler **Linien-Passung** (Reparatur-App ≠ Datensicherheit/Infrastruktur). Gegen FormBridge auf derselben Linie verliert RepairProbe bei Novelty, Verifizierbarkeit, Bedarfsevidenz und Reichweite; Ehrlichkeit und Test-Disziplin mildern das Glaubwürdigkeitsrisiko, nicht das Konkurrenzdefizit.

## Umsetzung im Entscheidungsprozess

Bestätigt die konservative Erstbewertung; Nachjustierungen: K1 4,5→4,0, K2 7,0→6,0, K3 7,0→6,5, K4 6,0→5,5, K5 6,0→5,5 (siehe scoring-matrix.md). Diese Entscheidung sagt nichts über RepairProbe-Eignung für andere Programme (z. B. reparaturspezifische Töpfe); der Portal-Entwurf bleibt unangetastet.
