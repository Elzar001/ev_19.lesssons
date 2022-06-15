"""
1. Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.
"""

# class Class1:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def sum_of_nums(self):
#         res = self.num1 + self.num2
#         print(f'Сумма первого и второго числа = {res}')

#     def mult(self):
#         res = self.num1 * self.num2
#         return res

# class Class2(Class1):
#     def __init__(self, num1, num2, num3):
#         super().__init__(num1, num2)
#         self.num3 = num3
    
#     def square(self):
#         print(f'Квадрат 3го числа: {self.num3 ** 2}')

#     def div(self):
#         print(f'Результат деления числа 1 на число 3: {self.num1 / self.num3}')

# cl = Class1(5,7)
# cl2 = Class2(5,6,3)

# cl.sum_of_nums()
# cl2.square()
# cl2.div()

"""
2. Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.
"""

class A:
    def method1(self):
        print('Основной функционал')

class B(A):
    def method1(self):
        print('Дополнительный функционал')

cl1 = A()
cl2 = B()

cl1.method1()
cl2.method1()