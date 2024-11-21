"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 2

Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы.
"""

from tabulate import tabulate
from utility.matrix_input import input_matrix


def rotate_clockwise(matrix, n):
    """Поворачивает матрицу на 90 градусов по часовой стрелке."""
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Сохраняем текущий элемент
            temp = matrix[i][j]

            # Перемещаем элементы против часовой стрелки
            # Перемещаем левый -> верхний
            matrix[i][j] = matrix[n - 1 - j][i]
            # Перемещаем нижний -> левый
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Перемещаем правый -> нижний
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Перемещаем сохраненный верхний -> правый
            matrix[j][n - 1 - i] = temp


def rotate_counterclockwise(matrix, n):
    """Поворачивает матрицу на 90 градусов против часовой стрелки."""
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Сохраняем текущий элемент
            temp = matrix[i][j]

            # Перемещаем элементы по часовой стрелке
            # Перемещаем правый -> верхний
            matrix[i][j] = matrix[j][n - 1 - i]
            # Перемещаем нижний -> правый
            matrix[j][n - 1 - i] = matrix[n - 1 - i][n - 1 - j]
            # Перемещаем левый -> нижний
            matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - j][i]
            # Перемещаем сохраненный верхний -> левый
            matrix[n - 1 - j][i] = temp


def print_matrix(matrix, title):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(matrix))]
    table = [[f"[{i}]"] + row for i, row in enumerate(matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))


def main():
    # Ввод размера матрицы
    n = int(input("Введите размер квадратной матрицы: "))

    # Ввод матрицы
    print("\nВвод матрицы:")
    matrix = input_matrix(n, n)
    if matrix is None:
        print("Ввод отменен")
        return

    # Создаем копию матрицы для работы
    working_matrix = [row[:] for row in matrix]

    # Выводим исходную матрицу
    print_matrix(working_matrix, "Исходная матрица")

    # Поворачиваем по часовой стрелке
    rotate_clockwise(working_matrix, n)
    print_matrix(working_matrix, "Матрица после поворота на 90° по часовой стрелке")

    # Поворачиваем против часовой стрелки
    rotate_counterclockwise(working_matrix, n)
    print_matrix(working_matrix, "Матрица после поворота на 90° против часовой стрелки")


if __name__ == "__main__":
    main()
