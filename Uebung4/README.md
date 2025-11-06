# Aufgabenblatt 4 – Test-Driven Development & API-Mocking

## Aufgabenstellung

In diesem Aufgabenblatt üben Sie die systematische Anwendung von Test-Driven Development (TDD) sowie den Einsatz von Mocks zur Entkopplung externer Abhängigkeiten (z.B. APIs).  
Die Übung erfolgt in zwei Teams mit Pair Programming.

---

## Übungsstruktur (3 Phasen)

### Phase 1: TDD-Katas (ca. 25–35 Minuten)
- **Team A (2–3 Personen):** FizzBuzz mit TDD
- **Team B (2–3 Personen):** String Calculator mit TDD
- Beide Teams arbeiten parallel und dokumentieren ihre TDD-Zyklen

### Phase 2: Erfahrungsaustausch & Cross-Testing (je Team ca. 7 Minuten)
- Kurze Präsentationen der Lösungen und Schilderung des Eindrucks von TDD für das Problem
- Hätten Sie die Lösung ohne TDD genauso implementiert?

### Phase 3: API-Mocking mit TDD (ca. 25–35 Minuten)
- **Team A:** Weather-API mocken (Temperatur → Wetterkategorie)
- **Team B:** Currency-API mocken (Wechselkurs → Bewertung)
- Testgetriebene Entwicklung mit gemockten API-Calls

---

## Arbeitsweise

**Test-Driven Development (TDD):**

1. **RED** – Test schreiben (Test schlägt fehl)
2. **GREEN** – minimalen Code schreiben (Test läuft korrekt durch)
3. **REFACTOR** – Code verbessern (ohne Funktionsänderung; Tests laufen weiterhin durch)

**Pair Programming:**

- Ein Studierender programmiert (Driver), der andere überprüft (Navigator)
- Rollenwechsel alle 10 Minuten (oder nach Phasenwechsel RED/GREEN/REFACTOR)
- Jeder Code entsteht testgetrieben!

**Dokumentation der Autorschaft:**

Dokumentieren Sie in Kommentaren am jeweiligen Test, wer welchen TDD-Schritt durchgeführt hat:

```python
# TDD-Zyklus 1: RED von [Kürzel1]
# TDD-Zyklus 1: GREEN von [Kürzel2]
# TDD-Zyklus 1: REFACTOR von [Kürzel1] & [Kürzel2]
```

---

## Phase 1: TDD-Katas

### Aufgabe 1: FizzBuzz mit TDD (Team A)

**Ziel:** Implementieren Sie die klassische FizzBuzz-Funktion vollständig testgetrieben.

**Regeln:**

- Zahl durch 3 teilbar → `"Fizz"`
- Zahl durch 5 teilbar → `"Buzz"`
- Zahl durch 3 **und** 5 teilbar → `"FizzBuzz"`
- Sonst: Zahl als String

**Dateien:**

- Tests: `Uebung4/Tests/test_fizzbuzz_kata.py`
- Implementierung: `Uebung4/Code/fizzbuzz_kata.py`

**Vorgehen:**

1. Schreiben Sie den einfachsten Test (z. B. `fizzbuzz(1) == "1"`)
2. Implementieren Sie **minimal**, um diesen Test zu bestehen
3. Fügen Sie den nächsten Test hinzu (z. B. `fizzbuzz(3) == "Fizz"`)
4. Erweitern Sie die Implementierung schrittweise
5. Refactoring nach jedem grünen Test

**Wichtige TDD-Prinzipien:**

- Starten Sie einfach
- Minimaler Code pro Test
- Ein Test nach dem anderen
- Regelmäßiges Refactoring

---

### Aufgabe 2: String Calculator mit TDD (Team B)

**Ziel:** Entwicklung eines String-basierten Addierers mit wachsender Funktionalität, vollständig testgetrieben.

**Basisregeln:**

- `""` → `0`
- `"1"` → `1`
- `"1,2"` → `3`
- `"1\n2,3"` → `6` (Newline als Trennzeichen)

**Erweiterungen (optional):**

1. Negative Zahlen werfen `ValueError` mit Liste der negativen Werte
2. Zahlen > 1000 werden ignoriert

**Dateien:**

- Tests: `Uebung4/Tests/test_string_calculator_kata.py`
- Implementierung: `Uebung4/Code/string_calculator_kata.py`

**Vorgehen:**

1. Beginnen Sie mit Basisfällen (`""`, `"1"`, `"1,2"`)
2. Erweitern Sie schrittweise das Parsing (`\n`-Unterstützung)
3. Fügen Sie optional Erweiterungen hinzu (negative Zahlen, >1000)
4. Refactoring: Extrahieren Sie Parsing-Logik in Hilfsfunktionen

**TDD-Checkliste:**

- Tests immer zuerst
- Jede Erweiterung durch neuen Test zuerst abdecken
- Fehlermeldungen getestet (negative Zahlen; Optional)

---

## Phase 2: Erfahrungsaustausch & Cross-Testing

### Aufgabe 3: Gegenseitige Präsentation

