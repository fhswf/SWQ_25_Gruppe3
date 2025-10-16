# Implementiert von: RNSR und ANGE

"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================

TODO: Team B - Implementieren Sie hier Ihre Tests NACH der KontoService-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die KontoService-Klasse in Code/konto_service.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Service
3. Testen Sie alle Service-Methoden gründlich
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für Service-Tests:
- Nutzen Sie pytest fixtures für Setup/Teardown
- Testen Sie Integration zwischen Service und Konto-Klasse
- Testen Sie sowohl normale als auch Grenzfälle
- Testen Sie Validierungslogik im Service
"""

import pytest
from decimal import Decimal

# TODO: Team B - Entkommentieren Sie nach Ihrer Implementierung:
from ..Code.konto_service import KontoService
from ..Code.konto import Konto

@pytest.fixture
def service():
    return KontoService()

class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    TODO: Team B - Testet Service-Initialisierung
    """
    def test_service_initialisierung(self, service):
        assert isinstance(service, KontoService)
        assert service.konten_auflisten() == []

    def test_placeholder_service_erstellung(self):
        """
        Placeholder-Test - ersetzen Sie diesen durch echte Tests!

        Beispiele für Tests:
        - Service ohne Parameter erstellen
        - Service mit initialen Konten erstellen
        - Service-Zustand nach Erstellung prüfen
        """
        # TODO: Team B - Ersetzen Sie diesen Placeholder durch echte Tests
        assert True, "Placeholder - bitte durch echte Tests ersetzen!"

        # Beispiel-Code (entkommentiert nach Implementierung):
        # service = KontoService()
        # assert len(service.konten_auflisten()) == 0


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    TODO: Team B - Testet alle Konto-Verwaltungs-Funktionen
    """
    def test_konto_erstellen(self, service):
        konto_id = service.konto_erstellen(Decimal("100.00"))
        konten = service.konten_auflisten()
        assert len(konten) == 1
        assert konten[0]["saldo"] == Decimal("100.00")
        assert konto_id == konten[0]["konto_id"]

    def test_get_max_konto_id(self, service):
        id1 = service.konto_erstellen()
        id2 = service.konto_erstellen()
        assert id2 > id1
        assert service.get_max_konto_id() == id2

    def test_placeholder_konto_erstellen(self):
        """TODO: Team B - Tests für konto_erstellen()"""
        # Beispiel-Tests:
        # - Konto mit gültigem Saldo erstellen
        # - Konto-ID wird automatisch vergeben
        # - Konto wird zur internen Liste hinzugefügt
        # - Rückgabe der Konto-ID
        # - Erstellen mit ungültigem Saldo → Exception?
        assert True, "TODO: Tests für konto_erstellen implementieren"

    def test_placeholder_konten_auflisten(self):
        """TODO: Team B - Tests für konten_auflisten()"""
        # Beispiel-Tests:
        # - Leere Liste bei Service-Start
        # - Liste nach Konto-Erstellung
        # - Korrekte Anzahl und Inhalte
        assert True, "TODO: Tests für konten_auflisten implementieren"

class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    TODO: Team B - Testet alle Geldtransaktionen über den Service
    """
    def test_ueberweisen(self, service):
        id1 = service.konto_erstellen(Decimal("200.00"))
        id2 = service.konto_erstellen(Decimal("50.00"))
        service.ueberweisen(id1, id2, Decimal("25.00"))
        konten = {k["konto_id"]: k["saldo"] for k in service.konten_auflisten()}
        assert konten[id1] == Decimal("175.00")
        assert konten[id2] == Decimal("75.00")

    def test_ueberweisen_negativer_betrag(self, service):
        id1 = service.konto_erstellen(Decimal("100.00"))
        id2 = service.konto_erstellen(Decimal("50.00"))
        with pytest.raises(ValueError):
            service.ueberweisen(id1, id2, Decimal("-10.00"))

    def test_ueberweisen_unbekanntes_konto(self, service):
        id1 = service.konto_erstellen(Decimal("100.00"))
        with pytest.raises(ValueError):
            service.ueberweisen(id1, 999, Decimal("10.00"))

    def test_placeholder_einzahlen(self):
        """TODO: Team B - Tests für einzahlen()"""
        # Beispiel-Tests:
        # - Einzahlung auf existierendes Konto
        # - Saldo wird korrekt erhöht
        # - Einzahlung auf nicht-existierendes Konto → Exception?
        # - Ungültiger Betrag → Exception?
        assert True, "TODO: Tests für einzahlen implementieren"

    def test_placeholder_auszahlen(self):
        """TODO: Team B - Tests für auszahlen()"""
        # Beispiel-Tests:
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        # - Auszahlung bei unzureichendem Saldo → Exception?
        # - Auszahlung von nicht-existierendem Konto → Exception?
        assert True, "TODO: Tests für auszahlen implementieren"

    def test_placeholder_ueberweisen(self):
        """TODO: Team B - Tests für ueberweisen()"""
        # Beispiel-Tests:
        # - Überweisung zwischen existierenden Konten
        # - Sender-Saldo wird reduziert
        # - Empfänger-Saldo wird erhöht
        # - Überweisung bei unzureichendem Saldo → Exception?
        # - Überweisung an nicht-existierendes Konto → Exception?
        # - Überweisung von nicht-existierendem Konto → Exception?
        assert True, "TODO: Tests für ueberweisen implementieren"


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    TODO: Team B - Testet Saldo-Abfragen und -Berechnungen
    """
    def test_gesamtsaldo_leer(self, service):
        assert service.gesamtsaldo_berechnen() == Decimal("0.00")

    def test_gesamtsaldo_mehrere(self, service):
        service.konto_erstellen(Decimal("10.00"))
        service.konto_erstellen(Decimal("20.00"))
        assert service.gesamtsaldo_berechnen() == Decimal("30.00")

    def test_placeholder_gesamtsaldo(self):
        """TODO: Team B - Tests für gesamtsaldo()"""
        # Beispiel-Tests:
        # - Gesamtsaldo bei leerer Kontenliste (0)
        # - Gesamtsaldo mit einem Konto
        # - Gesamtsaldo mit mehreren Konten
        # - Korrekte Summe aller Salden
        assert True, "TODO: Tests für gesamtsaldo implementieren"

class TestIntegration:
    """
    Integration tests for KontoService.

    This test class verifies the complete workflow of the account management system,
    ensuring that all components work together correctly.
    """
    def test_vollstaendiger_workflow(self, service):
        # 1. Zwei Konten erstellen
        id1 = service.konto_erstellen(Decimal("100.00"))
        id2 = service.konto_erstellen(Decimal("50.00"))

        # 2. Überweisung
        service.ueberweisen(id1, id2, Decimal("25.00"))

        # 3. Gesamtsaldo prüfen
        assert service.gesamtsaldo_berechnen() == Decimal("150.00")

        # 4. Konten prüfen
        konten = {k["konto_id"]: k["saldo"] for k in service.konten_auflisten()}
        assert konten[id1] == Decimal("75.00")
        assert konten[id2] == Decimal("75.00")

class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    TODO: Team B - Testet ID-Verwaltung und Export-Funktionen
    """

    def test_placeholder_get_max_konto_id(self):
        """TODO: Team B - Tests für get_max_konto_id()"""
        # Beispiel-Tests:
        # - Erste ID ist 1
        # - IDs werden fortlaufend vergeben
        # - Keine doppelten IDs
        assert True, "TODO: Tests für get_max_konto_id implementieren"

class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    TODO: Team B - Testet das Zusammenspiel aller Komponenten
    """

    def test_placeholder_vollstaendiger_workflow(self):
        """TODO: Team B - Test für kompletten Workflow"""
        # Beispiel-Test:
        # 1. Service erstellen
        # 2. Mehrere Konten erstellen
        # 3. Einzahlungen durchführen
        # 4. Überweisungen durchführen
        # 5. Gesamtsaldo prüfen
        assert True, "TODO: Integration-Test implementieren"
