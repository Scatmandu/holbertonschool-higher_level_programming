#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx > length:
        return my_list
    if length == 0:
        return my_list
    else:
        for x in range(length):
            if x == idx:
                my_list[idx] = element
                return my_list
