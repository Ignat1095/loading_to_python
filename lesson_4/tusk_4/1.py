# 1) ✔Напишите функцию для транспонирования матрицы


matrix_1 = [[1, 2], [3, 4], [5, 6]]
matrix_2 = [[1, 2, 3, ], [3, 4, 5], [6, 7, 8]]
matrix_3 = [[1, 2, 3], [4, 5, 6]]

list_matrix = [matrix_1, matrix_2, matrix_3]


def nested_loop(matrix):
    """Метод с использованием вложенного цикла"""
    trans_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    print(trans_matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]

    return trans_matrix


# print(nested_loop(matrix_2))

# Красивое и простое решение
def print_matrix(matrix: list[[int]]):
    for row in matrix:
        print(*row, sep='\t')


def troanposition(matrix: list[[int]]):
    return list(zip(*matrix))

for matrix in list_matrix:
    print_matrix(matrix)
    print()
    print_matrix((troanposition(matrix)))
    print("="*10 + '\n')