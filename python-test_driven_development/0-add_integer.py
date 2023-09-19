#!/usr/bin/python3
"""Integer addition function definition."""


def add_integer(a, b=98):
    """
    Return the sum of a + b as an integer.

    if a or b is not an integer or float, a TypeError exception is raised.

    if a or b is a float, they will be casted to integers first.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
