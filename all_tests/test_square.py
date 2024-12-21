import unittest
import square
from scenarios import scenarios


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        for side, expected in scenarios['square']['area']:
            with self.subTest(side=side, expected=expected):
                self.assertEqual(square.area(side), expected)

    def test_area_invalid_negative(self):
        for invalid_side in [-1, -10]:
            with self.subTest(side=invalid_side):
                with self.assertRaises(ValueError):
                    square.area(invalid_side)

    def test_area_invalid_non_numeric(self):
        for invalid_side in ['a', None]:
            with self.subTest(side=invalid_side):
                with self.assertRaises(TypeError):
                    square.area(invalid_side)


class TestSquarePerimeter(unittest.TestCase):
    def test_perimeter(self):
        for side, expected in scenarios['square']['perimeter']:
            with self.subTest(side=side, expected=expected):
                self.assertEqual(square.perimeter(side), expected)

    def test_perimeter_invalid_negative(self):
        for invalid_side in [-1, -10]:
            with self.subTest(side=invalid_side):
                with self.assertRaises(ValueError):
                    square.perimeter(invalid_side)

    def test_perimeter_invalid_non_numeric(self):
        for invalid_side in ['a', None]:
            with self.subTest(side=invalid_side):
                with self.assertRaises(TypeError):
                    square.perimeter(invalid_side)


if __name__ == '__main__':
    unittest.main()
