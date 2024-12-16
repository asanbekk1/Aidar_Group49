from decouple import config
from logic import play_game


min_number = config('MIN', cast=int)
max_number = config('DIAPOZONE', cast=int)
attempts = config('POPYTKA', cast=int)
initial_capital = config('DENGI', cast=int)


def main():
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас есть {attempts} попыток, чтобы угадать число от {min_number} до {max_number}.")
    print(f"Ваш начальный капитал: {initial_capital}.")

    play_game(min_number, max_number, attempts, initial_capital)


if __name__ == "__main__":
    main()
