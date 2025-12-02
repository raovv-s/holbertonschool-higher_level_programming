#!/usr/bin/python3
"""sys + requests"""
import sys
import requests

url = sys.argv[1]
getr = requests.get(url)
print(getr.header("X-Request-Id"))
