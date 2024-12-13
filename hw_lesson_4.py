import random

class Boss:
    def __init__(self, health=1000):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        print(f"Босс получил {damage} урона, оставшееся здоровье: {self.health}")
        if self.health <= 0:
            print("Босс побежден!")
        return self.health


class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона, оставшееся здоровье: {self.health}")
        if self.health <= 0:
            print(f"{self.name} погиб!")
        return self.health

    def attack_boss(self, boss):
        print(f"{self.name} атакует босса!")
        boss.take_damage(self.attack)

    def __str__(self):
        return f"{self.name}: HP = {self.health}, Attack = {self.attack}"


class Witcher(Hero):
    def __init__(self, health, attack, resurrect_chance=0.1):
        super().__init__("Witcher", health, attack)
        self.resurrect_chance = resurrect_chance
        self.resurrected = False

    def sacrifice_and_resurrect(self, fallen_hero):
        if random.random() < self.resurrect_chance and fallen_hero.health <= 0:
            fallen_hero.health = fallen_hero.max_health
            self.health = 0
            self.resurrected = True
            print(f"{self.name} пожертвовал собой и воскресил {fallen_hero.name}")
            return True
        return False

    def __str__(self):
        return f"{super().__str__()} (Resurrected: {self.resurrected})"


class Magic(Hero):
    def __init__(self, health, attack, buff_amount):
        super().__init__("Magic", health, attack)
        self.buff_amount = buff_amount
        self.rounds_buff_active = 0

    def apply_buff(self):
        if self.rounds_buff_active < 4:
            self.attack += self.buff_amount
            self.rounds_buff_active += 1
            print(f"{self.name} увеличил атаку на {self.buff_amount} на {4 - self.rounds_buff_active} раунда(ов)!")

    def __str__(self):
        return f"{super().__str__()} (Buffed attack: {self.attack})"


class Hacker(Hero):
    def __init__(self, health, attack, steal_amount):
        super().__init__("Hacker", health, attack)
        self.steal_amount = steal_amount

    def steal_health_from_boss(self, boss):
        damage = min(self.steal_amount, boss.health)
        boss.take_damage(damage)
        self.health += damage
        print(f"{self.name} забрал {damage} здоровья у босса и передал себе.")

    def __str__(self):
        return f"{super().__str__()} (Steal: {self.steal_amount})"


class Golem(Hero):
    def __init__(self, health, attack, shield):
        super().__init__("Golem", health, attack)
        self.shield = shield

    def take_damage(self, damage):
        damage_taken = damage * (1 - self.shield)
        super().take_damage(damage_taken)

    def __str__(self):
        return f"{super().__str__()} (Shield: {self.shield * 100}%)"


class Avrora(Hero):
    def __init__(self, health, attack):
        super().__init__("Avrora", health, attack)
        self.invisible = False
        self.invisibility_rounds = 0

    def go_invisible(self):
        if self.invisibility_rounds == 0:
            self.invisible = True
            self.invisibility_rounds = 2
            print(f"{self.name} становится невидимой на 2 раунда.")
        else:
            print(f"{self.name} уже был(а) невидим(а) в этом бою.")

    def take_damage(self, damage):
        if self.invisible > 0:
            print(f"{self.name} не получает урон (невидимость).")
            self.invisibility_rounds -= 1
        else:
            super().take_damage(damage)

    def __str__(self):
        return f"{super().__str__()} (Invisible: {self.invisible})"


boss = Boss(health=1000)
witcher = Witcher(health=500, attack=100)
magic = Magic(health=400, attack=60, buff_amount=20)
hacker = Hacker(health=300, attack=50, steal_amount=40)
golem = Golem(health=600, attack=30, shield=0.2)
avrora = Avrora(health=350, attack=70)


magic.apply_buff()
hacker.steal_health_from_boss(boss)
golem.take_damage(100)
avrora.go_invisible()

witcher.attack_boss(boss)
magic.attack_boss(boss)
hacker.attack_boss(boss)

boss.take_damage(50)

print(witcher)
print(magic)
print(hacker)
print(golem)
print(avrora)
