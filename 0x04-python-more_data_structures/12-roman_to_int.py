#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and \
            rom_n[roman_string[i]] < rom_n[roman_string[i + 1]]:
            sum -= rom_n[roman_string[i]]
        else:
            sum += rom_n[roman_string[i]]
    return sum
