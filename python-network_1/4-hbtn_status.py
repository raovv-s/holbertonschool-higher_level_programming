#!/usr/bin/python3
"""simple request (1line)"""
import requests

if __name__ == "__main__":
    req = request.get("https://intranet.hbtn.io/status")
    print("Body response")
    print(f"type: {type(req.text)}")
    print(f"content: {req.text}")
