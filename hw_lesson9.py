# Список магазинов (эти данные могут быть получены из базы данных)
stores = [
    "Asia",
    "Globus",
    "Spar"
]


def display_stores():
    # Отображаем список магазинов
    print("Перечень магазинов:")
    for index, store in enumerate(stores, start=1):
        print(f"{index}. {store}")
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

        # Проверяем, существует ли магазин с таким id
        if 1 <= store_id <= len(stores):
            print(f"Вы выбрали магазин: {stores[store_id - 1]}")
            # Здесь можно добавить функциональность для отображения продуктов, например:
            # display_products(store_id)
        else:
            print("Магазин с таким id не найден. Попробуйте снова.")


if __name__ == "__main__":
    main()
