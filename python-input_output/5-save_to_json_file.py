#!/usr/bin/python3
"""defines function to write json rep of object to file"""
import json


def save_to_json_file(my_obj, filename):
    """writes json rep of object to file"""

    with open(filename, 'w', encoding='utf-8') as file:

        json_str = json.dump(my_obj, file)
        return json_str
