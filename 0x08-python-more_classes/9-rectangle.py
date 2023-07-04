#!/usr/bin/python3
""" Rectangle """


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.width * self.height

    def perimeter(self):
        """perimeter"""
        if not self.width or not self.height:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """__str__"""
        rec = ""
        for i in range(self.height):
            for j in range(self.width):
                rec += str(self.print_symbol)
            if i != self.height - 1 and self.width:
                rec += "\n"
        return rec

    def __repr__(self):
        """__repr__"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """__del__"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """square"""
        return cls(size, size)
