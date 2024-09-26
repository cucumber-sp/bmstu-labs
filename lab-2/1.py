# Автор: Онищенко Андрей, группа ИУ7-12Б

import math

# Ввод значения аргумента x
x = float(input("Введите значение x: "))

# Определение значения функции y в зависимости от x
if x <= -4:
    y = -math.log(x + 5)
elif -4 < x <= 4:
    y = math.sqrt(4 - (x + 2) ** 2)
elif x <= 4:
    y = math.sqrt(x)
else:
    y = -x + 6

# Вывод результата
print(f"Значение функции y при x = {x}: {y:.7g}")