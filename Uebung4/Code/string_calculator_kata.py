# TODO: Implementiere den String Calculator mit TDD
# Hinweise: Beginne mit den Basisregeln ("" -> 0, "1" -> 1, "1,2" -> 3)
# Erweitere schrittweise mit Tests für \n, benutzerdefinierte Delimiter, etc.

def add(numbers: str) -> int:
    if "," in numbers:
        numbers = numbers.replace("\n", ",")
        num_list = numbers.split(",")
        total = 0
        contains_negative = False
        negative_numbers = []
        for num in num_list:
            if is_integer_string(num):
                if int(num) < 0:
                    contains_negative = True
                    negative_numbers.append(num)
                if int(num) <= 1000:
                    total += int(num)
            else:
                print(num)
                raise ValueError("Invalid input")
        if contains_negative:
            raise ValueError(f"[{','.join(negative_numbers)}]")
        return total
    if numbers == "":
        return 0
    else:
        return int(numbers)


def is_integer_string(num_str: str) -> bool:
    try:
        int(num_str)
        return True
    except ValueError:
        return False