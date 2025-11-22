#!/usr/bin/python3
def roman_to_int(roman_string):
    s = 0
    if not isinstance(roman_string, str):
        return None
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    for i in range(0, len(roman_string)):
        d = roman_string[i]
        e = roman_dict.get(d)
        s += e
    return s
