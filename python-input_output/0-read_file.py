#!/usr/bin/python3
"""read file func"""


def read_file(filename=""):
    """reads file and prints to stdout"""

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
