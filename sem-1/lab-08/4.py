"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Подпрограмма 4
Переставить местами столбцы с максимальной и минимальной суммой
элементов
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

max_sum = -99999999999999999999999999999999999
min_sum = 99999999999999999999999999999999999
max_index = -1
min_index = -1

for i in range(matrix_height):
    sum = 0
    for j in range(matrix_width):
        sum += matrix[i][j]
    if sum > max_sum:
        max_sum = sum
        max_index = i
    if sum < min_sum:
        min_sum = sum
        min_index = i

for i in range(matrix_height):
    (matrix[i][max_index], matrix[i][min_index]) = (
        matrix[i][min_index],
        matrix[i][max_index],
    )

print("Итоговая матрица")
print("\n".join(map(str, matrix)))
print("\n")
