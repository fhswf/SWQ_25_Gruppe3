"""
Interfaces für die Banking-Anwendung - Teil 1

Diese Datei enthält die Interfaces/Abstraktionen, die implementiert werden sollen.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from decimal import Decimal


class KontoInterface(ABC):
    """Interface für die Konto-Klasse"""
    
    @abstractmethod
    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        """
        Initialisiert ein neues Konto
        
        Args:
            konto_id: Die eindeutige Konto-ID (muss numerisch und nicht leer sein)
            saldo: Der Anfangssaldo (Standard: 0.00)
            
        Raises:
            ValueError: Wenn konto_id leer oder nicht numerisch ist
        """
        pass
    
    @property
    @abstractmethod
    def konto_id(self) -> int:
        """Gibt die Konto-ID zurück"""
        pass
    
    @property
    @abstractmethod
    def saldo(self) -> Decimal:
        """Gibt den aktuellen Saldo zurück"""
        pass
    
    @abstractmethod
    def einzahlen(self, betrag: Decimal) -> None:
        """
        Zahlt einen Betrag auf das Konto ein
        
        Args:
            betrag: Der einzuzahlende Betrag
            
        Raises:
            ValueError: Wenn der Betrag negativ oder null ist
        """
        pass
    
    @abstractmethod
    def auszahlen(self, betrag: Decimal) -> None:
        """
        Zahlt einen Betrag vom Konto aus
        
        Args:
            betrag: Der auszuzahlende Betrag
            
        Raises:
            ValueError: Wenn der Betrag negativ oder null ist
            RuntimeError: Wenn das Konto überzogen würde (Saldo < 0)
        """
        pass


class KontoServiceInterface(ABC):
    """Interface für den Konto-Service"""
    
    @abstractmethod
    def __init__(self):
        """Initialisiert den KontoService"""
        pass
    
    @abstractmethod
    def konten_auflisten(self) -> List[Dict]:
        """
        Listet alle Konten auf
        
        Returns:
            Liste von Dictionaries mit Konto-Informationen
        """
        pass
    
    @abstractmethod
    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        """
        Erstellt ein neues Konto
        
        Args:
            saldo: Der Anfangssaldo
            
        Returns:
            Die ID des neu erstellten Kontos
        """
        pass
    
    @abstractmethod
    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        """
        Überweist von einem Konto zu einem anderen
        
        Args:
            von_konto_id: Quell-Konto-ID
            zu_konto_id: Ziel-Konto-ID
            betrag: Der Betrag
            
        Raises:
            ValueError: Bei ungültigen Eingaben
            RuntimeError: Bei Überziehung
        """
        pass
    
    @abstractmethod
    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        """
        Zieht von einem Konto zu einem anderen ein (umgekehrte Überweisung)
        
        Args:
            von_konto_id: Konto von dem eingezogen wird
            zu_konto_id: Konto das einzieht
            betrag: Der Betrag
            
        Raises:
            ValueError: Bei ungültigen Eingaben
            RuntimeError: Bei Überziehung
        """
        pass
    
    @abstractmethod
    def get_max_konto_id(self) -> int:
        """
        Gibt die aktuell größte Konto-ID zurück
        
        Returns:
            Die größte Konto-ID oder 0 wenn keine Konten existieren
        """
        pass
    
    @abstractmethod
    def gesamtsaldo_berechnen(self) -> Decimal:
        """
        Berechnet den Gesamtsaldo aller Konten
        
        Returns:
            Die Summe aller Kontosalden
        """
        pass
