# Работа с файлами


# Указатель

# open(< Путь до вашего файла >)

# абсолютный путь:
# file = open('/home/elzar/Desktop/ev.19/files/text.txt')

# относительный путь (Относительно нынешней директории):
# file = open('text.txt')(

# Режимы / методы для работы с файлами:
# 1. r/r+ (read) - если нет файла - ошибка
# 2. w/w+ (write) - если нет файла создает новый файл
# 3. a/a+ (append) - если нет файла создает новый файл
# 4. t (text)
# 5. b (двоичный код)
# 6. x



# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()
# # Обязательно закрывать файл после открытия <name_of_file>.close()

# file = open('text.txt', 'r')
# data = file.readlines()
# print(data)
# file.close()


# Контекстный менеджер - как только выходим из тела контекстного менеджера файл закрывается

# with open('text.txt') as file:
#     data = file.read()
#     print(data)


# with open('text.txt', 'w') as file:
#     file.write('Hello, file was opened with')

# write
# writelines


# ls = ['Hello world', 'My name is John', "I'am 35 years old!!"]

# with open('text.txt', 'w') as file:
#     file.writelines(line + '\n' for line in ls)

# with open('/home/elzar/Desktop/ev.19/Files/text.txt', 'a') as file:
#     file.write('New string')

# *************

# file.tell() - > Возвращает индекс где находится указатель
# file.seek(int) -> Перемещает указатель на указанный int 

# *************

# ----------------------------------------------------
# Работа с файлами(Картинками)

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re

def get_imei_code(image):
    list_of_imei = []  
    string1 = pytesseract.image_to_string(image)
    list_of_imei.append(re.findall(r'IME.\d.\s\d+', string1))
    with open('imeicode.txt', 'w') as file:
        for x in list_of_imei[0]:
            file.write(x)

get_imei_code('/home/elzar/Desktop/ev.19/Files/imei.jpg')