**Ziel:** Von anderen Teams lernen und unterschiedliche Lösungsansätze kennenlernen.

**Vorgehen:**

1. **Präsentation Team A (ca. 7 Minuten):**
   - Vorstellen der FizzBuzz-Lösung
   - Interessante TDD-Entscheidungen erläutern
   - Refactoring-Schritte erläutern
   - Herausforderungen und Learnings teilen

2. **Präsentation Team B (ca. 7 Minuten):**
   - Vorstellen der String Calculator-Lösung
   - TDD-Zyklus und Teststrategie erklären
   - Besondere Implementierungsdetails zeigen
   - Herausforderungen und Learnings teilen

3. **Kurze Diskussion (ca. 1 Minute):**
   - Welche unterschiedlichen Ansätze gab es?
   - Was können wir voneinander lernen?

---

## Phase 3: API-Mocking mit TDD

### Einführung: Was sind Mocks?

**Problem:** Externe APIs (Wetter, Währungen, ...) sind in Tests problematisch:
- Erfordern Netzwerkverbindung
- Liefern unterschiedliche Ergebnisse (nicht deterministisch)
- Können langsam oder teuer sein
- Sind in Entwicklungsumgebung oft nicht verfügbar

**Gleiches gilt z.B. auch für Datenbanken oder andere externe Abhängigkeiten!**

**Lösung: Mocks**
- Ersetzen echte API-Aufrufe durch simulierte Antworten
- Tests werden schnell, deterministisch und offline lauffähig
- Fokus auf die eigene Logik, nicht auf externe Dienste

**Werkzeuge:**
- `unittest.mock.patch` → ersetzt Funktionen temporär
- `unittest.mock.Mock` / `MagicMock` → erstellt Mock-Objekte
- `mock.return_value` → definiert Rückgabewert

**Beispiel:**
```python
from unittest.mock import patch

def test_api_call():
    with patch('requests.get') as mock_get:
        # Definiere simulierte API-Antwort
        mock_get.return_value.json.return_value = {"temp": 25}
        
        # Rufe Code auf, der requests.get verwendet
        result = my_function()
        
        # Prüfe Ergebnis basierend auf gemockter Antwort
        assert result == "angenehm"
```

---

### Aufgabe 4: Weather-API mit Mocking (Team A)

**Ziel:** Implementieren Sie testgetrieben einen Service, der Temperatur-Daten von einer Weather-API abruft und kategorisiert.

**Spezifikation:**

Die Funktion `get_weather_category(city: str) -> str` soll:
1. Die Weather-API aufrufen: `GET https://api.weather.com/current?city={city}`
2. Die Temperatur aus der JSON-Response extrahieren
3. Eine Kategorie basierend auf der Temperatur zurückgeben

**Temperatur-Kategorien:**

| Temperatur (°C) | Kategorie |
|-----------------|-----------|
| < 0 | `"frostgefahr"` |
| 0–10 | `"kalt"` |
| 11–15 | `"kühl"` |
| 16–24 | `"angenehm"` |
| 25–30 | `"warm"` |
| > 30 | `"heiß"` |

**Dateien:**

- Tests: `Uebung4/Tests/test_weather_service.py`
- Implementierung: `Uebung4/Code/weather_service.py`

**TDD-Vorgehen:**

1. **Test 1 (RED):** Test für `get_weather_category("Berlin")` mit gemockter API-Antwort `{"temperature": 20}`
   - Erwartung: `"angenehm"`
   - Implementierung fehlt noch → Test schlägt fehl

2. **Implementierung (GREEN):** Minimal-Implementierung, die Test bestehen lässt

3. **Refactoring:** Code strukturieren, ggf. Kategorisierung in separate Funktion

4. **Weitere Tests:** Andere Temperaturbereiche testen (<0, 0–10, 11–15, 25–30, >30)

**Mock-Hinweise:**

```python
from unittest.mock import patch
import requests

def test_angenehm():
    with patch('requests.get') as mock_get:
        # Simuliere API-Response
        mock_get.return_value.json.return_value = {"temperature": 20}
        
        result = get_weather_category("Berlin")
        assert result == "angenehm"
        
        # Optional: Verifiziere, dass API korrekt aufgerufen wurde
        mock_get.assert_called_once_with(
            "https://api.weather.com/current?city=Berlin"
        )
```

**Dynamische Mocks (abhängig vom Aufruf):**

Wenn die Mock-Antwort vom Parameter abhängen soll, können Sie eine Funktion verwenden:

```python
def mock_weather_api(url, **kwargs):
    """Einfache Mock-Funktion für verschiedene Städte."""
    if "Berlin" in url:
        return {"temperature": 20}  # angenehm
    elif "München" in url:
        return {"temperature": -5}  # frostgefahr
    else:
        return {"temperature": 25}  # warm (Standard)

def test_verschiedene_staedte():
    with patch('requests.get') as mock_get:
        # Mock-Funktion als return_value verwenden
        mock_get.return_value.json = mock_weather_api
        
        assert get_weather_category("Berlin") == "angenehm"
        assert get_weather_category("München") == "frostgefahr"
        assert get_weather_category("Hamburg") == "warm"
```

