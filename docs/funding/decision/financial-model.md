# Finanzmodell v2 — Kostenrechnung und Finanzierung getrennt (korrigierte Fassung)

**Datum:** 13.11.2026 · **Revision 2** (ersetzt die Modell-A/B-Fassung vom 13.11.2026 Vormittag; Korrekturanlass siehe §Fehlerprotokoll) · **Alle Zahlen exakte Dezimalarithmetik, 2 Nachkommastellen, maschinell getestet (Test-Protokoll in validation-report.md §V3).**

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
| Kompatibel? | **Nur wenn** GK = 2.500 € (5 % von 50.000) oder als vereinfachte Kommunikation ohne GK-Zählung | ja, ergibt **47.381,25 €** max. Förderung (bei 950 h + GK-Pauschale) |

**Befund:** Die FAQ-Formulierung („Maximalfördersumme = 950 h × 50 €") und die strenge 95-%-Regellogik (95 % × (PK+GK)) sind **nicht gleichzeitig exakt erfüllbar**, wenn GK strikt = 5 % × PK gilt. Differenz: 118,75 €. Dies ist eine **unauflösbare Mehrdeutigkeit der öffentlichen Quellen** → Szenario E bildet die PTF-Kommunikationslogik separat ab; für die Antragsempfehlung gilt die konservative strenge Logik (L1). Klärung: Portal/Antragswerkstatt (remaining-questions.md Q3).

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
```
1,05 × PK = 50.000 ⇒ PK = 47.619,05 € ⇒ 952,38 h  > 950-h-Obergrenze
⇒ UNTER FAQ-REGELN NICHT KONSTRUIERBAR (Stunden-Cap bindet zuerst)
Praktisches Kostenmaximum bei 950 h: G = 49.875,00 € (Szenario B)
Die 50.000-€-Grenze ist nur erreichbar, wenn GK > 5 % × PK gesetzt wird (z. B. 2.500 €) — dafür
existiert keine öffentliche Primärquelle (FAQ sagt 5 % der PK). → UNRESOLVED, siehe Szenario E.
```

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

### Vorfinanzierung (nachlaufende Quartalsabrufe)

Beispiel Szenario B: Förderzeitraum 01.06.–30.11.2027; Abruf frühestens Anfang Q3 (01.07.) für geleistete Q2-Arbeit. → **mind. ein Quartal (~11.845 € bei B, F/6≈7.897 € monatlich ≈ 23.691 € je Quartal bei Gleichverteilung — genauer: F/6 × 3 = 23.690,63 € Vorfinanzierung bis zum ersten Abruf)** muss getragen werden; zusätzlich EA-Kontoauszug (Saldo ≥ 2.493,75 €).

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
- Kontoauszug-Saldo für den EA-Nachweis: ≥ 2.500 € deckt beide Modelle ab.

## 6. Fehlerprotokoll

| | Alt (Revision 1) | Befund | Neu (Revision 2) |
|---|---|---|---|
| Modell A | PK 47.500; F 47.500; Budget 50.000; EA 2.500 | **Finanzierungsidentität verletzt**: F = 100 % der ausgewiesenen Kosten (47.500), nicht 95 %; die 2.500 € EA hatten keine Kostenposition | A: F = 45.125,00 €, EA = 2.375,00 € (G = 47.500) |
| Modell B | PK 45.238,10 + GK 2.261,90 = 47.500; F 47.500; Budget 50.000; EA 2.500 | gleiche Identitätsverletzung (F = 100 % von G) | B: PK 47.500 + GK 2.375 = G 49.875; F = 47.381,25 €; EA = 2.493,75 € |
| Ursache | FAQ-Satz „Maximalfördersumme = 950 h × 50 €" wurde mit der RL-95-%-Struktur verrechnet, ohne die Kostenbasis zu prüfen; die 95-%-Struktur wurde auf ein angenommenes 50.000-€-Budget angewendet, dessen Kostenpositionen (PK+GK = 50.000) unter den 950-h-/GK-Regeln nicht konstruierbar sind | | Getrennte Kosten-/Finanzierungsrechnung; FAQ-Lesart als Szenario E isoliert; Mehrdeutigkeit Q3 dokumentiert |
