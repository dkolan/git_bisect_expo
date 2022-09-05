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
            math.pi * ((a + b) + (3 * (a - b**2)) / (10 * (a + b) + math.sqrt(a**2 + (14 * a * b) + b**2)))
        )

    def area(self):
        a = self.axis_1
        b = self.axis_2
        return math.pi * a * b

    def __str__(self):
        title = "========== ELLIPSE ==========\n\n"
        return title + "Cicumference: " + str(self.perimeter()) + "\nArea: " + str(self.area())

class Circle(Ellipse):
    def __init__(self, a1) -> None:
        super().__init__(a1, a1)

    def perimeter(self):
        a = self.axis_1
        return 2 * math.pi * a

    def area(self):
        return super().area()

    def __str__(self):
        title = "========== CIRCLE ==========\n\n"
        return title + super().__str__()

class Triangle(Shape):
    def __init__(self, sides: list[float], angles: list[float]) -> None:
        if ((sides[0] + sides[1] < sides[2] 
        or sides[0] + sides[2] < sides[3] 
        or sides[2] + sides[3] < sides[0])
        or (sum(angles) != 180)):
            raise ValueError
        else:
            self.side_1 = sides[0]
            self.side_2 = sides[1]
            self.side_3 = sides[2]
            self.angle_s1s2 = angles[0]
            self.angle_s2s3 = angles[1]
            self.angle_s3s1 = angles[2]       

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3))

    def __str__(self):
        title = "========== TRIANGLE ==========\n\n"
        return title + "Perimeter: " + str(self.perimeter()) + "\nArea: " + str(self.area())

class Quadrilateral(Shape):
    def __init__(self, sides: list[float], angles: list[float]) -> None:
        if ((sides[0] + sides[1] + sides[2] < sides[3] 
        or sides[0] + sides[1] + sides[3] < sides[2]  
        or sides[0] + sides[2] + sides[3] < sides[1]
        or sides[1] + sides[2] + sides[3] < sides[0])
        or (sum(angles) != 360)):
            raise ValueError
        else:
            self.side_1 = sides[0]
            self.side_2 = sides[1]
            self.side_3 = sides[2]
            self.side_4 = sides[3]
            self.angle_s1s2 = angles[0]
            self.angle_s2s3 = angles[1]
            self.angle_s3s4 = angles[2]  
            self.angle_s4s1 = angles[3]  


    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4

    def area(self):
        raise NotImplementedError

    def __str__(self):
        title = "========== QUADRILATERAL ==========\n\n"
        return "Perimeter: " + str(self.perimeter()) + "\nArea unknown without more information (diagonal or angles)."

class Parallelogram(Quadrilateral):
    def __init__(self, sides: list[float], angles: list[float]) -> None:
        # Check if there are pairs of equal sides
        side_1 = sides.pop(0)
        if (side_1 in sides):
            sides.remove(side_1)
        side_2 = sides.pop(0)
        if (side_2 in sides):
            self.side_1 = side_1
            self.side_2 = side_2
            self.side_3 = side_1
            self.side_4 = side_2
            self.angle_s1s2 = angles[0]
            self.angle_s2s3 = angles[1]
            self.angle_s3s4 = angles[2]  
            self.angle_s4s1 = angles[3]  
        else:
            raise ValueError

    def perimeter(self):
        return super().perimeter()

    def area(self):
        raise NotImplementedError

    def __str__(self):
        title = "========== PARALLELOGRAM ==========\n\n"
        return title + "Perimeter: " + str(self.perimeter()) + "\nArea unknown without more information (diagonal or angles)."

class Rectangle(Parallelogram):
    def __init__(self, sides: list[float], angles: list[float]) -> None:
        if len(set(angles)) == 1:
            super().__init__(sides, angles)
        else:
            raise ValueError

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return self.side_1 * self.side_2

    def __str__(self):
        title = "========== RECTANGLE ==========\n\n"
        return title + "Perimeter: " + str(self.perimeter()) + "\nArea: " + str(self.area())

class Square(Rectangle):
    def __init__(self, sides: list[float], angles: list[float]) -> None:
        if (
            len(set(sides)) == 1
            and len(set(angles)) == 1
        ):
            super().__init__(sides, angles)
        else:
            raise ValueError

    def perimeter(self):
        return self.side_1 * 4

    def area(self):
        return self.side_1**2

    def __str__(self):
        title = "========== SQUARE ==========\n\n"
        return title + "Perimeter: " + str(self.perimeter()) + "\nArea: " + str(self.area())

def main():
    rectangle = Rectangle([2, 4, 2, 4], [90, 90, 90, 90])
    print(rectangle.__str__())

if __name__ == "__main__":
    main()

