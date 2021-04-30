#!/usr/bin/python3
def no_c(my_string):
    remove_c = ['c', 'C']
    for i in remove_c:
        my_string = my_string.replace(i, '')
    return(my_string)
