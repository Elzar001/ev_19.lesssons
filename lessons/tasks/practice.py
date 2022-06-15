# import random
# from unittest import result

# ls = ['Плов', 'Манты', 'Лагман', 'Куурдак', 'Дымдама']

# p = 0
# m = 0
# l = 0
# k = 0
# d = 0

# for x in range(0, 10000):
#     r = random.choice(ls)
#     if r.lower() == 'плов':
#         p = p + 1 # p += 1 (инкремент)
#     elif r.lower() == 'манты':
#         m += 1 
#     elif r.lower() == 'лагман':
#         l += 1
#     elif r.lower() == 'куурдак':
#         k += 1
#     elif r.lower() == 'дымдама':
#         d += 1

# # print(f'Плов: {p}, Манты: {m} Лагман {l}, Куурдак: {k}, Дымдама: {d}')

# dict_ = {'Плов' : p, 'Манты': m, 'Лагман': l, 'Куурдак': k, 'Дымдама': d}
# print(dict_)
# res = dict(sorted(dict_.items(), key=lambda x: x[1]))
# winner = res.popitem()

# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]}')




#-------------------------------------------------------------

# username = input('Enter username: ')
# pass1 = input('Enter password: ')
# pass2 = input('Enter password: ')

# if len(username) < 8:
#     raise Exception('Слишком короткий пароль (>8)')
# if pass1 != pass2:
#     raise Exception('Пароли не совпадают')
# if len(pass1) <7:
#     raise Exception('Слишком короткий пароль (большо 8 символов)')
# print(f'Вы успешно зарегистрировались! Добро пожаловать, {username}')

# db_username = []
# db_username.append(username) # - Добавляет username в базу данных



#************************
# 6) Напишите программу, которая будет находить наибольшую цифру натурального
# числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

# a = int(input("vvedite chislo:"))
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)

# num=int(input('Введите число: '))
# # 9678 -> 9678 -> 567 -> 56 -> 9 -> 0
# # 9
# maxdigit=num%10
# num=num//10
# while num > 0:
#     if num%10 > maxdigit:
#         maxdigit = num%10
#     num = num//10 
# else:
#   print('Наибольшая цифра: ', maxdigit)


# # """
# 3) Создайте список изпользуя циклы.
# """

# spisok = []
# i = 0

# while i < 10:
#     str_ = input('Введите символ: ')
#     spisok.append(str_)
#     i += 1
# else:
#     print(spisok)

# 7) Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого
# числа и записать в новый список.

# 1-й способ: math.factorial
# from math import factorial

# ls = [3,4,5,6,7,8]
# res = []
# for x in ls:
#     res.append(factorial(x))
# print(ls)
# print(res)

# 2-й способ: algoritm of factorial

# spisok = [3,4,5,6,7,8]
# res = []
# for x in spisok:
#     fac = 1
#     i = 1
#     while i <= x:
#         fac = fac * i
#         i += 1
#     else:
#         res.append(fac)

# print('Числа: ', spisok)
# print('Факториалы: ', res)

# 5. Дан список, с числами. Посчитайте количество чётных и нечётных чисел в этом списке.

# ls = list(range(1,24))
# even_nums = list(filter(lambda x: x%2 == 0, ls))
# print(f"Четных чисел: {len(even_nums)}, Нечетных чисел {len(ls) - len(even_nums)}")


# 7. Даны списки из чисел. Проверьте,есть ли в нем отрицательные числа.

# ls = [1,2,3,5,46,4,96,8,5,5,6,1,7]
# # print(bool([]))
# result = list(filter(lambda x: x < 0, ls))

# if result:
#     print(f'Да, есть: {len(result)}')
# else:
#     print('Отрицательные числа отсутствуют')


# 2.Даны три числа x, y, z представляющие плоскости куба, также дано число n. Напишите функцию
# выдающую все возможные комбинации координат данных трех чисел, при условии что сумма 
# x + y + z не должна равняться числу ограничению n. Для решения использовать list 
# comprehensions. 
# Например: x, y, z = 1, 1, 2 
#                 n = 4 
# правильный вывод: [[2, 1, 2], [1, 2, 2], [2, 2, 1]]


# x, y, z = 1, 2, 2
# n = 4
# def cubecoords(x,y,z,n):
#     from itertools import permutations
#     ls = [x,y,z]
#     res = [i if sum(i) != n else None for i in list(permutations(ls, 3))]
#     return res

# print(cubecoords(x,y,z,n))

# strs = ["flower","flow","flight"]
# def longestCommonPrefix(strs: list) -> str:
#     short_str = min(strs, key = len)
#     for i, x in enumerate(short_str):
#         for other_str in strs:
#             # print(x)
#             if other_str[i] != x:
#                 return short_str[:i]
#     return short_str

# print(longestCommonPrefix(strs))


#--------------------------------------------------------

def validate_email(email):
    domains = ['gmail.com', 'mail.ru', 'yandex.ru']
    index = email.find('@')
    if '@' not in email:
        raise Exception ('Invalid Email!')
    elif not email[:index]:
        raise Exception ('Incorrect Email!')
    elif email[index+1:] not in domains:
        raise Exception (f'Invalid Email domain ({domains})!')
    print('Your email is valid and succesfully saved!')
    return True

def register(email, password, password2):
    db_email = None
    db_password = None
    if validate_email(email):
        db_email = email
    if password != password2:
        raise Exception ('Password don\'t match')
    db_password = password
    msg = 'You have succesfully registered, Welcome!'
    return {'email': db_email, 'password': db_password[::-1], 'msg': msg}


email = input('Enter email: ')    
pasw1 = input('Enter password: ')
pasw2 = input('Enter password: ')
    
print(register(email, pasw1, pasw2))










