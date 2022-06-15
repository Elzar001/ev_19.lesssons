# Инкапсуляция:
# 1. Связь данных с методами которые этими данными управляют
# 2. Набор инструментов для управления доступом или методами которые управляют этими данными

# Инкапсуляция как связь

# class Phone:
#     number = '+996 777 777 777'

#     def print_number(self):
#         print(f'Мой номер {self.number}')


# Инкапсуляция как управление доступом
# 3 уровня доступа в питоне
#   1. Публичный (public) - number
#   2. Защищенный (_protected, parent/ child) - _number
#   3. Приватный (__private, частный, только в текущем классе) - __number 

# class Car:
#     def __init__(self):
#         self.marka = 'Honda' #Puclic
#         self._model = 'FIT' #Protected
#         self.__engine = 'ABC' #Private

# class Audi(Car):
#     pass

# car1 = Audi()
# print(car1.marka)
# print(car1._model)
# print(car1.__engine)
# car = Car()
# print(car.marka)
# print(car._model)
# print(car.__engine)

# car.marka = 'BMW'
# print(car.marka)
# car._model = 'Accord'
# print(car._model)
# car.__engine = 'ACB'
# print(car.__engine)


# class Phone:
#     username = 'John'
#     _caller = 'Stark'
#     __count_of_rings = 15

#     def call(self):
#         print(f'Тебе звонит {self._caller}')

#     def __turn_on(self):
#         self.__count_of_rings += 1
#         print('Аллооо Whatsup bro')

# phone = Phone()
# print(phone.username)
# phone.call()
# print(phone._caller)
# phone._Phone__turn_on()
# # print(phone.__count_of_rings)
# print(phone._Phone__count_of_rings)

#-------------------------------------------------------------------------

# getter & setter
# Они используются для получения и установки значения, чтобы добавить логику проверки при получении данных. Еще чтобы избежать прямого доступа к защищенному полю класса.

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 0

#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}')


# john = Person('John')
# # print(john.name)
# # print(john.age)
# john.age = 'Gulchatai'
# john.age = -18
# print(john.name)
# print(john.age)

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0

#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.__age}')

#     def set_age(self, age): #setter
#         if 0 < age < 140: self.__age = age
#         else: print('Недопустимый возраст!')

#     def get_age(self): return self.__age # getter

# tom = Person('Tom')
# tom.display_info()
# tom.set_age(-18)
# tom.set_age(25)
# print(tom.get_age())
# tom.display_info()

#-------------------------------------------------------------------------------------------------
# Аннотации свойств
# @property

# class Person:
#     __name = 'John'
#     __age = 22

#     @property
#     def name(self):
#         print(self.__name)
    
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, age):
#         if 0 < age < 150:
#             self.__age = age
#         else: print('Недопустимый возраст!')

# obj = Person()
# obj.name #obj.get_name()
# obj.name = 'Tom' # obj,set_name('Tom')
# obj.name
# obj.age
# obj.age = 1000000
# obj.age = 25
# obj.age

# obj.get_name()
# obj.set_age(50)

#------------------------------------------------------------------------------------

# SOLID - I (Interface Segregation Principle)
# Принцип разделения интерфейса
# Интерфейс -> Абстрактный класс
# Пользователь -> Дочерний класс

# Не создавайте слишком большие абстракные классы, создавайте мелкозернистые абстракции.
# Не наследуйтесь от Абстрактных классов, которые не будут использованы в дочернем классе 





