import datetime

class Car:
    def __init__(self, marka, model, year, mileage):
        self.marka = marka
        self.model = model
        self._year = year
        self.__mileage = mileage

    def info(self):
        return f'Марка - {self.marka} \nМодель - {self.model}'

    def _calculator_age(self):
        current = datetime.datetime.now().year
        return f'Возраст машины - {current - self._year}'

    def __update_milage(self):
        return F'Миль - {self.__mileage}'

    def set_mileage(self):
        return f'{self.__update_milage()}'


car = Car("BMV", "X5", 2020, 513)
print(car.info())
print(car._calculator_age())
print(car.set_mileage())

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        plus = self.__cpu + self.__memory
        minus = self.__cpu - self.__memory
        mul = self.__cpu * self.__memory
        div = self.__cpu / self.__memory
        return f"Вычисления:\n{self.__cpu} + {self.__memory} = {plus}\n{self.__cpu} - {self.__memory} = {minus}\n{self.__cpu} * {self.__memory} = {mul}\n{self.__cpu} / {self.__memory} = {div}"

    def computations_info(self):
        return self.__make_computations()

    def get_cpu(self):
        return f'Количество cpu: {self.__cpu}'

    def get_memory(self):
        return f'Количество memory: {self.__memory}'


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def info(self):
        comp_info = self.computations_info()
        memory_card_info = f"Количество memory card: {self.__memory_card}"
        return f"{comp_info}\n{memory_card_info}"


laptop = Laptop(10, 5, 3)
print('Информация о компьютере')
print(laptop.info())
print(laptop.get_cpu())
print(laptop.get_memory())


