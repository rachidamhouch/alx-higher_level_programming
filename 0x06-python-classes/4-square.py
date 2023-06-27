#!/usr/bin/python3
""" Square """


class Square:
    """Square"""
    def __init__(self, size=0):
        """init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area"""
        return self.__size ** 2

    def size(self):
        """Size Geter"""
        return self.__size

    def size(self, value):
        """Size Seter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
