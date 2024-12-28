stores = [
    (101, "Store A"),
    (102, "Store B"),
    (103, "Store C"),
    (104, "Store D")
]


def display_stores():
    # Отображаем список магазинов
    print("Перечень магазинов:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")
    print("Для выхода из программы введите цифру 0:")


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

        # Поиск магазина по id
        store = next((s for s in stores if s[0] == store_id), None)

        if store:
            print(f"Вы выбрали магазин: {store[1]}")
            # Здесь можно добавить функциональность для отображения продуктов, например:
            # display_products(store_id)
        else:
            print("Магазин с таким id не найден. Попробуйте снова.")


if __name__ == "__main__":
    main()