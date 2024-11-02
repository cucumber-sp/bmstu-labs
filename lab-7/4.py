"""
Автор: Онищенко Андрей, группа ИУ7-12Б
Лабораторная работа №7 Подпрограмма 4
В каждой строке из введеного списка заменить все заглавные английские согласные на строчные
"""

list_ = list(input("Введите список строк: ").split())

for i in range(len(list_)):
    string_list = list(list_[i])
    for j in range(len(string_list)):
        letter = string_list[j]
        if letter.isupper() and letter in "QWRTPSDFGHJKLZXCVBNM":
            string_list[j] = letter.lower()
    list_[i] = ''.join(string_list)

print(list_)