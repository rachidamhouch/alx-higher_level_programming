#!/usr/bin/python3
def print_list_integer(my_list=[]):
    
    for i in my_list:
        if not isinstance(i, int):
            return
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
