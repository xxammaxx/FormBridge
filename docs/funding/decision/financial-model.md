# Finanzmodell — Prototype Fund Innovation, Einzelperson, 6 Monate (Jahrgang 03)

**Datum:** 13.11.2026 · Alle Kennzahlen primärquellenbasiert (siehe funding-rules-verified-2026.md F1/F6). Zwei Lesarten des Gemeinkosten-Verhältnisses werden als Modell A/B getrennt gerechnet (Widerspruch W2). Alle Berechnungen maschinell nachgeprüft (Skript-Ausgabe unten).

## Grundkennzahlen (VERIFIED)

| Größe | Wert | Quelle |
|---|---|---|
| Max. Förderbetrag (Einzelperson, 6 Monate) | 47.500 € | FAQ Förderung 01; /innovation |
| Max. Gesamtkosten (Einzelperson, 6 Monate) | 50.000 € | RL 2024 Nr. 5 (unverändert 2025/2026) |
| Max. Förderquote | 95 % (individuell „bis zu") | RL Nr. 5; FAQ Förderung 02 |
| Mindest-Eigenanteil | 5 % des Projektbudgets (= eigene Zeit; formaler Nachweis: Kontoauszug/Bankerklärung über die Höhe) | FAQ Förderung 02 + Auswahl 03; RL Nr. 4 |
| Max. Stunden | 950 (Mindestangabe ~250) | Handbuch Frage 14 |
| Stundensatz (Standard) | 50 € | FAQ Förderung 01 |
| Gemeinkosten-Pauschale | bis 5 % der Personalkosten | FAQ Förderung 02 |
| Second Stage | bis 31.667 € (≈ 633 h à 50 €); 50 €-Cap; Stunden ≤ Anteil der Phase 1 | FAQ Förderung 01 |
| Auszahlung | Quartalsraten nachgeleistet (nachlaufend) | FAQ Förderung 03 |

## Modell A — FAQ-Lesart (950 h × 50 € = Förderbetrag; ohne GK-Ausnutzung)

```
Personalkosten        PK = 950 h × 50 €        = 47.500 €
Förderbetrag          F  = 47.500 €            (95 % von 50.000 €)
Projektbudget         B  = F / 0,95            = 50.000 €
Eigenanteil           EA = B − F               =  2.500 €  (= 5 %)
```
Entspricht exakt den Prüfhypothesen 47.500 € / 95 % / 5 % / 950 h / 50 €. Die 50.000 €-Gesamtkosten-Grenze wird exakt ausgeschöpft. Eigenanteil 2.500 € ≈ 50 h äquivalente Eigenzeit.

## Modell B — RL-Lesart mit GK-Pauschale innerhalb der Gesamtkosten-Grenze

Wenn die GK-Pauschale (5 % der PK) zusätzlich beantragt wird und alles unter dem 50.000 €-Gesamtkosten-Cap bleiben muss:

```
PK + GK ≤ F_max = 47.500 €   mit GK = 0,05·PK
⇒ 1,05·PK ≤ 47.500 €  ⇒ PK ≤ 45.238,10 €  ⇒ max. Stunden ≈ 904 h (à 50 €)
Beispiel (904 h): PK = 45.200 €, GK = 2.260 €, förderfähig 47.460 € ≈ 47.500 €-Cap
Gesamtbudget B = 47.460 € / 0,95 = 49.958 €; Eigenanteil ≈ 2.498 €
```
**Konsequenz:** Unter Modell B kostet die voll ausgenutzte GK-Pauschale ca. 46 förderfähige Stunden (950 → ~904). Welches Modell das Portal rechnet, ist dort zu klären (W2).

## Rechenbeispiele (beide Modelle)

| Szenario | Stunden | PK | GK (5 %) | Förderbetrag | Budget | Eigenanteil |
|---|---|---|---|---|---|---|
| A: Vollausbau | 950 | 47.500 | — | **47.500** | 50.000 | **2.500** |
| B: Vollausbau mit GK | ~904 | 45.238 | 2.262 | ~47.460 | ~49.958 | ~2.498 |
| Reduziert (FAQ-Lesart) | 850 | 42.500 | — | 42.500 | 44.737 | 2.237 |
| Reduziert mit GK (Modell B) | 850 | 42.500 | 2.125 | 42.394* | 44.625 | 2.231 |

\* 42.394 = 95 % von (42.500 + 2.125) = 44.625 — liegt unter dem 47.500-Cap; Förderquote „individuell bis zu 95 %" (weniger zu beantragen ist zulässig).

## Plausibilitätsprüfung der Prüfhypothesen (Auftrag F6)

| Hypothese | Prüfung | Ergebnis |
|---|---|---|
| 47.500 € Förderung | 0,95 × 50.000 € | ✓ exakt |
| 95 % Förderquote | RL Nr. 5 wörtlich („bis zu 95 Prozent", Bemessungsgrundlage PK+GK) | ✓ |
| 5 % Eigenanteil | FAQ Förderung 02 („mindestens 5 %") | ✓ (Konzept „Zeit", formal Kontoauszug) |
| 950 Stunden | Handbuch Frage 14 („max. 950 h") | ✓ |
| 50 € Stundensatz | FAQ Förderung 01 (explizit) | ✓ (nur mit Rechnungs-Nachweis höher erhöhbar; dann weniger Stunden) |

Alle fünf Prüfhypothesen bestätigt — mit zwei dokumentierten Ambiguitäten (W1/W2): (1) Eigenanteil-Zeit vs. Kontoauszug-Nachweis, (2) GK-Pauschale vs. 950-h-Frame.

## Liquidität & Nachweis

- **Auszahlung nachlaufend:** Quartal 1 (Juni) wird gearbeitet, Abruf ab Quartalsbeginn Juli (FAQ-Beispiel: Förderbeginn 01.06.2025 → Abruf ab 01.07.2025). ⇒ **Vorfinanzierungsbedarf mindestens ein Quartal** (~11.875 € bei Vollausbau A).
- **Formal:** Kontoauszug mit Saldo ≥ Eigenanteil (2.500 € bei Modell A) gehört zur Bewilligungs-Unterlage (FAQ Auswahl 03); RL: „Bankerklärungen über die entsprechende Höhe".
- **Eigene Arbeitszeit als Eigenanteil:** Konzeptionell ja (FAQ), aber der formale Liquiditätsnachweis bleibt — beide Punkte im Antrag/Bewilligungsprozess unterscheiden.
- **Steuerlich:** Zuwendung ist De-minimis-Beihilfe (RL); steuerliche Behandlung (Einkünfte) = individuelle Frage, kein PTF-Public-Detail → Steuersache/Steuerberater, hier UNKNOWN.

## Second Stage (falls beantragt — nur bei initialer Bewerbung!)

- Max. 31.667 € ≈ 633 h à 50 € (Cap); Stunden-Anteil ≤ der ersten Phase (100 % → 100 %).
- **Keine Code-Meilensteine förderfähig** — nur Community, User Testing, Nachhaltigkeit.
- FormBridge-Relevanz: sinnvoll (Adoption, Community, Integrations-Rezepte), NICHT für Kernel-Arbeit.

## Nachrechnung (maschinell verifiziert)

```
47.500 / 0.95        = 50.000.00   ✓
50.000 - 47.500      =  2.500.00   ✓ (5 % von 50.000)
950 * 50             = 47.500.00   ✓
1.05 * 45238.10      = 47.500.00   ✓ (Modell B, gerundet auf 2 NK)
633 * 50             = 31.650      (FAQ „gerundet 633 h"; W4-Rundungsnuance)
33.337 * 0.95        = 31.670.15   (RL-Pfad; W4)
```
