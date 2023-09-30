import re

from bs4 import BeautifulSoup
import lxml
import json

with open('index.html') as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, 'lxml')
# print(soup)
# p1 = soup.find('h1')
# print(p1)
# p = soup.find_all('h1')
# for i in p:
#     print(i)
#
# user_info = soup.find('div', class_='user__name').find('span')
# print(user_info)

# find_all = (soup.find('div', class_= 'user__info').
#             find_all('span'))
# print(find_all)
#
# for i in find_all:
#     print(i.text)

# social_links = soup.find('div', class_='social__networks').find('ul').find_all('a')
# print(social_links)

# all_a = soup.find_all('a')
# # print(all_a)
# for i in all_a:
#     i_text = i.text
#     i_url = i.get('href')
#     print(f'{i_text}: {i_url}')

# link = soup.find('a', text = 'Одежда для взрослых')
# print(link)


# link = soup.find('a', text=re.compile('Одежда'))
# print(link)
#
# clos= soup.find_all(text=re.compile('[Оо]дежда'))
# print(clos)

# with open('index2.html', 'w') as file:
#     file.write(src)
#
# with open('json_file.json', 'w') as file:
#     json.dump(src.strip('\n'), file, indent=3, ensure_ascii=False)
