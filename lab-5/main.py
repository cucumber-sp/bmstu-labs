"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №5 "График"
Цель: написать программу, которая для заданных по варианту функций выведет
таблицу значений этих функций на некотором отрезке и построит график одной из них.
Вариант 52. Функции: d1 и d2
Оператор цикла: for
"""

import math

# Начальные параметры
while True:
    try:
        b0 = float(input("Введите начальное значение: "))
        break
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите число.")

while True:
    try:
        h = float(input("Введите значение шага: "))
        if h > 0:
            break
        print("Шаг должен быть положительным числом.")
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите число.")

while True:
    try:
        bn = float(input("Введите конечное значение: "))
        if bn >= b0 + h:
            break
        print("Конечное значение должно быть больше начального значения.")
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите число.")

# Ввод количества засечек с защитой от некорректного ввода
while True:
    try:
        ticks = int(input("Введите количество засечек по горизонтальной оси "
                          "(от 4 до 8): "))
        if 4 <= ticks <= 8:
            break
        else:
            print("Пожалуйста, введите целое число в диапазоне от 4 до 8.")
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите целое число.")

# Количество шагов на интервале
steps = int((bn - b0) / h) + 1

# Таблица значений в рамке
print("┌" + "─" * 11 + "┬" + "─" * 18 + "┬" + "─" * 18 + "┐")
print(f"│{'b':^11}│{'d1(b)':^18}│{'d2(b)':^18}│")
print("├" + "─" * 11 + "┼" + "─" * 18 + "┼" + "─" * 18 + "┤")

# Инициализация переменных для подсчета смены знака
previous_sign_d2 = None
sign_change_count_d2 = 0

# Расчет и вывод значений функций
min_d2, max_d2 = float('inf'), float('-inf')
for i in range(steps):
    b = b0 + i * h
    if (b + 1) <= 0:
        d1 = float('nan')
    else:
        d1 = math.sqrt(b + 1) - (1 / (b + 1)) - 0.5
    d2 = b**3 + 9.3 * b**2 + 7.4 * b - 16.3

    # Вывод значений
    print(f"│{b:<11.4g}│{d1:<18.7g}│{d2:<18.7g}│")

    # Определение минимального и максимального значений функции d2
    if d2 < min_d2:
        min_d2 = d2
    if d2 > max_d2:
        max_d2 = d2

    # Проверка смены знака для d2
    current_sign_d2 = d2 >= 0
    if previous_sign_d2 is not None and current_sign_d2 != previous_sign_d2:
        sign_change_count_d2 += 1
    previous_sign_d2 = current_sign_d2

print("└" + "─" * 11 + "┴" + "─" * 18 + "┴" + "─" * 18 + "┘")

# Вывод результатов
print(f"\nКоличество смен знака функции d2: {sign_change_count_d2}")

# Определение масштаба и параметров графика
graph_width = 120  # Ширина графика в символах
interval_width = max_d2 - min_d2
scale = interval_width / graph_width  # Масштаб для графика

# Нахождение позиции оси Y = 0
y_axis_position = int((0 - min_d2) / scale) if min_d2 <= 0 <= max_d2 else None

# Построение линейки масштаба оси X
interval = interval_width / (ticks - 1)
scale_line = " " * 10 + " " * graph_width
current_value = min_d2

# Расчет и печать засечек на оси X
for _ in range(ticks):
    position = int((current_value - min_d2) / scale)  # Позиция засечки на графике
    formatted_val = f"{current_value:.2g}"
    scale_line = (scale_line[:position + 10 - len(formatted_val) // 2] +
                  formatted_val +
                  scale_line[position + 10 + len(formatted_val) // 2:])
    current_value += interval

# Заголовок графика
print(" " * 10 + "─" * (graph_width + 1))
print(" " * 10 + f"{'График функции d2(b)':^{graph_width}}\n")

# Вывод линейки масштаба сверху графика
print(scale_line)
print(" " * 10 + "─" * (graph_width + 1))

# Построение графика
for i in range(steps):
    b = b0 + i * h
    d2 = b**3 + 9.3 * b**2 + 7.4 * b - 16.3

    # Определение позиции звезды на графике
    star_position = int((d2 - min_d2) / scale)  # Позиция звезды относительно min_d2

    # Построение строки графика
    if y_axis_position is not None:
        # Вставка оси Y, если она присутствует в видимой области графика
        if star_position < y_axis_position:
            graph_line = (f"{b:<10.4g}│ " + " " * star_position + "*" +
                          " " * (y_axis_position - star_position - 1) + "│")
        elif star_position > y_axis_position:
            graph_line = (f"{b:<10.4g}│ " + " " * y_axis_position + "│" +
                          " " * (star_position - y_axis_position - 1) + "*")
        elif star_position == y_axis_position:
            graph_line = f"{b:<10.4g}│ " + " " * star_position + "*"
    else:
        graph_line = f"{b:<10.4g}│ " + " " * star_position + "*"

    print(graph_line)

# Нижняя граница графика
print(" " * 10 + "─" * (graph_width + 1))
