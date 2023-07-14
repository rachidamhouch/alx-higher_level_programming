#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, value):
        """__eq__"""
        return self.real != value

    def __ne__(self, value):
        """__ne__"""
        return self.real == value
