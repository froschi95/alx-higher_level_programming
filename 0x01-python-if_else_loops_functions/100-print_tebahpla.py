#!/usr/bin/python3
for pos, letter in enumerate("abcdefghijklmnopqrstuvwxyz"[::-1]):
    if pos % 2 != 0:
        letter = chr(ord(letter) - 32)
    print('{}'.format(letter), end="")
