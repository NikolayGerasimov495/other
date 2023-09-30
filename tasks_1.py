# class Animal:
#     def __init__(self, height=0, power=0):
#         self.height = height
#         self.power = power
#         print('Animal')
#         super().say()
#
# class Animal2:
#     def say(self):
#         print('Animal2')
#
# class Cat(Animal, Animal2):
#     def __init__(self, weight=0, **kwargs):
#         self.weight = weight
#         print('Cat')
#         super().__init__(**kwargs)
#
#     @property
#     def count(self):
#         print('count')
#         return self.height + self.weight
#
#
# # Animal.one()
# # a = Animal()
# # a.say()
# c = Cat(height=2, weight=3, power=5)
# c.say()
# print(c.weight)
# print(c.height)
# print(c.power)
# print(c.count)
# #
# # Animal.zero()
import math
#
# a = 3
# # for i in range(a):
# #     print([j+1 for j in range(a)])
#
# for i in range(1, a+1):
#     print([j+1 for j in range(i)])

# l = []

# a = ('a'' ''b'' ''c'' ''d'' ''d').split()
# # for i in a:
# #     for j in i:
# #         lst = list(j)
# #         l.append(lst)
# # print(l)
#
# res = []
# for el in a:
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)

# tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
# # print(list(filter(None, tuples)))
# # print([e for e in tuples if e])
#
#
# tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
# # new_tuples = [i[:-1] + (100,) for i in tuples]
# new_tuples = []
# for i in tuples:
#     lst=list(i)
#     lst.append(100)
#     new_tuples.append(tuple(lst))
#
# print(new_tuples)


# numbers = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
#
# for i in range(len(numbers)):
#     print(numbers[i])

# for num in numbers:
#     print(num)

# not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
# print(not_sorted_tuple)
#
# sorted_tuple = sorted(not_sorted_tuple)
# print(tuple(sorted_tuple))

# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# count = 1
# for i in numbers:
#     count*=i
# print(count)

# import math
# n = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# print(math.prod(n))
#
# from math import prod
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# # print(prod(numbers))
# from functools import reduce
# print(reduce(lambda x,y: x + y, numbers))
# print(reduce(lambda x,y: x * y, numbers))
# print(eval('*'.join(map(str, numbers))))

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')[:-1] + ('Москва',)
# print(poet_data)
# a = list(poet_data)
# a[-1] = 'Москва'
# print(tuple(a))


# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))


# lst=[]
# for i in numbers:
#     lst.append(sum(i) / len(i))

# print([sum(i)/len(i) for i in numbers])
# print([sum(numbers[i])/len(numbers[i]) for i in range(len(numbers))])

# def func(a, b, c):
#     x = -(b / (2 * a))
#     y = (4 * a * c - b ** 2) / (4 * a)
#     return x, y
# funcc = func(int(input()), int(input()), int(input()))
# print(funcc)


# С использованием кортежей многие алгоритмы приобретают достаточно краткую форму. Например, вычисление чисел Фибоначчи может выглядеть следующим образом:
# n = int(input())
# f1, f2 = 1, 1
# for i in range(n):
#     print(f2)
#     f1, f2 = f2, f1 + f2

# a, b, c = 10, 20, 30
# c, b, a = a + b, b*2, a + b + c
#
# print(a, b, c)

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
#
# print(sum(i**2 for i in numbers))

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# sorted_fruit=sorted(fruits, reverse=True)
# for i in sorted_fruit:
#     print(i)
#
# print('YES' if len(s := input()) == len(set(s)) else 'NO')


# a = 'Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.'

# import string
# table = str.maketrans("", "", string.punctuation)
# new_s = a.translate(table)
# print(len(set(new_s.split())))
# print(len(set([i.strip('.,;:-?! ').lower() for i in a.split()])))


