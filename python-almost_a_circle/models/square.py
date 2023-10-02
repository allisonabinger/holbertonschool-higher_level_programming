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

    def update(self, *args, **kwargs):
        """updates each attribute of square

            args:
                args(ints): new attribute values:
                    1st: id
                    2nd: width
                    3rd: size
                    4th: x
                    5th: y
                **kwargs (dict): new key/value pairs
        """
        if len(args) >= 1:
            setattr(self, 'id', args[0])
        if len(args) >= 2:
            setattr(self, 'size', args[1])
        if len(args) >= 3:
            setattr(self, 'x', args[2])
        if len(args) >= 3:
            setattr(self, 'y', args[3])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return(
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            )
