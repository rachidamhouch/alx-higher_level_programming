#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    rev_list = my_list
    rev_list.reverse()
    for i in rev_list:
        print("{:d}".format(i))
