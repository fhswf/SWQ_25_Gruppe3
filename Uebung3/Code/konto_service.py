# Implementiert von: RNSR und ANGE


from decimal import Decimal
from typing import List, Dict

from .konto import Konto
from .interfaces import KontoServiceInterface, KontoInterface


class KontoService(KontoServiceInterface):
    """
    Die Klasse KontoService implementiert zentrale Funktionen eines Bank-Backends.

    Verantwortlichkeiten:
    - Verwaltung aller Konten (Erstellung, Auflistung)
    - Durchführung von Transaktionen (Überweisung, Einzug)
    - Berechnung aggregierter Werte (Gesamtsaldo)
    """

    def __init__(self):
        """
        Initialisiert den KontoService mit einer leeren Kontenliste.
        """
        self._konten: List[KontoInterface] = []

    # ---------------------------------------------------------------
    # Kontoerstellung & Auflistung
    # ---------------------------------------------------------------

    def _create_konto(self, konto_id: int, saldo: Decimal) -> KontoInterface:
        """
        Factory-Methode für Konto-Erstellung.

        Args:
            konto_id (int): Die eindeutige ID des neuen Kontos.
            saldo (Decimal): Der Startsaldo des neuen Kontos.

        Returns:
            KontoInterface: Das neu erstellte Kontoobjekt.
        """
        return Konto(konto_id, saldo)

    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        """
        Erstellt ein neues Konto mit automatischer ID-Vergabe.

        Args:
            saldo (Decimal): Startsaldo des Kontos (Standard 0.00).

        Returns:
            int: Die Konto-ID des neu erstellten Kontos.

        Raises:
            ValueError: Wenn der Startsaldo negativ ist.
        """
        if saldo < 0:
            raise ValueError("Negativer Startsaldo ist nicht erlaubt.")

        konto = self._create_konto(self.get_max_konto_id() + 1, saldo)
        self._konten.append(konto)
        return konto.konto_id

    def konten_auflisten(self) -> List[Dict]:
        """
        Gibt eine Liste aller Konten mit ID und Saldo zurück.

        Returns:
            List[Dict]: Liste von Dictionaries mit Konto-ID und Saldo.
        """
        return [{"konto_id": k.konto_id, "saldo": k.saldo} for k in self._konten]

    # ---------------------------------------------------------------
    # Transaktionen
    # ---------------------------------------------------------------

    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        """
        Führt eine Überweisung zwischen zwei Konten aus.

        Args:
            von_konto_id (int): ID des Quellkontos.
            zu_konto_id (int): ID des Zielkontos.
            betrag (Decimal): Zu überweisender Betrag.

        Raises:
            ValueError: Wenn Betrag ungültig ist oder Konto fehlt.
            RuntimeError: Wenn das Quellkonto überzogen würde.
        """
        if betrag <= 0:
            raise ValueError("Der Betrag muss positiv sein.")

        sender = next(
            (k for k in self._konten if k.konto_id == von_konto_id), None)
        receiver = next(
            (k for k in self._konten if k.konto_id == zu_konto_id), None)

        if sender is None or receiver is None:
            raise ValueError("Eines der Konten existiert nicht.")

        sender.auszahlen(betrag)
        receiver.einzahlen(betrag)

    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        """
        Führt eine Rückbuchung (Einzug) durch – inverse Überweisung.

        Args:
            von_konto_id (int): ID des Kontos, von dem eingezogen wird.
            zu_konto_id (int): ID des Kontos, das den Betrag erhält.
            betrag (Decimal): Betrag des Einzugs.

        Raises:
            ValueError: Bei ungültigen Eingaben.
        """
        if betrag <= 0:
            raise ValueError("Der Betrag muss positiv sein.")

        self.ueberweisen(von_konto_id, zu_konto_id, betrag)

    # ---------------------------------------------------------------
    # Hilfs- & Analysefunktionen
    # ---------------------------------------------------------------

    def get_max_konto_id(self) -> int:
        """
        Gibt die höchste Konto-ID zurück.

        Returns:
            int: Höchste Konto-ID oder 0, wenn keine Konten existieren.
        """
        return max((k.konto_id for k in self._konten), default=0)

    def gesamtsaldo_berechnen(self) -> Decimal:
        """
        Berechnet den Gesamtsaldo aller Konten.

        Returns:
            Decimal: Summe aller Kontosalden.
        """
        return sum((k.saldo for k in self._konten), Decimal('0.00'))
