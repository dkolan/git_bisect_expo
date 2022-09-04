import math

class Shape:
    def perimiter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class Ellipse(Shape):
    def __init__(self, a1, a2) -> None:
        self.axis_1 = a1
        self.axis_2 = a2

    def perimiter(self):
        a = self.axis_1
        b = self.axis_2
        return (
            math.pi * ((a + b) + (3(a - b**2)) / (10 * (a + b) + math.sqrt(a**2 + (14 * a * b) + b**2)))
        )

    def area(self):
        a = self.axis_1
        b = self.axis_2
        return math.pi * a * b

class Circle(Ellipse):
    def __init__(self, a1) -> None:
        super().__init__(a1, a1)

    def perimiter(self):
        a = self.axis_1
        return 2 * math.pi * a

    def area(self):
        a = self.axis_1
        return math.pi * a**2