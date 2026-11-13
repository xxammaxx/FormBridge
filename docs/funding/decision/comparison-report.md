# Vergleichsbericht & Förderentscheid: FormBridge vs. RepairProbe

**Datum:** 13.11.2026 · **Auftrag:** Auswahl **genau eines** Projekts für die Prototype-Fund-Bewerbung, Jahrgang 03, Förderlinie Innovation (Frist 30.11.2026, 15:00 CET)
**Verfahren:** gleiche Kriterien für beide Projekte · gewichtete Matrix + Sensitivitätsanalyse · zwei unabhängige adversarial Reviews ([A](review-A-formbridge.md), [B](review-B-repairprobe.md)) · Quellen: [sources-evidence.md](sources-evidence.md)
**Vertraulichkeit:** Dieser Bericht enthält nur öffentlich verifizierbare RepairProbe-Informationen (das private Haupt-Repo und der Portal-Entwurf wurden nicht eingesehen/zitiert).
**Instrument-Hinweis:** Die Zahlen sind ein strukturiertes Entscheidungsinstrument — **keine** Förderwahrscheinlichkeiten.

## 1. Entscheidung (Ergebnis)

**FORMBRIDGE** — siehe §6. Die Rangfolge ist in allen vier Sensitivitätsszenarien stabil. RepairProbe bleibt vollständig unverändert; der dortige Portal-Entwurf wird nicht angetastet.

## 2. Offizielle Förderbedingungen (Kurzfassung, Details in sources-evidence.md)

| Bedingung | Status |
|---|---|
| Frist 30.11.2026, 15:00 MEZ; Linien Innovation/Resilienz/Up and Coming | VERIFIED (bewerben.prototypefund.de) |
| Innovation = Datensicherheit + **Software-Infrastruktur**; „neues Modul für bestehende Software" ausdrücklich innovativ | VERIFIED (prototypefund.de/innovation, /innovativ) |
| Bestandsprojekte zulässig bei klarer Abgrenzung; „Verbesserung bestehender Software" nicht ausreichend; hoher Entwicklungsanteil (kein Docs/Marketing-only) | VERIFIED (Handbuch 2026, /bewerbung/details) |
| FOSS-Lizenz Pflicht; 47.500 € solo / 95.000 € Team; 01.06.–30.11.2027 | VERIFIED |
| Antragsberechtigung (18+, Wohnsitz DE solo; Team-GbR) | VERIFIED (Kriterien) / **UNKNOWN** (persönliche Situation — Owner-Prüfung) |
| Eigenanteil ≥ 5 % | INTERPRETATION (aus eigener Vor-Recherche; im Handbuch-Extrakt nicht direkt belegt — Portal-Check) |
| Mehrfachbewerbung: zwei Anträge einer Person im deutschen PTF | **UNKNOWN / OFFEN** (eigene Vor-Recherche: nur Schweizer-FAQ vorhanden, nicht übertragbar) → PTF-Team schriftlich klären |

## 3. Kriterienanalyse A–F (Kurzfassung; Belege in Matrix + Reviews)

