#!/usr/bin/python3
"""jsonplaceholder api"""
import requests


url = "https://jsonplaceholder.typicode.com/posts"
req = requests.get(url)

def fetch_and_print_posts(req):
    """post dump from JSONPlaceHolder"""

    if req.status_code == 200:
        json = req.json()
        print(json)
    else:
        print("None")

def fetch_and_save_posts(req):
    if req.status_code == 200:
        key_data = []
    for key in json:
    key_data.append({
    "id": post["id"],
    "title": post["title"],
    "body": post["body"]
})
    with open("posts.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(structured_posts)
