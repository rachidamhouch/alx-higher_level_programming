#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """__init__"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width geter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height geter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value