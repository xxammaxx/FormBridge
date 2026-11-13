# Finanzmodell v4 — exakte Dezimalrechnung, getrennte Kosten- und Finanzierungslogik

**Datum:** 13.11.2026 · **Revision 4** (v1: fehlerhaft, Finanzierungsidentität verletzt; v2: Identitätskorrektur; v3: Second Stage/De-minimis/Ratenhebel; **v4: unabhängige Quellenprüfung, 102/102-Testsuite, Second-Stage-Korrektur, 10-Monats-Option, rollierende De-minimis-Frist, Q3-Analyse**) · **Status:** Planungsmodell, keine Förderzusage · **Testbasis:** [`validation/financial_model.py`](validation/financial_model.py), [`validation/test_financial_model.py`](validation/test_financial_model.py), [`validation/test-output.txt`](validation/test-output.txt), [`validation/scenario-report.md`](validation/scenario-report.md)

**Quellen:** [Quellenregister](source-register-2026-11-13.md) · **Q3:** [Q3-Klärung](q3-clarification.md) · **Regeln:** [funding-rules-verified-2026.md](funding-rules-verified-2026.md)

## 0. Gegenstand und Namensabgrenzung

Dieses Modell rechnet den **6-monatigen Förderzeitraum** der Prototype-Fund-Linie Innovation (01.06.–30.11.2027) und die **4-monatige Second Stage** (01.12.2027–31.03.2028). Es rechnet **nicht** die Feldexa-Produktentwicklung als solche, sondern den in [`project-boundary.md`](../project-boundary.md) abgegrenzten Fördergegenstand (Feldexa-2.0-Kontext / FormBridge-Modul). Die 10-Monats-Option der Richtlinie ist als Szenario I dokumentiert, aber nicht Baseline.

**Kostenrechnung:**

```text
G = PK + GK
PK = Stunden × Stundensatz
GK <= 5 % × PK (FAQ-Pauschale; optional)
G <= 50.000 € (RL Nr. 5, 6 Monate, solo)
Stunden <= 950 (Handbuch Frage 14)
```

**Finanzierung:**

```text
G = F + EA
F <= 95 % × G (RL Nr. 5; FAQ Förderung 02)
EA >= 5 % × G
```

**Grundregel:** Förderung und Eigenanteil sind **Finanzierungsanteile der tatsächlich ausgewiesenen Kosten**. Ein Eigenanteil darf nicht auf ein Budget addiert werden, für das keine Kostenposition existiert. Der Eigenanteil ist nicht zusätzlich zu den Kosten zu addieren; er ist der nicht geförderte Teil derselben Kosten.

## 1. Verbindliche Regel vs. FAQ-Kommunikation

| Punkt | FAQ-/Handbuch-Kommunikation | Verbindliche RL-Logik |
|---|---|---|
| Maximalförderung solo | „47.500 € = 950 h × 50 €" (FAQ Förderung 01; Handbuch Frage 14) | 95 % der Gesamtkosten (PK+GK), Gesamtkosten <= 50.000 € (RL Nr. 5) |
| Gemeinkosten | „pauschal 5 % der Personalkosten" (FAQ Förderung 02) | Personal- und Gemeinkosten sind Bemessungsgrundlage (RL Nr. 5); die 5-%-Pauschale ist die FAQ-Konkretisierung |
| Eigenanteil | „mindestens 5 % … eure Zeit" (FAQ Förderung 02) | 95-%-Förderquote impliziert mindestens 5 % Eigenanteil; Nachweis über bonitätsprüfungsfähige Unterlagen (RL Nr. 4) |
| 950 h | „max. 950 h … insgesamt" (Handbuch Frage 14) | Die RL nennt keine Stundengrenze; die 950 h sind Programm-/Handbuchgrenze |
| 50.000 € | wird in der FAQ nicht als Gesamtkosten-Cap genannt | **Gesamtkosten**-Cap (RL Nr. 5) |

