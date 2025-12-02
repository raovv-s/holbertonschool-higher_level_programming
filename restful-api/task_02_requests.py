#!/usr/bin/python3
"""jsonapiholder api example"""

import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch posts and print their titles"""
    req = requests.get(URL)
    print(f"Status Code: {req.status_code}")
    
    if req.status_code == 200:
        posts = req.json()
        for post in posts:
            print(post["title"])
    else:
        print("request error")

def fetch_and_save_posts():
    """fetch and sace to csv """
    req = requests.get(URL)
    
    if req.status_code == 200:
        posts = req.json()
        structured_posts = []

        for post in posts:
            structured_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        
        with open("posts.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_posts)