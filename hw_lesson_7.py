import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')

conn.commit()

def add_sample_products():
    products = [
        ('Жидкое мыло с запахом ванили', 50.0, 10),
        ('Мыло детское', 30.0, 20),
        ('Шампунь для волос', 150.0, 5),
        ('Кондиционер для волос', 120.0, 8),
        ('Гель для душа', 70.0, 15),
        ('Пену для ванны', 100.0, 12),
        ('Мыло туалетное', 40.0, 25),
        ('Салфетки влажные', 20.0, 30),
        ('Туалетная бумага', 10.0, 50),
        ('Дезодорант', 80.0, 10),
        ('Зубная паста', 60.0, 18),
        ('Шариковая ручка', 5.0, 100),
        ('Блокнот', 25.0, 60),
        ('Папка для документов', 35.0, 40),
        ('Фломастеры', 15.0, 70)
    ]

    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)
    conn.commit()

def update_quantity(id, new_quantity):
    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, id))
    conn.commit()

def update_price(id, new_price):
    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, id))
    conn.commit()

def delete_product(id):
    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (id,))
    conn.commit()

def print_all_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def find_cheap_and_available_products(price_limit, quantity_limit):
    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products_by_title(keyword):
    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

add_sample_products()

print("Все товары:")
print_all_products()

update_quantity(1, 100)

update_price(2, 35.0)

delete_product(3)

print("\nВсе товары после изменений:")
print_all_products()

print("\nТовары, дешевле 50 сом и с количеством больше 10:")
find_cheap_and_available_products(50.0, 10)

print("\nТовары, содержащие 'мыло' в названии:")
search_products_by_title('мыло')