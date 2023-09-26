#!/usr/bin/python3
"""class-checking function"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a given class

        arguments:
            obj: object to check
            a_class: class to match to obj

        returns:
            true if match, false if not"""
    if type(obj) == a_class:
        return True
    return False
