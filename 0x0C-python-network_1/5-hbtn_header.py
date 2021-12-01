#!/usr/bin/python3
"""requests URL and displays X-Request-Id"""

if __name__ == "__main__":
    import requests
    from sys import argv

request = requests.get(argv[1])
header = request.headers
print(header.get('X-Request-Id'))
