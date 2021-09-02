import requests
from bs4 import BeautifulSoup

url = 'https://opennet.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a')

for quote in quotes:
    print(quote.text, quote.get('href'))