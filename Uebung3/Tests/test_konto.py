# Implementiert von: FARN und DLWG
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
from ..Code.konto import Konto


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
            Konto(1, None)
        with pytest.raises(ValueError):
            Konto(1, "abc")
        with pytest.raises(ValueError):
            Konto(1, Decimal("-50.00"))


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

    def test_property_konto_id(self):
        konto = Konto(1, Decimal("100.00"))
        assert konto.konto_id == 1

    def test_property_saldo(self):
        konto = Konto(1, Decimal("100.00"))
        assert konto.saldo == Decimal("100.00")


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

    def test_einzahlung_valid_amount(self):
        konto = Konto(1, Decimal("100.00"))
        konto.einzahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("150.00")

    def test_einzahlung_zero_amount(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("0.00"))

    def test_einzahlung_negative_amount(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(Decimal("-10.00"))

    def test_einzahlung_invalid_type(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.einzahlen(None)
        with pytest.raises(ValueError):
            konto.einzahlen("abc")


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

    def test_auszahlung_valid_amount(self):
        konto = Konto(1, Decimal("100.00"))
        konto.auszahlen(Decimal("50.00"))
        assert konto.saldo == Decimal("50.00")

    def test_auszahlung_insufficient_funds(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(RuntimeError):
            konto.auszahlen(Decimal("150.00"))

    def test_auszahlung_zero_amount(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("0.00"))

    def test_auszahlung_negative_amount(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(Decimal("-10.00"))

    def test_auszahlung_invalid_type(self):
        konto = Konto(1, Decimal("100.00"))
        with pytest.raises(ValueError):
            konto.auszahlen(None)
        with pytest.raises(ValueError):
            konto.auszahlen("abc")


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

    def test_grenzfall_grosse_betraege(self):
        konto = Konto(1, Decimal("1000000000.00"))
        konto.einzahlen(Decimal("500000000.00"))
        assert konto.saldo == Decimal("1500000000.00")
        konto.auszahlen(Decimal("200000000.00"))
        assert konto.saldo == Decimal("1300000000.00")

    def test_grenzfall_kleine_betraege(self):
        konto = Konto(1, Decimal("0.01"))
        konto.einzahlen(Decimal("0.02"))
        assert konto.saldo == Decimal("0.03")
        konto.auszahlen(Decimal("0.01"))
        assert konto.saldo == Decimal("0.02")

    def test_grenzfall_decimal_praezision(self):
        konto = Konto(1, Decimal("0.001"))
        konto.einzahlen(Decimal("0.002"))
        assert konto.saldo == Decimal("0.003")
        konto.auszahlen(Decimal("0.001"))
        assert konto.saldo == Decimal("0.002")

    def test_grenzfall_decimal_praezision_rounding(self):
        konto = Konto(1, Decimal("0.005"))
        konto.einzahlen(Decimal("0.005"))
        assert konto.saldo == Decimal("0.010")
        konto.auszahlen(Decimal("0.003"))
        assert konto.saldo == Decimal("0.007")

    def test_string_representation(self):
        konto = Konto(1, Decimal("100.00"))
        assert str(konto) is not None
        assert repr(konto) is not None

    def test_konto_equality(self):
        konto1 = Konto(1, Decimal("100.00"))
        konto2 = Konto(1, Decimal("100.00"))
        konto3 = Konto(2, Decimal("100.00"))
        assert konto1 != konto2  # Different instances
        assert konto1 != konto3  # Different IDs

# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation
