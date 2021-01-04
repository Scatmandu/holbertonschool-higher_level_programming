#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for idx in my_list:
        if my_list.index(idx) < x:
            try:
                print(idx, end='')
                count += 1
            except IndexError:
                break
    print()
    return count
