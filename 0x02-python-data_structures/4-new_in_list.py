#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx > length:
        return my_list
    else:
        new_list[idx] = element
        return new_list
