#!/usr/bin/python3
"""Contains the clas "Student"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance
        with specified attributes"""
        obj = (self.__dict__)
        if not attrs:
            return obj
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = obj[i]
            return new_dict
