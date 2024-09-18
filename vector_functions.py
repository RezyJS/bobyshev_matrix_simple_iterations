def multiply_matrix_vector(matrix, vector):
    result = [0 for _ in range(len(vector))]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result


def sum_vectors(vector1, vector2):
    result = [0 for _ in range(len(vector1))]
    for i in range(len(vector1)):
        result[i] = vector1[i] + vector2[i]
    return result
