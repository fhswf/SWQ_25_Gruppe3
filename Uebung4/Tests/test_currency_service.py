"""
TDD-Template für Currency-API Service
=====================================

TODO: Team B - Implementiert get_exchange_rate_assessment() testgetrieben!

Aufgabe:
- Funktion ruft Currency-API auf (mocken!)
- Extrahiert Wechselkurs aus JSON
- Gibt Bewertung zurück basierend auf Kurs

Wechselkurs-Bewertungen (Beispiel: EUR → USD):
- < 0.90:     "sehr ungünstig"
- 0.90-0.99:  "ungünstig"
- 1.00-1.09:  "fair"
- 1.10-1.19:  "günstig"
- ≥ 1.20:     "sehr günstig"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from unittest.mock import patch

# TODO: Team B - Import nach erster Implementierung:
from ..Code.currency_service import get_exchange_rate_assessment


class TestCurrencyService:
    """
    Tests für Currency-API Service
    
    TDD-Vorgehen:
    1. Test schreiben (RED)
    2. Minimale Implementierung (GREEN)
    3. Refactoring
    """
    
    def test_placeholder(self):
        """
        Placeholder - ersetzt durch echte Tests!
        
        Beispiel-Tests:
        - Kurs 1.05 → "fair"
        - Kurs 0.85 → "sehr ungünstig"
        - Kurs 0.95 → "ungünstig"
        - Kurs 1.15 → "günstig"
        - Kurs 1.25 → "sehr günstig"
        """
        assert True, "TODO: Durch echte Tests ersetzen"

    def test_fair_rate(self):
        # TDD-Autor: [ANGE 19:19]
        # TDD-Zyklus 1: RED von [ANGE]
        # TDD-Zyklus 1: GREEN von [RNSR]
        # TDD-Zyklus 1: REFACTOR von [ANGE] & [RNSR]
        with patch('requests.get') as mock_get:
        # Simuliere API-Response
            mock_get.return_value.json.return_value = {"rate": 1.05}
        
            result = get_exchange_rate_assessment("EUR", "USD")
            assert result == "fair"
        
            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()
    
    def test_very_unfavorable_rate(self):
        # TDD-Autor: [RNSR 19:25]
        # TDD-Zyklus 2: RED von [RNSR]
        # TDD-Zyklus 2: GREEN von [ANGE]
        # TDD-Zyklus 2: REFACTOR von [ANGE] & [RNSR]
        with patch('requests.get') as mock_get:
        # Simuliere API-Response
            mock_get.return_value.json.return_value = {"rate": 0.85}
        
            result = get_exchange_rate_assessment("EUR", "USD")
            assert result == "sehr ungünstig"
        
            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()

    def test_unfavorable_rate(self):
        # TDD-Autor: [ANGE 19:32]
        # TDD-Zyklus 3: RED von [ANGE]
        # TDD-Zyklus 3: GREEN von [RNSR]
        # TDD-Zyklus 3: REFACTOR von [RNSR] & [ANGE]
        with patch('requests.get') as mock_get:
        # Simuliere API-Response
            mock_get.return_value.json.return_value = {"rate": 0.95}
        
            result = get_exchange_rate_assessment("EUR", "USD")
            assert result == "ungünstig"
        
            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()
    
    def test_favorable_rate(self):
        # TDD-Autor: [RNSR 19:40]
        # TDD-Zyklus 4: RED von [RNSR]
        # TDD-Zyklus 4: GREEN von [ANGE]
        # TDD-Zyklus 4: REFACTOR von [RNSR] & [ANGE]
        with patch('requests.get') as mock_get:
        # Simuliere API-Response
            mock_get.return_value.json.return_value = {"rate": 1.15}
        
            result = get_exchange_rate_assessment("EUR", "USD")
            assert result == "günstig"
        
            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()

    def test_very_favorable_rate(self):
        # TDD-Autor: [ANGE 19:44]
        # TDD-Zyklus 5: RED von [ANGE]
        # TDD-Zyklus 5: GREEN von [RNSR]
        # TDD-Zyklus 5: REFACTOR von [RNSR] & [ANGE]
        with patch('requests.get') as mock_get:
        # Simuliere API-Response
            mock_get.return_value.json.return_value = {"rate": 1.35}
        
            result = get_exchange_rate_assessment("EUR", "USD")
            assert result == "sehr günstig"
        
            # Optional: Verifiziere API-Aufruf
            mock_get.assert_called_once()
    
    # TODO: Team B - Beispiel für ersten echten Test:
    # def test_fair_rate(self):
    #     """TDD-Zyklus 1: RED von [Name] um [Zeit]"""
    #     with patch('requests.get') as mock_get:
    #         # Simuliere API-Response
    #         mock_get.return_value.json.return_value = {"rate": 1.05}
    #         
    #         result = get_exchange_rate_assessment("EUR", "USD")
    #         assert result == "fair"
    #         
    #         # Optional: Verifiziere API-Aufruf
    #         mock_get.assert_called_once()
    
    # TODO: Team B - Weitere Tests für alle Bewertungskategorien hinzufügen!
