class Fruits:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        return f'Fruits - {self.name},color - {self.color},weight - {self.weight}'


apple = Fruits("Apple", "Red", "30g")
banana = Fruits("Banana", "Yellow", "70g")
mango = Fruits("Mango", "yellow-orange", "130g")

print(f'{apple.info()}; {banana.info()}; {mango.info()}')