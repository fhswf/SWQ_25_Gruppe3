# Implementiert von: RNSR und ANGE
"""
TDD-Template für String Calculator Kata
=======================================

TODO: Team B - Entwickelt String Calculator mit TDD!

String Calculator-Regeln:
- Leerer String → 0
- Ein String mit einer Zahl → diese Zahl
- Zwei Zahlen mit Komma getrennt → Summe
- Beliebig viele Zahlen → Summe aller
- Neue Zeilen als Trenner erlaubt: "1\n2,3" → 6
- Optional: Custom Delimiter: "//;\n1;2" → 3

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

from dataclasses import dataclass
import pytest
import Uebung4.Code.string_calculator_kata

add = Uebung4.Code.string_calculator_kata.add

# TODO: Team B - Import nach erster Implementierung:
# from ..Code.string_calculator_kata import add


class TestStringCalculatorTDD:

    """
    TODO: Team B - Entwickelt String Calculator mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_add_empty_string_returns_zero(self):
        # TDD-Autor: [RNSR 10:41]
        # TDD-Zyklus 1: RED von [RNSR]
        # TDD-Zyklus 1: GREEN von [ANGE]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        result = add("")
        assert result == 0, "Empty string should return 0"

    def test_add_single_number_returns_number(self):
        # TDD-Autor: [ANGE 10:51]
        # TDD-Zyklus 1: RED von [ANGE]
        # TDD-Zyklus 1: GREEN von [RNSR]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        result = add("5")
        assert result == 5, "Single digit number should return itself"

    def test_add_two_single_digit_numbers(self):
        # TDD-Autor: [RNSR 10:55]
        # TDD-Zyklus 1: RED von [RNSR]
        # TDD-Zyklus 1: GREEN von [ANGE]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        result = add("2,4")
        assert result == 6, "Two single digit numbers should return their sum"

    def test_add_function_non_numeric_input(self):
        # TDD-Autor: [ANGE 11:05]
        # TDD-Zyklus 1: RED von [ANGE]
        # TDD-Zyklus 1: GREEN von [RNSR]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        with pytest.raises(ValueError) as excinfo:
            add("1,a")
        assert str(excinfo.value) == "Invalid input", "Invalid input should raise ValueError"


class TestStringCalculatorErweitert:
    """
    TODO: Team B - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_placeholder_extended_tests(self):
        """
        TODO: Team B - Entwickelt weitere Tests für String Calculator

        Ideen:
        - Custom Delimiters testen
        - Edge Cases (negative Zahlen, große Zahlen)
        - Parametrisierte Tests (@pytest.mark.parametrize)
        - Fehlerbehandlung (ungültige Eingaben)
        """
        # TODO: Erweiterte Tests hier
        assert True, "TODO: Erweiterte String Calculator-Tests implementieren"

    def test_newline_delimiter(self):
        # TDD-Autor: [RNSR 11:11]
        # TDD-Zyklus 1: RED von [RNSR]
        # TDD-Zyklus 1: GREEN von [ANGE]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        result = add("1\n6,2")
        assert result == 9, "New line as delimiter should be supported"

    def test_ignore_numbers_greater_than_1000(self):
        # TDD-Autor: [RNSR 11:31]
        # TDD-Zyklus 1: RED von [RNSR]
        # TDD-Zyklus 1: GREEN von [ANGE]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        result = add("2,1001,3")
        assert result == 5, "Numbers greater than 1000 should be ignored"

    def test_negative_number_raises_exception(self):
        # TDD-Autor: [ANGE 11:23]
        # TDD-Zyklus 1: RED von [ANGE]
        # TDD-Zyklus 1: GREEN von [RNSR]
        # TDD-Zyklus 1: REFACTOR von [RNSR] & [ANGE]
        with pytest.raises(ValueError) as excinfo:
            add("4,-5,6")
        assert str(excinfo.value) == "[-5]", "Negative numbers should raise ValueError with list of negatives"

# TODO: Team B - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [Was getestet] - Autor: [Name] - Zeit: [Zeit]
Implementation 1: [Minimale Lösung] - Zeit: [Zeit]

Test 2: [Was getestet] - Autor: [Name] - Zeit: [Zeit]
Refactoring: [Was geändert] - Zeit: [Zeit]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
- Unterschiede zu FizzBuzz?
"""
