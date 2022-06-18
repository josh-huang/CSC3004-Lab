from random import random
from bs4 import BeautifulSoup
import requests 

random_location = []

html_text = requests.get('https://en.wikipedia.org/wiki/List_of_places_in_Singapore').text
soup = BeautifulSoup(html_text, 'html.parser')

# location = soup.find_all("div", class_ = "mw-body-content mw-content-ltr").div
table = soup.find("table",{"class":"wikitable sortable"})
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    # print(row)
    location = row.find('a')
    if location is not None: 
        random_location.append(location.text)

# print(random_location)