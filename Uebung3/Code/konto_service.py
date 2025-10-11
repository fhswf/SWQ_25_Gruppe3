# Implementiert von: RNSR und ANGE

"""
TODO: Implementieren Sie die KontoService-Klasse basierend auf dem KontoServiceInterface
"""

from decimal import Decimal
from typing import List, Dict
from .interfaces import KontoServiceInterface, KontoInterface


# TODO: Team B - Später ersetzt ihr diesen Import durch Team A's Implementation:
# from .konto import Konto


class KontoService(KontoServiceInterface):
    """
    TODO: Implementieren Sie diese Klasse

    HINWEIS für Team B - Parallele Entwicklung:
    - Arbeiten Sie mit dem KontoInterface, nicht der konkreten Konto-Klasse
    - Nutzen Sie die _create_konto() Factory-Methode für Konto-Erstellung
    - So können Sie sofort anfangen, ohne auf Team A zu warten!

    Funktionalitäten:
    - Konten verwalten (als List[KontoInterface])
    - Validierung der Benutzereingaben
    - Neue KontoID: max KontoID + 1
    - Export-Funktionen
    - Berechnungen
    """
    
    def __init__(self):
        # TODO: Team B - Implementierung
        self._konten: List[KontoInterface] = []
        

    def _create_konto(self, konto_id: int, saldo: Decimal) -> KontoInterface:
        """
        Factory-Methode für Konto-Erstellung - ermöglicht parallele Entwicklung!

        TODO: Team B - STARTEN SIE HIER! Diese Methode gibt Ihnen EXTREM EINFACHE Dummy-Objekte.

        JETZT: Verwenden Sie diese Dummy-Implementation für Ihre Service-Entwicklung
        SPÄTER: Ersetzen Sie durch `return Konto(konto_id, saldo)` wenn Team A fertig ist

        WICHTIG: Diese Dummy-Implementation macht fast NICHTS - das ist Absicht!
        Bei der Integration werden Sie Probleme entdecken, die Sie dann gemeinsam lösen.
        """
        # EXTREM EINFACHE DUMMY-IMPLEMENTATION für Team B:
        # Macht fast nichts, gibt nur konstante Werte zurück!
        class DummyKonto:
            def __init__(self, konto_id: int, saldo: Decimal):
                # Speichert die Werte, aber macht keine Validierung!
                pass

            @property
            def konto_id(self) -> int:
                return 1  # ← Immer konstant 1!

            @property
            def saldo(self) -> Decimal:
                return Decimal("100.00")  # ← Immer konstant 100!

            def einzahlen(self, betrag: Decimal) -> None:
                pass  # ← Macht nichts!

            def auszahlen(self, betrag: Decimal) -> None:
                pass  # ← Macht nichts, wirft keine Fehler!

        return DummyKonto(konto_id, saldo)

        # TODO: Team B - Später ersetzen Sie die obige Dummy-Implementation durch:
        # return Konto(konto_id, saldo)

    def konten_auflisten(self) -> List[Dict]:
        # TODO: Implementierung
        print(self._konten)
        return [{"konto_id": k.konto_id, "saldo": k.saldo} for k in self._konten]


    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        # TODO: Team B - Implementierung
        # Tipp: Nutzen Sie self._create_konto() für Konto-Erstellung!
        # Beispiel:
        # konto_id = self.get_max_konto_id() + 1
        # konto = self._create_konto(konto_id, saldo)
        # self._konten.append(konto)
        # return konto_id
        konto = self._create_konto(self.get_max_konto_id() + 1, saldo)
        self._konten.append(konto)
        return konto.konto_id
        

    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        sender = next((k for k in self._konten if k.konto_id == von_konto_id), None)
        receiver = next((k for k in self._konten if k.konto_id == zu_konto_id), None)
        if sender is None or receiver is None:
            raise ValueError("Eines der Konten existiert nicht.")
        if betrag <= 0:
            raise ValueError("Der Betrag muss positiv sein.")
        sender.auszahlen(betrag)
        receiver.einzahlen(betrag)

    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        self.ueberweisen(von_konto_id=zu_konto_id, zu_konto_id=von_konto_id, betrag=betrag)

    def get_max_konto_id(self) -> int:
        if not self._konten:
            return 0
        return max(k.konto_id for k in self._konten)

    def gesamtsaldo_berechnen(self) -> Decimal:
        return sum(k.saldo for k in self._konten)
