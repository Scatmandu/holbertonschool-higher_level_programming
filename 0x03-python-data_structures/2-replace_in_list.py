#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    for x in range(length):
        if idx < 0 or idx > length:
            return my_list
        elif x == idx:
            my_list[idx] = element
            return my_list
