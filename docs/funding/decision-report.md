# Entscheidungsbericht Feldexa 2.0 / FormBridge → Prototype Fund 2027 (Jahrgang 03, Innovation)

**Datum:** 13.11.2026 · **Bezug:** Issue #167 · Basis: `../research/prior-art-audit.md`, `../research/innovation-assessment.md`, `../research/reference-case-wohngeld.md`, `../research/technical-specification.md`, `prototype-fund-feasibility.md`, [Vergleichsbericht](decision/comparison-report.md)

> **Namensabgrenzung:** „Feldexa 2.0" ist die Produktanwendung; „FormBridge" ist das eigenständige, förderfähige Infrastrukturmodul im Feldexa-Kontext (siehe [project-boundary.md](project-boundary.md)). Dieser Bericht empfiehlt **FormBridge als Fördergegenstand**; die Entscheidung über F1 (Produkt), F2 (ProofLayer), F3 (FormBridge) oder RepairProbe trifft der Owner.

## Empfehlung: **CONDITIONAL_GO für FormBridge (F3) als Fördergegenstand**

FormBridge (eng gefasst, als app-unabhängiges Infrastrukturmodul) ist nach Quellcode-Audit und Referenzfall-Validierung eine **tragfähige, abrechnungsehrliche** Bewerbungshypothese für die Förderlinie Innovation (Frist 30.11.2026, 15:00 CET). Die GO gilt unter den Bedingungen B1–B6 unten; solange sie offen sind, ist der Status **conditional**, nicht go. **Das ist keine Entscheidung für den Owner und keine Förderzusage.**

## Evidenz in Kürze

1. **Kein geprüftes OSS-Projekt** implementiert die Kette statisches Behörden-PDF → versionierte FIM-Datenfeld-IDs mit Koordinaten, Confidence/UNKNOWN, Human-Gate, Provenienz und Validierung (13 Repos geprüft; die beiden kritischen deutschen Projekte KIWO und Formularagent erstmals im Quellcode, nicht nur nach Beschreibung).
2. **Die Lücke ist Ökosystem-dokumentiert:** FITKO dokumentiert den XDF-Konvertierungspfad als „in der Konzeption" (docs.fitko.de, 13.11.2026). **Nachtrag 13.11.2026:** Das FIM-Portal betreibt inzwischen einen Datenschema-Konverter (XDF2/XDF3 ↔ JSON Schema/XSD) und einen XDF-XSD-Konverter; er repariert aber nicht das veröffentlichte defekte S00000159-XSD und liefert keine PDF→FIM-Zuordnung. RF2 ist daher „Reparatur veröffentlichter defekter XSDs", nicht „Konvertierung fehlt".
3. **Neu entdecktes, belegbares Problem:** Das offizielle immutable XSD S00000159v1.4 ist standardkonform nicht kompilierbar (170 Parser-Fehler, libxml2/xmllint); Reparatur + Instanz-Validierung im Repo dokumentiert — Substanz für RF2 und für Ökosystem-Nutzen.
4. **Referenzfall real:** Fürth-PDF (Hash, 8 Seiten, Textlage) ↔ FIM-Schema: nur 7/30 Referenzfelder trivial mappbar; 7 Kontext-Mehrdeutigkeiten, 4 Codelisten, 4 Strukturtransformationen, 3 fachliche Deckungslücken (u. a. Vermieter-Identität nicht repräsentierbar) — die Forschungsfragen sind real, nicht konstruiert.
5. **Förderpassung verifiziert:** Innovation erlaubt ausdrücklich „neues Modul für bestehende Software"; Bestandsprojekte zulässig bei klarer Abgrenzung; hoher Entwicklungsanteil; FOSS-Pflicht — alles offiziell belegt.

## Bedingungen (B1–B6) für echtes GO

