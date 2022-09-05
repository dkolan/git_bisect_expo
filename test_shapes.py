import pytest

from shapes import *

class TestShapes:
    # @pytest.mark.parametrize("sides, angles, expected", [([1, 1, 1, 1], [90,90,90,90], 4), ([2, 4, 2, 4], [90, 90, 90, 90], 12), ([5, 6, 5, 6], [90, 90, 90, 90], 22)])
    # def test_rectangle_perimeter(self, sides, angles, expected):
    #     rectangle = Rectangle(sides, angles)
    #     actual = rectangle.perimeter()

    #     assert actual == expected

    def test_rectangle_perimeter(self):
        rectangle = Rectangle([2, 4, 2, 4], [90,90,90,90])
        actual = rectangle.perimeter()
        expected = 12

        assert actual == expected