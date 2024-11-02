"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №6 Подпрограмма 2a
"""

list_ = list(map(int, input("Введите список целых чисел: ").split()))

insert_index = int(input("Введите индекс удаления: "))

list_.pop(insert_index)

print(list_)
