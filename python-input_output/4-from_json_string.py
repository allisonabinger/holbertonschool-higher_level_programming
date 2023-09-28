#!/usr/bin/python3
"""defines json string deserialization function"""
import json


def from_json_string(my_str):
    """deserializes from json to python obj using loads"""

    py_obj = json.loads(my_str)
    return py_obj
