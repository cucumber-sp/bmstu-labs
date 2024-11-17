"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 6
Выполнить транспонирование квадратной матрицы.
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

for column in range(matrix_size):
    for row in range(column):
        (matrix[column][row], matrix[row][column]) = (
            matrix[row][column],
            matrix[column][row],
        )

print("Транспонированная матрица")
print("\n".join(map(str, matrix)))
