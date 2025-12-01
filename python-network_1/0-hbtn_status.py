#!/usr/bin/python3
"""request read"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as f:
        request = f.read()

    print("Body response:")
    print("\t- type: {}".format(type(request)))
    print("\t- content: {}".format(request))
    print("\t- utf8 content: {}".format(request.decode('utf-8')))
