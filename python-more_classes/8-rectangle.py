#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Attributes-
        number of instances of the rectangle
        print_symbol: symbol use for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public inst method: area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public inst method: perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """determines rectangle with greater area
        takes 2 rectangles as arguments
        raises type error if either rectangles arent valid rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area:
            return (rect_1)
        return(rect_2)

    def __str__(self):
        """returns printable rep of the rectangle
        represented with the # symbol"""
        if self.__width == 0 or self.__height == 0:
            return("")

        r = []
        for i in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """string representation of the rectangle"""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """prints goodbye message thats so sad :( lol
        as well as removes 1 from number_of_instances"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
