import requests
from bs4 import BeautifulSoup
import re
import json
import lxml

url = 'https://store.data-analyst.praktikum-services.ru'

req = requests.get(url)
src = req.text
print(src)

with open('index.html', 'w') as file:
    file.write(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
# print(soup.text)

all_table = []
all_products = soup.find_all('div', class_='t754__title t-name t-name_md js-product-name')
# print(all_products)
for item in all_products:
    all_text=item.text.split()
    product = all_text[0]
    product_type = all_text[1]
    brand_product = all_text[2]
    description = all_text[3:]

    all_table.append(
        {
           'product': product,
           'product_type' : product_type,
            'brand_product': brand_product,
            'description': description
        }
    )

with open('product_info.json', 'w') as file:
    json.dump(all_table, file, indent=4, ensure_ascii=False)
