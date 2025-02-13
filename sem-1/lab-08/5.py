"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 5
Найти максимальное значение в квадратной матрице над главной диагональю и
минимальное - под побочной диагональю.
"""

from os import system

matrix_size = int(input("Введите размер квадратной матрицы: "))

matrix = [["_"] * matrix_size for _ in range(matrix_size)]

system("clear")

for i in range(matrix_size):
    for j in range(matrix_size):
        system("clear")
        print("\n".join(map(str, matrix)))
        print("\n")
        elem = int(input("Введите элемент матрицы: "))
        matrix[i][j] = elem

system("clear")

print("Ваша матрица")
print("\n".join(map(str, matrix)))
print("\n")

max_val = -99999999999999999999999999999999999999
max_pos = (0, 0)

min_val = 99999999999999999999999999999999999
min_pos = (0, 0)

for column in range(matrix_size):
    for row in range(column):
        n = matrix[row][column]

        if n > max_val:
            max_val = n
            max_pos = (row, column)

for column in range(matrix_size):
    for row in range(matrix_size - column - 1, matrix_size):
        n = matrix[row][column]

        if n < min_val:
            min_val = n
            min_pos = (row, column)

print(f"Максимальное значение в квадратной матрице над главной диагональю: {max_val}")
print(f"Позиция: {max_pos[0] + 1} {max_pos[1] + 1}")
print("\n")
print(f"Минимальное значение в квадратной матрице под побочной диагональю: {min_val}")
print(f"Позиция: {min_pos[0] + 1} {min_pos[1] + 1}")
