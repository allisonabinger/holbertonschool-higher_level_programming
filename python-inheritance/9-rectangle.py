#!/usr/bin/python3
"""defines subclass rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using the class BaseGeometry"""

    def __init__(self, width, height):
        """initializes new rectangle

            args:
                width (int): width of the rectangle
                height (int): height of rectangle
            """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """implements area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the print and str reps of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
