import random


def play_game(min_number, max_number, attempts, capital):
    current_capital = capital

    for attempt in range(attempts):
        if current_capital <= 0:
            print("У вас закончился капитал!")
            break

        print(f"\nПопытка {attempt + 1}/{attempts}. Ваш текущий капитал: {current_capital}")

        bet = int(input("Введите вашу ставку: "))
        if bet > current_capital:
            print("У вас недостаточно средств для этой ставки.")
            continue

        random_number = random.randint(min_number, max_number)
        guess = int(input(f"Введите ваше предположение от {min_number} до {max_number}: "))

        if guess == random_number:
            print(f"Поздравляем! Вы угадали число {random_number}. Ваши средства удваиваются.")
            current_capital += bet
        else:
            print(f"Увы, вы не угадали. Загаданное число было {random_number}. Вы потеряли ставку.")
            current_capital -= bet

    print(f"Игра окончена. Ваш остаток капитала: {current_capital}")





