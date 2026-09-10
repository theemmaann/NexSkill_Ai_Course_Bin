import requests
from bs4 import BeautifulSoup
import csv, re

URL = 'https://zerolifestyle.co/pages/smart-watches'
r = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('product-list', attrs={'id': 'block-template--27465838100758__page_collections_iiYUig-collection_p8Uq6A'})
print('Container found:', table is not None)

items = table.find_all('product-item', class_='product-item')
print('Product items found:', len(items))

smart_watches = []

for row in items:
    # --- URL: pehla product link jiska href /products/ se start ho ---
    product_links = row.find_all('a', href=lambda h: h and h.startswith('/products/'))
    url = 'https://zerolifestyle.co' + product_links[0]['href'] if product_links else None

    # --- NAME: un links mein se woh jiska text khali na ho ---
    name = None
    for a in product_links:
        text = a.get_text(strip=True)
        if text:
            name = text
            break
    if not name:  # fallback: image ka alt text
        img_alt = row.find('img')
        name = img_alt.get('alt') if img_alt else None

    # --- IMAGE: pehli non-hidden img ---
    img = row.find('img', hidden=False) or row.find('img')
    image = None
    if img and img.get('src'):
        src = img['src']
        image = 'https:' + src if src.startswith('//') else src

    # --- DISCOUNT: row ke text se "XX% OFF" pattern ---
    row_text = row.get_text(' ', strip=True)
    discount_match = re.search(r'\d+%\s*OFF', row_text)
    discount = discount_match.group() if discount_match else None

    smart_watches.append({'url': url, 'image': image, 'name': name, 'discount': discount})

filename = 'Zero_lifestyle_2.0.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['url', 'image', 'name', 'discount'])
    w.writeheader()
    for watch in smart_watches:
        w.writerow(watch)

print(f"Wrote {len(smart_watches)} rows to {filename}")