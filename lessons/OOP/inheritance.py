# Наследование (inheritance)

# Принципы ООП:
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция
# 5. Агрегация
# 6. Композиция

# Наследование - Позволяет принимать родительские методы, атрибуты и поведение

# Родительским классом
# Дочерний класс

#--------------------------------------------------------------------------------------


# class Employee:
#     bonus = 1.5

#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# emp1 = Employee('John', 'Snow', 2000)
# print(emp1.get_full_name())
# emp1.give_bonus()
# print(emp1.salary)

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_language):
#         Employee.__init__(self, name, last_name, salary)
#         self.prog_language = prog_language


# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if emps == None:          
#             self.emps = []
#         else:
#             self.emps = emps

#     def add_emps(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee is allready in!')
    
#     def show_emps(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus * 2

        

# dev1 = Developer('John', 'Snow', 1500, 'Python')
# print(dev1.get_full_name())
# dev1.give_bonus()
# print(dev1.salary)
# print(dev1.prog_language)

# dev2 = Developer('Stive', 'Wozniak', 5000, 'Java')
# dev3 = Developer('Lary', 'Page', 500, 'JS')

# manager1 = Manager('Jamie', 'Lanister', 3000, [dev1, dev2])
# manager1.show_emps()
# manager1.add_emps(dev3)
# print(f'Manager {manager1.get_full_name()} has {manager1.show_emps()} developers, his salary is {manager1.salary}')



#-----------------------------------------------------------------------------------------------

# class Post:

#     def __init__(self, user):
#         self.user = user
#         self.posts = []
#         self.id = 0

#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status' : 201, 'msg' : 'succesfully created'}

#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return post
#         return {'status' : 404, 'msg': 'Not found!'}

#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 post.update(kwargs)
#                 return {'status' : 200, 'msg' : 'Updated'}
#         return {'status' : 404, 'msg': 'Not found!'}

#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.pop(self.posts.index(post))
#                 return {'status' : 200, 'msg' : 'Removed'}
#         return {'status' : 404, 'msg': 'Not found!'}


# acc1 = Post('JohnSnow')
# acc1.create_post('Хорошие новости', 'Моя сестра Санса родила девочку!', 'https://Bla.jpg')
# acc1.create_post('На прогулку', 'Сегодня отличная погода, вышел погулять', 'https://foto.jpg')
# acc1.create_post('На чиле!', 'Еду отдыхать в Турцию', 'https://photo.jpg')

# print(acc1.posts)
# print(acc1.retrieve_post(1))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(2, title = 'Прогулка обновлена', body = 'Сегодня гулял в 9 утра', image = 'https://foto.jpg'))
# print(acc1.retrieve_post(2))
# print(acc1.delete_post(2))
# print(acc1.posts)

# -------------------------------------------------------------------------

from abc import ABC, abstractmethod

class ChessPiece(ABC): # Абстрактный класс
    name = 'Piece'
    def show_name(self):
        print(f"Hello, I'm {self.name}")

    @abstractmethod # Декоратор
    def move(self):
        pass

class Queen(ChessPiece):
    name = 'Queen'

    def move(self):
        print('Куда хочу')

class Pawn(ChessPiece):
    name = 'Pawn'

    def move(self):
        print('На одну клетку вперед')

q = Queen()
p = Pawn()

q.show_name()
q.move()
p.show_name()
p.move()