**Folge:** Die kommunizierte 47.500-€-Zahl ist keine aus der RL abgeleitete Förderobergrenze. Sie ist mit der RL nur vereinbar, wenn die Gesamtkosten 50.000 € erreichen (siehe Q3, Erklärungen E3–E5). Bei 950 h × 50 € und 5 % GK auf PK sind die Gesamtkosten 49.875 €; die strenge Förderung ist 47.381,25 €.

## 2. Rundungsregeln (verbindlich für dieses Modell)

Alle Beträge sind `Decimal`, nie `float`. Die Regeln sind bewusst so gewählt, dass keine Rundung zu einer Überzeichnung führt:

| Größe | Regel | Begründung |
|---|---|---|
| PK | kaufmännisch auf Cent (`ROUND_HALF_UP`) | übliche Geldrundung |
| GK | **abrunden** auf Cent (`ROUND_DOWN`) | GK darf 5 % der PK nie überschreiten |
| G | exakte Summe der cent-gerundeten PK + GK | K1 bleibt cent-exakt |
| F | **abrunden** auf Cent (`ROUND_DOWN`) | F darf 95 % von G nie überschreiten; Half-up könnte um 0,005 € überzeichnen |
| EA | `G − F` (exakter Rest) | K2 bleibt cent-exakt |
| Quartalsraten | erste Raten abrunden, letzte Rate erhält den Rest | Summe = F exakt, keine 1-Cent-Drift |
| Monatlicher Eigenanteil | abrunden | keine Überzeichnung des eigenen Beitrags |

**Beispiel für die F-Rundung:** G = 36.750,01 €; 95 % = 34.912,5095 €. Half-up ergäbe 34.912,51 € und damit 0,0005 € **über** 95 %. Das Modell liefert 34.912,50 €. Der Test `test_funding_is_floored_not_half_up` sichert das.

## 3. Szenarien (Basis: 50 €/h, 5 % GK auf PK, sofern nicht anders angegeben)

### Szenario A — 950 h ohne Gemeinkosten

```text
PK = 950 × 50        = 47.500,00 €
G  = PK              = 47.500,00 €   (Cap 50.000 ✓)
F  = 0,95 × G        = 45.125,00 €   (nicht 47.500 €)
EA = G − F           =  2.375,00 €
```

### Szenario B — 950 h mit 5 % Gemeinkosten (konservative Planungsbasis)

```text
PK = 47.500,00 €;  GK = 0,05 × PK = 2.375,00 €
G  = 49.875,00 €                     (Cap 50.000 ✓, 125,00 € Headroom)
F  = 0,95 × G        = 47.381,25 €   (strenges Maximum)
EA = G − F           =  2.493,75 €
```

**Differenz zur FAQ:** 47.500,00 − 47.381,25 = **118,75 €**. Das ist genau 5 % der GK-Pauschale (5 % × 2.375 €). Die FAQ behandelt die GK insoweit als voll gefördert; die 95-%-Regel verlangt auch auf GK einen Eigenanteil.

**Absolute Untergrenze, falls GK nicht anerkannt wird:** Szenario A mit 45.125,00 €. Die Planung sollte daher nicht mehr als 47.381,25 € und nicht weniger als 45.125,00 € als belastbaren Korridor behandeln.

### Szenario C — Gesamtkosten 50.000 € mit GK = 5 % × PK

Bei exakt 50 €/h ist G = 49.875 €; die 50.000-€-Grenze bindet nicht. Mit einem **nachgewiesenen höheren Satz** (FAQ Förderung 01: Rechnungsnachweis) ist G = 50.000 € konstruierbar:

```text
1,05 × (950 × R) <= 50.000  ⇒  R <= 50,125313… €/h
Beispiel R = 50,125313 €/h (gerundeter Beispielsatz, exakt 50,1253132832…):
PK = 47.619,05 €; GK = 2.380,95 €; G = 50.000,00 €
F  = 47.500,00 €; EA = 2.500,00 €
```

