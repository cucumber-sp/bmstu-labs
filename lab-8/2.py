"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 2
Переставить местами строки с наибольшим и наименьшим количеством
отрицательных элементов.
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
min_count = matrix_width + 1
max_index = -1
min_index = -1

for i in range(matrix_height):
    count = 0
    for j in range(matrix_width):
        if matrix[i][j] < 0:
            count += 1
    if count > max_count:
        max_count = count
        max_index = i
    if count < min_count:
        min_count = count
        min_index = i

(matrix[max_index], matrix[min_index]) = (matrix[min_index], matrix[max_index])

print("Матрица после перестановки")
print("\n".join(map(str, matrix)))
print("\n")
