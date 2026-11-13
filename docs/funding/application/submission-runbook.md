# Submission-Runbook — FormBridge, Prototype Fund 2027

**Zweck:** Schritt-für-Schritt-Anleitung für den Owner nach der Freigabe. **Keine Aktion in diesem Runbook wurde ausgeführt.** Keine Einreichung, keine E-Mail, keine Portaländerung.

## 0. Harte Grenzen

- Frist: **30.11.2026, 15:00 Uhr MEZ** (CET). Puffer einplanen; Portallast am letzten Tag vermeiden.
- Keine Einreichung ohne Owner-Freigabe.
- Keinen bestehenden Portal-Draft (insbesondere RepairProbe) überschreiben.
- Keine E-Mail/Anfrage ohne Owner-Freigabe senden.
- Keine Lizenzfestlegung ohne Owner-Freigabe.
- Keine personenbezogenen Daten in dieses öffentliche Repository schreiben.

## 1. Preflight (T-7 bis T-3)

```bash
cd /home/xxammaxx/Schreibtisch/feldexa_forderung/FormBridge
git fetch origin
git status --short --branch
git rev-parse HEAD
python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v
```

Erwartet: Branch `docs/funding-decision-2026-11-13`, Working Tree clean, **109/109 Tests OK**. Linkcheck: 0 gebrochene relative Links.

**Owner-Checkliste:** [owner-checklist.md](owner-checklist.md) vollständig abarbeiten. Besonders:

- [ ] M1–M6 positiv; M8 planbar.
- [ ] O1 Lizenz; O2 Stunden (950/850); O3 Second Stage; O4 Projektfassung; O5 Q2-Anfrage.
- [ ] Persönliche Felder ergänzt; keine Platzhalter mehr im Portaltext.
- [ ] Q3/Q3b als offen dokumentiert; keine 47.500-€-Planung ohne Q3.

## 2. Portal öffnen

1. `https://bewerben.prototypefund.de/` öffnen.
2. Einloggen (E-Mail/Passwort oder bestehender Account). **Kein** neues Konto mit fremden Daten.
3. **Jahrgang 03: Innovation** wählen.
4. Prüfen: Frist wird als **30.11.2026** angezeigt; Förderlinie Innovation; Sprache Deutsch.

## 3. Live-Fragen abgleichen

1. [portal-field-mapping.md](portal-field-mapping.md) neben das Portal legen.
2. Jede Live-Frage mit dem Fragenwortlaut vergleichen.
3. Abweichungen notieren (Frage geändert? neues Pflichtfeld? anderes Limit?).
4. **Keine** erfundenen Limits übernehmen; die Live-Anzeige ist maßgeblich.
5. Falls ein Feld nicht in der Tabelle steht: als `PORTAL_UNVERIFIED` markieren und nach dem Ausfüllen hier ergänzen.

## 4. Antworten eintragen

Reihenfolge: §1 → §2 → §3 → §4 → §5 → §6 → §7 → §8 → §9 → Team → Erfahrung → Förderfähigkeit → Stunden → Motivation → Second Stage.

- Texte aus [application-final-de.md](application-final-de.md) kopieren.
- Nach jedem Feld die Zeichen-/Wortanzeige prüfen.
- Bei Kürzung: zuerst Kürzungsvorschläge aus dem Dokument nutzen, dann hier dokumentieren.
- Platzhalter `[OWNER_...]` **niemals** so absenden.
- Keine Behauptungen ergänzen, die nicht in [innovation-evidence.md](innovation-evidence.md) belegt sind.

## 5. Vor dem Absenden — Pflichtprüfung

- [ ] Alle Pflichtfelder ausgefüllt (Portal zeigt sie an).
- [ ] Keine Platzhalter mehr im Portaltext.
- [ ] Wort-/Zeichenlimits eingehalten.
- [ ] Projektlink `https://github.com/xxammaxx/FormBridge` korrekt.
- [ ] Stunden = 950 oder 850, konsistent mit Budget/Plan.
- [ ] Second Stage = Ja/Nein, konsistent mit Q16/Q17.
- [ ] FOSS-Zusage gesetzt; Lizenzstatus korrekt (offen oder entschieden).
- [ ] Keine sensiblen personenbezogenen Daten in öffentlichen Feldern, die nicht erforderlich sind.
- [ ] RepairProbe-Draft unverändert.
- [ ] Eigene Kopie/Screenshot der Zusammenfassung gespeichert.

## 6. Absenden

1. „Submit for review" (oder Portaläquivalent) anklicken.
2. Bestätigungs-E-Mail/Screenshot speichern.
3. Datum, Uhrzeit und Portal-ID notieren — **nicht** in dieses öffentliche Repo, sondern lokal/owner-privat.
4. Keine nachträgliche Änderung ohne Kenntnis der Portalregeln.

## 7. Nach dem Absenden

- Keine E-Mail an das PTF-Team ohne Owner-Freigabe; Q3-Anfrage bleibt separat.
- Keine Zusage als „Förderung erhalten" darstellen.
- Keine Implementierung vor Förderbescheid (project-boundary.md).
- Falls Rückfragen kommen: Antworten mit Quellen aus diesem Paket vorbereiten; keine erfundenen Angaben.

## 8. Falls das Portal nicht erreichbar ist

- Frist und Uhrzeit dokumentieren.
- Screenshot/Fehlermeldung speichern.
- Frühzeitig (nicht am 30.11.) `info@prototypefund.de` nur nach Owner-Freigabe kontaktieren.
- Keine Fristverlängerung behaupten.

## 9. Falls die Zeit nicht reicht

Priorität:

1. Pflichtfelder + §1/§2/§3/§4/§5/§7/§9.
2. Erfahrung/Motivation mit ehrlichen Platzhaltern ersetzen (nicht erfinden).
3. Second Stage weglassen (Nein), wenn Q16/Q17 nicht final sind.
4. **Nicht** eine unvollständige Bewerbung als „fertig" bezeichnen.

## 10. Nach der Einreichung — Beleg für den Owner

Lokal (nicht im öffentlichen Repo) ablegen:

- Datum/Uhrzeit der Einreichung
- Portal-Bestätigung (PDF/Screenshot)
- Eingereichter Text (Export)
- Offene Fragen (Q2/Q3/Q3b)
- Nächste Schritte nach Rückmeldung