---

### Aufgabe 5: Currency-API mit Mocking (Team B)

**Ziel:** Implementieren Sie testgetrieben einen Service, der Wechselkurs-Daten von einer Currency-API abruft und bewertet.

**Spezifikation:**

Die Funktion `get_exchange_rate_assessment(from_currency: str, to_currency: str) -> str` soll:
1. Die Currency-API aufrufen: `GET https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}`
2. Den Wechselkurs aus der JSON-Response extrahieren
3. Eine Bewertung basierend auf dem Kurs zurückgeben

**Wechselkurs-Bewertungen (Beispiel: EUR → USD):**

| Wechselkurs | Bewertung |
|-------------|-----------|
| < 0.90 | `"sehr ungünstig"` |
| 0.90–0.99 | `"ungünstig"` |
| 1.00–1.09 | `"fair"` |
| 1.10–1.19 | `"günstig"` |
| ≥ 1.20 | `"sehr günstig"` |

**Dateien:**

- Tests: `Uebung4/Tests/test_currency_service.py`
- Implementierung: `Uebung4/Code/currency_service.py`

**TDD-Vorgehen:**

1. **Test 1 (RED):** Test für `get_exchange_rate_assessment("EUR", "USD")` mit gemockter API-Antwort `{"rate": 1.05}`
   - Erwartung: `"fair"`
   - Implementierung fehlt noch → Test schlägt fehl

2. **Implementierung (GREEN):** Minimal-Implementierung

3. **Refactoring:** API-Aufruf und Bewertungslogik trennen

4. **Weitere Tests:** Andere Kursbereiche testen (< 0.90, 0.90–0.99, 1.10–1.19, ≥ 1.20)

**Mock-Hinweise:**

```python
from unittest.mock import patch

def test_fair_rate():
    with patch('requests.get') as mock_get:
        # Simuliere API-Response
        mock_get.return_value.json.return_value = {"rate": 1.05}
        
        result = get_exchange_rate_assessment("EUR", "USD")
        assert result == "fair"
        
        # Optional: Verifiziere API-Aufruf
        mock_get.assert_called_once()
```

**Dynamische Mocks (abhängig vom Aufruf):**

Für verschiedene Währungspaare unterschiedliche Kurse mocken:

```python
def mock_currency_api(url, **kwargs):
    """Einfache Mock-Funktion für verschiedene Währungspaare."""
    if "EUR" in url and "USD" in url:
        return {"rate": 1.05}  # fair
    elif "EUR" in url and "GBP" in url:
        return {"rate": 0.85}  # ungünstig
    else:
        return {"rate": 1.15}  # günstig (Standard)

def test_verschiedene_waehrungen():
    with patch('requests.get') as mock_get:
        # Mock-Funktion als return_value verwenden
        mock_get.return_value.json = mock_currency_api
        
        assert get_exchange_rate_assessment("EUR", "USD") == "fair"
        assert get_exchange_rate_assessment("EUR", "GBP") == "ungünstig"
        assert get_exchange_rate_assessment("USD", "EUR") == "günstig"
```

Oder ganz einfach mit einem Dictionary:

```python
def test_verschiedene_waehrungen_einfach():
    rates = {
        ("EUR", "USD"): {"rate": 1.05},
        ("EUR", "GBP"): {"rate": 0.85},
        ("USD", "EUR"): {"rate": 1.15}
    }
    
    with patch('requests.get') as mock_get:
        # Lambda für schnelle dynamische Antworten
        mock_get.return_value.json = lambda: rates.get(
            tuple(mock_get.call_args[1]['url'].split('from=')[1].split('&to=')),
            {"rate": 1.05}
        )
        
        assert get_exchange_rate_assessment("EUR", "USD") == "fair"
        assert get_exchange_rate_assessment("EUR", "GBP") == "ungünstig"
```

---

## Checkliste für Abgabe

- Beide Katas (FizzBuzz, String Calculator) vollständig implementiert und getestet
- Beide Teams haben ihre Lösungen präsentiert und Erfahrungen ausgetauscht
- Beide API-Mocking-Aufgaben (Weather, Currency) testgetrieben implementiert
- Alle Tests laufen ohne echte API-Aufrufe
- Vollständig dokumentierte Autorschaft

---

## Reflexion (falls noch Zeit)

Diskutieren Sie abschließend in der Gruppe:

- Welche Vorteile bietet TDD bei neuen Features?
- Wie haben Mocks die Tests vereinfacht?
- Welche Herausforderungen gab es beim Mocken?
- Wann sollte man Mocks verwenden, wann echte Abhängigkeiten?

---

## Ausführungshinweise

**Tests ausführen:**

```bash
pytest Uebung4/Tests -v
```

**Einzelne Testdatei ausführen:**

```bash
pytest Uebung4/Tests/test_weather_service.py -v
```

**Mit Coverage-Report:**

```bash
pytest Uebung4/Tests --cov=Uebung4/Code --cov-report=html
```
