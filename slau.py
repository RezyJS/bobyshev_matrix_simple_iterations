import math
from vector_functions import *
from metrics import *


def print_matrix(matrix: list[list[float]], freeTermsMatrix: list[float], epsilon: float) -> None:
    length = len(matrix)

    for i in range(length):
        for j in range(length):
            if str(matrix[i][j])[0] != "-":
                print(
                    f" {matrix[i][j]:.{epsilon + 2}f}  ".ljust(epsilon + 2),
                    end="  ",
                )
            else:
                print(
                    f"{matrix[i][j]:.{epsilon + 2}f}  ".ljust(epsilon + 2),
                    end="  ",
                )

        print(
            f"|  x{i + 1}  |  {freeTermsMatrix[i] if str(
                freeTermsMatrix[i])[0] == '-' else ' ' + str(freeTermsMatrix[i])}"
        )


def print_matrix_for_x1(matrix: list[list[float]], freeTermsMatrix: list[float], epsilon: float) -> None:
    length = len(matrix)

    for i in range(length):
        for j in range(length):
            if str(matrix[i][j])[0] != "-":
                print(
                    f" {matrix[i][j]:.{epsilon + 2}f}  ".ljust(epsilon + 2),
                    end="  ",
                )
            else:
                print(
                    f"{matrix[i][j]:.{epsilon + 2}f}  ".ljust(epsilon + 2),
                    end="  ",
                )

        print(
            f"|  {str(freeTermsMatrix[i] if str(freeTermsMatrix[i])[0] == '-' else ' ' + str(freeTermsMatrix[i])).ljust(max([len(str(x))
                                                                                                                             for x in freeTermsMatrix]))}  |  {freeTermsMatrix[i] if str(freeTermsMatrix[i])[0] == '-' else ' ' + str(freeTermsMatrix[i])}"
        )


def read_matrix(length: int) -> list[list[float]]:
    return [read_vector(f"Введите элемент из строчки {i + 1}: ", length) for i in range(length)]


def read_vector(text: str, length: int) -> list[float]:
    vector: list[float] = []
    vector_line: list[str] = []

    while len(vector_line) < length:
        vector_line.extend(input(text).split(' '))

    for equation in vector_line:
        if equation.count("/") > 0:
            number = list(map(float, equation.split('/')))
            vector.append(number[0] / number[1])
        else:
            vector.append(float(equation))

    return vector


def normalize_my_matrix(matrix: list[list[float]], vector: list[float], length: int) -> list[list[float]]:
    for i in range(length):
        element: float = matrix[i][i]

        for j in range(length):
            matrix[i][j] /= -element
        vector[i] /= element

        matrix[i][i] = 0


def check_alpha(matrix: list[list[float]], length) -> float:
    print("\nПроверяем выполнение условия alpha...")

    alpha_sums = [0 for _ in range(length)]
    for j in range(length):
        for i in range(length):
            alpha_sums[j] += math.fabs(matrix[j][i])

    if 0 <= max(alpha_sums) < (0.99):
        return (True, max(alpha_sums))

    else:
        return (False, max(alpha_sums))


def check_beta(matrix: list[list[float]], length) -> float:
    print("\nПроверяем выполнение условия beta...")

    beta_sums = [0 for _ in range(length)]
    for i in range(length):
        for j in range(length):
            beta_sums[i] += math.fabs(matrix[j][i])

    if 0 <= max(beta_sums) < (0.99):
        return (True, max(beta_sums))

    else:
        return (False, max(beta_sums))


def check_gamma(matrix: list[list[float]], length) -> float:
    print("\nПроверяем выполнение условия gamma...")

    gamma_sums = 0

    for i in range(length):
        for j in range(length):
            gamma_sums += matrix[i][j] ** 2

    if 0 <= gamma_sums < (0.99):
        return (True, gamma_sums)

    else:
        return (False, gamma_sums)


def get_iterations_value(epsilon: int, metric: callable, x0: list[float], x1: list[float], coefficient: tuple[bool, float]) -> float:
    return math.ceil(math.log(math.pow(10, -epsilon) / metric(x0, x1) * (1 - coefficient[1]), coefficient[1]))
