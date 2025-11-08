# TODO: Implementiere den String Calculator mit TDD
# Hinweise: Beginne mit den Basisregeln ("" -> 0, "1" -> 1, "1,2" -> 3)
# Erweitere schrittweise mit Tests für \n, benutzerdefinierte Delimiter, etc.

def add(numbers: str) -> int:
    if "," in numbers:
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        total = 0
        for num in num_list:
            if num.isdigit():
                if int(num) < 0:
                    raise ValueError(f"[{num}]")
                if int(num) <= 1000:
                    total += int(num)
            else:
                raise ValueError("Invalid input")
        return total
    if numbers == "":
        return 0
    else:
        return int(numbers)
