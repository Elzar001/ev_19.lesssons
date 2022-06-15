# JSON (JavaScript Object Notation) - Единый формат для хранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть(Интернет).
#<filename>.json

# {
#     'id': 1,
#     'author': 'John'
#     'posts': [...]
# }  --- это JSON, наша задача перевести его в Python dictionary.

# !!!
# JS object = {}
# Py dict = {}
# JSON == {}


# Процессы Сериализации данных и Десериализации

# Сериализация - перевод Python Dict в JSON формат (либо сохранить в файле, либо просто как текстовые данные).
# dump - это запись данных в JSON файл
# dumps - это запись данных в JSON текстовом формате

# Десериализация - Перевод из JSON в Python Dict.
# load - из файла JSON данные и переводим в Dict 
# loads - из JSON в текстовом формате переводим данные в Dict  

#-----------------------------------------------------------------------------------------------
# '''Процесс десериализации'''
# import json
# from urllib.request import urlopen


# data = urlopen('https://randomuser.me/api/')
# print(type(data))
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))
# print(generate_to_dict['results'])
# print(generate_to_dict.keys())

# with open('downAPI.json', 'w') as file:
#     file.write(str(generate_to_dict))


# Процесс сериализации
# import json

# data = {
#     'name': 'john', 'last_name': 'Snow',
#     'status': True
# }

# with open('downAPI.json', 'w') as file:
#     json.dump(data, file)

# import json
# data = {
#     'name': 'john', 'last_name': 'Snow',
#     'status': True
# }

# string = json.dumps(data)
# print(string)
# print(type(string))
# py_dict = json.loads(string)
# print(py_dict)
# print(type(py_dict))

# from urllib.request import urlopen 
# import json 

# data = urlopen('https://randomuser.me/api/')
# py_dict = json.load(data)
# print(type(py_dict))

# with open('downAPI.json', 'a') as file:
#     json.dump(py_dict, file)


nums = [2, 2, 3, 3, 4]

for x in nums:
    if nums.count(x) == 1:
        print(x)
