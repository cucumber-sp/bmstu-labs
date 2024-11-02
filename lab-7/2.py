"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №7 Подпрограмма 2
После каждого отрицательного элемента целочисленного списка, добавить его удвоенное значение
"""

list_ = list(map(int, input("Введите список целых чисел: ").split()))

orig_len = len(list_)

negative_count = 0
for item in list_:
    if item < 0:
        negative_count += 1

list_ += [0] * negative_count

for i in range(orig_len - 1, -1, -1):
    item = list_[i]
    if item >= 0:
        list_[i + negative_count] = item
    else:
        list_[i + negative_count] = item * 2
        list_[i + negative_count - 1] = item
        negative_count -= 1

print(list_)
