# try:
#     a: str = input("")
#     print(a / 0)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except TypeError:
#     print('Типы разные')
# except Exception as e:
#     print(e)


# print('test')

#----------------------------------------------

# str_ = "test"
# try:
#     print(str_[55])
# except IndexError:
#     print('Нету такого индекса')

# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Enter: '))
#     print(list_[index])
# except IndexError:
#     print('Нету такого индекса')
# except Exception as e:
#     print(e)
#     print('Мы поймали какую-то ошибку')

# while True:
#     try:
#         x = int(input('Введите число: '))
#         break
#     except:
#         print("что-то пошло не так!!!!")

# try:
#     n1 = int(input('Enter: '))
#     n2 = int(input('Enter: '))
#     res = n1 / n2
#     print(res)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели неправильные данные!')
#     print('или на ноль делить нельзя')


# dict_ = {'a' : 5, 'b' : 10, 'c' : 15, 'd' : 20}
# try:
#     n1 = input('Enter: ')
#     res = dict_[n1]
#     print(res)
# except KeyError:
#     print('Такого ключа нет')
# else:
#     res *= 2
#     print(res)

# try:
#     a = int(input('Enter: '))
#     res = 5 + a
#     print(res)
# except Exception as e:
#     print(f'Возникла ошибка {e}')
# finally:
#     res = 4
#     print(res)

# n = int(input('Enter: '))
# if n <= 0:
#     raise ValueError('Значение не может быть равным или меньше нуля')
# print(n)

# try:
#     num = int(input('enter: '))
# except TypeError:
#     num = 45
# finally:
#     print(num)
#     print('all ok!!')

# x = 'hello'
# if not type(x) is int:
#     raise TypeError('Только цифры')

# info_user = dict()

# email = input('enter your email: ')
# if not email.endswith('@gmail.com'):
#     raise ValueError('email должен окончаться на @gmail.com')
# print(email)

# password = input('enter password: ')
# password_confirm = input('enter passwrod again: ')
# if len(password) <= 8 and len(password_confirm) <= 8:
#     raise ValueError('Пароль должен быть не менее 8 символов!')
# if password != password_confirm:
#     raise ValueError('Пароли не совпадают')
    
# info_user["email"] = email
# info_user['password'] = password
# print(info_user)

# 5. Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, 
# возникающую в том случае, если такого ключа нет. 
# inp = input('Введите ключ: ')
# dict_ = {'a' : 1, 'b' : 2, 'c' : 3}

# try:
#     a = {inp:[value for key, value in dict_.items()]}
#     print(a)
# except KeyError:
#     print('Такого ключа нет!')

# --------------------------------------------

# try: except

# try:
#     <expression>
# except <Exception>:
#     <body>
# else: # Если все ок
#     <body>
# finally: # В любом случае
#     <body>
# print(dir(__builtins__))

# try:
#     1 / 0
# except ZeroDivisionError as error_:
#     print('На 0 делить нельзя!', error_)
# except:
#     print('Поймал другое исключение')


# my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
# ls = [1,2,3,4,5]
# try:
#     key = input('Введите ключ: ')
#     index = int(input('Введите индекс: '))
#     print(my_dict[key])
#     print(ls[index])
# except IndexError:
#     print('Такого индекса не существует!')
# except KeyError:
#     print('Этот ключ не найден!')
# except:
#     print('Что то пошло не так!')
# finally:
#     print('Our program still alive')


# a = 5
# def func(): 
#     if a < 10: # UnboundLocalError
#         a = 'stroka'
# a = b # Name error
# func()

