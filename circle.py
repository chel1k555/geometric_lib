import math


def area(r):
    if r < 0:
        raise AssertionError("raduis can't be negative")
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        raise AssertionError("raduis can't be negative")
    return 2 * math.pi * r
