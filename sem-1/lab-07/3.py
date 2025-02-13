"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №7 Подпрограмма 3
Вывести самую длинную строку не содержащую английских гласных
"""

list_ = input("Введите список строк: ").split()

max_length = 0
max_string = ""
for string in list_:

    str_len = len(string)
    if str_len <= max_length:
        continue
    lowercase_string = string.lower()
    if all(letter not in lowercase_string for letter in "eyuioa"):
        max_length = str_len
        max_string = string

print(max_string)
