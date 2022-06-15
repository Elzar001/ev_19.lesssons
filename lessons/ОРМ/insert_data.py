import peewee
from models import Category, Product

def add_category(name):
    try:
        row = Category(name=name.lower().strip())
        row.save()
        print('Сохранено')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такие категории уже сушествуют')

def add_product(name, price, category_name):
    category_exist=True
    try:
        category = Category.select().where(
            Category.name==category_name.lower().strip()
        ).get()
    
    except peewee.DoesNotExist:
        category_exist = False

    if category_exist:
        row = Product(
            title = name.lower().strip(),
            price = price,
            category = category
        )
        row.save()

# add_category('Платья')
# add_category('Футболки')
# add_category('Худи')

add_product('makers 001', 1000, 'Футболки')
add_product('makers 002', 1000, 'Футболки')
add_product('Суприм', 10000, 'Платья')
add_product('ЗАРА', 78000, 'Худи')
add_product('DG 022', 4000, 'Ислося')
