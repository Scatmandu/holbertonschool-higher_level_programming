#!/usr/bin/python3
"""requests URL and displays X-Request-Id"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        html = response.info()
    print(html.get('X-Request-Id'))
