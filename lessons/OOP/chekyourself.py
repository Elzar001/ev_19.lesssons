'''
1. Будильник. Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника. Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к нему метод для установки будильника, при вызове которого должен включатся будильник.
'''

class Clock:
  def time_now(self):
    print(f'Текущее время: 17:00')

class Alarm:
  def alarm_on(self):
    print('Alarm is on')

  def alarm_off(self):
    print('Alarm is off')

class AlarmClock(Clock, Alarm):
  def alarm_on(self):
    pass
  
  

clock = AlarmClock()
print(clock.alarm_on())

'''
2. Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина
'''

class RadioMixin:
  def __init__(self, song):
    self.song = song

  def play_music(self):
    print(f'Music {self.song} is on')

@RadioMixin
class Auto:
  pass

'''
3. Напишите класс Student, который описывает студента. У студента есть следующие атрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {math’: 100, ‘history’: 89, literature’: 88}. 
Сделайте так, чтобы сравнение студентов между собой производилось по средней оценке студента по предметам.
'''

class Student:
  ls = []
  def __init__(self, name, surname, subject, marks):
    self.name = name
    self.surname = surname
    self.subject = subject
    self.marks = marks

  def marks(self):
    res = ls.append(self.marks)

  def avg_mark(self):
    res = map(int, )

'''
4. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе __new__ напишите условие для удаления
пробелов и пустых строк в созданных словах.
'''


'''
5. Напишите класс учеников Makers, который будет содержать 4 атрибута: 

- атрибут экземпляра name (имя студента)
- атрибут класса students_count (количество учеников)
- атрибут экземпляра класса language (язык, которому обучается студент)
- атрибут экземпляра класса kpi (оценка студента)

Также класс должен содержать следующие методы:

- метод, который будет создавать нового ученика, и при этом увеличивать количество студентов на 1.
- метод который будет выводит имя и язык, выбранный учеником.
- а также метод, который будет устанавливать оценку ученику.
'''

#write your code here

'''
6. Напишите программу Python для создания нового файла JSON из существующего файла JSON. 
'''

#write your code here

'''
7. Напишите программу Python для преобразования данных в кодировке JSON в объекты Python.
'''

#write your code here