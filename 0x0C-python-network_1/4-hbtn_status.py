#!/usr/bin/python3
"""fetches a url"""


if __name__ == '__main__':
    import requests

    request = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {}'.format(type(request.text)))
    print('\t- content: {}'.format(request.text))
