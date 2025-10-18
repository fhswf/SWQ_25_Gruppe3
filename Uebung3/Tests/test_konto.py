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


    def test_placeholder_konto_erstellung(self):

        Placeholder-Test - ersetzen Sie diesen durch echte Tests!

        Beispiele für Tests, die Sie schreiben könnten:
        - Konto mit gültiger ID und positivem Saldo erstellen
        - Konto mit gültiger ID und Saldo 0 erstellen
        - Konto mit ungültiger ID (negativ, 0, String) → Exception?
        - Konto mit ungültigem Saldo (negativ, String) → Exception?

        # TODO: Team A - Ersetzen Sie diesen Placeholder durch echte Tests
        # Beispiel-Code (entkommentiert nach Implementierung):
        # konto = Konto(1, Decimal("100.00"))
        # assert konto.konto_id == 1
        # assert konto.saldo == Decimal("100.00")

    """

    def test_create_konto_with_valid_id_and_positive_balance(self):
        """
        Konto mit gültiger ID und positivem Saldo erstellen
        """
        # Arrange/Act
        konto = Konto(1, Decimal("100.00"))
        # Assert
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

    def test_create_konto_with_valid_id_and_zero_balance(self):
        """
        Konto mit gültiger ID und Saldo 0 erstellen
        """
        # Arrange/Act
        konto = Konto(2, Decimal("0.00"))
        # Assert
        assert konto.konto_id == 2
        assert konto.saldo == Decimal("0.00")

    # Arrange
    @pytest.mark.parametrize(
        "kto_id", [-1, 0, "abc", None],
        ids=["negative ID", "0", "String", "none"]
    )
    def test_create_konto_with_invalid_id(self, kto_id):
        """
        Konto mit ungültiger ID (negativ, 0, String,None) → Exception?
        """
        # Arrange
        saldo = Decimal("100.00")
        # Act / Assert
        with pytest.raises(ValueError):
            Konto(kto_id, saldo)

    @pytest.mark.parametrize(
        "balance", [None, "abc", Decimal("-50.00")],
        ids=["none", "String", "negative balance"]
    )
    def test_create_konto_with_invalid_balance(self, balance):
        """
        Konto mit ungültigem Saldo (None, String, negativ) → Exception?
        """
        # Arrange
        kto_id = 1
        # Act / Assert
        with pytest.raises(ValueError):
            Konto(kto_id, balance)


class TestKontoEigenschaften:
    """
    Tests für Konto-Eigenschaften (Properties)
    TODO: Team A - Testet konto_id und saldo Properties

    """
    """
    def test_placeholder_eigenschaften(self):
        ###TODO: Team A - Tests für Properties
        # Beispiel-Tests:
        # - konto.konto_id gibt korrekte ID zurück
        # - konto.saldo gibt korrekten Saldo zurück
        # - Properties sind read-only (falls gewünscht)
        assert True, "TODO: Tests für Eigenschaften implementieren"
    """

    def test_property_konto_id(self):
        """
        konto.konto_id gibt korrekte ID zurück
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        # Act
        konto = Konto(kto_id, saldo)
        # Assert
        assert konto.konto_id == kto_id

    def test_property_saldo(self):
        """
        Testet, ob konto.saldo korrekten Saldo zurückgibt
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        # Act
        konto = Konto(kto_id, saldo)
        # Assert
        assert konto.saldo == saldo


class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    TODO: Team A - Testet alle Einzahlungs-Szenarien
    """
    """
    def test_placeholder_einzahlung(self):
        ### TODO: Team A - Tests für einzahlen() Methode
        # Beispiel-Tests:
        # - Einzahlung von positivem Betrag
        # - Saldo wird korrekt erhöht
        # - Einzahlung von 0 → Exception?
        # - Einzahlung von negativem Betrag → Exception?
        # - Einzahlung von ungültigem Typ → Exception?
        assert True, "TODO: Tests für Einzahlung implementieren"
    """

    def test_einzahlung_valid_amount(self):
        """
        Testet Einzahlung von positivem Betrag
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        einzahlung = Decimal("50.00")
        # Act
        konto = Konto(kto_id, saldo)
        konto.einzahlen(einzahlung)
        # Assert
        assert konto.saldo == Decimal(saldo+einzahlung)

    def test_einzahlung_zero_amount(self):
        """
        Testet, ob Einzahlung von 0 ValueError wirft
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        konto = Konto(kto_id, saldo)
        einzahlung = Decimal("0.00")
        # Act / Assert
        with pytest.raises(ValueError):
            konto.einzahlen(einzahlung)

    def test_einzahlung_negative_amount(self):
        """
        Testet. on negative Einzahlung Value Error wirft
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        konto = Konto(kto_id, saldo)
        einzahlung = Decimal("-10.00")
        # Act / Assert
        with pytest.raises(ValueError):
            konto.einzahlen(einzahlung)

    # Arrange
    @pytest.mark.parametrize(
        "amount", [None, "abc", []],
        ids=["None", "String", "List"]
    )
    def test_einzahlung_invalid_type(self, amount):
        """
        Testet, ob ungültiger Typ im Einzahlungsbetrag (!Decimal) ValueError wirft
        """
        # Arrange
        konto = Konto(1, Decimal("100.00"))
        # Act / Assert
        with pytest.raises(ValueError):
            konto.einzahlen(amount)


class TestAuszahlung:
    """
    Tests für die Auszahlungs-Funktionalität
    TODO: Team A - Testet alle Auszahlungs-Szenarien
    """

    """
    def test_placeholder_auszahlung(self):
        ###TODO: Team A - Tests für auszahlen() Methode
        # Beispiel-Tests:
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        # - Auszahlung bei unzureichendem Saldo → Exception?
        # - Auszahlung von 0 → Exception?
        # - Auszahlung von negativem Betrag → Exception?
        # - Überziehung vermeiden
        assert True, "TODO: Tests für Auszahlung implementieren"
    """

    def test_auszahlung_valid_amount(self):
        """
        Testet, ob Auszahlung gelingt und Saldo reduziert wird
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        konto = Konto(kto_id, saldo)
        auszahlung = Decimal("50.00")
        # Act
        konto.auszahlen(auszahlung)
        # Assert
        assert konto.saldo == Decimal(saldo - auszahlung)

    def test_auszahlung_insufficient_funds(self):
        """
        Testet, ob Auszahlung bei unzureichendem Saldo RuntimeError wirft
        """
        # Arrange
        konto = Konto(1, Decimal("100.00"))
        auszahlung = Decimal("150.00")
        # Act / Assert
        with pytest.raises(RuntimeError):
            konto.auszahlen(auszahlung)

    def test_auszahlung_zero_amount(self):
        """
        Testet, ob Auszahlungsbetrag von 0 ValueError wirft
        """
        # Arrange
        konto = Konto(1, Decimal("100.00"))
        auszahlung = Decimal("0.00")
        # Act / Assert
        with pytest.raises(ValueError):
            konto.auszahlen(auszahlung)

    def test_auszahlung_negative_amount(self):
        """
        Testet, ob negativer  Auszahlungsbetrag Value Error wirft
        """
        # Arrange
        konto = Konto(1, Decimal("100.00"))
        auszahlung = Decimal("-10.00")
        # Act / Asssert
        with pytest.raises(ValueError):
            konto.auszahlen(auszahlung)

    # Arrange
    @pytest.mark.parametrize(
        "amount", [None, "abc", []],
        ids=["None", "String", "List"]
    )
    def test_auszahlung_invalid_type(self, amount):
        """
        Testet, ob ungültiger Typ im Auzszahlungsbetrag(!Decimal) ValueError wirft
        """
        konto = Konto(1, Decimal("100.00"))
        # Act / Assert
        with pytest.raises(ValueError):
            konto.auszahlen(amount)


