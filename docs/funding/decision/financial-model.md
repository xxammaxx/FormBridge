# Finanzmodell v3 — Kostenrechnung und Finanzierung getrennt (Revalidierungsrunde 2)

**Datum:** 13.11.2026 · **Revision 3** (v1: Ursprungsmodell — fehlerhaft, Finanzierungsidentität verletzt; v2: Identitätskorrektur; v3: + Second-Stage-Rahmen, De-minimis-Wirkung, AZK-Anker, Ratenhebel — nach Reviews A2/B2) · **Alle Zahlen exakte Dezimalarithmetik, 2 Nachkommastellen, maschinell getestet (Test-Protokoll in validation-report.md §V3).**
**RL-Zitate:** konsolidierte Fassung der RL 2024 (BAnz AT 15.11.2024 B4) per Änderungs-Bekanntmachungen vom 01.12.2025 und 25.06.2026; **Nr. 5 (Zuwendungshöhe/-quote) durch beide Änderungen unberührt** (Review B2, K8c).

## 0. Der korrigierte Rahmen

**Kostenrechnung (AZK-Kostenbasis):**
```
Gesamtkosten G = Personalkosten PK + Gemeinkosten GK
mit PK = Stunden × Stundensatz;  GK ≤ 5 % × PK (FAQ-Pauschale)
Grenze: G ≤ 50.000 € (RL Nr. 5); PK ≤ 950 h × 50 € (Handbuch Frage 14)
```

**Finanzierung:**
```
G = Förderung F + Eigenanteil EA
mit F ≤ 95 % × G (RL Nr. 5; FAQ Förderung 02)  ⇒  EA ≥ 5 % × G
```

**Regel:** Förderung und Eigenanteil sind **Finanzierungsanteile der tatsächlich ausgewiesenen Kosten**. Ein Eigenanteil darf nicht auf ein Budget addiert werden, für das keine Kostenposition existiert. (Dies war der Fehler der alten Modell-A-Darstellung; siehe §Fehlerprotokoll.)

## 1. Die offizielle Kommunikationslogik vs. die strenge Regellogik (W2, geschärft)

| | FAQ-/Portal-Kommunikation | Strenge RL-Regellogik |
|---|---|---|
| „Maximalfördersumme 47.500 €" | entspricht „950 h × 50 €" (FAQ Förderung 01, wörtlich) | erfordert G = 50.000 € (95 %-Quote) → benötigt PK + GK = 50.000 € |
| GK | „pauschal 5 % der Personalkosten" (= 2.375 € bei 950 h) | RL: Bemessungsgrundlage PK+GK, „bis zu 95 %" |
| Team-Konsistenz-Beleg | FAQ-Teamzahl 95.000 € = 0,95 × 100.000 € (RL-Gesamtkosten-Cap Teams) — **bestätigt den 95-%-Frame der Kommunikation** |
| Kompatibel? | **Nur wenn** GK = 2.500 € (5 % von 50.000) oder als vereinfachte Kommunikation ohne GK-Zählung | ja, ergibt **47.381,25 €** max. Förderung (bei 950 h + GK-Pauschale) |

