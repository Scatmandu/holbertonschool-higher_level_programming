#!/usr/bin/python3
"""takes URL and email and displays the response"""


if __name__ == "__main__":
    import requests
    from sys import argv

    dictionary = {}
    dictionary['email'] = argv[2]
    request = requests.post(argv[1], dictionary)
    print(request.text)
