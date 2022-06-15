# def say_hello():
#     print('Hello world')
#     return 'Hello world'

# # print(say_hello())
# func = say_hello
# print(func())


# *****************************************

# SOLID
# 1. S - single responsibility (Принцип единой обязанности)
# list_of_names = ['John', 'Sansa', 'Jamie']
# 2. O
# 3. L
# 4. I
# 5. D

# *****************************************

# def append_to_list(name):
#     list_of_names.append(name)
#     print(list_of_names) #Вторая обязанность(не рекомендуется)

# def read_list():
#     print(list_of_names) 

# def delete_name(name):
#     if name not in list_of_names:
#         print('Такого имени нет!')
#         return None
#     list_of_names.remove(name)

# append_to_list('Sanzhar')
# read_list()
# delete_name('Sanzhar')
# delete_name('Tirion')
# read_list()


# Функция высшего порядка - Это функция, которая в качестве аргумента принимает другую функцию

# Декоратор - это функция которая позволяет без изменения кода обернуть другую функцию для расширения 
# функционала обернутой функции

# def decorator(func):
#     print(func)
#     print('Я декоратор')
#     return func()

# def hello():
#     print('Я функция Hello')
#     return 'hello'

# print(hello())
# res = decorator(hello)
# print(res)


# def to_uppercase(func):
#     def wrapper():
#        original_text =  func()
#        modified = original_text.upper()
#        return modified
#     return wrapper

# @to_uppercase 
# def get_text():
#     return 'Hello world'

# print(get_text())


# def benchmark(func):
#     import time 
#     start = time.time()
#     func()e
#     end = time.time()
#     print(f'Время выполнения функции {func.__name__}, заняло: {end - start}')

# def loop():
#     range_number = 1000000
#     i = 0
#     while i <= range_number:
#         print(i)
#         i+=1

# benchmark(loop)


# Pythonic way -> @benchmark
# Синтаксический сахар - это красота кода

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Время выполнения {func.__name__}, заняло: {end - start}')
#     return wrapper

# @benchmark
# def loop():
#     range_number = 500000
#     i = 0
#     while i <= range_number:
#         print(i)
#         i+=1

# loop()

#-------------------------------------------------

# def capitalize_name(func):
#     def wrapper(name):
#         modified_name = name.capitalize()
#         return func(modified_name)
#     return wrapper

# @capitalize_name
# def say_hello(name):
#     return f'Hello {name}'

# @capitalize_name
# def say_whatsup(name):
#     return f"What's up {name}?"

# print(say_hello('john'))
# print(say_whatsup('john'))

#--------------------------------------------------------------
# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div
# @strong
# def get():
#     return 'John Snow'

# print(get())

# --------------------------------------------------------------







