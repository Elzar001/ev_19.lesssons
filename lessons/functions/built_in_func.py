# Встроенные функции 
# print()
# list()
# len()
# max()
# sum()
# min()
# divmod()
# globals()
# locals() etc..


# map()
# filter()
# zip()
# enumerate()
# functools.reduce() # из библиотеки functools


# Анонимные функции - lambda(такие же функции только без названия)

# Pythonic way 
# sum_ = lambda number: number+1
# result = sum_(5)
# print(result)


# Task сумма (10-10000)

# a, b = 10, 10000
# total_sum = 0
# while a <= b:
#     total_sum += a
#     a += 1
# print(total_sum)


# result = sum(range(10,10000))
# print(result)

# -------------------------------
# map(function, iterable) -> Она применяет функцию каждый элемент из itarable. 
# Возвращает mapobject

# numbers = [1,2,3,4,5]
# second = [1,2,3,4,5]
# # 3 способ:
# result3 = list(map(lambda *numbers: sum(numbers), numbers, second))
# print(result3)
# # 2 способ:
# def func(*numbers):
#     return sum(numbers)
# result2 = list(map(func, numbers, second))
# print(result2) 
# # 1 способ:
# def func1(numbers1, numbers2):
#     new_list = []
#     for i in range(0,5):
#         new_list.append(numbers1[i]+numbers2[i])
#     return new_list

# result1 = func1(numbers, second)
# print(result1)

# names = ['John', 'Jamie', 'Sansa']

# def function(name):
#     return f'Hello mr/mrs {name}'
# res = list(map(function, names))
# print(res)

# dict_ = {1:2, 3:4, 5:6}
# # {1:'2', 3:'4'...}
# listOfStrings = list(map(lambda value: str(value), dict_.values())) # ['2', '4', '6']
# # print(listOfStrings)
# def update_dict(values):
#     i = 0
#     for key in dict_:
#         dict_[key] = values[i]
#         # print(values[i], f'index: {i}')
#         i += 1
# print('Before', dict_)
# update_dict(listOfStrings)
# print('After:', dict_)

#---------------------------------
#filter(function, iterable) - Фильтрует по принципу того, что функция должна возвращать True.
# numbers = list(range(1,16))
#     #[2,4,6,8,10,12,14]
# # 2 способ:
# result = list(filter(lambda num: num % 2 == 0, numbers))
# print(result)

# 1 способ:
# def filter_nums(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# result = list(filter(filter_nums, numbers))
# print(result)

# symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'i', 'o', 'z']

# vowels = ['a', 'e', 'i', 'o', 'u', 'y']

# result = list(filter(lambda x: x in vowels, symbols))
# print(result)

# -----------------------------------
# zip(iterable, iterable, *) -> Он сопоставляет и соединяет каждый элемент из iterables.
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# result = list(zip(a, b))
# print(result)

# -------------------------------------
# reduce(function, iterable) -> Над каждым элементом из iterable применяет функцию
# при этом сохраняя результат, после возвращает одно значение # import from functools

# from functools import reduce

# numbers = [1,2,3,4,5]
# result = reduce(lambda x, y: x * y, numbers)
# print(result)


# list_ = ['ccc', 'aaaa', 'bb', 's']

# result = reduce(lambda x,y: x if len(x) > len(y) else y, list_)
# print(result) 

# ----------------------------------------------------
# enumerate()
# ls = [12,213,23423,121,3,23]
# for i, x in enumerate(ls):
#     print(f'index: {i}, element: {x}')

# *************************************************************************

# names = ['Raychel', 'John', 'Sandy', 'Fin', 'Kira', 'Chip', 'Deyle', 'Sooronbai']

## Your name is {len > 4}

# new_ls = list(map(lambda name: f'Your name is: {name}', filter(lambda name: len(name) >4, names)))
# print(new_ls)

# *-*-*-*--*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*--*-*-*-*--*-*-*
# Генератор паролей и шифров
from random import choices
from string import ascii_letters, digits
from itertools import repeat

print({f(choices(ascii_letters, k=5),choices(digits, k=5)) 
for f in repeat(lambda x,y: ''.join(set(x+y)), int(input('Введите кол-во паролей: ')))})

# --------------
import string
import random
def generate_rand_names():
    random_name =''.join(
        random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
        for i in range(1, 9) )
    return random_name

print(generate_rand_names())

random_name1 = str()



