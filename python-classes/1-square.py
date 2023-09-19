#!/usr/bin/python3
"""defines a class Square with more specificiation"""


class Square:
	
	def __init__(self, size):
		"""initialized square instance"""
		"""size of new square, double underscore to rep private"""
		self.__size = size
