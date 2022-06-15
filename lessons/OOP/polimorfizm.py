# len() - полиморфнная функция

# print(len('Makers'))
# print(len([1,2,3,4,5]))
# + - полиморфнный оператор

# print(5 + 5)
# print('Hello' + ' world')

# Полиморфизм - суть импользования заключается в использовании единственной сущности (метод, функции, операторы или же объекты) для представления различных типов в различных сценариях


# class Cat:
#     def init(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Я кошак. Меня зовут {self.name} и мне {self.age}')
    
#     def sound(self):
#         print('Мяу!')

# class Dog:
#     def init(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Я собака Меня зовут {self.name} и мне {self.age}')

#     def sound(self):
#         print('Гав!')

# cat = Cat('Murka', 10)
# dog = Dog('Mali', 20)

# for i in (cat, dog):
#     i.info()
#     i.sound()

# Асбртракция(АОстракци клас его можоно рассматривать как набор методов. которые должны быть созданы в любых дочерних классах, построенных на основе абстракного классех=

# Асбтрактный метод - это метод. которого есть объявление, но нет реализаций



# from abc import ABC, abstractmethod
# # from math import pi


# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass

# class Giraffe(Animal):
#     def eat(self):   
#         print('Я кушаю листву')

# class Pantera(Animal):
#     def eat(self):
#         print('я кушаю мясо')

# ob1 = Giraffe()
# ob2 = Pantera()
# ob1.eat()
# ob2.eat()


#==================================================
# from abc import ABC, abstractmethod
# from math import pi


# class Shape(ABC):
#     def init(self, name ) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass
    
#     def fact(self):
#         print('Я некая фигура в двумерной плоскости')
# class Square(Shape):
#     def init(self, len) -> None:
#         super().init('Квадрат')
#         self.len = len
#     def area(self):
#         print(self.len  2)
    
#     def fact(self):
#         print('У меня все углы равны 90 градусам')

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         print(pi * self.radius  2)

# a = Square(5)
# b = Circle(10)
# print(a.name)
# print(b.name)
# a.fact()
# a.area()
# b.fact()
# b.area()

# SOLID-принципы Дяди Боба расшифровываются следующим образом:

# S – Принцип единственной ответственности (Single Responsibility Principle),

# O – Принцип открытости/закрытости (Open‐Closed Principle),

# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

# I – Принцип разделения интерфейсов (Interface Segregation Principle),

# D – Принцип инверсии зависимостей (Dependency Inversion Principle).

# Цель принципа - это убедиться в том что подкласс может занять место своего родителя без ошибок


# Если код обнаруживает, что есть проверка на тип класса, то тогда ваш код нарушает принцип подстановки
