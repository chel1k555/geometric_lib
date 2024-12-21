import unittest
from calculate import calc
from scenarios import scenarios


class TestCalculateCorrectCircle(unittest.TestCase):
    def test_calc_circle_area(self):
        for radius, expected in scenarios['circle']['area']:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(calc(
                    'circle', 'area', [radius]), expected)

    def test_calc_circle_perimeter(self):
        for radius, expected in scenarios['circle']['perimeter']:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(calc(
                    'circle', 'perimeter', [radius]), expected)


class TestCalculateCorrectSquare(unittest.TestCase):
    def test_calc_square_area(self):
        for side, expected in scenarios['square']['area']:
            with self.subTest(side=side, expected=expected):
                self.assertAlmostEqual(calc(
                    'square', 'area', [side]), expected)

    def test_calc_square_perimeter(self):
        for side, expected in scenarios['square']['perimeter']:
            with self.subTest(side=side, expected=expected):
                self.assertAlmostEqual(calc(
                    'square', 'perimeter', [side]), expected)


class TestCalculateCorrectTriangle(unittest.TestCase):
    def test_calc_triangle_area(self):
        for sides, expected in scenarios['triangle']['area']:
            with self.subTest(sides=sides, expected=expected):
                self.assertAlmostEqual(calc(
                    'triangle', 'area', sides), expected)

    def test_calc_triangle_perimeter(self):
        for sides, expected in scenarios['triangle']['perimeter']:
            with self.subTest(sides=sides, expected=expected):
                self.assertAlmostEqual(calc(
                    'triangle', 'perimeter', sides), expected)


class TestCalculateIncorrectCircle(unittest.TestCase):
    def test_calc_incorrect_circle_area_negative_size(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [-1])

    def test_calc_incorrect_circle_area_non_numeric(self):
        with self.assertRaises(TypeError):
            calc('circle', 'area', ['a'])

    def test_calc_incorrect_circle_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [1])


class TestCalculateIncorrectSquare(unittest.TestCase):
    def test_calc_incorrect_square_area_negative_size(self):
        with self.assertRaises(ValueError):
            calc('square', 'area', [-1])

    def test_calc_incorrect_square_area_non_numeric(self):
        with self.assertRaises(TypeError):
            calc('square', 'area', ['a'])

    def test_calc_incorrect_square_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('square', 'volume', [1])


class TestCalculateIncorrectTriangle(unittest.TestCase):
    def test_calc_incorrect_triangle_area_negative_size(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [-1, 2, 3])

    def test_calc_incorrect_triangle_area_non_numeric(self):
        with self.assertRaises(TypeError):
            calc('triangle', 'area', [1, 'a', 3])

    def test_calc_incorrect_triangle_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'volume', [1, 2, 3])

    def test_calc_incorrect_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            calc('triangle', 'area', [1, 1, 10])


if __name__ == '__main__':
    unittest.main()
