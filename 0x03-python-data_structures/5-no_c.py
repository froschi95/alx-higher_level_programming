#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        letter = '' if letter in 'cC'
    return my_string
