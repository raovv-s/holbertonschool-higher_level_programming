#!/usr/bin/python3
"""body read with exception"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as f:
            print(f.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
