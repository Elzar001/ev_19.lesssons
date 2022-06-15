# Множества в python - "контейнер", который содержит в себе уникальные
# элементы в случайном порядке.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# литералы множества {}
# a = {1: 'a', 2: 'b'} -> словари
# a = {1,2,3,4, 'a'} -> множества

# a = set()
# print(type(a))
# print(a)

# a = set() -> set
# a = {} -> dict
# print(type(a))

# a = set('Hello')
# print(a)

# ls = [1,2,3,4,5,5,6,6,7,7,8,2,5,5,4,4,8,7,7,7,8,8,9,9,9,9]
# a = set(ls)
# ls = list(a)
# print(a)

# FIFO - first in first out
# a = {True, False,3,2,3,4,5,4,4,4,4,4,4,4,4,6,54,3,223,4,213}
# print(a)

# print(dir(set))

# Методы множеств:
# pop()

# a = {1,2,3,4,5}
# a.pop()
# print(a)

# LIFO -> last in first out
#--------------------------------

# months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May'])

# for x in months:
#     print(x)

# Метод add

# set_ = {1,2,3,4,5}
# set_.add('Hello')
# print(set_)


# remove/discard 

# remove -> KeyError 
# discard -> None

# set_ = {1,2,3,4,5,6,7}
# print('Before: ', set_)
# set_.discard(3)
# set_.discard(5)
# set_.discard(7)
# set_.discard(11)
# # set_.remove(5)
# # set_.remove(11)
# print('After: ', set_)

# Метод intersection - пересечение множеств

# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {11,22,33,5,6,7,12,13}
# z = set1.intersection(set2)
# print(z)
# print(set1 & set2) # = z

# Метод difference -> Разность множеств

# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {11,22,33,5,6,7,12,13}
# z = set1.difference(set2)
# print(z)
# print(set1 - set2) # = z


# Метод issubset - Подмножество

# set1 = {1,2,3,4,5,6,7}
# set2 = {5,6,7}
# # if set2.issubset(set1):
# #     print('Подмножество!')
# if set2 <= set1: # Операнд подмножества <= 
#     print('Подмножество!')

# Метод issuperset -> Надмножество

# set1 = {1,2,3,4,5,6,7}
# set2 = {5,6,7}
# # if set1.issuperset(set2):
# #     print('Надмножество!')
# print(set1 >= set2) # Операнд надмножества >=


# Метод symmetric_difference -> выдает общую разницу из двух множеств 

# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {11,22,33,5,6,7,12,13}
# z = set1.symmetric_difference(set2)
# print(z)
# print(set1 ^ set2) # = z

# Метод union -> Соединение

# set1 = {1,2,3}
# set2 = {4,5,6}
# z = set1 | set2
# print(set1.union(set2))
# print(set1 | set2) # = 112 строка, операнд соединения "|"

# print('Before: ', set1)
# print(set1.update(set2)) # Операнд update |= set 1 |= set2
# print('After: ', set1)

# ---------------------------------------------

# Frozenset -> неизменяемый тип данных

# a = set('qwerty')
# b = frozenset('qwerty')
# print(a == b)
# print(type(a))
# print(type(b))
# print(a)
# print(b)
# a.add(1)
# b.add(1)





