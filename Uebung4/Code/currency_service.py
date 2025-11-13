"""
Implementierung: Currency-API Service
=====================================

TODO: Team B - Implementiert get_exchange_rate_assessment() hier!

Die Funktion soll:
1. Currency-API aufrufen (in Tests gemockt)
2. Wechselkurs extrahieren
3. Bewertung zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}
- Response-Format: {"rate": 1.05}
- Startet mit minimalster Implementierung!
"""

import requests


def get_exchange_rate_assessment(from_currency: str, to_currency: str) -> str:
     url = (
         f"https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}")

     response = requests.get(url, timeout=5)
     response.raise_for_status()

     data = response.json()
     rate = data.get("rate")

     if rate < 0.90:
        return "sehr ungünstig"
     elif rate < 1.00:
        return "ungünstig"
     elif rate < 1.10:
        return "fair"
     
     


"""
    Ruft Currency-API auf und gibt Bewertung des Wechselkurses zurück
    
    Args:
        from_currency: Ausgangswährung (z.B. "EUR")
        to_currency: Zielwährung (z.B. "USD")
        
    Returns:
        Bewertung als String:
        - "sehr ungünstig" (< 0.90)
        - "ungünstig" (0.90-0.99)
        - "fair" (1.00-1.09)
        - "günstig" (1.10-1.19)
        - "sehr günstig" (≥ 1.20)
    """
    # TODO: Team B - Implementierung hier!
    # Tipp: Startet mit einfachstem Fall (z.B. nur "fair" zurückgeben)
    # Erweitert schrittweise basierend auf Tests!
    # 
    # API-Call-Code:
    # url = (
    #     f"https://api.exchangerate.com/convert?from={from_currency}&to={to_currency}"
    # )
    # response = requests.get(url, timeout=5)
    # response.raise_for_status()
    # data = response.json()
    # rate = data.get("rate")
