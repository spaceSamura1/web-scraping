#Goal: Scraping multiple links within the same page

import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#lxml is the parser you are selecting for the data

box = soup.find('article', class_='main-article')
#box is isolationg the main content of the page

links = []

for link in box.find_all('a', href=True):
    links.append(link['href'])


for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    #this for loop creates the url link by concatenating the root url with the href links obtained from the first for loop
    #it then parses through each link below

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)
        #this creates an individual txt file for each transcript
