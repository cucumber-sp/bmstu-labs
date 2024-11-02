"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 5
"""
import math

while True:
    list_ = list(map(int, input("Введите список целых чисел: ").split()))
    if len(list_) > 0:
        break
    print("Длина должна быть более 0")


min_index = -1
min_value = math.inf

max_index = -1
max_value = -math.inf

for i, value in enumerate(list_):
    if value < min_value:
        min_index = i
        min_value = value
    if value > max_value:
        max_index = i
        max_value = value

(list_[min_index], list_[max_index]) = (list_[max_index], list_[min_index])

print(list_)
