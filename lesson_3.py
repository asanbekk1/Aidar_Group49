class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, cpu):
        if cpu <= 0:
            print("Ошибка: Частота процессора не может быть отрицательной или равной нулю!")
        else:
            self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        if memory <= 0:
            print("Ошибка: Объем памяти не может быть меньше или равен нулю!")
        else:
            self.__memory = memory

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Computer: CPU = {self.__cpu} GHz, Memory = {self.__memory} GB"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def set_sim_cards(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards(self):
        return self.__sim_cards_list

    def add_sim_card(self, sim_card):
        self.__sim_cards_list.append(sim_card)

    def remove_sim_card(self, sim_card):
        if sim_card in self.__sim_cards_list:
            self.__sim_cards_list.remove(sim_card)
        else:
            print(f"Сим-карта {sim_card} не найдена.")

    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        computer_info = Computer.__str__(self)
        phone_info = Phone.__str__(self)
        return f"{computer_info}\n{phone_info}"


computer = Computer(cpu=3.5, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MTS", "MegaCom"])
smartphone1 = SmartPhone(cpu=2.8, memory=64, sim_cards_list=["Beeline", "MegaCom"])
smartphone2 = SmartPhone(cpu=3.0, memory=32, sim_cards_list=["MTS", "Tele2"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

smartphone1.use_gps("Almaty")
smartphone2.call(1, "+996 777 99 88 11")
print(f"Результат вычислений для компьютера: {computer.make_computations()}")

print(f"Компьютер 1 имеет больше памяти, чем Компьютер 2? {computer > Computer(3.0, 8)}")

phone.add_sim_card("Tele2")
print(phone.get_sim_cards())  # ['Beeline', 'MTS', 'MegaCom', 'Tele2']
phone.remove_sim_card("MTS")
print(phone.get_sim_cards())  # ['Beeline', 'MegaCom', 'Tele2']
