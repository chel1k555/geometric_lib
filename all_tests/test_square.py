import unittest
from math import pi
from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        radius = 1
        res = area(radius)
        self.assertEqual(res, pi)

    def test_perimeter(self):
        radius = 1
        res = perimeter(radius)
        self.assertEqual(res, 2 * pi)

    def test_area_zero(self):
        radius = 0
        res = area(radius)
        self.assertEqual(res, 0)

    def test_perimeter_zero(self):
        radius = 0
        res = perimeter(radius)
        self.assertEqual(res, 0)

    def test_area_neg(self):
        radius = -1
        with self.assertRaises(AssertionError):
            area(radius)

    def test_perimeter_neg(self):
        radius = -1
        with self.assertRaises(AssertionError):
            perimeter(radius)


if __name__ == '__main__':
    unittest.main()
