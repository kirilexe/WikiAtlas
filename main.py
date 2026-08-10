import requests
import time
import json
import csv

from create_atlas import create_atlas
from bs4 import BeautifulSoup

title = input("Enter a Wikipedia page title: ").strip()
filename = title + "_links.csv"
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Source', 'Target']) # header for the file

def get_links(title, limit=50):
    url = f"https://en.wikipedia.org/api/rest_v1/page/html/{title}"
    headers = {
        "user-agent": "WikiAtlas 0.0.1 (67431669+ic0e@users.noreply.github.com)"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch page: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        seen = set()

        # get all <a> tags inside the <p> tags
        for a in soup.select("p > a[href^='./']"):
            href = a.get("href", "")

            # clears the link title from "./Link" -> "Link"
            link_title = href.replace("./", "").replace("_", "")

            if ":" not in link_title and link_title not in seen:
                seen.add(link_title)
                links.append(link_title)

                if len(links) >= limit:
                    break

        return links

    except Exception as e: 
        print(f"Error fetching {title}: {e}")
        return []

def save_connection(source, target):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([source, target])

# fetch the links for the title
print("Fetching links for the title:", title)
layer1_links = get_links(title)

for l1_title in layer1_links:
    save_connection(title, l1_title)
    print(f"Fetched link: {l1_title}")

    print(f"  Fetching Layer 2: {l1_title}")
    layer2_links = get_links(l1_title)

    for l2_title in layer2_links:
        save_connection(l1_title, l2_title)

    time.sleep(0.1)

print("Data collection complete. Generating atlas...")
create_atlas(filename)
