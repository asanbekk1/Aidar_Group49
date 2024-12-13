class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def info(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.side_length}{Figure.unit}, area: {area}{Figure.unit}")

class Rectangle(Figure):  # Corrected 'Figures' to 'Figure'
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.length}{Figure.unit}, width: {self.width}{Figure.unit}, area: {area}{Figure.unit}")

figures = [
    Square(5),
    Square(3),
    Rectangle(5, 8),
    Rectangle(6, 4),
    Rectangle(7, 2)
]

for fig in figures:
    fig.info()
