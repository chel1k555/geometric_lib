import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        x, y, z = 5, 12, 13
        res = area(x, y, z)
        self.assertEqual(res, 30)

    def test_area_zero(self):
        x, y, z = 0, 0, 0
        res = area(x, y, z)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        x, y, z = 5, 12, 13
        res = perimeter(x, y, z)
        self.assertEqual(res, 30)

    def test_perimeter_zero(self):
        x, y, z = 0, 0, 0
        res = perimeter(x, y, z)
        self.assertEqual(res, 0)

    def test_area_neg(self):
        x, y, z = -5, -12, -13
        with self.assertRaises(AssertionError):
            area(x, y, z)

    def test_perimeter_neg(self):
        x, y, z = -5, -12, -13
        with self.assertRaises(AssertionError):
            perimeter(x, y, z)


if __name__ == '__main__':
    unittest.main()
