"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №8 Защита
Вычисление суммы ряда и обработка матрицы
"""

from math import factorial

# Ввод значения точности (epsilon)
while True:
    try:
        eps = float(input("Введите значение точности (epsilon > 0): "))
        if eps > 0:
            break
        print("Значение должно быть положительным!")
    except ValueError:
        print("Ошибка! Введите корректное число.")

# Ввод размеров матрицы
while True:
    try:
        rows = int(input("\nВведите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))
        if rows > 0 and cols > 0:
            break
        print("Размеры матрицы должны быть положительными!")
    except ValueError:
        print("Ошибка! Введите целое число.")

# Ввод элементов матрицы
print("\nВвод элементов матрицы:")
Y = []
for i in range(rows):
    row = []
    for j in range(cols):
        while True:
            try:
                elem = float(input("Введите элемент [{},{}]: ".format(i + 1, j + 1)))
                row.append(elem)
                break
            except ValueError:
                print("Ошибка! Введите число.")
    Y.append(row)

# Вычисление суммы ряда Z
n = 1
z = 0
term = float("inf")

while abs(term) >= eps:
    term = (n * (n + 1)) / factorial(2 * n - 1)
    z += term
    n += 1

# Создание пустого списка R для хранения элементов, меньших Z
R = []

# Обход матрицы по столбцам и поиск элементов, меньших Z
for j in range(cols):
    for i in range(rows):
        if Y[i][j] < z:
            R.append(Y[i][j])

# Вывод результатов
print("\nСумма ряда Z = {:.6f}".format(z))
print("\nМатрица Y:")
for row in Y:
    print(["{:7.2f}".format(x) for x in row])
print("\nМассив R (элементы, меньшие Z):")
print(["{}".format(round(x, 2)) for x in R])
