#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx > length:
        return
    else:
        for x in range(length):
            if x == idx:
                return my_list[x]
