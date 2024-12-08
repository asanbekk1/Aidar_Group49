import abc
import math


class Figure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if type(self.side_a) in (int, float) and type(self.side_b) in (int, float) and \
                type(self.side_c) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for {self.__class__.__name__}!")

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        return f"Perimeter is: {round(self.perimeter(), 3)}\nArea is: {round(self.area(), 3)}"


class Square(Figure):
    def __init__(self, side_a):
        self.side_a = side_a

        if type(self.side_a) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for {self.__class__.__name__}!")

    def perimeter(self):
        return 4 * self.side_a

    def area(self):
        return self.side_a * self.side_a

    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        return f"Perimeter is: {round(self.perimeter(), 3)}\nArea is: {round(self.area(), 3)}"


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

        if type(self.side_a) in (int, float) and type(self.side_b) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for {self.__class__.__name__}!")

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b

    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        return f"Perimeter is: {round(self.perimeter(), 3)}\nArea is: {round(self.area(), 3)}"


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

        if type(self.radius) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for {self.__class__.__name__}!")

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius * self.radius

    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        return f"Perimeter is: {round(self.perimeter(), 3)}\nArea is: {round(self.area(), 3)}"


if __name__ == '__main__':

    figures = []

    circle = Circle(1.5)
    figures.append(circle)

    rectangle = Rectangle(10, 5)
    figures.append(rectangle)

    square = Square(10)
    figures.append(square)

    triangle = Triangle(2, 2, 3)
    figures.append(triangle)

    triangle2 = Triangle(1, 2, 3)
    figures.append(triangle2)

    for i in figures:
        print(i.calculator())
