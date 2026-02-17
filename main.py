import requests
import time
import json
import csv
from create_atlas import create_atlas

API_URL = "https://en.wikipedia.org/w/api.php"
headers = {
    "user-agent": "Mini-Project for wikipedia mapping."
}

title = input("Enter a Wikipedia page title: ").strip()
filename = title + "_links.csv"
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target']) # header for the file

def get_links(title):
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": "50",
        "redirects": "1",
        "namespace": "0"
    }
    try:
        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()
        pages = data["query"]["pages"]

        for page_id in pages: 
            if "links" in pages[page_id]:
                return pages[page_id]["links"] # make sure it actually returns something
            else:
                print(f"No links found for {title}")
                return [] 
    except:
        return []

def save_connection(source, target):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([source, target])

# fetch the links for the title
print("Fetching links for the title:", title)
layer1_links = get_links(title)

for link in layer1_links:
    l1_title = link["title"]
    save_connection(title, l1_title)
    print(f"Fetched link: {l1_title}")

    print(f"  Fetching Layer 2: {l1_title}")
    layer2_links = get_links(l1_title)
    
    for sublink in layer2_links:
        l2_title = sublink["title"]
        save_connection(l1_title, l2_title)


print("Data collection complete. Generating atlas...")
create_atlas(filename)


"""
# base logic 
for page_id in pages:
    if "links" in pages[page_id]:
        print("Links from {title}") 
        for link in pages[page_id]["links"]:
            print(link["title"])
    else:
        print(f"No links found for {title}")
"""



