#!/usr/bin/python3
"""jsonplaceholder api"""
import requests


url = "https://jsonplaceholder.typicode.com/posts"
req = requests.get(url)

def fetch_and_print_posts(req):
    """post dump from JSONPlaceHolder"""
    req = requests.get(url)
    print(f"Status code: {req.status_code}")
    if req.status_code == 200:
        json = req.json()
        for post in posts:
            print(post["title"])
    else:
        print("None")

def fetch_and_save_posts(req):
    req = requests.get(url)

    if req.status_code == 200:
        json = req.json()
        keydata = []
    for key in json:
    keydata.append({
    "id": post["id"],
    "title": post["title"],
    "body": post["body"]
})
    with open("posts.csv", "w", encoding="utf-8") as f:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(structured_posts)
