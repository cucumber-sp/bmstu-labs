"""
Автор: Онищенко Андрей, группа ИУ7-12Б
"""

import math

x1 = float(input("Введите координату x точки 1: "))
y1 = float(input("Введите координату y точки 1: "))

x2 = float(input("Введите координату x точки 2: "))
y2 = float(input("Введите координату y точки 2: "))

if x1 == x2 and y1 == y2:
    raise ValueError("Точки совпадают")

x3 = float(input("Введите координату x точки 3: "))
y3 = float(input("Введите координату y точки 3: "))

x4 = float(input("Введите координату x точки 4: "))
y4 = float(input("Введите координату y точки 4: "))

if x3 == x4 and y3 == y4:
    raise ValueError("Точки совпадают")

# Расстояние от точки 1 до прямой заданной точками 3 и 4
d1_numerator = (y4 - y3) * x1 - (x4 - x3) * x1 + x4 * y3 - y3 * x4
d1_denominator = math.sqrt((y4 - y3) ** 2 + (x4 - x3) ** 2)
d1 = abs(d1_numerator) / d1_denominator

# Расстояние от точки 2 до прямой заданной точками 3 и 4
d2_numerator = (y4 - y3) * x2 - (x4 - x3) * x2 + x4 * y3 - y3 * x4
d2_denominator = math.sqrt((y4 - y3) ** 2 + (x4 - x3) ** 2)
d2 = abs(d2_numerator) / d2_denominator


# Проверка параллельности прямых через расстояния
# Используем сравнение чисел с плаващей точкой
if abs(d1 - d2) < 1e-9:
    print("Прямые параллельны")
else:
    print("Прямые не параллельны")
