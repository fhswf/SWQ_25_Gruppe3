# Python Testing mit pytest - Kurze Einführung

## Was ist Testing?

**Tests** sind Code-Stücke, die überprüfen, ob Ihr Code korrekt funktioniert:

- **Automatisch**: Tests laufen ohne manuelle Eingaben
- **Wiederholbar**: Gleiche Tests, gleiche Ergebnisse
- **Dokumentation**: Tests zeigen, wie Code verwendet werden soll

## pytest Basics

### Test-Dateien erstellen

```python
# test_beispiel.py
def test_simple_addition():
    result = 2 + 3
    assert result == 5  # Test bestanden

def test_string_length():
    text = "Hallo"
    assert len(text) == 5  # Test bestanden

def test_failing_example():
    assert 1 == 2  #  Test schlägt fehl
```

### Tests ausführen

```bash
# Alle Tests ausführen:
pytest

# Mit Details:
pytest -v

# Nur bestimmte Datei:
pytest test_beispiel.py

# Nur bestimmten Test:
pytest test_beispiel.py::test_simple_addition
```

## Assert-Statements

### Basis-Assertions

```python
def test_assertions():
    # Gleichheit prüfen
    assert 5 == 5
    assert "hello" == "hello"

    # Ungleichheit prüfen
    assert 5 != 3
    assert "a" != "b"

    # Wahrheitswerte
    assert True
    assert not False

    # Größer/Kleiner
    assert 10 > 5
    assert 3 < 7
    assert 5 >= 5
    assert 4 <= 4

    # Listen/Collections
    assert [1, 2, 3] == [1, 2, 3]
    assert len([1, 2, 3]) == 3
    assert 2 in [1, 2, 3]
    assert 5 not in [1, 2, 3]
```

### Decimal-Assertions (wichtig für Geld!)

```python
from decimal import Decimal

def test_decimal_money():
    saldo = Decimal("100.50")

    # Exact gleich
    assert saldo == Decimal("100.50")  # Richtig

    # NIEMALS mit float vergleichen!
    # assert saldo == 100.50  # Kann unerwartete Ergebnisse geben!

    # Berechnungen
    nach_einzahlung = saldo + Decimal("25.25")
    assert nach_einzahlung == Decimal("125.75")
```

## Exceptions testen

### pytest.raises verwenden

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Division durch Null nicht erlaubt")
    return a / b

def test_division_by_zero():
    # Test, dass Exception geworfen wird:
    with pytest.raises(ValueError):
        divide(10, 0)

    # Test mit spezifischer Fehlermeldung:
    with pytest.raises(ValueError, match="Division durch Null nicht erlaubt"):
        divide(5, 0)

    # Normale Division sollte funktionieren:
    result = divide(10, 2)
    assert result == 5
```

## Test-Klassen organisieren

```python
class TestKonto:
    """Alle Tests für die Konto-Klasse"""

    def test_konto_creation(self):
        # Test für Konto-Erstellung
        pass

    def test_einzahlung(self):
        # Test für Einzahlungen
        pass

    def test_auszahlung(self):
        # Test für Auszahlungen
        pass

class TestKontoService:
    """Alle Tests für den KontoService"""

    def test_service_creation(self):
        # Test für Service-Erstellung
        pass
```

## Setup und Teardown

### Für jeden Test (setup_method)

```python
from decimal import Decimal

class TestKonto:
    def setup_method(self):
        """Wird vor JEDEM Test ausgeführt"""
        self.test_konto = Konto(1, Decimal("100.00"))

    def test_saldo_abrufen(self):
        # self.test_konto ist verfügbar
        assert self.test_konto.saldo == Decimal("100.00")

    def test_einzahlung(self):
        # Jeder Test bekommt ein frisches test_konto
        self.test_konto.einzahlen(Decimal("50.00"))
        assert self.test_konto.saldo == Decimal("150.00")
```

## Gute Test-Patterns

### Test-Benennung

```python
# Gute Namen - beschreiben WAS getestet wird:
def test_konto_creation_with_valid_id():
def test_einzahlung_increases_saldo():
def test_auszahlung_with_insufficient_funds_raises_error():

#  Schlechte Namen:
def test_1():
def test_stuff():
def test_konto():
```

### AAA-Pattern (Arrange-Act-Assert)

```python
def test_einzahlung_increases_saldo():
    # Arrange - Setup
    konto = Konto(1, Decimal("100.00"))
    einzahlungsbetrag = Decimal("50.00")

    # Act - Aktion ausführen
    konto.einzahlen(einzahlungsbetrag)

    # Assert - Ergebnis prüfen
    expected_saldo = Decimal("150.00")
    assert konto.saldo == expected_saldo
```

### Ein Test, eine Sache

```python
# Gut - testet nur Einzahlung:
def test_einzahlung_increases_saldo():
    konto = Konto(1, Decimal("100.00"))
    konto.einzahlen(Decimal("50.00"))
    assert konto.saldo == Decimal("150.00")

# Schlecht - testet zu viele Dinge:
def test_konto_operations():
    konto = Konto(1, Decimal("100.00"))
    konto.einzahlen(Decimal("50.00"))  # Einzahlung
    assert konto.saldo == Decimal("150.00")
    konto.auszahlen(Decimal("25.00"))  # Auszahlung
    assert konto.saldo == Decimal("125.00")
    # Zu komplex - schwer zu debuggen!
```

---

## Import-Best Practices

### Relative vs. Absolute Imports

**Verwenden Sie relative Imports innerhalb eines Packages:**

```python
# In Tests/test_konto.py
from ..Code.konto import Konto
from ..Code.interfaces import KontoInterface

# Statt absoluter Imports:
# from Uebungen.Uebungsblatt3.Code.konto import Konto
```

**Vorteile relativer Imports:**

- **Flexibler**: Funktionieren auch wenn das Package umbenannt wird
- **Wartbarer**: Weniger abhängig von der absoluten Pfadstruktur
- **Sauberer**: Kürzer und fokussierter auf die lokale Struktur

**Wann relative Imports verwenden:**

- Innerhalb desselben Packages (z.B. Tests → Code)
- Bei eng zusammengehörigen Modulen
- Wenn das Package als Einheit entwickelt wird

**Wann absolute Imports verwenden:**

- Für externe Libraries (`import pytest`, `from fastapi import FastAPI`)
- Bei Package-übergreifenden Imports
- Wenn explizite Pfade gewünscht sind
