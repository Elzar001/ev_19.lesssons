'''
1. Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water. Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
'''

# class Auto:
#   def ride(self):
#     print('Riding on a ground')

# class Boat:
#   def swim(self):
#     print('floating on water')

# class Amphibian(Auto, Boat):
#   pass

# obj = Amphibian()
# obj.ride()
# obj.swim()

'''
2. Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина
'''

# class RadioMixin:
#   def __init__(self, name_of_song):
#     self.name_of_song = name_of_song

#   def play_music(self):
#     print(f'Music {self.name_of_song} is on')
    

# class Auto(RadioMixin):
#   def ride(self):
#     print('Riding on a ground')

# class Boat(RadioMixin):
#   def swim(self):
#     print('floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#   pass

# obj = Amphibian('Kosandra')
# obj.ride()
# obj.swim()
# obj.play_music()

'''
3. Будильник. Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника. Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к нему метод для установки будильника, при вызове которого должен включатся будильник.
'''

# class Clock:
#     def __init__(self, time_):
#         self.time_ = time_

#     def time(self):
#         print(f'Now is {self.time_}')

# class Alarm:
#     def alarm_on(self):
#         print('Alarm is on')

#     def alarm_off(self):
#         print('Alarm is off')

# class AlarmClock(Alarm, Clock):
#     def set_alarm(self):
#         pass

# obj = AlarmClock('21:16')
# obj.alarm_on()

'''
4. Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы.
'''

class Coder:
    count_code_time = 0
    def __init__(self, experience):
        self.experience = experience

    def get_info(self):
        
        