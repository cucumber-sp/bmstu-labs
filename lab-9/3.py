"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 3

Даны две матрицы A и B с одинаковым количеством столбцов.
Для каждого столбца матрицы А подсчитать количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
Преобразовать матрицу В, умножив элементы каждого столбца на соответствующее
ненулевое значение.
"""

from tabulate import tabulate
from utility.matrix_input import input_int_matrix


def calculate_column_means(matrix):
    """Вычисляет среднее арифметическое для каждого столбца матрицы."""
    n_cols = len(matrix[0])
    n_rows = len(matrix)
    means = []

    for j in range(n_cols):
        column_sum = sum(matrix[i][j] for i in range(n_rows))
        means.append(column_sum / n_rows)

    return means


def count_elements_greater_than_means(matrix_a, means):
    """Подсчитывает количество элементов в столбцах матрицы A,
    больших средних значений соответствующих столбцов."""
    n_cols = len(matrix_a[0])
    n_rows = len(matrix_a)
    counts = []

    for j in range(n_cols):
        count = sum(1 for i in range(n_rows) if matrix_a[i][j] > means[j])
        counts.append(count)

    return counts


def transform_matrix(matrix, multipliers):
    """Умножает каждый столбец матрицы на соответствующий ненулевой множитель."""
    n_cols = len(matrix[0])
    n_rows = len(matrix)

    for j in range(n_cols):
        if multipliers[j] != 0:
            for i in range(n_rows):
                matrix[i][j] *= multipliers[j]


def print_matrix(matrix, title):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(matrix[0]))]
    table = [[f"[{i}]"] + row for i, row in enumerate(matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))


def print_counts(counts):
    """Выводит количество элементов для каждого столбца."""
    print("\nКоличество элементов в столбцах матрицы A, больших среднего")
    print("арифметического соответствующих столбцов матрицы B:")
    headers = [f"Столбец {i}" for i in range(len(counts))]
    print(tabulate([counts], headers=headers, tablefmt="rounded_grid"))


def main():
    # Ввод размеров матриц
    n_cols = int(input("Введите количество столбцов для обеих матриц: "))
    rows_a = int(input("Введите количество строк матрицы A: "))
    rows_b = int(input("Введите количество строк матрицы B: "))

    # Ввод матриц
    print("\nВвод матрицы A:")
    matrix_a = input_int_matrix(rows_a, n_cols)
    if matrix_a is None:
        print("Ввод отменен")
        return

    print("\nВвод матрицы B:")
    matrix_b = input_int_matrix(rows_b, n_cols)
    if matrix_b is None:
        print("Ввод отменен")
        return

    # Вывод исходных матриц
    print_matrix(matrix_a, "Исходная матрица A")
    print_matrix(matrix_b, "Исходная матрица B")

    # Вычисление средних значений столбцов матрицы B
    means_b = calculate_column_means(matrix_b)

    # Подсчет элементов, больших средних значений
    counts = count_elements_greater_than_means(matrix_a, means_b)
    print_counts(counts)

    # Преобразование матрицы B
    transform_matrix(matrix_b, counts)
    print_matrix(matrix_b, "Преобразованная матрица B")


if __name__ == "__main__":
    main()
