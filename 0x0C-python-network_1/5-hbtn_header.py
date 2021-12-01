#!/usr/bin/python3
"""requests URL and displays X-Request-Id"""


if __name__ == "__main__":
    import requests
    from sys import argv


fard = requests.get(argv[1])
farder = fard.headers
print(farder.get('X-Request-Id'))
