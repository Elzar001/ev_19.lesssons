"""
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

class Salary:
    tax = 15 # 0.15

    def __init__(self, sum, work):
        self.salary_sum = sum
        self.work_time = work

    def total_tax(self):
        res = ((self.salary_sum * self.tax) / 100) * self.work_time
        print(res)

salary = Salary(50000, 10)
print('Сумма налога за весь стаж работы:')
salary.total_tax()
print(f'Зарплата и стаж работы: {salary.salary_sum}, {salary.work_time}')


"""
1. Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. 
Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например:
"Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""

     
# class Song:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author 
#         self.year = year

#     def show_author(self):
#         print(f'Автор этой песни: {self.author}')

#     def show_title(self):
#         print(f'Название этой песни: {self.name}')
    
#     def show_year(self):
#         print(f'Год выпуска этой песни: {self.year}')

# song = Song('Sunshine', 'Miyagi', 2017)
# song.show_author()
# song.show_title()
# song.show_year()

"""
2. Создайте класс  Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. 
Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и рассчитайте площадь фигуры.
"""


# class Circle:
#     color = 'blue'
#     pi_number = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         S = self.pi_number * (self.radius ** 2)
#         print(f'Площадь круга равна {S}')

# circle = Circle(5)
# circle.area()
# circle.color = 'Black'
# print(f'Цвет круга - {circle.color}')


"""
3. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""

# class BankAccount:
#     balance = 0

#     def __init__(self):
#         pass

#     def deposit(self, amount):
#         self.balance = amount + self.balance

#     def withdraw(self, amount):
#         self.balance = self.balance - amount  

# account = BankAccount()
# account.deposit(55000)
# account.withdraw(15800)
# print(account.balance)



"""
4. Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""

# class Taxi:
#     def __init__(self, company, fare, one_km_cost, distance):
#         self.company = company
#         self.fare = fare
#         self.one_km_cost = one_km_cost
#         self.distance = distance

#     def total_fare(self):
#         total = self.fare + (self.one_km_cost * self.distance)
#         print(f'Стоимость поездки на {self.company} такси на 15км составил = {total}')

# yandex = Taxi('Yandex', 50, 5, 15)
# jorgo = Taxi('Jorgo', 45, 4, 15)
# namba = Taxi('Namba', 54, 6, 15)

# yandex.total_fare()
# jorgo.total_fare()
# namba.total_fare()

"""
5. Создайте класс телефонной книги. У контактов должны быть имена и фамилии и телефонные номера. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888". Затем объявите экземляр класса и вызовите метод.
"""

# class Contacts:
#     def __init__(self, name, last_name, phone_number):
#         self.name = name
#         self.last_name = last_name
#         self.phone_number = phone_number

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, Телефон: {self.phone_number}')

# contact = Contacts('Иван', 'Петров', '+996555777888')
# contact.get_info()


"""
7. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())



который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
"""

# class Nobel:
#     def __init__(self, liter, year, name):
#         self.liter = liter
#         self.year = year
#         self.name = name

#     def get_year(self):
#         res = 2022 - self.year
#         print(f'выиграл {res} лет назад')

# winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
# winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ')

# print(winner1.liter, winner1.year, winner1.name)
# winner1.get_year()

# print(winner2.liter, winner2.year, winner2.name)
# winner2.get_year()

    

# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())



"""
8. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод __str__, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - **********
"""

# class Password:
#     symbols = ['@', '#', '&', '$', '%', '!', '~', '*']
#     def __init__(self, password):
#         self.password = password

#     def validate(self):
#         for password in self.password:
#             if password <= 8 and password >= 15:
#                 raise Exception('Password must be >8 and <15 symbols!')
#             elif password 
            
"""
9. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""
# from math import factorial

# class Math:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def get_factorial(self):
#         fac1 = factorial(self.num1)
#         fac2 = factorial(self.num2)
#         print(f'Факториал числа 1: {fac1} Факториал числа 2: {fac2}')

#     def get_sum(self):
#         sum_ = self.num1 + self.num2
#         print(f'Сумма чисел: {sum_}')

#     def get_mul_table(self):
#         n1 = f'{self.num1} * 1 = ', self.num1 * 1, f'{self.num1} * 2 =', self.num1 * 2
#         n2 = f'{self.num2} * 1 = ', self.num2 * 1, f'{self.num2} * 2 =', self.num2 * 2  # и так до  
#         print(n1)
#         print(n2)

# math = Math(5, 6)

# math.get_sum()
# math.get_factorial()
# math.get_mul_table()

        




