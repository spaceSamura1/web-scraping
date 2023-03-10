import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Budapest_Noir-5161018'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
