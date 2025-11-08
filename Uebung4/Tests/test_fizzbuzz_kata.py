"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from ..Code.fizzbuzz_kata import fizzbuzz

# TODO: Team A - Import nach erster Implementierung:
# from Teil2_TDD_und_Mocking.aufgaben.fizzbuzz_kata import fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_no_divisor(self):
        """
        TODO: Team A - Ersetzt diesen Placeholder durch euren ersten TDD-Test!

        Ideen für den ersten Test:
        - Was ist das einfachste Verhalten?
        - fizzbuzz(1) sollte was zurückgeben?

        TDD-Autor: [Name und Zeit]
        """
        # TODO: Euer erster TDD-Test hier

        assert fizzbuzz(1) == "1"

    def test_divisible_by_3(self):
        assert fizzbuzz(3) == "Fizz"

    def test_divisible_by_5(self):
        assert fizzbuzz(5) == "Buzz"

    def test_divisible_by_3_and_5(self):
        assert fizzbuzz(15) == "FizzBuzz"


class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_zero(self):
        assert fizzbuzz(0) == "FizzBuzz"

    def test_negative_number_no_divisor(self):
        assert fizzbuzz(-4) == "-4"
        assert fizzbuzz(-7) == "-7"
        assert fizzbuzz(-8) == "-8"

    def test_negative_number_divisible_by_3(self):
        assert fizzbuzz(-3) == "Fizz"
        assert fizzbuzz(-6) == "Fizz"
        assert fizzbuzz(-9) == "Fizz"

    def test_negative_number_divisible_by_5(self):
        assert fizzbuzz(-5) == "Buzz"
        assert fizzbuzz(-10) == "Buzz"
        assert fizzbuzz(-20) == "Buzz"

    def test_negative_number_divisible_by_3_and_5(self):
        assert fizzbuzz(-15) == "FizzBuzz"
        assert fizzbuzz(-30) == "FizzBuzz"
        assert fizzbuzz(-45) == "FizzBuzz"

    def test_big_number(self):
        assert fizzbuzz(999999) == "Fizz"
        assert fizzbuzz(1000000) == "Buzz"
        assert fizzbuzz(1500000) == "FizzBuzz"
        assert fizzbuzz(1000001) == "1000001"


# TODO: Team A - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [FizzBuzz(1) == "1"] - Autor: [FARN] - Zeit: [10:35]
Implementation 1: [return 1] : [10:36]
Refactoring 1: [if n%3 != 0 and n%5 != 0: return str(n)] - Zeit: [10:37]

Test 2: [FizzBuzz(3) - Autor: [DLWG] - Zeit: [10:40]
Implementation 1: [if n==3: return "Fizz"] : [10:42]
Refactoring 1: [if n%3 == 0] - Zeit: [10:43]

Test 3: [FizzBuzz(5) - Autor: [FARN] - Zeit: [10:45]
Implementation 1: [if n==5: return "Buzz"] : [10:46]
Refactoring 1: [if n%5 == 0] - Zeit: [10:47]

Test 4: [FizzBuzz(15) - Autor: [DLWG] - Zeit: [10:50]
Implementation 1: [if n==15: return "FizzBuzz"] : [10:51]
Refactoring 1: [if n%3==0 and n%5==0] - Zeit: [10:52]

Refactoring gesamt - Autor [DLWG,FARN]: Kombinieren der Bedingungen für Fizz, Buzz und FizzBuzz in String-Konkatenation 
Zeit: [10:55]



Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
"""
