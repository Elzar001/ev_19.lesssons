# Task

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 
# 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядки батареи

# class Phone:
#     def __init__(self, imei, os):
#         self._imei = imei
#         self._oc_info = os
#         self.__battery_level = 100

#     def get_info(self):
#         if self.__battery_level <= 0: raise Exception('Телефон разряжен')

#         if self.__battery_level - 0.5 < 0:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')

#         self.__battery_level -= 0.5
#         print(f'OS: {self._oc_info}\nIMEI: {self._imei}')

#     @property
#     def battery_level(self):
#         if self.__battery_level <= 0: raise Exception('Телефон разряжен')
#         if self.__battery_level - 0.5 < 0:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
        
#         self.__battery_level -= 0.5
#         print(f'Уровень заряда: {self.__battery_level}')

#     @battery_level.setter
#     def battery_level(self, charge_level):
#         if self.__battery_level < charge_level and charge_level <= 100:
#             self.__battery_level = charge_level
#             print(f'Телефон заряжен. Заряд батареи: {charge_level}')
#         else:
#             raise Exception('Вы не можете разряжать уровень батареи!')

    
#     def play_music(self):
#         if self.__battery_level <= 0: raise Exception('Телефон разряжен')
#         if self.__battery_level - 5 < 0:
#             self.__battery_level = 0
#             raise Exception('Телефон разряжен')
        
#         self.__battery_level -= 5
#         print('Слушаем музыку')

#     def play_video(self):
#         if self.__battery_level <= 0: raise Exception('Телефон разряжен')
#         if self.__battery_level <= 10: raise Exception('Недостаточно заряда для просмотра видео')

#         self.__battery_level -= 7
#         print('Смотрим видео')

# apple = Phone('123546789', 'iOS')
# apple.play_video()
# apple.play_music()
# apple.get_info()
# for x in range(1, 10):
#     apple.play_music()

# apple.battery_level

# for x in range(1, 8):
#     apple.play_music()

# apple.battery_level
# apple.battery_level = 90
# apple.battery_level


#--------------------------------------------------------------------------------------
# Class methods, instance methods, static methods

# Методы экземпляра класса(Instance methods) - Это те методы в ООП, которые могут изменять состояние экземпляра класса: def method(self)

# Методы класса(Class methods) - Это те методы, которые могут изменять состояние самого класса: def method(cls)
#@classmethod - это декоратор, который обозночает что метод является методом класса
#def method(cls) - cls - это ссылка на сам класс

# Статические методы(Static methods) - это те методы, которые не могут изменять состояние как экземпляра класса так и самого класса: #(Не принимает в себя ни cls, ни self)
# @staticmethod - это декоратор который обозначает статический метод
# def method():

# class Person:
#     surname = 'Snow'
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birt_date(cls, name, year):
#         print(cls, '!!!!!!!!!!')
#         from datetime import date
#         cls.surname = 'Lanister'
#         age = date.today().year - year      
#         return cls(name, age)

#     @staticmethod
#     def isAdult(age):
#         if age >= 18:
#             print('Человек совершеннолетний')
#         else:
#             print('Человек несовершеннолетний')

# john = Person('John', 24)
# print(john.name)
# print(john.surname)
# Person.isAdult(john.age)
# john.isAdult(17)

# jamie = Person.from_birt_date('Jamie', 1988)
# print(jamie.name)
# print(jamie.surname)
# print(jamie.age)
# Person.isAdult(jamie.age)

# sansa = Person('Sansa', 19)
# print(sansa.name)
# print(sansa.surname)


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     @classmethod
#     def from_string(cls, stroka):
#         day, month, year = map(int, stroka.split('.'))
#         return cls(day, month, year)


#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'

# date = Date(15, 4, 2022)
# print(date.string_to_db())

# string_date = '15.04.2022'
# day, month, year = map(int, string_date.split('.'))

# date1 = Date(day, month, year)
# print(date1.string_to_db())

# date2 = Date.from_string('09.05.2021')
# print(date2.string_to_db())

# ------------------------------------------------------------------------------------------------

# SOLID - D