Mit dem gerundeten Satz 50,1253 €/h ergibt sich G = 49.999,99 €, F = 47.499,99 €. Mit 50,13 €/h ergibt sich G = 50.004,67 € und damit ein **Cap-Verstoß**. Der exakte Schwellenwert ist `50.000 / (950 × 1,05) = 50,1253132832… €/h`; das Modell prüft ihn in `test_rate_lever_exact_threshold`.

**Praktische Bedeutung:** Der Ratenhebel ist nur relevant, wenn der Antragsteller höhere Stundenlöhne nachweisen kann. Für die Standardplanung bleibt es bei 50 €/h und Szenario B.

### Szenario D — reduzierter Stundenumfang (mit GK)

| Stunden | PK | GK (5 %) | G | F = 95 % × G | EA = 5 % × G |
|---:|---:|---:|---:|---:|---:|
| 700 | 35.000,00 | 1.750,00 | 36.750,00 | **34.912,50** | 1.837,50 |
| 800 | 40.000,00 | 2.000,00 | 42.000,00 | **39.900,00** | 2.100,00 |
| 850 | 42.500,00 | 2.125,00 | 44.625,00 | **42.393,75** | 2.231,25 |
| 950 | 47.500,00 | 2.375,00 | 49.875,00 | **47.381,25** | 2.493,75 |

Ohne GK: F = 33.250,00 / 38.000,00 / 40.375,00 / 45.125,00 €.

### Szenario E — FAQ-Kommunikationslogik (separat, nicht regelkonform)

```text
F = min(950 h × 50 €, 47.500 €) = 47.500,00 €
Dafür erforderliche Kostenbasis: G = 50.000,00 €
Erreichbar nur mit GK = 2.500,00 € (5 % des Gesamtbudgets) oder
1.000 Gesamtstunden ohne GK oder höherem Satz.
```

Setzt man GK = 2.500 € an, ist GK/PK = 5,263 % und damit **über** der FAQ-Grenze von 5 % der Personalkosten. Das Modell markiert diese Variante mit `overhead_above_5_percent_of_personnel` und `K7_overhead_base_exceeded`. Sie ist als **Kommunikations-/Portalvariante** dokumentiert, nicht als regelkonforme Planung.

### Szenario F — Teilzeit/Anstellung (Arbeitsschutz-Obergrenze)

Bei parallel bestehender Teilzeit-Anstellung begrenzen Arbeitsschutzgesetze die Gesamtstunden nach oben (FAQ Förderung 01). Beispiel 200 h/6 M.:

```text
PK = 10.000,00 €; GK = 500,00 €; G = 10.500,00 €
F = 9.975,00 €; EA = 525,00 €
```

