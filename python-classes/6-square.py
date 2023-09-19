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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the # symbol"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
