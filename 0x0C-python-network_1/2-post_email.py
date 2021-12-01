#!/usr/bin/python3
"""takes URL and email and displays the response"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    dictionary = {}
    dictionary['email'] = argv[2]
    data = parse.urlencode(dictionary)
    data = data.encode('utf-8')
    with request.urlopen(argv[1], data) as response:
        html = response.read()
        print(html.decode('UTF-8'))