**A. Innovationshöhe:** FormBridge: korpus-falsifizierte enge Lücke (13 Projekte, Quellcode-Ebene) + neu entdeckter amtlicher XSD-Defekt (170 Fehler, unabhängig reproduziert); Risiko: Trivialitäts-Wahrnehmung ohne Code (Review A: HIGH). RepairProbe: **kein** Prior-Art-Audit vorhanden; Review B fand mindestens vier aktive Konkurrenten, davon RepairVision mit demselben Differenzierungsmerkmal („provisorische Labels"); Evidenz-Trennung ist etablierte Methodik (FTA/FMEA, CBR).

**B. Gesellschaftlicher Nutzen:** FormBridge: Medienbruch-Abbau (D21 eGov-Monitor 2026: 50 % offline / 24 % Medienbruch) — breit, aber indirekt und unbezahlt an Nutzentests. RepairProbe: konkrete Gruppe (Repair-Cafés), Nachhaltigkeitsnarrativ — aber die einzige explorative Rückmeldung (n=1) **widerspricht** dem angenommenen Schmerzpunkt (verlorener Reparaturkontext = selten; eigentliche Leiden: Infosuche, Teile, Zugang — von FixBot/Teilemärkten bedient).

**C. Technische Machbarkeit:** FormBridge: messbarer 6-Monatsplan mit Abnahmekriterien; Risiko: Detektions-/Adaptierbarkeits-Scope (Lizenzrisiko durch Born-digital-Scope entschärft — Review A: REFUTED). RepairProbe: existierende 44-Test-Python-Baseline (echter Startvorteil); aber KI-Qualität/Bildverständnis laut eigenem README **unbewiesen**; monatliche Engpässe (Quellenrechte M4, Evaluationsdesign M6).

**D. Open-Source-Wirkung:** FormBridge: infrastrukturell (CLI/Bibliothek/Verifier) angelegt, öffentliches Repo, Lizenz offen (Owner-Entscheidung). RepairProbe: Apache-2.0 fixiert, aber Hauptcode **privat** — „eigene Vorarbeiten" für die Jury nicht verifizierbar (PTF-Kriterium, Review B: MED).

**E. Förderrechtliche Abgrenzung:** FormBridge: explizite A/B/C-Grenze mit Verbotensliste; Lehrbuch-Passung zur Linie („neues Modul", Infrastruktur). RepairProbe: Endnutzer-Werkzeug — Passung zur Linie argumentabel, aber schwächer (Review B); FOSS-Veröffentlichung des bisher Privaten nötig.

**F. Bewerbung & Evidenz:** FormBridge: vollständiger Bewerbungsentwurf + Evidenzkette im Repo, **noch nicht im Portal**; Review A fordert 3 Ergänzungen (§6). RepairProbe: 850-Stunden-Entwurf im Portal (Draft) — **Qualität für diese Prüfung nicht einsehbar** (UNKNOWN); öffentliche Kommunikation stark und ehrlich.

## 4. Bewertungsmatrix (Nach-Review-Stand)

Punkte 0–10 je Kriterium; Erstbewertung vor Reviews, symmetrische Nachjustierung nach Reviews mit Dokumentation jeder Änderung — Details und Berechnungen: [scoring-matrix.md](scoring-matrix.md).

| Kriterium | Gew. | FormBridge | RepairProbe |
|---|---|---|---|
| Innovationshöhe & Abgrenzbarkeit | 25 % | **6,5** | 4,0 |
| Gesellschaftlicher Nutzen | 20 % | **6,5** | 6,0 |
| Technische Machbarkeit | 20 % | **6,5** | 6,5 |
| Open-Source-Wiederverwendbarkeit | 15 % | **6,5** | 5,5 |
| Förderfähigkeit & rechtliche Risiken | 15 % | **8,0** | 5,5 |
| Bewerbung & Evidenz | 5 % | **6,5** | 6,0 |
| **Weighted Total** | 100 % | **6,725** | **5,45** |

Änderungen gegen Erstbewertung (dokumentiert): FB K1 7,0→6,5 (Trivialitäts-Risiko HIGH), K3 6,0→6,5 (Lizenz-Risiko REFUTED), K4 7,0→6,5, K6 7,0→6,5 · RP K1 4,5→4,0 (Konkurrenz inkl. RepairVision-UBS), K2 7,0→6,0 (n=1 widerspricht Bedarf), K3 7,0→6,5 (KI unbewiesen), K4 6,0→5,5 (privates Repo), K5 6,0→5,5 (Linien-Passung).

## 5. Sensitivitätsanalyse (Nach-Review-Scores)

| Szenario (Gewichtsverschiebung) | FormBridge | RepairProbe | Rangfolge |
|---|---|---|---|
| Basis | **6,725** | 5,45 | FB |
| S1 Innovation 40 % | **6,68** | 5,16 | FB (Abstand ↑) |
| S2 Nutzen 35 % | **6,68** | 5,56 | FB (Abstand ↓) |
| S3 Technisches Risiko 35 % | **6,695** | 5,66 | FB (kleinster Abstand) |
| S4 Streng gegen unbelegte Aussagen | **6,725** | 5,325 | FB (Abstand ↑↑) |

**Befund:** Die Rangfolge ist in allen Szenarien stabil. Der kleinste Abstand (S3) zeigt: bewertet eine Jury „existierende Baseline + reale Nutzergruppe" deutlich höher als Evidenz-Disziplin, wird es knapp — eine Umkehr liegt im gewählten Raster aber nicht mehr; eine echte Umkehrwahrscheinlichkeit kann mit diesem Instrument nicht angegeben werden.

## 6. Begründung der Empfehlung

1. **Warum FormBridge die bessere Bewerbung ist:** Der einzige belegte Unterschied auf dem entscheidenden Kriterium (Innovationshöhe, 25 %) ist die **Evidenzqualität**: FormBridge-Behauptungen wurden aktiv falsifiziert (13-Repos-Audit, unabhängig reproduzierter XSD-Defekt-Befund), RepairProbe-Novelty ist ungeprüft und durch aktive Konkurrenz (iFixit FixBot, NORA, AugRep/GYVA Live-Pilot, RepairVision mit identischem USP) belastet. Dazu kommt die explizite Linien-Passung („Software-Infrastruktur", „neues Modul") — bei RepairProbe argumentabel, aber schwächer.
2. **Entscheidende Stärken:** reproduzierbare Referenzfall-Evidenzkette; messbare Abnahmekriterien; saubere Fördergrenze ( öffentlich, auditierbar); Bewerbungsentwurf + Review-basierte Ergänzungsliste liegen fertig vor.
3. **Verbleibende Schwächen (FormBridge):** kein Code (Trivialitäts-Risiko), eine Referenz-PDF-Basis mit ungeklärter `copy:no`-Rechtslage, kein Held-out-Dokument beschafft, Lizenz unentschieden, Adaptierbarkeit nur schwach belegt.
4. **Wahrscheinliche Jury-Einwände:** „Das ist pdftotext+Regeln+xmllint" (→ RF-Messlogik + Reproduktions-Demo im Antragstext adressieren); „wofür XSD, wenn JSON-Schemata/Konverter existieren" (→ benannte Verbraucher/Toolchain-Argumentation); „nur ein PDF, nur ein Bundesland" (→ Held-out-PDF beschaffen); „wo ist der Code?" (→ Evidenz-Demo + Grenze Vorarbeit/Förderarbeit klar erzählen).
5. **Realistisch bis zur Frist (17 Tage):** (a) PTF-Team-Anfrage zur Mehrfachbewerbung + Eigenanteil-Check, (b) Held-out-Wohngeld-PDF (anderes Bundesland) herunterladen + Rechte prüfen, (c) Bewerbungstext um RF-Messabsatz + KI-/Document-AI-Abgrenzung + XSD-Verbraucherargument erweitern, (d) Lizenzentscheidung treffen, (e) Portal-Eintragung. Ein Mini-PoC ist **optional** — er würde Trivialitätsrisiko senken, aber Vorarbeit schaffen, die vom Förderumfang abgezogen werden muss (Owner-Entscheidung, siehe [owner-decisions.md](owner-decisions.md)).

## 7. RepairProbe — Achtung vor Fehlschluss

Diese Entscheidung sagt **nicht**, RepairProbe sei ein schwaches Projekt: Es hat die reifste Antragslage (Portal-Draft), eine existierende getestete Baseline und ehrliche, kriterienbewusste Öffentlichkeitsarbeit. Es verliert hier spezifisch auf der **Innovation-Linie** gegen den Jury-Kriterienkatalog (Novelty unbelegt + aktive Konkurrenz + Bedarfsevidenz widersprechend + Linien-Passung). Für andere Programme (NLnet ist wegen GenAI-Policy kritisch; Reparatur-spezifische Fördertöpfe wie DBU-Kontext) bleibt es ein legitimer Kandidat — ohne dass dieser Bericht dafür eine Aussage trifft.

## 8. Widersprüche zwischen den Reviews

Keine direkten Widersprüche in den Faktenbefunden (A: FormBridge-Kern hält, 3 Bedingungen; B: RepairProbe-Konkurrenz/Bedarf/Pasung schwach). Unterschiedlich gewichtete Rest-Risiken: A stuft „kein Code" als MED ein (produzierbar durch RF-Narrativ), B stuft „privates Repo" als MED ein (formal LOW) — beide betreffen F-und-D-Kriterien und sind in der Matrix je Seite gleich behandelt.
