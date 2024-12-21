
def area(a):
    if a < 0:
        raise AssertionError("side can't be negative")
    return a * a


def perimeter(a):
    if a < 0:
        raise AssertionError("side can't be negative")
    return 4 * a
