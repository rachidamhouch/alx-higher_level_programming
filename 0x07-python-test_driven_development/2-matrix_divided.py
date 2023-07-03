#!/usr/bin/python3
"""matrix_divided"""


def matrix_divided(matrix, div):
    """matrix_divided"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise TypeError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        if i > 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
            row.append(j / div)
        new_matrix.append(row)
    return new_matrix
