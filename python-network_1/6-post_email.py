#!/usr/bin/python3
""" post method in use, requests + sys"""

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    parse = getr.post(url, data=mail)
    print parse.text
