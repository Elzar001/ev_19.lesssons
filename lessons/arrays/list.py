# list()(Массив, список) - изменяемый, последовательный тип данных, который из себя представляет
# коллекцию каких - либо объектов.

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# 1. -> list(iterable)
# my_list  = list('Hello world')
# print(my_list)
# print(type(my_list))

# 2. -> range() -> возвращает последовательность элементов (принимает только целочисл-е)
# my_list = list(range(0, 100, 2))
# print(my_list)
# print(type(my_list))

# 3. -> [] 
# my_list = []
# print(type(my_list))

# print(dir(list))

# Методы строк:

# append(element) - добавляет как отдельный элемент в конец списка
# extend(element) - расширяет, добавляет элементы в конец по отдельности
# list_ = [1,2,3]
# list_.append([4,5,6])
# list_.extend([7,8,9])
# print(list_)

# insert(index, element) - добавл.
# list_ = ['string', 1,2,3]
# list_.insert(-1, 1)
# print(list_)

# len
# list_ = [1,2,5,5,6,3,4,5]
# print(len(list_))

# remove(element) - удаляет элемент
# list_ = [1,2,3,4,5]
# list_.remove(5)
# print(list_)

# pop([index])
# list_ = [1,2,3,4,5,6,7]
# a = list_.pop()
# b = list_.pop(1)
# print(list_)
# print(a)
# print(b)

# clear() -> полностью очищает список.
# list_ = [1,2,3,4,5,6,7]
# list_.clear()
# print(list_)


# WARNING!!!
# a = [1,2,3,4,5]
# b = a
# print(a)
# print(b)
# b.pop()
# print(a)
# print(id(a))
# print(id(b))

# copy()
# a = [1,2,3,4,5]
# b = a.copy()
# print(a)
# print(b)
# a.pop()
# print(b)

# print(id(a))
# print(id(b))



# sort([reverse=True/False, key=]) - фильтрация / сортировка
# list1 = [1,2,3,5651,1,56,32,51,-1]
# list1.sort()
# print(list1)

# list1 = [1,2,3,5651,1,56,32,51,-1]
# list1.sort(reverse=True)
# print(list1)

# list1 = ['awerd', 'hello', 'John', 'qwerty']
# list1.sort(key=len)
# print(list1)


# deepcopy
# copy

# from copy import copy, deepcopy

# a = [1,2,3,4,5, [1,2]]
# b = copy(a)
# c = deepcopy(a)

# print('a: ', a)
# print('b: ', b)
# print('c: ', c)
# a[-1] [0] = 'A'
# print('a after changes: ', a)
# print('b copy function: ', b)
# print('c deepcopy function: ', c)


