#!/usr/bin/python3
"""defines class named rectangle"""
from models.base import Base


class Rectangle(Base):
    """new class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize new rectangle

        args:
            [all integers]
            width: width of rectangle
            height: height of rectangle
            x: x coordinate of rectangle
            y: y coordiate of rectangle
            id: identity of rectangle

        raises:
            TypeError:
                if width or heigh is not an integer
                if x or y is not an integer
            ValueError:
                if width or height is <= 0
                if x or y is < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints rectangle using # character to stdout"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """updates rectangle

            args:
                args(ints): new attribute values:
                    1st: id
                    2nd: width
                    3rd: height
                    4th: x
                    5th: y
                **kwargs (dict): new key/value pairs
        """
        if len(args) >= 2:
            setattr(self, 'width', args[1])
        if len(args) >= 3:
            setattr(self, 'height', args[2])
        if len(args) >= 4:
            setattr(self, 'x', args[3])
        if len(args) >= 5:
            setattr(self, 'y', args[4])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """returns print and str representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