# a = input().split()
#
# lst=[]
# for i in a:
#     ch = int(i)
#     lst.append(ch)
#
# s = []
# for j in lst:
#     if j not in s:
#         print('NO')
#         s.append(j)
#     else:
#         print('YES')
#
#
# lst=[]
# for i in input().split():
#     ch = int(i)
#     if ch not in lst:
#         print('NO')
#         lst.append(ch)
#     else:
#         print('YES')
#
# numbers = [int(i) for i in input().split()]
# [print('YES') if numbers[i] in numbers[:i] else print('NO') for i in range(len(numbers))]
#
# set1 = {'a', 'b', 'c', 'd', 'h'}
# set2 = {'b', 'd', 'f', 'h'}
#
# set3 = set1 - set2&set1
# print(set3)
#
# set1=set(input().split())
# set2=set(input().split())
# set3=set1.intersection(set2)
# print(sorted(set3), reverse=False)

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
#
#
# print(*sorted({int(i) for i in set(items)}))


#
# myset1 = set(input().split())
# myset2 = set(input().split())
# myset3 = set(input().split())
#
# superset = set()
# #
# # superset.add(myset2.difference(myset3))
# # superset.add(myset1.difference(myset3))
#
# c = myset1.intersection(myset2)
#
# for i in c.difference(myset3):
#     superset.add(i)
#
# for i in c.difference(myset3):
#     superset.add(i)
#
# print(sorted(superset, reverse=True))
#
# print()
#
# a,b,c=(set(int(i) for i in input().split()) for i in range(3))
# # print(a,b,c, sep='\n')
# print(*sorted(a.intersection(b).difference(c), reverse=True))

# a,b,c=(set(int(i) for i in input().split()) for k in range(3))
# print(a,b,c, sep='\n')
# print(a.union(b).union(c))
# print(a.intersection(b).intersection(c))
# print(*sorted((a.union(b).union(c))-(a.intersection(b).intersection(c)), reverse=True))

# a,b,c = ([set(int(i) for i in input().split()) for k in range(3)])
# # print(a,b,c, sep='\n')
# print(*sorted(c-(a|b), reverse=True))

# a, b, c = ([set(int(i) for i in input().split()) for _ in range(3)])
# print(a, b, c, sep='\n')
#
# finish_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(finish_set)

# print(*sorted(finish_set-(a|b|c)))


# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
# print(*sorted(set([i.lower()[0] for i in words])))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, \
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, \
# over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, \
# you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and \
# traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''.lower().split()
# print(*sorted(set([i.strip("()'`.,;:-?! ") for i in sentence])))

# import string
# table = str.maketrans("", "", string.punctuation)
# new_s = a.translate(table)
# print(len(set(new_s.split())))
# print(len(set([i.strip('.,;:-?! ').lower() for i in a.split()])))
#
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, \
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, \
# over which, if you can still stand my style (I am writing under observation), the sun of my  set infancy had set: surely, \
# you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and \
# traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''.lower().split()
# print(*sorted(set([sentence[i].strip("()'` .:,;-?!") for i in range(len(sentence)) if len(sentence[i]) <4 ])))

# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', \
#          'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', \
#          'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
#
# print([str(i) for i in files])
#
# import re
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# stroka = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", sentence)
# spisok = stroka.lower().split()
#
# myset = {i for i in spisok if len(i) < 4}
# print(*sorted(myset))

# files = {'python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG'}
# print(files[::-1])
# print(*sorted({i.lower() for i in files if i.lower().endswith('.png')}))

# capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Чехия': 'Прага'}
# months = {1: 'Январь', 2: 'Февраль', 3: 'Март'}
#
# print('Минимальный ключ =', max(capitals))
# print('Максимальный ключ =', min(months))

#
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# print(*sorted([i['name'] for i in users if i['phone'].endswith('8')]))

# print(*sorted([i['name'] for i in users if 'email' not in i or i['email'] == '']))
# names = []
# for d in users:
#     try:
#         if d['email'] == '':
#             names.append(d['name'])
#     except KeyError:
#         names.append(d['name'])
# print(*sorted(names))

# digit = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
#
# #
# # for i in input():
# #     print(digit[int(i)], end=' ')
# print(*[digit[int(i)] for i in input()])
#
# # put your python code here
# digit = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
#
#
# print(*[digit[key] for key in input()])

# info = {
#     'CS101': "3004, Хайнс, 8:00",
#     'CS102': "4501, Альварадо, 9:00",
#     'CS103': "6755, Рич, 10:00",
#     'NT110': "1244, Берк, 11:00",
#     'CM241': '1411, Ли, 13:00'
#     }
#
#
# print(*[f"{i}: {info[i]}" for i in input().split()])

