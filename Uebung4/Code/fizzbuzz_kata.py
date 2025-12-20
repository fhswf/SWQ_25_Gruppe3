#Autoren: FARN und DLWG

"""
TDD Kata: FizzBuzz
Implementieren Sie die FizzBuzz-Funktion mit Test-Driven Development

Regeln:
1. Schreiben Sie zuerst einen Test (der fehlschlägt)
2. Schreiben Sie minimal nötigen Code, um den Test zu bestehen
3. Refactoring (Code verbessern ohne Funktionalität zu ändern)
4. Wiederholen Sie 1-3

FizzBuzz Regeln:
- Zahl durch 3 teilbar -> "Fizz"
- Zahl durch 5 teilbar -> "Buzz"  
- Zahl durch 3 UND 5 teilbar -> "FizzBuzz"
- Sonst -> Zahl als String
"""


def fizzbuzz(first: int, *others: int) -> str | list[str]:
    """
    Akzeptiert mindestens eine ganze Zahl und beliebig viele weitere.
    Gibt für jede Zahl das entsprechende FizzBuzz-Ergebnis als Liste von Strings zurück.

    Args:
        first: Mindestens eine positive Ganzzahl
        *others: Optionale weitere Ganzzahlen

    Returns:
        Liste von Strings mit "Fizz", "Buzz", "FizzBuzz" oder der Zahl als String
    """
    def _single(n: int) -> str:
        ret = ""
        if n % 3 == 0:
            ret += "Fizz"
        if n % 5 == 0:
            ret += "Buzz"
        if ret == "":
            return str(n)
        else:
            return ret

    if len(others) == 0:
        return _single(first)
    else:
        return [_single(n) for n in (first, *others)]
