#!/usr/bin/python3
"""defines class Square with specifications"""


class Square:
    """reps a square"""

    def __init__(self, size=0):
        """initializes new square"""

        self.size = size

    @property
    def size(self):
        """gets current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets size to valid integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2
