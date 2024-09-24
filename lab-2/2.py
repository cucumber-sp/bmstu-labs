# Автор: Онищенко Андрей, группа ИУ7-12Б

# Ввод координат точки
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Функции, описывающие границы
y1 = 2 * x - 4               # Первая линия
y2 = (x / 4) - 0.5           # Вторая линия
y3 = -(x - 4) ** 2 + 4        # Парабола, для x от 4 до 5.75
y4 = -3/4 * x - 4            # Третья линия

# Проверка принадлежности точки области
if x >= 4 and x <= 5.75 and y <= y3:  # Для параболы
    print("Точка принадлежит области.")
elif x <= 5.75 and y >= y4 and y <= y1 and y >= y2:  # Для остальных частей
    print("Точка принадлежит области.")
else:
    print("Точка не принадлежит области.")
