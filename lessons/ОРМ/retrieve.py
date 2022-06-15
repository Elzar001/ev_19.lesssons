import peewee
from models import Category, Product

def find_all_categories():
    return Category.select()

def find_all_products():
    return Product.select()

categories = find_all_categories()
products = find_all_products()

print('Категория в db: ')

for i in  categories:
    print(i.name)

print('Все продукты в db: ')

for i in products:
    if i.category == categories[1]:
        print(f'title: {i.title}, price {i.price}, category: {i.category} ')

