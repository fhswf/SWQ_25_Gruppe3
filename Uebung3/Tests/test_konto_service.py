# Implementiert von: RNSR und ANGE

import pytest
from decimal import Decimal

from ..Code.konto_service import KontoService
from ..Code.konto import Konto


@pytest.fixture
def service() -> KontoService:
    """Fixture: frischer KontoService pro Test."""
    return KontoService()

# ===============================================================
# 1. Service-Erstellung & Setup
# ===============================================================


class TestKontoServiceErstellung:
    """Tests für Service-Initialisierung und Grundzustand."""

    def test_service_startet_mit_leerer_kontenliste(self, service):
        # Arrange
        # (Service ist frisch erstellt durch Fixture)

        # Act
        konten = service.konten_auflisten()

        # Assert
        assert len(konten) == 0
        assert isinstance(konten, list)

    def test_service_typische_initialisierung(self):
        # Arrange / Act
        service = KontoService()

        # Assert
        assert isinstance(service, KontoService)
        assert service.get_max_konto_id() == 0

    def test_service_initialisierung_mit_konten(self):
        # Arrange
        service = KontoService()
        service.konto_erstellen(Decimal("100.00"))

        # Act / Assert
        assert isinstance(service, KontoService)
        assert service.get_max_konto_id() == 1
        assert len(service.konten_auflisten()) == 1


# ===============================================================
# 2. Konto-Verwaltung
# ===============================================================

class TestKontoVerwaltung:
    """Tests für Konto-Erstellung und Verwaltung."""

    def test_konto_erstellen_gueltig(self, service):
        # Arrange
        startsaldo = Decimal("100.00")

        # Act
        konto_id = service.konto_erstellen(startsaldo)

        # Assert
        konten = service.konten_auflisten()
        assert len(konten) == 1
        assert konten[0]["konto_id"] == konto_id
        assert konten[0]["saldo"] == startsaldo
    
    def test_konto_erstellen_negativer_saldo(self, service):
        # Arrange
        negativer_saldo = Decimal("-5.00")

        # Act / Assert
        with pytest.raises(ValueError):
            service.konto_erstellen(negativer_saldo)

    def test_konten_auflisten_mehrere(self, service):
        # Arrange
        service.konto_erstellen(Decimal("10.00"))
        service.konto_erstellen(Decimal("20.00"))

        # Act
        konten = service.konten_auflisten()

        # Assert
        assert len(konten) == 2
        assert all("konto_id" in k and "saldo" in k for k in konten)


# ===============================================================
# 3. Transaktions-Funktionen
# ===============================================================

class TestTransaktionen:
    """Tests für Geldbewegungen und Validierungen."""

    def test_ueberweisen_erfolgreich(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("200.00"))
        zu_konto_id = service.konto_erstellen(Decimal("50.00"))
        betrag = Decimal("25.00")

        # Act
        service.ueberweisen(von_konto_id, zu_konto_id, betrag)

        # Assert
        konten = {k["konto_id"]: k["saldo"]
                  for k in service.konten_auflisten()}
        assert konten[von_konto_id] == Decimal("175.00")
        assert konten[zu_konto_id] == Decimal("75.00")

    def test_ueberweisen_ungueltiger_betrag(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("100.00"))
        zu_konto_id = service.konto_erstellen(Decimal("50.00"))
        betrag = Decimal("-10.00")

        # Act / Assert
        with pytest.raises(ValueError):
            service.ueberweisen(von_konto_id, zu_konto_id, betrag)

    def test_ueberweisen_von_nicht_existierendes_konto(self, service):
        # Arrange
        zu_konto_id = service.konto_erstellen(Decimal("100.00"))
        unbekannt = 999

        # Act / Assert
        with pytest.raises(ValueError):
            service.ueberweisen(unbekannt, zu_konto_id, Decimal("10.00"))

    def test_ueberweisen_an_nicht_existierendes_konto(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("100.00"))
        unbekannt = 999

        # Act / Assert
        with pytest.raises(ValueError):
            service.ueberweisen(von_konto_id, unbekannt, Decimal("10.00"))

    def test_ueberweisen_ueberziehung(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("20.00"))
        zu_konto_id = service.konto_erstellen(Decimal("10.00"))
        betrag = Decimal("30.00")

        # Act / Assert
        with pytest.raises(RuntimeError):
            service.ueberweisen(von_konto_id, zu_konto_id, betrag)

    def test_einziehen_gleich_ueberweisung(self, service):
        # Arrange
        start_betrag_von_konto = Decimal("50.00")
        start_betrag_zu_konto = Decimal("200.00")

        transaktions_betrag = Decimal("25.00")

        end_betrag_von_konto = Decimal("25.00")
        end_betrag_zu_konto = Decimal("225.00")

        einziehen_von_konto_id = service.konto_erstellen(Decimal(start_betrag_von_konto))
        einziehen_zu_konto_id = service.konto_erstellen(Decimal(start_betrag_zu_konto))

        ueberweisen_von_konto_id = service.konto_erstellen(Decimal(start_betrag_von_konto))
        ueberweisen_zu_konto_id = service.konto_erstellen(Decimal(start_betrag_zu_konto))

        # Act
        service.einziehen(einziehen_von_konto_id, einziehen_zu_konto_id, transaktions_betrag)
        service.ueberweisen(ueberweisen_von_konto_id, ueberweisen_zu_konto_id, transaktions_betrag)

        # Assert
        konten = {k["konto_id"]: k["saldo"]
                  for k in service.konten_auflisten()}
        assert konten[einziehen_von_konto_id] == end_betrag_von_konto
        assert konten[ueberweisen_von_konto_id] == end_betrag_von_konto
        assert konten[einziehen_zu_konto_id] == end_betrag_zu_konto
        assert konten[ueberweisen_zu_konto_id] == end_betrag_zu_konto

    def test_einziehen_erfolgreich(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("150.00"))
        zu_konto_id = service.konto_erstellen(Decimal("75.00"))
        betrag = Decimal("50.00")

        # Act
        service.einziehen(von_konto_id, zu_konto_id, betrag)

        # Assert
        konten = {k["konto_id"]: k["saldo"]
                  for k in service.konten_auflisten()}
        assert konten[von_konto_id] == Decimal("100.00")
        assert konten[zu_konto_id] == Decimal("125.00")

    def test_einziehen_ungueltiger_betrag_null(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("50.00"))
        zu_konto_id = service.konto_erstellen(Decimal("200.00"))
        betrag = Decimal("0.00")

        # Act / Assert
        with pytest.raises(ValueError):
            service.einziehen(von_konto_id, zu_konto_id, betrag)

    def test_einziehen_ungueltiger_betrag_negativ(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("50.00"))
        zu_konto_id = service.konto_erstellen(Decimal("200.00"))
        betrag = Decimal("-10.00")

        # Act / Assert
        with pytest.raises(ValueError):
            service.einziehen(von_konto_id, zu_konto_id, betrag)

    def test_einziehen_von_nicht_existierendes_konto(self, service):
        # Arrange
        zu_konto_id = service.konto_erstellen(Decimal("100.00"))
        unbekannt = 999

        # Act / Assert
        with pytest.raises(ValueError):
            service.einziehen(unbekannt, zu_konto_id, Decimal("10.00"))

    def test_einziehen_an_nicht_existierendes_konto(self, service):
        # Arrange
        von_konto_id = service.konto_erstellen(Decimal("100.00"))
        unbekannt = 999

        # Act / Assert
        with pytest.raises(ValueError):
            service.einziehen(von_konto_id, unbekannt, Decimal("10.00"))