# dict_push = {
#     "1": ".,?!:",
#     "2": "ABC",
#     "3": "DEF",
#     "4": "GHI",
#     "5": "JKL",
#     "6": "MNO",
#     "7": "PQRS",
#     "8": "TUV",
#     "9": "WXYZ",
#     "0": " "
# }
# for i in input().upper():
#     for key, value in dict_push.items():
#         if i in value:
#             print(key * (value.index(i)+1), end='')


# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..q', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# print(*[dict(zip(letters, morse))[i] for i in input().upper() if i.strip("' ',.+=?!-")])


#
#
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
#
# print(result)
#
# result1 = {}
# for num in numbers:
#     result1[num] = result1.get(num, 0) + 1
#
# print(result1)

#
# result = {i:i**2 for i in range(1, 16)}
# print(result)

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# for key, value in dict2.items():
#     dict1[key] = dict1.setdefault(key, 0) + value
# result = dict1.copy()
# print(result)


# from collections import Counter
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# # result = dict(Counter(text))
# # print(result)
# # result={}
# # for i in text:
# #     result[i] = result.get(i, 0) + 1
# # print(result)
#
# print({i: text.count(i) for i in text})
from functools import reduce

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# res = {i:s.count(i) for i in s.split()}
# print(res)
# print(sorted([k for k, v in {i:s.count(i) for i in s.split()}.items() if v == max({i:s.count(i) for i in s.split()}.values())],reverse=False)[0])
# for k,v in res.items():
#     print(reduce(max, v), k)

# s = {i: s.count(i) for i in set(s.split())}
# print(min(i for i in s if s[i] == max(s.values())))


# res={}
# for i in s.split():
#     res[i] = res.get(i, 0) + 1
#
# print(max(res))

# res = {}
# for w in s.split():
#     res[w] = res.get(w, 0) + 1
# print(min(res, key=lambda x: (-res[x], x)))

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for i in pets:
#     result[i[1:]] = result.get(i[1:], []) + [i[0]]
#
# print(result)
# lst=[]
# res={}
# [lst.append(i.strip("()'` .:,;-? !")) for i in input().lower().split()]
# for j in lst:
#     res[j] = res.get(j, 0) + 1
# # print(min(res, key=lambda x: (res[x], x)))
# print(res)
#
# res={}
# a = [i for i in input().split()]
# print(a)
# for i in a:
#     res[i] = res.setdefault(i, -1) + 1
# print(res)


# d, l = {}, []
#
# for c in input().split():
#     if c not in l:
#         l.append(c)
#     else:
#         d[c]=d.get(c, 0) + 1
#         l.append(c + '_' + str(d[c]))
#
# print(l)

# lst = []
# a = {lst.append(input()) for i in range(int(input()))}
# s = {i.split(':')[0].lower(): i.split(': ')[1] for i in lst}
# p = [s.get(input().lower(), 'Не найдено') for i in range(int(input()))]
# print(*p, sep='\n')

# squares = {}
# for i in range(10):
#     if i % 2 == 0:
#         squares[i] = i**2
#     else:
#         squares[i] = i
#
# print(squares)

# squares = {i: {j: j**2 for j in range(i+1)} for i in range(5)}
#
# for value in squares.values():
#     print(value)

# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
# result = {i:numbers[i]**2 for i in range(len(numbers))}
# print(result)

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# print({k:v for k,v in colors.items() if v is not None})

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# print({k:v for k,v in favorite_numbers.items() if v in range(11, 100)})
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# print({v:k for k,v in months.items()})
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# print({int(i.split(':')[0]):i.split(':')[1] for i in s.split(' ')})
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# print({i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers})
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# print({i:[ord(i) for i in i] for i in words})
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# print({k:v for k,v in letters.items() if k not in remove_keys})
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# print({k:v for k,v in students.items() if v[0] > 167 and v[1] < 75})
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# print({i[0]:i[1:] for i in tuples})
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013', '12']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy', 'adda']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93, 21]
# print([{i:{n:g}} for i,n,g in zip(student_ids, student_names, student_grades)])

