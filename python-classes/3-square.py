#!/usr/bin/python3
"""defines class Square with specifications"""


class Square:

    """instance of a square"""

    def __init__(self, size=0):
        """initializes a new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """returns area of a square (size^2)"""
        return self.__size ** 2
