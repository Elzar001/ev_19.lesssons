# from bs4 import BeautifulSoup # as bs4

# import requests
# import datetime

# BASE_URL = 'https://cars.kg/offers'

# def get_html(url:str) -> str:
#     '''
#     Получает html код определенной страницы
#     '''
#     response = requests.get(url)
#     return response.text

# def get_data(html: str) -> None:
#     '''Функция парсер, получает все данные'''
#     soup = BeautifulSoup(html, 'lxml')
#     # print(soup)
#     catalog = soup.find('div', class_='catalog-list')
#     # print(catalog)
#     cars = catalog.find_all('a', class_='catalog-list-item')
#     # car1 = cars[0].find('span', class_='catalog-item-caption')
#     # print(car1.text.strip())
#     for car in cars:
#         title = car.find('span', class_='catalog-item-caption').text.strip()

#         mileage = car.find('span', class_='catalog-item-mileage').text
#         if not mileage:
#             mileage = 'Пробег отсутствует'
#         price = car.find('span', class_='catalog-item-price').text.strip()

#         try:
#             img = car.find('img', class_='catalog-item-cover-img').get('src')
#         except:
#             img = 'Картинки нет'

#         data = {'title': title, 'mileage': mileage, 'price': price, 'img': img}
        
#         write_to_csv(data)

#         # print(f'Название: {title} Пробег: {mileage}, Цена: {price}, Картинка: {img}')

# def write_to_csv(data: dict) -> None:
#     '''Функция для записи данных в csv файл'''
#     import csv
#     with open('cars.csv', 'a') as file:
#         fieldnames = ['Марка', 'Пробег', 'Цена', 'Фото']
#         writer = csv.DictWriter(file, fieldnames)
#         writer.writerow({'Марка': data.get('title'),
#         'Пробег': data.get('mileage'), 'Цена': data.get('price'),
#         'Фото': data.get('img')})


# # get_data(get_html(BASE_URL))

# i = 1
# k = 20

# start = datetime.datetime.now()
# while True:
#     BASE_URL = f'https://cars.kg/offers/{i}'
#     html = get_html(BASE_URL)
#     catalog = BeautifulSoup(html, 'lxml').find('div', class_='catalog-list')

#     if not catalog:
#         break

#     get_data(html)
#     i += 1
#     k += 20
#     print(f'Страница: {i}, Кол-во машин: {k}')
# end = datetime.datetime.now()
# print(end - start)

# -----------------------------# ----------------------------------

# """
# 1)	В текстовом файле посчитать количество  строк, а также для каждой отдельной строки
# определить количество в ней символов и слов.0
# """
# # with open(file) as file:
# #   file('file', 'r')
  
"""
2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""
from bs4 import BeautifulSoup as bs
import requests

base_url = 'https://vesti.kg/'

def get_html(url):
  response = requests.get(url).text
  return response

def get_data(html):
    soup = bs(html, 'lxml')
    div = soup.find('div', class_='itemList')
    titles = div.find_all('h2')
    for title in titles:
        print(title.text.strip())


get_data(get_html(base_url))








