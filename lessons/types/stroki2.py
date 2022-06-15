# print(dir(str))

# replace(old, new value, [count]) -> меняет в строке значение old на new value, если вы укажете count,
# то он заменит count раз.

#  text = 'ha ha ha ha'
#  result = text.replace('a', 'i', 2)
#  print(result)
#  print(type('ha'))

# strip() -> Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip
# text = '   Hello world  '
# result = text.strip()
# print(text)
# print(result)

# startswith(string, [start], [end]) -> Возвращает True если строка начинается с string,
# в противном случае указывается возвращается False.
# endswith(string)
# text = 'Hello world'
# print(text.startswith('W'))
# print(text.startswith('H'))
# print(text.startswith('Hello'))
# print(text.startswith('d', -1))

# ---------------------------------

# a = 'a'
# print('a' is a) # 'a' == a

# ---------------------------------

# isalpha() -> проверяет состоит ли наша строка из символов
# isdigit() -> проверяет состоит ли наша строка из чисел, выводит True. в против. случае False
# isalnum() -> проверяет состоит ли наша строка полностью из чисел

# index(value, [start], [end]) -> выводит индекс значения value в нашей строке
# rindex(value, [start], [end]) - с конца

# text = 'Hello world! This is John!'
# result = text.index('r', 4)
# print(result)

# find(value, [start], [end]) -> выводит индекс значения value в нашей строке. Разница с методом
# index в том, что, если value не найдено возвращается значение -1
# rfind 

# text = 'Hello world! This is John!'
# result = text.find('l', 4)
# print(result)

# split(разделитель) -> дробит строку по разделителю которая находится в строке. Разделяет
# строку и возвращает тип данных list.

# # разделитель.join(Iterable) -> соединяет строки, которые находятся в iterable по разделителю.
# text = 'Milk,Bread,Water'
# splited_text = text.split(',') # -> ['Milk', 'Bread', 'Water']
# print(splited_text)
# joinded_text = ','.join(splited_text) # -> 'Milk, Bread, Water'
# print(joinded_text)


# text = 'Hello world this is John Snow'
# result = text.split(' ')
# print(result)
# print(type(result))

# count(string) -> считает количество вхождений string в нашу строку,
# text = 'Hello world! I\'m from Earth!'
# a = text.count('l')
# print(a)

# swapcase() -> возвращает строку, в которой каждая буква будет иметь противоположный регистр
# upper, lower
# text = 'Hello world! S VAMI john'
# result = text.swapcase()
# upper_txt = text.upper()
# print(result)
# print(upper_txt)



