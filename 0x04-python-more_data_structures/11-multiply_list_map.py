#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul = (lambda n: n * number)
    new_matrix = list(map(mul, my_list))
    return new_matrix
