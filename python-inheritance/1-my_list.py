#!/usr/bin/python3
"""Subclass named MyList inherited from list"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()


    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
