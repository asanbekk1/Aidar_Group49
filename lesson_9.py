# Список магазинов (это могут быть данные из базы данных)
stores = [
    "Asia",
    "Globus",
    "Spar"
]

# Продукты в магазинах (реально эти данные будут взяты из базы данных, но для примера они заданы в коде)
products = [
    {"id": 1, "title": "Chocolate", "category": "FD", "unit_price": 10.5, "stock_quantity": 129, "store_id": 1},
    {"id": 2, "title": "Milk", "category": "FD", "unit_price": 1.2, "stock_quantity": 200, "store_id": 2},
    {"id": 3, "title": "Juice", "category": "FD", "unit_price": 2.5, "stock_quantity": 150, "store_id": 3},
    {"id": 4, "title": "Shampoo", "category": "CL", "unit_price": 5.0, "stock_quantity": 50, "store_id": 1},
    {"id": 5, "title": "Laptop", "category": "EL", "unit_price": 899.99, "stock_quantity": 15, "store_id": 2},
    {"id": 6, "title": "Bread", "category": "FD", "unit_price": 0.99, "stock_quantity": 100, "store_id": 3}
]

# Категории продуктов
categories = {
    "FD": "Food products",
    "CL": "Cleaning items",
    "EL": "Electronics"
}


def display_stores():
    # Отображаем список магазинов
    print("Перечень магазинов:")
    for index, store in enumerate(stores, start=1):
        print(f"{index}. {store}")
    print("Для выхода из программы введите цифру 0:")


def display_products(store_id):
    # Фильтруем продукты, которые находятся в выбранном магазине
    selected_products = [product for product in products if product["store_id"] == store_id]

    if selected_products:
        print("\nСписок продуктов в выбранном магазине:")
        for product in selected_products:
            category_title = categories.get(product["category"], "Неизвестная категория")
            print(f"Название продукта: {product['title']}")
            print(f"Категория: {category_title}")
            print(f"Цена: {product['unit_price']}")
            print(f"Количество на складе: {product['stock_quantity']}")
            print("-" * 40)
    else:
        print("В этом магазине нет продуктов.")


def main():
    while True:
        # Отображаем приглашение для пользователя
        display_stores()

        # Ввод пользователя
        user_input = input("Введите id магазина: ")

        # Преобразуем ввод в число
        try:
            store_id = int(user_input)
        except ValueError:
            print("Пожалуйста, введите цифру.")
            continue

        # Выход из программы
        if store_id == 0:
            print("Выход из программы.")
            break

        # Проверяем, существует ли магазин с таким id
        if 1 <= store_id <= len(stores):
            print(f"\nВы выбрали магазин: {stores[store_id - 1]}")
            # Отображаем продукты, связанные с выбранным магазином
            display_products(store_id)
        else:
            print("Магазин с таким id не найден. Попробуйте снова.")


if __name__ == "__main__":
    main()
