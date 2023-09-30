#!/usr/bin/python3
"""defines new base class model"""


class Base:
    """represents base model

        private class attribute:
            __nb_object (int): # of instantiated bases"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize new base
            args:
                id (int): id of new base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
