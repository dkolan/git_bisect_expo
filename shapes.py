import math

class Shape:
    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class Ellipse(Shape):
    def __init__(self, a1, a2) -> None:
        self.axis_1 = a1
        self.axis_2 = a2

    def perimeter(self):
        a = self.axis_1
        b = self.axis_2
        return (
            math.pi * ((a + b) + (3(a - b**2)) / (10 * (a + b) + math.sqrt(a**2 + (14 * a * b) + b**2)))
        )

    def area(self):
        a = self.axis_1
        b = self.axis_2
        return math.pi * a * b

    def __str__(self):
        return "Cicumference: " + str(self.perimeter()) + "\nArea: " + str(self.area())

class Circle(Ellipse):
    def __init__(self, a1) -> None:
        super().__init__(a1, a1)

    def perimeter(self):
        a = self.axis_1
        return 2 * math.pi * a

    def area(self):
        return super().area()

    def __str__(self):
        return super().__str__()

class Triangle(Shape):
    def __init__(self, s1, s2, s3) -> None:
        self.side_1 = s1
        self.side_2 = s2
        self.side_3 = s3

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3))

    def __str__(self):
        return "Perimeter: " + str(self.perimeter()) + "\nArea: " + str(self.area())