#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if not my_list:
        return my_list
    elif idx < 0:
        return my_list
    elif idx > length:
        return my_list
    else:
        for x in range(length):
            if x == idx:
                return my_list[x]
