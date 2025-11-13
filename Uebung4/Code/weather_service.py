"""
Implementierung: Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() hier!

Die Funktion soll:
1. Weather-API aufrufen (in Tests gemockt)
2. Temperatur extrahieren
3. Kategorie zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.weather.com/current?city={city}
- Response-Format: {"temperature": 20}
- Startet mit minimalster Implementierung!
"""

import requests


def get_weather_category(city: str) -> str | None:
    """
    Ruft Weather-API auf und gibt Temperatur-Kategorie zurück

    Args:
        city: Stadt, für die das Wetter abgefragt wird

    Returns:
        Temperatur-Kategorie als String:
        - "frostgefahr" (< 0°C)
        - "kalt" (0-10°C)
        - "kühl" (11-15°C)
        - "angenehm" (16-24°C)
        - "warm" (25-30°C)
        - "heiß" (> 30°C)
    """
    # TODO: Team A - Implementierung hier!
    # Tipp: Startet mit einfachstem Fall (z.B. nur "angenehm" zurückgeben)
    # Erweitert schrittweise basierend auf Tests!

    # API-Call-Code:
    url = f"https://api.weather.com/current?city={city}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    temperature = data.get("temperature")

    if temperature < 0:
        return "frostgefahr"
    elif temperature <= 10:
        return "kalt"
    elif temperature <= 15:
        return "kühl"
    elif temperature <= 24:
        return "angenehm"
    return None
