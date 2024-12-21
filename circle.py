
import math


def area(r):
    if r < 0 or not isinstance(r, (int, float)):
        raise ValueError("Radius must be a non-negative number")
    return math.pi * r * r


def perimeter(r):
    if r < 0 or not isinstance(r, (int, float)):
        raise ValueError("Radius must be a non-negative number")
    return 2 * math.pi * r
