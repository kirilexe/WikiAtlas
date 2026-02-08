import requests
from bs4 import BeautifulSoup
from collections import Counter
import time

# starting
start_url = "https://en.wikipedia.org/wiki/Animal"
base_url = "https://en.wikipedia.org"

# config
max_pages_to_crawl = 5 
links_per_page = 50 

headers = { # fixes 403 forbidden error due to the browser thinking the request is from a bot
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
}

page = requests.get(page_to_scrape, headers=headers, params={"q": "python"})
soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

links = soup.find_all('a')
for link in links:
    print(link.get('href'))

