import unittest
import triangle
from scenarios import scenarios


class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        for sides, expected in scenarios['triangle']['area']:
            with self.subTest(sides=sides, expected=expected):
                self.assertAlmostEqual(triangle.area(*sides), expected)

    def test_area_invalid_negative(self):
        invalid_scenarios = [
            (-1, 2, 3), (1, -2, 3), (1, 2, -3)
        ]
        for sides in invalid_scenarios:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    triangle.area(*sides)

    def test_area_invalid_non_numeric(self):
        invalid_scenarios = [
            (1, 'a', 3), ('a', 2, 3), (1, 2, None)
        ]
        for sides in invalid_scenarios:
            with self.subTest(sides=sides):
                with self.assertRaises(TypeError):
                    triangle.area(*sides)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle.area(1, 1, 10)


class TestTrianglePerimeter(unittest.TestCase):
    def test_perimeter(self):
        for sides, expected in scenarios['triangle']['perimeter']:
            with self.subTest(sides=sides, expected=expected):
                self.assertEqual(triangle.perimeter(*sides), expected)

    def test_perimeter_invalid_negative(self):
        invalid_scenarios = [
            (-1, 2, 3), (1, -2, 3), (1, 2, -3)
        ]
        for sides in invalid_scenarios:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    triangle.perimeter(*sides)

    def test_perimeter_invalid_non_numeric(self):
        invalid_scenarios = [
            (1, 'a', 3), ('a', 2, 3), (1, 2, None)
        ]
        for sides in invalid_scenarios:
            with self.subTest(sides=sides):
                with self.assertRaises(TypeError):
                    triangle.perimeter(*sides)

    def test_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 10)


if __name__ == '__main__':
    unittest.main()
