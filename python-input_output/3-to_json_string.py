#!/usr/bin/python3
"""defines json string serialization function"""
import json


def to_json_string(my_obj):
    """serializes to json using dumps"""

    json_string = json.dumps(my_obj)
    return json_string
