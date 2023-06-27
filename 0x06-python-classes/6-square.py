#!/usr/bin/python3
""" Square """


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """area"""
        return self.__size ** 2

    @property
    def size(self):
        """Size Geter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Seter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position"""
        if not isinstance(value, tuple) or len(value) != 2\
            or not isinstance(value[0], int)\
            or not isinstance(value[1], int) or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a\
            tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Size my_print"""
        for i in range(0, self.__position[1]):
            print()
        if not self.__size:
            print()
            return
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
