"""
Test-Template für die Konto-Klasse (Test-After Approach)
========================================================

TODO: Team A - Implementieren Sie hier Ihre Tests NACH der Konto-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die Konto-Klasse in Code/konto.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Code
3. Testen Sie normale Fälle UND Grenzfälle
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für gute Tests:
- Verwenden Sie aussagekräftige Test-Namen
- Testen Sie eine Sache pro Test
- Nutzen Sie pytest.raises() für Exception-Tests
- Denken Sie an Grenzwerte (0, negative Zahlen)
"""

import pytest
from decimal import Decimal

# TODO: Team A - Entkommentiert nach eurer Implementierung:
from Uebung3.Code.konto import Konto


class TestKontoErstellung:
    """
    Tests für die Konto-Erstellung
    TODO: Team A - Implementieren Sie Tests für den Konstruktor
    """

    def test_placeholder_konto_erstellung(self):
        """
        Placeholder-Test - ersetzen Sie diesen durch echte Tests!

        Beispiele für Tests, die Sie schreiben könnten:
        - Konto mit gültiger ID und positivem Saldo erstellen
        - Konto mit gültiger ID und Saldo 0 erstellen  
        - Konto mit ungültiger ID (negativ, 0, String) → Exception?
        - Konto mit ungültigem Saldo (negativ, String) → Exception?
        """
        # TODO: Team A - Ersetzen Sie diesen Placeholder durch echte Tests
        # Beispiel-Code (entkommentiert nach Implementierung):
        # konto = Konto(1, Decimal("100.00"))
        # assert konto.konto_id == 1
        # assert konto.saldo == Decimal("100.00")
        
    def test_create_konto_with_valid_id_and_positive_balance(self):
        """Konto mit gültiger ID und positivem Saldo erstellen"""
        konto = Konto(1, Decimal("100.00"))
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")
    
    def test_create_konto_with_valid_id_and_zero_balance(self):
        """Konto mit gültiger ID und Saldo 0 erstellen"""
        konto = Konto(2, Decimal("0.00"))
        assert konto.konto_id == 2
        assert konto.saldo == Decimal("0.00")

    def test_create_konto_with_invalid_id(self):
        """Konto mit ungültiger ID (negativ, 0, String,None) → Exception?"""
        with pytest.raises(ValueError):
            Konto(-1, Decimal("100.00"))
        with pytest.raises(ValueError):
            Konto(0, Decimal("100.00"))
        with pytest.raises(ValueError):
            Konto("abc", Decimal("100.00"))
        with pytest.raises(ValueError):
            Konto(None, Decimal("100.00"))
    
         
    def test_create_konto_with_invalid_balance(self):
        """Konto mit ungültigem Saldo (negativ, String) → Exception?"""
        with pytest.raises(ValueError):
            Konto(1, Decimal("-50.00"))
        with pytest.raises(ValueError):
            Konto(1, "abc")




class TestKontoEigenschaften:
    """
    Tests für Konto-Eigenschaften (Properties)
    TODO: Team A - Testet konto_id und saldo Properties
    """

    def test_placeholder_eigenschaften(self):
        """TODO: Team A - Tests für Properties"""
        # Beispiel-Tests:
        # - konto.konto_id gibt korrekte ID zurück
        # - konto.saldo gibt korrekten Saldo zurück
        # - Properties sind read-only (falls gewünscht)
        assert True, "TODO: Tests für Eigenschaften implementieren"


class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    TODO: Team A - Testet alle Einzahlungs-Szenarien
    """

    def test_placeholder_einzahlung(self):
        """TODO: Team A - Tests für einzahlen() Methode"""
        # Beispiel-Tests:
        # - Einzahlung von positivem Betrag
        # - Saldo wird korrekt erhöht
        # - Einzahlung von 0 → Exception?
        # - Einzahlung von negativem Betrag → Exception?
        # - Einzahlung von ungültigem Typ → Exception?
        assert True, "TODO: Tests für Einzahlung implementieren"


class TestAuszahlung:
    """
    Tests für die Auszahlungs-Funktionalität  
    TODO: Team A - Testet alle Auszahlungs-Szenarien
    """

    def test_placeholder_auszahlung(self):
        """TODO: Team A - Tests für auszahlen() Methode"""
        # Beispiel-Tests:
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        # - Auszahlung bei unzureichendem Saldo → Exception?
        # - Auszahlung von 0 → Exception?
        # - Auszahlung von negativem Betrag → Exception?
        # - Überziehung vermeiden
        assert True, "TODO: Tests für Auszahlung implementieren"


class TestKontoGrenzfaelle:
    """
    Tests für Grenzfälle und Besonderheiten
    TODO: Team A - Testet Edge Cases und besondere Situationen
    """

    def test_placeholder_grenzfaelle(self):
        """TODO: Team A - Tests für Grenzfälle"""
        # Beispiel-Tests:
        # - Sehr große Beträge
        # - Sehr kleine Beträge (Cent-Bereich)
        # - Decimal-Präzision
        # - String-Repräsentation (__str__, __repr__)
        # - Gleichheit von Konten
        assert True, "TODO: Tests für Grenzfälle implementieren"


# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation