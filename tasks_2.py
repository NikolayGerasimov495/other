# #НАЙТИ МАКСИМУМ
# number = [12,31,4,5,53,99]
# def num_max(num):
#     return max(num)
# print(num_max(number))
#
# # ПОДСЧЕТ ЦИФР ПОВТОРЕНИЙ
# # from collections import Counter
# # elements = [2, 3, 4, 2, 2, 4, 5, 6, 7]
# # def count(lst):
# #     return Counter(lst)
# # print(count(elements))
# #
# repeats = {}
# for elem in elements:
#     if elem in repeats:
#         repeats[elem] += 1
#     else:
#         repeats[elem] = 1
# print(repeats)
#
# #ОДНО ЧИСЛО КОТОРОЕ ЧАСТО ПОВТОРЯЕТСЯ
# (from collections import Counter)
# elements = [2, 3, 4, 2, 2, 4, 5, 6, 7]
# def count(lst):
#     return Counter(lst).most_common(1)[0][0]
# print(count(elements))


# from collections import Counter  #ПОДСЧЕТ ЧИСЕЛ СПИСКА ПО ЭЛЕМЕНТНО
# print(Counter([2, 2, 3, 4, 5, 6, 7]))
#
# # print('-------------------------------------')
# #
# a = [43, 5, 20, 30, 99]
# for i in a:
#     print(i, a.index(i))
# #
# for i in range(5): #on index
#     print(i, a[i])
#
# a = [1,2,3,32,2,3]
# b=[]
# for i in a:
#     if not i in b: #удаляем дубли
#         b.append(i)
# print(b)
#
# a = [1,2,3,32,2,3]
# nechet=[]
# chet=[]
# n = len(a)
# for i in range(n):
#     if a[i]%2==0:
#         chet.append(i)
#     elif a[i]%2!=0:
#         nechet.append(i)
# print(nechet)
# print(chet)
#
# vowels='aeiou'
# s = 'audncbcjoonclkncqkuiiqoq'
# n=len(s)
# for i in range(n-1):
#     if s[i] in vowels and s[i+1] in vowels:
#         print(s[i], s[i+1])
# #
# for i in range(4):
#     for j in range(6):
#         print('*', end = '')
#     print()
#
# for i in range(10):
#     for j in range(i):
#         print('*', end = '')
#     print()
# #
# s = input() #сколько раз встречалася элемент
# d = {}
# for i in s:
#     if i.isalpha():
#         d[i] = d.get(i, 0) + 1
# print(d)
#
# def factorial(x):
#     pr = 1
#     for i in range(2, x+1):
#         pr*=i
#     return pr
# #


# # n = int(input())
# # for i in range(1, n + 1):
# #     print(i, factorial(i))
#
# def func(*args): # при помощи данного оператора можем передать бесконечное кол-во НЕИМЕНОВЫННЫХ элементов. Все они будут распаковываться в виде кортежа.
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(func(123, 12, 12, 21, 1, 12))
# #
# print(func(1,2123,132,13,123,))
# def func(**kwargs): #для именнованных параметоров. Создается словарь.
#     for k, v in kwargs.items():
#         print(k, v)
#
# func(a=1, b=3, c=4)
#
# #
# def rec(x):   #РЕКУРСИЯ в простом виде
#     if x<4:
#         print(x)
#         rec(x+1)
#         print(x)
# #
# rec(1)
#
# def palindron(s):
#     if len(s) == 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindron(s[1 : -1])
#
# print(palindron('шалаш'))
#
# s =list(map(int, input().split()))
# print(s)

# # def d(x):
# #     return x>9 and x<100
#
# a = ['14', ' ', 'hello','qdqqq', 'qq']
# b = list(filter(lambda x: len(x)>3, a))
# print(b)
c = '123123dqadqcqc12acqcfqcwqfc'
v = list(filter(str.isdigit, c))
print(v)
# # #
#
# ДЕКОРАТОР

# def header(func):
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h>>')
#     return inner
#
# def table(func):
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>>')
#     return inner
# @table
# @header
# def say (name, first_name, age):
#     print('Hello', name, first_name, age)
#
# say('Vasya', 'Ivanov', 18)

# from functools import wraps
#
# def table(func):
#
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print('<table>')
#         func(*args, **kwargs)
#         print('</table>>')
#     return inner
#
# @table
# def sqr (x):
#     """
#     функция возводить в квадрат х
#     :param x:
#     :return:
#
#     """
#     print(x ** 2)
#
# sqr(2)
# print(sqr)
# print(sqr.__name__)
# print(sqr.__doc__)
# #

# def log_ex(func):
#     def name(*args):
#         print(f'arguments: {args}')
#         return func(*args)
#     return name
#
#
# @log_ex
# def add_numbers(a, b):
#     return a + b
#
#
# result = add_numbers(3, 5)
# print("result:", result)
#


