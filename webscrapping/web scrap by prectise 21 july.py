import requests
from bs4 import BeautifulSoup
import csv
 
URL = 'https://books.toscrape.com/'
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
 
books_scrap = []
 
# Har book <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3"> ke andar hai
for row in soup.find_all('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
    books = {}
    books['url'] = URL + row.a['href']                     # relative link ko full URL banaya
    books['image'] = URL + row.img['src'].replace('../', '')  # image ka full path
    books['name'] = row.h3.a['title']                       # book ka poora naam
    books['price'] = row.find('p', class_='price_color').text  # price
    books['rating'] = row.find('p', class_='star-rating')['class'][1]  # e.g. Three, Four
    books_scrap.append(books)
 
filename = 'books.toscrape.com.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['url', 'image', 'name', 'price', 'rating'])
    w.writeheader()
    for book in books_scrap:
        w.writerow(book)
 
print(f"{len(books_scrap)} books saved to {filename}")
           
