"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 1b
"""

list_ = list(map(int, input("Введите список целых чисел: ").split()))

insert_index = int(input("Введите индекс вставки: "))
insert_value = int(input("Введите значение вставки: "))

if insert_index < 0 or insert_index > len(list_):
    print("Индекс должен быть в пределах длины списка")
else:
    list_ += [0]
    for i in range(len(list_) - 1, insert_index, -1):
        list_[i] = list_[i - 1]
    list_[insert_index] = insert_value

    print(list_)
