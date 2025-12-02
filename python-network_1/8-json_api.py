#!/usr/bin/python3
"""post json data via using requests lib"""
import requests 
import sys
if __name__ == "__main__"":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    parse = requests.post(url, data={"q": q})
    try:
        r = data.json()
    except ValueError:
        print("Not a valid JSON")    
    if not r:
        print("No result")
