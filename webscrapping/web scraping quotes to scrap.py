import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://quotes.toscrape.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

quotes_scrap = []

for row in soup.find_all('div', class_='quote'):
    quote = {}
    quote['quote'] = row.find("span", class_="text").text
    quote['author'] = row.find("small", class_="author").text
    author_link = row.find('a')['href']          # (about) link -> author page
    quote['author_url'] = URL + author_link.lstrip('/')
    tags = [t.text for t in row.find_all('a', class_='tag')]
    quote['tags'] = ', '.join(tags)
    quotes_scrap.append(quote)

filename = 'quotes.toscrape.com.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['quote', 'author', 'author_url', 'tags'])
    w.writeheader()
    for q in quotes_scrap:
        w.writerow(q)

print(f"{len(quotes_scrap)} quotes saved to {filename}")
           