class TestKontoGrenzfaelle:
    """
    Tests für Grenzfälle und Besonderheiten
    TODO: Team A - Testet Edge Cases und besondere Situationen

    """

    """

    def test_placeholder_grenzfaelle(self):
        # TODO: Team A - Tests für Grenzfälle
        # Beispiel-Tests:
        # - Sehr große Beträge
        # - Sehr kleine Beträge (Cent-Bereich)
        # - Decimal-Präzision
        # - String-Repräsentation (__str__, __repr__)
        # - Gleichheit von Konten
        assert True, "TODO: Tests für Grenzfälle implementieren"
    """

    def test_grenzfall_grosse_betraege_bewegen(self):
        """
        Testet, ob Ein- und Auszahlung großer Beträge auf großen Kontostand
        richtigen Kontostand hervorruft
        """
        # Arrange
        saldo = Decimal("1000000000.00")
        einzahlung = Decimal("500000000.00")
        auszahlung = Decimal("200000000.00")
        konto = Konto(1, saldo)
        # Act
        konto.einzahlen(Decimal("500000000.00"))
        # Assert
        assert konto.saldo == Decimal(saldo+einzahlung)
        # Arrange
        new_saldo = konto.saldo
        konto.auszahlen(auszahlung)
        # Assert
        assert konto.saldo == Decimal(new_saldo-auszahlung)

    def test_grenzfall_kleine_betraege(self):
        """
        Testet, ob Ein- und Auszahlung kleiner Beträge auf kleinen Kontostand
        richtigen Kontostand hervorruft
        """
        # Arrange
        saldo = Decimal("0.01")
        einzahlung = Decimal("0.02")
        auszahlung = Decimal("0.01")
        konto = Konto(1, saldo)
        # Act
        konto.einzahlen(Decimal("0.02"))
        # Assert
        assert konto.saldo == Decimal(saldo+einzahlung)
        # Arrange
        new_saldo = konto.saldo
        # Act
        konto.auszahlen(auszahlung)
        # Assert
        assert konto.saldo == Decimal(new_saldo-auszahlung)

    def test_grenzfall_decimal_praezision(self):
        """
        Testet, ob bei Ein- und Auszahlung extrem kleiner Beträge die Dezimalstellen
        des Kontostandes exakt bleiben
        """
        # Arrange
        saldo = Decimal("0.0001")
        einzahlung = Decimal("0.0002")
        auszahlung = Decimal("0.0001")
        konto = Konto(1, saldo)

        # Act
        konto.einzahlen(einzahlung)
        # Assert
        assert konto.saldo == Decimal(saldo+einzahlung)
        # Arrange
        new_saldo = konto.saldo
        # Act
        konto.auszahlen(auszahlung)
        assert konto.saldo == Decimal(new_saldo-auszahlung)

    def test_string_representation(self):
        """
        Testet ob Stringrepräsentationen wie erwartet dargestellt werden
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        konto = Konto(kto_id, saldo)
        expected_string_str = object.__str__(konto) + \
            f" (ID: {kto_id}, Saldo: {saldo})"
        expected_string_repr = object.__repr__(konto) + \
            f" (ID: {kto_id}, Saldo: {saldo})"
        # Act / Assert
        assert str(konto) == expected_string_str
        assert repr(konto) == expected_string_repr

    def test_konto_equality(self):
        """         
        Testet, ob zwei verschiedene Kontoinstanzen
        mit gleicher ID und gleichem Saldo als gleich gelten;
        testet __eq__-Methode
        """
        # Arrange
        kto_id = 1
        saldo = Decimal("100.00")
        # Act
        konto1 = Konto(kto_id, saldo)
        konto2 = Konto(kto_id, saldo)
        # Assert
        assert konto1 == konto2  # Dasselbe Konto
        assert konto1 is not konto2  # Aber nicht dieselbe Instanz

# TODO: Team A - Erweitern Sie diese Klassen oder fügen Sie neue hinzu!
# Weitere mögliche Test-Klassen:
# - TestKontoStringRepresentation
# - TestKontoEquality
# - TestKontoValidation
