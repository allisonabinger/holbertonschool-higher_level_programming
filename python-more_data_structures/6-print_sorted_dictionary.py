#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = list(a_dictionary.keys())
    key.sort()
    for i in key:
        print("{}: {}".format(i, a_dictionary[i]))
