#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """text_indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i in ".:?":
            print()
            print()