# GIT
# #main
# 1
# 2
# 3
# 4
#
# feature
# 1
# 2
# 2.1
# 2.2
#
# #feature >>  main
#
# 1
# 2
# 2.1
# 2.2
# 3
# 4
#
# 1. (main) git checkout - b TEMP_MAIN
# 2. (main) git reset --hard 2
# 3.git merge feature
# 4. (main) git cherry_pick TEMP_MAIN 3 4

# data = (['bee'], 'pygen')
# data[0] += ['geek']
# print(data)


# def convert(n):
#     return ''.join(map(str, range(n+1)))
#
# print(convert(12))
# 0123456789101112

# is_even = lambda x: x % 2 == 0
#
# seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# filtered = filter(is_even, seq)
# print(list(filtered))
#
#
# seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
# result = map(lambda x, y: x + y, seq, seq2)
# print(list(result))

# fib1 = fib2 = 1
# n = int(input())
# print(fib1, fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# def find_missing(lst):
#     return sorted(set(range(lst[0], lst[-1])) - set(lst))
# #
# # # Driver code
# lst = [1, 2, 4, 6, 7, 9, 10, 10, 12]
# print(find_missing(lst))
#
# print(set(lst))
#
# b=[]
# for i in range(lst[0], lst[-1]):
#     b.append(i)
#
# print(sorted(set(b) - set(lst)))

# #считает сумму чисел
# a = int(input('Введите число: '))
# s = 0
# while a > 0:
#     s += a % 10
#     a = a // 10
# print(s)

# s = input('Введите строку: ')
# a = ''
# for i in s:
#     if i not in a and i != ' ':
#         a += i
# print(a)
from collections import Counter
#
# s = input('Введите строку: ').split()
# print(len(s))

# a = 'hello'
# # print(sorted(a, reverse=True))
# res = ''
# for i in range(len(a)-1, -1, -1):
#     res += a[i]
# print(res)


''' 1) уметь находить максимальный элемент в одномерном массиве '''
# a = [2, 1, 2, 3, 4, 5, 6, 7]
# # print(max(a))
# #
# # max = a[0]
# elem = 0
# for i in range(len(a)):
#     if a[i] > a[elem]:
#         elem = i
# #
# print(elem)


'''2) уметь находить максимальный элемент с четным/нечетным индексом в одномерном массиве '''
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# chet = []
# nechet = []
# for i in a:
#     if i % 2 == 0:
#         chet.append(i)
#     if i % 2 != 0:
#         nechet.append(i)
# print(max(chet))
# print(min(nechet))




''' 3) уметь посчитать количество пар элементов, у которых произведение/сумма/разность будет равняться какому-то числу 8 '''
# a = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10, 0]
# # total = []
# sub = []
# mult = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] == 8:
#             t = a[i], a[j]
#             total.append(t)
#
#         elif a[j] - a[i] == 8 or a[i] - a[j] == 8:
#             l = a[i], a[j]
#             sub.append(l)
#
#         elif a[i] * a[j] == 8:
#             m = a[i], a[j]
#             mult.append(m)
#
# print(len(total), total)
# print(len(sub), sub)
# print(len(mult), mult)


''' 4) уметь посчитать в массиве количество подотрезков с суммой равной какому-то числу k. Решение за O(n^3) '''


# a = [1, 5, 3, 4]
# lists = []
# for i in range(len(a)+1):
#     for j in range(i):
#         lists.append(a[j:i])
#         lists = sorted(lists, key=len)
#
# print(lists)

''' 5) уметь развернуть массив (например, из массива [5, 4, 3, 10, -1] получить [-1, 10, 3, 4, 5]) '''
# a = [5, 4, 3, 10, -1]
# print(list(reversed(a)))


# 6) уметь циклически сдвинуть массив на какое-то число k

#
# class Human():
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight
#
#     @staticmethod
#     def check(value):
#         if not isinstance(value, (int, float)) or value < 0:
#             raise TypeError("Значение роста и веса человека должно быть неотрицательным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height_value):
#         self.check(height_value)
#         self.__height = height_value
#         self.__body_mass_index = None
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight_value):
#         self.check(weight_value)
#         self.__weight = weight_value
#         self.__body_mass_index = None
#
#     @property
#     def body_mass_index(self):
#         if self.__body_mass_index is None:
#             self.__body_mass_index = self.weight / self.height ** 2
#         return self.__body_mass_index
#
#     def display_bmi(self):
#         if self.body_mass_index < 18.5:
#             print("Недостаточная масса")
#         elif self.body_mass_index > 25:
#             print("Избыточная масса")
#         else:
#             print("Оптимальная масса")
#
#
# weight, height = float(input()), float(input())
# Human(height, weight).display_bmi()


# a = int(input())
# print(f'{a:,}')

# i = lambda x: x + 2
# print(i(4))
# print(list('123'))
# a = tuple('cnhjrf')
# print(a)
