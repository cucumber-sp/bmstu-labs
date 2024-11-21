"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 5

Даны 2 матрицы А и В. Получить матрицу С, равную произведению матриц А и В.
"""

from tabulate import tabulate
from utility.matrix_input import input_int_matrix


def multiply_matrices(matrix_a, matrix_b):
    """Умножает две матрицы."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Создаем матрицу результата
    matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Выполняем умножение матриц
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


def print_matrix(matrix, title):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(matrix[0]))]
    table = [[f"[{i}]"] + row for i, row in enumerate(matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))


def main():
    # Ввод размеров первой матрицы
    rows_a = int(input("Введите количество строк матрицы A: "))
    cols_a = int(input("Введите количество столбцов матрицы A: "))

    # Ввод размеров второй матрицы
    print("\nКоличество строк матрицы B должно быть равно", cols_a)
    rows_b = cols_a
    cols_b = int(input("Введите количество столбцов матрицы B: "))

    # Ввод матриц
    print("\nВвод матрицы A:")
    matrix_a = input_int_matrix(rows_a, cols_a)
    if matrix_a is None:
        print("Ввод отменен")
        return

    print("\nВвод матрицы B:")
    matrix_b = input_int_matrix(rows_b, cols_b)
    if matrix_b is None:
        print("Ввод отменен")
        return

    # Умножение матриц
    matrix_c = multiply_matrices(matrix_a, matrix_b)

    # Вывод результатов
    print_matrix(matrix_a, "Матрица A")
    print_matrix(matrix_b, "Матрица B")
    print_matrix(matrix_c, "Матрица C = A × B")


if __name__ == "__main__":
    main()
