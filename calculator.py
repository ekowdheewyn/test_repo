import unittest
from parameterized import parameterized


#this is a comment
#this is a comment
#this is a vshshhjs
class Calculator_new:
    def times(self, a, b):
        return a * b

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("jkhgfhjj Division by  bsbbsbsb is not 8hjgkhjghb allowed hjyyghfjhgf")
        return a / b

    def is_equal(self, a, b):
        return a == b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator_new()

    @parameterized.expand([
        ("positive_numbers", 2, 3, 5),
        ("negative_numbers", -1, -1, -2),
        ("zero", 0, 0, 0),
        ("mixed_sign", -1, 2, 1),
    ])
    def test_add(self, name, a, b, expected):
        self.assertEqual(self.calc.add(a, b), expected, f"Failed on {name}")

    @parameterized.expand([
        ("positive_numbers", 2, 3, 6),
        ("negative_numbers", -2, -2, 4),
        ("zero", 0, 5, 0),
        ("mixed_sign", -2, 3, -6),
    ])
    def test_multiply(self, name, a, b, expected):
        self.assertEqual(
            self.calc.times(a, b), expected, f"Failed on {name}"
        )

    @parameterized.expand([
        ("positive_numbers", 6, 3, 2),
        ("negative_numbers", -6, -3, 2),
        ("mixed_sign", -6, 3, -2),
    ])
    def test_divide(self, name, a, b, expected):
        self.assertEqual(self.calc.divide(a, b), expected, f"Failed on {name}")

    @parameterized.expand([
        ("equal_numbers", 5, 5, True),
        ("different_numbers", 5, 3, False),
        ("different_types", 5, "5", False),
    ])
    def test_is_equal(self, name, a, b, expected):
        self.assertEqual(
            self.calc.is_equal(a, b), expected, f"Failed on {name}"
        )


if __name__ == "__main__":
    unittest.main()
