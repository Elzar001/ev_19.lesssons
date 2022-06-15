# String - Строки

# Строки в Python - набор последовательных символов, которые мы используем
# для хранения и представления текстовой информации.

# name = 'John'
# name1 = "John"
# name2 = """
# John
# Snow
# """
# name3 = str("John Snow")
# print(name)
# print(name1)
# print(name2)
# print(name3)
# print(type(name))
# print(type(name1))
# print(type(name2))
# print(type(name3))

# a = 5
# print(id(a))
# b = 5
# print(id(b))

# a = 'Hello '
# b = 'Hello '
# print (id(a), id(b))

# Экранирование - при помощи экранирования можно вставлять символы, которые сложно
# ввести с клавиатуры.

# \n -> перенос строки
# \f -> перевод страницы
# \r -> возврат указателя
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция

# name = 'John\nSnow'
# print(name)
# lastName = input('Введите свою фамилию:')
# print(lastName)
# print(Im John \\nSnow)

# name = 'Rachel '
# print(name * 3)

#************************************************
# Индексация сиволов в строке
# name = 'John'
#         # J = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])


# a = 'birthday'
# print(len(a))
# функция len - длина строки (кол-во символов)

# *******
# Конкатенация строк
# hello = 'hello'
# world = 'world'
# result = hello + ' ' + world
# print(result)
# print(result.count('l',3, 5))
            # symbol "3 - старт (с какого символа начинать)", "5 - стоп (где закончить)"

# ************(
# Форматирование строк
# 1. С помощью %
# 2. С использованием метода .format()
# 3. Интерполяция строк) (f-строки)

# %
# name = input('Enter your name:')
# last_name = input('last name:')
# print('Hello, %s %s' % (name, last_name))

# # с помощью .format
# name = input('Enter your name:')
# last_name = input('Enter your last name:')
# print('Hello, {} {} '.format(name, last_name))
# print(f'hello,{name}, {last_name}')
# f-строки
# name = input('Enter your name:')
# last_name = input('Enter your last name')
# print(f'Hello,{name} {last_name}')


# Срезы по индексам
# [start:end:step]
# text = 'Hello world! My name is John'
# print(text[0:5])
# print(text[:-1])
# print(text[::-1])
# print(text[3::2])

# text = 'hello'
# text2 = 'world'
# result = 'hello' + ' ' 'world'
# print(result)

# text = "The quick brown fox jumps over the lazy dog"
# rep = text.upper("The quick brown fox jumps over the lazy dog")
# print(rep)

# name = input('Введите свое имя:')
# lastname = input('Введите свою фамилию')
# age = input('Введите свой возраст')
# print(f'Здравствуйте, Ваше имя:{name}, Ваша фамилия:{lastname}, Ваш возраст:{age}')

# txt =  'Makers bootcamp' 
# print(txt[1::2])

# txt = 'abracadabra'
# txt1 = txt.replace( [5], 'K')
# print(txt1)