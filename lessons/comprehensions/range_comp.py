
# range
# list comprehesions
# dict comprehesions

# range -> start:end:[step]
# ls = list(range(1,100,2))
# print(ls)

# for x in range(1,100,25):
#     print(x)

# for x in range(100,-1,-2):
#     print(x)

# hello = 'hello world'
# for x in range(0,len(hello)):
#     print(hello[x])


# ----------------------------------------
# list comprehensions
# синтаксис:
# newlist = [expression for item in iterable <if condition == True>]

# ls = []
# for i in range(1,100,2):
#     ls.append(i)

# print(ls)

# ls = [i for i in range(0,100,2)]
# print(ls)

# ls = [i * i # i **2 for i in range(1,11)]
# print(ls)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if 'a' in x]
# print(ls)

# ls = [x for x in fruits if x != 'apple']
# print(ls)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# new_list = [n for n in list1 if n % 2 == 0 if n % 3 == 0]
# print(new_list)

# list_ = [[1,2,3], [3,4,5], [7,8,9]]
# ls = [num for x in list_ for num in x]
# print(ls)

# # С помощью for
# ls = []
# for x in list_:
#     for num in x:
#         ls.append(num)
# print(ls)

# from datetime import datetime

# start = datetime.now()
# ls = []
# for x in range(1, 1000000):
#     ls.append(x)
# print(datetime.now() - start)

# ls = [x for x in range(1, 1000000)]
# print(datetime.now() - start)


# ls = [x + 10 if x == 8 else x+1 for x in range(1,100) if x % 2 == 0]
# print(ls)

# ls = [x**2 if x%2==0 else x**3 for x in range(1, 101)]
# print(ls)

# ----------------------------------------------
# dict comprehensions
# dict_ = {'key1' : 'value1', 'key2' : 'value2'}
# new_dict = {key: value*2 for key, value in dict_.items()}
# print(new_dict)

# dict_ = {n:n**2 for n in range(1,11)}
# print(dict_)

# dict1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6}
# new_dict = {key: 'even' if value%2==0 else 'odd' for key, value in dict1.items()}
# print(new_dict)

# names = ['John', 'Jamie', 'Tirion', 'Peter', 'Sansa']
# dict_names = {i:value for i, value in enumerate(names)}
# print(dict_names)

# inp = int(input('Введите число от 1 до 10: '))
# dict_ = {inp : [x for x in range(1,500) if inp%x == 0]}
# print(dict_)


# 11. Дан словарь, в котором значениями являются целые числа. Пройдитесь по элементам 
# и замените значения на список чисел от 1 до числа, которое является значением. 
# Нужно использовать comprehension.
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {key: [value for value in range(int(value+1))] for key, value in a.items()}
# print(dict_)

# 12 задание
# dict_ = {'age': 20, 'year_of_birth': 2000, 'weight': 61}
# new_dict = {key: ['even' if value % 2 == 0 else 'odd'] for key, value in dict_.items()}
# print(new_dict)

# 13 задание:
# a = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# nums = [a.find('13') num for num in a]
# print(nums)



