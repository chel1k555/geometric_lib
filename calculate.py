import circle
import square
import triangle

FIGS = ['circle', 'square', 'triangle']
FUNCS = ['perimeter', 'area']
SIZES = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}


def calc(fig, func, size):
    assert fig in FIGS, "Invalid figure"
    assert func in FUNCS, "Invalid function"

    key = f'{fig}-{func}'
    args = SIZES.get(key)
    assert args is not None, "Size arguments were not found"
    assert len(size) == args, "Invalid size arguments number"

    assert all(s >= 0 for s in size), "Negative size values are not allowed"

    if fig == "triangle":
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle size"

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in FIGS:
        fig = input(f"Enter figure name, available are {FIGS}:\n")

    while func not in FUNCS:
        func = input(f"Enter function name, available are {FUNCS}:\n")

    expected_size = SIZES.get(f"{fig}-{func}", 1)
    while len(size) != expected_size:
        size = list(map(int, input(
            f"Input figure sizes separated by space, {expected_size} values for {fig} {func}:\n"
        ).split()))

    result = calc(fig, func, size)
    print(f"Result: {result}")
