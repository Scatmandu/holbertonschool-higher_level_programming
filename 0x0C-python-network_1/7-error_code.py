#!/usr/bin/python3
"""takes in a URL, sends request to URL and displays body of the response"""

if __name__ == "__main__":
    import requests
    from sys import argv

    request = requests.get(argv[1])

    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
