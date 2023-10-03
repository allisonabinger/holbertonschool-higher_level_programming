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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is list:
            for dictionaries in list_dictionaries:
                if type(dictionaries) is not dict:
                    return "[]"
            return json.dumps(list_dictionaries)
        else:
            return "[]"
