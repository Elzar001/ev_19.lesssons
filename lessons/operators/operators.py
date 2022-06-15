# 07.03.2022

# NoneType
# Условные операторы
# Операторы сравнения
# Логические операторы


#NoneType
# a = None
# db_connection = db.connect(...)
# # db_connection = None
# if db_connection == None:
#     print('Uups chto to powlo ne tak')



# Операторы сравнения
# == (равно), != (не равно)
# <, >, >=, <=
# все операторы сравнения возвращают True/False

# a = 10
# b = 8
# print(a == b) # False
# print(a != b) # True
# str1 = 'Hello'
# str2 = 'World'
# print(str1 > str2) # False 72>87
# print(str1 < str2) # True
# print(ord("H")) # Символ -> ASCII Code
# print(ord("W"))
# a = 'hhw'
# b = 'hab'
# print(ord('h'))
# print(ord('a'))

# a = 'Hello world'
# b = 'John Snow'
# # len() -> Возвращает длину объекта
# print(len(a), len(b))

#chr -> ASCII Code -> символ
# print(chr(1100)) # ь

# bool(x) - возвращает True если x == True, в противном случае False

# 1 -> True
# 0 -> False
# 'a' -> True
# '' -> False

# a = 5
# b = 'abc'
# c = ''
# d = [1,2,3]
# res = f'a is : {bool(a)}\n'
# res1 = f'b is : {bool(b)}\n'
# res2 = f'c is : {bool(c)}\n'
# res3 = f'd is : {bool(d)}\n'
# print(res, res1, res2, res3)


# Условные операторы: if, elif, else

# if <condition> :
#     <body>
#     <body>
# elif <condition>:
#     <body>
# else:
#     <body>

# string = input('Enter smth:')

# if string == 'Hello':
#     print("Hello world")
# elif string == 'Mercedes':
#     print("Mercedes-Benz S-class")
# else:
#     print('Совпадение не найдено!')

# print('End of code')



# Логические операторы:
# and -> логическая "и"
# or -> логич. "или"
# not -> логич. отрицание

# Операторы идентификации:
# in -> Проверяет наличие элемента
# is -> Сравнивает ячейки памяти
    # == -> Сравнивает по значению 
# is not -> Отрицательное сравнение ячеек памяти    

# string = 'Hello world'
# choice = input('Введите символ: ')
# if choice in string:
#     print(f'Символ \"{choice}" есть в данной строке: "{string}"')
# else:
#     print(f'Символа \"{choice}" нет в данной строке "{string}"')

# for number in range(1, 101):
#     if number % 2 != 0:
#         print(f'{number} -> Нечетное!!!')
#     else:
#         print(f'{number} -> Четное!!!')

# Задание
# дано: [1 -- 100]
# если на 3 без остатка - fu
# 5 - ba
# 3, 5 - fuba


# for number in range(1,100):
#     if number % 5 == 0 and number % 3 == 0:
#         print(f'{number} - делится на 3 и на 5 ')
#     elif number % 5 == 0:
#         print(f'{number} - делится на 5 ')
#     elif number % 3 == 0:
#         print(f'{number} - делится на 3 ') 



# Написать калькулятор

# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# operator = input('Введите действие (*, /, +, -): ')

# if operator == '*':
#     print(num1 * num2)
# elif operator == '/':
#     if num2 == 0:
#         print('Деление на 0!')
#     else:
#         print(num1 / num2)
# elif operator == '-':
#         print(num1 - num2)
# elif operator == '+':
#     print(num1 + num2)
# else:
#     print('Неправильный ввод ')

# ************************************

# ДЗ

# a = input('Введите слово: ')
# if len(a) >= 5:
#     print('True')
# else: 
#     print('False')


# Extra ЗАДАНИЯ

# n = int(input('Введите число n: '))
# m = int(input('Введите число m: '))
# k = int(input('Введите число k: '))
# result = (m*n)/2
# if result >= k:
#     print('Yes')
# else:
#     print('No')

# age = int(input('Введите возраст: '))
# dogs_age = 0
# if age <= 2:
#     dogs_age = age * 5.25
# else: 
#     dogs_age = 10.5 + ((age - 2) * 4)
# print(dogs_age)


# 6 задание 

# n1 = int(input('Введите число 1: '))
# n2 = int(input('Введите число 2: '))
# n3 = int(input('Введите число 3: '))
# if n1 < n2 or n2 > n1:
#     print(n1)
# elif n3 < n2 or n3 < n1:
#     print(n3)
# elif n2 < n1 or n2 < n3:
#     print(n2)

# 7 задание:

# n1 = int(input('Введите число 1: '))
# n2 = int(input('Введите число 2: '))
# n3 = int(input('Введите число 3: '))
# if n1 == n2 and n2 == n1 and n3 == n1 and n3 == n2:
#     print('Все 3 числа совпадают')
# elif n1 == n2 or n2 == n1:
#     print('2 числа совпадают')
# elif n3 == n1 or n3 == n2:
#     print('2 числа совпадают')
# else:
#     print('0 Совпадений')

# 8 задание 

# 8.Вводятся два целых числа. Проверить делится ли первое на второе. 
# Вывести на экран сообщение следующее: частное (вывоить в любом случае), 
# а также остаток от деления (если он есть)


# 9.Дано номер года. Требуется определить, является ли год с данным номером 
# високосным. Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# a = int(input('Введите номер года: '))

# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('YES')
# else:
#     print('NO')


# 10.Перевести число, введенное пользователем, в байты или килобайты в зависимости от его 
# выбора

# num = int(input('Введите число: '))
# value = input('Перевести в байты/килобайты: ')
# byte = num / 1024
# kb = num * 1024

# if 'байты' in value:
#     print(byte)
# elif 'килобайты' in value:
#     print(kb)

# **************************************