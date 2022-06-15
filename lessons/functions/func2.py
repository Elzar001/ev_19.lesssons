# def a(a: int,b: int,c: int, d: int) -> int: # Параметры
#     """Function returns sum of all parameters"""
#     return a+b+c+d

# # result = a(1,2,3,5) # Аргументы
# result = a
# print(result(10, 15, 12, 17))


# Позиционные и именованные аргументы:

# def test(a = None, b = None, c = None): # = None аргумент становится опциональным (необязательным)
#     print(a, 'is on "a"')
#     print(b, 'is on "b"') 
#     print(c, 'is on "c"')

# test(c = 3, b = 2) # Именованные аргументы (Keyword arguments)
# test(1,2,3) # Позиционные аргументы (arguments)

# test (1,2, c = 3)


# ls = ['123', '1233', '1', '12']
# ls.sort(key=len)
# print(ls)


# оператор * (оператор распоковки)
# a = [1,2,3]
# b = [*a, 4,5,6]
# c = [*a, *b]
# print(c)


# --------------------------------------------
# *args, **kwargs в функциях

# def printScores(student, *args):
#     print(f'Student name: {student}')
#     for score in args:
#         print(score)

# printScores('John', 100, 90, 95, 88, 100, 96)


# def printPetNames(owner, **pets):#**kwargs
#     print(f'Owner name: {owner}')
#     # for pet, name in pets.items():
#     #     print(f'{pet}: {name}')
#     print(pets)
#     print(type(pets))

# printPetNames('John', dog='Arstan', fish=['Nemo', 'Dori', 'Larry'], turtle = 'Leonardo')

# def get_some_data(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(kwargs['lang'])
#     print('Аргументы: ', args)
#     print('Именованные Аргументы: ', kwargs)

# get_some_data(1,2,3,4, lang = 'Python', name = 'John')
    


# def add(num1: float, num2: float) -> float:
#     """Функция возвращает сумму двух чисел"""
#     return num1 + num2

# def subtract(num1: float, num2: float) -> float: 
#     """Функия разности"""
#     return num1 - num2

# def divide(num1: float, num2: float) -> float:
#     """Функция деления""" 
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!!!')

# def multiply(num1: float, num2: float) -> float: 
#     """Функция произведения"""
#     return num1 * num2

# def main() -> None:
#     """Функция main"""
#     try:
#         num1 = float(input('\nВведите число 1: '))
#         num2 = float(input('Введите число 2: '))
#     except ValueError:
#         print('Вы ввели некорректные данные!!!')
#     operator = input('Введите операцию (+, -, *, /): ')
#     result = None

#     if operator == '+': result = add(num1, num2)
#     elif operator == '-': result = subtract(num1, num2)
#     elif operator == '*': result = multiply(num1,num2)
#     elif operator == '/': result = divide(num1,num2)
#     else:
#         print('Вы ввели некорректный оператор!!!')
#     print(result)
#     question = input('Хотите продолжить?(Yes/No): ')
#     if question.lower() == 'yes':
#         main()
#     else:
#         print('До свидания!')

# main()





