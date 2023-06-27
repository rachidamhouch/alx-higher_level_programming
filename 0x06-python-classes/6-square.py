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
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a \
tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print a square of #"""
        [print() for i in range(0, self.position[1])]
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
        if self.size == 0:
            print()
