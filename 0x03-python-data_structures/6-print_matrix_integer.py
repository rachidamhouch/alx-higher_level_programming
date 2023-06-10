#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
        return
    for i in matrix:
        for n in i:
            print("{:d}{:s}".format(n, " " if (n != i[-1]) else "\n"), end="")
