#!/usr/bin/python3
"""includes a class: Square, that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new square:

            args:
                size(int): size of square (length and width)
                x(int): x coordinate
                y(int): y coordinate
                id(int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        "getter for size"
        return self.width

    @size.setter
    def size(self, value):
        "setter: sets width and height to the same size"
        self.width = value
        self.height = value
