#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    s = 0
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    leng = len(roman_string)
    for i in range(l):
        e = roman_dict[roman_string[i]]
        if i < leng - 1 and e < roman_dict[roman_string[i + 1]]:
            s -= e
        else:
            s += e
    return s