# print(*[('YES') if (sorted(input())) == (sorted(input())) else ('NO')])
# a,b = input(), input()#.strip('.,!?:;-')
# aa={}
# bb={}
# a = (''.join([word.lower().strip('.,; :-?!') for word in input().split()]))
# b = (''.join([word.lower().strip('.,; :-?!') for word in input().split()]))
# for i in a:
#     aa[i]=aa.get(i,0)+1
# for j in b:
#     bb[j] = bb.get(j, 0) + 1
# print(*[('YES') if aa == bb else ('NO')])

# s1 = ''.join([i for i in input().lower() if i.isalpha()])


# b = {i[0]: i[1] for i in [input().split() for i in range(int(input()))]}
# c = input()
# for k,v in b.items():
#     if v == c:
#         print(k)
#     elif k == c:
#         print(v)

# res = {}
# for i in range(int(input())):
#     a, b = input().lower().split()
#     res[b] = res.get(b, []) + [a]
# for i in range(int(input())):
#     name = input().lower()
#     print(*res.get(name, ['абонент не найден']))
#
# word = input()
# data = {}
# for _ in range(int(input())):
#     book, n = input().split(': ')
#     data[int(n)] = book
#
# for i in word:
#     print(data[word.count(i)], end='')


# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# print({k: [i for i in v if i <=20] for k, v in my_dict.items()})

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
#     res = {}
#     for k,v in emails.items():
#         for i in v:
#             res[i]=res.get(i, '') + k
#     print(*sorted([k+'@'+v for k,v in res.items()]),sep='\n')

# res = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# rnk=input().upper()
# for i in rnk:
#     for k,v in res.items():
#         if i == k:
#             print(v, end='')

# прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон
# res={}
# for i in input().split():
#     res[i]=res.get(i,0)+1
#     print(res[i], end=' ')

# DANSER
# d = {
#     1: {'A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'},
#     2: {'D', 'G'},
#     3: {'B', 'C', 'M', 'P'},
#     4: {'F', 'H', 'V', 'W', 'Y'},
#     5: {'K'},
#     8: {'J', 'X'},
#     10: {'Q', 'Z'}
# }
# res = 0
# for i in input():
#     for k, v in d.items():
#         for j in v:
#             if i == j:
#                 res += k
# print(res)
# def build_query_string(params):
#     return '&'.join([f"{key}={value}" for key, value in sorted(params.items())])

# def merge(values):      # values - это список словарей
#     result={}
#     for d in values:
#         for key in d:
#             result.setdefault(key, set()).add(d[key])
#     return result
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

# res={}
# d = {'W': 'write', 'R': 'read', 'X': 'execute'}
#
# for _ in range(int(input())):
#     x = input().split()
#     res[x[0]]=[d[i] for i in x[1:]]
#
# for _ in range(int(input())):
#     x = input().split()
#     if x[0] in res[x[1]]:
#         print('OK')
#     else:
#         print('Access denied')

# res={}
# for _ in range(int(input())):
#     name, prod, count = input().split()
#     res.setdefault(name, {})
#     res[name][prod] = res[name].get(prod, 0) + int(count)
#
# for k,v in sorted(res.items()):
#     print(f'{k}:')
#     for i in sorted(v):
#         print(i, v[i])

# def matrix(n =1,m = 0, a = 0):
#     if n == 1 and not m:
#         m = 1
#     elif n != 1 and not m:
#         m = n
#     return [[a]*m for _ in range(n)]
# def matrix(n=1, m=None, a=0):
#     if m is None:
#         m = n
#     return [[a] * m for _ in range(n)]
#
#
# print(matrix(3,1))
# def count_args(*args):
#     return len(args)
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# def sq_sum(*args):
#     return sum([i ** 2 for i in (args)])
#
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def mean(*args):
#     s = [i for i in args if type(i) is float or type(i) is int]
#     return (float(0) if len(s) == 0 else float(sum(s)/len(s)))
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def greet(name, *args):
#     s = ['and '+ i for i in args if len(i) > 0]
#     if len(args)<1:
#         return f'Hello, {name}!'
#     else:
#         return f"Hello, {name} {' '.join(s)}!"
#
# def greet(name, *args):
#     return f'Hello, {" and ".join((name,) + args)}!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))


