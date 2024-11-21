"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №9 Задание 6

Дана матрица символов. Преобразовать её следующим образом: заменить все
согласные латинские буквы на заглавные, а все гласные латинские буквы на
строчные.
"""

from tabulate import tabulate
from utility.matrix_input import input_symbol_matrix

# Множества гласных и согласных букв
VOWELS = set("aeiouAEIOU")
CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")


def transform_matrix(matrix):
    """Преобразует матрицу согласно условию."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу для результата
    result = [["" for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            char = matrix[i][j]
            # Проверяем, является ли символ латинской буквой
            if char.isalpha():
                # Если гласная - делаем строчной
                if char in VOWELS:
                    result[i][j] = char.lower()
                # Если согласная - делаем заглавной
                elif char in CONSONANTS:
                    result[i][j] = char.upper()
                else:
                    result[i][j] = char  # Не латинская буква
            else:
                result[i][j] = char  # Не буква

    return result


def print_matrix(matrix, title):
    """Выводит матрицу с заголовком."""
    print(f"\n{title}:")
    headers = [f"[{i}]" for i in range(len(matrix[0]))]
    table = [[f"[{i}]"] + row for i, row in enumerate(matrix)]
    print(tabulate(table, headers=[""] + headers, tablefmt="rounded_grid"))


def main():
    # Ввод размеров матрицы
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    # Ввод матрицы
    print("\nВвод матрицы символов:")
    matrix = input_symbol_matrix(rows, cols)
    if matrix is None:
        print("Ввод отменен")
        return

    # Выводим исходную матрицу
    print_matrix(matrix, "Исходная матрица")

    # Преобразуем матрицу
    transformed_matrix = transform_matrix(matrix)

    # Выводим преобразованную матрицу
    print_matrix(transformed_matrix, "Преобразованная матрица")


if __name__ == "__main__":
    main()
