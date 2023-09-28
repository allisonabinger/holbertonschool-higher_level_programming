#!/usr/bin/python3
"""defines append function"""


def append_write(filename="", text=""):
    """appends text entered to a file"""

    with open(filename, 'a', encoding='utf-8') as file:
        chars = file.write(text)
        return chars
