import math


def ro_inf(x: list, y: list) -> int:
    ro = math.fabs(x[0] - y[0])

    for (i, j) in zip(x, y):
        ro = max(ro, math.fabs(i - j))

    return ro


def ro_1(x: list, y: list) -> int:
    ro = 0

    for (i, j) in zip(x, y):
        ro += math.fabs(i - j)

    return ro


def ro_2(x: list, y: list) -> int:
    ro = 0

    for (i, j) in zip(x, y):
        ro += math.fabs(i - j) ** 2

    return math.sqrt(ro)
