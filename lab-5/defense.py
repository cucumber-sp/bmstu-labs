"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №5 "График"
Цель: написать программу, которая для заданных по варианту функций выведет
таблицу значений этих функций на некотором отрезке и построит график одной из них.
Функция: d(b) = sin(1) / b
Оператор цикла: while
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
        print("Конечное значение должно быть больше начального значения + шаг.")
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите число.")

# Ввод количества засечек с защитой от некорректного ввода
while True:
    try:
        ticks = int(
            input("Введите количество засечек по горизонтальной оси " "(от 2 до 8): ")
        )
        if 2 <= ticks <= 8:
            break
        else:
            print("Пожалуйста, введите целое число в диапазоне от 2 до 8.")
    except ValueError:
        print("Некорректный ввод! Пожалуйста, введите целое число.")

# Таблица значений в рамке
print("┌" + "─" * 11 + "┬" + "─" * 18 + "┐")
print(f"│{'b':^11}│{'d(b)':^18}│")
print("├" + "─" * 11 + "┼" + "─" * 18 + "┤")


# Расчет и вывод значений функций
b = b0
min_d, max_d = float("inf"), float("-inf")

while b <= bn:
    if b == 0:
        d = float("nan")
    else:
        d = math.sin(1 / b)

    if d < min_d:
        min_d = d
    if d > max_d:
        max_d = d

    # Вывод значений
    print(f"│{b:<11.4g}│{d:<18.7g}│")

    b += h

print("└" + "─" * 11 + "┴" + "─" * 18 + "┘")

# Определение масштаба и параметров графика
graph_width = 120  # Ширина графика в символах
interval_width = max_d - min_d
scale = interval_width / graph_width  # Масштаб для графика

# Нахождение позиции оси Y = 0
y_axis_position = int((0 - min_d) / scale) if min_d <= 0 <= max_d else None

# Построение линейки масштаба оси X
interval = interval_width / (ticks - 1)
scale_line = " " * 10 + " " * graph_width
current_value = min_d

# Расчет и печать засечек на оси X
for _ in range(ticks):
    position = int((current_value - min_d) / scale)  # Позиция засечки на графике
    formatted_val = f"{current_value:.2g}"
    scale_line = (
        scale_line[: position + 10 - len(formatted_val) // 2]
        + formatted_val
        + scale_line[position + 10 + len(formatted_val) // 2 :]
    )
    current_value += interval

# Заголовок графика
print(" " * 10 + "─" * (graph_width + 1))
print(" " * 10 + f"{'График функции d(b)':^{graph_width}}\n")

# Вывод линейки масштаба сверху графика
print(scale_line)
print(" " * 10 + "─" * (graph_width + 1))

# Построение графика
b = b0
while b <= bn:

    if b == 0:
        d = float("nan")
    else:
        d = math.sin(1 / b)

    if math.isnan(d):
        if y_axis_position is not None:
            graph_line = f"{b:<10.4g}│ " + " " * y_axis_position + "│"
        else:
            graph_line = f"{b:<10.4g}│ " + " " * graph_width
    else:
        # Определение позиции звезды на графике
        star_position = int((d - min_d) / scale)  # Позиция звезды относительно min_d

        # Построение строки графика
        if y_axis_position is not None:
            # Вставка оси Y, если она присутствует в видимой области графика
            if star_position < y_axis_position:
                graph_line = (
                    f"{b:<10.4g}│ "
                    + " " * star_position
                    + "*"
                    + " " * (y_axis_position - star_position - 1)
                    + "│"
                )
            elif star_position > y_axis_position:
                graph_line = (
                    f"{b:<10.4g}│ "
                    + " " * y_axis_position
                    + "│"
                    + " " * (star_position - y_axis_position - 1)
                    + "*"
                )
            else:
                graph_line = f"{b:<10.4g}│ " + " " * star_position + "*"
        else:
            graph_line = f"{b:<10.4g}│ " + " " * star_position + "*"

    print(graph_line)

    b += h

# Нижняя граница графика
print(" " * 10 + "─" * (graph_width + 1))