# def print_products(*args):
#     #s = list(filter(None, [i for i in args if type(i) is str]))
#     #s = list(filter(len, [i for i in args if type(i) is str]))
#     #str_list = ' '.join(s).split()
#     prod = [i for i in args if isinstance(i, str) if i]
#     if prod:
#         for indx, i in enumerate(prod, 1):
#             print(f'{indx}) {i}')
#     else:
#         print('Нет продуктов')
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')


# def info_kwargs(**kwargs):
#     [print(f'{k}: {v}') for k,v in sorted(kwargs.items())]
#     # for k,v in sorted(kwargs.items()):
#     #     print (f'{k}: {v}')

# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')


# def comparator(pair):
#     return pair[1]
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)

# def comparator(pair):
#     return pair[0] + pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# print((comparator(pairs)))

#
# print(''.join([(format(ord(i), '08b')) for i in input()])) #01001110 01101001 01101011 01101111 01101100 01100001 01111001
# #
# print(' '.join([(bin(ord(i))) for i in input()])) #0b1001110 0b1101001 0b1101011 0b1101111 0b1101100 0b1100001 0b1111001
# #
#
#
# mes = "Nikolay"
# bstr =" ".join(format(ord(c), '08b') for c in mes)
# print(bstr)
# print(type(bstr)) #01001110 01101001 01101011 01101111 01101100 01100001 01111001
#
# s = "Nikolay"
# result = list(map(bin, bytearray(s, "utf-8")))
# print(*result)  # 0b1001110 0b1101001 0b1101011 0b1101111 0b1101100 0b1100001 0b1111001

#
# bins = "0b10011100b11010010b11010110b11011110b11011000b11000010b1111001".replace('b', '')
# str = ""
# for i in range(0, len(bins), 8):
#     binc = bins[i:i + 8]
#     num = int(binc, 2)
#     str += chr(num)
# print("The normal representation of ",bins ,"is", str)
# print(type(str))

# from bitarray import bitarray
# bins = "0b10011100b11010010b11010110b11011110b11011000b11000010b1111001".replace('b', '')
# bts = bitarray(bins)
# ascs = bts.tobytes().decode('ascii')
# print("The normal string is: ", ascs)
# print(type(ascs))

# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total)
# print(product)
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]
#
# var1 = max(numbers, key=abs)
# var2 = min(map(abs, numbers))
# print(var1, var2)
# print(var1 + var2)

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# print(*(map(lambda x: round(x, 2), numbers)), sep='\n')


#
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# # Напишите программу, которая с помощью функций filter() и map() отбирает из заданного списка numbers трёхзначные числа,
# # дающие при делении на 5 остаток 2 и выводит их кубы, каждый в отдельной строке.
# def funk(x):
#     return [i**3 for i in numbers if i%5==2 and i in range(100, 1000)]
# print(*funk(numbers), sep='\n')
# def funk(x):
#     return x % 5 == 2 and 100 < x < 1000
#
# def cub(x):
#     return x**3
#
# print(*map(cub, (filter(funk, numbers))), sep='\n')

# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# def squ(x, y):
#     return x + y ** 2
#
# print(reduce(squ, numbers, 0))


# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# def squ(x, y):
#     return x + y ** 2
#
# def funk(x):
#     return x % 7 == 0 and 10 < abs(x) < 100
#
#
# print(reduce(squ, (filter(funk, numbers)), 0))
#
# print (sum([pow(elem, 2) for elem in numbers if abs(elem)//100 == 0 and abs(elem)//10 > 0 and elem%7==0]))

