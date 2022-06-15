# while expression:
#     <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз')
#     i += 1 #i = i + 1
# print('Цикл закончился')

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Введите имя 1: ')
#     name2 = input('Введите имя 2: ')
#     i += 1
#     if i > 5:
#         print('Цикл остановлен')
#         break
# else:
#     print('Вы ввели правильное имя')

# admin = ['John', 'ilovepython']
# i = 3
# password = None

# while admin[1] != password:
#     password = input('John, введите пароль: ')
#     i -= 1
#     if i == 0:
#         print('Вы заблокированы!!! ')
#         break
# else:
#     print('John, вы вошли в систему.')


# ЦИКЛ for



# for <variable> in <iter object>:
#     <body>

#list, range, tuple, set... (iter)

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']

# for item in pizza:
#     print(f'Eating {item} of pizza')

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for item in pizza:
#     new_item = item.split('_')
#     # print(new_item)
#     spisok.append(new_item[0].capitalize())
# print(spisok)


# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# i = 0

# while i < len(pizza):
#     new_item = pizza[i].split('_') [0].capitalize()
#     spisok.append(new_item)
#     i += 1   
# print(spisok)

#Упрощенная версия кода: 

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# i = 0

# while i < len(pizza):
#     spisok.append(pizza[i].split('_') [0].capitalize())
#     i += 1   
# print(spisok)


# str_ = [1,2,3,4,5]
# i = str_.__iter__()
# print(i)
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())


# Задачи: 

# nums = [1,2,7,4,5]
# target = 9

# for x in nums:
#     n = target - x
#     if n in nums:
#         print(x,n)


# nums = [1,2,7,4,5]
# target = 11
# nums = [4,11,2,5,1,6]
# target = 8
# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num == nums[i]:
#             continue
#         k = nums.index(num)
#         print(f'Ответ: {i} {k}')
#         break



# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if x.startswith('four'):
#         continue # пропускает одну итерацию
#     else:
#         spisok.append(x)

# print(spisok)


# sea = None
# c = 0







