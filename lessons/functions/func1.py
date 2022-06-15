# def <name_of_function>(a,b # параметры функции):    
#     ...
#     body
#     ...
#     return 'some text'

# <name_of_function(5,6 # аргументы функции)>

# Аргументы функции - это переменная либо данные, которые мы передаем для параметров функции
# при вызове функции

# Параметры функции - это значения которые принимают функции, 
# в теле функции мы работаем с этими данными или переменными.


# return нужен для того, чтобы функция что то возвращала, для того чтобы мы могли работать с 
# результатом функции, return является необязательным 
# (в таком случае возвращает - None - по дефолту)


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# a = 5
# b = int(input('Введите число: '))

# print(isEven(11))
# print(isEven(8))
# print(isEven(a))
# print(isEven(b))


# Аннотации к функциям

# def isEven(num: int) -> bool:
#     """
#     Наша функция проверяет является ли число типа int четным.
#     """
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# isEven()


# def get_polindrom(words: list) -> list:
#     """
#     Функция возвращает список из полиндромов
#     """
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#         else:
#             continue
#     return result

# some_words = ['John', 'ono', 'Kazak', 'Peter', 'Anna', 'dovod', 'apa', 'tenet','juice']


# print(get_polindrom(some_words))


# def func():
#     print('Hello')

# func()

#**********************************
# default parametres

# def welcome(name = 'user'):
#     print(f'Welcome, {name}!')

# welcome('Elzar')


# def get_percentage(money: float, period: int) -> float:
#     """
#     Return final amount of money.
#     """
#     i = 0
#     while i < period:
#         money = money + (money * 0.10) # money*1.1 / money +(money/100*10)
#         i += 1

#     return money 

# money = float(input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: ')) 
# print(get_percentage(money, year))




# def get_reverse(text: str) -> str:
#     """Return reversed string"""
#     spisok = text.split(' ')
#     ls = []
#     for item in spisok[::-1]:
#         ls.append(item)
#     result_str = ' '.join(ls)
#     print(result_str)
#     return result_str

# get_reverse('Hello world! My name is John, last name is Snow. Nice to meet you!')
 


# 1. Создайте функцию, которая будет
# принимать 2 числа, складывать их и возвращать результат сложения.

# def sum_of_numbers(num1, num2: int) -> int:
#     """Return sum of 2 numbers"""
#     res = num1 + num2
#     return res

# num1 = int(input('Введите чило 1: '))
# num2 = int(input('Введите число 2: '))
# print(sum_of_numbers(num1, num2))


# 2. Создайте функцию, которая будет принимать строку. 
# Функция должна выводить длину этой строки.
# """

# def len_of_string(text:str) -> int:
#     """Функция выводит длину строки"""
#     res = len(text)
#     return res

# text = input('Введите текст: ')
# print(len_of_string(text))


# 3. Создайте функцию, которая принимает два обязательных параметра. Задача этой 
# функции выводить тип данных принятых аргументов.
# """

# def type_of_args(t1, n1):
#     res = type(t1)
#     res2 = type(n1)    
#     return res, res2
    

# t1 = 'Hello world'
# n1 = 55

# print(type_of_args(t1,n1))

# 5. Создайте функцию, которая принимает словарь. 
# Пройдитесь по словарю циклом и распечатайте все его ключи

# def dict_(dict1):
#     keys = {keys for keys in dict1.keys()}
#     return keys

# dict1 = {'a':1, 'b':2, 'c':3}
# print(dict_(dict1))

# 6. Напишите функцию, которая принимает список чисел и возвращает их произведение.

# def product_of_nums(num1, num2):
#     prod = num1 * num2
#     return prod

# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))

# print(product_of_nums(num1, num2))

# 7. Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр.

# def sum_of_nums(number):
#     nums = [int(i) for i in number]
#     res = sum(nums)
#     return res

# number = input('Ввдите число: ')

# print(sum_of_nums(number))


# 8. Создайте функцию, которая принимает число и выводит "It's even number" 
# если число четное(делится на 2 без остатка - 2, 4, 20 и.т.п), если же число
#  нечетное (3, 9 и.т.п) функция должна выводить "It's odd number".

# def even_or_odd(num):
#     if num % 2 == 0:
#         return "it's even number"
#     else:
#         return "it's odd number"

# num = int(input('Введите число: '))
# print(even_or_odd(num))


# 9. Создайте функцию которая принимает от пользователя два числа. 
# Функция должна сравнить эти числа между собой и вывести максимальное значение.


# def max_of_nums(number1, number2):
#     # if number1 > number2:
#     #     return number1
#     # else:
#     #     return number2
#     max_ = max(number1, number2)
#     return max_

# number1 = int(input('Введите число 1: '))
# number2 = int(input('Введите число 2: '))

# print(max_of_nums(number1, number2))

# def is_polindrom(txt:str)-> bool:
#     """Функция проверяет является ли строка палиндромом"""
#     for words in txt:
#         if txt[::].lower().strip() == txt[::-1].lower().strip():
#             return True
#         else:
#             return False

# txt = input('Введите слово: ')
# print(is_polindrom(txt))

# 1.Напишите функцию которая принимает интервал в виде двух чисел, например 1000 и 3001 и 
# выдает список всех чисел, в заданном интервале, состоящиx из четных цифер - 
# ['2000', '2002', '2004', '2006', '2008', '2020', '2022', '2024', '2026' ... ] 

# def even_nums(range1, range2):
#     ls = []
#     for i in range(range1, range2):
#         if i % 2 == 0:
#             ls.append(i)
#     return ls 
            

# range1 = int(input('Введите интервал1: '))
# range2 = int(input('Введите интервал2: '))    

# print(even_nums(range1, range2))

# 2. Вы используете приложение для построения маршрутов - каждый раз, 
# когда вы нажимаете кнопку, приложение отправляет вам маршрут для прогулки в виде 
# списка однобуквенных строк 
# (например, ['с', 'ю', 'з', 'в'] - север, юг, запад и восток соответственно). 
# Вы всегда проходите только один квартал для каждого направления, и тратите ровно одну 
# минуту для пересечения одного городского квартала. Напишите функцию, которая вернет True, 
# если прогулка, которую дает вам приложение, 
# займет у вас ровно десять минут с учетом того, что вы также должны успеть вернутся в исходную 
# точку. В противном случае программа должна вернуть False. 




