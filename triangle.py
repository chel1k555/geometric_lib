from math import sqrt


def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("sides can't be negative")
    x = (a + b + c) / 2
    return sqrt(x * (x - a) * (x - b) * (x - c))


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("sides can't be negative")
    return a + b + c
