import slau
import metrics
import vector_functions as vf


if __name__ == "__main__":

    # Указываем погрешность
    epsilon: int = int(input("Введите точность (без знака, количество чисел после запятой): "))

    # Указываем размер матрицы (n x n)
    length: int = int(input("Введите размер матрицы: "))
    if length <= 0: raise ValueError("Размер матрицы не может быть меньше единицы.")
    print()

    # Считываем матрицу и вектор-столбец свободных членов
    coefficients_matrix: list[list[float]] = slau.read_matrix(length)
    free_terms_vector: list[float] = slau.read_vector("Введите столбец свободных членов: ", length)

    coefficients_matrix_copy: list[list[float]] = [ x.copy() for x in coefficients_matrix ]
    free_terms_vector_copy: list[float] = [ x for x in free_terms_vector ]

    print("\nВы ввели матрицу: ")
    slau.print_matrix(coefficients_matrix, free_terms_vector, epsilon)

    # Приводим матрицу к удобному нам виду
    # для выполнения простых итераций
    slau.normalize_my_matrix(coefficients_matrix_copy, free_terms_vector_copy, length)

    # Проверяем выполнения достаточных условий
    alpha: float = slau.check_alpha(coefficients_matrix_copy, length)
    beta: float = slau.check_beta(coefficients_matrix_copy, length)
    gamma: float = slau.check_gamma(coefficients_matrix_copy, length)

    print()
    print(f"{'alpha:'.ljust(7)} {alpha}")
    print(f"{'beta:'.ljust(7)} {beta}")
    print(f"{'gamma:'.ljust(7)} {gamma}")
    print()

    if not (alpha[0] or beta[0] or gamma[0]):
        print("Не выполняются достаточные условия.")
    else:
        x0: list[list[float]] = free_terms_vector_copy
        print(f'x0:\n{x0}')

        print('\nx1:')
        slau.print_matrix_for_x1(coefficients_matrix_copy, free_terms_vector_copy, epsilon)

        print(f"\nx1 вектор после преобразования: \n{(x1 := vf.sum_vectors(vf.multiply_matrix_vector(coefficients_matrix_copy, x0), free_terms_vector_copy))}\n")

        iterations_k: int = 0
        iterations_k_list: list[(bool, int)] = []

        iterations_k_list.append([alpha[0], slau.get_iterations_value(epsilon, metrics.ro_inf, x0, x1, alpha)])
        iterations_k_list.append([beta[0], slau.get_iterations_value(epsilon, metrics.ro_1, x0, x1, beta)])
        iterations_k_list.append([gamma[0], slau.get_iterations_value(epsilon, metrics.ro_2, x0, x1, gamma)])

        iterations_k = min(filter(lambda x: x[0] is True, iterations_k_list))[1]

        print("Число итераций для:")
        print(f"{'alpha:'.ljust(7)} {iterations_k_list[0][1]}")
        print(f"{'beta :'.ljust(7)} {iterations_k_list[1][1]}")
        print(f"{'gamma:'.ljust(7)} {iterations_k_list[2][1]}\n")

        if (iterations_k > 2):
            print(f"Количество итераций: {iterations_k}")

            print("\nПроводим итерации: ")
            print(f"\nx0={x0}\nx1={x1}\n\n...\n")

            x_list = [x0, x1]

            for i in range(2, iterations_k + 1):
                x_n = vf.sum_vectors(vf.multiply_matrix_vector(coefficients_matrix_copy, x_list[i - 1]), free_terms_vector_copy)
                x_list.append(x_n)

                if i > iterations_k - 5:
                    print(f"x_{i}=[ ", end="")
                    for _ in x_n:
                        print(f"{_:.{epsilon+2}f}", end=" ")
                    print("]")

            print("\nСчитаем невязку: ")
            temp_A = vf.sum_vectors(
                vf.multiply_matrix_vector(
                    coefficients_matrix, x_list[iterations_k]),
                [(-1) * x for x in free_terms_vector],
            )
            for i in temp_A:
                if str(i)[0] == '-':
                    print(f"{i:.{epsilon+2}f}")
                else:
                    print(f" {i:.{epsilon+2}f}")

        else:
            print(f"Количество итераций < 2; x0={x0}, x1={x1}")
