def area(a):
    if a < 0 or not isinstance(a, (int, float)):
        raise ValueError("Side length must be a non-negative number")
    return a * a


def perimeter(a):
    if a < 0 or not isinstance(a, (int, float)):
        raise ValueError("Side length must be a non-negative number")
    return 4 * a
