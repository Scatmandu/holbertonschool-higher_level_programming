#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list[::-1]
    for x in range(len(reverse_list)):
        print("{}".format(reverse_list[x]))