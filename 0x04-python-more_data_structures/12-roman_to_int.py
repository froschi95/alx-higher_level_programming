#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    look_up = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = result = 0
    for ch in roman_string:
        result += look_up[ch] if look_up[ch] <= prev else look_up[ch] - prev * 2
        prev = look_up[ch]
    return result
