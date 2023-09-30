# import os
#
# os.rename('qqq.txt', 'qqq.txt')
# f = open('work on file/qqq.txt', 'r')
# print(f.readline())
#


# f = open('abc.txt', 'w', encoding='utf-8')
# f.write('''Красивое лучше уродливого.
# Явное лучше неявного.
# Простое лучше сложного.
# Сложное лучше запутанного.
# Развернутое лучше вложенного.
# Разреженное лучше плотного.
# Читаемость имеет значение.''')
# f.close()
# print(f.readline())
# for row in f:
#     print(row)
#     for letter in row:
#         print(letter)
#
# s = f.readlines()
# print(s)
#
# for row in  f:
#     print(row)
# try:
#     with open('abc.txt', 'a+') as file:
#         file.write('\nПишем дальше..')
# except:
#     print('Ошибка при работе с файлом')
#
# try:
#     with open('abc.txt', 'a+') as file:
#         file.seek(0)
#         file.writelines(['2 add\n', '3 add\n'])
#         print(file.readlines())
# except:
#     print('Ошибка при работе с файлом')
#
# import pickle
# books = [("Онегин", "Пушкин", 200)]
# file = open('out.bin', 'wb')
# pickle.dump(books, file)
# file.close()
#
# try:
#     with open('abc.txt', 'w') as file:
#         for row in file.readline():
#             print(row)
# except:
#     print('Ошибка при работе с файлом')

# with open('nums.txt', 'r') as file:
    # print(sum([int(i .replace(' ', '').strip('\n')) for i in file if i.strip()]))
    # print(file.read().split())

# with open('prices.txt', 'r') as file:
#     print(sum([int(i.split()[2])*int(i.split()[1]) for i in file]))

# with open('liza.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')
#
# with open('text.txt') as file:
#     print(file.read()[::-1])


# with open('data.txt') as file:
    # print(*file.readlines()[::-1])
    # print(*[i.strip() for i in file.readlines()[::-1]], sep='\n')

# with open('lines.txt') as file:
#     print(*[i for i in file.readlines() if len(i)>4], sep='')

# max_len = 0
# max_str = []
#
# with open('lines.txt') as file:
#     for line in file.readlines():
#         if len(line) > max_len:
#             max_len = len(line)
#             max_str = [line]
#         elif len(line) == max_len:
#             max_str.append(line)
#
# for elem in max_str:
#     print(elem, end='')
from functools import reduce
# with open('numbers.txt') as file:
#     for i in file.readlines():
#         print(sum([int(j) for j in i.split()]))