# def func_apply(func, x):
#     return [func(i) for i in x]
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# def func(elem1, elem2, elem3, elem4):
#     return elem1 + elem2 + elem3+ elem4
#
#
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [10, 20, 30, 40, 50]
# numbers3 = [100, 200, 300, 400, 500]
#
# new_numbers = list(map(func, numbers1, numbers2, numbers3))  #  преобразуем итератор в список
#
# print(new_numbers)
#
# import operator
#
# words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
# numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]
#
# opposite_numbers = list(map(operator.neg, numbers))    #  смена знаков элементов списка
# concat_words = reduce(operator.add, words)             #  конкатенация элементов списка
#
# print(opposite_numbers)
# print(concat_words)
#
# iterable = [[1], [2], [3]]
# result = list(map(len, iterable))
# print(result)
#
# random_list = [1, 'a', 0, False, True, '0', 7, '']
# filtered_list = list(filter(None, random_list))
# print(filtered_list)
#
# def filter_vowels(letter):
#     return letter in 'aeiou'
#
#
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# filtered_vowels = filter(filter_vowels, letters)
# print(*filtered_vowels)
#
# listA = [2, 3, 4]
# listB = [3, 2, 1]
#
# result = sum(map(pow, listA, listB))
# print(result)
#
# from operator import mul
# from functools import reduce
#
# result = reduce(mul, range(1, 6))
# print(result)
#
# from operator import add
#
# result = list(map(add, 'abc', '1234'))
# print(result) #['a1', 'b2', 'c3']
#
# from operator import mul
#
# result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
# print(result) #['a', 'bb', 'ccc']
#
# from operator import add
# from functools import reduce
#
# result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(result)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
#
# new_strings = list(map(lambda x, y: x*y, strings, numbers))
#
# print(new_strings) #['aaa', 'bb', 'c', 'dddd', 'eeeee']


# numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
# positive_numbers = list(filter(lambda x: x > 0, numbers))      #  положительные числа
# large_numbers = list(filter(lambda x: x > 50, numbers))        #  числа, большие 50
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))     #  четные числа
#
# print(positive_numbers)
# print(large_numbers)
# print(even_numbers)

# def generator_square_polynom(a, b, c):
#     def square_polynom(x):
#         return a*x**2 + b*x + c
#     return square_polynom
# #Такой код можно переписать так:
#
# def generator_square_polynom(a, b, c):
#     return lambda x: a*x**2 + b*x + c

# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
#
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
#
# print(result) #['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

#
# from functools import reduce
#
# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
# result = reduce(lambda x, y: x + y, obj, 0)
#
# print(result)

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num:round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name)>4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# a1 = filter(lambda x: x[1]>10000000 and x[2] == 'primary',data)
# a2 = list(sorted(map(lambda x: x[0], a1)))
# sentence = reduce(lambda x, y: x +', '+ y, a2)
# print(f'Cities: {sentence}')
#
# numbers = [1, 2, 5, 3, 4]
# numbers.sort(key=lambda x: -x)
# print(numbers)

#
# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
#
# print(func(19))
# print(func(13))
# print(func(20))
# print(func(15))
# print(func(247))

# func = lambda x: True if x.lower()[0] == 'a' and x.lower()[-1] == 'a' else False
#
# print(func('abcd'))
# print(func('bcda'))
# print(func('abcda'))
# print(func('Abcd'))
# print(func('bcdA'))
# print(func('abcdA'))
from operator import *

# is_num = lambda b: True if b.replace('.', '', 1).replace('-', '', 1).isdigit() and b.rfind('-') <= 0 else False
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))


# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry',
#          'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# print(*sorted(list(filter(lambda x: len(x) == 6, words))))
#
#
# nums = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80,
#            80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78,
#            83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74,
#            15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = list(map(lambda x: x//2 if x%2==0 else x, filter(lambda x: x%2==0 or (x%2!=0 and x<47), nums)))
# print(*res)
#
# colors = ['red', 'green', 'blue']
#
# for pair in enumerate(colors, 100):
#     print(pair)
#
# colors = ['red', 'green', 'blue']
#
# pairs = enumerate(colors)
#
# print(pairs)
# print(list(pairs))
#
# numbers = [1, 2, 3]
# words = ['one', 'two', 'three']
#
# for pair in zip(numbers, words):
#     print(pair)
#
#     numbers = [1, 2, 3]
#     words = ['one', 'two', 'three']
#
#     result = zip(numbers, words)
#
#     print(result)
#     print(list(result))
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# result = 0
# for x, y in zip(list1, list2):
#     print(x,y)
#     result += x*y
#     print(result)


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
#     for word in ignore:
#         if word in command:
#             return True
#     return False
#
# ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
# ignore_command = any(map(lambda x: x in ignore, ignore))
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))
import math
#
# a = 3
# b = 4
# c = math.sqrt(a*a + b*b) #гипотенузa
# print(c)
#
# a = 3
# b = 4
# c = 5
# perimeter = a + b + c #периметр
# s = (a + b + c) / 2
# area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #Формула Герона
# print(area, perimeter)
#
#
# n = 23810
# seconds = n % 60
# hours = (n // 3600 )
# minutes = n % 3600 // 60
# print(hours)
# print(minutes)
# print(seconds)

