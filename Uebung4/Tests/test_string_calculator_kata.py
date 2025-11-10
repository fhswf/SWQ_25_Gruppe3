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

    def test_add(self):
        @dataclass
        class TestCase:
            name: str
            input: str
            expected: int
            raises: Exception = None
            msg: str = None

        testCases = [
            # TDD-Autor: [RNSR 10:41]
            TestCase("Empty string returns 0", "", 0),
            # TDD-Autor: [ANGE 10:51]
            TestCase("Single number returns the number itself",
                     "5", 5),
            # TDD-Autor: [RNSR 10:55]
            TestCase("Two numbers return their sum", "2,4", 6),
            # TDD-Autor: [RNSR 11:05]
            TestCase("Faulty input raises exception", "1,a", None,
                     ValueError, "Invalid input"),
            # TDD-Autor: [ANGE 11:11]
            TestCase("New line as delimiter", "1\n6,2", 9),
            # TDD-Autor: [ANGE 11:23]
            TestCase("Negative numbers return ValueError and List of negatives",
                     "-9", None, ValueError, "[-9]"),
            # TDD-Autor: [RNSR 11:31]
            TestCase("Ignoring numbers greater than 1000",   "1\n1001,2,3", 6),
        ]

        for tc in testCases:
            if tc.raises:
                with pytest.raises(tc.raises) as excinfo:
                    add(tc.input)
                assert tc.msg == str(excinfo.value)

            else:
                result= add(tc.input)
                assert result == tc.expected, f"Failed: {tc.name}"


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
