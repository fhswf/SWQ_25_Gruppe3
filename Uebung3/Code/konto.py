# Implementiert von: FARN und DLWG
"""
Hier sollen Sie Ihre Implementierung der Konto-Klasse erstellen.

TODO: Implementieren Sie die Konto-Klasse basierend auf dem KontoInterface
"""

from decimal import Decimal
from .interfaces import KontoInterface


class Konto(KontoInterface):
    """
    TODO: Implementieren Sie diese Klasse

    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """

    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        """
        Konstruktor; erstellt Objekt der Klasse Konto

        Args:
            konto_id(int): ID des Kontos
            saldo(Decimal, > 0): Startkontostand

        """
        if konto_id is None or not isinstance(konto_id, int) or konto_id <= 0:
            raise ValueError(
                "konto_id muss eine numerische ID sein und darf nicht leer sein.")
        if not isinstance(saldo, Decimal):
            raise ValueError("Saldo muss vom Typ Decimal sein.")
        if saldo < Decimal('0.00'):
            raise ValueError("Startsaldo darf nicht negativ sein.")
        self._konto_id = konto_id
        self._saldo = saldo

    def __str__(self):
        """
        Wandelt Konto-Objekt in seine String-Repräsentation um

        """
        return super().__str__() + f" (ID: {self._konto_id}, Saldo: {self._saldo})"

    def __repr__(self):
        """
        Wandelt Konto-Objekt in seine String-Repräsentation um

        """
        return super().__repr__() + f" (ID: {self._konto_id}, Saldo: {self._saldo})"

    @property
    def konto_id(self) -> int:
        """
        Gibt Konto-ID des Objekts zurück

        Return:
            _konto_id(int): ID des Kontos
        """
        return self._konto_id

    @property
    def saldo(self) -> Decimal:
        """
        Gibt aktuellen Saldo des Kontos zurück

        Return:
            _saldo(Decimal): Kontostand
        """
        return self._saldo

    def einzahlen(self, betrag: Decimal) -> None:
        """
        Schreibt übergebenen Betrag dem Konto gut und zahlt ein

        Args:
            betrag(Decimal, > 0): Einzuzahlender Betrag

        """
        if betrag is None:
            raise ValueError("Leere Einzahlungen sind nicht erlaubt.")
        if not isinstance(betrag, Decimal):
            raise ValueError("Betrag muss vom Typ Decimal sein.")
        if betrag <= Decimal('0.00'):
            raise ValueError("Konto darf keine negative Einzahlung erhalten.")

        self._saldo += betrag

    def auszahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung
        """
        Reduziert Kontostand um übergebenen Betrag und zahlt aus

        Args:
            betrag(Decimal, > 0, <= _saldo): Auszuzahlender Betrag
        """
        if betrag is None:
            raise ValueError("Leere Auszahlungen sind nicht erlaubt.")
        if not isinstance(betrag, Decimal):
            raise ValueError("Betrag muss vom Typ Decimal sein.")
        if betrag <= Decimal('0.00'):
            raise ValueError("Konto darf keine negative Auszahlung erhalten.")
        if self._saldo - betrag < Decimal('0.00'):
            raise RuntimeError("Konto darf nicht überzogen werden.")

        self._saldo -= betrag
