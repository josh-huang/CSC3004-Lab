from random import random
from bs4 import BeautifulSoup
import requests 

random_location = []
# web scrapping location from wikipedia and store in random location array
try: 
    html_text = requests.get('https://en.wikipedia.org/wiki/List_of_places_in_Singapore').text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # find location element in html 
    table = soup.find("table",{"class":"wikitable sortable"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    # append random location in random_location array
    for row in rows:
        # print(row)
        location = row.find('a')
        if location is not None: 
            random_location.append(location.text)
except:
    print('Wikipedia server has crashed. Please try again later')
