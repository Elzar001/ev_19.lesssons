# Magic methods / dunder methods(магические методы / Служебные методы) - __init__

# res = 5 + 5 # __add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения

# __eq__(self, other) -> == # 7 == 6

# __ne__(self, other) -> != # 7 != 6

# __lt__(self, other) -> < # 7 < 6
 
# __gt__(self, other) -> > # 7>6

# __le__(self, other) -> <=

# __ge__(self, other) -> >=


# class Word(str):
#     def __new__(cls, word):
#         word = word.split(' ')
#         word = ''.join(word)
#         return super().__new__(cls, word)

#     def __init__(self, word):
#         self.word = word

#     def __gt__(self, other):
#         print('gt сработал')
#         return len(self) > len(other)

#     def __lt__(self, other: str) -> bool:
#         print('lt сработал')
#         return len(self) < len(other)

#     def __eq__(self, other: object) -> bool:
#         return len(self) == len(other)


# obj = Word(' Hello  Wo  r ld')
# obj1 = Word('helloworld')
# print(obj == obj1)

# word1 = Word('John')
# word2 = Word('Tom1')
# result = word1 > word2
# print(result)
# print(word1 < word2) # < -> __lt__ 
# print(word1 == word2)

# print(ord('J')) # ASCII CODE
# print(ord('T'))

# -------------------------------------------------------------------------------------------------

# Конструктор -> __new__
# Инициализатор -> __init__
# Деструктор -> __del__
# del a

# class Conventer(float):
#     def __new__(cls, number):
#         return super().__new__(cls, number ** 2)

#     def __init__(self, number):
#         self.number = number

# obj = Conventer(5.0)
# print(obj.number)
# print(obj + 5)


# class Human:
#     def __new__(cls, stroka):
#         return 'stroka ' + stroka
    
#     def __init__(self, stroka):
#         self.stroka = stroka

# obj = Human('Hello world')
# obj1 = Human('Omega')
# print(obj)
# print(obj1)

#---------------------------------------------------------------------------------------------
# Эти методы нужны для отображения объекта

# __str__ -> Для отображения для пользователей
# __repr__ -> Для отображения для программистов

# class Base:
#     def __init__(self, string):
#         self.string = string

#     def __repr__(self):
#         return f'Класс: {self.__class__.__name__}\nОбъект: {self.string}'

#     def __str__(self):
#         return f'Объект: {self.string}'

# obj = Base('Hello John')
# print(obj)
# print(repr(obj))

# __getitem__ [1,2,3,4,5]
# __setitem__
# __delitem__


# + - * /

# class Cifra(int):
#     def __new__(cls, number):
#         print('Вызов new')
#         instance = super().__new__(cls)
#         if not 0 < number < 100:
#             raise ValueError('Введите число от 0 до 100!')

#         else:
#             return instance

#     def __init__(self, number):
#         self.number = number

#     def __add__(self, other):
#         print('__add__ вызван!')
#         print(f'Результат: {self.number + other.number}')
#         return f'Результат: {self.number + other.number}'


# value1 = Cifra(95)
# value2 = Cifra(15)
# value1 + value2 

# __sub__ -> -
# __mul__ -> *
# __floordiv__ -> //
# __div__ -> /
# __mod__ -> %


'''
4. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
'''

# class Student:
#     def __init__(self, bally):
#         self.bally = bally
#         self.avg_res = (bally['math'] + bally['history'] + bally['literature']) / 3

#     def __gt__(self, other):
#         print(f'gt сработал {self.avg_res}, {other.avg_res}')
#         return self.avg_res > other.avg_res

# john = Student({'math': 100, 'history': 80, 'literature': 76})
# jamie = Student({'math': 90, 'history': 90, 'literature': 95})
# print(jamie > john)
# print(john > jamie)


'''
3. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
'''

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls
# # ls[0]
#     def __getitem__(self, index):
#         print(self.ls[index - 1])


# x = MyList([1,2,3,4,5])
# x[1]
