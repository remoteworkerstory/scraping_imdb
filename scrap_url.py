import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

with open('total_url.json') as json_file:
     data = json.load(json_file)
#
print(len(data))
h=1
#dito = ['https://www.imdb.com/title/tt0663861/', 'https://www.imdb.com/title/tt0663893/','https://www.imdb.com/title/tt0663880/']
for url in data:
    geturl = requests.get(url, "html.parser")
    print(h)
    # geturl1 = geturl.text
    f= open('./detail_html/{}.html'.format(h), 'w+') #membuat file html
    f.write(geturl.text)
    f.close()
    h = h+1



