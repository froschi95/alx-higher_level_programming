#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    del a_dictionary[key] if key in list(a_dictionary)
    return a_dictionary