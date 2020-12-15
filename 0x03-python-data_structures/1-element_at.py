#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    for x in range(length):
        if idx < 0 or idx > length:
            return
        elif x == idx:
            return my_list[x]
