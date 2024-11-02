"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 2b
"""


list_ = list(map(int, input("Введите список целых чисел: ").split()))

insert_index = int(input("Введите индекс удаления: "))

if not 0 <= insert_index < len(list_):
    print("Индекс должен быть в пределах длины списка")
else:
    for i in range(insert_index, len(list_) - 1):
        list_[i] = list_[i + 1]
    list_.pop()

    print(list_)
