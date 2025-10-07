# Aufgabenblatt 3 – Testing-Basics: Test-After Approach

---

## Aufgabenstellung

Im Rahmen dieser Übung üben Sie das Vorgehen nach dem **Test-After-Ansatz**.
Zunächst implementieren Sie Klassen, anschließend entwickeln Sie umfassende Tests.
Die Übung erfolgt in Kleingruppen mit Pair Programming. Besonderer Fokus liegt auf:

- Grundlagen von pytest
- Anwendung des AAA-Patterns (Arrange–Act–Assert)
- Dokumentation der Autorschaft
- Integration von Klassen und gemeinsames Debugging

---

## Gruppenstruktur

- **Team A (2 Personen):** Implementiert die Klasse `Konto`
- **Team B (1–3 Personen):** Implementiert die Klasse `KontoService`

**Hinweis:** Team B kann unabhängig von Team A beginnen. Dazu wird das `KontoInterface` verwendet. Über eine Factory-Methode werden zunächst Dummy-Objekte erzeugt.

---

## Vorbereitung

- **Pflichtlektüre:** `Anleitungen/pytest-einfuehrung.md`
- **Tests ausführen, um den Status zu prüfen:**
  ```bash
  pytest Uebung3/Tests/ -v
  ```

---

## Arbeitsweise: Test-After Approach

1. **Phase 1:** Parallele Implementierung beider Klassen
3. **Phase 2:** Test-Entwicklung (unabhängig)
2. **Phase 3:** Integration und gemeinsames Debugging
3. **Phase 4:** Test-Verbesserung

**Pair Programming:**

- Eine Person schreibt Code (Driver), die andere denkt mit (Navigator)
- Rollenwechsel alle 10 Minuten
- Beide Teams arbeiten parallel, dann gemeinsam

**Autorschaftsdokumentation:**
Jede Datei muss zu Beginn folgenden Kommentar enthalten:

```python
# Implementiert von: [Kürzel1], [Kürzel1]
```

---

## Aufgabe 1: Code-Implementierung

### Team A – Klasse `Konto`

Implementieren Sie die Klasse `Konto` in `Code/konto.py`

### Team B – Klasse `KontoService`

Implementieren Sie die Klasse `KontoService` in `Code/konto_service.py`

**Wichtig für Team B:** Nutzen Sie zunächst die `DummyKonto`-Klasse (bereits implementiert), um unabhängig zu arbeiten.

---

## Aufgabe 2: Tests entwickeln

- **Erweitern Sie die vorhandenen Tests** in `Tests/`.
- Die Test-Dateien enthalten bereits Placeholder-Tests - **implementieren Sie diese!**
- Nutzen Sie pytest und das AAA-Pattern (Arrange–Act–Assert).
- Testen Sie insbesondere:
  - Konto-Erstellung
  - Ein- und Auszahlung
  - Fehlerfälle (z. B. ungültige Werte, Überziehung falls definiert)

**Hinweis:** Die Tests in `Tests/` sind bereits vorbereitet - Sie müssen nur die `# TODO` Teile ausfüllen.

---

## Aufgabe 3: Integration und Debugging

Nachdem beide Teams ihre Klassen implementiert haben:

1. **Team B ersetzt die Dummy-Implementation:**

   ```python
   def _create_konto(self, konto_id: int, saldo: Decimal):
       # Ersetzen Sie DummyKonto durch echte Konto-Klasse:
       return Konto(konto_id, saldo)
   ```

2. **Gemeinsames Debugging:**

   - Führen Sie die Tests aus: `pytest Tests/ -v`
   - Beheben Sie auftretende Import- oder Integrationsprobleme
   - Stellen Sie sicher, dass beide Klassen korrekt zusammenarbeiten

3. **Code-Review:**
   - Beide Teams erklären sich gegenseitig ihren Code
   - Diskutieren Sie gefundene Probleme und Lösungsansätze

---

## Aufgabe 4: Tests verbessern

- **Erweitern Sie die vorhandenen Tests** in `Tests/`.
- Prüfen Sie, welche Änderungen Sie nach der Integration an den Tests noh vornehmen müssen.

---

## Erwartete Ergebnisse

- Beide Klassen sind vollständig implementiert
- Integration zwischen den Klassen funktioniert
- Tests laufen erfolgreich durch
- Autorschaftsdokumentation ist vorhanden
- Code-Review wurde durchgeführt

**Bitte beachten:** Der Code soll wie bei Übung 2 eingereicht werden und wird von einem anderem Team begutachtet. Die Einreichung läuft analog zu Übung 2.