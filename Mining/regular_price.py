import time
from bs4 import BeautifulSoup
import json




with open('prices (1).xml') as file:
    src = file.read()

soup = BeautifulSoup(src, 'xml')


all_price = soup.find_all('regular_price')


table_price = []
for item in all_price:
    all_item_price = float(item.text)
    table_price.append(all_item_price)

print(f'Total regular_price: {round(sum(table_price), 2)}')

# all_name = soup.find_all('name')
#
# table_name = []
# for name in all_name:
#     item_name = name.text
#     table_name.append(item_name)
#
# table_zip = zip(table_name, table_price)
# for tables in table_zip:
#     # print(*tables, sep = '---')


# print()
# time.sleep(0.8)
# print(f'Total regular_price: {round(sum(table_price), 2)}')

