#!/usr/bin/python3
def print_last_digit(number):
#     if number > 0:
    last = int(repr(number)[-1])
#     elif number < 0:
#         last = int(repr(number)[-1]) * -1
#     else:
#         last = 0
    print(f"{last}", end="")
    return last
