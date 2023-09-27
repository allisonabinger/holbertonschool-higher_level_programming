#!/usr/bin/python3
"""function to check if instance is inherited"""


def inherits_from(obj, a_class):
    """function that checks if instance is inherited directly
    or indirectly from a specified class

        args:
            obj: object to check
            a_class: parent class

        returns: true if so, false if not"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
