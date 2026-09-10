import requests
from bs4 import BeautifulSoup
import csv

URL='https://zerolifestyle.co/pages/smart-watches'
r=requests.get(URL)
soup=BeautifulSoup(r.content, 'html5lib')
table=soup.find('product-list', attrs={'id':'block-template--27465838100758__page_collections_iiYUig-collection_p8Uq6A'})
print('Container found:', table is not None)
smart_watches=[]  # first product ka raw HTML dekho  
items = table.find_all('product-item', class_='product-item')  # trailing space removed
print('Product items found:', len(items))

for row in items:
    link = row.find('a', class_='product-item-meta__title') or row.find('a')
    img = row.find('img')
    discount_span = row.find('span', class_=lambda c: c and 'badge' in c.lower())
    watches = {
        'url': 'https://zerolifestyle.co' + link.get('href') if link and link.get('href') else None,
        'image': img.get('src') or img.get('data-src') if img else None,
        'name': link.get_text(strip=True) if link else None,
        'discount': discount_span.get_text(strip=True) if discount_span else None,
    }
    smart_watches.append(watches)
filename='Zero_lifestyle_2.0.csv'  
with open(filename,'w',newline="")as f:
    w=csv.DictWriter(f,['url','image','name','discount']) 
    w.writeheader() 
    for watches in smart_watches:
        w.writerow(watches)
        print(f"Wrote {len(smart_watches)} rows to {filename}")