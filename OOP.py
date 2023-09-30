#
# clname=None
#     model = 'BMW'
#     engine= 1.6
# @staticmethod
# def drive():
#     print("Let`s go!")
import self


# class Car:
#
#     def __init__(self, name='BMW', color='black', engine='benz', road='AWD'):
#         print('Hello new object is', self, name, color, engine, road)
#         self.name = name
#         self.color = color
#         self.engine = engine
#         self.road = road
#
# class Cat:
#
#     def __init__(self, name, bread='pers', age=1, color='black'):
#         print('hello new object is', self, name, bread, age, color)
#         self.name = name
#         self.age = age
#         self.bread = bread
#         self.color = color


# class Point:
#
#     def __init__(self, coord_x=0, coord_y=0):
#         self.move_to(coord_x, coord_y)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0,0)
#
#     def print_point(self):
#         print(f'Точка с координатами ({self.x},{self.y})')

#
# class BankAccount:
#
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     def print_public_data(self):
#         self.__print_private_data()
#
#     def print_protected_data(self):
#         print(self._name, self._balance, self._passport)
#
#     def __print_private_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# account1 = BankAccount('Bob', 10000, 4512123)
# account1.print_public_data()
# # print(account1.__name)
# # print(account1.__balance)
# # print(account1.__passport)
# a = BankAccount()

# class BankAcc:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property
#     def my_balance(self):
#         print('get balance')
#         return self.__balance
#
#     @my_balance.setter
#     def my_balance(self, value):
#         print('set balance')
#         if not isinstance(value, (int, float)):
#             raise ValueError('Баланс должен быть числом')
#         self.__balance = value
#
#     @my_balance.deleter
#     def my_balance(self):
#         print('delete balance')
#         del self.__balance

# from string import digits
#
# class User:
#     def __init__(self, login, password):
#         self.login = login
#         self.__password = password
#         self.__secret = 'abracadabra'
#
#     @property
#     def secret(self):
#         s = input('введите ваш пароль')
#         if s == self.__password:
#             return self.__secret
#         else:
#             raise ValueError ('доступ закрыт')
#
#     @property
#     def password(self):
#         print('getter called')
#         return self.__password
#
#     @staticmethod
#     def is_include_number(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#             return False
#
#     @password.setter
#     def password(self, value):
#         print('setter called')
#         if not isinstance(value, str):
#             raise TypeError('Пароль должен быть строкой')
#         if len(value) < 4:
#             raise ValueError('Длина пороля короткая, минимум 4 символа')
#         if len(value) > 12:
#             raise ValueError('Длина пороля длинная, максимум 12 символов')
#         self.__password = value

# class BankAccount:
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other):
#         print('__add__ call')
#         if isinstance(other, BankAccount):
#             return self.balance + other.balance
#         if isinstance(other, (int, float)):
#             return self.balance + other
#         raise NotImplemented
#
#     def __mul__(self, other):
#         print('__mul__ call')
#         if isinstance(other, BankAccount):
#             return self.balance * other.balance
#         if isinstance(other, (int, float)):
#             return self.balance * other
#         if isinstance(other, str):
#             return self.name + other
#         raise NotImplemented
#
#     def __radd__(self, other):
#         print('__radd__ call')
#         return self + other
#
# class Person:
#
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#     def breathe(self):
#         print('человек дышит')
#
#     def __str__(self):
#         return (f'Person {self.name} {self.lastname}')
#
#
#     def info(self):
#         print('Person class')
#         print(self)
#
#
# class Doctor(Person):
#
#     def __init__(self, name, lastname, age):
#         super().__init__(name, lastname)
#         self.age = age
#
#     def breathe(self):
#         print('доктор дышит')3
#         super().breathe()
#
#     def __str__(self):
#         return (f'Doctor {self.name} {self.lastname}')
#
#
#
# p = Person('ivan', 'ivanov')
# d = Doctor('vasya', 'petrov', 25)
# print(p.name, p.lastname)
# print(d.name, d.lastname, d.age)
# d.info()
# p.info()
