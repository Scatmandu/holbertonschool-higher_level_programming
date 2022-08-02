#!/usr/bin/python3
"""takes in args and prints how many are given"""


if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc != 2:
        if argc == 1:
            print("0 arguments.")
        else:
            print("{:d} arguments:".format(argc - 1))
    else:
        print("1 argument:")
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
