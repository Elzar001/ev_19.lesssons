# Множественное наслодование - Это дочерний класс наследуется от двух или более классов

# MRO(Method Resolution Order / Порядок разрешения методов) - Поиск родительских классов. Был создан для решения проблемы ромба (С3)


# class Auto:
#     def play_music_at_station(self):
#         print('Music is on')

#     def ride(self):
#         print('We\'re riding on the ground')

# class Plane:
#     def fly(self):
#         print('We\'re flying')

#     def play_music_at_station(self):
#         print('Music is playing')

# class FutureAuto(Plane ,Auto): # (Auto, Plane) - по принципу локального старшинства
#     pass

# obj1 = FutureAuto()
# obj1.fly()
# obj1.ride()
# obj1.play_music_at_station()

#-------------------------------------------------------------------------------------------

# class Zero:
#     def say(self):
#         print('class Zero')

# class First:
#     # def say(self):
#     #     print('class First')
#     pass

# class Second(First, Zero):
#     # def say(self):
#     #     print('class Second')
#     pass

# class Third(Zero):
#     def say(self):
#         print('class Third')

# class Fourth(Second, Third):
#     def say(self):
#         super().say()
#         print('class Fourth')

# obj = Fourth()
# obj.say()

# print(Fourth.__mro__)


# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y, X):
#     pass

# class G(A, B): # Ошибка
#     pass


# class MyMRO(type):
#     def mro(cls):
#         return(cls, A, B, X, Y, object)

# class G(A, B, metaclass=MyMRO):
#     def say(self):
#         print('hello')

# obj = G()
# obj.say()

#*******************************************************************************

# Mixins(Миксины)

# class MusicPlayerMixin:
#     def play_music_on_station(self):
#         print('Music is on')

# class Machines:
#     def start_engine(self):
#         print('Engine started')

# class Auto(Machines, MusicPlayerMixin):
#     # def play_song_on_station(self):
#     #     print('Music is on')
#     pass

# class Plane(Machines):
#     pass

# class Boat(Machines):
#     pass

# class Smartclock(Machines, MusicPlayerMixin):
#     # def play_music_on_station(self):
#     #     print('Music is on')
#     pass

# obj = Auto()
# obj.play_music_on_station()

#---------------------------------------------------------------------------------------------------

# SOLID - O(Open closed principle) - Принцип открытости и закрытости
# Классы, функции должны быть открыты для расширения, но закрыты для изменения


# class FlyMixin:
#     def fly():
#         print('Мы можем летать со скоростью 500 км/ч')

# class Car(FlyMixin):
#     def ride():
#         print('Мы можем разогнаться до 250 км/ч')

# class SportCar(Car):
#     def ride():
#         print('Мы можем разогнаться до 500 км/час')


# Car.ride()
# Car.fly()





