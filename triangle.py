import math


def area(a, b, c):
    if (
        a <= 0 or b <= 0 or c <= 0
        or not all(isinstance(side, (int, float)) for side in [a, b, c])
        or (a + b <= c) or (a + c <= b) or (b + c <= a)
    ):
        raise ValueError("Sides must be positive numbers"
                         " and form a valid triangle")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def perimeter(a, b, c):
    if (
        a <= 0 or b <= 0 or c <= 0
        or not all(isinstance(side, (int, float)) for side in [a, b, c])
        or (a + b <= c) or (a + c <= b) or (b + c <= a)
    ):
        raise ValueError("Sides must be positive numbers"
                         " and form a valid triangle")
    return a + b + c