Formal zulässig, aber unter der ~250-h-Verwaltungsgrenze (Handbuch Frage 14: darunter „lohnt der administrative Aufwand nicht") → praktisch ungeeignet.

### Szenario G — Second Stage (4 Monate; nur bei initialer Bewerbung mitbeantragt)

**Korrigierte Rechnung (vorherige Dokumentation war fehlerhaft):** Die frühere Zeile „konservativ 31.650,00 € (633 h à 50 €)" verwechselte **Personalkosten** mit **Förderung**. 633 h × 50 € = 31.650 € PK; bei 5 % GK und 95 % Förderung ergibt das:

| Variante | PK | GK | G | F = 95 % | EA |
|---|---:|---:|---:|---:|---:|
| 633 h | 31.650,00 | 1.582,50 | 33.232,50 | **31.570,87** | 1.661,63 |
| 634 h | 31.700,00 | 1.585,00 | 33.285,00 | **31.620,75** | 1.664,25 |
| 635 h | 31.750,00 | 1.587,50 | 33.337,50 | Cap-Verstoß | — |

Der theoretische Cap bei G = 33.337 € und 95 % ist **31.670,15 €**; er ist mit 50 €/h und 5 % GK nicht exakt konstruierbar (634 h liegen darunter, 635 h darüber). Die FAQ-Kommunikation 31.667 € ist eine gerundete Näherung; die Differenz zu 633 h beträgt **96,13 €**, zu 634 h **46,25 €**.

**Regeln:** 50-€/h-Cap in der Second Stage (kein Ratenhebel); Stunden <= Umfang der regulären Phase (Handbuch: bis zu 100 %, wenn 100 % beantragt); **keine Code-Meilensteine** förderfähig (Handbuch Frage 16). Die Second Stage ist nur jetzt mitbeantragbar; späteres Hinzufügen ist ausgeschlossen.

### Szenario H — De-minimis-Obergrenze (kann die Förderhöhe deckeln)

Die Zuwendung ist De-minimis-Beihilfe (RL Nr. 1.3/5; Anlage Nr. 1). Der Freibetrag beträgt **300.000 € in einem rollierenden Dreijahreszeitraum** (VO (EU) 2023/2831, Art. 3 Abs. 2 und Erwägungsgrund 11), nicht kalenderjährlich.

```text
Verfügbare F-Obergrenze = min(F_Szenario, 300.000 − Summe anderer De-minimis-Beihilfen der letzten 3 Jahre)
```

Beispiel: Vorbelastung 260.000 € → verfügbar 40.000 € → F = 40.000,00 €; EA steigt auf 9.875,00 €; die Kostenbasis bleibt 49.875,00 €. Bei Vorbelastung 300.000 € ist keine De-minimis-Förderung mehr möglich (`deminimis_exhausted`). Die De-minimis-Prüfung umfasst **auch die Second Stage und andere Projekte**; die Summe aller Förderungen im Dreijahreszeitraum muss <= 300.000 € bleiben. Aufbewahrung nach RL Anlage: mindestens **3 Jahre** (nicht 10; eine längere AZK-Aufbewahrung ist separat zu prüfen).

### Szenario I — 10-Monats-Option (6 + 4 Monate; Alternativszenario)

Die RL Nr. 4 erlaubt eine zehnmonatige Laufzeit (6 Monate Entwicklung + 4 Monate Vertiefung nach Evaluation); RL Nr. 5 begrenzt die zweite Phase auf 33.337 € Gesamtkosten. Die kombinierte Obergrenze ist 83.337 €; die strikte Förderobergrenze ist **79.170,15 €**. Die FAQ nennt gerundet 79.167 € (Differenz 3,15 €). Beispiel mit 950 h + 634 h:

```text
G = 49.875,00 + 33.285,00 = 83.160,00 €
F = 79.002,00 €; EA = 4.158,00 €
```

Die 10-Monats-Option ist **nicht** die Baseline; sie ist eine strategische Alternative, falls der Owner die längere Laufzeit und die zweite Phase will. Die Detailseite verlangt die Angabe „sechs- oder zehnmonatig" bereits in der Bewerbung.

## 4. Q3 — die 118,75-€-Differenz

**Status: UNRESOLVED.** Die öffentlichen Quellen sind nicht widerspruchsfrei. Die vollständige Analyse mit fünf Erklärungsvarianten und dem Anfrageentwurf steht in [q3-clarification.md](q3-clarification.md). Kurzfassung:

- **Planungsbasis:** 47.381,25 € (Szenario B).
- **Kommunizierte Obergrenze:** 47.500,00 € (FAQ).
- **Differenz:** 118,75 € (5 % der GK-Pauschale).
- **Nicht entschieden:** ob 950 h Gesamt- oder Förderstunden sind; ob GK auf PK oder Gesamtbudget berechnet wird; ob die FAQ vereinfacht.
- **Nicht senden:** Die Anfrage in Q3 ist ein Entwurf; Versand nur mit Owner-Freigabe.
- **Nicht als offizielle Klärung darstellen:** Keine der Varianten ist durch eine schriftliche Autoritätsaussage bestätigt.

## 5. Vorfinanzierung und Cash-Flow

Beispiel Szenario B, Förderzeitraum 01.06.–30.11.2027. Die Auszahlung erfolgt nachlaufend zu Quartalsbeginn (FAQ Förderung 03):

| Rate | Zeitpunkt | Zeitraum | Betrag |
|---|---|---|---|
| 1 | 01.07.2027 | Juni | **7.896,87 €** |
| 2 | 01.10.2027 | Juli–September | **23.690,62 €** |
| 3 | 01.01.2028 | Oktober–November | **15.793,76 €** |
| **Summe** | | | **47.381,25 €** |

Die Raten werden abgerundet; die letzte Rate erhält den Rest, damit die Summe exakt bleibt. (Die frühere Dokumentation nannte 7.896,88 € und 23.690,63 €; das summierte sich zu 47.381,26 €.)

**Cash-Bedarf:**

- Monatliche Gesamtkosten: 49.875,00 / 6 = **8.312,50 €**.
- Erstes Monatsloch: 8.312,50 − 7.896,87 = **415,63 €** (das ist der Eigenanteil des ersten Monats).
- Konservativer Peak **externer Vorfinanzierung**: F/2 = **23.690,62 €** (ein volles Quartal Juli–September vor der nächsten Rate).
- Peak **gesamter Cash-Bedarf**: G/2 = **24.937,50 €** (davon 1.246,88 € eigener Anteil).
- Kontoauszug-Saldo für den Eigenanteil: **>= 2.500,00 €** deckt die strenge Lesart (2.493,75 €) und die FAQ-Lesart (2.500,00 €) ab.

**Wichtig:** Die 2.500 € sind ein **Liquiditätsnachweis**, keine zusätzliche Kostenposition. Sie werden nicht auf G addiert.

## 6. Identitäten (müssen für jedes Szenario gelten)

```text
K1  Kostenidentität:      G = PK + GK
K2  Finanzierung:         G = F + EA
K3  Förderquote:          F <= 0,95 × G
K4  Eigenanteil:          EA >= 0,05 × G
K5  Stunden-Cap:          Stunden <= 950 (regulär; Second Stage <= regulärer Umfang)
K6  Betrags-Caps:         G <= 50.000 € (regulär); G_second <= 33.337 €; G_ten <= 83.337 €
K7  GK-Regel:             GK <= 0,05 × PK (FAQ-Lesart)
K8  Rundung:              alle Größen cent-exakt; K1/K2 nach Rundung erhalten
```

Zusätzlich prüft das Modell: `F <= 47.500 €` (Kommunikationsdeckel), `F_second <= 31.667 €` (Kommunikationsdeckel), `F_ten <= 79.170,15 €` (abgeleiteter Cap) und die De-minimis-Restverfügbarkeit.

## 7. Reproduzierbare Testevidenz

**Befehl (aus dem Repository-Root):**

```bash
python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v
```

**Ergebnis am 13.11.2026:** `Ran 102 tests … OK` — **102/102 PASS**. Vollständige Ausgabe: [`validation/test-output.txt`](validation/test-output.txt). Szenariotabelle: [`validation/scenario-report.md`](validation/scenario-report.md). Modell: [`validation/financial_model.py`](validation/financial_model.py). Tests: [`validation/test_financial_model.py`](validation/test_financial_model.py). Laufzeitumgebung: Python 3.12 (stdlib `unittest`, `decimal`), keine externen Abhängigkeiten.

**Abgedeckte Regressionen (Auszug):**

- Ursprüngliches Modell A (F = 47.500 bei G = 47.500) verletzt K2/K3.
- GK auf Gesamtbudget statt PK (5,263 %) verletzt K7.
- F > 95 % von G (47.500 auf 49.875) wird erkannt.
- EA < 5 % von G (2.493,74 auf 49.875) wird erkannt.
- 951 h, 50.000,01 €, GK > 5 %, Rate > 50 ohne Nachweis, Second-Stage-Rate > 50.
- Cent-Rundung, Floor-vs-Half-up, Quartalssummen, Schwellenwert 50,125313 €/h.
- Second Stage 633/634/635 h; 31.650-€-Fehlclaim; 31.667-€-Differenz.
- De-minimis 0 / 260.000 / 299.900 / 300.000 / 310.000; Kombination regular + Second Stage.
- 10-Monats-Cap 83.337 € und 79.170,15 €.

**Hinweis zur Vorgeschichte:** Die frühere Behauptung „56/57 Tests, 1 Skript-Bug" war **nicht reproduzierbar**, weil das Testskript nicht im Repository archiviert war. Revision 4 ersetzt sie durch die hier archivierte, vollständig lauffähige Suite. Die Zahl 57 ist damit historisch; der aktuelle, tatsächliche Testumfang ist **102**.

## 8. Planungsempfehlung (keine Förderzusage)

1. **Antragshöhe:** 950 h beantragen; Förderung konservativ mit **47.381,25 €** planen. Im Portal ggf. auf 47.381 € runden; falls das Portal die FAQ-Logik abbildet, wird automatisch bis 47.500 € ausgeschöpft.
2. **Nicht** 47.500 € als selbstverständliche Planungsgröße festschreiben, bevor Q3 geklärt ist.
3. **Eigenanteil:** **2.500 €** Kontoauszug-Saldo vorhalten; das deckt 2.493,75 € (streng) und 2.500,00 € (FAQ) ab.
4. **Ratenhebel:** Nur mit Rechnungsnachweis; ein Satz ab 50,125313 €/h erlaubt G = 50.000 € innerhalb von 950 h. Ohne Nachweis nicht planen.
5. **Second Stage:** Falls mitbeantragt, konservativ **31.570,87 €** (633 h) bzw. **31.620,75 €** (634 h) planen; nicht 31.650 € als Förderung ansetzen. Keine Code-Meilensteine.
6. **De-minimis:** Vor Antrag alle Beihilfen der letzten drei Jahre (rollierend) addieren; bei Werten nahe 300.000 € F begrenzen. Die Second Stage zählt mit.
7. **10 Monate:** Nur als bewusste Alternative; dann 83.337 € Gesamtkosten und 79.170,15 € Fördercap beachten.
8. **Q3:** Anfrageentwurf vorbereitet, **nicht senden** ohne Owner-Freigabe. Klärung ist nicht einreichungsblockierend.

## 9. Fehlerprotokoll

| Revision | Anlass | Änderung | Validierung |
|---|---|---|---|
| v1 | — | FAQ-Formel „950 h × 50 €" als Förderbetrag; Eigenanteil additiv | **fehlerhaft** (K2/K3 verletzt) |
| v2 | Externer Befund | Trennung Kostenrechnung/Finanzierung; Szenarien A–F; FAQ-Lesart als E | 61/61 Dezimal-Tests (nicht archiviert) |
| v3 | Review A2/B2 | Second Stage, De-minimis, Ratenhebel, AZK-Anker, Vorfinanzierung | 56/57 (1 Skript-Bug; nicht archiviert) |
| **v4** | **Unabhängige Neuprüfung 13.11.2026** | **Second-Stage-31.650-€-Fehler korrigiert (31.570,87/31.620,75); 10-Monats-Option ergänzt; De-minimis rollierend statt kalenderjährlich; Aufbewahrung 3 statt 10 Jahre; 102/102-Testsuite archiviert; Q3 mit fünf Erklärungen; 47.500-€-Aussage als Kommunikationsgröße präzisiert** | **102/102 PASS; Review A/B siehe [final-validation-report.md](final-validation-report.md)** |

**Ursache des ursprünglichen Fehlers:** Die FAQ-Formel wurde mit der RL-95-%-Struktur verrechnet, ohne die Kostenbasis zu prüfen. Das 50.000-€-„Budget" wurde als Finanzierungsgröße behandelt, obwohl unter 950 h + GK-Regeln nur 47.500 € (ohne GK) bzw. 49.875 € (mit GK) Kosten konstruierbar sind. Der Eigenanteil wurde als zusätzliche Finanzierung auf nicht existierende Kosten addiert.

**Ursache des Second-Stage-Fehlers (v3):** 31.650 € (633 h × 50 €) sind Personalkosten; die Dokumentation bezeichnete sie als Förderung. Das ist dieselbe Kategorienverwechslung wie in v1, nur in der Second Stage. v4 trennt PK, GK, G, F und EA auch dort.
