"""
Hier sollen Sie Ihre Implementierung der Konto-Klasse erstellen.

TODO: Implementieren Sie die Konto-Klasse basierend auf dem KontoInterface
"""

from decimal import Decimal
from interfaces import KontoInterface

class Konto(KontoInterface):
    """
    TODO: Implementieren Sie diese Klasse
    
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """
    
    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if konto_id is None or not isinstance(konto_id, int):
            raise ValueError("konto_id muss eine numerische ID sein und darf nicht leer sein.")
        if saldo < Decimal('0.00'):
            raise ValueError("Startsaldo darf nicht negativ sein.")
        self._konto_id = konto_id
        self._saldo = saldo
    
    @property
    def konto_id(self) -> int:
        return self._konto_id
    
    @property
    def saldo(self) -> Decimal:
        return self._saldo
    
    def einzahlen(self, betrag: Decimal) -> None:
        if betrag is None:
            raise ValueError("Leere Einzahlungen sind nicht erlaubt.")
        if betrag < Decimal('0.00'):
            raise ValueError("Konto darf keine negative Einzahlung erhalten.")
        
        self._saldo += betrag

    def auszahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung

        if betrag is None:
            raise ValueError("Leere Auszahlungen sind nicht erlaubt.")
        if betrag < Decimal('0.00'):
            raise ValueError("Konto darf keine negative Auszahlung erhalten.")
        if self._saldo - betrag < Decimal('0.00'):
            raise ValueError("Konto darf nicht überzogen werden.")

        self._saldo -= betrag
