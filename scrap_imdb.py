import requests
from bs4 import BeautifulSoup
import json

master_listing = []
url =[]
season = 4
## 1. membuat list url
for n in range(1,season+1):
    response = requests.get('https://www.imdb.com/title/tt0362359/episodes?season={}'.format(n))
    html = response.text
    soup = BeautifulSoup(html, "html5lib")
    listing = soup.find_all("div", {"class":"list_item"})
    print(len(listing))
    for i in range(len(listing)):
        a_listing = listing[i]
        urls = "https://www.imdb.com"+a_listing.a['href']
        url.append(urls)

## 1.  membuat list url di file json
print(len(url))
print(url)
with open('total_url.json', 'w') as outfile:
    json.dump(url, outfile)