| # | Bedingung | Fälligkeit |
|---|---|---|
| B1 | **Formale Klärung Antragsteller** (Einzelperson Wohnsitz DE / Team-GbR) + Portal-Check aktueller Kriterien + Teilnahme an Sprechstunde 16.11.2026 | vor Einreichung |
| B2 | **Entscheid Feldexa-Fassung (F1/F2/F3) vs. RepairProbe bestätigen** für genau eine Bewerbung (RepairProbe bleibt unverändert; Vergleich: docs/funding/decision/comparison-report.md, bedingte Empfehlung F3) | vor Einreichung |
| B3 | **Modul-Repo-Isolierung beschließen** (eigenes Repo/Lizenz; kein Produktcode im Förderumfang; bis Förderbeginn keine Modul-Implementierung, um Vorab-Leistungs-Problematik zu vermeiden) | vor Einreichung |
| B4 | **Falsifikations-Fortlauf:** Suche nach konkurrierenden Projekten (incl. FITKO-Announcements) bis Abgabedatum; bei fundierter Widerlegung → PIVOT (Alternative: Schema-Hygiene-Tool + Provenienzformat als schmaleres Vorhaben) | bis 30.11.2026 |
| B5 | **De-Overclaim-Pass auf Bewerbungstext** (keine universalen Negativbehauptungen; Nutzenkette nicht über das Modul hinaus) | vor Einreichung — in Revisionsstufe 2 (13.11.2026) vorab umgesetzt, vor Einreichung final prüfen |
| B6 | **Kein Zirkel-Evaluationsszenario:** Held-out-Dokument (andere Landes-Variante) + externe Testpersonen für RF4 in Spec §6/§7 verankert | vor Einreichung — in Revisionsstufe 2 verankert; konkrete Beschaffung des Held-out-PDFs klären |

## Unbeantwortete Fragen (ehrlich offen)

- Jury-Perspektive auf Verwaltungs-Infrastruktur (keine Quelle; Risikominderung über Bürger-Nutzen-Erzählung).
- Genauigkeit der Codelisten-Zuordnungen fachlich (FIM-Portal-Referenzcheck steht aus — Modul-Arbeit, nicht Recherche-Rest).
- Ob weitere amtliche XSDs dieselben Defektklassen zeigen (RF2-Korpus erst im Förderzeitraum).
- Feldexa-Produkt-E2E-Pilot (#165) bleibt NOT_RUN bis separate Freigabe; nicht Bedingung dieser Bewerbung, aber wertvoller Messlieferant.

## Nächste Aktionen (konkret)

1. B1–B3 durch Maintainer entscheiden (keine Agentur-Aktion möglich).
2. Falls GO bestätigt: Bewerbungsbausteine ([application-draft-de.md](application-draft-de.md)) finalisieren und um Review-A-Ergänzungen (RF-Messabsatz, Document-AI-Abgrenzung, XSD-Verbraucherargument, Held-out-PDF) erweitern, Portal-Felder ausfüllen, Audit-Matrix als Anhang exportieren; Voraussetzungen A1–A6 siehe [decision/owner-decisions.md](decision/owner-decisions.md); Einreichung vor 30.11.2026 15:00 CET.
3. Issue #165 (Produkt-Pilot) bleibt separat; Issue #151/#167-Verweise pflegen.
4. Falls PIVOT/NO_GO: Schema-Hygiene + Provenienzformat als eigenständige, kleinere FOSS-Beitragsoption dokumentieren (keine Förderabhängigkeit).

## Was diese Empfehlung NICHT ist

Keine Förderzusage, keine Erfolgsprognose, keine Freigabe von Implementierung oder Produktaufgaben, kein Merge. Proposal PR bleibt Draft.

---

**Herkunft (Provenienz):** Ursprünglich erstellt am 13.11.2026 im Repository [`xxammaxx/Feldexa_2.0`](https://github.com/xxammaxx/Feldexa_2.0) — Branch `docs/research-167-prior-art-audit`, Commit `cb122fe2f96a8f5cbde2f075e0b6529342caf676`, Draft-PR [#168](https://github.com/xxammaxx/Feldexa_2.0/pull/168). Am 13.11.2026 in dieses unabhängige FormBridge-Repository migriert; Umfang der Anpassungen: siehe [project-boundary.md](project-boundary.md#e-provenienz-der-migrierten-dokumente) §E (Pfade/Namen, Redistribuierungs-Filter, Grenzdokumentation — keine Änderung von Forschungsergebnissen).