# ===============================================================
# 4. Saldo-Funktionen
# ===============================================================


class TestSaldoFunktionen:
    """Tests für Saldo-Abfragen und Berechnungen."""

    def test_gesamtsaldo_leer(self, service):
        # Arrange / Act
        gesamtsaldo = service.gesamtsaldo_berechnen()

        # Assert
        assert gesamtsaldo == Decimal("0.00")

    def test_gesamtsaldo_ein_konto(self, service):
        # Arrange
        service.konto_erstellen(Decimal("10.00"))

        # Act
        result = service.gesamtsaldo_berechnen()

        # Assert
        assert result == Decimal("10.00")

    def test_gesamtsaldo_mehrere_konten(self, service):
        # Arrange
        service.konto_erstellen(Decimal("10.00"))
        service.konto_erstellen(Decimal("20.00"))
        service.konto_erstellen(Decimal("30.00"))

        # Act
        gesamtsaldo = service.gesamtsaldo_berechnen()

        # Assert
        assert gesamtsaldo == Decimal("60.00")


# ===============================================================
# 5. Utility-Funktionen
# ===============================================================

class TestUtilityFunktionen:
    """Tests für ID-Verwaltung."""

    def test_get_max_konto_id_bei_leerem_service(self, service):
        # Arrange / Act
        max_id = service.get_max_konto_id()

        # Assert
        assert max_id == 0

    def test_erste_konto_id(self, service):
        # Arrange/Act
        erste_id = service.konto_erstellen(Decimal("0.00"))

        # Assert
        assert erste_id == 1

    def test_get_max_konto_id_nach_mehreren_konten(self, service):
        # Arrange
        id1 = service.konto_erstellen(Decimal("0.00"))
        id2 = service.konto_erstellen(Decimal("0.00"))

        # Act
        result = service.get_max_konto_id()

        # Assert
        assert result == id2
        assert id2 == id1 + 1
        assert result == id2
    
    def test_keine_doppelten_ids(self, service):
        # Arrange
        ids = set()
        anzahl_konten = 1000

        # Act
        for _ in range(anzahl_konten):
            konto_id = service.konto_erstellen(Decimal("0.00"))
            ids.add(konto_id)

        # Assert
        assert len(ids) == anzahl_konten


# ===============================================================
# 6. Integrationstest
# ===============================================================

class TestKontoServiceIntegration:
    """Integrationstest zwischen Service und Konto."""

    def test_vollstaendiger_workflow(self, service):
        # Arrange
        id1 = service.konto_erstellen(Decimal("100.00"))
        id2 = service.konto_erstellen(Decimal("50.00"))
        id3 = service.konto_erstellen(Decimal("0.00"))

        # Act
        # Schritt 1: Überweisung
        service.ueberweisen(id1, id2, Decimal("20.00"))
        # Schritt 2: Einzug (Rückbuchung)
        service.einziehen(id2, id3, Decimal("10.00"))

        # Assert
        konten = {k["konto_id"]: k["saldo"]
                  for k in service.konten_auflisten()}
        assert konten[id1] == Decimal("80.00")
        assert konten[id2] == Decimal("60.00")
        assert konten[id3] == Decimal("10.00")
        assert service.gesamtsaldo_berechnen() == Decimal("150.00")
