import unittest
import circle
from scenarios import scenarios


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        for radius, expected in scenarios['circle']['area']:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(circle.area(radius), expected)

    def test_area_invalid_negative(self):
        for invalid_radius in [-1, -10]:
            with self.subTest(radius=invalid_radius):
                with self.assertRaises(ValueError):
                    circle.area(invalid_radius)

    def test_area_invalid_non_numeric(self):
        for invalid_radius in ['a', None]:
            with self.subTest(radius=invalid_radius):
                with self.assertRaises(TypeError):
                    circle.area(invalid_radius)


class TestCirclePerimeter(unittest.TestCase):
    def test_perimeter(self):
        for radius, expected in scenarios['circle']['perimeter']:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(circle.perimeter(radius), expected)

    def test_perimeter_invalid_negative(self):
        for invalid_radius in [-1, -10]:
            with self.subTest(radius=invalid_radius):
                with self.assertRaises(ValueError):
                    circle.perimeter(invalid_radius)

    def test_perimeter_invalid_non_numeric(self):
        for invalid_radius in ['a', None]:
            with self.subTest(radius=invalid_radius):
                with self.assertRaises(TypeError):
                    circle.perimeter(invalid_radius)


if __name__ == '__main__':
    unittest.main()
