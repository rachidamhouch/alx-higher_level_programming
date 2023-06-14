#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = lambda n: n * n
    for i in matrix:
        new_matrix.append(list(map(square, i)))
    return new_matrix
