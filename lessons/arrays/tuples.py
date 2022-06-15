# tuple() -> Кортеж, неизменяемый тип данных
# Занимает меньше памяти, можно использовать вместо списков

# a = [1,2,3,4,5,6]
# b = (1,2,3,4,5,6)

# print('List: ', a.__sizeof__())
# print('Tuple: ', b.__sizeof__())

#WARNING!!!
# tuple_ = ('string', 'abs')
# print(tuple_)
# print(type(tuple_))

# tuple_ = tuple('Hello world')
# print(tuple_)
# print(type(tuple_))

# a = 1
# b = 2
# c = 3
# res = a, b, c
# print('Res: ', res)
# new1, new2, new3 = res
# print(new1)
# print(new2)
# print(new3)


# Неизменяемый
# tuple1 = (1,2,3,4,5)
# del tuple1[0]

# tuple1 = tuple(range(1, 100))
# print(tuple1)

# print(dir(tuple))

# index(element, [start], [end])
# tuple1 = (1,2,3)
# res = tuple1.index(3)
# print(res)

# count(element)
# tuple1 = (1,2,3,2,2,)
# print(tuple1.count(3))

# +, *
# a = (1, 2, 3)
# b = (4, 5, 6)
# print(a + b)
# print(a * 3)
# print(b * 3)