# price_new = 89.99
# price_old = 75.50
# result = round((((price_new*100) / price_old) - 100), 2) #19.19

#
# price_new = 24
# price_old = 72
# # result = #66.67
#
# result = abs(round((((price_new*100) / price_old) - 100), 2))
#
# print(result)

from functools import reduce

# a = 5
# b = str(10)
# c = bool(True)
#
# my_sum=a + int(b) + int(c)
# print(my_sum)

# def sum_digit(**kwargs):
#     return sum([int(v) for k,v in kwargs.items()])
#
# print(sum_digit(a=5, b="10", c=True))

# x = 2
# inf = f'{x}' '+' f"{x}0{x}0{x}".split('+')
# result = sum([int(i) for i in inf])
# print(result)

# m = 410
# optimal_sleep_duration = False
# m = 500
# # optimal_sleep_duration = True
# optimal_sleep_duration = True if 7 <= m // 60 <= 9 else False
# print(optimal_sleep_duration)
# x = 21
# result=True if x % 3 == 0 and x % 7 == 0 else False
# print(result)

#
# print(False ** True)
# print(False - True)
# print(True ** 0.5)
# print(True + 0.1)
# print(True + 0)
# print(bool(False + 1))
# print(2 == True)

#
# string1 = '\'Манчестер Юнайтед\' - чемпион Англии!\n2013'
# print(string1)
# print("Hello\nworld!")
# print("C:\\Users\\user\\Desktop\\file.txt")
# print("Name:\tJohn")
# print('It\'s a beautiful day!')
# print("It's a beautiful day!")


# for i in range(4):
#     for j in range(4):
#         print('*', end=' ')
#     print()


# a = [1,2,3,4,5,6,7,2,3]
# count = a.count(1)
# print(count)

# my_list = [1, 2, 2, 3, 2]
# index = my_list.index(2, 2, 5)
# print(index) # 2

#
# my_list = ['Anatoly', 'Fedor', 1, 2, 3]
# first_item = my_list[0]
# last_item = my_list[-1]
# reversed_list = my_list[::-1]
# even_items = my_list[::2]
# # even_items = ['Anatoly', 1, 3]
#
# print(first_item)
# print(last_item)
# print(reversed_list)
# print(even_items)


# var_1 = list(range(-100, 101))
# var_2 = list(range(250, -1, -2))
# var_3 = list(range(101, 201, 2))
#
# # print(var_1)
# # print(var_2)
# print(var_3)
#
# my_list = [1, 10, 0, 10, 11]
# eleven_index = my_list.index(11)
# ten_count = my_list.count(10)
# print(eleven_index)
# print(ten_count)

# student_names = ['Ian', 'Ivan']
# scores = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lessons = ['Python', 'Analytics']
#
# # ===>
# #
# # student_names = ['Ian', 'Ivan', 'Anatoly', 'Oksana']
# # scores = [0, 2, 3, 5, 6, 7, 8, 9]
# # lessons = ['Analytics', 'Python']
# student_names.append('Anatoly')
# student_names.append('Oksana')
# scores.pop(1)
# scores.pop(3)
# scores.pop(-1)
# lessons.sort()
# print(student_names)
# print(scores)
# print(lessons)


# numbers_list = [1, 1, 2, 2, 3, 3, 4, 4]
# numbers_list_ordered = sorted(numbers_list, reverse=True)
# numbers_set = set(sorted(set(numbers_list).union(set([max(numbers_list) + 1]))))
# numbers_frozenset = frozenset(sorted(set(numbers_list).difference(set([min(numbers_list)]))))
# print(numbers_list_ordered)
# print(numbers_set)
# print(numbers_frozenset)


