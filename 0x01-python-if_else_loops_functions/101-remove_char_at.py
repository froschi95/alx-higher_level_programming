#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    new_str = str.replace(str[n], "")
    return new_str
