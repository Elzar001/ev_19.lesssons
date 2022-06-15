# dict() (изменяемый тип данных) -> Словари это упорядоченная(после Python 3.7)
# коллекция элементов.
# Каждый элемент в словаре хранится в виде пары - ключ:значение(key:value)

# Ключи должны быть уникальными и быть неизменяемым типом данных (str, int, tuple ...)
# Тогда как значениями могут выступать любой тип данных и они могут дублироваться

# thisdict = {
#     'brand' : 'Ford', 
#     'model' : 'Mustang',
#     'year' : 1964
# }
# print(thisdict)
# # print(thisdict['model'])


from email.policy import default
from unicodedata import name


user_info = {
    'first_name' : 'John',
    'last_name' : 'Snow',
    'age' : 28,
    'email' : 'johnsnow1@gmail.com',
    'role' : 'moderator',
    # [1,2,3]: 'list - ERROR!!!
    'number' : 67_9878_6666
}
# print(user_info)
# print(user_info['first_name'])
# print(user_info['number'])
# user_info['role'] = 'admin'
# print(user_info['role'])
# print(user_info.keys())
# for value in user_info.values():
#     print(value)
# for key, value in user_info.items():
#     print(f'Ключ: {key}, Значение: {value}')

# Метод clear() - очищает словарь

# Метод copy() - копирует

# dict_.get(key, [default == None]) == dict_[key]

# print(user_info.get('123', 'Такого ключа нет'))

# dict_.pop(key, [default]) - удаляет по ключу
# a = user_info.pop('last_name', 'Нет ключа')
# print(a)
# print(user_info)

# update([other]) - обновляет словар, добавляя пары ключ : значение из other
# a = {'hobby' : 'Ubivat\ belyh hodokov', 'Цвет волос' : 'Черный'}
# user_info.update(a)
# print(user_info)

# print(dir(dict))

# 1. Первый способ применения, добавление пары
# setdefault(key, [value == None]) -> работает так же как и get,
# но если нет такого ключа он создаст новую пару.
# dict_ = {'name' : 'Tirion', 'age' : 20}
# # res = dict_.setdefault('name')
# # print(res)

# # 2. Второй способ применения, добавление пары.
# dict_.setdefault('last_name', 'Lanister')
# print(dict_)

# Метод fromkeys 
# dict_.fromkeys(keys, [value]) 
# tuple_ = (1,2,3,4,5,6)
# thisdict = dict.fromkeys(tuple_, 'ev.19')
# print(thisdict)

# ******************
# Итерация - это термин, который объясняет возможность взятия каких - либо элементов 
# из какого - либо объекта
# ******************





