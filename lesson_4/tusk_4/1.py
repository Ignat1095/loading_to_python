# 1) ✔Напишите функцию для транспонирования матрицы


matrix_list = [[1, 2], [3, 4], [5, 6]]
print(matrix_list)


def nested_loop(matrix):
    """Метод с использованием вложенного цикла"""
    trans_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    print(trans_matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]

    return trans_matrix

print(nested_loop(matrix_list))