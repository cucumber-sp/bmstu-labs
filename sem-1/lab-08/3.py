"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 3
Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2
"""

from os import system

matrix_width = int(input("Введите число столбцов матрицы: "))
matrix_height = int(input("Введите число строк матрицы: "))

matrix = [["_"] * matrix_width for _ in range(matrix_height)]

system("clear")

for i in range(matrix_height):
    for j in range(matrix_width):
        system("clear")
        print("\n".join(map(str, matrix)))
        print("\n")
        elem = int(input("Введите элемент матрицы: "))
        matrix[i][j] = elem

system("clear")

print("Ваша матрица")
print("\n".join(map(str, matrix)))
print("\n")

max_count = -1
max_index = -1

for j in range(matrix_width):
    count = 0
    for i in range(matrix_height):
        n = matrix[i][j]
        if (n & (n - 1) == 0) and n != 0:
            count += 1
    if count > max_count:
        max_count = count
        max_index = j

print(f"Столбец с наибольшим количеством степеней 2: {max_index}")
