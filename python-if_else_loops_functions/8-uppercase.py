#!/usr/bin/python3
def uppercase(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)

    print(result)
