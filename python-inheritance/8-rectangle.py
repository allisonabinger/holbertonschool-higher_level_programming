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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
