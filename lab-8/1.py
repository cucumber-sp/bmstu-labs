"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 1
Найти строку, имеющую наименьшее количество чётных элементов.
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
for i in range(matrix_height):
    count = 0
    for j in range(matrix_width):
        if matrix[i][j] % 2 == 0:
            count += 1
    if count > max_count:
        max_count = count
        max_index = i

print(f"Строка с наименьшим количеством чётных элементов: {max_index + 1}")
