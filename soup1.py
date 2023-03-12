#Goal: Scraping multiple links within the same page

import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movies'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#lxml is the parser you are selecting for the data

box = soup.find('article', class_='main-article')
#box is isolationg the main content of the page

box.find_all('a', href=True)

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#strip removes trailing and leading spaces only at the beginning and end of the data
#separator replaces a new line with a blank space

with open('budapest-noir.txt', 'w') as file:
    file.write(transcript)