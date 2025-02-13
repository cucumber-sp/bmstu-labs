"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 1a
"""

list_ = list(map(int, input("Введите список целых чисел: ").split()))

insert_index = int(input("Введите индекс вставки: "))
insert_value = int(input("Введите значение вставки: "))

list_.insert(insert_index, insert_value)
print(list_)
