#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx > length:
        return my_list
    else:
        for x in range(length):
            if x == idx:
                new_list[x] = element
                break
        return new_list
