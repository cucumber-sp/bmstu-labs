"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №7 Подпрограмма 1
Удалить из списка все положительные числа
"""

list_ = list(map(int, input("Введите список целых чисел: ").split()))

shift = 0
for i in range(len(list_)):
    if list_[i] <= 0:
        list_[i - shift] = list_[i]
    else:
        shift += 1

list_ = list_[: len(list_) - shift]

print(list_)