list_1 = [1, 5, 3]
list_2 = [2, 8]
# # ->
# list_1 = [1, 3, 5]
# list_2 = [8, 2]
# list_3 = [1, 2, 3, 5, 8]
# list_3_len = 5
# list_3 = []
# list_1 = sorted(list_1)
# list_2 = sorted(list_2, reverse=True)
# list_3.extend(list_1)
# list_3.extend(list_2)
# list_3 = sorted(list_3)
# list_3_len = len(list_3)
# print(list_1)
# print(list_2)
# print(list_3)
# print(list_3_len)

# menu = {'White Chocolate Mocha', 'Americano', 'Flat White', 'Latte',
#         'Blueberry Muffin', 'Chocolate Chip Cookie'}
# stop = {'White Chocolate Mocha', 'Blueberry Muffin'}
# # menu_today = {'Americano', 'Flat White', 'Latte', 'Chocolate Chip Cookie'}
# menu_today = menu.difference(stop)
# print(menu_today)

# my_set = {0, 10, 100}
# to_delete = 0

# ====>
# my_set = {10, 100} # удалили 0
#
# my_set = {0, 10, 100}
# to_delete = -2
# my_set.discard(to_delete)
# # ====>
# # my_set = {0, 10, 100} # ничего не сделали
#
# print(my_set)

# students = {'Кравченко Виталий', 'Полякова Ольга', 'Некрасов Игорь', 'Дудочкин Илья', 'Захарова Мария'}
# new_student = 'Василенко Анна'
# churn_student = 'Полякова Ольга'
# # ->
# # students = {'Кравченко Виталий', 'Некрасов Игорь', 'Дудочкин Илья', 'Захарова Мария', 'Василенко Анна'}
#
# students.add(new_student)
# students.remove(churn_student)
# print(students)

# # студенты курса "Аналитик данных"
# da_students = {'Ivanov Alexander', 'Loginov Vladislav', 'Ershova Anna', 'Korneva Daria'}
# # студенты курса "Визуализация данных"
# dv_students = {'Ershova Anna', 'Egunov Andrey', 'Ignatov Alexey', 'Loginov Vladislav'}
#
# # результат
# # students = {'Loginov Vladislav', 'Ershova Anna'}
#
# students = da_students.intersection(dv_students)
# print(students)

# a = [1, 2, 4, 3]
# one = sum(a[:len(a)//2])
# two = sum(a[len(a)//2:])
# res= True if one == two else False
# print(one, two, res)

# a = [1, 2, 2, 1, 3, 2, 3]
# b = 1
#
# a.remove(b)
# a.reverse()
# a.remove(b)
# a.reverse()
# print(a)

# -> a = [2, 2, 3, 2, 3]
#
# a = [1, 2, 2, 1, 3, 2, 3]
# b = 2
# # -> a = [1, 2, 1, 3, 3]
# a.remove(b)
# a.reverse()
# a.remove(b)
# a.reverse()
# print(a)


# a = [2, 3, 4, 5, 1, 10, -1, 7]
# #
# # """
# # найти и вывести на экран сумму элементов равных 9
# #
# # """
#
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == 9:
#             print(a[i], a[j])
#
# try:
#     a, b = int(input('введите число номер 1: ')), int(input('введите число номер 2: '))
# except ValueError:
#     print('Ввод должен быть числом')
# count = 0
# for i in range(a, b +1):
#     print(i)
#     count += i
# print()
# print(f'Кол-во чисел {count}')

# a = [1,3, 4, 5, 6, 7,8, 9, 0]
# count = 0
# b = []
# while len(a) > count:
#     if a[count] % 2 == 0:
#         b.append(a[count])
#     count += 1
#
# print(b)

# a = [1, 3, 4, 6, 7, 8, 9, 0]
# count = 0
# for i in range(len(a)):
#     if len(a) + a[0] == 9:
#         print(a[i])
#     count += 1


# x = 'шалаш'
# result=[]
# for i in str(x):
#     result.append(i)
# print(result)
# if result[0] == result[-1]:
#     print('yes')
# else:
#     print('no')
#
#


