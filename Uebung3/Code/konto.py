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
        # TODO: Implementierung
        pass
    
    @property
    def konto_id(self) -> int:
        # TODO: Implementierung
        pass
    
    @property
    def saldo(self) -> Decimal:
        # TODO: Implementierung
        pass
    
    def einzahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung
        pass
    
    def auszahlen(self, betrag: Decimal) -> None:
        # TODO: Implementierung
        pass
