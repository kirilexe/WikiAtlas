import requests
import time
import json

API_URL = "https://en.wikipedia.org/w/api.php"
headers = {
    "user-agent": "Mini-Project for wikipedia mapping."
}

title = "Animal"

params = {
    "action": "query",
    "format": "json",
    "titles": title,
    "prop": "links",
    "pllimit": "max",
}

response = requests.get(API_URL, headers=headers, params=params)
data = response.json()

pages = data["query"]["pages"]

for page_id in pages:
    if "links" in pages[page_id]:
        print("Links from {title}") 
        for link in pages[page_id]["links"]:
            print(link["title"])
    else:
        print(f"No links found for {title}")