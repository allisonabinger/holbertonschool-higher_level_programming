#!/usr/bin/python3
"""class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance or inherited instance of a class

        Args:
            obj: object to check
            a_class: class to reference
        Returns:
            true if either, false if not"""
    if isinstance(obj, a_class):
        return True
    return False
