#!/usr/bin/python3
import json
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string from python dictionary"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return ('"[]"')
        else:
            new_string = json.dumps(list_dictionaries)
            return new_string