**Befund:** Die FAQ-Formulierung („Maximalfördersumme = 950 h × 50 €") und die strenge 95-%-Regellogik (95 % × (PK+GK)) sind **nicht gleichzeitig exakt erfüllbar**, wenn GK strikt = 5 % × PK gilt. Differenz: 118,75 €. Dies ist eine **unauflösbare Mehrdeutigkeit der öffentlichen Quellen** → Szenario E bildet die PTF-Kommunikationslogik separat ab; für die Antragsempfehlung gilt die konservative strenge Logik (L1). Klärung: Portal/Antragswerkstatt (remaining-questions.md Q3).

**Stützbeleg für die Kommunikationslogik (Review A2, M6):** Auch die Second-Stage-Zahlen folgen keiner einzelnen strengen Formel — 31.667 € ≙ „gerundet 633 h" (633 × 50 = 31.650,00) bzw. 0,95 × 33.337 = 31.670,15 (RL-Pfad): PTF kommuniziert **gerundete, planungsorientierte Maximalwerte**, keine exakte Formel-Ausgabe. Das stützt die Lesart, dass „47.500 €" als Kommunikations-Deckel und die strenge Rechnung als verbindliche Abrechnungslogik parallel existieren (Q3).

## 2. Szenarien (95 %-Quote, Stundensatz 50 €, GK-Pauschale 5 % der PK — sofern genutzt)

### Szenario A — 950 h ohne Gemeinkosten
```
PK = 950 × 50        = 47.500,00 €
G  = PK              = 47.500,00 €   (Cap 50.000 ✓)
F  = 0,95 × G        = 45.125,00 €   ← NICHT 47.500 €
EA = G − F           =  2.375,00 €
```

### Szenario B — 950 h mit 5 % Gemeinkosten
```
PK = 47.500,00 €;  GK = 0,05 × PK = 2.375,00 €
G  = 49.875,00 €                     (Cap 50.000 ✓, nicht ausgeschöpft)
F  = 0,95 × G        = 47.381,25 €   ← praktisches Maximum unter strenger Logik
EA = G − F           =  2.493,75 €
```

### Szenario C — Gesamtkosten exakt 50.000 € mit GK = 5 % × PK

**Bei exakt 50 €/h: nicht konstruierbar.**
```
1,05 × PK = 50.000 ⇒ PK = 47.619,05 € ⇒ 952,38 h  > 950-h-Obergrenze
```
**Mit Ratenhebel (FAQ-Support): konstruierbar.** FAQ Förderung 01 erlaubt einen **höheren Stundensatz bei Rechnungs-Nachweis** höherer Stundenlöhne (50-€-Cap gilt nur für die Second Stage). Bedingung für G = 50.000 € innerhalb von 950 h:
```
1,05 × (950 × R) ≤ 50.000  ⇒  R ≤ 50,13 €/h  (genau: 50,1256 €/h)
Beispiel R = 50,10 €/h: PK = 950 × 50,10 = 47.595,00 €; GK = 2.379,75 €;
G = 49.974,75 € ≤ 50.000 ✓; F = 0,95 × G = 47.476,01 €; EA = 2.498,74 €
```
Das heißt: Die 50.000-€-Grenze **bindet unter Standard-Satz 50 €/h nie** (950 h → max. G 49.875 €), sie wird erst mit nachgewiesen höheren Sätzen relevant (ab ~50,13 €/h). Ob das Portal die GK-Pauschale in dieser Struktur abbildet, bleibt Q3.

### Szenario D — reduzierter Stundenumfang (mit GK-Pauschale; ohne GK in Klammern)

| Stunden | PK | GK (5 %) | G | F = 95 % × G | EA = 5 % × G |
|---|---|---|---|---|---|
| 700 | 35.000,00 | 1.750,00 | 36.750,00 | **34.912,50** | 1.837,50 |
| 800 | 40.000,00 | 2.000,00 | 42.000,00 | **39.900,00** | 2.100,00 |
| 850 | 42.500,00 | 2.125,00 | 44.625,00 | **42.393,75** | 2.231,25 |
| 950 | 47.500,00 | 2.375,00 | 49.875,00 | **47.381,25** | 2.493,75 |

(Ohne GK-Pauschale: F = 0,95 × PK = 33.250,00 / 38.000,00 / 40.375,00 / 45.125,00.)

### Szenario E — PTF-Kommunikationslogik (FAQ-Lesart, separat ausgewiesen)

```
F = min(950 h × Stundensatz, 47.500 €)   — FAQ formuliert die Höchstförderung direkt aus Stunden × Satz
Konsistente Kostenbasis dafür: G = 50.000 € (dann EA = 2.500 €)
Offen: ob das Portal GK-Pauschale (2.375 €) innerhalb dieser 50.000 € abbucht oder die
Kommunikation vereinfacht. → Nur im Portal/Antragswerkstatt klärbar (Q3).
Risiko bei Planung nach E: falls das Portal streng rechnet (L1), liegt das Maximum bei 47.381,25 €;
eine Antragsplanung mit 950 h bleibt zulässig, die Förderhöhe wäre dann 47.381,25 €.
```

### Szenario F — Teilzeit/Anstellung (Arbeitsschutz-Obergrenze)

Bei parallel bestehender Teilzeit-Anstellung begrenzen Arbeitsschutzgesetze die Gesamtstunden nach oben (FAQ Förderung 01). Beispiel: 40-h-Anstellung (80 %) ⇒ projektplanbar ≤ 8 h/Woche ≈ 200 h/6 M. → F (mit GK) = 0,95 × (200×50×1,05) = **9.975,00 €**. Formal zulässig, aber unter der ~250-h-Verwaltungsgrenze (Handbuch: darunter „lohnt der administrative Aufwand nicht") → praktisch ungeeignet.

### Szenario G — Second Stage (nur bei initialer Bewerbung mitbeantragt)

Vier Rahmen für die kommunizierten 31.667 € (alle öffentlich dokumentiert; W4):

| Frame | Rechnung | Wert |
|---|---|---|
| FAQ-Kommunikation | „bis zu 31.667 € beantragen … entspricht gerundet 633 Arbeitsstunden mit einem Stundensatz von 50 €" | 31.667 € (kommuniziert) |
| Stunden × Satz | 633 × 50 | 31.650,00 € |
| RL-95-%-Pfad | 0,95 × 33.337 € (RL Nr. 5, zweite Förderphase) | 31.670,15 € |
| Anteil-Frame | 47.500 × 4/6 | 31.666,67 € |

Konservative Planung: **31.650,00 €** (633 h à 50 €). **Keine Code-Meilensteine** in der Second Stage förderfähig (Handbuch Frage 16); 50-€-Cap gilt; Stunden ≤ Anteil der regulären Phase. Klärung der exakten Portal-Berechnung: Q3-Erweiterung.

### Szenario H — De-minimis-Obergrenze (kann die Förderhöhe DECKELN)

RL Nr. 5 + Anlage Nr. 1: Zuwendung ist **De-minimis-Beihilfe**; Freibetrag **300.000 € innerhalb von 3 Jahren** (Kalenderjahre) über alle Beihilfen, die eine „eine Unternehmereinheit" bildenden Struktur kumuliert wurden; **Kumulierungsverbot** (keine Überkompensation); De-minimis-Erklärung ist Teil der Bewilligungsunterlagen (FAQ Auswahl 03).

```
Verfügbare F-Obergrenze = min(F_Szenario, 300.000 − Summe anderer De-minimis-Beihilfen der letzten 3 Jahre)
```
Für Erst-Antragsteller ohne sonstige Beihilfen ist das nicht bindend; mit vorhandenen Beihilfen (z. B. andere Zuschüsse) **kann F unter 47.381,25 €/47.500 € gedrückt werden** — individuell zu prüfen (Owner, Q-Erweiterung). Aufbewahrung der Erklärungen 10 Jahre (Buchungspflicht AZK/Anlage).

### Zuwendungsfähige Kosten (AZK-Anker)

Gefördert wird auf **Kostenbasis (AZK)**: „Richtlinien für Zuwendungsanträge auf Kostenbasis" (Vordruck 0047) nebst Merkblatt **Vorkalkulation** regeln, welche Kosten zuwendungsfähig sind (RL Nr. 5/6-Verweise). Inhaltlich bestätigt durch FAQ Förderung 02: **Personalkosten** (Stunden × bewilligter Satz) + **Gemeinkosten-Pauschale bis 5 % der Personalkosten**; weitere Kostenpositionen nennt keine öffentliche PTF-Quelle für Einzelpersonen → Modell beschränkt sich bewusst auf PK + GK (weitere Positionen = OWNER-Frage im Antragswerkstatt-Kontext).

### Vorfinanzierung (nachlaufende Quartalsabrufe)

Beispiel Szenario B: Förderzeitraum 01.06.–30.11.2027; Abruf frühestens Anfang Q3 (01.07.) für geleistete Q2-Arbeit — der erste Abruf deckt zunächst **nur den Juni** (F/6 = **7.896,88 €**); konservativer Planungs-Peak ist ein volles Quartal (**F/2 = 23.690,63 €**, z. B. Juli–September vor dem nächsten Abruf). Zusätzlich EA-Kontoauszug (Saldo ≥ 2.500 €; deckt strenge Lesart 2.493,75 € und FAQ-Lesart 2.500 €).

## 3. Identitäten (müssen für JEDES Szenario gelten)

```
K1  Kostenidentität:      G = PK + GK
K2  Finanzierung:         G = F + EA
K3  Förderquote:          F ≤ 0,95 × G
K4  Eigenanteil:          EA ≥ 0,05 × G
K5  Stunden-Cap:          Stunden ≤ 950
K6  Betrags-Caps:         F ≤ 47.500 €;  G ≤ 50.000 €
K7  GK-Regel:             GK ≤ 0,05 × PK  (FAQ-Lesart)
K8  Rundung:              alle Größen auf Cent gerundet; Σ-Identität nach Rundung erhalten
```

## 4. Test-Protokoll (reproduzierbar; Skript + Ausgabe archiviert in validation-report.md §V3)

Das Testskript (exakte Dezimalarithmetik, `decimal`-Modul) prüft K1–K8 für Szenarien A–D und die Grenzfälle (950 h exakt, 951 h → Verstoß, 95 %-Grenze, GK > 5 % → Verstoß, Gesamtkosten 50.000,01 → Verstoß, Teilzeit 200 h, EA-Nachweis-Höhe). Ergebnis: **ALLE TESTS BESTANDEN** nach Korrektur; das alte Modell A wäre in K2/K3 gefailt (F > 0,95 × G). Details: validation-report.md.

## 5. Empfehlung für die Antragshöhe

- **Planung konservativ nach strenger Logik (Szenario B): 950 h beantragen, Förderhöhe 47.381,25 €** — im Portal ggf. auf 47.381 € runden; falls das Portal die FAQ-Logik (E) abbildet, wird automatisch bis 47.500 € ausgeschöpft.
- **Nicht** 47.500 € als Förderbetrag in Planungsrechnungen festschreiben, bevor Q3 (Portal-Logik) geklärt ist.
- **Ratenhebel (nur mit Rechnungs-Nachweis):** ein nachgewiesener Satz > 50 €/h (ab ~50,13 €/h) erlaubt G bis 50.000 € innerhalb von 950 h (Szenario C) — nur relevant für Applicant mit entsprechendem Nachweis.
- **De-minimis-Vorprüfung:** vorhandene Beihilfen der letzten 3 Jahre summieren (Szenario H); bei Werten nahe 300.000 € F-Limit vor Antrag klären.
- Kontoauszug-Saldo für den EA-Nachweis: ≥ 2.500 € deckt beide Modelle ab.
- Second Stage (falls mitbeantragt): konservativ 31.650,00 € planen (633 h à 50 €); keine Code-Meilensteine.

## 6. Fehlerprotokoll

**Ursache des ursprünglichen Fehlers (v1):** Der FAQ-Satz „Maximalfördersumme = 950 h × 50 €" wurde mit der RL-95-%-Struktur verrechnet, **ohne die Kostenbasis zu prüfen**: Die 95-%-Struktur wurde auf ein angenommenes 50.000-€-Budget angewendet, dessen Kostenpositionen (PK+GK = 50.000 €) unter den 950-h-/GK-5-%-Regeln nicht konstruierbar sind; der Eigenanteil wurde als Finanzierung auf Kosten addiert, die nicht existierten.

| Revision | Anlass | Änderung | Validierung |
|---|---|---|---|
| v2 | Externer Befund + Review: Finanzierungsidentität verletzt (Modell A/B: F = 100 % der ausgewiesenen Kosten; EA ohne Kostenposition) | Strikte Trennung Kostenrechnung (G = PK + GK) und Finanzierung (G = F + EA); Szenarien A–F neu gerechnet; FAQ-Lesart als Szenario E isoliert; konservative Empfehlung 47.381,25 € | 61/61 Dezimal-Tests, inkl. Negativ-Test „altes Modell A verletzt K3" |
| v3 | Review B2 K6/K7/K8 + Review A2 M6/M10: Second-Stage- und De-minimis-Sektionen fehlten; Szenario-C-Unkonstruierbarkeit galt nur bei exakt 50 €/h; AZK-Anker fehlte; Vorfinanzierungs-Satz inkonsistent | Szenario G (Second Stage, 4 Frames, konservativ 31.650 €), Szenario H (De-minimis-Limit 300.000 €/3 J.), Szenario C mit Ratenhebel (R ≤ ~50,13 €/h → G = 50.000 € konstruierbar), AZK-Anker-Abschnitt, Team-Konsistenz-Beleg (§1), RL-Konsolidierungs-Label, Vorfinanzierung F/6 je Monat + F/2-Peak | Tests erweitert (Szenario G/H + Ratenhebel-Boundary R = 50,1256 €/h) — validation-report.md §V3 |
